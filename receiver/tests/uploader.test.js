import test from "node:test";
import assert from "node:assert/strict";
import { Outbox, MemoryStore, sessionKey } from "../src/outbox.js";
import { Uploader } from "../src/uploader.js";

const card = { token: "tok", patient: "Patient/p1", device: "Device/d1" };
const card2 = { token: "tok2", patient: "Patient/p2", device: "Device/d2" };
const rec = (n, key = sessionKey(card)) => ({ identifier: `id-${n}`, sessionKey: key, observation: { n } });
const resp = (status, body) => ({ status, ok: status < 300, text: async () => (typeof body === "string" ? body : JSON.stringify(body ?? {})) });

function setup(replies, c = card) {
  const store = new MemoryStore();
  const outbox = new Outbox(store);
  const calls = [];
  const sleeps = [];
  const statuses = [];
  const q = [...replies];
  const fetchFn = async (url, init) => {
    calls.push({ url, init, stored: store.all().length });
    const r = q.length > 1 ? q.shift() : q[0];
    if (r instanceof Error) throw r;
    return r;
  };
  const up = new Uploader({ outbox, fetchFn, card: c, sleep: async (ms) => { sleeps.push(ms); },
    onStatus: (s) => statuses.push(s) });
  return { store, outbox, calls, sleeps, statuses, up };
}

test("POST sends Authorization, If-None-Exist: identifier=<value>, fhir+json", async () => {
  const t = setup([resp(201)]);
  await t.outbox.add(rec(1));
  assert.equal(await t.up.step(), "sent");
  const { url, init } = t.calls[0];
  assert.equal(url, "/fhir-r4/v1/Observation");
  assert.equal(init.method, "POST");
  assert.equal(init.headers.Authorization, "Bearer tok");
  assert.equal(init.headers["If-None-Exist"], "identifier=id-1");
  assert.equal(init.headers["Content-Type"], "application/fhir+json");
  assert.deepEqual(JSON.parse(init.body), { n: 1 });
});

test("201 and 200 both delete the record", async () => {
  const t = setup([resp(201), resp(200)]);
  await t.outbox.add(rec(1));
  await t.outbox.add(rec(2));
  assert.equal(await t.up.step(), "sent");
  assert.equal(await t.up.step(), "sent");
  assert.equal(t.store.all().length, 0);
  assert.equal(await t.up.step(), "idle");
  assert.equal(t.statuses.at(-1).confirmed, 2);
});

test("record stays until the response arrives", async () => {
  const t = setup([resp(201)]);
  await t.outbox.add(rec(1));
  await t.up.step();
  assert.equal(t.calls[0].stored, 1);
  assert.equal(t.store.all().length, 0);
});

test("fetch throwing keeps the record and returns retry", async () => {
  const t = setup([new TypeError("net")]);
  await t.outbox.add(rec(1));
  assert.equal(await t.up.step(), "retry");
  assert.equal(t.store.all().length, 1);
  assert.equal(t.statuses.at(-1).state, "retry");
});

test("500 keeps the record and returns retry", async () => {
  const t = setup([resp(500, "boom")]);
  await t.outbox.add(rec(1));
  assert.equal(await t.up.step(), "retry");
  assert.equal(t.store.all().length, 1);
});

test("backoff goes 1,2,4,8,16,30,30 s, and resets after success", async () => {
  const t = setup([resp(503), resp(503), resp(503), resp(503), resp(503), resp(503), resp(503), resp(201), resp(503)]);
  await t.outbox.add(rec(1));
  await t.outbox.add(rec(2));
  for (let i = 0; i < 7; i++) assert.equal(await t.up.step(), "retry");
  assert.deepEqual(t.sleeps, [1000, 2000, 4000, 8000, 16000, 30000, 30000]);
  assert.equal(await t.up.step(), "sent");
  assert.equal(await t.up.step(), "retry");
  assert.equal(t.sleeps.at(-1), 1000);
});

test("401 and 403 return auth, keep the record, and stop sending until resume", async () => {
  for (const code of [401, 403]) {
    const t = setup([resp(code), resp(201)]);
    await t.outbox.add(rec(1));
    assert.equal(await t.up.step(), "auth");
    assert.equal(t.statuses.at(-1).state, "auth");
    assert.equal(await t.up.step(), "auth");
    assert.equal(t.calls.length, 1);
    assert.equal(t.store.all().length, 1);
    t.up.resume({ ...card, token: "new" });
    assert.equal(await t.up.step(), "sent");
    assert.equal(t.calls[1].init.headers.Authorization, "Bearer new");
    assert.equal(t.store.all().length, 0);
  }
});

test("400 marks rejected with OperationOutcome text and moves to next", async () => {
  const oo = { resourceType: "OperationOutcome", issue: [{ details: { text: "bad data" } }, { details: { text: "second" } }] };
  const t = setup([resp(400, oo), resp(201)]);
  await t.outbox.add(rec(1));
  await t.outbox.add(rec(2));
  assert.equal(await t.up.step(), "rejected");
  assert.equal(t.store.all().length, 2);
  assert.equal(t.statuses.at(-1).lastRejectedReason, "bad data");
  assert.equal(await t.up.step(), "sent");
  assert.equal(t.calls[1].init.headers["If-None-Exist"], "identifier=id-2");
  assert.equal(t.store.all().length, 1);
  assert.equal(t.statuses.at(-1).confirmed, 1);
});

test("400 with a non-JSON body gives reason 'HTTP 400'", async () => {
  const t = setup([resp(400, "<html>")]);
  await t.outbox.add(rec(1));
  assert.equal(await t.up.step(), "rejected");
  assert.equal(t.statuses.at(-1).lastRejectedReason, "HTTP 400");
  assert.equal(t.store.all()[0].reason, "HTTP 400");
});

test("chunks are sent oldest first, one at a time", async () => {
  const t = setup([resp(201)]);
  for (const n of [1, 2, 3]) await t.outbox.add(rec(n));
  await t.up.step(); await t.up.step(); await t.up.step();
  assert.deepEqual(t.calls.map((c) => c.init.headers["If-None-Exist"]),
    ["identifier=id-1", "identifier=id-2", "identifier=id-3"]);
});

test("other session's chunks are skipped and counted", async () => {
  const t = setup([resp(201)]);
  await t.outbox.add(rec(1, sessionKey(card2)));
  assert.equal(await t.up.step(), "idle");
  assert.equal(t.calls.length, 0);
  assert.deepEqual(await t.outbox.counts(sessionKey(card)), { pending: 0, rejected: 0, otherSession: 1 });
});

test("resume with their card sends them", async () => {
  const t = setup([resp(201)]);
  await t.outbox.add(rec(1, sessionKey(card2)));
  t.up.resume(card2);
  assert.equal(await t.up.step(), "sent");
  assert.equal(t.calls[0].init.headers.Authorization, "Bearer tok2");
  assert.equal(t.store.all().length, 0);
});

test("408 and 429 are retried, not rejected", async () => {
  for (const code of [408, 429]) {
    const t = setup([resp(code)]);
    await t.outbox.add(rec(1));
    assert.equal(await t.up.step(), "retry");
    assert.equal(t.store.all()[0].rejected, false);
    assert.equal(t.statuses.at(-1).state, "retry");
  }
});

test("a resume during an in-flight step does not mix records and tokens", async () => {
  const store = new MemoryStore();
  const outbox = new Outbox(store);
  await outbox.add(rec(1));
  let release;
  const gate = new Promise((r) => { release = r; });
  const seen = [];
  const fetchFn = async (url, init) => { seen.push(init.headers.Authorization); await gate; return resp(201); };
  const up = new Uploader({ outbox, fetchFn, card, sleep: async () => {}, onStatus: () => {} });
  const p = up.step();
  await new Promise((r) => setTimeout(r, 5));
  up.resume(card2);
  release();
  await p;
  assert.deepEqual(seen, ["Bearer tok"]);
  assert.equal(store.all().length, 0);
});

test("a storage failure in the loop is reported as error and the loop keeps going", async () => {
  const t = setup([resp(201)]);
  await t.outbox.add(rec(1));
  const orig = t.outbox.nextFor.bind(t.outbox);
  let n = 0;
  t.outbox.nextFor = async (k) => { if (n++ === 0) throw new Error("db gone"); return orig(k); };
  let slept = 0;
  t.up.sleep = async () => { if (++slept > 20) t.up.stop(); await new Promise((r) => setTimeout(r, 1)); };
  t.up.start();
  for (let i = 0; i < 100 && t.store.all().length > 0; i++) await new Promise((r) => setTimeout(r, 5));
  t.up.stop();
  assert.ok(t.statuses.some((s) => s.state === "error"));
  assert.equal(t.store.all().length, 0);
});

test("a throwing onStatus does not end the loop", async () => {
  const t = setup([resp(201)]);
  await t.outbox.add(rec(1));
  let first = true;
  t.up.onStatus = (s) => { if (first) { first = false; throw new Error("ui"); } t.statuses.push(s); };
  t.up.sleep = async () => { await new Promise((r) => setTimeout(r, 1)); };
  t.up.start();
  for (let i = 0; i < 100 && t.store.all().length > 0; i++) await new Promise((r) => setTimeout(r, 5));
  t.up.stop();
  assert.equal(t.store.all().length, 0);
});

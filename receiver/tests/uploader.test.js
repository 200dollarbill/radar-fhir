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

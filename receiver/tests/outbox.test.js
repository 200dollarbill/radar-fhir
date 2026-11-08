import test from "node:test";
import assert from "node:assert/strict";
import { Outbox, MemoryStore, sessionKey } from "../src/outbox.js";

const card = { patient: "Patient/p1", device: "Device/d1" };
const rec = (n, key = sessionKey(card)) => ({ identifier: `id-${n}`, sessionKey: key, observation: { n } });

test("sessionKey joins patient and device", () => {
  assert.equal(sessionKey(card), "Patient/p1|Device/d1");
});

test("nextFor returns the oldest pending record of that session", async () => {
  const ob = new Outbox(new MemoryStore());
  await ob.add(rec(1, "other"));
  await ob.add(rec(2));
  await ob.add(rec(3));
  assert.equal((await ob.nextFor(sessionKey(card))).identifier, "id-2");
  assert.equal(await ob.nextFor("none"), null);
});

test("records survive into a new Outbox on the same store", async () => {
  const store = new MemoryStore();
  await new Outbox(store).add(rec(1));
  const next = await new Outbox(store).nextFor(sessionKey(card));
  assert.equal(next.identifier, "id-1");
});

test("markRejected keeps the record, excluded from nextFor, counted as rejected", async () => {
  const store = new MemoryStore();
  const ob = new Outbox(store);
  const a = await ob.add(rec(1));
  await ob.add(rec(2));
  await ob.add(rec(3, "other"));
  await ob.markRejected(a, "bad");
  assert.equal((await ob.nextFor(sessionKey(card))).identifier, "id-2");
  assert.equal(store.all().length, 3);
  assert.deepEqual(await ob.counts(sessionKey(card)), { pending: 1, rejected: 1, otherSession: 1 });
});

test("remove deletes the record", async () => {
  const store = new MemoryStore();
  const ob = new Outbox(store);
  const a = await ob.add(rec(1));
  await ob.remove(a);
  assert.equal(store.all().length, 0);
});

test("add rejects with QuotaExceededError when the store throws it", async () => {
  const store = new MemoryStore();
  store.put = () => { throw new DOMException("full", "QuotaExceededError"); };
  await assert.rejects(new Outbox(store).add(rec(1)), (e) => e.name === "QuotaExceededError");
});

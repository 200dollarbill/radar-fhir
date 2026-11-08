import test from "node:test";
import assert from "node:assert/strict";
import { Capture } from "../src/capture.js";
import { Outbox, MemoryStore, sessionKey } from "../src/outbox.js";
import { formatLine } from "../src/simulator.js";

const card = {
  token: "t", patient: "Patient/p1", encounter: "Encounter/e1",
  device: "Device/d1", org: "org1", label: "L",
};

async function* gen(items, thenThrow) {
  for (const x of items) yield x;
  if (thenThrow) throw thenThrow;
}
const lines = (idxs) => idxs.map((i) => formatLine(i, 100, {}));

function make(extra = {}) {
  const store = new MemoryStore();
  const outbox = new Outbox(store);
  const samples = [];
  let n = 0;
  const cap = new Capture({
    outbox, sessionKey: sessionKey(card), card, source: "SIMULATED",
    onSample: (s) => samples.push(s), newId: () => "cap-" + ++n, ...extra,
  });
  return { store, outbox, cap, samples };
}

test("lines reach onSample and the outbox", async () => {
  const { cap, samples, store } = make();
  await cap.run(gen(lines([0, 1, 2])));
  assert.equal(samples.length, 3);
  assert.equal(store.all().length, 1);
});

test("every chunk is in the outbox before run resolves", async () => {
  const slow = new Outbox(new MemoryStore());
  const orig = slow.add.bind(slow);
  slow.add = async (r) => { await new Promise((r2) => setTimeout(r2, 5)); return orig(r); };
  const { cap } = make({ outbox: slow });
  await cap.run(gen(lines(Array.from({ length: 2500 }, (_, i) => i))));
  const rows = slow.store.all();
  assert.equal(rows.length, 3);
  assert.deepEqual(rows.map((r) => r.identifier.split("-").pop()), ["0", "1", "2"]);
});

test("ending the iterable flushes the partial chunk and returns ended", async () => {
  const { cap, store } = make();
  assert.equal(await cap.run(gen(lines([0, 1]))), "ended");
  assert.equal(store.all().length, 1);
});

test("the iterable throwing flushes and returns disconnected", async () => {
  const { cap, store } = make();
  assert.equal(await cap.run(gen(lines([0, 1]), new Error("unplugged"))), "disconnected");
  assert.equal(store.all().length, 1);
});

test("store quota error stops reading and returns quota", async () => {
  const outbox = new Outbox(new MemoryStore());
  outbox.add = async () => { throw new DOMException("full", "QuotaExceededError"); };
  let consumed = 0;
  async function* src() { for (let i = 0; i < 5000; i++) { consumed++; yield* lines([i]); } }
  const { cap } = make({ outbox });
  assert.equal(await cap.run(src()), "quota");
  assert.ok(consumed < 5000);
});

test("each run has a new captureId", async () => {
  const { cap, store } = make();
  await cap.run(gen(lines([0])));
  await cap.run(gen(lines([0])));
  const ids = store.all().map((r) => r.identifier);
  assert.equal(ids.length, 2);
  assert.notEqual(ids[0], ids[1]);
  assert.match(ids[0], /^cap-1-/);
});

test("stats count samples, gaps and rejected lines", async () => {
  const seen = [];
  const { cap } = make({ onStatus: (s) => seen.push({ ...s }) });
  await cap.run(gen([...lines([0, 1]), "{bad", "banner text", ...lines([4])]));
  assert.deepEqual(cap.stats, { samples: 3, gaps: 2, rejected: 1 });
  assert.deepEqual(seen.at(-1), cap.stats);
});

test("rejected line followed by the next index produces an E gap", async () => {
  const { cap, store } = make();
  await cap.run(gen([...lines([0]), '{"bad":1}', ...lines([2])]));
  const obs = store.all()[0].observation;
  assert.equal(obs.component[0].valueSampledData.data.split(" ")[1], "E");
  assert.match(obs.note[0].text, /"rejected_lines":1/);
});

test("a throwing onSample rejects run() instead of reporting disconnected", async () => {
  const boom = new Error("ui bug");
  const { cap, store } = make({ onSample: () => { throw boom; } });
  await assert.rejects(cap.run(gen(lines([0, 1]))), (e) => e === boom);
  assert.equal(store.all().length, 1);
});

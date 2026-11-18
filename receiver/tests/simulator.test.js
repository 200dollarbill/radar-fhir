import test from "node:test";
import assert from "node:assert/strict";
import { parseLine } from "../src/jsonlines.js";
import { simulatorLines } from "../src/simulator.js";

// Fake clock: sleep advances time by `step` ms; stops after `ticks` sleeps.
async function collect({ fs = 100, step = 1000, ticks = 1 } = {}) {
  let t = 1_000_000;
  let n = 0;
  const ac = new AbortController();
  const sleep = async () => { t += step; if (++n >= ticks) ac.abort(); };
  const lines = [];
  for await (const l of simulatorLines({ fs, now: () => t, sleep, signal: ac.signal })) lines.push(l);
  return lines;
}

test("each line parses to a sample with consecutive sampleIdx", async () => {
  const lines = await collect({ ticks: 3 });
  assert.ok(lines.length > 0);
  lines.forEach((l, i) => {
    const r = parseLine(l);
    assert.equal(r.kind, "sample");
    assert.equal(r.sample.sampleIdx, i);
    assert.equal(r.sample.fs, 100);
  });
});

test("I and Q stay inside 0 to 3.3 V", async () => {
  for (const l of await collect({ ticks: 10 })) {
    const { I, Q } = parseLine(l).sample;
    assert.ok(I >= 0 && I <= 3.3 && Q >= 0 && Q <= 3.3);
  }
});

test("emits elapsed×fs lines after a long sleep, catching up", async () => {
  const lines = await collect({ fs: 100, step: 2500, ticks: 2 });
  assert.equal(lines.length, 250);
});

test("an aborted signal ends the generator", async () => {
  const ac = new AbortController();
  ac.abort();
  const lines = [];
  for await (const l of simulatorLines({ signal: ac.signal, sleep: async () => {} })) lines.push(l);
  assert.deepEqual(lines, []);
});

test("abort during the default sleep ends the generator promptly", async () => {
  const ac = new AbortController();
  const gen = simulatorLines({ signal: ac.signal });
  const p = (async () => { for await (const _ of gen) { /* drain */ } })();
  setTimeout(() => ac.abort(), 50);
  await p;
});

test("virtualBoard makes a SIM id and key once and keeps them", async () => {
  const { virtualBoard } = await import("../src/simulator.js");
  const m = new Map();
  const storage = { getItem: (k) => m.get(k) ?? null, setItem: (k, v) => m.set(k, v) };
  const a = virtualBoard(storage);
  assert.match(a.id, /^SIM-[0-9A-F]{8}$/);
  assert.match(a.key, /^[0-9a-f]{64}$/);
  assert.deepEqual(virtualBoard(storage), a);
  // no storage at all still gives a usable board for this page load
  assert.match(virtualBoard(null).id, /^SIM-/);
});

test("the simulator answers BOARD? between samples", async () => {
  const { simulatorSource } = await import("../src/simulator.js");
  const { parseBoardLine } = await import("../src/board.js");
  let t = 0;
  const board = { id: "SIM-0A1B2C3D", key: "ab".repeat(32) };
  const ac = new AbortController();
  const src = simulatorSource(board, { now: () => t, sleep: async () => { t += 20; }, signal: ac.signal });
  const out = [];
  for await (const line of src.lines) {
    out.push(line);
    if (out.length === 3) await src.send("BOARD?\n");
    if (out.length > 12) break;
  }
  const replies = out.map(parseBoardLine).filter(Boolean);
  assert.equal(replies.length, 1);
  assert.deepEqual({ id: replies[0].id, key: replies[0].key }, board);
  assert.ok(out.filter((l) => l.startsWith("{")).length >= 10);
});

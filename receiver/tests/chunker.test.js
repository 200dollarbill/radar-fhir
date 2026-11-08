import test from "node:test";
import assert from "node:assert/strict";
import { Chunker } from "../src/chunker.js";

const s = (idx, o = {}) => ({
  sampleIdx: idx, fs: 100, missed: 0,
  I: 1, Q: 2, ax: 0, ay: 0, az: 1, gx: 0, gy: 0, gz: 0, ...o,
});
function make(opts = {}) {
  const chunks = [];
  const c = new Chunker({ now: () => 1_000_000, onChunk: (k) => chunks.push(k), ...opts });
  return { c, chunks };
}
const feed = (c, from, n) => { for (let i = 0; i < n; i++) c.addSample(s(from + i)); };

test("1000 samples emit one chunk; chunk 2 gets index 1", () => {
  const { c, chunks } = make();
  feed(c, 0, 1000);
  assert.equal(chunks.length, 1);
  assert.equal(chunks[0].chunkIndex, 0);
  assert.equal(chunks[0].segment, 0);
  assert.equal(chunks[0].channels.I.length, 1000);
  feed(c, 1000, 1000);
  assert.equal(chunks.length, 2);
  assert.equal(chunks[1].chunkIndex, 1);
});

test("gap of 3 fills 3 E in every channel and counts gapSamples 3", () => {
  const { c, chunks } = make();
  feed(c, 0, 2);
  c.addSample(s(5));
  c.flush();
  const k = chunks[0];
  assert.deepEqual(k.channels.I, [1, 1, "E", "E", "E", 1]);
  for (const ch of Object.values(k.channels)) assert.equal(ch.length, 6);
  assert.deepEqual(k.channels.gz, [0, 0, "E", "E", "E", 0]);
  assert.equal(k.gapSamples, 3);
});

test("gap crossing a chunk boundary: both chunks 1000 long, none lost", () => {
  const { c, chunks } = make();
  feed(c, 0, 998);
  c.addSample(s(1003)); // gap of 5: 2 fill fill the chunk, 3 start the next
  feed(c, 1004, 996);
  assert.equal(chunks.length, 2);
  assert.equal(chunks[0].channels.I.length, 1000);
  assert.equal(chunks[1].channels.I.length, 1000);
  assert.equal(chunks[0].gapSamples, 2);
  assert.equal(chunks[1].gapSamples, 3);
  assert.deepEqual(chunks[1].channels.I.slice(0, 4), ["E", "E", "E", 1]);
  assert.equal(chunks[0].segment, chunks[1].segment);
});

test("gap of 999 fills; gap of 1000 starts a new segment", () => {
  const a = make();
  a.c.addSample(s(0));
  a.c.addSample(s(1000)); // gap 999
  assert.equal(a.chunks.length, 1); // 1 + 999 fill = 1000 -> emitted
  a.c.flush();
  assert.equal(a.chunks.length, 2);
  assert.equal(a.chunks[0].gapSamples, 999);
  assert.equal(a.chunks[1].segment, 0);

  const b = make();
  b.c.addSample(s(0));
  b.c.addSample(s(1001)); // gap 1000
  b.c.flush();
  assert.equal(b.chunks.length, 2);
  assert.equal(b.chunks[0].channels.I.length, 1);
  assert.equal(b.chunks[1].segment, 1);
  assert.equal(b.chunks[1].chunkIndex, 0);
  assert.equal(b.chunks[1].gapSamples, 0);
});

test("sample_idx going backwards flushes and starts segment+1, chunkIndex 0", () => {
  const { c, chunks } = make();
  feed(c, 10, 5);
  feed(c, 0, 3);
  c.flush();
  assert.equal(chunks.length, 2);
  assert.equal(chunks[0].channels.I.length, 5);
  assert.equal(chunks[1].segment, 1);
  assert.equal(chunks[1].chunkIndex, 0);
  assert.equal(chunks[1].channels.I.length, 3);
});

test("repeated sample_idx starts a new segment", () => {
  const { c, chunks } = make();
  c.addSample(s(4));
  c.addSample(s(4));
  c.flush();
  assert.equal(chunks.length, 2);
  assert.equal(chunks[1].segment, 1);
});

test("fs change flushes and starts a new segment", () => {
  const { c, chunks } = make();
  feed(c, 0, 3);
  c.addSample(s(3, { fs: 250 }));
  c.flush();
  assert.equal(chunks.length, 2);
  assert.equal(chunks[0].fs, 100);
  assert.equal(chunks[1].fs, 250);
  assert.equal(chunks[1].segment, 1);
  assert.equal(chunks[1].gapSamples, 0);
});

test("first sample at any index causes no gap", () => {
  const { c, chunks } = make();
  c.addSample(s(123456));
  c.flush();
  assert.equal(chunks[0].channels.I.length, 1);
  assert.equal(chunks[0].gapSamples, 0);
  assert.equal(chunks[0].segment, 0);
});

test("flush emits a partial chunk; flush with nothing emits nothing", () => {
  const { c, chunks } = make();
  c.flush();
  assert.equal(chunks.length, 0);
  feed(c, 0, 7);
  c.flush();
  assert.equal(chunks.length, 1);
  assert.equal(chunks[0].channels.Q.length, 7);
  c.flush();
  assert.equal(chunks.length, 1);
});

test("noteRejected counts on the next emitted chunk, then resets", () => {
  const { c, chunks } = make();
  c.noteRejected(); c.noteRejected();
  feed(c, 0, 2);
  c.flush();
  feed(c, 2, 2);
  c.flush();
  assert.equal(chunks[0].rejectedLines, 2);
  assert.equal(chunks[1].rejectedLines, 0);
});

test("rejected count survives an empty flush", () => {
  const { c, chunks } = make();
  c.noteRejected();
  c.flush();
  assert.equal(chunks.length, 0);
  feed(c, 0, 1);
  c.flush();
  assert.equal(chunks[0].rejectedLines, 1);
});

test("all channels have equal length in every emitted chunk", () => {
  const { c, chunks } = make({ chunkSize: 10 });
  feed(c, 0, 7);
  c.addSample(s(30));
  feed(c, 31, 5);
  c.flush();
  assert.ok(chunks.length >= 3);
  for (const k of chunks) {
    const lens = new Set(Object.values(k.channels).map((a) => a.length));
    assert.equal(lens.size, 1);
    assert.deepEqual(Object.keys(k.channels), ["I", "Q", "ax", "ay", "az", "gx", "gy", "gz"]);
  }
});

test("deviceMissed is the latest sample's missed", () => {
  const { c, chunks } = make();
  c.addSample(s(0, { missed: 2 }));
  c.addSample(s(1, { missed: 5 }));
  c.flush();
  assert.equal(chunks[0].deviceMissed, 5);
});

test("startTimeMs back-dates by leading gap entries", () => {
  const { c, chunks } = make({ chunkSize: 4 });
  feed(c, 0, 3);
  c.addSample(s(8)); // last idx 2, so gap 5
  c.flush();
  // chunk 2 begins with 4 fill entries, 1 fill + real? see below
  // chunk 1: samples 0,1,2 + fill -> full. chunk 2: 4 fill -> full. chunk 3: real.
  assert.equal(chunks.length, 3);
  assert.equal(chunks[0].startTimeMs, 1_000_000);
  // chunk 2 first entry is a fill with 4 fill entries remaining (incl. itself): 4 * 10 ms
  // gap = 8 - 2 - 1 = 5; 1 went to chunk 1; 4 remain.
  assert.equal(chunks[1].startTimeMs, 1_000_000 - 40);
  assert.equal(chunks[2].startTimeMs, 1_000_000);
});

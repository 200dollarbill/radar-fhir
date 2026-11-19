import test from "node:test";
import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { parseLine, LineSplitter, FIELDS } from "../src/jsonlines.js";

const good = {
  epoch_id: 1, sample_idx: 5, t_host_unix: 1.5, fs: 100, crc_ok: true, missed: 0,
  I: 1.65, Q: 1.7, ax: 0, ay: 0, az: 1, gx: 0, gy: 0, gz: 0,
};
const line = (o) => JSON.stringify(o);
const without = (k) => { const o = { ...good }; delete o[k]; return o; };

test("valid firmware line gives a sample", () => {
  const r = parseLine(line(good));
  assert.equal(r.kind, "sample");
  assert.deepEqual(r.sample, {
    sampleIdx: 5, fs: 100, missed: 0, I: 1.65, Q: 1.7,
    ax: 0, ay: 0, az: 1, gx: 0, gy: 0, gz: 0,
  });
});

test("READY banner and ingest text are ignored, not rejected", () => {
  assert.equal(parseLine("READY radar_json i_pin=1 q_pin=2 fs=100 imu_ok=true").kind, "ignored");
  assert.equal(parseLine("ingest POST -> 200").kind, "ignored");
});

test("blank line is ignored", () => {
  assert.equal(parseLine("").kind, "ignored");
  assert.equal(parseLine("  \r").kind, "ignored");
});

test("broken {json is rejected", () => {
  assert.equal(parseLine('{"epoch_id":1,').kind, "rejected");
});

test("missing field is rejected, naming it", () => {
  const r = parseLine(line(without("gz")));
  assert.equal(r.kind, "rejected");
  assert.match(r.reason, /gz/);
});

test("non-integer sample_idx or fs is rejected", () => {
  assert.equal(parseLine(line({ ...good, sample_idx: 1.5 })).kind, "rejected");
  assert.equal(parseLine(line({ ...good, fs: "100" })).kind, "rejected");
});

test("negative sample_idx and fs of 0 are rejected", () => {
  assert.equal(parseLine(line({ ...good, sample_idx: -1 })).kind, "rejected");
  assert.equal(parseLine(line({ ...good, fs: 0 })).kind, "rejected");
});

test("string I value is rejected", () => {
  assert.equal(parseLine(line({ ...good, I: "1.65" })).kind, "rejected");
});

test("crc_ok:false is rejected with reason crc_ok", () => {
  const r = parseLine(line({ ...good, crc_ok: false }));
  assert.equal(r.kind, "rejected");
  assert.match(r.reason, /crc_ok/);
});

test("JSON array starting [ is ignored", () => {
  assert.equal(parseLine("[1,2,3]").kind, "ignored");
});

test("FIELDS match radar_json.ino", () => {
  const ino = readFileSync("arduino/radar_json/radar_json.ino", "utf8");
  const keys = [...ino.matchAll(/\\"(\w+)\\":/g)].map((m) => m[1]);
  assert.deepEqual(keys, FIELDS);
});

test("a line split across pushes comes out once, whole", () => {
  const s = new LineSplitter();
  assert.deepEqual(s.push('{"a":'), []);
  assert.deepEqual(s.push("1}\n"), ['{"a":1}']);
});

test("two lines in one push come out in order", () => {
  assert.deepEqual(new LineSplitter().push("a\nb\n"), ["a", "b"]);
});

test("CRLF is stripped", () => {
  assert.deepEqual(new LineSplitter().push("a\r\nb\r\n"), ["a", "b"]);
});

test("a partial line stays buffered", () => {
  const s = new LineSplitter();
  assert.deepEqual(s.push("a\npar"), ["a"]);
  assert.deepEqual(s.push("t\n"), ["part"]);
});

test("a mid-line start parses as ignored", () => {
  const [l] = new LineSplitter().push('":1.2,"Q":3}\n');
  assert.equal(parseLine(l).kind, "ignored");
});

test("over 4096 chars without newline is emitted and the buffer resets", () => {
  const s = new LineSplitter();
  const out = s.push("x".repeat(4097));
  assert.equal(out.length, 1);
  assert.equal(out[0].length, 4097);
  assert.deepEqual(s.push("y\n"), ["y"]);
});

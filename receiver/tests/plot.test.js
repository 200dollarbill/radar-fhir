import test from "node:test";
import assert from "node:assert/strict";
import { Trace } from "../src/plot.js";

test("capacity keeps only the last 1000 points", () => {
  const t = new Trace();
  for (let n = 0; n < 1500; n++) t.push(n, -n);
  const p = t.points(1000, 100);
  assert.equal(p.i.length, 1000);
  assert.equal(p.q.length, 1000);
  // oldest kept sample is 500, so it is the lowest I: it sits at the bottom (largest y)
  assert.ok(p.i[0][1] > p.i[999][1]);
});

test("a constant signal gives finite y values", () => {
  const t = new Trace();
  for (let n = 0; n < 50; n++) t.push(1.65, 1.65);
  const p = t.points(200, 100);
  for (const [x, y] of [...p.i, ...p.q]) {
    assert.ok(Number.isFinite(x) && Number.isFinite(y));
  }
});

test("points stay inside width and height", () => {
  const t = new Trace(100);
  for (let n = 0; n < 300; n++) t.push(Math.sin(n / 5) * 3, Math.cos(n / 7) * 0.001);
  const p = t.points(320, 120);
  for (const [x, y] of [...p.i, ...p.q]) {
    assert.ok(x >= 0 && x <= 320 && y >= 0 && y <= 120, `${x},${y}`);
  }
});

test("an empty trace has no points", () => {
  assert.deepEqual(new Trace().points(100, 50), { i: [], q: [] });
});

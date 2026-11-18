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

test("seriesPoints maps +3 SD to the top and -3 SD to the bottom, clamped", async () => {
  const { seriesPoints } = await import("../src/plot.js");
  const p = seriesPoints([3, 0, -3, 10, -10], 400, 100);
  assert.deepEqual(p.map(([, y]) => y), [0, 50, 100, 0, 100]);
  assert.equal(p[0][0], 0);
  assert.equal(p[4][0], 400);
  assert.deepEqual(seriesPoints([], 400, 100), []);
});

test("scatterTransform keeps equal aspect and stays inside the canvas", async () => {
  const { scatterTransform } = await import("../src/plot.js");
  const I = [1.0, 1.002, 1.002, 1.0];
  const Q = [2.0, 2.0, 2.002, 2.002];
  const t = scatterTransform(I, Q, 300, 200);
  const pts = I.map((v, k) => t.map(v, Q[k]));
  const dx = Math.abs(pts[1][0] - pts[0][0]);
  const dy = Math.abs(pts[2][1] - pts[1][1]);
  assert.ok(Math.abs(dx - dy) < 1e-9 && dx > 0);
  for (const [x, y] of pts) assert.ok(x >= 0 && x <= 300 && y >= 0 && y <= 200);
  // Q grows upward on screen
  assert.ok(pts[2][1] < pts[1][1]);
});

test("scatterTransform ignores NaN and survives a single point", async () => {
  const { scatterTransform } = await import("../src/plot.js");
  const t = scatterTransform([1, NaN, 1], [2, NaN, 2], 100, 100);
  const [x, y] = t.map(1, 2);
  assert.ok(Number.isFinite(x) && Number.isFinite(y));
});

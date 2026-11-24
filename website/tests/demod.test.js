import test from "node:test";
import assert from "node:assert/strict";
import { METHODS, fitCircle, demodulate } from "../src/dsp/demod.js";

function corr(a, b) {
  const n = a.length;
  const ma = a.reduce((s, v) => s + v, 0) / n;
  const mb = b.reduce((s, v) => s + v, 0) / n;
  let sab = 0, saa = 0, sbb = 0;
  for (let k = 0; k < n; k++) {
    sab += (a[k] - ma) * (b[k] - mb);
    saa += (a[k] - ma) ** 2;
    sbb += (b[k] - mb) ** 2;
  }
  return sab / Math.sqrt(saa * sbb);
}

// Deterministic pseudo-noise so tests never flake.
function noise(seed) {
  let s = seed;
  return () => {
    s = (s * 1664525 + 1013904223) % 4294967296;
    return s / 4294967296 - 0.5;
  };
}

function arc(n, spanRad, { r = 0.05, xc = 1.6, yc = 1.5, sd = 0, seed = 1 } = {}) {
  const rnd = noise(seed);
  const phase = Array.from({ length: n }, (_, k) => (spanRad / 2) * Math.sin((2 * Math.PI * k) / n));
  const I = phase.map((p) => xc + r * Math.cos(p) + sd * rnd());
  const Q = phase.map((p) => yc + r * Math.sin(p) + sd * rnd());
  return { phase, I, Q };
}

test("the method list is fixed", () => {
  assert.deepEqual(METHODS, ["single", "pca", "arctan-mean", "arctan-fit", "dacm-fit", "hybrid"]);
});

test("fitCircle recovers centre, radius and span of a clean arc", () => {
  const { I, Q } = arc(1000, 2);
  const c = fitCircle(I, Q);
  assert.ok(Math.abs(c.xc - 1.6) < 1e-6 && Math.abs(c.yc - 1.5) < 1e-6);
  assert.ok(Math.abs(c.r - 0.05) < 1e-6);
  assert.ok(Math.abs(c.spanDeg - 114.59) < 0.1, `span ${c.spanDeg}`);
  assert.ok(c.residualSd < 1e-9);
});

test("arctan-fit recovers the phase of an arc", () => {
  const { phase, I, Q } = arc(1000, 2);
  assert.ok(corr(demodulate("arctan-fit", I, Q).x, phase) > 0.999);
});

test("pca recovers the coordinate along a straight-line cloud", () => {
  const t = Array.from({ length: 500 }, (_, k) => Math.sin(k / 20));
  const I = t.map((v) => 1.5 + 0.003 * v);
  const Q = t.map((v) => 1.5 - 0.004 * v);
  assert.ok(Math.abs(corr(demodulate("pca", I, Q).x, t)) > 0.999);
});

test("hybrid uses pca on a short noisy arc and arctan-fit on a long arc", () => {
  const short = arc(1000, (3 * Math.PI) / 180, { sd: 0.0005 });
  assert.equal(demodulate("hybrid", short.I, short.Q).used, "pca");
  const long = arc(1000, 2, { sd: 0.0005 });
  assert.equal(demodulate("hybrid", long.I, long.Q).used, "arctan-fit");
});

test("a line-like cloud like the RABITS capture makes hybrid choose pca", () => {
  const rnd = noise(7);
  const t = Array.from({ length: 1000 }, (_, k) => Math.sin(k / 30) + 0.3 * rnd());
  const I = t.map((v) => 1.548 - 0.004 * v + 0.0008 * rnd());
  const Q = t.map((v) => 1.549 + 0.005 * v + 0.0008 * rnd());
  assert.equal(demodulate("hybrid", I, Q).used, "pca");
});

test("constant input gives finite zeros for every method", () => {
  const I = new Array(300).fill(1.65);
  const Q = new Array(300).fill(1.65);
  for (const m of METHODS) {
    const { x } = demodulate(m, I, Q);
    assert.equal(x.length, 300, m);
    assert.ok(x.every((v) => v === 0), m);
  }
});

test("dacm-fit equals arctan-fit up to a constant", () => {
  const { I, Q } = arc(1000, 4);
  const a = demodulate("arctan-fit", I, Q).x;
  const d = demodulate("dacm-fit", I, Q).x;
  const off = a[0] - d[0];
  assert.ok(a.every((v, k) => Math.abs(v - d[k] - off) < 1e-3));
});

test("arctan unwraps through more than one full turn", () => {
  const { phase, I, Q } = arc(2000, 10);
  const c = fitCircle(I, Q);
  assert.ok(c.spanDeg > 360);
  assert.ok(corr(demodulate("arctan-fit", I, Q).x, phase) > 0.999);
});

test("unknown method throws", () => {
  assert.throws(() => demodulate("magic", [1], [1]), /unknown method/);
});

test("pca has a fixed sign convention: the output rises with I", () => {
  // Two clouds on the same axis, sampled in opposite orders: same orientation.
  for (const dir of [1, -1]) {
    const t = Array.from({ length: 400 }, (_, k) => dir * Math.sin(k / 15));
    const I = t.map((v) => 1.5 - 0.004 * v);
    const Q = t.map((v) => 1.5 + 0.003 * v);
    assert.ok(corr(demodulate("pca", I, Q).x, I) > 0.99, `dir ${dir}`);
  }
});

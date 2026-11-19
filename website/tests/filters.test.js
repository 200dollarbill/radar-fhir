import test from "node:test";
import assert from "node:assert/strict";
import { butterBandpass, filtfilt, detrend, fillGaps } from "../src/dsp/filters.js";

const fs = 100;
const sine = (f, n, amp = 1) => Array.from({ length: n }, (_, k) => amp * Math.sin(2 * Math.PI * f * k / fs));
const rms = (x) => Math.sqrt(x.reduce((s, v) => s + v * v, 0) / x.length);
const middle = (x) => x.slice(Math.floor(x.length * 0.2), Math.floor(x.length * 0.8));

test("1.2 Hz passes the wide band with unit gain and no lag", () => {
  const x = sine(1.2, 2000);
  const y = filtfilt(butterBandpass(0.5, 10, fs), x);
  const ratio = rms(middle(y)) / rms(middle(x));
  assert.ok(ratio > 0.9 && ratio < 1.1, `gain ${ratio}`);
  // zero phase: the best-matching lag between input and output is 0
  let best = { lag: null, c: -Infinity };
  for (let lag = -10; lag <= 10; lag++) {
    let c = 0;
    for (let k = 500; k < 1500; k++) c += x[k] * y[k + lag];
    if (c > best.c) best = { lag, c };
  }
  assert.equal(best.lag, 0);
});

test("0.05 Hz and 30 Hz are attenuated by the wide band", () => {
  const band = butterBandpass(0.5, 10, fs);
  const slow = sine(0.05, 6000);
  const fast = sine(30, 2000);
  assert.ok(rms(middle(filtfilt(band, slow))) / rms(middle(slow)) < 0.1);
  assert.ok(rms(middle(filtfilt(band, fast))) / rms(middle(fast)) < 0.1);
});

test("filtfilt output has the input length and stays finite on short input", () => {
  const y = filtfilt(butterBandpass(0.5, 10, fs), sine(1, 40));
  assert.equal(y.length, 40);
  assert.ok(y.every(Number.isFinite));
});

test("detrend removes a straight line", () => {
  const y = detrend(Array.from({ length: 100 }, (_, k) => 3 + 0.5 * k));
  assert.ok(y.every((v) => Math.abs(v) < 1e-9));
});

test("fillGaps interpolates NaN and holds edges", () => {
  assert.deepEqual(fillGaps([1, NaN, 3]), [1, 2, 3]);
  assert.deepEqual(fillGaps([NaN, 2]), [2, 2]);
  assert.deepEqual(fillGaps([4, NaN, NaN]), [4, 4, 4]);
  assert.deepEqual(fillGaps([NaN, NaN]), [0, 0]);
});

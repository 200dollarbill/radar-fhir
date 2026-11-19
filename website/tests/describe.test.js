import test from "node:test";
import assert from "node:assert/strict";
import { describeInfo } from "../src/dsp/describe.js";
import { demodulate } from "../src/dsp/demod.js";

const circle = { ok: true, r: 0.005, residualSd: 0.002, spanDeg: 17.2 };

test("too short", () => {
  assert.equal(describeInfo({ used: null, reason: "too-short" }, "hybrid"), "Waiting for 2 s of samples.");
});

test("flat input says no movement", () => {
  const d = demodulate("hybrid", [1, 1, 1], [2, 2, 2]);
  assert.equal(d.flat, true);
  assert.match(describeInfo({ used: d.used, flat: true }, "hybrid"), /No movement/);
});

test("hybrid falling back to pca on a short arc names the arc", () => {
  const s = describeInfo({ used: "pca", circle: { ...circle, residualSd: 0.0002 } }, "hybrid");
  assert.match(s, /linear projection/);
  assert.match(s, /arc of 17° is under 30°/);
  assert.doesNotMatch(s, /spread/);
  assert.match(s, /sign .* arbitrary/);
});

test("hybrid falling back to pca on a scattered cloud names the spread, not the arc", () => {
  // the RABITS case: the fit reports a long arc, but the points are not on a ring
  const s = describeInfo({ used: "pca", circle: { ...circle, spanDeg: 474, residualSd: 0.00155 } }, "hybrid");
  assert.match(s, /not on a circle/);
  assert.match(s, /spread 31 % of radius, limit 15 %/);
  assert.doesNotMatch(s, /474/);
});

test("hybrid on an arc names the arctangent and the arc", () => {
  const s = describeInfo({ used: "arctan-fit", circle: { ...circle, spanDeg: 115.4, residualSd: 0.0001 } }, "hybrid");
  assert.match(s, /arctangent/);
  assert.match(s, /arc 115°/);
  assert.doesNotMatch(s, /arbitrary/);
});

test("a fixed method is named; linear ones carry the sign note", () => {
  assert.match(describeInfo({ used: "single" }, "single"), /^single\..*arbitrary/);
  assert.equal(describeInfo({ used: "arctan-mean" }, "arctan-mean"), "arctan-mean.");
});

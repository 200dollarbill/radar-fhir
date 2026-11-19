import test from "node:test";
import assert from "node:assert/strict";
import { processWindow, BANDS, DEFAULT_METHOD } from "../src/dsp/pipeline.js";
import { METHODS } from "../src/dsp/demod.js";
import { butterBandpass, filtfilt } from "../src/dsp/filters.js";

const fs = 100;
const sd = (x) => {
  const m = x.reduce((s, v) => s + v, 0) / x.length;
  return Math.sqrt(x.reduce((s, v) => s + (v - m) ** 2, 0) / x.length);
};
function corr(a, b) {
  const ma = a.reduce((s, v) => s + v, 0) / a.length;
  const mb = b.reduce((s, v) => s + v, 0) / b.length;
  let sab = 0, saa = 0, sbb = 0;
  for (let k = 0; k < a.length; k++) {
    sab += (a[k] - ma) * (b[k] - mb);
    saa += (a[k] - ma) ** 2;
    sbb += (b[k] - mb) ** 2;
  }
  return sab / Math.sqrt(saa * sbb);
}

function circleWindow(n) {
  const phase = Array.from({ length: n }, (_, k) => 0.8 * Math.sin(2 * Math.PI * 0.25 * k / fs) + 0.3 * Math.sin(2 * Math.PI * 1.2 * k / fs));
  return {
    phase,
    I: phase.map((p) => 1.6 + 0.05 * Math.cos(p + 0.6)),
    Q: phase.map((p) => 1.5 + 0.05 * Math.sin(p + 0.6)),
  };
}

test("bands and default are the spec values", () => {
  assert.deepEqual(BANDS, { wide: [0.5, 10], narrow: [0.7, 3], breathing: [0.1, 0.5] });
  assert.ok(METHODS.includes(DEFAULT_METHOD));
});

test("a window under 2 s returns nothing, with a reason", () => {
  const { I, Q } = circleWindow(150);
  const r = processWindow(I, Q, { fs });
  assert.deepEqual(r.wave, []);
  assert.deepEqual(r.breath, []);
  assert.equal(r.info.reason, "too-short");
});

test("gaps (NaN from E) never reach the output", () => {
  const { I, Q } = circleWindow(1000);
  for (const k of [0, 1, 500, 501, 502, 999]) { I[k] = NaN; Q[k] = NaN; }
  for (const m of METHODS) {
    const r = processWindow(I, Q, { fs, method: m });
    assert.equal(r.wave.length, 1000);
    assert.ok(r.wave.every(Number.isFinite) && r.breath.every(Number.isFinite), m);
  }
});

test("the wide wave follows the band-passed true phase on a clean arc", () => {
  const { phase, I, Q } = circleWindow(1000);
  const truth = filtfilt(butterBandpass(0.5, 10, fs), phase, 300);
  const r = processWindow(I, Q, { fs, method: "arctan-fit" });
  assert.ok(corr(r.wave, truth) > 0.95);
  assert.ok(Math.abs(sd(r.wave) - 1) < 1e-6);
  assert.ok(Math.abs(sd(r.breath) - 1) < 1e-6);
});

test("a flat window gives all-zero output, not NaN", () => {
  const I = new Array(500).fill(1.65);
  const r = processWindow(I, I.slice(), { fs });
  assert.ok(r.wave.every((v) => v === 0) && r.breath.every((v) => v === 0));
});

test("info reports what hybrid actually used", () => {
  const { I, Q } = circleWindow(1000);
  assert.equal(processWindow(I, Q, { fs, method: "hybrid" }).info.used, "arctan-fit");
});

test("bandSignal is the filter processWindow uses, so truth can share it", async () => {
  const { bandSignal } = await import("../src/dsp/pipeline.js");
  const { phase, I, Q } = circleWindow(1000);
  const r = processWindow(I, Q, { fs, method: "arctan-fit" });
  const viaBand = bandSignal(phase, "wide", fs);
  assert.ok(corr(r.wave, viaBand) > 0.9999);
});

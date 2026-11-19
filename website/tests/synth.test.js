import test from "node:test";
import assert from "node:assert/strict";
import { SCENARIOS, scenario, jvpBeat, mulberry32, LSB } from "../eval/synth.js";
import { fitCircle } from "../src/dsp/demod.js";

test("scenario list is the spec's six plus the averaging what-if", () => {
  assert.deepEqual(SCENARIOS.map((s) => s.name), [
    "neck-small", "neck-weak", "chest-large", "imbalance", "dc-drift", "quarter-arc", "neck-weak-avg16",
  ]);
  assert.deepEqual(SCENARIOS.filter((s) => s.ranked).length, 6);
});

test("the same seed gives identical recordings", () => {
  const a = scenario("neck-small", 3, { seconds: 5 });
  const b = scenario("neck-small", 3, { seconds: 5 });
  assert.deepEqual(a.I, b.I);
  assert.deepEqual(a.truth, b.truth);
  assert.notDeepEqual(scenario("neck-small", 4, { seconds: 5 }).I, a.I);
});

test("samples are quantized to the 12-bit, 3.3 V ADC", () => {
  assert.ok(Math.abs(LSB - 3.3 / 4095) < 1e-15);
  const r = scenario("neck-small", 1, { seconds: 5 });
  for (const v of [...r.I, ...r.Q]) {
    const counts = v / LSB;
    assert.ok(Math.abs(counts - Math.round(counts)) < 1e-6);
  }
});

test("chest-large wraps past 180 degrees, neck-weak has an 8 mV radius", () => {
  const chest = scenario("chest-large", 1, { seconds: 20 });
  assert.ok(fitCircle(chest.I, chest.Q).spanDeg > 180);
  assert.equal(SCENARIOS.find((s) => s.name === "neck-weak").radiusV, 0.008);
});

test("the JVP beat has its largest peak (a wave) early in the cycle and two descents", () => {
  const p = Array.from({ length: 100 }, (_, k) => k / 100);
  const y = p.map(jvpBeat);
  const peak = y.indexOf(Math.max(...y));
  assert.ok(peak < 15, `a wave at ${peak}`);
  assert.ok(y[32] < 0 && y[70] < 0, "x and y descents below baseline");
});

test("mulberry32 is deterministic and in [0, 1)", () => {
  const r = mulberry32(42);
  const v = Array.from({ length: 1000 }, r);
  assert.ok(v.every((x) => x >= 0 && x < 1));
  assert.deepEqual(Array.from({ length: 5 }, mulberry32(42)), v.slice(0, 5));
});

test("generate takes a custom configuration; scenario is generate with the listed one", async () => {
  const { generate } = await import("../eval/synth.js");
  const cfg = SCENARIOS[0];
  const a = generate(cfg, 1 * 7919 + 0, { seconds: 3 });
  assert.deepEqual(a.I, scenario("neck-small", 1, { seconds: 3 }).I);
  const wide = generate({ ...cfg, respMm: 2.5 }, 5, { seconds: 20 });
  assert.ok(fitCircle(wide.I, wide.Q).spanDeg > 100);
});

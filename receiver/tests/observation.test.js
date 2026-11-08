import test from "node:test";
import assert from "node:assert/strict";
import { buildObservation, identifierValue } from "../src/observation.js";

const card = {
  token: "t", patient: "Patient/p1", encounter: "Encounter/e1",
  device: "Device/d1", org: "org9", label: "x",
};
const chunk = (o = {}) => ({
  segment: 2, chunkIndex: 5, fs: 100, startTimeMs: Date.UTC(2026, 10, 4, 1, 2, 3, 999),
  channels: {
    I: [1.65, "E", 1.649], Q: [2, 2, 2], ax: [0, 0, 0], ay: [0, 0, 0], az: [1, 1, 1],
    gx: [0, 0, 0], gy: [0, 0, 0], gz: [0, 0, 0],
  },
  gapSamples: 1, rejectedLines: 4, deviceMissed: 7, ...o,
});
const opts = { captureId: "cap-abc", source: "serial" };

test("code, identifier, references and component order match the spec", () => {
  const o = buildObservation(chunk(), card, opts);
  assert.equal(o.resourceType, "Observation");
  assert.equal(o.status, "final");
  assert.deepEqual(o.identifier, [{
    system: "http://sys-ids.kemkes.go.id/organization/org9", value: "cap-abc-2-5",
  }]);
  assert.equal(identifierValue("cap-abc", chunk()), "cap-abc-2-5");
  assert.deepEqual(o.code, { coding: [{
    system: "urn:prata:radar-signal", code: "raw-capture", display: "Raw radar I/Q capture",
  }] });
  assert.deepEqual(o.subject, { reference: "Patient/p1" });
  assert.deepEqual(o.encounter, { reference: "Encounter/e1" });
  assert.deepEqual(o.device, { reference: "Device/d1" });
  assert.deepEqual(
    o.component.map((c) => c.code.coding[0].code),
    ["i-voltage", "q-voltage", "accel-x", "accel-y", "accel-z", "gyro-x", "gyro-y", "gyro-z"],
  );
  for (const c of o.component) {
    assert.equal(c.code.coding[0].system, "urn:prata:radar-signal");
    assert.equal(c.valueSampledData.dimensions, 1);
    assert.equal(c.valueSampledData.origin.value, 0);
    assert.equal(c.valueSampledData.origin.system, "http://unitsofmeasure.org");
  }
});

test("note parses to {source, gap_samples, rejected_lines, device_missed}", () => {
  const o = buildObservation(chunk(), card, opts);
  assert.equal(o.note.length, 1);
  assert.deepEqual(JSON.parse(o.note[0].text),
    { source: "serial", gap_samples: 1, rejected_lines: 4, device_missed: 7 });
  assert.equal(o.note[0].text,
    '{"source":"serial","gap_samples":1,"rejected_lines":4,"device_missed":7}');
});

test("period is 10 at fs 100 and 4 at fs 250", () => {
  assert.equal(buildObservation(chunk(), card, opts).component[0].valueSampledData.period, 10);
  assert.equal(buildObservation(chunk({ fs: 250 }), card, opts).component[0].valueSampledData.period, 4);
});

test("data joins numbers and E with single spaces", () => {
  const o = buildObservation(chunk(), card, opts);
  assert.equal(o.component[0].valueSampledData.data, "1.65 E 1.649");
  assert.equal(o.component[1].valueSampledData.data, "2 2 2");
});

test("origin unit and UCUM code per channel: V, [g], deg/s", () => {
  const o = buildObservation(chunk(), card, opts);
  const units = o.component.map((c) => [c.valueSampledData.origin.unit, c.valueSampledData.origin.code]);
  assert.deepEqual(units, [
    ["V", "V"], ["V", "V"], ["[g]", "[g]"], ["[g]", "[g]"], ["[g]", "[g]"],
    ["deg/s", "deg/s"], ["deg/s", "deg/s"], ["deg/s", "deg/s"],
  ]);
});

test("effectiveDateTime has the form YYYY-MM-DDThh:mm:ss+00:00", () => {
  const o = buildObservation(chunk(), card, opts);
  assert.equal(o.effectiveDateTime, "2026-11-04T01:02:03+00:00");
});

test("no category and no top-level value", () => {
  const o = buildObservation(chunk(), card, opts);
  assert.equal("category" in o, false);
  assert.equal(Object.keys(o).some((k) => k.startsWith("value")), false);
});

test("SIMULATED source appears in note", () => {
  const o = buildObservation(chunk(), card, { captureId: "cap-abc", source: "SIMULATED" });
  assert.equal(JSON.parse(o.note[0].text).source, "SIMULATED");
});

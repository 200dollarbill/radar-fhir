import test from "node:test";
import assert from "node:assert/strict";
import { parseCsv, parseBundle, parseRecording } from "../src/recording.js";

const CSV = `epoch_id,sample_idx,t_host_unix,fs,crc_ok,missed,I,Q,ax,ay,az,gx,gy,gz
11,0,1789460288.94302,100,1,0,1.5295,1.5327,-0.685,0.724,-0.172,-1,1,0
11,1,1789460288.95302,100,1,0,1.5287,1.5328,-0.688,0.73,-0.166,0,0,0
`;

function chunk(index, i, q) {
  const comp = (code, data) => ({
    code: { coding: [{ system: "urn:prata:radar-signal", code }] },
    valueSampledData: { origin: { value: 0 }, period: 10, dimensions: 1, data },
  });
  return {
    resource: {
      resourceType: "Observation",
      code: { coding: [{ system: "urn:prata:radar-signal", code: "raw-capture" }] },
      identifier: [{ value: `cap-0-${index}` }],
      component: [comp("i-voltage", i), comp("q-voltage", q)],
    },
  };
}

test("CSV in the firmware column order parses", () => {
  const r = parseCsv(CSV);
  assert.equal(r.fs, 100);
  assert.deepEqual(r.I, [1.5295, 1.5287]);
  assert.deepEqual(r.Q, [1.5327, 1.5328]);
});

test("Bundle chunks are sorted by chunk number, E becomes NaN, fs from period", () => {
  const bundle = { resourceType: "Bundle", entry: [chunk(1, "3 4", "7 8"), chunk(0, "1 E", "5 6")] };
  const r = parseBundle(bundle);
  assert.equal(r.fs, 100);
  assert.equal(r.I.length, 4);
  assert.equal(r.I[0], 1);
  assert.ok(Number.isNaN(r.I[1]));
  assert.deepEqual(r.I.slice(2), [3, 4]);
  assert.deepEqual(r.Q, [5, 6, 7, 8]);
});

test("Bundle entries that are not raw captures are skipped", () => {
  const other = { resource: { resourceType: "Observation", code: { coding: [{ code: "8867-4" }] } } };
  const r = parseBundle({ resourceType: "Bundle", entry: [other, chunk(0, "1 2", "3 4")] });
  assert.deepEqual(r.I, [1, 2]);
});

test("parseRecording picks the format from the first character", () => {
  assert.equal(parseRecording(CSV).I.length, 2);
  const json = JSON.stringify({ resourceType: "Bundle", entry: [chunk(0, "1 2", "3 4")] });
  assert.equal(parseRecording("  " + json).I.length, 2);
});

test("a CSV without I and Q columns is refused", () => {
  assert.throws(() => parseCsv("a,b\n1,2\n"), /I and Q/);
});

test("a Bundle without raw captures is refused", () => {
  assert.throws(() => parseBundle({ resourceType: "Bundle", entry: [] }), /no raw-capture/);
});

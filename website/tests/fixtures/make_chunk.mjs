// Usage: node make_chunk.mjs '<card JSON>'
// Prints {"observation", "identifier", "expected"} for one chunk that includes a gap.
// Lines go through formatLine, the real parser, the real chunker and the real builder.
import { formatLine } from "../../src/simulator.js";
import { parseLine } from "../../src/jsonlines.js";
import { Chunker } from "../../src/chunker.js";
import { buildObservation, identifierValue } from "../../src/observation.js";

const card = JSON.parse(process.argv[2]);
const captureId = "cap-e2e-fixture";
const FS = 100;
const GAP = [10, 11]; // sample indexes the "device" never sent
const N = 20;
const CHANNELS = ["I", "Q", "ax", "ay", "az", "gx", "gy", "gz"];

const chunks = [];
const chunker = new Chunker({ now: () => 1_700_000_000_000, onChunk: (c) => chunks.push(c) });
const expected = Object.fromEntries(CHANNELS.map((c) => [c, []]));

for (let i = 0; i < N; i++) {
  const values = { I: 1.5 + i * 0.01, Q: 1.8 - i * 0.01, ax: 0.1 * i, ay: -0.05 * i, az: 1, gx: i, gy: -i, gz: 0 };
  if (GAP.includes(i)) {
    for (const c of CHANNELS) expected[c].push("E");
    continue;
  }
  // Expected tokens come from the wire format (6 decimals) independently of the chunker.
  for (const c of CHANNELS) expected[c].push(String(Number(values[c].toFixed(6))));
  const parsed = parseLine(formatLine(i, FS, values));
  if (parsed.kind !== "sample") throw new Error(`line ${i} not a sample`);
  chunker.addSample(parsed.sample);
}
chunker.flush();
if (chunks.length !== 1) throw new Error(`expected 1 chunk, got ${chunks.length}`);

const observation = buildObservation(chunks[0], card, { captureId, source: "SIMULATED" });
const identifier = `http://sys-ids.kemkes.go.id/organization/${card.org}|${identifierValue(captureId, chunks[0])}`;
console.log(JSON.stringify({ observation, identifier, expected }));

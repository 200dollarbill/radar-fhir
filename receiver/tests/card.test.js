import test from "node:test";
import assert from "node:assert/strict";
import { parseCard } from "../src/card.js";

const good = {
  token: "tok", patient: "Patient/p1", encounter: "Encounter/e1",
  device: "Device/d1", org: "org1", label: "Synthetic A",
};

test("a valid card parses", () => {
  assert.deepEqual(parseCard(JSON.stringify(good)), good);
});

test("empty string gives a message saying to paste a card", () => {
  assert.throws(() => parseCard("  "), /paste/i);
});

test("non-JSON text gives a message saying it is not valid JSON", () => {
  assert.throws(() => parseCard("hello"), /not valid JSON/i);
});

test("seed summary JSON is rejected, naming the missing field", () => {
  const seed = { organization: "org1", patients: [], practitioner: "x" };
  assert.throws(() => parseCard(JSON.stringify(seed)), /missing field token/);
});

test("patient without the Patient/ prefix is rejected", () => {
  assert.throws(() => parseCard(JSON.stringify({ ...good, patient: "p1" })), /patient must start with Patient\//);
});

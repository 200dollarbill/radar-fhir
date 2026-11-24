import test from "node:test";
import assert from "node:assert/strict";
import { patientOptions, practitionerOptions, freeBoards, fmtTime, apiError } from "../src/sessions-view.js";

const bundle = (resources) => ({ resourceType: "Bundle", entry: resources.map((resource) => ({ resource })) });

test("patientOptions lists name and id, sorted by name", () => {
  const b = bundle([
    { resourceType: "Patient", id: "P2", name: [{ text: "Sesi S002" }] },
    { resourceType: "Patient", id: "P1", name: [{ text: "Budi Santoso" }] },
    { resourceType: "Patient", id: "P3" },
  ]);
  assert.deepEqual(patientOptions(b), [
    { value: "Patient/P3", label: "(no name) · P3" },
    { value: "Patient/P1", label: "Budi Santoso · P1" },
    { value: "Patient/P2", label: "Sesi S002 · P2" },
  ]);
  assert.deepEqual(patientOptions({ resourceType: "Bundle" }), []);
});

test("practitionerOptions uses the name text", () => {
  const b = bundle([{ resourceType: "Practitioner", id: "N1", name: [{ text: "drg. Contoh" }] }]);
  assert.deepEqual(practitionerOptions(b), [{ value: "Practitioner/N1", label: "drg. Contoh" }]);
});

test("freeBoards keeps boards without an open session", () => {
  const boards = [{ id: "A", session: null }, { id: "B", session: { id: "s" } }, { id: "SIM-0000000C", session: null }];
  assert.deepEqual(freeBoards(boards).map((b) => b.id), ["A", "SIM-0000000C"]);
});

test("fmtTime shows a local date and time, and a dash for none", () => {
  assert.equal(fmtTime(null), "—");
  assert.match(fmtTime("2026-11-18T10:05:00+00:00"), /2026/);
});

test("apiError reads the OperationOutcome text, else the status", async () => {
  const oo = { issue: [{ details: { text: "Board X already has an open session" } }] };
  assert.equal(await apiError({ status: 409, text: async () => JSON.stringify(oo) }), "Board X already has an open session");
  assert.equal(await apiError({ status: 500, text: async () => "oops" }), "HTTP 500");
});

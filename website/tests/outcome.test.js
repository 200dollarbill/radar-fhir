import test from "node:test";
import assert from "node:assert/strict";
import { apiError } from "../src/outcome.js";

const oo = (text) => JSON.stringify({ resourceType: "OperationOutcome", issue: [{ severity: "error", code: "throttled", details: { text } }] });

test("apiError gives the OperationOutcome text", async () => {
  assert.equal(await apiError({ status: 429, text: async () => oo("Too many login attempts. Try again in a minute.") }),
    "Too many login attempts. Try again in a minute.");
});

test("apiError falls back to the status for a body that is not JSON", async () => {
  assert.equal(await apiError({ status: 503, text: async () => "<html>Bad gateway</html>" }), "HTTP 503");
});

test("apiError falls back to the status for an OperationOutcome without text", async () => {
  const body = JSON.stringify({ resourceType: "OperationOutcome", issue: [{ severity: "error", code: "invalid" }] });
  assert.equal(await apiError({ status: 400, text: async () => body }), "HTTP 400");
});

import test from "node:test";
import assert from "node:assert/strict";
import { recordingSummary } from "../src/recstate.js";

const base = { label: "S001", fs: 100, samples: 1325, saved: 2, pending: 0, rejected: 0,
  uploader: "idle", reason: null, savedAt: "19:42" };

test("nothing to say before the first recording", () => {
  assert.equal(recordingSummary({ ...base, phase: "idle" }), null);
});

test("while recording: label, duration and chunks saved so far", () => {
  assert.deepEqual(recordingSummary({ ...base, phase: "recording", samples: 1200, saved: 1, pending: 0 }),
    { kind: "rec", text: "● Recording S001: 12 s · 1 chunk saved so far." });
});

test("after stop, chunks still uploading: saving", () => {
  assert.deepEqual(recordingSummary({ ...base, phase: "stopped", saved: 1, pending: 1, uploader: "sending" }),
    { kind: "busy", text: "Saving S001: 1 chunk left to upload…" });
});

test("after stop, all uploaded: saved, with duration, chunks and time", () => {
  assert.deepEqual(recordingSummary({ ...base, phase: "stopped" }),
    { kind: "ok", text: "✓ Saved: 13 s of S001 (2 chunks) stored on the server at 19:42." });
});

test("server unreachable: not saved yet, kept in the browser", () => {
  const r = recordingSummary({ ...base, phase: "stopped", pending: 2, saved: 0, uploader: "retry" });
  assert.equal(r.kind, "warn");
  assert.match(r.text, /^Not saved yet: the server is unreachable, retrying\. 2 chunks are kept in this browser\.$/);
});

test("board key refused: not saved, kept in the browser", () => {
  const r = recordingSummary({ ...base, phase: "stopped", pending: 1, saved: 1, uploader: "auth" });
  assert.equal(r.kind, "warn");
  assert.match(r.text, /^Not saved: the server refused the board key \(session ended\?\)\. 1 chunk is kept in this browser\.$/);
});

test("rejected chunks are reported even when nothing is pending", () => {
  const r = recordingSummary({ ...base, phase: "stopped", rejected: 1, reason: "Encounter is not in-progress" });
  assert.equal(r.kind, "warn");
  assert.equal(r.text, "Saved with problems: 2 chunks stored, 1 rejected by the server (Encounter is not in-progress).");
});

test("a stop with no samples says nothing was recorded", () => {
  assert.deepEqual(recordingSummary({ ...base, phase: "stopped", samples: 0, saved: 0 }),
    { kind: "warn", text: "Nothing was recorded: no samples arrived while recording." });
});

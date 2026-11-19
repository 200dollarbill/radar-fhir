import test from "node:test";
import assert from "node:assert/strict";
import { serialSend } from "../src/serial.js";

test("serialSend writes UTF-8 bytes and releases the writer", async () => {
  const written = [];
  let released = 0;
  const port = { writable: { getWriter: () => ({ write: async (b) => { written.push(b); }, releaseLock: () => { released++; } }) } };
  await serialSend(port, "BOARD?\n");
  assert.equal(new TextDecoder().decode(written[0]), "BOARD?\n");
  assert.equal(released, 1);
});

test("serialSend releases the writer when the write fails", async () => {
  let released = 0;
  const port = { writable: { getWriter: () => ({ write: async () => { throw new Error("gone"); }, releaseLock: () => { released++; } }) } };
  await assert.rejects(serialSend(port, "x"), /gone/);
  assert.equal(released, 1);
});

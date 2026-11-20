import test from "node:test";
import assert from "node:assert/strict";
import { setEnvLine } from "../tunnel-token.mjs";

test("adds the line and keeps the other secrets", () => {
  assert.equal(setEnvLine("export A=1\nexport B=2\n", "TOKEN", "xyz"), "export A=1\nexport B=2\nexport TOKEN=xyz\n");
});

test("replaces an existing line instead of adding a second one", () => {
  assert.equal(setEnvLine("export A=1\nexport TOKEN=old\nexport B=2\n", "TOKEN", "new"), "export A=1\nexport TOKEN=new\nexport B=2\n");
});

test("copes with a file without a final newline, and with an empty file", () => {
  assert.equal(setEnvLine("export A=1", "TOKEN", "v"), "export A=1\nexport TOKEN=v\n");
  assert.equal(setEnvLine("", "TOKEN", "v"), "export TOKEN=v\n");
});

test("does not touch a line whose name only starts the same", () => {
  assert.equal(setEnvLine("export TOKEN_OLD=1\n", "TOKEN", "v"), "export TOKEN_OLD=1\nexport TOKEN=v\n");
});

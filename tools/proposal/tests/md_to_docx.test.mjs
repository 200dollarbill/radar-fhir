import { test } from "node:test";
import assert from "node:assert/strict";
import { mdToDocx, parseBlocks } from "../md_to_docx.mjs";
import { fileURLToPath } from "node:url";
import path from "node:path";

const here = path.dirname(fileURLToPath(import.meta.url));

test("heading becomes a heading block", () => {
  const b = parseBlocks("### 1.1 Latar Belakang");
  assert.equal(b[0].kind, "heading");
  assert.equal(b[0].level, 3);
});

test("missing image throws with its path", async () => {
  await assert.rejects(mdToDocx("![Gambar](figures/x.png)", here), /figures\/x\.png/);
});

test("pipe table yields a table block with 3 columns", () => {
  const b = parseBlocks("| a | b | c |\n|---|---|---|\n| 1 | 2 | 3 |");
  assert.equal(b[0].kind, "table");
  assert.equal(b[0].rows[0].length, 3);
  assert.equal(b[0].rows.length, 2);
});

test("html comments are stripped from paragraphs", () => {
  const b = parseBlocks("Teks diagnosis. <!-- check:ok diagnosis -->");
  assert.equal(b[0].text, "Teks diagnosis.");
});

test("export stops at the student notes block", () => {
  const b = parseBlocks("Isi.\n\nCatatan untuk Mahasiswa\nCatatan lama.");
  assert.equal(b.length, 1);
});

test("output is a zip buffer", async () => {
  const buf = await mdToDocx("# Judul\n\nParagraf **tebal**.", here);
  assert.equal(buf.subarray(0, 2).toString(), "PK");
});

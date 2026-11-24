import test from "node:test";
import assert from "node:assert/strict";
import { existsSync, mkdtempSync, readFileSync, writeFileSync, mkdirSync } from "node:fs";
import { tmpdir } from "node:os";
import { join, dirname } from "node:path";
import { fileURLToPath } from "node:url";
import { build, HEADERS, REDIRECTS } from "../build.mjs";

const websiteDir = join(dirname(fileURLToPath(import.meta.url)), "..", "..", "website");

async function built() {
  const outDir = join(mkdtempSync(join(tmpdir(), "prata-build-")), "public");
  mkdirSync(outDir);
  writeFileSync(join(outDir, "stale.txt"), "left over from an older build");
  await build({ websiteDir, outDir });
  return outDir;
}

test("the pages and their modules are copied under capture/", async () => {
  const out = await built();
  for (const f of ["index.html", "sessions.html", "review.html", "guard.js", "site.css", "src/auth.js", "src/outcome.js"]) {
    assert.ok(existsSync(join(out, "capture", f)), f);
  }
});

test("tests, evaluation and package.json are left out", async () => {
  const out = await built();
  for (const f of ["tests", "eval", "package.json"]) assert.ok(!existsSync(join(out, "capture", f)), f);
});

test("_headers and _redirects are written", async () => {
  const out = await built();
  assert.equal(readFileSync(join(out, "_headers"), "utf8"), HEADERS);
  assert.equal(readFileSync(join(out, "_redirects"), "utf8"), REDIRECTS);
  assert.equal(REDIRECTS, "/ /capture/sessions.html 302\n");
  assert.match(HEADERS, /^\/\*\n  Content-Security-Policy: default-src 'self'; style-src 'self' 'unsafe-inline'\n/);
  assert.match(HEADERS, /\n  Permissions-Policy: serial=\(self\)\n/);
});

test("files from an older build are removed", async () => {
  const out = await built();
  assert.ok(!existsSync(join(out, "stale.txt")));
});

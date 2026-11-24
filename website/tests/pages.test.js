// Static checks of the three pages: navigation must work without JavaScript, and a
// page whose script fails to load must say so instead of looking alive but dead.
import test from "node:test";
import assert from "node:assert/strict";
import { readFileSync } from "node:fs";

const PAGES = [
  { file: "index.html", script: "app.js", current: "./" },
  { file: "sessions.html", script: "sessions.js", current: "sessions.html" },
  { file: "review.html", script: "review.js", current: "review.html" },
];
const read = (f) => readFileSync(new URL(`../${f}`, import.meta.url), "utf8");

for (const p of PAGES) {
  test(`${p.file}: the top bar links are in the HTML, current page marked`, () => {
    const html = read(p.file);
    const nav = html.match(/<nav[^>]*id="topnav"[^>]*>([\s\S]*?)<\/nav>/);
    assert.ok(nav, "nav#topnav present");
    for (const href of ["sessions.html", "./", "review.html"]) {
      assert.ok(nav[1].includes(`href="${href}"`), `link to ${href}`);
    }
    assert.match(nav[1], new RegExp(`href="${p.current.replace(".", "\\.")}" aria-current="page"`));
  });

  test(`${p.file}: a failed script load is repaired, else reported`, () => {
    const html = read(p.file);
    assert.match(html, /id="load-error"[^>]*hidden/);
    const guard = html.indexOf('<script src="guard.js"></script>');
    const moduleTag = html.indexOf(`<script type="module" src="${p.script}">`);
    assert.ok(guard > 0 && moduleTag > guard, "guard.js before the module script");
    assert.doesNotMatch(html, /addEventListener\("error"/, "no inline copy of the guard");
    assert.match(read(p.script), /window\.prataLoaded = true;\s*$/);
  });
}

test("guard.js re-fetches the page's files past the cache, reloads, and gives up after two tries", () => {
  const g = read("guard.js");
  assert.match(g, /getEntriesByType\("resource"\)/);
  assert.match(g, /cache: "reload"/);
  assert.match(g, /location\.reload\(\)/);
  assert.match(g, /MAX_TRIES = 2/);
  assert.match(g, /Ctrl\+Shift\+R/);
});

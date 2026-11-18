import test from "node:test";
import assert from "node:assert/strict";
import { navItems, userLabel } from "../src/nav.js";

test("the bar lists Sessions, Capture, Review and marks the current page", () => {
  const labels = (p) => navItems(p).map((i) => i.label + (i.current ? "*" : ""));
  assert.deepEqual(labels("/capture/"), ["Sessions", "Capture*", "Review"]);
  assert.deepEqual(labels("/capture/index.html"), ["Sessions", "Capture*", "Review"]);
  assert.deepEqual(labels("/capture/sessions.html"), ["Sessions*", "Capture", "Review"]);
  assert.deepEqual(labels("/capture/review.html"), ["Sessions", "Capture", "Review*"]);
  assert.deepEqual(navItems("/capture/").map((i) => i.href), ["sessions.html", "./", "review.html"]);
});

test("userLabel names the login, or null", () => {
  assert.equal(userLabel({ username: "admin", role: "admin" }), "admin (admin)");
  assert.equal(userLabel(null), null);
});

import test from "node:test";
import assert from "node:assert/strict";
import { coalesce } from "../src/coalesce.js";

function fakeTimers() {
  const pending = [];
  return { setTimer: (f) => { pending.push(f); return pending.length; }, pending };
}

test("many calls before the timer fires run fn once", async () => {
  const t = fakeTimers();
  let n = 0;
  const schedule = coalesce(async () => { n++; }, 250, t);
  for (let k = 0; k < 100; k++) schedule();
  assert.equal(t.pending.length, 1);
  await t.pending.shift()();
  assert.equal(n, 1);
  assert.equal(t.pending.length, 0);
});

test("never runs two at once; a call during a run triggers one later run", async () => {
  const t = fakeTimers();
  let active = 0, maxActive = 0, runs = 0;
  let release;
  const schedule = coalesce(async () => {
    runs++; active++; maxActive = Math.max(maxActive, active);
    await new Promise((r) => { release = r; });
    active--;
  }, 250, t);
  schedule();
  const first = t.pending.shift()();
  schedule(); schedule();
  assert.equal(t.pending.length, 0);
  release();
  await first;
  assert.equal(t.pending.length, 1);
  const second = t.pending.shift()();
  release();
  await second;
  assert.equal(runs, 2);
  assert.equal(maxActive, 1);
});

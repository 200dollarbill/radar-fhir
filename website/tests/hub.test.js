import test from "node:test";
import assert from "node:assert/strict";
import { LineHub } from "../src/hub.js";
import { channel } from "./channel.js";

const tick = () => new Promise((r) => setTimeout(r, 0));

async function take(sub, n) {
  const out = [];
  for (let k = 0; k < n; k++) out.push((await sub.next()).value);
  return out;
}

test("every subscriber gets the lines that arrive after it subscribed", async () => {
  const src = channel();
  const hub = new LineHub(src);
  const running = hub.run();
  const a = hub.subscribe();
  src.push("1");
  await tick();
  const b = hub.subscribe();
  src.push("2");
  src.push("3");
  assert.deepEqual(await take(a, 3), ["1", "2", "3"]);
  assert.deepEqual(await take(b, 2), ["2", "3"]);
  src.end();
  assert.equal(await running, "ended");
  assert.equal((await a.next()).done, true);
});

test("unsubscribing ends that subscriber only; the source and others go on", async () => {
  const src = channel();
  const hub = new LineHub(src);
  const running = hub.run();
  const preview = hub.subscribe();
  const record = hub.subscribe();
  src.push("x");
  await tick();
  hub.unsubscribe(record);
  assert.equal((await record.next()).value, "x"); // queued lines still delivered
  assert.equal((await record.next()).done, true);
  src.push("y");
  assert.deepEqual(await take(preview, 2), ["x", "y"]);
  src.end();
  await running;
});

test("for-await break unsubscribes", async () => {
  const src = channel();
  const hub = new LineHub(src);
  hub.run();
  const sub = hub.subscribe();
  src.push("a");
  for await (const line of sub) { assert.equal(line, "a"); break; }
  assert.equal(hub.subs.size, 0);
  src.end();
});

test("a source failure reaches subscribers as a rejection and run reports disconnected", async () => {
  const src = channel();
  const hub = new LineHub(src);
  const running = hub.run();
  const sub = hub.subscribe();
  src.fail(new Error("device lost"));
  await assert.rejects(sub.next(), /device lost/);
  assert.equal(await running, "disconnected");
  await assert.rejects(hub.subscribe().next(), /device lost/);
});

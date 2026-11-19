import test from "node:test";
import assert from "node:assert/strict";
import { parseBoardLine, formatBoardLine, requestBoard } from "../src/board.js";
import { LineHub } from "../src/hub.js";
import { channel } from "./channel.js";

const KEY = "0123456789abcdef".repeat(4);
const LINE = `BOARD {"id":"AB12CD34EF56","key":"${KEY}","fw":"radar_json"}`;

test("parseBoardLine accepts the firmware line and rejects everything else", () => {
  assert.deepEqual(parseBoardLine(LINE), { id: "AB12CD34EF56", key: KEY, fw: "radar_json" });
  assert.deepEqual(parseBoardLine(LINE + "\r").id, "AB12CD34EF56");
  assert.equal(parseBoardLine('{"sample_idx":1}'), null);
  assert.equal(parseBoardLine("BOARD {bad json"), null);
  assert.equal(parseBoardLine(`BOARD {"id":"ab12cd34ef56","key":"${KEY}"}`), null);
  assert.equal(parseBoardLine(`BOARD {"id":"AB12CD34EF56","key":"xyz"}`), null);
  assert.equal(parseBoardLine(`BOARD {"id":"SIM-0A1B2C3D","key":"${KEY}"}`).id, "SIM-0A1B2C3D");
});

test("formatBoardLine round-trips", () => {
  const b = { id: "SIM-0A1B2C3D", key: KEY };
  assert.deepEqual(parseBoardLine(formatBoardLine(b, "simulator")), { ...b, fw: "simulator" });
});

test("requestBoard asks, skips sample lines, and returns the board", async () => {
  const src = channel();
  const hub = new LineHub(src);
  hub.run();
  const sent = [];
  const send = async (t) => {
    sent.push(t);
    src.push('{"sample_idx":1}');
    src.push("READY radar_json id=AB12CD34EF56");
    src.push(LINE);
  };
  const board = await requestBoard(hub, send, { timeoutMs: 500, retryMs: 100 });
  assert.equal(board.id, "AB12CD34EF56");
  assert.deepEqual(sent, ["BOARD?\n"]);
  assert.equal(hub.subs.size, 0);
  src.end();
});

test("requestBoard asks again each retry and gives up at the timeout", async () => {
  const src = channel();
  const hub = new LineHub(src);
  hub.run();
  const sent = [];
  await assert.rejects(
    requestBoard(hub, async (t) => { sent.push(t); src.push('{"sample_idx":1}'); },
      { timeoutMs: 260, retryMs: 100 }),
    (e) => e.code === "no-reply");
  assert.ok(sent.length >= 3 && sent.length <= 4, `sent ${sent.length}`);
  assert.equal(hub.subs.size, 0);
  src.end();
});

test("requestBoard reports a disconnect", async () => {
  const src = channel();
  const hub = new LineHub(src);
  hub.run();
  await assert.rejects(
    requestBoard(hub, async () => { src.end(); }, { timeoutMs: 500, retryMs: 100 }),
    (e) => e.code === "disconnected");
});

// The board handshake: ask "BOARD?" and wait for the board's ID and key.
// KNOWN VULNERABILITY (spec 2026-11-18): the key crosses the port in clear text.

export const BOARD_ID = /^(?:[0-9A-F]{12}|SIM-[0-9A-F]{8})$/;
export const BOARD_KEY = /^[0-9a-f]{64}$/;

export function parseBoardLine(line) {
  const text = String(line).trim();
  if (!text.startsWith("BOARD ")) return null;
  let body;
  try { body = JSON.parse(text.slice(6)); } catch { return null; }
  if (!body || !BOARD_ID.test(body.id) || !BOARD_KEY.test(body.key)) return null;
  return { id: body.id, key: body.key, fw: typeof body.fw === "string" ? body.fw : null };
}

export function formatBoardLine({ id, key }, fw) {
  return `BOARD ${JSON.stringify({ id, key, fw })}`;
}

function boardError(code, message) {
  const e = new Error(message);
  e.code = code;
  return e;
}

const TIMER = Symbol("timer");

// Asks once per retryMs until a BOARD line arrives or timeoutMs passes.
export async function requestBoard(hub, send, { timeoutMs = 3000, retryMs = 1000, now = Date.now,
  sleep = (ms) => new Promise((r) => setTimeout(r, ms)) } = {}) {
  const sub = hub.subscribe();
  const deadline = now() + timeoutMs;
  let nextSend = now();
  let pending = null;
  try {
    for (;;) {
      if (now() >= deadline) throw boardError("no-reply", "The board did not answer BOARD?. Flash the current firmware.");
      if (now() >= nextSend) {
        await send("BOARD?\n");
        nextSend = now() + retryMs;
      }
      pending ??= sub.next();
      const wait = Math.max(0, Math.min(nextSend, deadline) - now());
      let step;
      try {
        step = await Promise.race([pending, sleep(wait).then(() => TIMER)]);
      } catch {
        throw boardError("disconnected", "The board disconnected.");
      }
      if (step === TIMER) continue;
      pending = null;
      if (step.done) throw boardError("disconnected", "The board disconnected.");
      const board = parseBoardLine(step.value);
      if (board) return board;
    }
  } finally {
    hub.unsubscribe(sub);
  }
}

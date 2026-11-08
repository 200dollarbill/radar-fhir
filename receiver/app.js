// Page wiring only. Logic lives in src/.
import { parseCard } from "./src/card.js";
import { Outbox, IndexedDbStore, sessionKey } from "./src/outbox.js";
import { Uploader } from "./src/uploader.js";
import { Capture } from "./src/capture.js";
import { simulatorLines } from "./src/simulator.js";
import { serialLines } from "./src/serial.js";
import { Trace, draw } from "./src/plot.js";
import { coalesce } from "./src/coalesce.js";

const $ = (id) => document.getElementById(id);
const outbox = new Outbox(new IndexedDbStore());
const trace = new Trace();

let card = null;
let uploader = null;
let abort = null;
let stats = { samples: 0, gaps: 0, rejected: 0 };
let up = { confirmed: 0, lastRejectedReason: null, state: "idle" };
let counts = { pending: 0, rejected: 0, otherSession: 0 };
let running = false;

const showError = (msg) => { $("error").textContent = msg; };

async function refresh() {
  if (card) {
    try { counts = await outbox.counts(sessionKey(card)); } catch (e) { showError(`Storage error: ${e.message}`); }
  }
  $("status").textContent =
    `Samples ${stats.samples} | Chunks confirmed ${up.confirmed} | Chunks pending ${counts.pending} | ` +
    `Gaps ${stats.gaps} | Rejected lines ${stats.rejected}`;
  const notes = [];
  if (counts.rejected > 0) {
    notes.push(`${counts.rejected} chunks rejected by the server` +
      (up.lastRejectedReason ? `; latest reason: ${up.lastRejectedReason}` : "") + ".");
  }
  if (counts.otherSession > 0) {
    notes.push(`${counts.otherSession} chunks belong to another session. Paste that session's card to send them.`);
  }
  $("notes").textContent = notes.join(" ");
}

// At most ~4 refreshes a second and never two at once: counts() clones the whole outbox.
const scheduleRefresh = coalesce(refresh, 250);

function onUploadStatus(s) {
  up = s;
  if (s.state === "auth") showError("Token invalid. Paste a new card.");
  scheduleRefresh();
}

function setRunning(on, simulated = false) {
  running = on;
  $("stop").disabled = !on;
  $("connect").disabled = on || !navigator.serial;
  $("simulate").disabled = on;
  $("simulated").hidden = !(on && simulated);
}

function useCard() {
  showError("");
  let parsed;
  try {
    parsed = parseCard($("card").value);
  } catch (e) {
    showError(e.message);
    return;
  }
  card = parsed;
  try { sessionStorage.setItem("prata-card", $("card").value); } catch { /* storage unavailable */ }
  $("card-label").textContent = `Using card: ${card.label}`;
  if (uploader) uploader.resume(card);
  else {
    uploader = new Uploader({ outbox, fetchFn: (...a) => fetch(...a), card, onStatus: onUploadStatus });
    uploader.start();
  }
  scheduleRefresh();
}

async function startCapture(kind) {
  showError("");
  if (!card) { showError("Paste the session card and click Use card first."); return; }
  abort = new AbortController();
  const { signal } = abort;
  let lines;
  if (kind === "sim") {
    lines = simulatorLines({ signal });
  } else {
    try {
      const port = await navigator.serial.requestPort();
      lines = serialLines(port, { signal });
    } catch (e) {
      showError(`Could not open serial port: ${e.message}`);
      return;
    }
  }
  const capture = new Capture({
    outbox, sessionKey: sessionKey(card), card,
    source: kind === "sim" ? "SIMULATED" : "serial",
    onSample: (s) => { trace.push(s.I, s.Q); draw($("plot"), trace); },
    onStatus: (st) => { stats = st; scheduleRefresh(); },
  });
  setRunning(true, kind === "sim");
  try {
    const result = await capture.run(lines);
    if (result === "disconnected") showError("Disconnected. Click Connect to resume.");
    else if (result === "quota") {
      showError("Browser storage is full. Capture stopped. The unsaved partial chunk was lost.");
    }
  } catch (e) {
    showError(`Capture failed: ${e.message}`);
  } finally {
    abort = null;
    setRunning(false);
    scheduleRefresh();
  }
}

$("use-card").addEventListener("click", useCard);
$("connect").addEventListener("click", () => startCapture("serial"));
$("simulate").addEventListener("click", () => startCapture("sim"));
$("stop").addEventListener("click", () => { abort?.abort(); });

if (!navigator.serial) {
  $("connect").disabled = true;
  $("connect").title = "This browser has no Web Serial. Use Chrome or Edge.";
  showError("This browser has no Web Serial. Use Chrome or Edge.");
}

try {
  const saved = sessionStorage.getItem("prata-card");
  if (saved) { $("card").value = saved; useCard(); }
} catch { /* storage unavailable */ }

// Chunks left from an earlier load are reported; they upload once a card is set.
(async () => {
  try {
    const rows = await outbox.store.all();
    if (rows.length > 0 && !card) {
      $("notes").textContent = `${rows.length} chunks are waiting from an earlier session. Paste a card to send them.`;
    }
  } catch (e) {
    showError(`Storage error: ${e.message}`);
  }
})();

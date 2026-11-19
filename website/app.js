// Capture page wiring. Logic lives in src/.
// Flow (spec 2026-11-18): connect -> ask the board BOARD? -> ask the server for that
// board's open session -> preview always, upload only while recording.
import { Outbox, IndexedDbStore, sessionKey } from "./src/outbox.js";
import { Uploader } from "./src/uploader.js";
import { Capture } from "./src/capture.js";
import { simulatorSource, virtualBoard } from "./src/simulator.js";
import { serialLines, serialSend, SERIAL_OPTIONS } from "./src/serial.js";
import { parseLine } from "./src/jsonlines.js";
import { LineHub } from "./src/hub.js";
import { requestBoard } from "./src/board.js";
import { loadAuth, clearAuth, authHeaders } from "./src/auth.js";
import { apiError } from "./src/outcome.js";
import { renderNav } from "./src/nav.js";
import { Trace, draw, drawSeries, drawScatter } from "./src/plot.js";
import { coalesce } from "./src/coalesce.js";
import { processWindow, DEFAULT_METHOD } from "./src/dsp/pipeline.js";
import { METHODS } from "./src/dsp/demod.js";
import { describeInfo } from "./src/dsp/describe.js";
import { recordingSummary } from "./src/recstate.js";

const $ = (id) => document.getElementById(id);
const outbox = new Outbox(new IndexedDbStore());

let conn = null;      // { kind, hub, send, abort }
let board = null;     // { id, key }
let card = null;      // session from the server, token = board key
let recording = null; // { sub, done }
let uploader = null;
let trace = new Trace();
let sampleFs = 100;
let framePending = false;
let stats = { samples: 0, gaps: 0, rejected: 0 };
let up = { confirmed: 0, lastRejectedReason: null, state: "idle" };
let counts = { pending: 0, rejected: 0, otherSession: 0 };
// The last recording, for the Recording panel's status line (src/recstate.js).
let rec = { phase: "idle", label: "", key: null, confirmedAtStart: 0, savedAt: null };

const showError = (msg) => { $("error").textContent = msg; };
const auth = () => loadAuth(localStorage);

function nav() {
  renderNav($("topnav"), {
    path: location.pathname, auth: auth(),
    onLogout: () => { clearAuth(localStorage); nav(); showBoard(); },
  });
}
window.addEventListener("storage", () => { nav(); showBoard(); }); // login in another tab

// ---------- board panel ----------
let boardMsg = { text: "No board connected. Plug the board in by USB and click Connect board.", kind: "" };

function showBoard() {
  const st = $("board-status");
  st.textContent = boardMsg.text;
  st.className = "notice" + (boardMsg.kind ? " " + boardMsg.kind : "");
  const unregistered = boardMsg.state === "unregistered";
  const noSession = boardMsg.state === "no-session";
  $("board-actions").hidden = !(unregistered || noSession);
  $("register").hidden = !(unregistered && auth()?.role === "admin");
  $("to-sessions").hidden = !(unregistered || noSession);
  $("connect").disabled = !!conn || !navigator.serial;
  $("simulate").disabled = !!conn;
  $("disconnect").disabled = !conn;
  $("record").disabled = !card || !!recording;
  $("stop").disabled = !recording;
}

function setBoardMsg(text, kind = "", state = null) {
  boardMsg = { text, kind, state };
  showBoard();
}

async function checkSession() {
  if (!board) return;
  setBoardMsg(`Board ${board.id}: looking up its session…`);
  let res;
  try {
    res = await fetch("/api/board/session", {
      method: "POST",
      headers: { Authorization: `Bearer ${board.key}`, "Content-Type": "application/json" },
      body: JSON.stringify({ id: board.id }),
    });
  } catch {
    setBoardMsg(`Board ${board.id}: the server is unreachable. Is it running?`, "warn", "no-session");
    return;
  }
  if (res.status === 200) {
    const s = await res.json();
    card = { ...s, token: board.key };
    setBoardMsg(`Board ${board.id} · Session ${s.label} · ${s.patientName ?? s.patient} · ${s.encounter}`, "ok");
    startUploader();
    scheduleRefresh();
  } else if (res.status === 401) {
    card = null;
    const admin = auth()?.role === "admin";
    setBoardMsg(`Board ${board.id} is not registered.` + (admin
      ? " As an admin you can register it here."
      : " An admin must register it: log in as admin (Sessions page), then click Check again."),
    "warn", "unregistered");
  } else if (res.status === 404) {
    card = null;
    setBoardMsg(`No open session for board ${board.id}. Open one on the Sessions page, then click Check again.`,
      "warn", "no-session");
  } else {
    card = null;
    setBoardMsg(`Board ${board.id}: ${await apiError(res)}`, "warn", "no-session");
  }
}

async function registerBoard() {
  const a = auth();
  if (!board || a?.role !== "admin") return;
  showError("");
  const res = await fetch("/api/boards", {
    method: "POST",
    headers: { ...authHeaders(a), "Content-Type": "application/json" },
    body: JSON.stringify({ id: board.id, key: board.key }),
  });
  if (res.status !== 200 && res.status !== 201) {
    showError(`Could not register board ${board.id}: ${await apiError(res)}`);
    return;
  }
  await checkSession();
}

// ---------- connection ----------
async function connect(kind) {
  showError("");
  const abort = new AbortController();
  let lines;
  let send;
  if (kind === "sim") {
    const vb = virtualBoard(localStorage);
    const src = simulatorSource(vb, { signal: abort.signal });
    lines = src.lines;
    send = src.send;
  } else {
    try {
      const port = await navigator.serial.requestPort();
      await port.open(SERIAL_OPTIONS);
      lines = serialLines(port, { signal: abort.signal });
      send = (text) => serialSend(port, text);
    } catch (e) {
      showError(`Could not open serial port: ${e.message}`);
      return;
    }
  }
  const hub = new LineHub(lines);
  conn = { kind, hub, send, abort };
  trace = new Trace();
  $("simulated").hidden = kind !== "sim";
  setBoardMsg(kind === "sim" ? "Simulated board connected. Asking for its ID…" : "Board connected. Asking for its ID…");
  const ended = hub.run();
  preview(hub);
  ended.then((how) => onDisconnected(how));
  try {
    board = await requestBoard(hub, send);
  } catch (e) {
    if (conn?.hub === hub) setBoardMsg(e.message, "warn");
    return;
  }
  await checkSession();
}

async function disconnect() {
  if (recording) await stopRecording();
  conn?.abort.abort();
}

function onDisconnected(how) {
  conn = null;
  board = null;
  card = null;
  setBoardMsg(how === "disconnected" ? "The board was disconnected. Plug it back in and click Connect board."
    : "Disconnected.");
}

// The preview reads every line for the plots, recording or not.
async function preview(hub) {
  for await (const line of hub.subscribe()) {
    const r = parseLine(line);
    if (r.kind !== "sample") continue;
    trace.push(r.sample.I, r.sample.Q);
    sampleFs = r.sample.fs;
    if (!framePending) {
      framePending = true;
      requestAnimationFrame(() => { framePending = false; draw($("plot"), trace); drawProcessed(); });
    }
  }
}

// ---------- recording ----------
function startUploader() {
  if (uploader) uploader.resume(card);
  else {
    uploader = new Uploader({ outbox, fetchFn: (...a) => fetch(...a), card, onStatus: (s) => { up = s; scheduleRefresh(); } });
    uploader.start();
  }
}

function record() {
  if (!conn || !card || recording) return;
  showError("");
  const sub = conn.hub.subscribe();
  rec = { phase: "recording", label: card.label, key: sessionKey(card), confirmedAtStart: up.confirmed, savedAt: null };
  const capture = new Capture({
    outbox, sessionKey: sessionKey(card), card,
    source: conn.kind === "sim" ? "SIMULATED" : "serial",
    onStatus: (st) => { stats = st; scheduleRefresh(); },
  });
  const done = capture.run(sub).then((result) => {
    if (result === "disconnected") showError("The board disconnected while recording. Recorded chunks are kept.");
    else if (result === "quota") showError("Browser storage is full. Recording stopped. Unsaved data (up to about 10 s) was lost.");
  }).catch((e) => showError(`Recording failed: ${e.message}`))
    .finally(() => { recording = null; rec.phase = "stopped"; showBoard(); scheduleRefresh(); });
  recording = { sub, done };
  showBoard();
}

async function stopRecording() {
  if (!recording) return;
  conn?.hub.unsubscribe(recording.sub);
  await recording.done;
}

// ---------- status ----------
async function refresh() {
  const key = rec.key ?? (card ? sessionKey(card) : null); // the recording's session, even after Disconnect
  if (key) {
    try { counts = await outbox.counts(key); } catch (e) { showError(`Storage error: ${e.message}`); }
  }
  if (rec.phase === "stopped" && counts.pending === 0 && !rec.savedAt) {
    rec.savedAt = new Date().toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" });
  }
  const summary = recordingSummary({
    phase: rec.phase, label: rec.label, fs: sampleFs, samples: stats.samples,
    saved: up.confirmed - rec.confirmedAtStart, pending: counts.pending, rejected: counts.rejected,
    uploader: up.state, reason: up.lastRejectedReason, savedAt: rec.savedAt,
  });
  $("rec-state").hidden = !summary;
  if (summary) {
    $("rec-state").textContent = summary.text;
    $("rec-state").className = `notice ${summary.kind}`;
  }
  $("status").textContent =
    `Samples ${stats.samples} | Chunks confirmed ${up.confirmed} | Chunks pending ${counts.pending} | ` +
    `Gaps ${stats.gaps} | Rejected lines ${stats.rejected}`;
  const notes = [];
  if (up.state === "auth") {
    notes.push("The server refused the board key: the session may have ended, or the board was registered again. Chunks stay in this browser.");
  } else if (up.state === "retry") notes.push("Server unreachable, retrying.");
  else if (up.state === "error") notes.push("Local storage error while uploading, retrying.");
  if (counts.rejected > 0) {
    notes.push(`${counts.rejected} chunks rejected by the server` +
      (up.lastRejectedReason ? `; latest reason: ${up.lastRejectedReason}` : "") + ".");
  }
  if (counts.otherSession > 0) {
    notes.push(`${counts.otherSession} chunks belong to another session. Connect that session's board to send them.`);
  }
  $("notes").textContent = notes.join(" ");
}
const scheduleRefresh = coalesce(refresh, 250);

// ---------- display ----------
for (const m of METHODS) {
  const opt = document.createElement("option");
  opt.value = m;
  opt.textContent = m === DEFAULT_METHOD ? `${m} (default)` : m;
  $("method").append(opt);
}
$("method").value = DEFAULT_METHOD;

let lastProcessed = 0;
function drawProcessed(force = false) {
  const now = performance.now();
  if (!force && now - lastProcessed < 100) return;
  lastProcessed = now;
  const out = processWindow(trace.i, trace.q, { fs: sampleFs, method: $("method").value, band: $("band").value });
  drawSeries($("wave"), [{ values: out.breath, colour: "#c2571b" }, { values: out.wave, colour: "#1b6ec2" }]);
  drawScatter($("iq"), trace.i, trace.q, out.info.used === "arctan-fit" ? out.info.circle : null);
  $("proc-info").textContent = describeInfo(out.info, $("method").value);
}

// ---------- events ----------
$("connect").addEventListener("click", () => connect("serial"));
$("simulate").addEventListener("click", () => connect("sim"));
$("disconnect").addEventListener("click", disconnect);
$("check").addEventListener("click", checkSession);
$("register").addEventListener("click", registerBoard);
$("record").addEventListener("click", record);
$("stop").addEventListener("click", stopRecording);
$("method").addEventListener("change", () => drawProcessed(true));
$("band").addEventListener("change", () => drawProcessed(true));

nav();
showBoard();
if (!navigator.serial) {
  $("connect").title = "This browser has no Web Serial. Use Chrome or Edge.";
  showError("This browser has no Web Serial. Use Chrome or Edge, or the simulated board.");
}
(async () => {
  try {
    const rows = await outbox.store.all();
    if (rows.length > 0) {
      $("notes").textContent = `${rows.length} chunks are waiting from an earlier recording. Connect that session's board to send them.`;
    }
  } catch (e) {
    showError(`Storage error: ${e.message}`);
  }
})();

window.prataLoaded = true;

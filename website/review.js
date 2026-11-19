// Review page wiring. Logic lives in src/.
import { parseRecording } from "./src/recording.js";
import { processWindow, DEFAULT_METHOD } from "./src/dsp/pipeline.js";
import { METHODS } from "./src/dsp/demod.js";
import { describeInfo } from "./src/dsp/describe.js";
import { drawSeries, drawScatter } from "./src/plot.js";
import { loadAuth, clearAuth } from "./src/auth.js";
import { renderNav } from "./src/nav.js";

const $ = (id) => document.getElementById(id);
function nav() {
  renderNav($("topnav"), { path: location.pathname, auth: loadAuth(localStorage),
    onLogout: () => { clearAuth(localStorage); nav(); } });
}
nav();
window.addEventListener("storage", nav);
const WINDOW_S = 10;
let rec = null;

const rows = Object.fromEntries(METHODS.map((m) => {
  const div = document.createElement("div");
  div.className = m === DEFAULT_METHOD ? "method default" : "method";
  const h = document.createElement("h3");
  h.textContent = m;
  const canvas = document.createElement("canvas");
  canvas.width = 1000;
  canvas.height = 120;
  canvas.className = "method-plot";
  const p = document.createElement("p");
  div.append(h, canvas, p);
  $("methods").append(div);
  return [m, { canvas, p }];
}));

function render() {
  if (!rec) return;
  const start = Number($("start").value);
  $("start-label").textContent = `${start} s`;
  const a = Math.round(start * rec.fs);
  const b = Math.min(rec.I.length, a + WINDOW_S * rec.fs);
  const I = rec.I.slice(a, b);
  const Q = rec.Q.slice(a, b);
  let circle = null;
  for (const m of METHODS) {
    const out = processWindow(I, Q, { fs: rec.fs, method: m, band: $("band").value });
    drawSeries(rows[m].canvas, [{ values: out.breath, colour: "#c2571b" }, { values: out.wave, colour: "#1b6ec2" }]);
    rows[m].p.textContent = describeInfo(out.info, m);
    if (m === DEFAULT_METHOD && out.info.used === "arctan-fit") circle = out.info.circle;
  }
  drawScatter($("iq"), I, Q, circle);
}

$("file").addEventListener("change", async () => {
  $("error").textContent = "";
  const file = $("file").files[0];
  if (!file) return;
  try {
    rec = parseRecording(await file.text());
  } catch (e) {
    rec = null;
    $("error").textContent = `Could not read ${file.name}: ${e.message}`;
    return;
  }
  const seconds = rec.I.length / rec.fs;
  const gaps = rec.I.filter((v) => !Number.isFinite(v)).length;
  $("summary").textContent = `${file.name}: ${rec.I.length} samples, ${seconds.toFixed(1)} s at ${rec.fs} Hz, ${gaps} missing.`;
  $("start").max = String(Math.max(0, Math.floor(seconds - WINDOW_S)));
  $("start").value = "0";
  $("start").disabled = false;
  render();
});
$("start").addEventListener("input", render);
$("band").addEventListener("change", render);

window.prataLoaded = true;

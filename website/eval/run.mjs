// Scores the six display methods and applies the selection rule fixed in
// docs/design/specs/2026-11-18-radar-display-processing-design.md.
// Run from the repo root: node website/eval/run.mjs
import { readFileSync, writeFileSync, mkdirSync } from "node:fs";
import { METHODS, fitCircle } from "../src/dsp/demod.js";
import { processWindow, bandSignal } from "../src/dsp/pipeline.js";
import { parseCsv } from "../src/recording.js";
import { SCENARIOS, scenario, generate, FS } from "./synth.js";

const SEEDS = [1, 2, 3, 4, 5];
const SECONDS = 60;
const WIN = 10 * FS;
const REAL = "data/rabits_Sep_15_1519.csv";
const OUT = "docs/eval/2026-11-18-radar-display-processing";

const absCorr = (a, b) => {
  const n = a.length;
  const ma = a.reduce((s, v) => s + v, 0) / n;
  const mb = b.reduce((s, v) => s + v, 0) / n;
  let sab = 0, saa = 0, sbb = 0;
  for (let k = 0; k < n; k++) {
    sab += (a[k] - ma) * (b[k] - mb);
    saa += (a[k] - ma) ** 2;
    sbb += (b[k] - mb) ** 2;
  }
  return saa > 0 && sbb > 0 ? Math.abs(sab / Math.sqrt(saa * sbb)) : 0;
};
const quantile = (x, q) => {
  const s = [...x].sort((a, b) => a - b);
  const pos = (s.length - 1) * q;
  const lo = Math.floor(pos);
  return s[lo] + (s[Math.min(lo + 1, s.length - 1)] - s[lo]) * (pos - lo);
};
const f2 = (v) => v.toFixed(2);

// ---- synthetic ----
const scores = {}; // scores[scenario][method] = { shape: [], shapeNarrow: [], breathing: [], hybridArc: n }
const timing = Object.fromEntries(METHODS.map((m) => [m, 0]));
let windowsTimed = 0;
for (const sc of SCENARIOS) {
  scores[sc.name] = Object.fromEntries(METHODS.map((m) => [m, { shape: [], shapeNarrow: [], breathing: [], arcUsed: 0 }]));
  for (const seed of SEEDS) {
    const rec = scenario(sc.name, seed, { seconds: SECONDS });
    for (let w = 0; w + WIN <= rec.I.length; w += WIN) {
      const I = rec.I.slice(w, w + WIN);
      const Q = rec.Q.slice(w, w + WIN);
      const truth = rec.truth.slice(w, w + WIN);
      const tWide = bandSignal(truth, "wide", FS);
      const tBreath = bandSignal(truth, "breathing", FS);
      windowsTimed++;
      for (const m of METHODS) {
        const t0 = performance.now();
        const wide = processWindow(I, Q, { fs: FS, method: m, band: "wide" });
        timing[m] += performance.now() - t0;
        const narrow = processWindow(I, Q, { fs: FS, method: m, band: "narrow" });
        const s = scores[sc.name][m];
        s.shape.push(absCorr(wide.wave, tWide));
        s.shapeNarrow.push(absCorr(narrow.wave, tWide));
        s.breathing.push(absCorr(wide.breath, tBreath));
        if (wide.info.used === "arctan-fit" && m === "hybrid") s.arcUsed++;
      }
    }
  }
}

const ranked = SCENARIOS.filter((s) => s.ranked).map((s) => s.name);
const med = (sc, m, k = "shape") => quantile(scores[sc][m][k], 0.5);
const overall = Object.fromEntries(METHODS.map((m) => [m, quantile(ranked.flatMap((sc) => scores[sc][m].shape), 0.5)]));

// Selection rule: highest overall median shape; disqualified if median < 0.5 in a
// scenario where another method reaches 0.8; ties within 0.02 go to the simpler one.
const disq = {};
for (const m of METHODS) {
  for (const sc of ranked) {
    const someoneGood = METHODS.some((o) => o !== m && med(sc, o) >= 0.8);
    if (someoneGood && med(sc, m) < 0.5) (disq[m] ??= []).push(sc);
  }
}
const eligible = METHODS.filter((m) => !disq[m]);
const best = Math.max(...eligible.map((m) => overall[m]));
const winner = eligible.find((m) => overall[m] >= best - 0.02); // METHODS is ordered simplest first

// ---- guard sweep: arc size between neck-small and quarter-arc (not ranked) ----
const SWEEP_MM = [0.3, 0.5, 0.7, 0.9, 1.1, 1.4, 1.8, 2.5, 3.5];
const SWEEP_METHODS = ["pca", "arctan-fit", "hybrid"];
const sweep = SWEEP_MM.map((respMm, j) => {
  const cfg = { ...SCENARIOS[0], respMm, ranked: false };
  const r = Object.fromEntries(SWEEP_METHODS.map((m) => [m, []]));
  let arcUsed = 0;
  for (const seed of SEEDS) {
    const rec = generate(cfg, 100000 + 97 * j + seed, { seconds: SECONDS });
    for (let w = 0; w + WIN <= rec.I.length; w += WIN) {
      const I = rec.I.slice(w, w + WIN);
      const Q = rec.Q.slice(w, w + WIN);
      const t = bandSignal(rec.truth.slice(w, w + WIN), "wide", FS);
      for (const m of SWEEP_METHODS) {
        const o = processWindow(I, Q, { fs: FS, method: m });
        r[m].push(absCorr(o.wave, t));
        if (m === "hybrid" && o.info.used === "arctan-fit") arcUsed++;
      }
    }
  }
  return {
    respMm, arcDeg: (4 * Math.PI * respMm / 12.5) * 180 / Math.PI, arcUsed, windows: r.hybrid.length,
    median: Object.fromEntries(SWEEP_METHODS.map((m) => [m, quantile(r[m], 0.5)])),
    hybridMin: Math.min(...r.hybrid),
  };
});

// ---- real data ----
const real = parseCsv(readFileSync(REAL, "utf8"));
const realRows = [];
for (let w = 0; w + WIN <= real.I.length; w += WIN) {
  const I = real.I.slice(w, w + WIN);
  const Q = real.Q.slice(w, w + WIN);
  const mi = I.reduce((s, v) => s + v, 0) / WIN;
  const mq = Q.reduce((s, v) => s + v, 0) / WIN;
  let a = 0, b = 0, c = 0;
  for (let k = 0; k < WIN; k++) {
    a += (I[k] - mi) ** 2;
    b += (I[k] - mi) * (Q[k] - mq);
    c += (Q[k] - mq) ** 2;
  }
  const tr = a + c;
  const disc = Math.sqrt(((a - c) / 2) ** 2 + b * b);
  const ratio = (tr / 2 + disc) / Math.max(tr / 2 - disc, 1e-30);
  const circle = fitCircle(I, Q);
  const out = Object.fromEntries(METHODS.map((m) => [m, processWindow(I, Q, { fs: FS, method: m })]));
  const agree = Object.fromEntries(METHODS.map((m) => [m, absCorr(out[m].wave, out[winner].wave)]));
  realRows.push({
    startS: w / FS,
    eigenRatio: ratio,
    radiusMv: circle.r * 1000,
    residualFrac: circle.residualSd / circle.r,
    spanDeg: circle.spanDeg,
    hybridUsed: out.hybrid.info.used,
    finite: METHODS.every((m) => out[m].wave.every(Number.isFinite)),
    agreeWithWinner: agree,
  });
}

// ---- report ----
const json = {
  generated: new Date().toISOString(),
  seeds: SEEDS, secondsPerRecord: SECONDS, windowSeconds: WIN / FS,
  overallMedianShape: overall, disqualified: disq, winner,
  perScenario: Object.fromEntries(SCENARIOS.map((sc) => [sc.name, Object.fromEntries(METHODS.map((m) => [m, {
    shapeMedian: med(sc.name, m), shapeP10: quantile(scores[sc.name][m].shape, 0.1),
    shapeNarrowMedian: med(sc.name, m, "shapeNarrow"), breathingMedian: med(sc.name, m, "breathing"),
    hybridArcWindows: scores[sc.name][m].arcUsed, windows: scores[sc.name][m].shape.length,
  }]))])),
  guardSweep: sweep,
  msPerWindow: Object.fromEntries(METHODS.map((m) => [m, timing[m] / windowsTimed])),
  real: { file: REAL, windows: realRows },
};

const lines = [];
lines.push("# Radar display processing: evaluation results", "");
lines.push(`Generated by \`node website/eval/run.mjs\` on ${json.generated}. Do not edit by hand; rerun instead.`, "");
lines.push(`Synthetic: ${SCENARIOS.length} scenarios × ${SEEDS.length} seeds × ${SECONDS} s, scored in ${WIN / FS} s windows ` +
  `(${scores[ranked[0]][METHODS[0]].shape.length} windows per scenario). Score = absolute correlation with the true displacement through the same filter.`, "");
lines.push("## Winner", "");
lines.push(`**${winner}** (overall median shape ${f2(overall[winner])}).`, "");
lines.push("| Method | Overall median shape | Disqualified in |", "|---|---|---|");
for (const m of METHODS) lines.push(`| ${m} | ${f2(overall[m])} | ${disq[m]?.join(", ") ?? ""} |`);
lines.push("", "## Shape (wide band 0.5 to 10 Hz), median [10th percentile]", "");
lines.push(`| Scenario | ${METHODS.join(" | ")} |`, `|---|${METHODS.map(() => "---").join("|")}|`);
for (const sc of SCENARIOS) {
  const tag = sc.ranked ? sc.name : `${sc.name} (what-if, not ranked)`;
  lines.push(`| ${tag} | ${METHODS.map((m) => `${f2(med(sc.name, m))} [${f2(quantile(scores[sc.name][m].shape, 0.1))}]`).join(" | ")} |`);
}
lines.push("", "## Filter: wide (0.5 to 10 Hz) against narrow (0.7 to 3 Hz), median correlation with the wide truth", "");
lines.push("| Scenario | wide | narrow |", "|---|---|---|");
for (const sc of SCENARIOS) lines.push(`| ${sc.name} | ${f2(med(sc.name, winner))} | ${f2(med(sc.name, winner, "shapeNarrow"))} |`);
lines.push("", `Method: ${winner}. The narrow band smooths the beat into one hump, so it loses the a, c and v deflections the wide truth keeps.`);
lines.push("", "## Breathing band (0.1 to 0.5 Hz), median", "");
lines.push(`| Scenario | ${METHODS.join(" | ")} |`, `|---|${METHODS.map(() => "---").join("|")}|`);
for (const sc of SCENARIOS) lines.push(`| ${sc.name} | ${METHODS.map((m) => f2(med(sc.name, m, "breathing"))).join(" | ")} |`);
lines.push("", "## Hybrid guard decisions (windows using arctan-fit, of total)", "");
lines.push("| Scenario | arctan-fit windows |", "|---|---|");
for (const sc of SCENARIOS) lines.push(`| ${sc.name} | ${scores[sc.name].hybrid.arcUsed} / ${scores[sc.name].hybrid.shape.length} |`);
lines.push("", "## Guard sweep: breathing amplitude between neck-small and quarter-arc (not ranked)", "");
lines.push("neck-small settings with only the breathing amplitude changed. Median shape, and the worst hybrid window.", "");
lines.push("| Breathing pp (mm) | Arc (°) | pca | arctan-fit | hybrid | hybrid worst | hybrid used arctan-fit |", "|---|---|---|---|---|---|---|");
for (const r of sweep) {
  lines.push(`| ${r.respMm} | ${r.arcDeg.toFixed(0)} | ${f2(r.median.pca)} | ${f2(r.median["arctan-fit"])} | ${f2(r.median.hybrid)} | ${f2(r.hybridMin)} | ${r.arcUsed} / ${r.windows} |`);
}
lines.push("", "## Cost per 10 s window (ms, this machine)", "");
lines.push(`| ${METHODS.join(" | ")} |`, `|${METHODS.map(() => "---").join("|")}|`);
lines.push(`| ${METHODS.map((m) => json.msPerWindow[m].toFixed(2)).join(" | ")} |`);
lines.push("", `## Real capture: \`${REAL}\` (no ground truth, not ranked)`, "");
lines.push(`| Window start (s) | I/Q eigenvalue ratio | Fitted radius (mV) | Residual / radius | Arc span (°) | hybrid used | All finite | ${METHODS.map((m) => `agree ${m}`).join(" | ")} |`);
lines.push(`|---|---|---|---|---|---|---|${METHODS.map(() => "---").join("|")}|`);
for (const r of realRows) {
  lines.push(`| ${r.startS} | ${r.eigenRatio.toFixed(1)} | ${r.radiusMv.toFixed(2)} | ${f2(r.residualFrac)} | ${r.spanDeg.toFixed(0)} | ${r.hybridUsed} | ${r.finite ? "yes" : "NO"} | ` +
    `${METHODS.map((m) => f2(r.agreeWithWinner[m])).join(" | ")} |`);
}
lines.push("", `"agree" is the absolute correlation of each method's wide waveform with the winner's (${winner}) on the same window.`);

mkdirSync("docs/eval", { recursive: true });
writeFileSync(`${OUT}.json`, JSON.stringify(json, null, 2) + "\n");
writeFileSync(`${OUT}.md`, lines.join("\n") + "\n");
console.log(lines.slice(0, 14).join("\n"));
console.log(`\nwinner: ${winner}\nwrote ${OUT}.md and ${OUT}.json`);

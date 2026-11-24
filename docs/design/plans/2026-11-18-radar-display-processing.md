# Radar display processing Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Turn raw radar I/Q into a displayed skin-movement waveform on `/capture/`, with six candidate methods scored on synthetic ground truth and the real RABITS capture, and the winner as default.

**Architecture:** Pure ES modules in `receiver/src/dsp/` (no build, no npm deps), used by the live page, a review page and a Node evaluation script, so scores describe what the page shows.

**Tech Stack:** Plain JS (ES modules), `node --test`, canvas.

**Spec:** `docs/.superpowers/specs/2026-11-18-radar-display-processing-design.md`

## Execution record (2026-11-18, inline, unsupervised)

All tasks done. Deviations, each kept small:
- Task 3: test and code were written in one step, so its first run was not seen failing.
- Added `receiver/src/dsp/describe.js` (the info line, tested) and `flat: true` from `demodulate`.
- Added `generate(config, rngSeed)` to `synth.js` and a guard sweep to `run.mjs`, to test the hybrid switch region.
- Hybrid guard lost its 360° cap (real chest motion can wrap); sign rule became a fixed PCA convention (no live flipping).
- Browser check: headless Chrome over CDP, scratch DB, port 8765. Simulator on `/capture/`, review page with the RABITS CSV, a server-exported Bundle and an empty Bundle. Only console error: the existing favicon 404.

## Global Constraints

- No npm dependencies, no build step; `receiver/package.json` stays `{"private":true,"type":"module"}`.
- Page copy: "Display processing only. Not a measurement result." No rate number on any page.
- Waveform shown in "relative units".
- Wavelength 12.5 mm (24 GHz); ADC 12-bit, 3.3 V, i.e. LSB 3.3/4095 V.
- Bands: wide 0.5–10 Hz, narrow 0.7–3 Hz, breathing 0.1–0.5 Hz. fs 100 Hz.
- Hybrid guard: radial residual SD < 0.15·r and arc span ≥ 30° (no upper limit).
- Do not commit: the owner stages and commits (`Local/claude.md`). Each task ends with tests green instead.

## Review Focus

1. Window with `E` gaps (NaN) from the chunker: the pipeline must fill them (linear interpolation) and never emit NaN. Test in Task 2.
2. Constant input (radar unplugged, flat line): every method returns finite zeros, no division by zero. Test in Task 2.
3. Very short window (< 2 s at start of capture): pipeline returns an empty result with `info.reason = "too-short"` instead of filter garbage. Test in Task 3.
4. Bundle with chunks out of order (search results unsorted, run guide): the loader sorts by the chunk suffix of the identifier. Test in Task 4.
5. Line-like cloud (the real RABITS case): `hybrid` must choose `pca`. Test in Task 2.

---

### Task 1: Filters

**Files:** Create `receiver/src/dsp/filters.js`; Test `receiver/tests/filters.test.js`

**Interfaces — Produces:**
- `butterBandpass(lowHz, highHz, fs, order = 4) -> Biquad[]` (order 4 → two high-pass + two low-pass sections, RBJ cookbook, Q values 0.5412 and 1.3066)
- `filtfilt(sections: Biquad[], x: number[]) -> number[]` (reflect-pad 3·(longest section count)·… use `padLen = min(n-1, 3*fs-equivalent passed in)`; signature `filtfilt(sections, x, padLen = 150)`)
- `detrend(x) -> number[]` (remove least-squares line)
- `fillGaps(x) -> number[]` (NaN → linear interpolation, edges held)

- [ ] Tests: 1.2 Hz sine passes `wide` with amplitude ratio within 0.9–1.1 and zero lag (peak cross-correlation at lag 0); 0.05 Hz sine attenuated below 0.1; 30 Hz below 0.1; `detrend` of a line returns all |v| < 1e-9; `fillGaps([1,NaN,3])` = `[1,2,3]`, `fillGaps([NaN,2])` = `[2,2]`.
- [ ] Run `node --test receiver/tests/filters.test.js`, expect FAIL (module missing).
- [ ] Implement.
- [ ] Run, expect PASS.

### Task 2: Demodulation methods

**Files:** Create `receiver/src/dsp/demod.js`; Test `receiver/tests/demod.test.js`

**Interfaces — Produces:**
- `METHODS = ["single","pca","arctan-mean","arctan-fit","dacm-fit","hybrid"]`
- `fitCircle(I, Q) -> {xc, yc, r, residualSd, spanDeg}` (Kasa algebraic fit)
- `demodulate(method, I, Q) -> {x: number[], used: string, circle?: object}`; `x` is phase in radians for arctangent methods, volts along the axis for linear ones; `used` is the method actually applied (`hybrid` reports `"arctan-fit"` or `"pca"`).

- [ ] Tests: points on a circle of radius 0.05 around (1.6,1.5), phase 0..2 rad → `fitCircle` centre within 1e-6, span ≈ 114.6°; `arctan-fit` recovers phase (corr > 0.999); `pca` on a straight-line cloud recovers the line coordinate (|corr| > 0.999); `hybrid` on short-arc noisy cloud (span 3°, noise) reports `used: "pca"`; `hybrid` on the 114° arc reports `"arctan-fit"`; constant input → every method returns finite values all equal to 0; `dacm-fit` matches `arctan-fit` up to a constant (max abs difference after removing the mean < 1e-3).
- [ ] Run, expect FAIL. Implement. Run, expect PASS.

### Task 3: Pipeline

**Files:** Create `receiver/src/dsp/pipeline.js`; Test `receiver/tests/pipeline.test.js`

**Interfaces — Consumes:** Tasks 1–2. **Produces:**
- `BANDS = {wide:[0.5,10], narrow:[0.7,3], breathing:[0.1,0.5]}`
- `processWindow(I, Q, {fs=100, method="<winner>", band="wide"}) -> {wave: number[], breath: number[], info: {used, reason?, circle?}}`; `wave` and `breath` are normalised to unit SD ("relative units"); sign flipped so that the largest absolute excursion of `wave` is positive.
- `DEFAULT_METHOD` (set to the winner after Task 5; start with `"hybrid"`).

- [ ] Tests: window of 150 samples → `wave` empty, `info.reason === "too-short"`; window with NaN gaps → all outputs finite; synthetic 1.2 Hz phase on a circle → `wave` correlates > 0.95 with the band-passed truth; output SD 1 (± 1e-6) unless all zero.
- [ ] Run, expect FAIL. Implement. Run, expect PASS.

### Task 4: Recording loader

**Files:** Create `receiver/src/recording.js`; Test `receiver/tests/recording.test.js`

**Interfaces — Produces:** `parseCsv(text) -> {fs, I, Q}` (header with `I`,`Q`,`fs` columns, as `data/rabits_*.csv`); `parseBundle(json) -> {fs, I, Q}` (raw-capture Observations, sorted by the last `-`-separated number of `identifier[0].value`, components `i-voltage`/`q-voltage`, `E` → NaN, `fs = 1000/period`); `parseRecording(text) -> {fs, I, Q}` picks by first char `{`.

- [ ] Tests: two-row CSV parses; a Bundle with chunks 1 then 0 returns chunk 0 samples first; `E` becomes NaN; `fs` from period 10 is 100.
- [ ] Run, expect FAIL. Implement. Run, expect PASS.

### Task 5: Evaluation

**Files:** Create `receiver/eval/synth.js`, `receiver/eval/run.mjs`; Test `receiver/tests/synth.test.js`; Output `docs/eval/2026-11-18-radar-display-processing.md` and `.json`.

**Interfaces — Produces:** `mulberry32(seed)`; `jvpBeat(phase01) -> number` (a, c, v Gaussians, x and y descents); `scenario(name, seed, {seconds=60, fs=100}) -> {fs, I, Q, truth}` for the six spec scenarios; `SCENARIOS` list.

- [ ] Tests: same seed → identical arrays; quantization: every I value is a multiple of 3.3/4095 (within 1e-9); `chest-large` arc span > 180°; `neck-weak` radius 8 mV.
- [ ] Run, expect FAIL. Implement. Run, expect PASS.
- [ ] `run.mjs`: 5 seeds × 6 scenarios × 10 s windows × 6 methods, metrics `shape`, `shape-narrow`, `breathing` (abs Pearson); real-data section for `data/rabits_Sep_15_1519.csv`; apply the spec's selection rule in code and print the winner. Run `node receiver/eval/run.mjs`; it writes the report.
- [ ] Set `DEFAULT_METHOD` to the winner; re-run all receiver tests.

### Task 6: Pages

**Files:** Modify `receiver/src/plot.js`, `receiver/index.html`, `receiver/app.js`; Create `receiver/review.html`, `receiver/review.js`; Test `receiver/tests/plot.test.js` (extend).

**Interfaces — Produces:** `seriesPoints(values, width, height) -> [x,y][]` (fixed ±3 SD scale for normalised data); `scatterPoints(I, Q, width, height) -> [x,y][]` (equal-aspect, centred); `drawSeries(canvas, seriesList)`, `drawScatter(canvas, I, Q)`.

- [ ] Tests: `seriesPoints` maps +3 to y=0 and −3 to y=height, clamps beyond; `scatterPoints` keeps aspect (a 1:1 square of points stays square).
- [ ] Run, expect FAIL. Implement. Run, expect PASS.
- [ ] Wire `/capture/`: processed canvas + scatter + method `<select>` (default `DEFAULT_METHOD`), recomputed on animation frame from the 10 s trace, label copy from Global Constraints.
- [ ] `review.html`: file input → `parseRecording` → window slider (10 s) → one row per method with its trace and `info.used`.
- [ ] Browser check in headless Chrome: simulator on `/capture/` shows a processed trace; review page renders the RABITS CSV with six rows; no console errors. Screenshots kept in the scratchpad.
- [ ] Full suites: `node --test "receiver/tests/*.test.js"` and `.venv/bin/python -m pytest tests -q` green.

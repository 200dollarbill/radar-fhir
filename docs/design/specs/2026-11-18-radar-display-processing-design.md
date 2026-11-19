# Radar display processing: choosing how raw I/Q becomes a waveform on the website

Date: 2026-11-18. Status: implemented 2026-11-18; result **`hybrid` with the
0.5 to 10 Hz band** (see Results). Decided by Claude without the owner (owner asked
for an unsupervised evaluation and a recommendation at the end). Every ruling below
is open to the owner's correction.

## Why

The capture page at `/capture/` plots raw I and Q voltages. A doctor cannot read
those: what they need to see is one waveform of skin movement. The firmware now
reads a real radar on G7/G8, so the website needs a defined way to turn I/Q into
that waveform, and evidence for why that way was chosen.

This is **display processing**, not a contribution and not a measurement. The
RADAR group owns signal processing (`proposal_CLAUDE.md` §3). The page only needs
a sensible, documented default so the integrated view can show something
readable. Nothing here produces a JVP value, a rate, or a finding.

## Rulings

| # | Ruling | Why | Cost if wrong |
|---|---|---|---|
| R1 | "Method" means the demodulation plus filter chain from raw I/Q to the displayed waveform | The owner's request names a method, tests and website output. The latest work is radar pins on the firmware, and the page shows only raw I/Q | The owner meant something else. The code is isolated in `receiver/src/dsp/`, so nothing else changes |
| R2 | Processing runs in the browser as plain ES modules, tested in Node, and the same code runs the evaluation | One code path for live, review and evaluation, so the scores describe what the page shows. Matches D1 of the capture spec (no build step) | Slower than numpy, which does not matter for 10 s windows |
| R3 | The waveform is shown in **relative units**, with a "display only, not a measurement" label, and no rate number | The device is uncalibrated, and the scope forbids measurement or diagnosis claims | The doctor sees shape only, which is the purpose |
| R4 | Selection rule fixed **before** running the evaluation (below) | Avoids picking the winner after seeing the numbers | None |
| R5 | No firmware change. Quantization findings are reported as advice for the RADAR group | Hardware and acquisition belong to the RADAR group | None |

## Candidate methods

Literature in `docs/papers/RADAR/md/`: P13 (24 GHz CW) uses arctangent
demodulation and a 0.7 to 3 Hz band pass. P5 (24 GHz CW, JVP) uses a 0.5 to
10 Hz band pass, which keeps 3 to 4 deflections per beat. P4 (60 GHz FMCW) uses
the arctangent phase and 0.75 to 4 Hz.

Demodulation, each applied to one window of I/Q samples:

| Id | Method | Idea |
|---|---|---|
| `single` | Single channel | The channel with the larger variance, mean removed. Baseline |
| `pca` | Linear projection | Project the centred I/Q cloud on its principal axis. Valid when the arc is short |
| `arctan-mean` | Arctangent, mean centre | `unwrap(atan2(Q - mean Q, I - mean I))`. The naive version |
| `arctan-fit` | Arctangent, fitted centre | Algebraic circle fit (Kasa) for the DC offset, then unwrapped `atan2` |
| `dacm-fit` | Extended DACM | Differentiate and cross multiply around the fitted centre, then cumulative sum |
| `hybrid` | Guarded arctangent | `arctan-fit` when the fit is trustworthy, else `pca` |

`hybrid` guard: the circle is trusted only if the radial residual spread is under
15 % of the radius **and** the arc spans at least 30°. A line-like cloud fails the
guard. That is the case seen in the real RABITS capture, where the fit puts the
centre inside the cloud and the residual spread is a large part of the radius.
(An upper limit of 360° was drafted and dropped: real chest motion can wrap more
than one turn, and the residual test already catches the bad fit.)

The sign of `pca` and `single` is arbitrary. `pca` keeps a fixed convention (the
output rises with I), so the live trace does not flip between frames, and the page
says the sign is arbitrary. (A drafted rule, "flip so the largest excursion points
up", was dropped because it flips the live trace whenever two peaks are similar.)
The scoring uses absolute correlation.

Filters, all zero phase (forward and backward biquads, reflected padding):

| Id | Band | Source |
|---|---|---|
| `wide` | 0.5 to 10 Hz | P5 (JVP waveform shape) |
| `narrow` | 0.7 to 3 Hz | P13 (heartbeat) |
| breathing | 0.1 to 0.5 Hz | shown as a second trace |

## Evaluation

**Synthetic, with ground truth** (`receiver/eval/`). Each scenario generates skin
displacement `x(t)`: breathing plus a JVP-like beat (a, c and v waves with x and
y descents as Gaussians, heart rate 60 to 80 with beat-to-beat jitter). This is
mapped to I/Q with a 24 GHz wavelength (12.5 mm), an unknown DC offset, gain,
1 mV Gaussian noise per read and 12-bit quantization at 3.3 V (the firmware's
`analogRead`). Amplitudes are peak to peak. Scenarios:

| Scenario | What it stresses |
|---|---|
| neck-small | Neck, 0.3 mm breathing, 0.1 mm beat, 40 mV arc radius |
| neck-weak | Same motion, 8 mV radius, near quantization (like the RABITS capture) |
| chest-large | 5 mm breathing (arc beyond 180°), 0.2 mm beat |
| imbalance | neck-small with 15 % gain and 8° phase imbalance |
| dc-drift | neck-small with a slow DC drift of 10 mV over the window |
| quarter-arc | 2 mm breathing, arc of about 115° |
| neck-weak-avg16 | What-if, not ranked: neck-weak if the firmware averaged 16 ADC reads per sample |

A guard sweep (not ranked) varies only the breathing amplitude of neck-small from
0.3 to 3.5 mm, to check that `hybrid` does not dip where it switches methods.

Each scenario runs 5 seeds and is cut into 10 s windows, the page's view.
Metrics per window:

- **shape**: absolute Pearson correlation of the method's `wide` output with the
  true displacement through the same `wide` filter;
- **shape-narrow**: the method's `narrow` output against the same `wide` truth, i.e.
  how much of the beat shape a narrow display keeps;
- **breathing**: the same in the breathing band.

**Selection rule (R4):** highest median `shape` over all windows. A method is
disqualified if its median `shape` is under 0.5 in any scenario where some other
method reaches 0.8. Ties within 0.02 go to the simpler method (order: `single`,
`pca`, `arctan-mean`, `arctan-fit`, `dacm-fit`, `hybrid`). The filter is chosen
by comparing `shape` (wide output against the wide truth) with `shape-narrow`, but
`wide` is kept if the difference is small, because P5 needs the beat shape.

**Real data, without ground truth:** `data/rabits_Sep_15_1519.csv` (48 s, the
RADAR group's device). Reported: I/Q geometry (eigenvalue ratio, fitted radius),
the guard decision, whether each method stays finite and bounded, and agreement
between methods. It cannot rank the methods, and is not reported as a heartbeat.

## Website

- `/capture/`: keeps the raw I/Q canvas, and adds a processed canvas with the
  `wide` waveform and the breathing trace over the last 10 s, an I/Q scatter
  (shows if the radar sees an arc or noise), and a method selector defaulting to
  the winner. Label: "Display processing only. Not a measurement result."
- `/capture/review.html`: load a recording file (firmware CSV such as
  `data/rabits_*.csv`, or a FHIR searchset Bundle saved with the run guide's curl
  command), and see every method side by side on the same window.

## Files

```
receiver/src/dsp/filters.js     biquad Butterworth, zero phase filter, detrend
receiver/src/dsp/demod.js       the six methods, circle fit, PCA
receiver/src/dsp/pipeline.js    window -> {wave, breath, info}
receiver/src/recording.js       CSV / Bundle -> {fs, I, Q}
receiver/eval/synth.js          scenario generator (seeded)
receiver/eval/run.mjs           runs the evaluation, writes results JSON + Markdown
receiver/review.html, review.js the side-by-side page
receiver/app.js, index.html, src/plot.js   processed view on /capture/
```

## Non-goals

Heart rate or JVP values, interval detection, IQ imbalance correction, motion
artefact removal with the IMU, server-side processing, firmware changes.

## Results (2026-11-18)

Full tables: `docs/eval/2026-11-18-radar-display-processing.md` (regenerate with
`node receiver/eval/run.mjs`). Scores were re-derived independently with
numpy/scipy for 8 method-window pairs and matched to 4 decimals.

| Method | Overall median shape | Fails in |
|---|---|---|
| single | 0.69 | chest-large |
| pca | 0.76 | chest-large |
| arctan-mean | 0.11 | neck-small, imbalance, dc-drift, quarter-arc |
| arctan-fit | 0.56 | dc-drift |
| dacm-fit | 0.17 | neck-small, imbalance, dc-drift |
| **hybrid** | **0.92** | none |

- Small neck motion (arc under about 30°): linear methods win (0.92); circle fits
  are unreliable (0.05 to 0.52).
- Large chest motion (arc over 180°): linear methods collapse (0.10); arctangent
  with a fitted centre reaches 0.99.
- `hybrid` matches the best method in every scenario, and in the guard sweep it
  stays within 0.01 of the better of `pca` and `arctan-fit` at every arc size.
- `wide` keeps the beat shape better than `narrow` in 5 of 6 scenarios. The
  exception is `neck-weak`, where every method is poor.
- **Weak signal is a hardware limit, not a method choice.** At an 8 mV arc radius
  (about 10 ADC levels, as in the RABITS capture) the best score is 0.42. Averaging
  16 ADC reads per sample would raise it to 0.88. That is advice for the RADAR
  group (R5), not a firmware change made here.
- Real RABITS capture: the I/Q cloud is line-like (eigenvalue ratio 7 to 23) and
  sits on a coarse quantization grid. The circle fit puts the centre inside the
  cloud (spread 31 to 41 % of the radius), so `hybrid` uses `pca` on every window.
  `single`, `pca` and `hybrid` agree (0.95 to 1.00); the arctangent methods do not
  (0.14 to 0.42). This shows the guard working on real data. It cannot show which
  method is right, and the capture is not reported as a heartbeat.

// One window of raw I/Q -> the waveform the page shows. Display processing only.
import { demodulate } from "./demod.js";
import { butterBandpass, filtfilt, detrend, fillGaps } from "./filters.js";

export const BANDS = { wide: [0.5, 10], narrow: [0.7, 3], breathing: [0.1, 0.5] };

// Chosen by website/eval/run.mjs under the selection rule in the design spec.
export const DEFAULT_METHOD = "hybrid";

const MIN_SECONDS = 2;

function unitSd(x) {
  const m = x.reduce((s, v) => s + v, 0) / (x.length || 1);
  const sd = Math.sqrt(x.reduce((s, v) => s + (v - m) ** 2, 0) / (x.length || 1));
  return sd > 0 ? x.map((v) => (v - m) / sd) : x.map(() => 0);
}

// Detrend, band-pass (zero phase) and scale to unit SD. Breathing uses 2nd-order
// edges and full-length padding, because a 10 s window holds only 1 to 5 breaths.
export function bandSignal(x, band, fs = 100) {
  const n = x.length;
  const [lo, hi] = BANDS[band];
  const d = detrend(x);
  const y = band === "breathing"
    ? filtfilt(butterBandpass(lo, hi, fs, 2), d, n - 1)
    : filtfilt(butterBandpass(lo, hi, fs), d, Math.min(n - 1, 3 * fs));
  return unitSd(y);
}

// Returns { wave, breath, info: { used, circle?, reason? } }. wave and breath are in
// relative units (unit standard deviation).
export function processWindow(I, Q, { fs = 100, method = DEFAULT_METHOD, band = "wide" } = {}) {
  const n = Math.min(I.length, Q.length);
  if (n < MIN_SECONDS * fs) return { wave: [], breath: [], info: { used: null, reason: "too-short" } };
  const d = demodulate(method, fillGaps(I.slice(0, n)), fillGaps(Q.slice(0, n)));
  return {
    wave: bandSignal(d.x, band, fs),
    breath: bandSignal(d.x, "breathing", fs),
    info: { used: d.used, circle: d.circle, flat: d.flat === true },
  };
}

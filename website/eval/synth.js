// Synthetic radar recordings with known skin displacement, for scoring the
// display methods. The model is deliberately simple and is not a physiological claim:
// it only needs a beat with several deflections (so filters that smear shape lose),
// breathing, and the I/Q imperfections the real board has.

export const FS = 100;
export const WAVELENGTH_MM = 12.5; // 24 GHz
export const LSB = 3.3 / 4095; // firmware: analogRead 12-bit, 3.3 V reference
export const NOISE_V = 0.001; // about 1.2 LSB per read, before quantization

// Amplitudes are peak to peak, in mm. radiusV is the I/Q arc radius at the ADC.
export const SCENARIOS = [
  { name: "neck-small", respMm: 0.3, beatMm: 0.1, radiusV: 0.04, ranked: true },
  { name: "neck-weak", respMm: 0.3, beatMm: 0.1, radiusV: 0.008, ranked: true },
  { name: "chest-large", respMm: 5, beatMm: 0.2, radiusV: 0.04, ranked: true },
  { name: "imbalance", respMm: 0.3, beatMm: 0.1, radiusV: 0.04, gain: 1.15, skewDeg: 8, ranked: true },
  { name: "dc-drift", respMm: 0.3, beatMm: 0.1, radiusV: 0.04, driftV: 0.01, ranked: true },
  { name: "quarter-arc", respMm: 2, beatMm: 0.1, radiusV: 0.04, ranked: true },
  // What-if, not ranked: neck-weak if the firmware averaged 16 ADC reads per sample.
  { name: "neck-weak-avg16", respMm: 0.3, beatMm: 0.1, radiusV: 0.008, avg: 16, ranked: false },
];

export function mulberry32(seed) {
  let a = seed >>> 0;
  return () => {
    a = (a + 0x6d2b79f5) >>> 0;
    let t = a;
    t = Math.imul(t ^ (t >>> 15), t | 1);
    t ^= t + Math.imul(t ^ (t >>> 7), t | 61);
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

function gaussian(rnd) {
  const u = Math.max(rnd(), 1e-12);
  return Math.sqrt(-2 * Math.log(u)) * Math.cos(2 * Math.PI * rnd());
}

// Venous-pulse-like beat over one cycle, p in [0, 1): a and c waves, x descent,
// v wave, y descent. Gaussians on the circle so consecutive beats join smoothly.
const WAVES = [
  { mu: 0.08, sd: 0.04, amp: 1.0 }, // a
  { mu: 0.2, sd: 0.025, amp: 0.4 }, // c
  { mu: 0.32, sd: 0.06, amp: -0.6 }, // x descent
  { mu: 0.55, sd: 0.06, amp: 0.7 }, // v
  { mu: 0.7, sd: 0.07, amp: -0.5 }, // y descent
];
const BEAT_PP = 1.6;

export function jvpBeat(p) {
  let y = 0;
  for (const w of WAVES) {
    let d = Math.abs(p - w.mu);
    d = Math.min(d, 1 - d);
    y += w.amp * Math.exp(-0.5 * (d / w.sd) ** 2);
  }
  return y;
}

const quantize = (v) => Math.min(4095, Math.max(0, Math.round(v / LSB))) * LSB;

// Returns { fs, I, Q, truth } where truth is the displacement in mm.
export function scenario(name, seed, opts = {}) {
  const idx = SCENARIOS.findIndex((s) => s.name === name);
  if (idx < 0) throw new Error(`unknown scenario: ${name}`);
  return generate(SCENARIOS[idx], seed * 7919 + idx, opts);
}

// Any configuration shaped like a SCENARIOS entry; rngSeed fixes every random draw.
export function generate(config, rngSeed, { seconds = 60, fs = FS } = {}) {
  const cfg = { gain: 1, skewDeg: 0, driftV: 0, avg: 1, ...config };
  const rnd = mulberry32(rngSeed);
  const n = Math.round(seconds * fs);

  const rr0 = 60 / (60 + 20 * rnd()); // 60 to 80 per minute
  const fb = 0.2 + 0.13 * rnd(); // 12 to 20 breaths per minute
  const phb = 2 * Math.PI * rnd();
  const theta0 = 2 * Math.PI * rnd();
  const dcI = 1.5 + 0.1 * rnd();
  const dcQ = 1.5 + 0.1 * rnd();
  const driftPh = [2 * Math.PI * rnd(), 2 * Math.PI * rnd()];
  const skew = (cfg.skewDeg * Math.PI) / 180;

  // beat boundaries with 3 % beat-to-beat jitter
  const starts = [-rr0 * rnd()];
  while (starts[starts.length - 1] < seconds + 2) {
    starts.push(starts[starts.length - 1] + rr0 * (1 + 0.03 * gaussian(rnd)));
  }

  const I = new Array(n);
  const Q = new Array(n);
  const truth = new Array(n);
  let b = 0;
  for (let k = 0; k < n; k++) {
    const t = k / fs;
    while (starts[b + 1] <= t) b++;
    const p = (t - starts[b]) / (starts[b + 1] - starts[b]);
    const resp = (cfg.respMm / 2) * Math.sin(2 * Math.PI * fb * t + phb) * (1 + 0.1 * Math.sin(2 * Math.PI * 0.03 * t));
    const x = resp + (cfg.beatMm / BEAT_PP) * jvpBeat(p);
    truth[k] = x;
    const phi = (4 * Math.PI * x) / WAVELENGTH_MM + theta0;
    const di = cfg.driftV * Math.sin(2 * Math.PI * 0.03 * t + driftPh[0]);
    const dq = cfg.driftV * Math.sin(2 * Math.PI * 0.03 * t + driftPh[1]);
    const ci = dcI + di + cfg.radiusV * Math.cos(phi);
    const cq = dcQ + dq + cfg.radiusV * cfg.gain * Math.sin(phi + skew);
    let si = 0;
    let sq = 0;
    for (let r = 0; r < cfg.avg; r++) {
      si += quantize(ci + NOISE_V * gaussian(rnd));
      sq += quantize(cq + NOISE_V * gaussian(rnd));
    }
    I[k] = si / cfg.avg;
    Q[k] = sq / cfg.avg;
  }
  return { fs, I, Q, truth };
}

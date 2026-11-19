// Small filter toolkit for display processing. No dependencies.
// Butterworth sections follow the RBJ audio cookbook; filtfilt runs them forward
// and backward, so the displayed waveform has no time shift.

const BUTTER4_Q = [0.5411961, 1.3065630]; // 4th-order Butterworth as two 2nd-order sections

function section(kind, f0, fs, q) {
  const w0 = (2 * Math.PI * f0) / fs;
  const cos = Math.cos(w0);
  const alpha = Math.sin(w0) / (2 * q);
  const a0 = 1 + alpha;
  const b = kind === "low"
    ? [(1 - cos) / 2, 1 - cos, (1 - cos) / 2]
    : [(1 + cos) / 2, -(1 + cos), (1 + cos) / 2];
  return { b0: b[0] / a0, b1: b[1] / a0, b2: b[2] / a0, a1: (-2 * cos) / a0, a2: (1 - alpha) / a0 };
}

// order 2 or 4 per edge. Returns high-pass then low-pass sections.
export function butterBandpass(lowHz, highHz, fs, order = 4) {
  const qs = order === 2 ? [Math.SQRT1_2] : BUTTER4_Q;
  return [...qs.map((q) => section("high", lowHz, fs, q)), ...qs.map((q) => section("low", highHz, fs, q))];
}

// One pass through every section (transposed direct form II), with each section
// started in its steady state for the first input value, as scipy's lfilter_zi does.
function pass(sections, x) {
  let y = x;
  for (const s of sections) {
    const out = new Array(y.length);
    const u = y[0];
    const dc = (s.b0 + s.b1 + s.b2) / (1 + s.a1 + s.a2);
    const yss = dc * u;
    let z2 = s.b2 * u - s.a2 * yss;
    let z1 = s.b1 * u - s.a1 * yss + z2;
    for (let n = 0; n < y.length; n++) {
      const xn = y[n];
      const yn = s.b0 * xn + z1;
      z1 = s.b1 * xn - s.a1 * yn + z2;
      z2 = s.b2 * xn - s.a2 * yn;
      out[n] = yn;
    }
    y = out;
  }
  return y;
}

// Zero-phase filter with odd reflection padding at both ends.
export function filtfilt(sections, x, padLen = 150) {
  const n = x.length;
  if (n === 0) return [];
  const p = Math.max(0, Math.min(padLen, n - 1));
  const ext = new Array(n + 2 * p);
  for (let k = 0; k < p; k++) ext[k] = 2 * x[0] - x[p - k];
  for (let k = 0; k < n; k++) ext[p + k] = x[k];
  for (let k = 0; k < p; k++) ext[p + n + k] = 2 * x[n - 1] - x[n - 2 - k];
  const fwd = pass(sections, ext);
  const back = pass(sections, fwd.reverse()).reverse();
  return back.slice(p, p + n);
}

// Remove the least-squares straight line.
export function detrend(x) {
  const n = x.length;
  if (n < 2) return x.map(() => 0);
  const tm = (n - 1) / 2;
  let xm = 0;
  for (const v of x) xm += v;
  xm /= n;
  let num = 0;
  let den = 0;
  for (let k = 0; k < n; k++) {
    num += (k - tm) * (x[k] - xm);
    den += (k - tm) ** 2;
  }
  const slope = num / den;
  return x.map((v, k) => v - xm - slope * (k - tm));
}

// Missing samples (NaN, the chunker's E) become a straight line between neighbours.
export function fillGaps(x) {
  const out = x.slice();
  const known = [];
  for (let k = 0; k < out.length; k++) if (Number.isFinite(out[k])) known.push(k);
  if (known.length === 0) return out.map(() => 0);
  for (let k = 0; k < known[0]; k++) out[k] = out[known[0]];
  const last = known[known.length - 1];
  for (let k = last + 1; k < out.length; k++) out[k] = out[last];
  for (let j = 0; j + 1 < known.length; j++) {
    const a = known[j];
    const b = known[j + 1];
    for (let k = a + 1; k < b; k++) out[k] = out[a] + ((out[b] - out[a]) * (k - a)) / (b - a);
  }
  return out;
}

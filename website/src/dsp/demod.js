// Six ways to turn one window of radar I/Q into one movement signal.
// Display processing only: none of these outputs is a measurement.

export const METHODS = ["single", "pca", "arctan-mean", "arctan-fit", "dacm-fit", "hybrid"];

// hybrid trusts the fitted circle only when the points lie on a ring (radial
// spread under 15 % of the radius) and the ring covers at least 30 degrees.
export const GUARD = { maxResidualFrac: 0.15, minSpanDeg: 30 };

const mean = (x) => x.reduce((s, v) => s + v, 0) / (x.length || 1);

function unwrap(p) {
  const out = p.slice();
  let shift = 0;
  for (let k = 1; k < p.length; k++) {
    const d = p[k] - p[k - 1];
    if (d > Math.PI) shift -= 2 * Math.PI;
    else if (d < -Math.PI) shift += 2 * Math.PI;
    out[k] = p[k] + shift;
  }
  return out;
}

function phaseAround(I, Q, xc, yc) {
  return unwrap(I.map((v, k) => Math.atan2(Q[k] - yc, v - xc)));
}

// Kasa algebraic circle fit on mean-centred data (better conditioned).
export function fitCircle(I, Q) {
  const mi = mean(I);
  const mq = mean(Q);
  const u = I.map((v) => v - mi);
  const v = Q.map((w) => w - mq);
  let suu = 0, svv = 0, suv = 0, suz = 0, svz = 0, sz = 0;
  for (let k = 0; k < u.length; k++) {
    const z = u[k] * u[k] + v[k] * v[k];
    suu += u[k] * u[k];
    svv += v[k] * v[k];
    suv += u[k] * v[k];
    suz += u[k] * z;
    svz += v[k] * z;
    sz += z;
  }
  const n = u.length || 1;
  // Normal equations for [2a, 2b, c] with sum(u) = sum(v) = 0:
  //   [suu suv] [a]   [suz/2]
  //   [suv svv] [b] = [svz/2]
  const det = suu * svv - suv * suv;
  const scale = (suu + svv) ** 2;
  if (!(scale > 0) || Math.abs(det) <= 1e-12 * scale) {
    return { xc: mi, yc: mq, r: 0, residualSd: 0, spanDeg: 0, ok: false };
  }
  const a = (svv * suz / 2 - suv * svz / 2) / det;
  const b = (suu * svz / 2 - suv * suz / 2) / det;
  const r = Math.sqrt(a * a + b * b + sz / n);
  const xc = mi + a;
  const yc = mq + b;
  let ss = 0;
  for (let k = 0; k < u.length; k++) ss += (Math.hypot(I[k] - xc, Q[k] - yc) - r) ** 2;
  const ph = phaseAround(I, Q, xc, yc);
  const spanDeg = ((Math.max(...ph) - Math.min(...ph)) * 180) / Math.PI;
  return { xc, yc, r, residualSd: Math.sqrt(ss / n), spanDeg, ok: true };
}

function zeros(n) {
  return new Array(n).fill(0);
}

function single(I, Q) {
  const mi = mean(I);
  const mq = mean(Q);
  const vi = I.reduce((s, v) => s + (v - mi) ** 2, 0);
  const vq = Q.reduce((s, v) => s + (v - mq) ** 2, 0);
  if (!(vi > 0) && !(vq > 0)) return zeros(I.length);
  return vi >= vq ? I.map((v) => v - mi) : Q.map((v) => v - mq);
}

function pca(I, Q) {
  const mi = mean(I);
  const mq = mean(Q);
  let a = 0, b = 0, c = 0;
  for (let k = 0; k < I.length; k++) {
    const u = I[k] - mi;
    const v = Q[k] - mq;
    a += u * u;
    b += u * v;
    c += v * v;
  }
  if (!(a + c > 0)) return zeros(I.length);
  // Principal axis of [[a b] [b c]]. theta lies in (-90, 90] degrees, so cos >= 0: the
  // output always rises with I. A fixed convention keeps the live trace from flipping;
  // which way is "toward the radar" is unknown for this method.
  const theta = 0.5 * Math.atan2(2 * b, a - c);
  const ex = Math.cos(theta);
  const ey = Math.sin(theta);
  return I.map((v, k) => (v - mi) * ex + (Q[k] - mq) * ey);
}

function centred(x) {
  const m = mean(x);
  return x.map((v) => v - m);
}

function dacm(I, Q, xc, yc) {
  const out = zeros(I.length);
  for (let k = 1; k < I.length; k++) {
    const i0 = I[k - 1] - xc, q0 = Q[k - 1] - yc;
    const i1 = I[k] - xc, q1 = Q[k] - yc;
    const den = i1 * i1 + q1 * q1;
    // i1*(q1-q0) - q1*(i1-i0) = r^2 sin(dphi)
    out[k] = out[k - 1] + (den > 0 ? (q1 * i0 - i1 * q0) / den : 0);
  }
  return out;
}

// Returns { x, used, circle? }. x is radians for arctangent methods, volts for linear ones.
export function demodulate(method, I, Q) {
  const n = I.length;
  if (!METHODS.includes(method)) throw new Error(`unknown method: ${method}`);
  // A flat input (radar unplugged, or a window of one repeated value) has no movement.
  if (I.every((v) => v === I[0]) && Q.every((v) => v === Q[0])) {
    return { x: zeros(n), used: method === "hybrid" ? "pca" : method, flat: true };
  }
  switch (method) {
    case "single":
      return { x: single(I, Q), used: method };
    case "pca":
      return { x: pca(I, Q), used: method };
    case "arctan-mean":
      return { x: centred(phaseAround(I, Q, mean(I), mean(Q))), used: method };
    case "arctan-fit":
    case "dacm-fit": {
      const circle = fitCircle(I, Q);
      if (!circle.ok) return { x: zeros(n), used: method, circle };
      const x = method === "arctan-fit"
        ? phaseAround(I, Q, circle.xc, circle.yc)
        : dacm(I, Q, circle.xc, circle.yc);
      return { x: centred(x), used: method, circle };
    }
    case "hybrid": {
      const circle = fitCircle(I, Q);
      const trusted = circle.ok
        && circle.residualSd < GUARD.maxResidualFrac * circle.r
        && circle.spanDeg >= GUARD.minSpanDeg;
      if (trusted) return { x: centred(phaseAround(I, Q, circle.xc, circle.yc)), used: "arctan-fit", circle };
      return { x: pca(I, Q), used: "pca", circle };
    }
    default:
      throw new Error(`unknown method: ${method}`);
  }
}

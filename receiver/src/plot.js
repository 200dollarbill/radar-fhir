// Rolling trace of the I and Q voltages. Pure maths in Trace; draw() only paints.

export class Trace {
  constructor(capacity = 1000) {
    this.capacity = capacity;
    this.i = [];
    this.q = [];
  }

  push(i, q) {
    this.i.push(i);
    this.q.push(q);
    if (this.i.length > this.capacity) {
      this.i.shift();
      this.q.shift();
    }
  }

  // Each series is scaled to its own range, so the shape is visible at any offset.
  points(width, height) {
    return { i: scale(this.i, this.capacity, width, height), q: scale(this.q, this.capacity, width, height) };
  }
}

function scale(values, capacity, width, height) {
  if (values.length === 0) return [];
  const lo = Math.min(...values);
  const hi = Math.max(...values);
  const span = hi - lo;
  const step = capacity > 1 ? width / (capacity - 1) : 0;
  return values.map((v, n) => {
    const frac = span > 0 ? (v - lo) / span : 0.5; // constant signal: draw mid-height
    return [n * step, height - frac * height];
  });
}

export function draw(canvas, trace) {
  const ctx = canvas.getContext("2d");
  const { width, height } = canvas;
  ctx.clearRect(0, 0, width, height);
  const p = trace.points(width, height);
  for (const [pts, colour] of [[p.i, "#1b6ec2"], [p.q, "#c2571b"]]) {
    ctx.strokeStyle = colour;
    ctx.beginPath();
    pts.forEach(([x, y], n) => (n === 0 ? ctx.moveTo(x, y) : ctx.lineTo(x, y)));
    ctx.stroke();
  }
}

// Processed waveforms are in relative units (unit SD), so a fixed scale of +-3 SD
// keeps the trace steady between frames instead of rescaling on every redraw.
const SERIES_SD = 3;

export function seriesPoints(values, width, height) {
  if (values.length === 0) return [];
  const step = values.length > 1 ? width / (values.length - 1) : 0;
  return values.map((v, n) => {
    const y = height / 2 - (v / SERIES_SD) * (height / 2);
    return [n * step, Math.min(height, Math.max(0, y))];
  });
}

// I/Q plane with equal scale on both axes, centred on the mean, Q upward.
export function scatterTransform(I, Q, width, height) {
  let si = 0, sq = 0, n = 0;
  for (let k = 0; k < I.length; k++) {
    if (Number.isFinite(I[k]) && Number.isFinite(Q[k])) { si += I[k]; sq += Q[k]; n++; }
  }
  const mi = n ? si / n : 0;
  const mq = n ? sq / n : 0;
  let reach = 0;
  for (let k = 0; k < I.length; k++) {
    if (Number.isFinite(I[k]) && Number.isFinite(Q[k])) {
      reach = Math.max(reach, Math.abs(I[k] - mi), Math.abs(Q[k] - mq));
    }
  }
  const scale = reach > 0 ? (0.45 * Math.min(width, height)) / reach : 0;
  return {
    scale,
    map: (i, q) => [width / 2 + (i - mi) * scale, height / 2 - (q - mq) * scale],
  };
}

function line(ctx, pts, colour) {
  ctx.strokeStyle = colour;
  ctx.beginPath();
  pts.forEach(([x, y], n) => (n === 0 ? ctx.moveTo(x, y) : ctx.lineTo(x, y)));
  ctx.stroke();
}

// series: [{ values, colour }]
export function drawSeries(canvas, series) {
  const ctx = canvas.getContext("2d");
  const { width, height } = canvas;
  ctx.clearRect(0, 0, width, height);
  ctx.strokeStyle = "#ccc";
  ctx.beginPath();
  ctx.moveTo(0, height / 2);
  ctx.lineTo(width, height / 2);
  ctx.stroke();
  for (const s of series) line(ctx, seriesPoints(s.values, width, height), s.colour);
}

// circle: the fitted circle to outline, only when the method used it.
export function drawScatter(canvas, I, Q, circle = null) {
  const ctx = canvas.getContext("2d");
  const { width, height } = canvas;
  ctx.clearRect(0, 0, width, height);
  const t = scatterTransform(I, Q, width, height);
  ctx.fillStyle = "rgba(27, 110, 194, 0.35)";
  for (let k = 0; k < I.length; k++) {
    if (!Number.isFinite(I[k]) || !Number.isFinite(Q[k])) continue;
    const [x, y] = t.map(I[k], Q[k]);
    ctx.fillRect(x - 1, y - 1, 2, 2);
  }
  if (circle && circle.r > 0 && t.scale > 0) {
    const [cx, cy] = t.map(circle.xc, circle.yc);
    ctx.strokeStyle = "#c2571b";
    ctx.beginPath();
    ctx.arc(cx, cy, circle.r * t.scale, 0, 2 * Math.PI);
    ctx.stroke();
  }
}

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

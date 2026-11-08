// Parse the newline-delimited JSON the radar_json firmware prints on serial.
// Plain ES module: runs unchanged in the browser and in Node.

export const FIELDS = [
  "epoch_id", "sample_idx", "t_host_unix", "fs", "crc_ok", "missed",
  "I", "Q", "ax", "ay", "az", "gx", "gy", "gz",
];
const INT_FIELDS = ["epoch_id", "sample_idx", "fs", "missed"];
const NUM_FIELDS = ["t_host_unix", "I", "Q", "ax", "ay", "az", "gx", "gy", "gz"];

const MAX_LINE = 4096;

const rejected = (reason) => ({ kind: "rejected", reason });

export function parseLine(line) {
  const text = String(line).trim();
  if (!text.startsWith("{")) return { kind: "ignored" };
  let p;
  try {
    p = JSON.parse(text);
  } catch {
    return rejected("invalid JSON");
  }
  if (p === null || typeof p !== "object" || Array.isArray(p)) {
    return rejected("packet must be a JSON object");
  }
  for (const f of FIELDS) {
    if (!(f in p)) return rejected(`missing field ${f}`);
  }
  for (const f of INT_FIELDS) {
    if (!Number.isInteger(p[f])) return rejected(`field ${f} must be an integer`);
  }
  if (typeof p.crc_ok !== "boolean") return rejected("field crc_ok must be boolean");
  for (const f of NUM_FIELDS) {
    if (typeof p[f] !== "number" || !Number.isFinite(p[f])) {
      return rejected(`field ${f} must be a finite number`);
    }
  }
  if (p.sample_idx < 0) return rejected("sample_idx must be >= 0");
  if (p.fs <= 0) return rejected("fs must be > 0");
  if (!p.crc_ok) return rejected("crc_ok is false");
  return {
    kind: "sample",
    sample: {
      sampleIdx: p.sample_idx, fs: p.fs, missed: p.missed,
      I: p.I, Q: p.Q, ax: p.ax, ay: p.ay, az: p.az, gx: p.gx, gy: p.gy, gz: p.gz,
    },
  };
}

// Reassembles lines from arbitrary text chunks (serial reads split anywhere).
export class LineSplitter {
  constructor() {
    this.buf = "";
  }

  push(text) {
    this.buf += text;
    const parts = this.buf.split("\n");
    this.buf = parts.pop();
    const out = parts.map((l) => (l.endsWith("\r") ? l.slice(0, -1) : l));
    if (this.buf.length > MAX_LINE) {
      out.push(this.buf);
      this.buf = "";
    }
    return out;
  }
}

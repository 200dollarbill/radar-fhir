// Simulated device: yields the same lines the firmware prints.
import { FIELDS } from "./jsonlines.js";

export function formatLine(sampleIdx, fs, values) {
  const v = { missed: 0, I: 1.65, Q: 1.65, ax: 0, ay: 0, az: 1, gx: 0, gy: 0, gz: 0, ...values };
  const f6 = (x) => Number(x).toFixed(6);
  const rec = {
    epoch_id: 0, sample_idx: sampleIdx, t_host_unix: "0.000", fs, crc_ok: "true", missed: v.missed,
    I: f6(v.I), Q: f6(v.Q), ax: f6(v.ax), ay: f6(v.ay), az: f6(v.az),
    gx: f6(v.gx), gy: f6(v.gy), gz: f6(v.gz),
  };
  return "{" + FIELDS.map((k) => `"${k}":${rec[k]}`).join(",") + "}";
}

function defaultSleep(ms, signal) {
  return new Promise((resolve) => {
    const done = () => { clearTimeout(timer); signal?.removeEventListener("abort", done); resolve(); };
    const timer = setTimeout(done, ms);
    signal?.addEventListener("abort", done, { once: true });
  });
}

// Respiration sine + pulse + small noise, as phase of the I/Q vector.
function phaseAt(t) {
  const resp = 0.8 * Math.sin(2 * Math.PI * 0.25 * t);
  const pulse = 0.15 * Math.sin(2 * Math.PI * 1.2 * t);
  const noise = (Math.random() - 0.5) * 0.02;
  return resp + pulse + noise;
}

export async function* simulatorLines({ fs = 100, now = Date.now, sleep, signal } = {}) {
  const wait = sleep ?? ((ms) => defaultSleep(ms, signal));
  const start = now();
  let emitted = 0;
  while (!signal?.aborted) {
    const due = Math.floor(((now() - start) / 1000) * fs) - emitted;
    for (let n = 0; n < due; n++) {
      if (signal?.aborted) return;
      const phase = phaseAt(emitted / fs);
      yield formatLine(emitted, fs, {
        I: 1.65 + 0.4 * Math.cos(phase + 0.6),
        Q: 1.65 + 0.4 * Math.sin(phase + 0.6),
      });
      emitted++;
    }
    await wait(20);
  }
}

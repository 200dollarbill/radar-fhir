// Web Serial line source. Yields text lines until the signal aborts or the device is lost.
import { LineSplitter } from "./jsonlines.js";

export async function* serialLines(port, { baudRate = 115200, signal } = {}) {
  await port.open({ baudRate });
  const reader = port.readable.pipeThrough(new TextDecoderStream()).getReader();
  const stop = () => { reader.cancel().catch(() => {}); };
  signal?.addEventListener("abort", stop, { once: true });
  if (signal?.aborted) stop();
  const splitter = new LineSplitter();
  try {
    for (;;) {
      const { value, done } = await reader.read(); // a device-lost error propagates
      if (done) return;
      for (const line of splitter.push(value)) yield line;
    }
  } finally {
    signal?.removeEventListener("abort", stop);
    try { await reader.cancel(); } catch { /* already closed or errored */ }
    try { await port.close(); } catch { /* device may be gone */ }
  }
}

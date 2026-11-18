// Web Serial line source. The caller opens the port (so open errors can be shown);
// this yields text lines until the signal aborts or the device is lost, then closes it.
import { LineSplitter } from "./jsonlines.js";

export async function* serialLines(port, { signal } = {}) {
  const decoder = new TextDecoderStream();
  // Keep the pipe promise: the port stays locked until the pipe has finished closing.
  const piped = port.readable.pipeTo(decoder.writable).catch(() => {});
  const reader = decoder.readable.getReader();
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
    await piped; // readable is unlocked now, so close() can succeed
    try { await port.close(); } catch { /* device may be gone */ }
  }
}

// 64 KiB: the 255-byte default overruns in about 13 ms at 19 KB/s.
export const SERIAL_OPTIONS = { baudRate: 115200, bufferSize: 65536 };

// Host-to-board command, e.g. "BOARD?\n". Holds the writer only for this write.
export async function serialSend(port, text) {
  const writer = port.writable.getWriter();
  try {
    await writer.write(new TextEncoder().encode(text));
  } finally {
    writer.releaseLock();
  }
}

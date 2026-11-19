// The Recording panel's status line: is it recording, saving, saved, or stuck?
// phase: "idle" | "recording" | "stopped". saved = chunks this recording confirmed by
// the server; pending/rejected = this session's chunks still in the browser.

const chunks = (n) => `${n} chunk${n === 1 ? "" : "s"}`;
const seconds = (samples, fs) => `${Math.round(samples / (fs || 100))} s`;

export function recordingSummary({ phase, label, fs, samples, saved, pending, rejected, uploader, reason, savedAt }) {
  if (phase === "idle") return null;
  if (phase === "recording") {
    return { kind: "rec", text: `● Recording ${label}: ${seconds(samples, fs)} · ${chunks(saved)} saved so far.` };
  }
  if (samples === 0 && saved === 0 && pending === 0) {
    return { kind: "warn", text: "Nothing was recorded: no samples arrived while recording." };
  }
  if (pending > 0) {
    const kept = `${chunks(pending)} ${pending === 1 ? "is" : "are"} kept in this browser.`;
    if (uploader === "retry" || uploader === "error") {
      return { kind: "warn", text: `Not saved yet: the server is unreachable, retrying. ${kept}` };
    }
    if (uploader === "auth") {
      return { kind: "warn", text: `Not saved: the server refused the board key (session ended?). ${kept}` };
    }
    return { kind: "busy", text: `Saving ${label}: ${chunks(pending)} left to upload…` };
  }
  if (rejected > 0) {
    return { kind: "warn",
      text: `Saved with problems: ${chunks(saved)} stored, ${rejected} rejected by the server` +
        (reason ? ` (${reason}).` : ".") };
  }
  return { kind: "ok", text: `✓ Saved: ${seconds(samples, fs)} of ${label} (${chunks(saved)}) stored on the server at ${savedAt}.` };
}

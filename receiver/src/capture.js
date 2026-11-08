// Capture controller: serial/simulated lines -> samples -> chunks -> outbox.
// Stop is done by the caller ending the line source.
import { parseLine } from "./jsonlines.js";
import { Chunker } from "./chunker.js";
import { buildObservation, identifierValue } from "./observation.js";

const MAX_FILL = 999; // mirrors Chunker: a larger gap starts a new segment

const isQuota = (e) => e?.name === "QuotaExceededError";

export class Capture {
  constructor({ outbox, sessionKey, card, source, onSample, onStatus, newId = () => "cap-" + crypto.randomUUID() }) {
    Object.assign(this, { outbox, sessionKey, card, source, onSample, onStatus, newId });
    this.stats = { samples: 0, gaps: 0, rejected: 0 };
  }

  _emit() {
    this.onStatus?.({ ...this.stats });
  }

  async run(lines) {
    const captureId = this.newId();
    this.stats = { samples: 0, gaps: 0, rejected: 0 };
    let failure = null; // always an Error once set, never falsy
    let chain = Promise.resolve();
    const chunker = new Chunker({
      onChunk: (chunk) => {
        chain = chain.then(async () => {
          if (failure) return;
          try {
            await this.outbox.add({
              identifier: identifierValue(captureId, chunk),
              sessionKey: this.sessionKey,
              observation: buildObservation(chunk, this.card, { captureId, source: this.source }),
            });
          } catch (e) {
            failure = e ?? new Error("outbox write failed");
          }
        });
      },
    });

    let result = "ended";
    let lastIdx = null;
    let lastFs = null;
    let procError = null;
    let finished = false;
    const it = lines[Symbol.asyncIterator]();
    // Only a failure of the line source itself counts as a disconnect.
    for (;;) {
      let step;
      try {
        step = await it.next();
      } catch {
        result = "disconnected";
        finished = true;
        break;
      }
      if (step.done) { finished = true; break; }
      try {
        const r = parseLine(step.value);
        if (r.kind === "sample") {
          const s = r.sample;
          if (lastIdx !== null && s.fs === lastFs) {
            const gap = s.sampleIdx - lastIdx - 1;
            if (gap > 0 && gap <= MAX_FILL) this.stats.gaps += gap;
          }
          lastIdx = s.sampleIdx;
          lastFs = s.fs;
          this.stats.samples += 1;
          chunker.addSample(s);
          this.onSample?.(s);
          this._emit();
        } else if (r.kind === "rejected") {
          this.stats.rejected += 1;
          chunker.noteRejected();
          this._emit();
        }
      } catch (e) {
        procError = e;
        break;
      }
      if (failure) break;
    }
    if (!finished) {
      try { await it.return?.(); } catch { /* source cleanup failure is not actionable */ }
    }
    if (!failure) chunker.flush();
    await chain;
    if (procError) throw procError;
    if (failure) {
      if (isQuota(failure)) return "quota";
      throw failure;
    }
    return result;
  }
}

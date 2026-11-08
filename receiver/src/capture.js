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
    let failure = null;
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
            failure = e;
          }
        });
      },
    });

    let result = "ended";
    let lastIdx = null;
    let lastFs = null;
    try {
      for await (const line of lines) {
        const r = parseLine(line);
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
        if (failure) break;
      }
    } catch {
      result = "disconnected";
    }
    if (!failure) chunker.flush();
    await chain;
    if (failure) {
      if (isQuota(failure)) return "quota";
      throw failure;
    }
    return result;
  }
}

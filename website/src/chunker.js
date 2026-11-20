// Group samples into chunks of at most chunkSize entries per channel.
// A gap inside a chunk is filled with "E" so the sample clock stays regular.
// Plain ES module: runs unchanged in the browser and in Node.

export const CHANNELS = ["I", "Q", "ax", "ay", "az", "gx", "gy", "gz"];
const MAX_FILL = 999; // a larger gap starts a new segment

export class Chunker {
  constructor({ chunkSize = 1000, now = Date.now, onChunk } = {}) {
    this.chunkSize = chunkSize;
    this.now = now;
    this.onChunk = onChunk;
    this.segment = 0;
    this.chunkIndex = 0;
    this.lastIdx = null;
    this.fs = null;
    this.pendingRejected = 0;
    this.deviceMissed = 0;
    this._reset();
  }

  _reset() {
    this.channels = Object.fromEntries(CHANNELS.map((c) => [c, []]));
    this.gapSamples = 0;
    this.startTimeMs = null;
  }

  noteRejected() {
    this.pendingRejected += 1;
  }

  // `remaining` = fill entries still to add before the current real sample,
  // counting the entry being added now when it is a fill.
  _begin(remaining) {
    if (this.startTimeMs === null) {
      this.startTimeMs = this.now() - remaining * (1000 / this.fs);
    }
  }

  _emitIfFull() {
    if (this.channels.I.length >= this.chunkSize) this.flush();
  }

  addSample(sample) {
    if (this.lastIdx !== null) {
      const gap = sample.sampleIdx - this.lastIdx - 1;
      if (gap < 0 || gap > MAX_FILL || sample.fs !== this.fs) {
        this.flush();
        this.segment += 1;
        this.chunkIndex = 0;
        this.lastIdx = null;
      }
    }
    this.fs = sample.fs;
    this.deviceMissed = sample.missed;
    if (this.lastIdx !== null) {
      const gap = sample.sampleIdx - this.lastIdx - 1;
      for (let i = 0; i < gap; i++) {
        this._begin(gap - i);
        for (const c of CHANNELS) this.channels[c].push("E");
        this.gapSamples += 1;
        this._emitIfFull();
      }
    }
    this._begin(0);
    for (const c of CHANNELS) this.channels[c].push(sample[c]);
    this.lastIdx = sample.sampleIdx;
    this._emitIfFull();
  }

  flush() {
    if (this.channels.I.length === 0) return;
    const chunk = {
      segment: this.segment,
      chunkIndex: this.chunkIndex,
      fs: this.fs,
      startTimeMs: this.startTimeMs,
      channels: this.channels,
      gapSamples: this.gapSamples,
      rejectedLines: this.pendingRejected,
      deviceMissed: this.deviceMissed,
    };
    this.chunkIndex += 1;
    this.pendingRejected = 0;
    this._reset();
    this.onChunk(chunk);
  }
}

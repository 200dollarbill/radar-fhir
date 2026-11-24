// Fans one line source out to several readers: the preview plot, the board
// handshake and the recording each subscribe; unsubscribing ends only that reader.

class Subscription {
  constructor(hub) {
    this.hub = hub;
    this.queue = [];
    this.waiters = [];
    this.done = false;
    this.error = null;
  }

  _push(line) {
    if (this.done) return;
    const w = this.waiters.shift();
    if (w) w.resolve({ value: line, done: false });
    else this.queue.push(line);
  }

  _end(error) {
    if (this.done) return;
    this.done = true;
    this.error = error ?? null;
    for (const w of this.waiters.splice(0)) {
      if (this.error) w.reject(this.error);
      else w.resolve({ value: undefined, done: true });
    }
  }

  next() {
    if (this.queue.length) return Promise.resolve({ value: this.queue.shift(), done: false });
    if (this.done) {
      return this.error ? Promise.reject(this.error) : Promise.resolve({ value: undefined, done: true });
    }
    return new Promise((resolve, reject) => this.waiters.push({ resolve, reject }));
  }

  return() {
    this.hub.unsubscribe(this);
    this.queue.length = 0;
    return Promise.resolve({ value: undefined, done: true });
  }

  [Symbol.asyncIterator]() { return this; }
}

export class LineHub {
  constructor(source) {
    this.source = source;
    this.subs = new Set();
    this.state = "running";
    this.error = null;
  }

  subscribe() {
    const sub = new Subscription(this);
    if (this.state === "running") this.subs.add(sub);
    else sub._end(this.error);
    return sub;
  }

  unsubscribe(sub) {
    this.subs.delete(sub);
    sub._end(null);
  }

  // Resolves "ended" when the source finishes, "disconnected" when it fails.
  async run() {
    try {
      for await (const line of this.source) for (const s of this.subs) s._push(line);
      this.state = "ended";
      for (const s of this.subs) s._end(null);
      return "ended";
    } catch (e) {
      this.state = "failed";
      this.error = e ?? new Error("line source failed");
      for (const s of this.subs) s._end(this.error);
      return "disconnected";
    } finally {
      this.subs.clear();
    }
  }
}

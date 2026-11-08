// Sends outbox records one at a time. A record is deleted only after 200 or 201.

import { sessionKey } from "./outbox.js";

const BACKOFF_MS = [1000, 2000, 4000, 8000, 16000, 30000];
const IDLE_MS = 500;

export class Uploader {
  constructor({ outbox, fetchFn, card, sleep, onStatus, baseUrl = "/fhir-r4/v1" }) {
    this.outbox = outbox;
    this.fetchFn = fetchFn;
    this.card = card;
    this.sleep = sleep ?? ((ms) => new Promise((r) => setTimeout(r, ms)));
    this.onStatus = onStatus ?? (() => {});
    this.baseUrl = baseUrl;
    this.confirmed = 0;
    this.lastRejectedReason = null;
    this.failures = 0;
    this.paused = false;
    this.running = false;
  }

  _status(state) {
    this.onStatus({ state, confirmed: this.confirmed, lastRejectedReason: this.lastRejectedReason });
  }

  async step() {
    if (this.paused) return "auth";
    const rec = await this.outbox.nextFor(sessionKey(this.card));
    if (!rec) { this._status("idle"); return "idle"; }
    this._status("sending");

    let res;
    try {
      res = await this.fetchFn(`${this.baseUrl}/Observation`, {
        method: "POST",
        headers: {
          Authorization: `Bearer ${this.card.token}`,
          "Content-Type": "application/fhir+json",
          Accept: "application/fhir+json",
          "If-None-Exist": `identifier=${rec.identifier}`,
        },
        body: JSON.stringify(rec.observation),
      });
    } catch {
      return await this._retry();
    }

    if (res.status === 200 || res.status === 201) {
      await this.outbox.remove(rec.id);
      this.confirmed++;
      this.failures = 0;
      this._status("sending");
      return "sent";
    }
    if (res.status === 401 || res.status === 403) {
      this.paused = true;
      this._status("auth");
      return "auth";
    }
    if (res.status >= 500) return await this._retry();

    // Other 4xx (and anything unexpected): keep the record, mark it rejected.
    const reason = await this._reason(res);
    await this.outbox.markRejected(rec.id, reason);
    this.lastRejectedReason = reason;
    this._status("sending");
    return "rejected";
  }

  async _reason(res) {
    try {
      const oo = JSON.parse(await res.text());
      const text = (oo.issue ?? []).map((i) => i?.details?.text).find((t) => typeof t === "string" && t);
      if (text) return text;
    } catch { /* fall through */ }
    return `HTTP ${res.status}`;
  }

  async _retry() {
    const delay = BACKOFF_MS[Math.min(this.failures, BACKOFF_MS.length - 1)];
    this.failures++;
    this._status("retry");
    await this.sleep(delay);
    return "retry";
  }

  start() {
    if (this.running) return;
    this.running = true;
    (async () => {
      while (this.running) {
        const r = await this.step();
        if (r === "idle" || r === "auth") await this.sleep(IDLE_MS);
      }
    })();
  }

  stop() { this.running = false; }

  resume(card) {
    this.card = card;
    this.paused = false;
    this.failures = 0;
  }
}

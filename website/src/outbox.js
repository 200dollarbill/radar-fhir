// Durable outbox: records stay until the server confirms them (see uploader.js).
// Store interface: put(record) -> id, update(record), delete(id), all() -> record[] in id order.
// Store methods may be sync or async; Outbox awaits them.

export function sessionKey(card) {
  return `${card.patient}|${card.device}`;
}

export class MemoryStore {
  constructor() { this._rows = new Map(); this._next = 1; }
  put(record) {
    const id = this._next++;
    this._rows.set(id, { ...record, id });
    return id;
  }
  update(record) { this._rows.set(record.id, { ...record }); }
  delete(id) { this._rows.delete(id); }
  all() { return [...this._rows.values()].sort((a, b) => a.id - b.id); }
}

export class IndexedDbStore {
  constructor(dbName = "prata-capture") {
    this._dbName = dbName;
    this._db = null;
  }

  async _open() {
    if (this._db) return this._db;
    this._db = await new Promise((resolve, reject) => {
      const req = indexedDB.open(this._dbName, 1);
      req.onupgradeneeded = () => req.result.createObjectStore("outbox", { keyPath: "id", autoIncrement: true });
      req.onsuccess = () => resolve(req.result);
      req.onerror = () => reject(req.error);
    });
    try { await navigator.storage?.persist?.(); } catch { /* refusal is fine */ }
    return this._db;
  }

  async _tx(mode, fn) {
    const db = await this._open();
    return new Promise((resolve, reject) => {
      const tx = db.transaction("outbox", mode);
      const req = fn(tx.objectStore("outbox"));
      tx.oncomplete = () => resolve(req.result);
      const fail = () => reject(tx.error ?? req.error ?? new Error("IndexedDB request failed"));
      tx.onerror = fail;
      tx.onabort = fail;
    });
  }

  put(record) { const { id, ...rest } = record; return this._tx("readwrite", (s) => s.add(rest)); }
  update(record) { return this._tx("readwrite", (s) => s.put(record)); }
  delete(id) { return this._tx("readwrite", (s) => s.delete(id)); }
  all() { return this._tx("readonly", (s) => s.getAll()); }
}

export class Outbox {
  constructor(store) { this.store = store; }

  async add({ identifier, sessionKey: key, observation }) {
    return await this.store.put({ identifier, sessionKey: key, observation, rejected: false, reason: null });
  }

  async nextFor(key) {
    const rows = await this.store.all();
    return rows.find((r) => r.sessionKey === key && !r.rejected) ?? null;
  }

  async remove(id) { await this.store.delete(id); }

  async markRejected(id, reason) {
    const row = (await this.store.all()).find((r) => r.id === id);
    if (!row) return;
    await this.store.update({ ...row, rejected: true, reason });
  }

  async counts(key) {
    const c = { pending: 0, rejected: 0, otherSession: 0 };
    for (const r of await this.store.all()) {
      if (r.sessionKey !== key) c.otherSession++;
      else if (r.rejected) c.rejected++;
      else c.pending++;
    }
    return c;
  }
}

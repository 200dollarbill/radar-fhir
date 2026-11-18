import test from "node:test";
import assert from "node:assert/strict";
import { login, saveAuth, loadAuth, clearAuth, decodeJwt, authHeaders } from "../src/auth.js";

const b64url = (o) => Buffer.from(JSON.stringify(o)).toString("base64url");
const jwt = (claims) => `${b64url({ alg: "HS256" })}.${b64url(claims)}.sig`;

function memStorage() {
  const m = new Map();
  return { getItem: (k) => m.get(k) ?? null, setItem: (k, v) => m.set(k, String(v)), removeItem: (k) => m.delete(k), m };
}

test("decodeJwt reads the claims", () => {
  assert.deepEqual(decodeJwt(jwt({ role: "admin", exp: 10 })), { role: "admin", exp: 10 });
  assert.equal(decodeJwt("garbage"), null);
});

test("login posts JSON and returns who is logged in", async () => {
  let seen;
  const fetchFn = async (url, init) => {
    seen = { url, init };
    return { ok: true, status: 200, json: async () => ({ access_token: jwt({ role: "doctor", ref: "Practitioner/N1", exp: 2000 }) }) };
  };
  const a = await login(fetchFn, "doctor", "pw");
  assert.equal(seen.url, "/auth/token");
  assert.equal(seen.init.headers["Content-Type"], "application/json");
  assert.deepEqual(JSON.parse(seen.init.body), { username: "doctor", password: "pw" });
  assert.deepEqual({ ...a, token: undefined }, { token: undefined, username: "doctor", role: "doctor", ref: "Practitioner/N1", expiresAt: 2000000 });
  assert.deepEqual(authHeaders(a), { Authorization: `Bearer ${a.token}` });
});

test("a failed login says so", async () => {
  await assert.rejects(login(async () => ({ ok: false, status: 401 }), "x", "y"), /wrong username or password/);
});

test("saved login is returned until it expires, then dropped", () => {
  const s = memStorage();
  const a = { token: "t", username: "admin", role: "admin", ref: null, expiresAt: 5000 };
  saveAuth(s, a);
  assert.deepEqual(loadAuth(s, 4000), a);
  assert.equal(loadAuth(s, 5000), null);
  assert.equal(s.m.size, 0);
});

test("corrupt or missing storage gives null; clearAuth removes it", () => {
  const s = memStorage();
  assert.equal(loadAuth(s, 0), null);
  s.setItem("prata-auth", "{not json");
  assert.equal(loadAuth(s, 0), null);
  saveAuth(s, { token: "t", username: "a", role: "admin", expiresAt: 9e15 });
  clearAuth(s);
  assert.equal(loadAuth(s, 0), null);
  const broken = { getItem() { throw new Error("blocked"); }, setItem() { throw new Error("blocked"); }, removeItem() {} };
  assert.equal(loadAuth(broken, 0), null);
  saveAuth(broken, { token: "t" }); // must not throw
});

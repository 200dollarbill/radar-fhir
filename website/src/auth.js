// Login shared by every page of the site: the JWT lives in sessionStorage, so
// closing the tab logs out (spec B11).

import { apiError } from "./outcome.js";

const KEY = "prata-auth";

export function decodeJwt(token) {
  try {
    const part = String(token).split(".")[1];
    const b64 = part.replace(/-/g, "+").replace(/_/g, "/");
    const text = typeof atob === "function" ? atob(b64) : Buffer.from(b64, "base64").toString();
    return JSON.parse(decodeURIComponent(escape(text)));
  } catch {
    return null;
  }
}

export async function login(fetchFn, username, password) {
  const res = await fetchFn("/auth/token", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ username, password }),
  });
  if (res.status === 401) throw new Error("Login failed: wrong username or password.");
  if (!res.ok) throw new Error(`Login failed: ${await apiError(res)}`);
  const { access_token: token } = await res.json();
  const claims = decodeJwt(token) ?? {};
  return { token, username, role: claims.role ?? null, ref: claims.ref ?? null, expiresAt: (claims.exp ?? 0) * 1000 };
}

export function saveAuth(storage, auth) {
  try { storage.setItem(KEY, JSON.stringify(auth)); } catch { /* storage blocked */ }
}

export function loadAuth(storage, now = Date.now()) {
  let auth;
  try { auth = JSON.parse(storage.getItem(KEY)); } catch { return null; }
  if (!auth || typeof auth.token !== "string" || !(auth.expiresAt > now)) {
    try { storage.removeItem(KEY); } catch { /* ignore */ }
    return null;
  }
  return auth;
}

export function clearAuth(storage) {
  try { storage.removeItem(KEY); } catch { /* ignore */ }
}

export function authHeaders(auth) {
  return { Authorization: `Bearer ${auth.token}` };
}

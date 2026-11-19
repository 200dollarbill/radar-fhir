import test from "node:test";
import assert from "node:assert/strict";
import { randomBytes } from "node:crypto";
import worker from "../src/worker.js";

const COPY = {
  403: "Account management is only available on the PRATA laptop.",
  429: "Too many login attempts. Try again in a minute.",
  503: "PRATA server is offline (laptop off or tunnel down).",
};

// Stand-ins for the Worker's bindings; they record what they receive.
function laptop(respond = () => new Response("{}", { status: 200, headers: { "Content-Type": "application/fhir+json" } })) {
  return { requests: [], async fetch(req) { this.requests.push(req); return respond(req); } };
}
function limiter(ok = true) {
  return { keys: [], async limit({ key }) { this.keys.push(key); return { success: ok }; } };
}
function env({ lap = laptop(), lim = limiter() } = {}) {
  return { LAPTOP: lap, LOGIN_LIMIT: lim };
}
const call = (req, e) => worker.fetch(req, e, {});
const login = (headers = {}) => new Request("https://prata.example.workers.dev/auth/token", {
  method: "POST", headers: { "Content-Type": "application/json", ...headers },
  body: JSON.stringify({ username: "u", password: "p" }),
});

async function assertOutcome(res, status, code) {
  assert.equal(res.status, status);
  assert.equal(res.headers.get("Content-Type"), "application/fhir+json");
  const body = await res.json();
  assert.equal(body.resourceType, "OperationOutcome");
  assert.equal(body.issue[0].severity, "error");
  assert.equal(body.issue[0].code, code);
  assert.equal(body.issue[0].details.text, COPY[status]);
}

test("admin path is refused and never forwarded", async () => {
  const e = env();
  const res = await call(new Request("https://x.dev/fhir-r4/v1/admin/accounts"), e);
  await assertOutcome(res, 403, "forbidden");
  assert.equal(e.LAPTOP.requests.length, 0);
});

test("login under the limit is forwarded, keyed by client IP", async () => {
  const e = env();
  const res = await call(login({ "CF-Connecting-IP": "203.0.113.7" }), e);
  assert.equal(res.status, 200);
  assert.deepEqual(e.LOGIN_LIMIT.keys, ["203.0.113.7"]);
  assert.equal(e.LAPTOP.requests.length, 1);
  assert.equal(e.LAPTOP.requests[0].method, "POST");
});

test("login over the limit gets 429", async () => {
  const e = env({ lim: limiter(false) });
  const res = await call(login({ "CF-Connecting-IP": "203.0.113.7" }), e);
  assert.equal(res.headers.get("Retry-After"), "60");
  await assertOutcome(res, 429, "throttled");
  assert.equal(e.LAPTOP.requests.length, 0);
});

test('login without CF-Connecting-IP is limited as "unknown"', async () => {
  const e = env();
  await call(login(), e);
  assert.deepEqual(e.LOGIN_LIMIT.keys, ["unknown"]);
});

test("only POST /auth/token is rate limited", async () => {
  const e = env();
  await call(new Request("https://x.dev/api/sessions"), e);
  await call(new Request("https://x.dev/fhir-r4/v1/metadata"), e);
  assert.deepEqual(e.LOGIN_LIMIT.keys, []);
});

test("forwarding keeps method, path, query, auth, content type and body bytes", async () => {
  const e = env();
  const bytes = new Uint8Array(randomBytes(100_000));
  await call(new Request("https://x.dev/fhir-r4/v1/Observation?x=1", {
    method: "POST",
    headers: { Authorization: "Bearer abc.def.ghi", "Content-Type": "application/fhir+json" },
    body: bytes,
  }), e);
  const got = e.LAPTOP.requests[0];
  assert.equal(got.method, "POST");
  assert.equal(got.url, "http://127.0.0.1/fhir-r4/v1/Observation?x=1");
  assert.equal(got.headers.get("Authorization"), "Bearer abc.def.ghi");
  assert.equal(got.headers.get("Content-Type"), "application/fhir+json");
  assert.deepEqual(new Uint8Array(await got.arrayBuffer()), bytes);
});

test("GET with $ in the path has no body and an unchanged URL", async () => {
  const e = env();
  await call(new Request("https://x.dev/fhir-r4/v1/Device/abc/$provision?a=1"), e);
  const got = e.LAPTOP.requests[0];
  assert.equal(got.url, "http://127.0.0.1/fhir-r4/v1/Device/abc/$provision?a=1");
  assert.equal(got.body, null);
});

test("cookies are dropped", async () => {
  const e = env();
  await call(new Request("https://x.dev/api/sessions", { headers: { Cookie: "a=b", Authorization: "Bearer t" } }), e);
  assert.equal(e.LAPTOP.requests[0].headers.get("cookie"), null);
  assert.equal(e.LAPTOP.requests[0].headers.get("Authorization"), "Bearer t");
});

test("laptop answers pass through unchanged", async () => {
  for (const status of [401, 500]) {
    const body = JSON.stringify({ resourceType: "OperationOutcome", issue: [{ severity: "error", code: "security", details: { text: `from laptop ${status}` } }] });
    const e = env({ lap: laptop(() => new Response(body, { status, headers: { "Content-Type": "application/fhir+json" } })) });
    const res = await call(new Request("https://x.dev/api/sessions"), e);
    assert.equal(res.status, status);
    assert.equal(res.headers.get("Content-Type"), "application/fhir+json");
    assert.equal(res.headers.get("X-Content-Type-Options"), "nosniff");
    assert.equal(await res.text(), body);
  }
});

test("unreachable laptop gives 503", async () => {
  const e = env({ lap: laptop(() => { throw new Error("connection refused"); }) });
  const res = await call(new Request("https://x.dev/fhir-r4/v1/metadata"), e);
  assert.equal(res.headers.get("Retry-After"), "30");
  await assertOutcome(res, 503, "transient");
});

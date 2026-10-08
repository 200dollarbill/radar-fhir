# Public Exposure via Cloudflare + Request-History Frontend — Design

**Date:** 2026-10-08
**Status:** Design approved in conversation (two sections + tunnel amendment); written spec pending user review
**Parent:** walking-skeleton spec `docs/.superpowers/specs/2026-09-29-fhir-r4-server-walking-skeleton-design.md`

## Goal

Expose the local FHIR R4 server at a public HTTPS address (reachable only by the
project owner) and provide an HTML page showing the history of GETs/POSTs with
full request bodies. Cloudflare is only the gate: DNS + Cloudflare Access +
the tunnel transport. Authorization of data remains the server's existing
JWT/device-token machinery.

## Decisions taken in brainstorming (with rationale)

| # | Decision | Rationale |
|---|---|---|
| P1 | Audience: **just the owner, remote** — no third-party credentials | Simplest security story; owner already holds tokens |
| P2 | Transport: **Cloudflare Tunnel (cloudflared)** — outbound connection from this machine, edge → Access → tunnel → nginx → 127.0.0.1. **No router port-forward** | Owner amended the topology mid-design: transmission passes through Cloudflare's connection; no home-IP exposure, no router admin |
| P3 | Frontend: **nginx-served static HTML** (`deploy/history.html`) | Owner's choice; no Worker code or KV storage; same-origin fetches, no CORS |
| P4 | Auth gate: **Cloudflare Access + existing FHIR JWT** | Access authenticates the hostname before traffic reaches nginx; FHIR JWT roles still authorize every data operation |
| P5 | History rows: **metadata + FULL request JSON bodies** (owner's explicit choice; duplicate-patient-data risk stated and accepted) | Owner wants debugging visibility; mitigations: never headers/tokens, Access-protected page, retention bounds |
| P6 | Retention: **7 days + 10 000-row cap** (whichever trips first), purged on write | Bounds PHI duplication while keeping recent debugging history |
| P7 | Audit capture lives in **FastAPI middleware**, not nginx | nginx cannot capture request bodies portably; middleware is pytest-able like the rest of the repo |
| P8 | Log-read API: **admin FHIR JWT only** at `GET /fhir-r4/v1/admin/request-log` | Reuses the existing account/role machinery; Access gates the hostname, JWT gates the data |

## Topology (amended)

```text
Owner (phone / laptop, anywhere)
   |  https
Cloudflare edge  ── Cloudflare Access (identity check: owner only)
   |                DNS (orange-cloud) + Tunnel endpoint
cloudflared (daemon on this machine, outbound connection — no open ports)
   |
nginx (127.0.0.1:8080, this machine, TLS not required locally —
       Cloudflare edge terminates TLS; nginx serves HTTP on loopback)
   ├── GET /history          → static history.html (deploy/)
   └── /                     → proxy_pass http://127.0.0.1:8000 (uvicorn)
                                |
                         FastAPI
                         ├── audit middleware → request_log table (SQLite)
                         └── existing FHIR routes / auth / validation (unchanged)
```

Note: since the tunnel terminates TLS at the Cloudflare edge and cloudflared
speaks plain HTTP to its local ingress target, nginx runs on loopback without
its own certificates. Cloudflare's origin certificate is **not** needed.

## Scope

### Included

- `fhir_server/audit.py`: middleware + repository + retention (7 days, 10 000 rows).
- `request_log` SQLite table: `id, ts, method, path, query, status, duration_ms,
  role, resource_type, body_json (nullable), body_bytes`.
- `GET /fhir-r4/v1/admin/request-log?limit=<1..500>` — admin JWT; returns rows
  newest-first with bodies (no cursor; the page shows the newest window).
- `deploy/history.html`: static page — login prompt (token kept in page memory),
  same-origin fetch to the log endpoint, newest-first table, expandable row
  shows full body as **escaped text** (no innerHTML), manual + 10 s auto refresh.
- `deploy/nginx.conf`: `/history` static root, `/` proxy to uvicorn, standard
  hardening headers (`X-Content-Type-Options`, no server-token leaking).
- `deploy/cloudflared.yml`: tunnel ingress config (hostname → 127.0.0.1:8080).
- `deploy/README.md`: walkthrough — install cloudflared/nginx, Cloudflare DNS
  record (tunnel), Access policy (owner's email only), nginx site install,
  systemd units, secrets checklist (strong admin password, no token sharing),
  verification steps.
- `fhir_server/cli.py`: `serve --host` flag (default `127.0.0.1`, unchanged).
- Tests: audit middleware, retention, redaction, admin-only log endpoint,
  history-page escaping (static assertion), nginx config syntax check.

### Excluded

- Cloudflare Workers (superseded by P3), any Cloudflare-side storage of payloads.
- Router port-forwarding (superseded by P2/tunnel).
- Response-body logging (request bodies only, per P5).
- TLS certs on nginx (edge terminates TLS).
- Logout/token revocation UI, multi-user log views, log export.
- Any change to FHIR routes, auth, validation, or firmware.
- HTTPS claims about the public URL without live verification in the owner's
  environment (see Verification).

## Request-history record

Every request that reaches FastAPI produces one row:

| Field | Source | Notes |
|---|---|---|
| `ts` | middleware, UTC `+00:00` | same instant format as resources |
| `method` / `path` / `query` | ASGI scope | raw path, not decoded twice |
| `status` | response status | including 401/403/404/500 |
| `duration_ms` | monotonic clock around call | integer |
| `role` | principal kind if resolved, else `anonymous` | resolution best-effort; never fails the request |
| `resource_type` | first path segment under `/fhir-r4/v1/` if it matches a supported type | else null |
| `body_json` | request body, up to 100 KB | **full JSON** for typical FHIR payloads; larger bodies stored as `null` with `body_bytes` recorded; non-JSON bodies stored as null |
| `body_bytes` | len of raw body | always recorded |

**Never stored:** `Authorization` header, cookies, any header at all, response
bodies. Token *values* cannot appear in rows because headers are never read into
the log; body JSON is client payload, not credentials (the `/auth/token` route's
body contains a password — that route's body is **redacted to null** as the one
exception, since login payloads are credentials).

**Retention:** after each insert, delete rows older than 7 days; if still over
10 000 rows, delete oldest until at cap. Purge failures are logged, never
fail the proxied request.

## Data flow

1. Client → Cloudflare edge (HTTPS) → Access (identity) → tunnel → nginx → uvicorn.
2. FastAPI audit middleware runs around the route: measures duration, lets the
   route produce status/body, then writes one `request_log` row (redacting
   `/auth/token` bodies), then returns the untouched route response.
3. Owner opens `https://<hostname>/history` (also Access-gated), enters their
   admin username/password → page calls `POST /auth/token` same-origin → keeps
   JWT in memory → `GET /fhir-r4/v1/admin/request-log` → renders rows.

## Error handling

- Audit write failure → `logging` warning only; the FHIR response is unaffected
  (audit is observational, never on the correctness path).
- Log endpoint without/with invalid admin JWT → existing 401/403 OperationOutcome.
- History page: failed login/fetch shows a visible error message; no console-only
  failures; token cleared from memory on logout/refresh.
- cloudflared or nginx down → requests fail at the edge with Cloudflare's own
  error page (documented in deploy README); local server keeps running.
- SQLite lock timeout on the audit insert → warning path above; the FHIR
  response itself is already committed by then.

## Testing

- **TDD** (failing test → green → commit) for every new Python unit.
- Middleware: row written with metadata/body; `/auth/token` body redacted;
  Authorization absent from row; duration/status recorded; >100 KB body →
  `body_json` null but `body_bytes` set; db failure does not break response.
- Retention: rows beyond 7 days purged; cap enforced at 10 000.
- Endpoint: non-admin JWT → 403; admin → newest-first rows; `limit` respected.
- History page: test asserts the body-render path uses text insertion (no
  `innerHTML` assignment) — static test of the shipped HTML.
- `nginx -t` syntax check for `deploy/nginx.conf` (skips with a clear message
  if nginx is absent).
- **Verification gate:** local `uvicorn` + `nginx` + curl through localhost is
  runnable here; the Cloudflare half (DNS, Access, live tunnel) must be verified
  by the owner per `deploy/README.md` — never claimed as working without it.

## Security posture (explicit)

- Edge: Cloudflare Access = identity gate (owner's account only).
- App: unchanged FHIR JWT/device-token authz = data gate.
- Secrets: audit never persists headers; login body redacted; `.env`, `*.db`
  already gitignored.
- Residual accepted risks (owner's choices): full request bodies duplicated in
  SQLite for 7 days (P5/P6); public hostname discoverable by third parties
  (mitigated by Access, not hidden).

## Deliverables layout

```text
fhir_server/audit.py            # middleware + repository + retention
fhir_server/app.py              # mount middleware
fhir_server/routes/admin.py     # + GET /admin/request-log
fhir_server/cli.py              # serve --host
deploy/history.html
deploy/nginx.conf
deploy/cloudflared.yml
deploy/README.md
tests/test_audit.py
tests/test_admin_log.py (extends test_routes or separate)
```

## Sources

- Parent spec: `docs/.superpowers/specs/2026-09-29-fhir-r4-server-walking-skeleton-design.md`
- `docs/reference/claude/fhir-security.md` (access-control error shapes)
- Brainstorming session 2026-10-08 (decisions P1–P8, tunnel amendment)

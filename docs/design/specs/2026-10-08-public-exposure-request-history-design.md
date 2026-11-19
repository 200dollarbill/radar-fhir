# Public Exposure via Cloudflare + Request-History Frontend — Design

**Date:** 2026-10-08
**Status:** Design approved in conversation (two sections + tunnel amendment +
real-time transport amendment P9–P11); written spec pending user review
**Parent:** walking-skeleton spec `docs/.superpowers/specs/2026-09-29-fhir-r4-server-walking-skeleton-design.md`

## Goal

Expose the local FHIR R4 server at a public HTTPS address (reachable only by the
project owner) and provide an HTML page showing the history of GETs/POSTs with
full request bodies. Cloudflare is only the gate: DNS + Cloudflare Access +
the tunnel transport. Authorization of data remains the server's existing
JWT/device-token machinery.

Additionally, the measurement device streams **1 Hz heart-rate readings over
one long-lived WebSocket** through the same public path: no per-message TLS
handshake, sequence numbers persisted across reboot so lost readings are
detectable, and UTC timestamps for exact time indexing.

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
| P9 | Transport (owner requirement, technically corrected): measurements flow over **one persistent WebSocket per device** — TLS at the Cloudflare edge is established **once** and reused, never re-handshaked per message; cloudflared's tunnel is likewise a single long-lived connection. A public Cloudflare hostname cannot be plain HTTP, but per-reading handshake cost is **zero** | Owner wanted "no handshake constantly" — that is what a WebSocket already provides; the change is in transport, not in removing edge security |
| P10 | WS payload: **heart-rate readings only** — `{device_id, seq, utc, bpm}` at ~1 Hz, replacing today's HTTP POST path; each message validated and stored as the same FHIR Observation | Owner chose this over raw 100 Hz I/Q telemetry (deferred); nine-step E2E flow stays intact |
| P11 | Sequence: **persisted on the device across reconnects and reboots**, monotonic (ESP32 NVS/Preferences); server records `(device_id, seq, utc)` per Observation, detects gaps/duplicates, and reconciles missing readings on reconnect | Owner's choice; a per-session index would hide gaps across reboots |

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
                               WS Upgrade headers configured on stream path
                                |
                         FastAPI
                         ├── audit middleware → request_log table (SQLite)
                         ├── GET /fhir-r4/v1/stream (WebSocket, device token)
                         └── existing FHIR routes / auth / validation (unchanged)
```

Note: since the tunnel terminates TLS at the Cloudflare edge and cloudflared
speaks plain HTTP to its local ingress target, nginx runs on loopback without
its own certificates. Cloudflare's origin certificate is **not** needed.

**Transport reality check (P9):** the device's only TLS event is the initial
`wss://` handshake at the Cloudflare edge; every subsequent reading rides the
same connection end-to-end (edge → tunnel → nginx `Upgrade` → uvicorn). nginx
must forward `Upgrade`/`Connection` headers on `/fhir-r4/v1/stream` and hold
the proxied connection open (`proxy_read_timeout` ≥ 75 s, refreshed by the
device's 1 Hz traffic). TLS at the edge cannot be removed for a Cloudflare
hostname — it costs nothing per message after the first handshake, which is
the property the owner needs.

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
- **WebSocket stream:** `GET /fhir-r4/v1/stream` — device authenticates in the
  WS handshake with the existing device bearer token (documented placement);
  message schema `{device_id, seq, utc, bpm}`; each valid message reuses the
  existing Observation validation/minting (P10) with `identifier` carrying
  `(device_id, seq)` for durable duplicate/gap tracking; server replies an
  `{ok, last_seq}` ack so the device knows what landed.
- **Gap detection:** `GET /fhir-r4/v1/admin/gaps?device=…` (admin JWT)
  reports sequence gaps derived from stored Observations.
- **Firmware change:** `arduino/radar_json/ingest.*` switches from HTTP POST
  to a WebSocket client (1 Hz); sequence counter persisted in ESP32
  Preferences/NVS so it survives reboot (P11); `configTime` supplies UTC —
  same source as today.
- **Python device client:** `device_client` gains a WS mode mirroring the
  firmware contract for tests and manual runs.
- Tests: audit middleware, retention, redaction, admin-only log endpoint,
  history-page escaping (static assertion), nginx config syntax check,
  WS handshake auth (401/403), message → Observation conversion, sequence
  gap detection + duplicate suppression, reconnect replay.

### Excluded

- Cloudflare Workers (superseded by P3), any Cloudflare-side storage of payloads.
- Router port-forwarding (superseded by P2/tunnel).
- Response-body logging (request bodies only, per P5).
- TLS certs on nginx (edge terminates TLS).
- Logout/token revocation UI, multi-user log views, log export.
- Any change to the existing HTTP FHIR routes, auth, or validation (the WS
  path reuses them internally; it adds, not modifies).
- Raw 100 Hz radar telemetry streaming (P10 defers it to a later sub-project).
- Server-side clock sync beyond UTC+00 discipline (NTP on device, `configTime`,
  is unchanged from today).
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
4. Device connects `wss://<hostname>/fhir-r4/v1/stream` once (token in the
   handshake) → sends `{device_id, seq, utc, bpm}` at 1 Hz on that one
   connection → server validates, mints the Observation, acks `{ok, last_seq}`.
   After a reconnect the device first re-sends unacked readings (`seq >
   last_seq`) so nothing is silently lost; the server suppresses duplicates by
   `(device_id, seq)`.

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
- WS handshake without/invalid device token → close before accept (equivalent
  of 401); assignment mismatch on a message → `{ok: false, error}` on the open
  socket (the socket stays up for the next reading).
- Device disconnect → nothing to clean up server-side (stateless per message);
  server keeps serving HTTP; device reconnects with exponential backoff
  (firmware) and resumes from `last_seq + 1`.

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
- WS: handshake rejects bad/missing tokens; valid token converts messages
  through the same validation path (bad bpm → error ack, not socket close);
  duplicate `seq` acked without a second Observation; out-of-order/replay
  messages stored idempotently; `last_seq` ack correct after each store.
- Firmware contract: same treatment as `test_firmware_contract.py` — the WS
  message builder's JSON is parsed in tests and compared with `device_client`.
- **Verification gate:** local `uvicorn` + `nginx` + curl/WS client through
  localhost is runnable here; the Cloudflare half (DNS, Access, live tunnel)
  must be verified by the owner per `deploy/README.md` — never claimed as
  working without it.

## Security posture (explicit)

- Edge: Cloudflare Access = identity gate (owner's account only).
- App: unchanged FHIR JWT/device-token authz = data gate.
- Secrets: audit never persists headers; login body redacted; `.env`, `*.db`
  already gitignored.
- Stream: device token required at handshake; WS upgrade path is the only
  route the device ever needs — it cannot read Patient/Encounter resources
  (existing authz unchanged); Access does not gate the device path, FHIR's own
  device-token authz does (documented in deploy README).
- Residual accepted risks (owner's choices): full request bodies duplicated in
  SQLite for 7 days (P5/P6); public hostname discoverable by third parties
  (mitigated by Access, not hidden).

## Deliverables layout

```text
fhir_server/audit.py            # middleware + repository + retention
fhir_server/app.py              # mount middleware
fhir_server/routes/admin.py     # + GET /admin/request-log
fhir_server/cli.py              # serve --host
fhir_server/stream.py           # WebSocket endpoint + ack/gap logic
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
- Brainstorming session 2026-10-09 (decisions P9–P11: WebSocket transport,
  heart-rate payload, persisted sequence; owner requirement: no per-message
  handshake, exact time indexing)

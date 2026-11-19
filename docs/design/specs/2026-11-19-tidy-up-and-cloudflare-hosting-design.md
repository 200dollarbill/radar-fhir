# Repo tidy-up and Cloudflare hosting: design

Date: 2026-11-19. Status: implemented 2026-11-19 (plan
`docs/design/plans/2026-11-19-tidy-up-and-cloudflare-hosting.md`; live check results at the
end; check 2 partial, owner board check open). Approved by the owner 2026-11-19.
Supersedes the **topology** of `2026-10-08-public-exposure-request-history-design.md`
(rulings P2, P3, P4); that spec's request history and WebSocket stream stay open.

## Why

The owner asked for two things on 2026-11-19:

1. "host this on cloudflare workers, i have an account": a public link to the website.
2. "make the source aka the current directory more human readable because currently not
   even i can deduce where things are supposed to be and how to run the server or the
   sites".

Both land in one spec because the run instructions must describe the hosted setup and the
hosting folder must land in the new layout. They are built in two phases, in order, with
every test suite green between them.

## State on 2026-11-19 (checked)

- Server 217 pytest pass; website 172 `node --test` pass.
- Server: FastAPI, `fhir.resources`, PyJWT, one SQLite file via stdlib `sqlite3`, about
  2,900 lines. Website: plain JS pages served by the server at `/capture/`; all API calls
  use relative paths (`/auth/token`, `/api/...`, `/fhir-r4/v1/...`). No page polls.
- Login hashes with PBKDF2-SHA256, 100,000 rounds.
- No top-level README. Run instructions are split over `docs/RUN-GUIDE.md`,
  `fhir_server/README.md` (partly stale: `m5stack_cores3` FQBN, "do not upload") and
  `CLAUDE.md`.
- **The GitHub repo `200dollarbill/radar-fhir` is public.** Tracked and pushed to
  `origin/master`: `.env/notes.env` (a VM login line and internal ITS addresses) and
  `PraTAVENV/` (5,423 files of a Python environment). The scraper under `.tools/scrape/`
  is gitignored, so it exists only on this disk.

## Rulings

| # | Ruling | Why |
|---|---|---|
| H1 | Two phases: **phase 1 tidy-up**, then **phase 2 hosting**. All suites pass between them | Hosting files and run docs land in the new layout once |
| H2 | **Workers Free.** The website is served by a Worker; the Python server stays on the owner's laptop | Owner: "Stay Free: site on Workers, server on laptop". Free allows 10 ms CPU per request; the PBKDF2 login and 1000-sample validation exceed it in Python. R2 being paid does not change Workers limits (pricing page, 2026-11-19) |
| H3 | The Worker reaches the laptop through **Workers VPC** (a VPC Service on a Cloudflare Tunnel to `127.0.0.1:8000`). No domain; the laptop has no public address | Owner chose approach A. Workers VPC is beta and free on all plans (docs, 2026-11-19). Fallback if it misbehaves: a public tunnel hostname, which needs a domain |
| H4 | Anyone with the link may open the site; **only accounts the owner creates can log in**. Test and simulated data only | Owner: "Anyone with the link", then "i create each account" |
| H5 | Account management (`/fhir-r4/v1/admin/*`) is **not reachable from the public site**; accounts are made with laptop CLI commands | Accounts are only ever made by the owner, so the public side does not need the route |
| H6 | Login rate limit in the Worker: 10 tries per 60 s per client IP | The login faces the internet; FastAPI sees every request as coming from `cloudflared`, so only the Worker knows the client IP |
| H7 | The site is online exactly while `make server` and `make tunnel` run. No boot services | The laptop is never exposed without the owner knowing |
| H8 | This spec supersedes the 2026-10-08 topology (tunnel to nginx behind Cloudflare Access) | See contradictions below |
| H9 | Folders renamed by role; the Python package `fhir_server` keeps its name | Owner chose "Rename by role". Keeping the package name means no import changes |
| H10 | Historical specs, plans and the 2026-11-18 handover are **not rewritten**; the README maps old paths to new | They are records of what was true when written |
| H11 | Claude stages and commits its own work; **never pushes without asking** | Owner: "you can actually commit it when you want". The repo is public |

## Contradictions, recorded verbatim, and rulings

| Source A | Source B | Ruling |
|---|---|---|
| 2026-10-08 spec, Excluded: "Cloudflare Workers (superseded by P3)" | Owner 2026-11-19: "i want you to host this on cloudflare workers" | B wins (H2, H8): newer, explicit owner instruction. The tunnel survives as the Worker's path to the laptop |
| `CLAUDE.md`: "SATUSEHAT-compatible ... while running entirely locally" | Hosting puts the website and the request path on Cloudflare | Data is still **stored** only on the laptop. Phase 2 rewrites the sentence: "data stored only on the owner's laptop; the public site is a Cloudflare Worker that forwards requests to it; never calls the hosted SATUSEHAT platform" |
| `Local/claude.md`: "Do not automatically commit and stage the folders. I will do it myself." and handover: "Do not commit." | Owner 2026-11-19: "you can actually commit it when you want" | B wins (H11). `CLAUDE.md` and `Local/claude.md` updated the same day |
| Owner, plan question: "Paid ($5/month) is fine" | Owner, next message: "im actually on free tier, but im on R2 paid" | The correction wins: Workers Free (H2) |

## Phase 1: tidy-up

### Target layout

```
PRATA/
├── README.md        START HERE: what this is, folder map, how to run
├── Makefile         make help (default) and the commands below
├── fhir_server/     the server (Python, FastAPI)           unchanged
├── website/         Sessions, Capture, Review pages        was receiver/
├── firmware/        radar_json/ sketch for the AtomS3R     was arduino/
├── hosting/         Cloudflare Worker (phase 2)            new
├── device_client/   Python stand-in for the board (tests)  unchanged
├── tests/           server tests                           unchanged
├── tools/scrape/    reference scraper, now in git          was .tools/scrape/ (ignored)
├── data/            sample CSVs and the local databases    databases moved in
├── docs/
│   ├── RUN-GUIDE.md full walkthrough
│   ├── design/      specs/, plans/, reports/               was docs/.superpowers/ etc.
│   └── (thesis folders, reference/, eval/, handover/ unchanged)
├── Local/           owner's notes; apk/ moved in (gitignored)
└── CLAUDE.md, proposal_CLAUDE.md   instructions for Claude
```

### Moves

Plain moves; every reference in code, tests, `Makefile`, `README.md`, `RUN-GUIDE.md`,
`fhir_server/README.md`, `firmware/radar_json/README.md`, `website/eval/run.mjs`, `CLAUDE.md`
and `proposal_CLAUDE.md` is updated.

| From | To | References to update |
|---|---|---|
| `receiver/` | `website/` | `fhir_server/app.py` (`RECEIVER_DIR`), `tests/test_capture_e2e.py` (fixture path), `website/eval/run.mjs` (comment and generated text) |
| `arduino/radar_json/` | `firmware/radar_json/` | `tests/firmware/*.cpp` includes, `tests/test_firmware_contract.py`, `.gitignore` (`config.h`). The sketch folder keeps its name: Arduino requires it to match `radar_json.ino` |
| `docs/.superpowers/specs/`, `plans/` | `docs/design/specs/`, `plans/` | `CLAUDE.md` names `docs/design/specs/` as the spec location from now on |
| `.superpowers/sdd/` | `docs/design/reports/` | Untracked today, so this publishes it: scanned 2026-11-19 for JWTs, 64-hex keys and quoted passwords, none found; rescan at the move |
| `docs/implementation/` (one old action plan) | `docs/design/plans/` | |
| `.tools/scrape/` and the `tools/scrape` symlink | `tools/scrape/` (real folder, tracked) | `.gitignore`; `CLAUDE.md` commands. The scripts find the repo root as `parents[2]`, the same depth as before |
| `fhir_server.db`, `fhir_server.backup-20261118.db` | `data/` | Default `FHIR_DB_PATH` in `fhir_server/config.py` and `fhir_server/cli.py` becomes `data/fhir_server.db`, with a test. Moved only while the server is stopped |
| `apk/` | `Local/apk/` | Still gitignored (`apk/` matches at any depth) |

The website keeps its address `/capture/`.

### Removed

- `python_receiver/`: the September prototype, replaced by `fhir_server/` and the website.
  It stays in git history.
- `PraTAVENV/`: an old Python environment; `.venv/` is the one in use. Deleted locally
  and from the index.
- `docs/learning (Copy)/`: identical to `docs/learning/` (checked with `diff -rq`).
- From the index only (kept on disk, gitignored): `prata_fhir_server.egg-info/`
  (regenerated by `pip install -e .`) and `.env/notes.env`.

`.gitignore` gains `*.egg-info/`, `.pytest_cache/`, `node_modules/`, `.wrangler/` and
`hosting/public/`, and loses `.tools/` and `tools/`.

### New files

- **`README.md`**: what PRATA is (two lines, linking the thesis goal); folder map; quick
  start; local versus hosted; where secrets live (`.env/prata.env`, never committed);
  the old-name to new-name table for older documents; links to `docs/RUN-GUIDE.md` and
  the design folder.
- **`Makefile`** (`make` alone prints `make help`):

  | Target | Does |
  |---|---|
  | `setup` | create `.venv`, `pip install -e .`; in phase 2 also `npm install` in `hosting/` |
  | `server` | load `.env/prata.env`, run `python -m fhir_server serve --port 8000` |
  | `test` | server pytest, website `node --test`, scraper pytest, view linter; phase 2 adds hosting `node --test` |
  | `firmware` / `flash` | `arduino-cli compile` / compile and upload to `/dev/ttyACM0` |
  | `eval` | `node website/eval/run.mjs` |
  | `tunnel` (phase 2) | `cloudflared tunnel run --token $CLOUDFLARE_TUNNEL_TOKEN` from `.env/prata.env` |
  | `deploy` (phase 2) | build `hosting/public/`, then `wrangler deploy` |

- **`docs/RUN-GUIDE.md`**: same steps, new paths, `make` commands.
- **`fhir_server/README.md`**: cut to server internals (endpoints, roles, ingest
  contract); run instructions point to the README; the stale FQBN line fixed.

### Phase 1 done when

- All suites pass: 217 server, 172 website, 34 scraper, linter "0 problem(s)", firmware
  compiles.
- Searching for `receiver/`, `arduino/`, `.tools/`, `docs/.superpowers` and the old
  bare default `"fhir_server.db"` (not preceded by `data/`) in the files still in use finds
  nothing. Files still in use: code, tests, `Makefile`, `.gitignore`, both READMEs,
  `RUN-GUIDE.md`, `CLAUDE.md`, `proposal_CLAUDE.md`. Historical documents are excluded (H10).
- `make server` serves `/capture/` from `website/` (checked in a browser).
- Committed (H11), not pushed.

## Phase 2: hosting

### Topology

```
Browser (anywhere)                          Owner's laptop (no public address)
 ├─ Web Serial ← board (USB)                ┌──────────────────────────────┐
 │  https://prata.<account>.workers.dev     │ cloudflared (outbound only)  │
 ▼                                          │        ▼                     │
Worker "prata"                              │ FastAPI 127.0.0.1:8000       │
 ├─ /capture/*  static pages (free)         │ SQLite in data/              │
 ├─ /           → /capture/sessions.html    │                              │
 └─ /auth/* /api/* /fhir-r4/* ── Workers VPC ── tunnel ────────────────────┘
```

Web Serial keeps working: the board plugs into the computer running the browser, and the
Worker's address is HTTPS, which Web Serial requires.

### `hosting/`

- `wrangler.jsonc`: name `prata`; `workers_dev: true`; `preview_urls: false`; assets from
  `./public` with `run_worker_first: ["/auth/*", "/api/*", "/fhir-r4/*"]` (only these
  run Worker code; static requests are free and unlimited); `vpc_services` binding
  `LAPTOP` (service ID from setup step 3; an account resource ID, not a secret);
  `ratelimits` binding `LOGIN_LIMIT` (simple, limit 10, period 60).
- `src/worker.js`: plain JS, no build step, about 100 lines.
- `build.mjs`: copies `website/` into `public/capture/`, leaving out `tests/`, `eval/`
  and `package.json`; writes `_headers` and `_redirects` (`/ /capture/sessions.html 302`).
  `public/` is generated and gitignored.
- `package.json`: Wrangler pinned as a dev dependency; `package-lock.json` committed.
- `tests/`: `node --test` with stand-in bindings.

### Request handling

| Request | Worker response |
|---|---|
| `/fhir-r4/v1/admin/*` | 403 OperationOutcome: account management is only on the laptop. Never forwarded |
| `POST /auth/token` | `LOGIN_LIMIT.limit({key: CF-Connecting-IP})` (key `"unknown"` if the header is missing, so such requests share one budget); over the limit: 429, `Retry-After: 60`. Otherwise forwarded |
| other `/auth/*`, `/api/*`, `/fhir-r4/*` | Forwarded to `LAPTOP` unchanged: method, path, query, headers, streamed body; `Cookie` dropped. The answer is passed back as is, plus `X-Content-Type-Options: nosniff` |
| laptop unreachable | 503 OperationOutcome, `Retry-After: 30`: "PRATA server is offline (laptop off or tunnel down)" |

Errors made by the Worker are OperationOutcome (`application/fhir+json`), like the
server's. How the VPC binding reports an unreachable laptop (a thrown error or an error
response) is found in live check 5; the Worker and its unit test follow what is observed.

### Static headers (`_headers`)

`Content-Security-Policy: default-src 'self'; style-src 'self' 'unsafe-inline'` (pages use
`style=` attributes and one `<style>` block; all scripts are same-origin files);
`Permissions-Policy: serial=(self)`; `X-Frame-Options: DENY`; `Referrer-Policy:
no-referrer`; `Strict-Transport-Security: max-age=31536000`; `X-Content-Type-Options:
nosniff`. The default `Cache-Control: public, max-age=0, must-revalidate` already makes
the browser revalidate every file, like today's `no-cache`; `guard.js` stays.

### Page fixes

- `website/src/auth.js`: today any failed login reads "wrong username or password".
  It keeps that text for 401 and shows the server's OperationOutcome text otherwise
  (429, 503).
- `website/app.js`: the board-session message shows the OperationOutcome text instead of
  "HTTP 503".
- Uploads need no change: the uploader already retries on 5xx, 408 and 429 with backoff,
  and the IndexedDB outbox keeps chunks while the laptop is offline.

### Accounts (laptop CLI)

| Command | Does |
|---|---|
| `add-account --role doctor --username U --name "N"` | Creates a Practitioner through the validating service (synthetic NIK, prefix `9900` like test patients) and an account linked to it |
| `add-account --role admin --username U` | Admin account, no linked record |
| `add-account --role patient --username U --ref Patient/<id>` | Account linked to an existing Patient |
| `list-accounts` | Username, role, linked record, active |
| `disable-account --username U` | Sets the account inactive; that user's next request gets 401 |

The password is asked twice at the prompt and never echoed; `--from-env VAR` is accepted
as with `set-password`. Never on the command line. A duplicate username, a missing or
unresolvable `--ref`, or a mismatched password repeat writes nothing.

### Laptop setup (once; steps needing a browser or `sudo` are the owner's)

1. `! npx wrangler login` (browser authorization).
2. Workers VPC dashboard, Tunnels: create `prata-laptop`; install `cloudflared` from the
   commands shown; put the token in `.env/prata.env` as `CLOUDFLARE_TUNNEL_TOKEN`.
3. `npx wrangler vpc service create prata-laptop --type http --tunnel-id <id> --ipv4
   127.0.0.1 --http-port 8000`; the service ID goes into `hosting/wrangler.jsonc`.
4. `make setup` (adds `npm install` in `hosting/`), then `make deploy`.

Day to day: `make server` (terminal 1) and `make tunnel` (terminal 2). `make deploy` only
when pages or the Worker change.

### Known limits (recorded, not fixed here)

- The rate limiter counts per Cloudflare location and is approximate.
- The board key is still sent in clear on request (2026-11-18 spec). On a public address,
  whoever holds it can upload into that board's open session until the session ends.
  Planned fix unchanged: challenge and response.
- The JWT stays in `localStorage`; the content policy is the guard against script
  injection.
- TLS ends at Cloudflare's edge, so Cloudflare can read traffic in transit. Storage stays
  on the laptop.
- Workers VPC is beta; its API may change.
- Free plan: 100,000 Worker requests a day. Only API calls count; an upload is one call
  per 10 s of recording.

## Security actions for the owner (outside this build)

- **Change the VM password** named in `.env/notes.env`. It is public on GitHub; untracking
  the file does not undo that.
- Consider making the GitHub repo private: it also holds consultation notes and paper PDFs.

## Testing

TDD for all new code.

- **Worker** (`hosting/tests/worker.test.js`): admin path gives 403 and is not forwarded;
  login under the limit is forwarded, over it gives 429 with `Retry-After`, keyed by
  `CF-Connecting-IP`; forwarding keeps method, path, query, `Authorization`,
  `Content-Type` and body bytes, and drops `Cookie`; the laptop's status and body come back
  unchanged plus `nosniff`; an unreachable laptop gives 503 OperationOutcome.
- **Build** (`hosting/tests/build.test.js`): `public/capture/` holds the three pages,
  `src/`, `guard.js`, `site.css`; `public/` holds `_headers` and `_redirects`; no `tests/`,
  `eval/` or `package.json`.
- **Website**: login and board messages show the server's text for 429 and 503, and the
  old text for 401.
- **Server** (pytest): each `add-account` role; duplicate and bad `--ref` write nothing;
  password never in output; `list-accounts`; a disabled account gets 401; default database
  path `data/fhir_server.db`.

### Live checks (scratch database and scratch admin first; the real database only after all pass)

1. `GET /fhir-r4/v1/metadata` on the public address answers from the laptop.
2. Rapid wrong logins eventually get 429.
3. `/fhir-r4/v1/admin/accounts` gives 403.
4. Headless Chrome, simulated board: log in, open a session, record; chunks land in the
   laptop's database.
5. Stop the server: the page says offline and chunks wait in the outbox; restart: they
   upload, with no duplicates. Repeat with only the tunnel stopped.
6. No content-policy violations in the console on the three pages.
7. Worker CPU per request (`wrangler tail`) well under 10 ms.

Owner check: the real board over Web Serial on the hosted address (the port picker needs a
click).

### Phase 2 done when

All suites pass, live checks 1 to 7 pass, and `README.md`, `docs/RUN-GUIDE.md` and
`CLAUDE.md` (status, commands, the data-location sentence) describe the hosted setup.
Two new documents exist, written from the code (owner request, 2026-11-19):
- `docs/HOW-IT-WORKS.md`: the whole program's flow, kept outside the README.
- `docs/accounts/`: setup guides for admin, doctor and patient. Features not built yet
  (the doctor's integrated view, the patient's own-record page) are marked placeholders.

Committed, not pushed.

## Out of scope

Workers Paid, Python on Workers, D1, Containers; Cloudflare Access; a custom domain;
request history and the WebSocket stream (2026-10-08 spec); board-key challenge and
response; real patient data; boot services for the server or tunnel; CI; rewriting git
history to purge `.env/notes.env` (the password change is the fix).

## Live check results (2026-11-19)

Deployed at `https://prata.haifa.workers.dev` (Worker `prata`, VPC service
`01a1f23b-8b1f-7c90-9643-057de206fbe1`, tunnel `prata-laptop`). Checks 1 to 7 ran on a
scratch database in the session scratchpad, then the real database was checked once.

| # | Check | Result |
|---|---|---|
| 1 | Metadata through the Worker | Pass. `fhirVersion` 4.0.1 from the laptop; `/` gives 302 to `/capture/sessions.html` |
| 2 | Rapid wrong logins get 429 | **Partial.** 51 wrong logins at about 1 per second (16 + 15 serial, 20 in parallel), one client IP, one location (SIN): 0 × 429. 100 logins at concurrency 10: 5 × 429. The binding works but, as Cloudflare documents, counts are local and approximate; it stops fast bursts, not slow guessing |
| 3 | `/fhir-r4/v1/admin/accounts` | Pass. 403 with the exact copy, never forwarded |
| 4 | Simulated board, headless Chrome | Pass. Logged in, created *Sesi L001*, registered `SIM-FAC5C78B`, opened session L1, recorded 25 s: 3 Observations, 3 distinct identifiers |
| 5 | Offline, then back | Pass, both cases. Server stopped: the Worker answered 503 with the exact copy, the page read `Server unreachable, retrying.`, the outbox held 2 chunks; after restart it drained in 16.0 s. Tunnel stopped: same, drained in 17.1 s. Final count 13 Observations, 13 distinct identifiers (no duplicates) |
| 6 | Content-policy messages on the three pages | Pass. 0. Other console errors were the expected network answers: 10 × 503 (offline test), 2 × 404 (favicon, no open session yet), 1 × 401 (board before registration) |
| 7 | Worker CPU per request (`wrangler tail` `cpuTime`) | Pass. 204 requests: max 3 ms, mean 0.46 ms (limit 10 ms) |
| — | Real database through the Worker | Pass. `make server` on `data/fhir_server.db` answered metadata 200 through the Worker; the file was unchanged |

Found and fixed during the checks: Cloudflare's static assets serve `sessions.html` at
`/capture/sessions` (307), so the top bar lost its current-tab mark; `nav.js` now ignores
a trailing `.html` (commit `8bc52f3`).

Open: **check 2.** A slow password guesser is not stopped by the Worker. Options for the
owner: a per-username lockout in the server (strict, free, local), or a Durable Object
limiter in the Worker. Neither is built; the owner decides.

Owner check, not yet done: the real board over Web Serial on the hosted address.

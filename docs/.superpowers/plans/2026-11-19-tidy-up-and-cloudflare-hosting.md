# Repo tidy-up and Cloudflare hosting Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Rename the repo's folders by role with a README and Makefile (phase 1), then serve
the website from a free Cloudflare Worker that forwards API calls to the laptop's server
through Workers VPC (phase 2).

**Architecture:** Phase 1 is moves plus reference updates, gated by every test suite. Phase 2
adds `hosting/`: a build script that copies `website/` into static assets, and a small
plain-JS Worker that runs only for `/auth/*`, `/api/*`, `/fhir-r4/*`, rate-limits login,
blocks account management, and forwards everything else to the `LAPTOP` VPC binding. The
server gains three account commands and refuses tokens of disabled accounts.

**Tech Stack:** Python ≥3.12 (FastAPI, sqlite3, pytest), Node 22 (`node --test`, ESM),
Wrangler `4.164.0`, Cloudflare Workers static assets, Workers VPC, rate-limit binding,
`cloudflared`, GNU make, `arduino-cli`.

**Spec:** `docs/.superpowers/specs/2026-11-19-tidy-up-and-cloudflare-hosting-design.md`
(moves to `docs/design/specs/` in Task 4; this plan moves to `docs/design/plans/`).

## Global Constraints

- The website keeps its address `/capture/`; the Python package keeps the name `fhir_server`.
- Commit at the end of every task, staging only that task's files (review `git status`
  first). Messages end with `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`.
  **Never push.**
- Never run `seed --reset` on `data/fhir_server.db`. Live checks use a scratch database
  until Task 11 says to switch.
- Never print passwords, JWTs, board keys or the tunnel token (not in output, not in commits).
- Historical documents are not rewritten: specs and plans dated before 2026-11-19,
  `docs/design/reports/*`, `docs/handover/*`, and the 2026-11-19 spec's moves table.
- Old-path sweep (phase 1 gate): no `receiver/`, `arduino/`, `.tools/`, `docs/.superpowers`,
  or bare `fhir_server.db` (not preceded by `/`) in code, tests, `Makefile`, `.gitignore`,
  `README.md`, `fhir_server/README.md`, `firmware/radar_json/README.md`,
  `docs/RUN-GUIDE.md`, `CLAUDE.md`, `proposal_CLAUDE.md`.
- Worker error bodies are OperationOutcome, `Content-Type: application/fhir+json`:
  `{"resourceType":"OperationOutcome","issue":[{"severity":"error","code":C,"details":{"text":T}}]}`.
  Exact copy:
  - 403, code `forbidden`: `Account management is only available on the PRATA laptop.`
  - 429, code `throttled`, `Retry-After: 60`: `Too many login attempts. Try again in a minute.`
  - 503, code `transient`, `Retry-After: 30`: `PRATA server is offline (laptop off or tunnel down).`
- Login limit: 10 per 60 s, key = `CF-Connecting-IP` header, or `"unknown"` when absent.
- Board flash: FQBN `m5stack:esp32:m5stack_atoms3r:USBMode=hwcdc,CDCOnBoot=cdc`, port `/dev/ttyACM0`.

## Review Focus

1. **A full 1000-sample chunk (≈100 KB body) through the Worker** must arrive byte-identical
   at the laptop. Test in Task 9.
2. **GET requests and FHIR paths with `$` and query strings** (`/fhir-r4/v1/Device/x/$provision?a=1`,
   `?_count=100`) must be forwarded with the path and query unchanged and no body. Test in Task 9.
3. **Errors the laptop itself returns** (401 for an expired login, 500) must reach the page
   unchanged, not be turned into "offline". Test in Task 9.
4. **A login request without `CF-Connecting-IP`** must still be limited, under the key
   `"unknown"`. Test in Task 9.
5. **A disabled account whose login token is still valid** (up to 1 h) must get 401 on its
   next request, not keep working until expiry. Test in Task 6.

---

## Phase 1: tidy-up

### Task 1: Databases live in `data/`

**Files:**
- Modify: `fhir_server/config.py:15`, `fhir_server/cli.py:199`, `fhir_server/db.py` (`connect`)
- Test: `tests/test_default_db_path.py` (create)

**Interfaces:**
- Produces: default database path `data/fhir_server.db` (env `FHIR_DB_PATH` still overrides);
  `db.connect(db_path)` creates the parent folder when missing.

- [ ] **Step 1: Write the failing tests**

```python
from fhir_server.config import Settings
from test_cli_seed import run_cli

def test_settings_default_db_is_in_data(monkeypatch):
    monkeypatch.delenv("FHIR_DB_PATH", raising=False)
    assert Settings.from_env(jwt_secret="x" * 32).db_path == "data/fhir_server.db"

def test_init_db_default_creates_data_folder(tmp_path, monkeypatch):
    monkeypatch.delenv("FHIR_DB_PATH", raising=False)
    monkeypatch.chdir(tmp_path)
    p = run_cli(["init-db"], {"FHIR_JWT_SECRET": "x" * 32})
    assert p.returncode == 0, p.stderr
    assert "initialized data/fhir_server.db" in p.stdout
    assert (tmp_path / "data" / "fhir_server.db").is_file()
```

- [ ] **Step 2:** Run `.venv/bin/python -m pytest tests/test_default_db_path.py -q`. Expected: 2 failed.
- [ ] **Step 3:** Change both defaults to `"data/fhir_server.db"`. In `db.connect`, create
  `Path(db_path).parent` (`parents=True, exist_ok=True`) unless `db_path == ":memory:"`.
- [ ] **Step 4:** Run the new tests (2 passed), then `.venv/bin/python -m pytest tests -q` (0 failed).
- [ ] **Step 5: Move the files, but only if no server is running.** `pgrep -af "fhir_server serve"` must
  print nothing (if it prints, stop and ask the owner). Then
  `mv fhir_server.db fhir_server.backup-20261118.db data/` and check that `git check-ignore data/fhir_server.db`
  prints the `*.db` rule.
- [ ] **Step 6: Commit** `fhir_server/config.py fhir_server/cli.py fhir_server/db.py tests/test_default_db_path.py`
  (message: `refactor: databases default to data/`).

### Task 2: `receiver/` becomes `website/`

**Files:**
- Move: `receiver/` → `website/` (`git mv receiver website`)
- Modify: `fhir_server/app.py:15,24,92` (`RECEIVER_DIR` → `WEBSITE_DIR = ... / "website"`, docstring path),
  `tests/test_capture_e2e.py:12`, `website/eval/run.mjs:3,159`
- Regenerate: `docs/eval/2026-11-18-radar-display-processing.{md,json}`

**Interfaces:**
- Produces: website source at `website/`, tests run as `node --test "website/tests/*.test.js"`.

- [ ] **Step 1:** `git mv receiver website`, then update the five references above.
- [ ] **Step 2:** `grep -rn "receiver/" fhir_server tests website --include='*.py' --include='*.js' --include='*.mjs' --include='*.html'`
  Expected: no output.
- [ ] **Step 3:** Run `.venv/bin/python -m pytest tests -q` (0 failed) and `node --test "website/tests/*.test.js"` (172 pass, 0 fail).
- [ ] **Step 4:** `node website/eval/run.mjs`, then `git diff docs/eval/`. Expected: only the
  `generated` timestamp and the `Generated by ...` line change; every score is identical.
- [ ] **Step 5: Commit** `website receiver fhir_server/app.py tests/test_capture_e2e.py docs/eval`
  (message: `refactor: rename receiver/ to website/`).

### Task 3: `arduino/` becomes `firmware/`

**Files:**
- Move: `arduino/` → `firmware/` (`git mv arduino firmware`; the untracked `config.h` moves with it)
- Modify: `tests/firmware/board_test.cpp:1,7`, `tests/firmware/sampling_test.cpp:1,7`,
  `tests/test_firmware_contract.py:8`, `.gitignore` (`arduino/radar_json/config.h` → `firmware/radar_json/config.h`),
  any `arduino/radar_json` mention inside `firmware/radar_json/README.md`

- [ ] **Step 1:** Move and update the references.
- [ ] **Step 2:** `git check-ignore -v firmware/radar_json/config.h` prints the new rule.
- [ ] **Step 3:** `.venv/bin/python -m pytest tests -q` gives 0 failed (the firmware host tests compile with g++).
- [ ] **Step 4:** `arduino-cli compile --fqbn "m5stack:esp32:m5stack_atoms3r:USBMode=hwcdc,CDCOnBoot=cdc" firmware/radar_json`
  succeeds (about 19 % flash).
- [ ] **Step 5: Commit** `arduino firmware tests/firmware tests/test_firmware_contract.py .gitignore`
  (message: `refactor: rename arduino/ to firmware/`).

### Task 4: Design docs, scraper, leftovers, `.gitignore`

**Files:**
- Move: `docs/.superpowers/specs` → `docs/design/specs`, `docs/.superpowers/plans` → `docs/design/plans` (git mv);
  `.superpowers/sdd` → `docs/design/reports` (plain mv, becomes tracked);
  `docs/implementation/2026-09-22-radar-json-fhir-dummy-action-plan.md` → `docs/design/plans/`;
  `.tools/scrape` → `tools/scrape` (after `rm tools/scrape`, the symlink); `apk/` → `Local/apk/`
- Remove: `python_receiver/` (`git rm -r`), `PraTAVENV/` (`git rm -r --cached`, then `rm -rf`),
  `docs/learning (Copy)/` (`git rm -r`)
- Untrack, keep on disk: `prata_fhir_server.egg-info/`, `.env/notes.env` (`git rm -r --cached`)
- Modify: `.gitignore`, `CLAUDE.md`, `proposal_CLAUDE.md` (paths)

- [ ] **Step 1: Rescan before publishing the reports.**
  `grep -rlE 'eyJ[A-Za-z0-9_-]{20,}|[0-9a-f]{64}' .superpowers/sdd | wc -l` must print `0`. If not, stop and ask.
- [ ] **Step 2:** Do the moves, removals and untracking above. Remove the folders left empty
  (`docs/.superpowers`, `.superpowers`, `docs/implementation`, `.tools`).
- [ ] **Step 3:** Write `.gitignore` as exactly:

```
.goutputstream-*
__pycache__/
*.pyc
*.egg-info/
.pytest_cache/
.venv/
.env
*.db
apk/
node_modules/
.wrangler/
hosting/public/
firmware/radar_json/config.h
```

- [ ] **Step 4:** In `CLAUDE.md` and `proposal_CLAUDE.md`, replace `docs/.superpowers/` with
  `docs/design/` and `.tools/scrape` with `tools/scrape`. Point `CLAUDE.md`'s spec location
  at `docs/design/specs/`.
- [ ] **Step 5: Verify.**
  - `python3 -m pytest tools/scrape/tests -q`: 34 passed.
  - `python3 tools/scrape/lint_views.py`: `0 problem(s)`.
  - `.venv/bin/python -m pytest tests -q`: 0 failed.
  - `git ls-files | grep -cE '^(PraTAVENV|python_receiver|prata_fhir_server\.egg-info)/|^\.env/'`: `0`.
  - `git status --short` shows only this task's changes.
- [ ] **Step 6: Commit** (message: `chore: design docs to docs/design, scraper into git, remove leftovers`).

### Task 5: README, Makefile, run guide (phase 1 gate)

**Files:**
- Create: `README.md`, `Makefile`
- Modify: `docs/RUN-GUIDE.md`, `fhir_server/README.md`, `CLAUDE.md` (repo map and Commands block)

**Interfaces:**
- Produces: make targets `help setup server test firmware flash eval`. Task 8 adds `tunnel deploy`
  and extends `setup` and `test`.

- [ ] **Step 1: Write `Makefile`.** The exact commands are fixed here:

```make
# PRATA: run `make` to list commands.
FQBN := m5stack:esp32:m5stack_atoms3r:USBMode=hwcdc,CDCOnBoot=cdc
PORT ?= /dev/ttyACM0
PY   := .venv/bin/python
ENV  := .env/prata.env

.DEFAULT_GOAL := help
.PHONY: help setup server test firmware flash eval

help: ## list commands
	@grep -E '^[a-z-]+:.*## ' $(MAKEFILE_LIST) | awk -F':.*## ' '{printf "  make %-10s %s\n", $$1, $$2}'

setup: ## create .venv and install the server
	python3 -m venv .venv
	$(PY) -m pip install -e .

server: ## run the server on http://127.0.0.1:8000 (website at /capture/)
	@test -f $(ENV) || { echo "missing $(ENV): see README.md, Secrets"; exit 1; }
	. ./$(ENV) && $(PY) -m fhir_server serve --port 8000

test: ## run every test suite
	$(PY) -m pytest tests -q
	node --test "website/tests/*.test.js"
	python3 -m pytest tools/scrape/tests -q
	python3 tools/scrape/lint_views.py

firmware: ## compile the board firmware
	arduino-cli compile --fqbn "$(FQBN)" firmware/radar_json

flash: firmware ## compile and upload to the board on $(PORT)
	arduino-cli upload -p $(PORT) --fqbn "$(FQBN)" firmware/radar_json

eval: ## rescore the display methods (rewrites docs/eval/)
	node website/eval/run.mjs
```

- [ ] **Step 2: Write `README.md`** with these sections, in this order:
  - **What this is:** two lines, linking the thesis goal in `CLAUDE.md`.
  - **Start here:** `make setup`, then create `.env/prata.env` (the two `export` lines from
    `RUN-GUIDE.md`), then `make server`, then open `http://127.0.0.1:8000/capture/sessions.html`.
  - **Folder map:** the spec's target-layout table.
  - **Everyday commands:** the output of `make help`.
  - **Secrets:** `.env/prata.env`, never committed.
  - **Old names:** the table `receiver/`→`website/`, `arduino/radar_json/`→`firmware/radar_json/`,
    `docs/.superpowers/`→`docs/design/`, `.superpowers/sdd/`→`docs/design/reports/`,
    `docs/implementation/`→`docs/design/plans/`, `.tools/scrape/`→`tools/scrape/`,
    `fhir_server.db`→`data/fhir_server.db`, `python_receiver/`→removed (in git history).
    Say that older specs, plans and handovers use the old names.
  - **Read next:** `docs/RUN-GUIDE.md`, `docs/design/specs/`, `CLAUDE.md`, `proposal_CLAUDE.md`.
- [ ] **Step 3: Update `docs/RUN-GUIDE.md`.**
  - Paths become the new ones.
  - `source .env/prata.env` plus the serve command becomes `make server`; flashing becomes
    `make flash`; the Tests section becomes `make test`.
  - Seeding and `set-password` commands keep the explicit `source` line, since they are
    run by hand.
  - The "Where things are saved" table gets `data/fhir_server.db`.
- [ ] **Step 4: Cut down `fhir_server/README.md`.**
  - Keep: Endpoints, Roles, Device ingest contract (path `firmware/radar_json/`).
  - Replace Run, Raw capture receiver and Tests with one line: "Run and test: see `README.md`
    and `docs/RUN-GUIDE.md`." This also drops the stale `m5stack_cores3` line.
- [ ] **Step 5: Update `CLAUDE.md`.**
  - The repo map becomes the new layout.
  - The Commands block becomes `make` targets, each with its raw command.
- [ ] **Step 6: Old-path sweep (Global Constraints).**
  `grep -rnE 'receiver/|arduino/|\.tools/|docs/\.superpowers|(^|[^/])fhir_server\.db' fhir_server tests website firmware device_client tools Makefile .gitignore README.md docs/RUN-GUIDE.md CLAUDE.md proposal_CLAUDE.md | grep -v __pycache__`
  Expected: no output.
- [ ] **Step 7: Phase 1 gate.** `make` prints the target list. `make test` passes every suite.
  `make firmware` compiles. Run `make server` in the background, then
  `for p in index.html sessions.html review.html guard.js src/auth.js; do curl -s -o /dev/null -w "%{http_code} $p\n" http://127.0.0.1:8000/capture/$p; done`
  must print all `200`. Take a headless-Chrome screenshot of `/capture/sessions.html` showing
  the top bar (pattern in `docs/handover/2026-11-18-handover.md` §3.6). Stop the server.
- [ ] **Step 8: Commit** `README.md Makefile docs/RUN-GUIDE.md fhir_server/README.md CLAUDE.md`
  (message: `docs: README, Makefile and run guide for the new layout`).

---

## Phase 2: hosting

### Task 6: Account commands; disabled accounts lose access at once

**Files:**
- Modify: `fhir_server/repositories/accounts.py`, `fhir_server/services/sessions.py`,
  `fhir_server/cli.py`, `fhir_server/routes/deps.py:get_principal`
- Test: `tests/test_cli_accounts.py` (create; reuses `seeded` from `test_cli_capture_session`,
  `run_cli` from `test_cli_seed`, `can_login` pattern from `test_cli_set_password`)

**Interfaces:**
- Produces:
  - `accounts.list_all(conn) -> list[dict]`: all accounts, active and inactive, ordered by username.
  - `accounts.set_active(conn, username: str, active: bool) -> bool`: False when there is no such account.
  - `sessions.make_test_practitioner(svc: FhirService, name: str) -> dict`: Practitioner with NIK
    `"9900"` + 12 random digits (`https://fhir.kemkes.go.id/id/nik`) and
    `name=[{"use":"official","text":name}]`, created via `svc.create(ADMIN, ...)`. Retries on 409
    like `make_test_patient`.
  - CLI commands:
    - `add-account --role {admin,doctor,patient} --username U [--name N] [--ref Patient/<id>] [--from-env VAR]`
    - `list-accounts`
    - `disable-account --username U`

Rules for `add-account`:
- Username must match `^[A-Za-z0-9._-]{3,32}$`.
- A doctor needs `--name`. A patient needs `--ref` naming an existing Patient. An admin takes
  neither (giving one is a usage error).
- The password comes from `--from-env VAR`, or else from `getpass` twice (`Password: `,
  `Repeat password: `).
- Check order: username, then role arguments, then `--ref`, then password. Only after all four
  pass: create the Practitioner (doctor), then the account.
- Exit codes:
  - 2: usage errors (bad username, missing or extra `--name` / `--ref`, empty variable,
    passwords differ, with the message `passwords do not match`);
  - 1: `account U already exists` (checked against active **and** inactive accounts) or
    `no Patient/<id>`;
  - 0: success, printing `created <role> <username>` plus ` (<ref>)` when there is a ref.
- `list-accounts` prints a header line `username\trole\tref\tactive`, then one tab-separated
  line per account (`ref` shown as `-` when none, active as `yes`/`no`).
- `disable-account` prints `disabled U`, or exits 1 with `no account named U`.

`get_principal`: when the JWT verifies and the principal has an `account_id`, and
`accounts.get(conn, account_id)` is None, raise a 401 FhirError with text `Account disabled`
(rule 20007).

- [ ] **Step 1: Write the failing tests** in `tests/test_cli_accounts.py`:
  - `test_add_doctor_creates_practitioner_and_login`:
    - `add-account --role doctor --username dr_ana --name "Ana Putri" --from-env NEW_PW` (NEW_PW=`ana-pass-123`) exits 0.
    - `ana-pass-123` is not in stdout or stderr.
    - `can_login(db, "dr_ana", "ana-pass-123")`.
    - The account ref starts `Practitioner/`; that resource's NIK is 16 digits starting `9900`,
      and its `name[0].text == "Ana Putri"`.
  - `test_add_admin_and_patient`:
    - `--role admin --username admin2` exits 0.
    - `--role patient --username pat2 --ref Patient/<seed patient_id>` exits 0.
    - Both can log in.
  - `test_refusals_write_nothing`. Each case gives the stated exit code:
    - existing username `doctor`: 1, `already exists`;
    - `--ref Patient/nope`: 1;
    - patient without `--ref`: 2;
    - doctor without `--name`: 2;
    - admin with `--name X`: 2;
    - username `has space`: 2;
    - `--from-env UNSET_XYZ`: 2.

    Afterwards the account count (`accounts.list_all`) and the Practitioner count are unchanged.
  - `test_interactive_passwords_must_match`: in-process `cli.main([...])` with `getpass`
    monkeypatched to return `a1b2c3` then `zzzzzz` raises `SystemExit(2)`, and no account is written.
  - `test_list_accounts_shows_role_ref_and_active`: the header line is
    `username\trole\tref\tactive`, and the `doctor` line equals
    `doctor\tdoctor\tPractitioner/N10000000\tyes`.
  - `test_disabled_account_loses_login_and_live_token`:
    - Log in as `doctor` (password `doctor-pw`) and keep the token.
    - `disable-account --username doctor` exits 0.
    - `GET /api/sessions` with that token gives 401; logging in again gives 401; `list-accounts`
      shows `no`.
    - `disable-account --username nobody` exits 1.
- [ ] **Step 2:** Run `.venv/bin/python -m pytest tests/test_cli_accounts.py -q`. Expected: all fail.
- [ ] **Step 3:** Implement the interfaces above.
- [ ] **Step 4:** New tests pass; `.venv/bin/python -m pytest tests -q` gives 0 failed.
- [ ] **Step 5: Commit** (message: `feat(server): add-account, list-accounts, disable-account`).

### Task 7: Pages show the server's message for 429 and 503

**Files:**
- Create: `website/src/outcome.js`
- Modify:
  - `website/src/sessions-view.js`: `apiError` moves out; re-export it with
    `export { apiError } from "./outcome.js";` so its importers are unchanged.
  - `website/src/auth.js`: `login`.
  - `website/app.js:105-106,119-120`.
- Test: `website/tests/outcome.test.js` (create), `website/tests/auth.test.js`

**Interfaces:**
- Produces: `apiError(res: Response-like) -> Promise<string>`. It returns the first non-empty
  `issue[].details.text` of an OperationOutcome body, else `HTTP <status>`. The body is
  unchanged from today's `sessions-view.js`.

- [ ] **Step 1: Write the failing tests.**
  - `outcome.test.js`: an OO body gives its text; a non-JSON body with status 503 gives
    `HTTP 503`; an OO with no text gives `HTTP 400`.
  - `auth.test.js`, with fake responses `{ok:false,status,text:async()=>body}`:
    - 401 rejects with `Login failed: wrong username or password.`
    - 429 with an OO body rejects with
      `Login failed: Too many login attempts. Try again in a minute.`
    - 503 with body `<html>` rejects with `Login failed: HTTP 503`.
- [ ] **Step 2:** Run `node --test "website/tests/*.test.js"`. Expected: the new tests fail.
- [ ] **Step 3: Implement.**
  - Create `outcome.js` and add the re-export in `sessions-view.js`.
  - `login`: on 401, keep the old message; on any other non-ok answer, throw
    `` `Login failed: ${await apiError(res)}` ``.
  - `app.js` `checkSession`, last branch:
    `` `Board ${board.id}: ${await apiError(res)}` ``.
  - `app.js` `registerBoard`:
    `` `Could not register board ${board.id}: ${await apiError(res)}` ``.
- [ ] **Step 4:** `node --test "website/tests/*.test.js"`: 0 fail.
- [ ] **Step 5: Commit** (message: `fix(website): show the server's message when login or board lookup fails`).

### Task 8: `hosting/` scaffold and build

**Files:**
- Create:
  - `hosting/package.json`:
    `{"private":true,"type":"module","scripts":{"build":"node build.mjs","deploy":"node build.mjs && wrangler deploy"},"devDependencies":{"wrangler":"4.164.0"}}`
  - `hosting/package-lock.json` (from `npm install`)
  - `hosting/build.mjs`
  - `hosting/wrangler.jsonc`
  - `hosting/tests/build.test.js`
- Modify: `Makefile` (`setup`, `test`; new `tunnel`, `deploy`)

**Interfaces:**
- Produces:
  - `build({ websiteDir: string, outDir: string }) -> Promise<void>`: empties `outDir`, copies
    `websiteDir` to `outDir/capture/` without the top-level `tests/`, `eval/`, `package.json`
    and `node_modules/`, then writes `outDir/_headers` (= `HEADERS`) and `outDir/_redirects`
    (= `REDIRECTS`).
  - Running `node build.mjs` uses `../website` and `./public`, relative to the script.
  - Exported constants:
    - `REDIRECTS = "/ /capture/sessions.html 302\n"`
    - `HEADERS`, exactly:

```
/*
  Content-Security-Policy: default-src 'self'; style-src 'self' 'unsafe-inline'
  Permissions-Policy: serial=(self)
  X-Frame-Options: DENY
  Referrer-Policy: no-referrer
  Strict-Transport-Security: max-age=31536000
  X-Content-Type-Options: nosniff
```

- `wrangler.jsonc`, exactly (the service ID is filled in by Task 10):

```jsonc
{
  "$schema": "node_modules/wrangler/config-schema.json",
  "name": "prata",
  "main": "src/worker.js",
  "compatibility_date": "2026-11-15",
  "workers_dev": true,
  "preview_urls": false,
  "assets": { "directory": "./public", "run_worker_first": ["/auth/*", "/api/*", "/fhir-r4/*"] },
  "vpc_services": [{ "binding": "LAPTOP", "service_id": "SET_IN_TASK_10", "remote": true }],
  "ratelimits": [{ "name": "LOGIN_LIMIT", "namespace_id": "1001", "simple": { "limit": 10, "period": 60 } }]
}
```

- [ ] **Step 1: Write the failing test** `build.test.js` (real `website/`, temporary `outDir`):
  - These exist: `capture/{index,sessions,review}.html`, `capture/guard.js`, `capture/site.css`,
    `capture/src/auth.js`, `capture/src/outcome.js`.
  - These don't: `capture/tests`, `capture/eval`, `capture/package.json`.
  - `_headers` equals `HEADERS` and `_redirects` equals `REDIRECTS`.
  - A file `stale.txt` written to `outDir` before the build is gone after it.
- [ ] **Step 2:** `node --test "hosting/tests/*.test.js"`: fails (no `build.mjs`).
- [ ] **Step 3:** Implement `build.mjs` (use `fs.cp` with a `filter`). Run `cd hosting && npm install`.
- [ ] **Step 4:** The test passes. `cd hosting && npx wrangler --version` prints `4.164.0`.
- [ ] **Step 5: Makefile.**
  - `setup` gains `cd hosting && npm install`.
  - `test` gains `node --test "hosting/tests/*.test.js"`.
  - Add these targets (both added to `.PHONY`):

```make
tunnel: ## connect this laptop to Cloudflare (keep running next to `make server`)
	@test -f $(ENV) || { echo "missing $(ENV): see README.md, Secrets"; exit 1; }
	. ./$(ENV) && test -n "$$CLOUDFLARE_TUNNEL_TOKEN" && TUNNEL_TOKEN="$$CLOUDFLARE_TUNNEL_TOKEN" cloudflared tunnel run

deploy: ## build the website and deploy the Worker
	cd hosting && npm run deploy
```

  The token goes through the `TUNNEL_TOKEN` environment variable, so it never shows in `ps`.
- [ ] **Step 6:** `make test` passes; `make -n tunnel deploy` prints the commands.
- [ ] **Step 7: Commit** `hosting/package.json hosting/package-lock.json hosting/build.mjs hosting/wrangler.jsonc hosting/tests Makefile`
  (message: `feat(hosting): static build and Worker config`).

### Task 9: The Worker

**Files:**
- Create: `hosting/src/worker.js`, `hosting/tests/worker.test.js`
- Modify: the spec's request-handling row says "streamed body". Change it to "body bytes
  (buffered; chunks are about 100 KB)": Node's `Request` needs `duplex` for streamed bodies,
  and Workers do not document that option.

**Interfaces:**
- Consumes: bindings `env.LAPTOP.fetch(Request) -> Promise<Response>` and
  `env.LOGIN_LIMIT.limit({key}) -> Promise<{success: boolean}>`.
- Produces:
  - `export default { fetch(request, env, ctx) -> Promise<Response> }`
  - `export function outcome(status, code, text, headers = {}) -> Response`: the OperationOutcome
    shape from Global Constraints.

Routing, in order (the Worker only ever sees `/auth/*`, `/api/*`, `/fhir-r4/*`):
1. A path starting `/fhir-r4/v1/admin/` gives 403.
2. `POST /auth/token`: call `LOGIN_LIMIT.limit({key})`; when `success` is false, answer 429.
3. Forward. Build `new Request("http://127.0.0.1" + pathname + search, {method, headers, body})`.
   `headers` is a copy of the request headers without `cookie`. `body` is
   `await request.arrayBuffer()`, or null for GET/HEAD.
4. If `LAPTOP.fetch` throws, answer 503. Otherwise return `new Response(res.body, res)` with
   `X-Content-Type-Options: nosniff` set.

- [ ] **Step 1: Write the failing tests** in `worker.test.js`. The stand-ins record what they
  receive: `laptop(respond)` keeps the `Request`s it gets, and `limiter(ok)` keeps the keys.
  - `admin path is refused and never forwarded`: GET `/fhir-r4/v1/admin/accounts` gives 403.
    The body's `issue[0].details.text` is the exact 403 copy, the content type is
    `application/fhir+json`, and the laptop saw 0 requests.
  - `login under the limit is forwarded, keyed by client IP`: the key equals the
    `CF-Connecting-IP` value, and the laptop saw 1 POST.
  - `login over the limit gets 429`: 429, `Retry-After` is `60`, the 429 copy, laptop saw 0.
  - `login without CF-Connecting-IP is limited as "unknown"`: the key is `"unknown"`.
  - `forwarding keeps method, path, query, auth, content type and body bytes`:
    - POST `/fhir-r4/v1/Observation?x=1` with a 100,000-byte body (random bytes), plus
      `Authorization` and `Content-Type: application/fhir+json`.
    - The laptop sees the URL `http://127.0.0.1/fhir-r4/v1/Observation?x=1`, the same headers,
      and identical bytes.
  - `GET with $ in the path has no body and an unchanged URL`:
    `/fhir-r4/v1/Device/abc/$provision?a=1` arrives as `http://127.0.0.1/fhir-r4/v1/Device/abc/$provision?a=1`
    with a null body.
  - `cookies are dropped`: the laptop's request has no `cookie` header.
  - `laptop answers pass through unchanged`: the laptop's 401 and 500 come back with the same
    status, body and content type, plus `X-Content-Type-Options: nosniff`.
  - `unreachable laptop gives 503`: when `LAPTOP.fetch` throws, the answer is 503 with
    `Retry-After: 30` and the 503 copy.
- [ ] **Step 2:** `node --test "hosting/tests/*.test.js"`: the worker tests fail.
- [ ] **Step 3:** Implement `worker.js` per the routing above.
- [ ] **Step 4:** `make test`: everything passes. `cd hosting && npx wrangler deploy --dry-run`
  exits 0. This validates the config without deploying; if it rejects the placeholder service
  ID, note it and continue.
- [ ] **Step 5: Commit** `hosting/src hosting/tests/worker.test.js docs/design/specs/2026-11-19-tidy-up-and-cloudflare-hosting-design.md`
  (message: `feat(hosting): Worker forwards API calls, limits logins, blocks account admin`).

### Task 10: Tunnel, VPC service, first deploy (owner steps marked **OWNER**)

**Files:**
- Modify: `hosting/wrangler.jsonc` (`service_id`)
- Local only: `.env/prata.env` (gains `export CLOUDFLARE_TUNNEL_TOKEN=...`; gitignored)

- [ ] **Step 1: Install `cloudflared` without sudo.**
  `curl -fsSL -o ~/.local/bin/cloudflared https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64 && chmod +x ~/.local/bin/cloudflared && cloudflared --version`
  The machine is `x86_64`. Expected: a version line.
- [ ] **Step 2: OWNER:** `! (cd hosting && npx wrangler login)`, which opens the browser. Then
  `cd hosting && npx wrangler whoami` shows the account.
- [ ] **Step 3: OWNER:**
  - In the dashboard, go to Workers VPC, then Tunnels, then Create, and name the tunnel `prata-laptop`.
  - Copy the token into `.env/prata.env` as `export CLOUDFLARE_TUNNEL_TOKEN=<token>`.
  - Tell Claude the tunnel ID (it is not secret). Skip the dashboard's install command:
    Step 1 already installed `cloudflared`.
- [ ] **Step 4:** `cd hosting && npx wrangler vpc service create prata-laptop --type http --tunnel-id <TUNNEL_ID> --ipv4 127.0.0.1 --http-port 8000`
  Put the printed service ID into `wrangler.jsonc`.
- [ ] **Step 5: Scratch server and tunnel.**
  - `export SCR=$(mktemp -d)`, then `FHIR_DB_PATH=$SCR/live.db` with `. ./.env/prata.env` and
    `.venv/bin/python -m fhir_server seed --reset`. The path is `$SCR/live.db`, **never** `data/`.
  - In the background: `FHIR_DB_PATH=$SCR/live.db make server` and `make tunnel`.
  - The dashboard shows the tunnel as connected.
- [ ] **Step 6:** `make deploy`. Expected: Wrangler prints `https://prata.<subdomain>.workers.dev`.
- [ ] **Step 7: Live check 1.**
  `curl -s https://prata.<subdomain>.workers.dev/fhir-r4/v1/metadata | python3 -c 'import json,sys;print(json.load(sys.stdin)["fhirVersion"])'`
  prints `4.0.1`. `curl -sI https://prata.<subdomain>.workers.dev/` shows a 302 to `/capture/sessions.html`.
- [ ] **Step 8: Commit** `hosting/wrangler.jsonc` (message: `chore(hosting): bind the laptop VPC service`).

### Task 11: Live checks 2 to 7, then the real database

Use the scratch server from Task 10. `URL` = the deployed address.

- [ ] **Step 1 (check 2):** 15 POSTs to `$URL/auth/token` with a wrong password. At least one
  answer is 429 (the limiter is approximate; if none, repeat once and record the count).
- [ ] **Step 2 (check 3):** `curl -s -o /dev/null -w '%{http_code}' $URL/fhir-r4/v1/admin/accounts` prints `403`.
- [ ] **Step 3 (check 4):** Headless Chrome on `$URL/capture/` with the simulated board:
  - log in as the scratch admin;
  - register the simulated board;
  - open a session for a new test patient;
  - record about 25 s, then stop.

  `sqlite3 $SCR/live.db "select count(*) from resources where type='Observation'"` must be ≥ 2.
- [ ] **Step 4 (check 5): Offline.**
  - Record again, then kill the server process and keep recording 20 s.
  - The page status reads `Server unreachable, retrying.` and the outbox (IndexedDB, read with
    `Runtime.evaluate`) holds more than 0 chunks.
  - `curl -s -i $URL/fhir-r4/v1/metadata` shows how the dead laptop is reported. If it is not
    the Worker's 503 copy (for example a 502 from the VPC layer), add that status to Task 9's
    offline rule, with a test, and redeploy.
  - Restart the server: the outbox drains to 0, and the count of Observations equals the count
    of distinct identifiers (no duplicates).
  - Repeat with only `make tunnel` stopped.
- [ ] **Step 5 (check 6):** The console messages on the three pages contain no
  `Content Security Policy` entries.
- [ ] **Step 6 (check 7):** Run `cd hosting && npx wrangler tail prata --format json` during
  steps 1 to 3. Every event's `cpuTime` is < 10; record the maximum. If the events carry no
  `cpuTime`, read the CPU time chart under the Worker's Metrics in the dashboard instead, and
  say which source was used.
- [ ] **Step 7: Switch to the real database.**
  - Stop the scratch server, run `make server` (default `data/fhir_server.db`), and check that
    metadata answers 200 through `$URL`.
  - `rm -rf $SCR`. Clear the scratch login from the hosted origin's `localStorage`.
  - The owner's existing `admin` login keeps working. If the owner wants named accounts now
    (for example, for supervisors), create them with `add-account`; the owner types each
    password at the prompt.
- [ ] **Step 8:** Record the results of checks 1 to 7 (numbers, not adjectives) in the spec
  under a new `## Live check results (date)` section. Commit it, plus any Task 9 change from
  Step 4 (message: `test(hosting): live checks on the deployed Worker`).
- [ ] **Step 9: OWNER:** connect the real board on `$URL/capture/` and record 30 s. A chunk
  is stored.

### Task 12: Documentation for the hosted setup

**Files:**
- Create: `docs/HOW-IT-WORKS.md`, `docs/accounts/README.md`, `docs/accounts/admin.md`,
  `docs/accounts/doctor.md`, `docs/accounts/patient.md` (owner request, 2026-11-19)
- Modify: `README.md`, `docs/RUN-GUIDE.md`, `CLAUDE.md`, the spec's Status line

Write every claim in the new documents from the code as it stands after Tasks 1 to 11,
not from this plan or the spec. Name the file behind each step so a reader can find the
code. Owner-facing prose: plain English, no FHIR jargon without a one-line gloss.

- [ ] **Step 1: `docs/HOW-IT-WORKS.md`**: the whole program's flow, separate from the
  README. Sections, in this order:
  1. **The pieces:** one table with each piece, its folder and what it does: board firmware,
     website pages, Worker, tunnel, server, database.
  2. **One recording, end to end:** a Mermaid sequence diagram plus numbered steps:
     - the board samples I/Q at 100 Hz and writes JSON lines over USB;
     - the capture page reads them over Web Serial, asks `BOARD?`, and gets the board's
       session from `/api/board/session`;
     - the preview shows the display processing (`hybrid`, display only);
     - Record cuts chunks, the outbox keeps them in IndexedDB, and the uploader posts each
       chunk as an Observation and retries on failure;
     - hosted only: the Worker forwards the post through the tunnel;
     - the server checks the login and the rules, validates the resource, and stores it in
       `data/fhir_server.db`.
  3. **Logging in and roles:** how a login becomes a token (lifetime, what the token
     carries), and one table of who may read or write what for admin, doctor, patient and
     board (from `fhir_server/authz.py` and `fhir_server/services/sessions.py`).
  4. **Boards and sessions:** board identity (`BOARD?`, chip ID, key), registration, test
     patients, and a session as an Encounter that ties a board to a patient and a doctor.
  5. **What is stored:** the resource types written, what each holds, and the database file.
  6. **When something fails:** offline laptop or tunnel (503, outbox waits, no duplicates
     on drain), too many logins (429), account management from the web (403), rejected
     data (the validation error the page shows).
  7. **Local and hosted:** the same pages and server; hosted adds the Worker and the tunnel
     (Mermaid flowchart of both paths).
  8. **Not built yet:** the doctor's integrated view (RME, RADAR JVP, 12-lead ECG), the
     patient page, ECG input, and radar-derived heart rate (firmware values are
     placeholders). Link to the account guides' placeholder sections.
- [ ] **Step 2: `docs/accounts/`**: account setup guides.
  - **`README.md`:**
    - the three roles in one table;
    - account management is laptop-only (the Worker returns 403);
    - `add-account`, `list-accounts` and `disable-account`, with an example each;
    - password entry (prompt twice, or `--from-env`), username rule `^[A-Za-z0-9._-]{3,32}$`;
    - a disabled account is refused on its next request;
    - links to the three role guides.
  - **Each role guide** (`admin.md`, `doctor.md`, `patient.md`) has these sections:
    - **Create the account:** the exact command.
    - **Log in:** local and hosted address; which page to open.
    - **What this account can do today:** from the code.
    - **Not built yet:** each unbuilt feature on its own line, starting with
      `> **Placeholder (not implemented yet):**` and naming what will go there, so it is
      easy to find and fill in later.
  - **Role-specific content:**
    - **admin:**
      - the existing `admin` login, and creating a named admin;
      - registering a board, creating a test patient, opening a session on behalf of a
        doctor;
      - listing and disabling accounts.
    - **doctor:**
      - creating the account makes a Practitioner with a synthetic NIK;
      - a new doctor sees no patients until an admin opens a session that names them
        (`participates_in_patient`), so the guide says to do that first;
      - opening and ending their own sessions; reading their sessions' Observations.
      - Placeholder: the integrated patient view.
    - **patient:**
      - finding the `Patient/<id>` to pass to `--ref`;
      - what logging in shows today (the not-staff message on the sessions page);
      - the API can read the patient's own Patient, Encounter and Observation.
      - Placeholder: the patient's own-record page.
- [ ] **Step 3: `README.md`** gains:
  - a **Hosted site** section:
    - the URL, and that anyone can open it but only accounts you create can log in;
    - `make server` plus `make tunnel` (online only while both run);
    - `make deploy` (only when pages or the Worker change);
    - one line linking `docs/accounts/`.
  - In **Read next**, `docs/HOW-IT-WORKS.md` goes first, then `docs/accounts/README.md`.
- [ ] **Step 4: `docs/RUN-GUIDE.md`** gains:
  - a "Hosted site" section: the one-time setup (Task 10 steps 1 to 4) and day to day;
  - an "Accounts" line linking `docs/accounts/README.md` (no copy of its content);
  - troubleshooting rows: `PRATA server is offline` (start `make server` and `make tunnel`),
    `Too many login attempts` (wait a minute), 403 on account management (use the laptop CLI),
    and "tunnel not connected" (check the token in `.env/prata.env`).
- [ ] **Step 5: `CLAUDE.md`.**
  - Replace the sentence "...while running entirely locally." with "...Data is stored only on
    the owner's laptop; the public site is a Cloudflare Worker that forwards requests to it. We
    never call the hosted platform."
  - Change the status bullet to "implemented", citing the live check results.
  - The repo map gains `hosting/`, `docs/HOW-IT-WORKS.md` and `docs/accounts/`.
  - The Commands block gains `tunnel`, `deploy` and the account commands.
- [ ] **Step 6: Check the new documents against the repo.**
  - Every backticked repo path in `docs/HOW-IT-WORKS.md` and `docs/accounts/*.md` exists.
    URL paths (`/api/...`) start with `/` and references (`Patient/<id>`) with a capital, so
    the pattern skips them. Expected: no output.

    ```bash
    grep -ohE '`[a-z_][a-z_./-]*/[A-Za-z0-9_.-]+`' docs/HOW-IT-WORKS.md docs/accounts/*.md \
      | tr -d '`' | sort -u | while read -r p; do test -e "$p" || echo "missing $p"; done
    ```
  - Run each account command from the guides once against a scratch database
    (`FHIR_DB_PATH=$SCR/doc.db`, `--from-env`), then `rm -rf $SCR`. Expected: each one
    succeeds as the guide says.
  - `grep -c 'Placeholder (not implemented yet)' docs/accounts/*.md` gives at least 1 for
    `doctor.md` and `patient.md`.
- [ ] **Step 7:** The spec's Status line becomes "implemented 2026-11-.. (plan
  `docs/design/plans/2026-11-19-tidy-up-and-cloudflare-hosting.md`)". `make test` passes.
- [ ] **Step 8: Commit.**
  - Files: the five new documents plus `README.md docs/RUN-GUIDE.md CLAUDE.md` and the spec.
  - Message: `docs: how it works, account guides, hosted site`.
  - Ask the owner before any push.

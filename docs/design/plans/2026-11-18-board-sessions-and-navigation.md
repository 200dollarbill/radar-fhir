# Board sessions and navigation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** The board identifies itself over serial, admins and doctors manage sessions on a dashboard, and the capture page gets its session from the plugged-in board. All pages share one navigation bar.

**Architecture:** FastAPI gains `boards` and `board_sessions` tables, a board-key principal and `/api` routes. The firmware answers `BOARD?`. The page gets a board handshake, a line hub (preview and record), shared auth and navigation, and a Sessions page.

**Tech Stack:** Python 3.12 / FastAPI / SQLite, ESP32 Arduino (Preferences, eFuse MAC), plain ES modules, `node --test`, pytest, g++ host tests.

**Spec:** `docs/.superpowers/specs/2026-11-18-board-sessions-and-navigation-design.md`

## Global Constraints

- Board ID `^[0-9A-F]{12}$` (real) or `^SIM-[0-9A-F]{8}$` (virtual); key `^[0-9a-f]{64}$`.
- Serial: host sends `BOARD?\n`; board answers `BOARD {"id":"…","key":"…","fw":"radar_json"}`.
- Only SHA-256 of keys stored. One open session per board.
- Page copy keeps "Display processing only. Not a measurement result." on the waveform.
- No commits: the owner commits (`Local/claude.md`).

## Review Focus

1. A board key with no open session must not upload: POST Observation → 403. Test in Task 1.
2. Re-registering a board replaces its key: the old key stops working. Test in Task 2.
3. Opening a second session on a busy board → 409, and the first stays open. Test in Task 2.
4. Board replies arrive between sample lines and after stale backlog lines: the handshake skips sample lines and finds the `BOARD` line. Test in Task 4.
5. Stop recording must not close the port or the preview: the hub ends only the recording subscriber. Test in Task 4.

---

### Task 1: Board storage and board-key principal
**Files:** Modify `fhir_server/db.py`, `fhir_server/routes/deps.py`; Create `fhir_server/repositories/boards.py`; Test `tests/test_boards.py`.
**Produces:** `boards.register(conn, serial, device_id, key) -> bool created`, `boards.by_key(conn, key) -> row|None`, `boards.get(conn, serial)`, `boards.list(conn)`, `boards.open_session(conn, serial) -> row|None`, `boards.start_session(conn, row)`, `boards.end_session(conn, id, ended)`, `boards.sessions(conn, open_only)`.
- [ ] Tests: register/get/by_key; re-register replaces hash; second open session on same serial raises `sqlite3.IntegrityError`; principal from board key has the open session's `Patient/x`; no session → `patient_id None`; device Observation POST with board key and no session → 403.
- [ ] Fail, implement, pass.

### Task 2: Session service and `/api` routes
**Files:** Create `fhir_server/services/sessions.py`, `fhir_server/routes/sessions.py`; Modify `fhir_server/app.py`, `fhir_server/cli.py` (reuse helpers); Test `tests/test_sessions_api.py`.
**Produces:** routes in the spec table; `make_test_patient(svc, label) -> patient`, `open_visit(svc, principal, patient_id, practitioner_ref, label) -> encounter`, `finish_visit(svc, principal, encounter_id)`.
- [ ] Tests: admin registers (201) and re-keys (200, old key 401 on `/api/board/session`); non-admin register 403; admin creates test patient; admin opens session (Encounter in-progress, participant = chosen doctor); board busy 409; doctor not participating 403; doctor participating 201; `/api/board/session` 200 shape, 404 no session, 401 bad key or id mismatch; board key uploads raw chunk 201 during session; end → Encounter finished, upload 403; doctor lists only own sessions; existing `test_cli_capture_session.py` green.
- [ ] Fail, implement, pass. Full pytest green.

### Task 3: Firmware board identity
**Files:** Create `arduino/radar_json/board.h`, `tests/firmware/board_test.cpp`, `tests/test_firmware_board.py`; Modify `arduino/radar_json/radar_json.ino`.
**Produces:** `LineReader::push(char) -> bool` + `line()`, `formatBoardLine(char*, size_t, id, key) -> int`, `isBoardQuery(const char*) -> bool`, `hexId(uint64_t mac, char out[13])`.
- [ ] Host tests: CR/LF handling, overlong line dropped, query match exact, formatted line is valid JSON after the `BOARD ` prefix (checked from Python), MAC bytes formatted in transmission order.
- [ ] Fail, implement, pass. `arduino-cli compile` succeeds.

### Task 4: Page core modules
**Files:** Create `receiver/src/board.js`, `receiver/src/hub.js`, `receiver/src/auth.js`, `receiver/src/nav.js`; Modify `receiver/src/simulator.js`; Tests for each.
**Produces:** `parseBoardLine(line) -> {id,key}|null`; `requestBoard({lines, send}, {timeoutMs=3000, retryMs=1000}) -> {id,key}` (throws `no-reply`); `virtualBoard(storage) -> {id,key}`; `simulatorLines({..., commands})` answers `BOARD?`; `LineHub(iterable)` with `subscribe() -> asyncIterable`, `unsubscribe(sub)`, `run()`; `saveAuth/loadAuth/clearAuth(storage, now)`, `login(fetchFn, user, pass)`; `navItems(path, auth) -> [{href,label,current}]`, `renderNav(el, path, auth)`.
- [ ] Tests per module, fail, implement, pass.

### Task 5: Pages
**Files:** Create `receiver/site.css`, `receiver/sessions.html`, `receiver/sessions.js`; Modify `receiver/index.html`, `receiver/app.js`, `receiver/review.html`, `receiver/review.js`.
- [ ] Capture page per spec panels; Sessions page per spec; nav on all three.
- [ ] Node suite green.

### Task 6: Browser check and docs
- [ ] Headless Chrome on a scratch DB: the spec's end-to-end path, screenshots, console clean.
- [ ] Update `docs/RUN-GUIDE.md`, `fhir_server/README.md` receiver note, `CLAUDE.md` status.
- [ ] All suites green: pytest, node, linter.

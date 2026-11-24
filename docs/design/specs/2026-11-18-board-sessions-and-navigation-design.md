# Board identity, sessions dashboard and site navigation: design

Date: 2026-11-18. Status: approved in conversation ("implement it"); owner chose
"board sends its key when prompted, note the vulnerability for later".

## Why

The capture page needed a session card pasted from a terminal. The card holds a
token, so it ended up on screen, in the terminal and in chat. The owner wants:

- the **board** to identify itself, with an ID unique to that physical board;
- **admins and doctors** to decide on a dashboard which patients and sessions exist,
  and which board records which session;
- the capture page to get its session from the board that is plugged in, with no card
  pasted anywhere;
- **proper navigation** across the pages and their options.

## Who does what

```
Admin, once per board     Capture page: Connect board -> "Register this board"
                          server stores Device (identifier = board ID) + key hash
Admin or doctor           Sessions page: pick or create test patient -> open session
  per subject             (an in-progress Encounter) -> assign a free board
Capture page, each time   Connect board -> page asks "BOARD?" -> board answers ID + key
                          -> server returns that board's open session -> Record
```

## Rulings

| # | Ruling | Why |
|---|---|---|
| B1 | Board ID = ESP32 factory MAC from eFuse, 12 uppercase hex digits | Unique per chip, needs no setup. Owner: "the device also has a unique id" |
| B2 | Board key = 32 random bytes (64 hex) made by the board on first boot, kept in NVS (`Preferences`, namespace `prata`) | The board makes its own secret, so it survives reflashing the sketch (not a full flash erase) |
| B3 | The board sends ID and key whenever it receives the line `BOARD?` | Owner's choice. Vulnerability recorded below |
| B4 | The server stores only the SHA-256 of the key, like device tokens today | A database leak does not leak keys |
| B5 | The board key is the bearer token for uploads. The server maps it to the board's **open session** at request time | No second token to mint and hand out. Ending the session ends the board's write access |
| B6 | One open session per board (unique index). A session is an in-progress Encounter plus a `board_sessions` row | Keeps the FHIR record as the visit, the table as operational state |
| B7 | Roles follow the existing server. **Admin:** register boards, create test patients, open and end any session (choosing the doctor). **Doctor:** open sessions for patients they already take part in, end their own sessions | The walking skeleton limits doctors to patients they participate in. Relaxing that is a privacy decision left to the owner |
| B8 | Test patients only (synthetic NIK `9900…`), as `capture-session` makes today | Real data needs ethics approval (capture spec D10) |
| B9 | The capture page separates **preview** (plot only) from **recording** (plot and upload). Connect starts preview; Record needs an open session | The operator can aim the radar before a session exists, and nothing uploads by accident |
| B10 | The simulator is a **virtual board** that answers `BOARD?` with ID `SIM-` + 8 hex and a key kept in that browser's `localStorage`. It must be registered like a real board | Keeps the hardware-free test path with no shared hard-coded key. Its uploads stay marked `SIMULATED` |
| B11 | JWT kept in `localStorage` (`prata-auth`), shared by all pages and tabs, dropped at its expiry (1 h by default) or on Log out; nothing else about the session is stored | The workflow is Sessions in one tab and Capture in another (leaving the Capture page drops the serial connection). `sessionStorage` is per tab, so it would force a second login. Drafted as `sessionStorage`, changed during implementation |
| B12 | Paste-a-card is removed from the page. `capture-session` stays for the CLI, device client and tests | The page no longer needs it |

## Known vulnerability (for later)

**The board key travels in clear text and is handed out on request.** Any program
that can open the serial port, or any web page the user grants Web Serial access to,
can send `BOARD?`, read the key and act as that board. That means uploading to the
board's open session until an admin re-registers the board with a new key. The
simulated board's key sits in the browser's `localStorage`, readable by any script on
the same origin. HTTP on `127.0.0.1` is not encrypted, which is acceptable only while
everything is local.

**Later fix:** challenge and response. The server sends a one-time nonce through the
page, and the board answers with HMAC-SHA256(key, nonce), so the key never leaves the
board after registration. Registration would reveal the key once, and only after a
press of the board's button. The server side would add a nonce endpoint and HMAC
check; the firmware already has mbedTLS.

## Serial protocol additions

Host to board: `BOARD?\n`. The board ignores any other line, and lines over 63
characters.

Board to host: `BOARD {"id":"AB12CD34EF56","key":"<64 hex>","fw":"radar_json"}\n`.

`READY …` gains `id=AB12CD34EF56` (never the key). The display shows `ID AB12CD34EF56`.
The page treats lines not starting with `{` as non-samples already, so older pages
ignore the new line.

## Server

- **Tables:** `boards(serial PK, device_id UNIQUE, key_sha256 UNIQUE, registered)`,
  `board_sessions(id PK, serial, device_id, patient_id, encounter_id, practitioner,
  label, started, ended NULL)`, with a unique index on `serial WHERE ended IS NULL`.
- **`get_principal`:** after JWT and device tokens, a bearer matching a board key
  gives `Principal(kind="device", device_id, patient_id=<open session's
  "Patient/x"> or None)`. The existing device rules then apply unchanged: own
  Device, assigned patient, in-progress Encounter.
- **Routes (`/api`, JSON, errors as OperationOutcome):**

| Method and path | Who | Does |
|---|---|---|
| `POST /api/board/session` body `{id}` | board key | 200 `{board, device, patient, patientName, encounter, org, label, session}`; 401 unknown key or ID mismatch; 404 no open session |
| `GET /api/boards` | admin, doctor | boards with their open session, if any |
| `POST /api/boards` body `{id, key}` | admin | register (201), or re-key a known ID (200). Creates the Device resource |
| `POST /api/patients` body `{label}` | admin | create a test patient named `Sesi <label>` |
| `GET /api/sessions?open=1` | admin (all), doctor (own) | sessions, newest first |
| `POST /api/sessions` body `{board, patient, label, practitioner?}` | admin, doctor | Encounter arrived then in-progress, plus the session row. 409 if the board is busy |
| `POST /api/sessions/{id}/end` | admin, doctor on it | Encounter finished, session ended |

- Patients and practitioners for the pickers come from the existing FHIR search,
  so a doctor sees only patients they take part in.
- `capture-session` reuses the same test-patient and open-visit helpers.

## Site and navigation

All pages share `site.css` and a top bar from `src/nav.js`:

```
PRATA   Sessions   Capture   Review                 admin (admin) · Log out
```

The current page is highlighted. With no login, the right side shows "Log in", which
goes to Sessions.

**Sessions** (`sessions.html`): a login form when logged out. Otherwise there are four
panels: *Open sessions* (label, patient, board, doctor, started, End button);
*Open a session* (patient, free board, label, doctor for admins); *Test patients*
(admin: create by label); *Boards* (ID, registered, current session).

**Capture** (`index.html`), three panels in order of use:

```
1 Board      [Connect board] [Use simulated board] [Disconnect]
             Board AB12CD34EF56 · Session S001 · Sesi S001        (or: not registered
             [Register this board] for admins / no open session -> Sessions page)
2 Recording  [Record] [Stop recording]   Samples … Chunks confirmed … pending …
3 Display    Method [hybrid] Band [0.5 to 10 Hz]   raw I/Q, movement waveform, I/Q plane
```

**Review**: unchanged apart from the shared bar and styles.

## Errors

| Situation | Behaviour |
|---|---|
| No `BOARD` reply within 3 s (asked once a second) | "This board does not answer BOARD?. Flash the current firmware." Preview keeps running |
| Unknown board | "Board X is not registered." Admins get a Register button |
| No open session | "No open session for board X." Link to Sessions, and a Check again button |
| Session ended while recording | Uploads get 403. The page shows "Session ended; chunks are kept in this browser" |
| JWT expired on Sessions | Back to the login form with "Logged out: session expired" |

Ending a session with chunks still pending in the browser leaves them stuck. They
stay in IndexedDB and are not lost, but they cannot upload. The Sessions page warns
about this on End.

## Testing

TDD throughout. **pytest:** board key principal; register and re-key; one open
session per board; doctor participation rule; end session; `/api/board/session`
codes; `capture-session` unchanged. **Host C++:** `board.h` line reader and
formatter. **Compile:** `arduino-cli compile`. **Node:** board handshake (reply,
retry, timeout), virtual board, line hub (preview and record), auth storage, nav
items. **Headless Chrome:** admin login → simulated board not registered → register
→ test patient → open session → Record → chunks confirmed → End session.

**Not verifiable here:** the real board. No board is connected, so the firmware is
compile-checked and host-tested only.

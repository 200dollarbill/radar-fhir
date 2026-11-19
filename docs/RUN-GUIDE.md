# Run guide: server, board and website

Everything here runs on your laptop. Nothing talks to the real SATUSEHAT.
Commands assume you are in the repo root:

```bash
cd "/mnt/Data/yep/Kuliah/Tugas/Semester 7 ntr lagi lulus/PRATA"
```

## The picture

```
K-LC7 radar ──wires──> AtomS3R (G7=I, G8=Q) ──USB──> Chrome: Capture page ──HTTP──> FHIR server ──> data/fhir_server.db
                        firmware, 100 Hz              (asks the board BOARD?)        127.0.0.1:8000   (SQLite file)
                        own ID + key                  Chrome: Sessions page ─────────┘
```

- The **firmware** samples I/Q plus the IMU 100 times a second and prints one JSON line per
  sample. Asked `BOARD?`, it answers with its own ID and key.
- The **Sessions page** is where an admin or doctor decides which patient is recorded with
  which board (a *session*).
- The **Capture page** reads the board over USB, gets that board's open session from the
  server, plots the signal, and while you record posts 10 s chunks as `raw-capture`
  Observations.
- The **server** checks every Observation and stores it in `data/fhir_server.db`.

## The website at a glance

Every page has the same top bar: **PRATA · Sessions · Capture · Review**, with who is logged
in on the right. Open it at <http://127.0.0.1:8000/capture/sessions.html>.

| Page | Who | What it is for |
|---|---|---|
| **Sessions** | admin, doctor | Log in. See open and ended sessions, open a session (patient + board + label), end one. Admins also create test patients and see all boards |
| **Capture** | anyone at the bedside with the board | Connect the board, see the raw and processed signal, Record and Stop |
| **Review** | anyone | Load a saved recording file and compare the six display methods side by side |

Keep **Sessions and Capture in two tabs**. Leaving the Capture page drops the USB connection.
The login is shared by all tabs and lasts one hour.

## One-time setup (skip if already done)

```bash
make setup
```

### Keep your secrets in one file

The server needs `FHIR_JWT_SECRET`. It tries to save one to `.env`, but in this repo `.env`
is a **folder** (it holds `notes.env`), so the save fails and you get a new random secret
every restart. That logs everyone out. Fix it once: make a file inside that folder (the
whole folder is gitignored, so it never gets committed):

```bash
cat > .env/prata.env <<'EOF'
export FHIR_JWT_SECRET=pick-any-long-random-string
export FHIR_ADMIN_PASSWORD=pick-an-admin-password
EOF
```

`make server` loads this file for you. For the commands you run by hand below (`seed`,
`set-password`, `curl`), run `source .env/prata.env` first in that terminal.

**`FHIR_ADMIN_PASSWORD` is read only when the database is seeded (Step 1).** Changing it
later, or writing `prata.env` after seeding, does not change the stored password. To make
the admin password match `prata.env` without wiping anything:

```bash
source .env/prata.env
.venv/bin/python -m fhir_server set-password --username admin
```

It reads the new password from `FHIR_ADMIN_PASSWORD` (or another variable with
`--from-env NAME`) and never prints it. The same works for `--username doctor` or `patient`.

## Every session, step by step

### Step 1. Database (first time only)

```bash
source .env/prata.env
.venv/bin/python -m fhir_server seed --reset
```

**`--reset` deletes `data/fhir_server.db` and starts fresh.** Run it only the first time, or when
you really want to throw everything away. The last line it prints is a JSON summary with the
passwords (admin, doctor, patient) and IDs. Copy it into `.env/notes.env` if you want to keep
it. Adding tables later (as the session tables were) needs no reset: the server adds missing
tables when it starts.

### Step 2. Start the server (terminal 1, leave it running)

```bash
make server
```

Check it: open <http://127.0.0.1:8000/fhir-r4/v1/metadata>. You should see JSON.
Stop it with `Ctrl+C`. After pulling new server code, restart it; page changes only need a
browser reload.

### Step 3. Flash the firmware (when the firmware code changed)

The board must run firmware from 2026-11-18 or later, or the Capture page says the board
did not answer `BOARD?`. Close anything holding the port first (Arduino Serial Monitor, the
Capture page).

```bash
make flash              # compiles, then uploads to /dev/ttyACM0
make flash PORT=/dev/ttyACM1   # if the board shows up on another port
```

The board screen shows `Pra-TA radar`, `ONLINE` or `SENDING`, the sample counter,
`I pin: 7  Q pin: 8`, and in small text its **ID** (12 characters, from the chip). The key
is made on first boot and kept through later flashes. A full flash erase makes a new key;
then register the board again (Step 5).

### Step 4. Log in (Sessions page)

Open <http://127.0.0.1:8000/capture/sessions.html> and log in.

| Account | Password | Can |
|---|---|---|
| `admin` | `FHIR_ADMIN_PASSWORD` at seed time (see the setup note above) | everything: register boards, create test patients, open and end any session, choose the doctor |
| `doctor` | `doctor-pw` unless `FHIR_DOCTOR_PASSWORD` was set at seed time | open sessions for patients they already take part in, end their own sessions |
| `patient` | `patient-pw` unless `FHIR_PATIENT_PASSWORD` was set at seed time | not this page (FHIR API only, own records) |

*Login failed: wrong username or password* means exactly that. Reloading the page does not
help. Run `set-password` (setup note above).

### Step 5. Register the board (admin, once per board)

1. In a **second tab**, open **Capture** from the top bar. Plug the board in, click
   **Connect board**, pick the AtomS3R port (`/dev/ttyACM0`, often named "USB JTAG/serial
   debug unit").
2. The page asks the board for its ID and shows *Board AB12CD34EF56 is not registered*.
3. Click **Register this board** (shown only while an admin is logged in).

The panel then says *No open session for board ...*. The plots already run, so you can aim
the radar while the session is set up.

### Step 6. Open a session (admin or doctor, once per subject)

On **Sessions**:

1. Admin only, if the subject is new: **Test patients** → label such as `S001` →
   **Create test patient**. It makes a synthetic patient *Sesi S001* with a test NIK.
2. **Open a session**: pick the patient, a free board, a label, and (admin) the doctor →
   **Open session**. The session appears under **Open sessions**, and **Boards** shows the
   board as taken.

A board can have only one open session. Labels are 1 to 32 letters, digits or hyphens.

### Step 7. Record (Capture page)

1. Click **Check again** (or connect the board if it is not). The Board panel turns green:
   *Board AB12CD34EF56 · Session S001 · Sesi S001 · Encounter/...*.
2. Click **Record**. The status line reads *● Recording S001: 12 s · 1 chunk saved so far*
   (a chunk is 10 s and is uploaded as soon as it is full).
3. Click **Stop recording**. The line changes to *Saving S001: 1 chunk left to upload…*, then
   to **✓ Saved: 13 s of S001 (2 chunks) stored on the server at 19:42**. Only then is the
   recording on the server. If the server is down it says *Not saved yet … kept in this
   browser* and finishes by itself when the server is back. The plots keep running until
   **Disconnect**.

### Step 8. End the session (Sessions page)

Only after the Capture page shows **✓ Saved**: click **End**, then **Confirm end**.
The visit (Encounter) is finished, the board is free again, and the board can no longer
upload into that session. Ended sessions are listed at the bottom.

### Step 9. Read the movement waveform (Capture, Display panel)

**Movement waveform** turns the last 10 s of I and Q into one trace of skin movement (blue:
pulse band, orange: breathing). It is display processing only, in relative units, not a
measurement. The square on the right is the I/Q plane: a clean arc means the radar sees
movement; a blob or a grid of dots means the signal is too weak or the radar is aimed at
nothing. The grey line under it says which method ran and why. Keep the method on
**hybrid** (the evaluated default) unless you are comparing.

To compare all six methods on a saved recording, open **Review** and pick a file: a
firmware CSV such as `data/rabits_Sep_15_1519.csv`, or the JSON saved in Step 10.

### Step 10. Check what was stored

The patient ID is the part after `·` in the Sessions patient list (`Sesi S001 · P123...`).

```bash
source .env/prata.env
ADM=$(curl -s http://127.0.0.1:8000/auth/token \
  -H 'Content-Type: application/json' \
  -d "{\"username\":\"admin\",\"password\":\"$FHIR_ADMIN_PASSWORD\"}" \
  | python3 -c 'import sys,json;print(json.load(sys.stdin)["access_token"])')
curl -s -H "Authorization: Bearer $ADM" \
  "http://127.0.0.1:8000/fhir-r4/v1/Observation?subject=Patient/<patient id>&_count=100" \
  > capture.json
```

Each `raw-capture` Observation holds up to 10 s: 8 channels (I, Q, accel x/y/z, gyro x/y/z)
as space-separated numbers in `component[].valueSampledData.data`. An `E` in the data means
a missing sample. Load `capture.json` on the Review page to see it.

## No board? Use the simulated board

On Capture, **Use simulated board** behaves like a real board: it has an ID `SIM-xxxxxxxx`
and a key kept in this browser, answers `BOARD?`, and must be registered and given a session
like a real one. A red **SIMULATED** banner shows, and its chunks are marked `SIMULATED`.

## Troubleshooting

| You see | Why | Do |
|---|---|---|
| *Login failed: wrong username or password* | The stored password is the one from seed time | `set-password` (setup note) |
| *The board did not answer BOARD?* | Old firmware on the board | Flash the current firmware (Step 3) |
| *Board ... is not registered* and no Register button | Not logged in as admin, or logged in another way | Log in as admin on Sessions, then **Check again** |
| *No open session for board ...* | No session uses this board | Open one on Sessions (Step 6), then **Check again** |
| *The server refused the board key* | The session ended, or the board was registered again | Open a new session; chunks already recorded stay in the browser |
| *N chunks belong to another session* | Chunks recorded under an earlier session wait in the browser | Open that session's board again to send them; they upload only while that session is open |
| *Could not open serial port* | Another program holds the port | Close the Arduino Serial Monitor or any terminal reading `/dev/ttyACM0` |
| Uploads fail with 405 | Page opened from VS Code Live Server (`:5500`) | Use `http://127.0.0.1:8000/capture/` |
| *Updating outdated files in the browser cache, then reloading…* | The browser had an old copy of a page file next to new ones | Nothing: the page re-downloads its files and reloads itself |
| *This page failed to load (…)* | The automatic repair did not help (tried twice) | Reload with **Ctrl+Shift+R**. If that does not help, restart the server |
| Connect board shows *No port selected* | The port picker was closed without choosing | Click Connect board again and pick the AtomS3R port |

## Where things are saved

| What | Where | Notes |
|---|---|---|
| All server data | `data/fhir_server.db` | SQLite, one file, gitignored. `seed --reset` deletes it. Point elsewhere with `--db <path>` before the subcommand or `FHIR_DB_PATH` |
| Recordings | `data/fhir_server.db`, `Observation` rows | No separate CSV or WAV file is written |
| Boards and sessions | `data/fhir_server.db`, tables `boards` and `board_sessions`; each board is also a `Device`, each session an `Encounter` | Only a hash of each board key is stored |
| Chunks not yet uploaded | Chrome's IndexedDB, database `prata-capture`, per page address | Kept if the server is down or the tab closes |
| Login | Chrome `localStorage`, `prata-auth` | Shared by all tabs; gone after one hour or Log out |
| Simulated board's ID and key | Chrome `localStorage`, `prata-virtual-board` | One per browser profile |
| Real board's key | The board's flash (NVS, namespace `prata`) | Survives reflashing the sketch |
| Secrets | `.env/prata.env` (you make it), `.env/notes.env` | Gitignored |
| WiFi and token for the firmware | `firmware/radar_json/config.h` | Gitignored. Only for WiFi heart-rate posting, a placeholder 72 bpm, not a measurement |
| Code | `fhir_server/` (server), `website/` (served at `/capture/`), `firmware/radar_json/` (firmware) | See the folder map in `README.md` |

## Pointing the radar

The K-LC7 is a 24 GHz radar. It only sees **movement** toward or away from its face (the
side with the antenna patches). Face down on a desk it sees a still desk, so you get a
flat line plus noise. To record a person, point the patch side at the chest or neck from
roughly 20 to 50 cm, and keep the board and cables still, because moving cables also show up.

The module has two receivers (I1/Q1 and I2/Q2). Write down which pair goes to G7 and G8.

## Known weakness (for later)

The board hands its key to anything that sends `BOARD?` over the USB port, so any program
on this PC with access to the port could copy it and upload as that board while it has an
open session. The simulated board's key sits in the browser's `localStorage`. The planned
fix is challenge and response, so the key never leaves the board: see
`docs/design/specs/2026-11-18-board-sessions-and-navigation-design.md`.

## Known quirks

- **The login curl needs `-H 'Content-Type: application/json'`.** Without it the server
  answers "Authentication failed".
- **The first few samples can be old.** While nothing reads the USB port, the board keeps a
  small backlog. When you connect, that backlog arrives first, stamped with the current
  time. Recording starts only when you click Record, which usually skips it.
- **`device_missed` in each chunk's note counts since the board powered on**, not since you
  pressed Record. A big number mostly means the port sat unread for a while.
- **Search results are not sorted.** Order chunks by the number at the end of their
  identifier (`...-segment-chunk`). The Review page does this for you.
- Unplugging the board resets nothing on the server. Restarting the server keeps all data
  (only `seed --reset` wipes it).
- The terminal card (`capture-session --label S001`) still works for the device client and
  tests. The page no longer takes a pasted card.

## Tests

```bash
make test     # server (plus firmware host tests), website, scraper, view linter
make eval     # rescore the display methods (rewrites docs/eval/)
```

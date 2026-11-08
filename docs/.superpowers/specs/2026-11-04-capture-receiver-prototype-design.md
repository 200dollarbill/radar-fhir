# Capture receiver and backend prototype: design

Date: 2026-11-04. Status: approved; implemented as prototype.

## Purpose

A browser page reads raw radar samples from a board over USB serial, shows them
live, and uploads them to the FHIR server as Observations. This proves the path
device → connected computer → server for raw 100 Hz data. It is a pipeline
prototype, not a measurement: it produces no JVP result and no interpretation.

## Scope

In scope:

- `receiver/`: the capture page, with a serial source and a simulator source.
- `fhir_server/`: a raw-capture Observation rule, conditional create, serving the
  page, and a `capture-session` CLI command.

Out of scope for this prototype:

- **Cloudflare Tunnel, Access and nginx.** Everything runs on the owner's Linux
  computer at `http://127.0.0.1:8000`. Web Serial accepts localhost as a secure
  context, and page and API share an origin, so adding the tunnel later needs no
  page changes. The tunnel stays the chosen hosting route.
- **Firmware format changes.** The page reads the format `arduino/radar_json/radar_json.ino`
  already emits. Amended after the hardware test: the sketch's sample timing was fixed
  (`sample_idx` is now a time slot, so lost time is a visible gap), with the line format unchanged.
- **Bluetooth.** The RABITS BLE protocol below is recorded for later use. The
  owner's Bluetooth is broken, so it cannot be tested now.
- **JVP processing, ECG, RME and the doctor dashboard.**
- **Viewing stored captures.** The live plot covers the capture itself.

## Decisions

| # | Decision | Why |
|---|---|---|
| D1 | Web Serial page in Chrome, not a Python client | Reusable in the eventual website. Owner chose a web client; serial replaces Bluetooth for now |
| D2 | One Observation per chunk of up to 1000 samples (10 s), with `SampledData` components | Keeps FHIR canonical and reuses auth and validation |
| D3 | Store values exactly as received (volts, g, deg/s) | The serial format has no raw ADC counts. This replaces the earlier idea of storing counts with a `factor` |
| D4 | Chunk boundaries come from `sample_idx`, not `epoch_id` | `radar_json.ino` never increments `epoch_id` |
| D5 | Retries use R4 conditional create, `If-None-Exist: identifier=<value>` | Server mints IDs and device tokens cannot update. Source: `docs/reference/claude/fhir-rest-api.md:38` |
| D6 | Local code system `urn:prata:radar-signal` | No standard code for radar I/Q was found. Added to `ALLOWED_SYSTEMS` |
| D7 | Raw chunks carry no `category` | The rule accepts only `vital-signs` when a category is present, and raw I/Q is not a vital sign. `category` is 0..* in R4 |
| D8 | Time comes from the computer's clock when a chunk's first sample arrives | The firmware's `t_host_unix` is `millis()` since boot, not Unix time |
| D9 | FastAPI serves the page at `/capture/` | One process for the prototype. nginx can serve the same files later |
| D10 | Synthetic subjects only, identified by a session code | Ethics approval and UU PDP data-location questions are unresolved |

## Architecture

```
board ─USB─> Web Serial ┐
simulator ──────────────┴─> jsonlines parser ─> chunker ─> outbox (IndexedDB)
                                     │                         │
                                     └─> live plot             └─> uploader
                                                                    │ POST + If-None-Exist
                                                                    ▼
                                                     FastAPI ─> SQLite (127.0.0.1:8000)
```

### Receiver modules (`receiver/`)

Plain ES modules with no build step and no npm dependencies.

| File | Job | Depends on |
|---|---|---|
| `src/serial.js` | Open port at 115200, yield text lines | Web Serial API |
| `src/simulator.js` | Yield the same lines at 100 Hz from a synthetic I/Q signal | nothing |
| `src/jsonlines.js` | Line → validated sample, or a counted rejection | nothing |
| `src/chunker.js` | Samples → chunks; handles gaps and segments | nothing |
| `src/observation.js` | Chunk + session card → Observation JSON | nothing |
| `src/outbox.js` | Durable FIFO of chunks behind a small store interface | store |
| `src/uploader.js` | Send outbox chunks, classify responses | `fetch`, outbox |
| `src/plot.js` | Scrolling canvas of the last 10 s of I and Q | canvas |
| `app.js`, `index.html` | Wiring and status display | all above |

The simulator is labelled "SIMULATED" on screen and in the Observation's `note`.

### Serial line format (input)

From `radar_json.ino`, one JSON object per line, about 100 lines per second:

`epoch_id, sample_idx, t_host_unix, fs, crc_ok, missed, I, Q, ax, ay, az, gx, gy, gz`

Field rules mirror `python_receiver/models.py`. Non-JSON lines such as
`READY radar_json…` and `ingest POST -> 201` are ignored without counting as
errors when they do not start with `{`. A line starting with `{` that fails
validation counts as rejected.

`crc_ok` is hard-coded true in the firmware (both branches of the ternary), so
serial data has **no real integrity check** beyond JSON and field validation.
`crc_ok: false` is still honoured as a rejection.

### Observation shape

```json
{
  "resourceType": "Observation",
  "status": "final",
  "identifier": [{"system": "http://sys-ids.kemkes.go.id/organization/<org>",
                  "value": "<captureId>-<segment>-<chunkIndex>"}],
  "code": {"coding": [{"system": "urn:prata:radar-signal",
                       "code": "raw-capture",
                       "display": "Raw radar I/Q capture"}]},
  "subject": {"reference": "Patient/<id>"},
  "encounter": {"reference": "Encounter/<id>"},
  "device": {"reference": "Device/<id>"},
  "effectiveDateTime": "<first sample, computer clock, UTC>",
  "note": [{"text": "{\"source\":\"serial\",\"gap_samples\":0,\"rejected_lines\":0,\"device_missed\":0}"}],
  "component": [{
    "code": {"coding": [{"system": "urn:prata:radar-signal", "code": "i-voltage"}]},
    "valueSampledData": {
      "origin": {"value": 0, "unit": "V",
                 "system": "http://unitsofmeasure.org", "code": "V"},
      "period": 10, "dimensions": 1, "data": "1.650000 1.651000 E 1.649000"
    }
  }]
}
```

Components: `i-voltage`, `q-voltage` (V), `accel-x/y/z` (UCUM `[g]`) and
`gyro-x/y/z` (`deg/s`). `period` is `1000 / fs` milliseconds. A chunk is about
80 KB of JSON, or about 29 MB per hour.

Later JVP results become separate Observations whose `derivedFrom` points at these
chunks, so raw data needs no migration.

### Server changes

- **`rules_observation.py`:** dispatch on code. Keep the heart-rate rule unchanged.
  The new raw-capture rule shares the status, subject, encounter, device and
  identifier checks, and adds:
  - no `value[x]` at the top level;
  - `i-voltage` and `q-voltage` required, all component codes from the known set,
    no duplicates;
  - every component uses `valueSampledData` with `dimensions` = 1, `period` > 0,
    and the same `period` as the others;
  - every `data` token is a decimal or `E`/`L`/`U`, with 1 to 1000 tokens, and the
    same count in every component;
  - exactly one identifier with a non-empty value.
- **`rules_common.py`:** add `urn:prata:radar-signal` to `ALLOWED_SYSTEMS`.
- **Conditional create (Observation only):** `POST` accepts
  `If-None-Exist: identifier=<value>` or `identifier=<system>|<value>`.
  - No match: validate, create, record the key, return `201`.
  - Match: return `200` with the stored resource after an authorization read
    check. A different device's record returns `403`.
  - Any other parameter in the header: `400`.
  - Lookup uses a new table `conditional_keys(type, identifier_value, resource_id,
    PRIMARY KEY (type, identifier_value))`. It holds only keys from conditional
    creates, because the existing client reuses `radar-1` on plain POST and that
    behaviour must keep working. Scanning `resources` is not viable at 80 KB a row.
  - The header carries the value only. The client's `organization/<org>` system is
    rewritten on mint, so matching on it would miss.
- **`app.py`:** mount `receiver/` at `/capture/` as static files.
- **`cli.py capture-session --label S001`:** with the seeded Organization, Location,
  Practitioner and Device, creates a synthetic Patient (generated 16-digit NIK, as
  the validator requires, with the label as its name), an in-progress Encounter
  and a device token through `FhirService`, so normal validation runs. Prints one
  JSON session card: `{token, patient, encounter, device, org, label}`. Fails with
  a clear message if the database is not seeded.

## Data flow

1. Owner runs `capture-session` and pastes the card into the page. The card is kept
   in `sessionStorage`, so closing the tab drops the token.
2. Owner clicks Connect (Web Serial needs a user gesture) or Start simulator. The
   page generates a new `captureId`.
3. Each valid sample updates the plot and enters the chunker.
4. A full chunk is built into an Observation and written to the outbox **before** any
   upload attempt.
5. The uploader sends the oldest chunk and deletes it only after a `200` or `201`.
6. Stop flushes the partial chunk and uploads continue until the outbox is empty. The
   status line reads: samples received, chunks confirmed, chunks pending, gaps,
   rejected lines.

## Error handling

| Situation | Behaviour |
|---|---|
| `sample_idx` jumps by fewer than 1000 | Fill the gap with `E` in every channel, add to `gap_samples` |
| `sample_idx` jumps by 1000 or more, or goes backwards (reboot) | Flush the chunk, start a new segment |
| `fs` changes | Flush the chunk, start a new segment |
| Malformed `{…}` line or `crc_ok: false` | Add to `rejected_lines`. The missing index then becomes an `E` gap |
| Serial port disappears | Flush the chunk, show "disconnected", no auto-reconnect |
| Network failure or `5xx` | Keep chunk, retry with backoff 1 s to 30 s, capture continues |
| `401` or `403` | Pause uploads, show "token invalid, paste a new card", keep chunks |
| Other `4xx` | Mark chunk rejected, keep it in the outbox, show the OperationOutcome text and count, move to the next chunk |
| Encounter no longer in progress | Rejected by the existing rule, handled as the row above |
| IndexedDB quota exceeded | Stop capture and show an error. Never drop data silently |
| Tab reopened with chunks pending | Page reports them and uploads after a card is pasted. Chunks already hold their references |

## Testing

All TDD. Baseline before this work: 134 server tests pass.

- **Node (`node --test "receiver/tests/*.test.js"`):** parser, chunker (gap, reboot, `fs` change,
  flush), Observation builder, outbox with an in-memory store, uploader response
  classes with a fake `fetch`, simulator line format.
- **Contract:** a test feeds the simulator's lines and a line in the exact
  `radar_json.ino` printf shape through the parser, so the formats cannot drift.
- **Pytest:** raw-capture rule accept and reject cases, conditional create (`201`
  then `200`, other device `403`, bad header `400`), plain POST reuse of an identifier
  still allowed, static route, `capture-session`. All existing tests stay green.
- **End to end (`tests/test_capture_e2e.py`):** Node builds a real chunk, the test
  posts it twice, gets `201` then `200`, reads it back and compares every sample.
- **Manual browser check:** simulator in real Chrome through to stored Observations.
  This is the only coverage of real IndexedDB, Web Serial permission and canvas.

## Acceptance

1. All automated tests pass.
2. In Chrome, the simulator runs for at least 60 s, and the stored Observations hold
   all samples with none duplicated, including after stopping the server mid-run and
   restarting it.
3. Hardware smoke test, run with the owner since the port picker needs a click: flash
   `radar_json.ino` to the **spare blank board**, connect, see lines reach the server.

The board's ADC pins are placeholders and no radar wiring is confirmed, so test 3
proves the data path only. Its values are not radar signal and must not be reported
as such.

## Known limits

- **USB output is unverified.** Native USB serial on the AtomS3R depends on the build
  option `USB CDC On Boot`. If the port stays silent, check this first.
- **Search scales poorly.** `res.list` parses every stored Observation on each search,
  and `_count` caps at 100 with no paging. Acceptable for this prototype. The dashboard
  will need a summary or paged read.
- **The server PC must be running** to accept uploads. Chunks wait in the browser.
- **Only full chunks reach the outbox,** so a crash or reload mid-capture loses up to 10 s.
- **Create and key insert commit separately,** so a crash in that window can duplicate
  one chunk on retry.
- **Other-session or rejected chunks have no discard path.** Clear site data to remove them.
- **The RABITS firmware format differs** from what this page parses (below).

## Later: RABITS BLE protocol

Static JADX reading of `com.rabits.app` v0.6.5, not tested on hardware. A future
`src/ble.js` plus an epoch parser would feed the same chunker. The prof's firmware
source would settle what is inferred here.

- **Connection:** device name contains `RABITS`. Service
  `6e400001-b5a3-f393-e0a9-e50e24dcca9e`, RX write `…0002`, TX notify `…0003`, LIVE
  notify `…0004` (optional). Write ASCII `READY` to arm. The app refuses MTU below 243;
  whether Windows reaches that under Web Bluetooth is untested.
- **Framing on TX:** ASCII header `EPI|EPO,epochId,nSamples,fs,vRef,adcMax,missed`, then
  binary body of nSamples × stride bytes, then ASCII `END,<crc32 hex>` over the body.
- **Body, little-endian:** `EPO` stride 4 is I, Q as u16. `EPI` stride 16 adds ax, ay, az
  as i16 / 1000 (g) and gx, gy, gz as i16 (deg/s). Volts = raw × vRef / adcMax.

That format carries raw counts and a real CRC, so D3 would change for BLE captures
(`factor` = vRef / adcMax, origin 0).

## Relation to other specs

`2026-10-08-public-exposure-request-history-design.md` remains the plan for the tunnel,
Access, nginx and audit log. Its decision to defer raw I/Q (P10) is settled by this
spec for browser uploads. Its device WebSocket (P9, P11) is not used here.

# Capture Receiver and Backend Prototype Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** A Chrome page reads raw radar samples over USB serial (or a simulator), plots them live, and uploads them as FHIR Observations that survive retries and server outages.

**Architecture:** Plain ES modules in `receiver/`, served by the existing FastAPI app at `/capture/`. Pure modules (parser, chunker, builder, outbox, uploader, controller) are tested under Node; browser-only code stays in thin files checked by hand. The server gains a raw-capture validation rule, R4 conditional create and a `capture-session` CLI command.

**Tech Stack:** Python 3 / FastAPI / SQLite / pytest (existing). Browser JavaScript with Web Serial, IndexedDB and canvas. `node --test` (Node 22). No npm dependencies and no build step.

**Spec:** `docs/.superpowers/specs/2026-11-04-capture-receiver-prototype-design.md`

## Global Constraints

- Everything runs at `http://127.0.0.1:8000`. No Cloudflare, nginx or Bluetooth in this plan.
- Firmware is not changed. `arduino/radar_json/radar_json.ino` is the input format.
- Never label output as JVP, diagnosis, or a measurement. Simulated data carries `"source":"SIMULATED"` in `note` and "SIMULATED" on screen.
- Synthetic subjects only.
- Code system: `urn:prata:radar-signal`. Top-level code `raw-capture`, display `Raw radar I/Q capture`. Component codes `i-voltage`, `q-voltage` (UCUM `V`), `accel-x`, `accel-y`, `accel-z` (UCUM `[g]`), `gyro-x`, `gyro-y`, `gyro-z` (UCUM `deg/s`).
- Chunk limit: 1000 samples at most. `period` = `1000 / fs` ms. No `category` on raw chunks.
- Serial baud 115200.
- Commit message ending: `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`.
- Commands: `.venv/bin/python -m pytest tests -q` and `node --test receiver/tests/`. Baseline: 134 pytest tests pass.

**Facts the code imposes, not stated in the spec:**

- `canonicalize_datetimes` truncates to whole seconds, so `effectiveDateTime` has 1 s resolution. Order within a capture comes from segment and chunk index.
- Encounters must be created as `arrived`, then moved to `in-progress` with a PUT.
- Values are written with JavaScript's number-to-string, so `1.650000` is stored as `1.65`. The value is identical and chunks are slightly smaller.
- `captureId` is `cap-<uuid>`. The prefix stops an identifier from looking date-shaped to `check_datetimes`.

## Review Focus

1. A tab reopened with pending chunks from session S001 and a card for S002 is pasted: S002 uploads normally and S001's chunks wait, reported on screen, instead of blocking the queue on `403`. Test in Task 6.
2. A chunk is retried after its Encounter finished, because the first response was lost: the server returns `200` with the stored record, not a rejection. Test in Task 2.
3. Serial reads split lines anywhere, the port opens mid-line, lines end in CRLF, and a stream can lack newlines: only complete lines are parsed and memory stays bounded. Test in Task 4.
4. A board reboots mid-chunk, or a gap crosses a chunk boundary: no samples lost, no chunk over 1000, and all channels stay equal in length. Tests in Task 5.
5. The owner pastes garbage, an empty string, or a seed summary instead of a session card: a clear message and nothing uploaded. Test in Task 7.

---

### Task 1: Raw-capture validation rule

**Files:**
- Modify: `fhir_server/validation/rules_observation.py`, `fhir_server/validation/rules_common.py`, `.gitignore`
- Test: `tests/test_rules_observation.py`

**Interfaces:**
- Produces: `validate_observation` keeps its signature and dispatches on `code.coding[0]`. Constants `RAW_SYSTEM = "urn:prata:radar-signal"`, `RAW_CODE = "raw-capture"`.

- [ ] **Step 1: Write failing tests** in `tests/test_rules_observation.py`.

Add a helper `raw(**kw)` returning a valid chunk with all eight components of three samples, plus:

```python
def test_raw_capture_valid(): assert errs(raw()) == []
def test_raw_accepts_error_tokens():  # data "1.65 E -0.5"
def test_raw_requires_i_and_q():      # drop q-voltage -> issue
def test_raw_rejects_unknown_component_code():
def test_raw_rejects_duplicate_component_code():
def test_raw_rejects_top_level_value():   # valueQuantity present -> issue
def test_raw_rejects_non_sampled_component():  # valueQuantity in a component
def test_raw_rejects_dimensions_not_one():
def test_raw_rejects_period_zero():
def test_raw_rejects_mismatched_period():
def test_raw_rejects_mismatched_sample_count():
def test_raw_rejects_bad_token():     # data "1.65 abc"
def test_raw_rejects_nan_token():     # data "1.65 NaN"
def test_raw_accepts_exponent_token():  # data "1e-7"
def test_raw_rejects_over_1000_samples():  # 1001 tokens
def test_raw_accepts_exactly_1000_samples():
def test_raw_rejects_empty_data():
def test_raw_requires_exactly_one_identifier():  # 0 and 2 -> issue
def test_raw_requires_identifier_value():
def test_raw_keeps_device_rule():     # wrong device_ref -> issue, as heart rate
def test_raw_keeps_finished_encounter_rule():
def test_heart_rate_code_still_required_for_other_codes():  # LOINC other than 8867-4 still rejected
```

Each reject test asserts at least one issue whose `expression` starts with `Observation`.

- [ ] **Step 2: Run to verify failure**

Run: `.venv/bin/python -m pytest tests/test_rules_observation.py -q`
Expected: new tests FAIL with a code-not-found issue on valid raw payloads. Existing tests pass.

- [ ] **Step 3: Implement.** Split `validate_observation` into shared checks (status, subject, encounter, device, assignment, identifier system) and two branches: `_heart_rate_rules` (existing code, category and `valueQuantity` checks unchanged) and `_raw_capture_rules`. Use `L_OBSERVATION_VALUE` as the rule number. Data tokens match `^-?\d+(\.\d+)?([eE][+-]?\d+)?$` or are exactly `E`, `L`, `U`. JavaScript can write very small numbers like `1e-7`, so the exponent form must pass.

Add `"urn:prata:radar-signal"` to `ALLOWED_SYSTEMS`. Add `apk/` to `.gitignore`.

- [ ] **Step 4: Run to verify pass**

Run: `.venv/bin/python -m pytest tests -q`
Expected: all pass, including the original 134.

- [ ] **Step 5: Commit**

```bash
git add fhir_server/validation/rules_observation.py fhir_server/validation/rules_common.py tests/test_rules_observation.py .gitignore docs/.superpowers/plans/2026-11-04-capture-receiver-prototype.md
git commit -m "feat(server): validate raw radar capture Observations"
```

---

### Task 2: Conditional create

**Files:**
- Modify: `fhir_server/db.py`, `fhir_server/services/fhir_service.py`, `fhir_server/routes/fhir.py`, `fhir_server/app.py` (CapabilityStatement)
- Test: `tests/test_conditional_create.py`

**Interfaces:**
- Consumes: raw rule from Task 1.
- Produces: `FhirService.conditional_create(principal, resource_type, payload, if_none_exist: str) -> tuple[str, dict, bool]` returning `(id, doc, created)`. Table `conditional_keys(type TEXT, identifier_value TEXT, resource_id TEXT, PRIMARY KEY (type, identifier_value))`. Route status `201` when created, `200` otherwise. `FhirService.create` is unchanged.

- [ ] **Step 1: Write failing tests** in `tests/test_conditional_create.py`, using the `client` pattern from `tests/test_routes.py`: seed an org, patient, in-progress Encounter and device token.

```python
def test_first_post_201_second_200_same_id():
def test_second_post_stores_no_new_row():  # count of Observation rows stays 1
def test_system_pipe_value_form_matches_value_only_key():
    # header "identifier=<sys>|v" after a post with "identifier=v" -> 200
def test_retry_after_encounter_finished_returns_200():  # Review Focus 2
def test_other_device_gets_403_not_the_record():
def test_header_param_other_than_identifier_400():
def test_malformed_header_400():       # "identifier" and "identifier="
def test_header_value_not_in_payload_400():  # cannot poison another chunk's key
def test_non_observation_type_400():
def test_invalid_payload_400_records_no_key():  # corrected retry then gets 201
def test_key_of_deleted_resource_creates_again():  # admin DELETE, then POST -> 201
def test_plain_post_may_reuse_identifier():  # two plain POSTs "radar-1" -> both 201
def test_plain_post_ignores_conditional_keys():  # conditional then plain, same value -> 201
```

- [ ] **Step 2: Run to verify failure**

Run: `.venv/bin/python -m pytest tests/test_conditional_create.py -q`
Expected: FAIL. The second POST returns `201`.

- [ ] **Step 3: Implement.** Add the table to `SCHEMA`. It is `IF NOT EXISTS`, so existing databases gain it at `init`.

`conditional_create` order:
1. Parse the header. Accept exactly one `identifier=` parameter, taking the part after `|` when present. Otherwise raise `FhirError` with `400`.
2. Reject any type other than Observation with `400`.
3. Require the value to equal a `payload.identifier[].value`, otherwise `400`.
4. Look up the key. On a hit with a live resource, run `authz.check(principal, "read", ...)` and return `(id, doc, False)`. This comes **before** validation so Review Focus 2 holds.
5. On a hit with a deleted resource, delete the key and continue.
6. Call `self.create(...)`, insert the key, return `(id, doc, True)`.

In the `create` route, read the payload first, then branch on `request.headers.get("If-None-Exist")`. Everything after the `await` runs without yielding on the single event loop, so two retries cannot interleave.

Set `conditionalCreate: true` on the Observation entry of the CapabilityStatement.

- [ ] **Step 4: Run to verify pass**

Run: `.venv/bin/python -m pytest tests -q`
Expected: all pass.

- [ ] **Step 5: Commit**

```bash
git add fhir_server/db.py fhir_server/services/fhir_service.py fhir_server/routes/fhir.py fhir_server/app.py tests/test_conditional_create.py
git commit -m "feat(server): conditional create for Observation retries"
```

---

### Task 3: `capture-session` CLI

**Files:**
- Modify: `fhir_server/cli.py`
- Test: `tests/test_cli_capture_session.py`

**Interfaces:**
- Produces: `python -m fhir_server capture-session --label S001`. The last stdout line is JSON `{"token","patient":"Patient/<id>","encounter":"Encounter/<id>","device":"Device/<id>","org","label"}`.

- [ ] **Step 1: Write failing tests**, using `run_cli` as in `tests/test_cli_seed.py`.

```python
def test_card_has_all_fields_and_references():
def test_card_can_post_a_raw_chunk():  # valid raw chunk with this token -> 201
def test_doctor_can_read_the_chunk():  # seeded doctor reads the Observation -> 200
def test_two_sessions_get_different_patients():
def test_same_label_twice_succeeds():
def test_unseeded_db_exits_1_with_message():
    assert p.returncode == 1 and "seed" in p.stderr
def test_bad_label_rejected():  # "a b", "" -> nonzero exit, nothing created
```

- [ ] **Step 2: Run to verify failure**

Run: `.venv/bin/python -m pytest tests/test_cli_capture_session.py -q`
Expected: FAIL with an argparse error (invalid choice).

- [ ] **Step 3: Implement `cmd_capture_session(args)`.** Label must match `^[A-Za-z0-9-]{1,32}$`.

Take the first Organization, Location, Practitioner and Device from `resources.list`. If any is missing, print `database not seeded: run "seed" first` to stderr and exit 1.

Use `FhirService(conn, Settings.from_env(db_path=args.db))` with `Principal(kind="admin")`:
- **Patient:** NIK `"9900"` + 12 random digits, which is not a real province code and so marks it synthetic. Retry on collision. Name text `Sesi <label>`, and `birthDate`, `gender`, `multipleBirthBoolean` and `address` with `administrativeCode` copied in shape from `cmd_seed`. The validator requires these fields, and their values are placeholders.
- **Encounter:** create as `arrived` with one history entry, identifier value `capture-<label>-<8 hex>`, and `participant` naming the Practitioner. Then `update` to `in-progress` with the history extended.
- **Token:** `provision_device`.

- [ ] **Step 4: Run to verify pass**

Run: `.venv/bin/python -m pytest tests -q`
Expected: all pass.

- [ ] **Step 5: Commit**

```bash
git add fhir_server/cli.py tests/test_cli_capture_session.py
git commit -m "feat(server): capture-session command prints a session card"
```

---

### Task 4: Line parsing and simulator

**Files:**
- Create: `receiver/src/jsonlines.js`, `receiver/src/simulator.js`
- Test: `receiver/tests/jsonlines.test.js`, `receiver/tests/simulator.test.js`

**Interfaces:**
- Produces:
  - `parseLine(line: string) -> {kind:"ignored"} | {kind:"rejected", reason:string} | {kind:"sample", sample:Sample}`
  - `Sample = {sampleIdx, fs, missed, I, Q, ax, ay, az, gx, gy, gz}`, all numbers
  - `FIELDS`: the 14 serial field names
  - `class LineSplitter { push(text: string) -> string[] }`
  - `simulatorLines({fs=100, now=Date.now, sleep}) -> AsyncGenerator<string>`
  - `formatLine(sampleIdx, fs, values) -> string`

- [ ] **Step 1: Write failing tests**

```js
// jsonlines.test.js
test("valid firmware line gives a sample")
test("READY banner and ingest text are ignored, not rejected")
test("blank line is ignored")
test("broken {json is rejected")
test("missing field is rejected, naming it")
test("non-integer sample_idx or fs is rejected")
test("negative sample_idx and fs of 0 are rejected")
test("string I value is rejected")
test("crc_ok:false is rejected with reason crc_ok")
test("JSON array starting [ is ignored")  // does not start with {

// Contract: the firmware's printf keys equal FIELDS
test("FIELDS match radar_json.ino", () => {
  const ino = readFileSync("arduino/radar_json/radar_json.ino", "utf8");
  const keys = [...ino.matchAll(/\\"(\w+)\\":/g)].map(m => m[1]);
  assert.deepEqual(keys, FIELDS);
});

// LineSplitter, Review Focus 3
test("a line split across pushes comes out once, whole")
test("two lines in one push come out in order")
test("CRLF is stripped")
test("a partial line stays buffered")
test("a mid-line start parses as ignored")  // '":1.2,"Q":3}\n'
test("over 4096 chars without newline is emitted and the buffer resets")

// simulator.test.js
test("each line parses to a sample with consecutive sampleIdx")
test("I and Q stay inside 0 to 3.3 V")
test("emits elapsed×fs lines after a long sleep, catching up")  // fake clock
```

- [ ] **Step 2: Run to verify failure**

Run: `node --test receiver/tests/`
Expected: FAIL with module not found.

- [ ] **Step 3: Implement.** Field rules mirror `python_receiver/models.py` plus `sample_idx >= 0` and `fs > 0`. A trimmed line not starting with `{` is `ignored`.

Simulator signal, from the app's `SimRadar`: `I = 1.65 + 0.4·cos(phase + 0.6)`, `Q = 1.65 + 0.4·sin(phase + 0.6)`, phase = respiration sine + pulse + small noise. IMU values fixed at `az = 1`, others 0. Each tick, yield `floor(elapsed × fs) − emitted` lines so a throttled background tab catches up.

- [ ] **Step 4: Run to verify pass**

Run: `node --test receiver/tests/`
Expected: all pass. Run from the repo root, because the contract test reads a repo path.

- [ ] **Step 5: Commit**

```bash
git add receiver/src/jsonlines.js receiver/src/simulator.js receiver/tests/
git commit -m "feat(receiver): parse serial lines and simulate the device"
```

---

### Task 5: Chunker and Observation builder

**Files:**
- Create: `receiver/src/chunker.js`, `receiver/src/observation.js`
- Test: `receiver/tests/chunker.test.js`, `receiver/tests/observation.test.js`

**Interfaces:**
- Consumes: `Sample` from Task 4.
- Produces:
  - `class Chunker { constructor({chunkSize=1000, now=Date.now, onChunk}); addSample(sample); noteRejected(); flush() }`
  - `Chunk = {segment, chunkIndex, fs, startTimeMs, channels:{I,Q,ax,ay,az,gx,gy,gz}, gapSamples, rejectedLines, deviceMissed}`. Channel arrays hold numbers or `"E"`.
  - `identifierValue(captureId, chunk) -> string`, `<captureId>-<segment>-<chunkIndex>`
  - `buildObservation(chunk, card, {captureId, source}) -> object`. `source` is `"serial"` or `"SIMULATED"`.

- [ ] **Step 1: Write failing tests**

```js
// chunker.test.js
test("1000 samples emit one chunk; chunk 2 gets index 1")
test("gap of 3 fills 3 E in every channel and counts gapSamples 3")
test("gap crossing a chunk boundary: both chunks 1000 long, none lost")  // Review Focus 4
test("gap of 999 fills; gap of 1000 starts a new segment")
test("sample_idx going backwards flushes and starts segment+1, chunkIndex 0")  // Review Focus 4
test("repeated sample_idx starts a new segment")
test("fs change flushes and starts a new segment")
test("first sample at any index causes no gap")
test("flush emits a partial chunk; flush with nothing emits nothing")
test("noteRejected counts on the next emitted chunk, then resets")
test("rejected count survives an empty flush")
test("all channels have equal length in every emitted chunk")
test("deviceMissed is the latest sample's missed")
test("startTimeMs back-dates by leading gap entries")  // period × entries before the real sample

// observation.test.js
test("code, identifier, references and component order match the spec")
test("note parses to {source, gap_samples, rejected_lines, device_missed}")
test("period is 10 at fs 100 and 4 at fs 250")
test("data joins numbers and E with single spaces")
test("origin unit and UCUM code per channel: V, [g], deg/s")
test("effectiveDateTime has the form YYYY-MM-DDThh:mm:ss+00:00")
test("no category and no top-level value")
test("SIMULATED source appears in note")
```

- [ ] **Step 2: Run to verify failure**

Run: `node --test receiver/tests/`
Expected: FAIL with module not found for the new files.

- [ ] **Step 3: Implement.** With `gap = idx − lastIdx − 1`: `0` append, `1..999` fill then append, `>= 1000` new segment, negative or `idx == lastIdx` new segment. Spec D4: never read `epoch_id`. After each append, emit when the channel length reaches `chunkSize`, including during gap fill.

When a chunk's first entry is added, `startTimeMs = now() − (fill entries remaining before the current real sample) × (1000 / fs)`.

- [ ] **Step 4: Run to verify pass**

Run: `node --test receiver/tests/`
Expected: all pass.

- [ ] **Step 5: Commit**

```bash
git add receiver/src/chunker.js receiver/src/observation.js receiver/tests/
git commit -m "feat(receiver): group samples into chunks and build Observations"
```

---

### Task 6: Outbox and uploader

**Files:**
- Create: `receiver/src/outbox.js`, `receiver/src/uploader.js`
- Test: `receiver/tests/outbox.test.js`, `receiver/tests/uploader.test.js`

**Interfaces:**
- Consumes: Observation and `identifierValue` from Task 5.
- Produces:
  - `sessionKey(card) -> string`, `"<patient>|<device>"`
  - Store interface: `put(record) -> id`, `update(record)`, `delete(id)`, `all() -> record[]` in id order. `class MemoryStore`, `class IndexedDbStore(dbName="prata-capture")`.
  - `class Outbox { constructor(store); add({identifier, sessionKey, observation}); nextFor(sessionKey) -> record|null; remove(id); markRejected(id, reason); counts(sessionKey) -> {pending, rejected, otherSession} }`
  - `class Uploader { constructor({outbox, fetchFn, card, sleep, onStatus, baseUrl="/fhir-r4/v1"}); step() -> "idle"|"sent"|"rejected"|"retry"|"auth"; start(); stop(); resume(card) }`

- [ ] **Step 1: Write failing tests** (`MemoryStore`, fake `fetchFn`, fake `sleep`)

```js
// outbox.test.js
test("nextFor returns the oldest pending record of that session")
test("records survive into a new Outbox on the same store")
test("markRejected keeps the record, excluded from nextFor, counted as rejected")
test("add rejects with QuotaExceededError when the store throws it")

// uploader.test.js
test("POST sends Authorization, If-None-Exist: identifier=<value>, fhir+json")
test("201 and 200 both delete the record")
test("record stays until the response arrives")  // inspect the store during fetch
test("fetch throwing keeps the record and returns retry")
test("500 keeps the record and returns retry")
test("backoff goes 1,2,4,8,16,30,30 s, and resets after success")
test("401 and 403 return auth, keep the record, and stop sending until resume")
test("400 marks rejected with OperationOutcome text and moves to next")
test("400 with a non-JSON body gives reason 'HTTP 400'")
test("chunks are sent oldest first, one at a time")
test("other session's chunks are skipped and counted")  // Review Focus 1
test("resume with their card sends them")  // Review Focus 1
```

- [ ] **Step 2: Run to verify failure**

Run: `node --test receiver/tests/`
Expected: FAIL with module not found for the new files.

- [ ] **Step 3: Implement.** The reason text is the first `issue[].details.text` in the OperationOutcome. `IndexedDbStore` is a thin wrapper with an auto-increment key, covered by the manual check in Task 9. It calls `navigator.storage.persist()` once on open and ignores a refusal.

- [ ] **Step 4: Run to verify pass**

Run: `node --test receiver/tests/`
Expected: all pass.

- [ ] **Step 5: Commit**

```bash
git add receiver/src/outbox.js receiver/src/uploader.js receiver/tests/
git commit -m "feat(receiver): durable outbox and retrying uploader"
```

---

### Task 7: Session card and capture controller

**Files:**
- Create: `receiver/src/card.js`, `receiver/src/capture.js`
- Test: `receiver/tests/card.test.js`, `receiver/tests/capture.test.js`

**Interfaces:**
- Consumes: Tasks 4 to 6.
- Produces:
  - `parseCard(text: string) -> Card`, throwing `Error` with a user-readable message
  - `class Capture { constructor({outbox, sessionKey, card, source, onSample, onStatus, newId=() => "cap-"+crypto.randomUUID()}); async run(lines: AsyncIterable<string>) -> "ended"|"disconnected"|"quota"; stats -> {samples, gaps, rejected} }`

`Capture.run` feeds lines through `parseLine` and `Chunker`, and writes each chunk to the outbox through a sequential promise chain, so chunk order is kept.

- [ ] **Step 1: Write failing tests**

```js
// card.test.js, Review Focus 5
test("a valid card parses")
test("empty string gives a message saying to paste a card")
test("non-JSON text gives a message saying it is not valid JSON")
test("seed summary JSON is rejected, naming the missing field")
test("patient without the Patient/ prefix is rejected")

// capture.test.js
test("lines reach onSample and the outbox")
test("every chunk is in the outbox before run resolves")
test("ending the iterable flushes the partial chunk and returns ended")
test("the iterable throwing flushes and returns disconnected")
test("store quota error stops reading and returns quota")
test("each run has a new captureId")
test("stats count samples, gaps and rejected lines")
test("rejected line followed by the next index produces an E gap")
```

- [ ] **Step 2: Run to verify failure**

Run: `node --test receiver/tests/`
Expected: FAIL with module not found for the new files.

- [ ] **Step 3: Implement** to the signatures above. Stop is done by the caller ending the line source, so `Capture` has no separate stop path.

- [ ] **Step 4: Run to verify pass**

Run: `node --test receiver/tests/`
Expected: all pass.

- [ ] **Step 5: Commit**

```bash
git add receiver/src/card.js receiver/src/capture.js receiver/tests/
git commit -m "feat(receiver): session card parsing and capture controller"
```

---

### Task 8: The page

**Files:**
- Create: `receiver/index.html`, `receiver/app.js`, `receiver/src/serial.js`, `receiver/src/plot.js`
- Modify: `fhir_server/app.py`
- Test: `receiver/tests/plot.test.js`, `tests/test_routes.py`

**Interfaces:**
- Consumes: all receiver modules.
- Produces:
  - `/capture/` static route
  - `serialLines(port, {baudRate=115200}) -> AsyncGenerator<string>`
  - `class Trace { constructor(capacity=1000); push(i, q); points(width, height) -> {i:[x,y][], q:[x,y][]} }`, plus `draw(canvas, trace)`

- [ ] **Step 1: Write failing tests**

```python
# tests/test_routes.py
def test_capture_page_served(client):
    r = client.get("/capture/")
    assert r.status_code == 200 and "Raw signal" in r.text

def test_capture_module_has_js_mime(client):
    r = client.get("/capture/src/jsonlines.js")
    assert r.status_code == 200 and "javascript" in r.headers["content-type"]
```

```js
// plot.test.js
test("capacity keeps only the last 1000 points")
test("a constant signal gives finite y values")  // no divide by zero
test("points stay inside width and height")
```

- [ ] **Step 2: Run to verify failure**

Run: `.venv/bin/python -m pytest tests/test_routes.py -q -k capture ; node --test receiver/tests/plot.test.js`
Expected: `404` and module not found.

- [ ] **Step 3: Implement.**

`app.py`: mount `StaticFiles(directory=<repo>/receiver, html=True)` at `/capture`, after the routers.

`index.html` has:
- heading "Raw signal capture" and a fixed line: "Raw signal only. Not a measurement result or a clinical finding."
- card paste box and Use card button
- Connect serial, Start simulator and Stop buttons
- canvas
- status line showing samples received, chunks confirmed, chunks pending, gaps, rejected lines
- an error area, and a large SIMULATED banner while the simulator runs

`app.js` keeps the card in `sessionStorage` only, wrapped in try/catch, and connects:

| Condition | Message or action |
|---|---|
| `navigator.serial` missing | Disable Connect: "This browser has no Web Serial. Use Chrome or Edge." The simulator stays usable. |
| Run returned `disconnected` | "Disconnected. Click Connect to resume." No auto-reconnect |
| Run returned `quota` | "Browser storage is full. Capture stopped." |
| Uploader status `auth` | "Token invalid. Paste a new card." |
| Rejected chunks | Show count and latest reason |
| `otherSession > 0` | "N chunks belong to another session. Paste that session's card to send them." |
| Load with pending chunks | Report them and start uploading once a card is set |

`serial.js`: `port.open({baudRate})`, `TextDecoderStream`, `LineSplitter`. Stop calls `reader.cancel()`, and the port is closed in `finally`. A device-lost read error propagates to `Capture.run`.

- [ ] **Step 4: Run to verify pass**

Run: `.venv/bin/python -m pytest tests -q && node --test receiver/tests/`
Expected: all pass.

- [ ] **Step 5: Commit**

```bash
git add receiver/index.html receiver/app.js receiver/src/serial.js receiver/src/plot.js receiver/tests/plot.test.js fhir_server/app.py tests/test_routes.py
git commit -m "feat(receiver): capture page served at /capture"
```

---

### Task 9: End-to-end test, docs and browser check

**Files:**
- Create: `receiver/tests/fixtures/make_chunk.mjs`, `tests/test_capture_e2e.py`
- Modify: `fhir_server/README.md`, `CLAUDE.md`

**Interfaces:**
- Consumes: everything above.
- Produces: `node receiver/tests/fixtures/make_chunk.mjs '<card JSON>'` prints `{"observation":..., "identifier":..., "expected":{"I":[...], ...}}`. Lines come from `formatLine`, go through the real parser, chunker and builder, and include one gap.

- [ ] **Step 1: Write the failing test**

```python
def test_chunk_round_trip(tmp_path):
    # seed and capture-session via CLI, make_chunk.mjs via subprocess
    r1 = post(obs, identifier); assert r1.status_code == 201
    r2 = post(obs, identifier); assert r2.status_code == 200
    assert r2.json()["id"] == r1.json()["id"]
    stored = client.get(f"/fhir-r4/v1/Observation/{r1.json()['id']}", headers=auth).json()
    for comp in stored["component"]:
        got = comp["valueSampledData"]["data"].split(" ")
        assert got == [str_token(v) for v in expected[channel(comp)]]
```

If `node` is missing, the test fails rather than skips, so a silent skip cannot hide the contract.

- [ ] **Step 2: Run to verify failure**

Run: `.venv/bin/python -m pytest tests/test_capture_e2e.py -q`
Expected: FAIL because the fixture script does not exist.

- [ ] **Step 3: Write the fixture.** Add a run guide section to `fhir_server/README.md`: `seed`, `capture-session`, `serve`, open `http://127.0.0.1:8000/capture/` in Chrome. In `CLAUDE.md`, update Status, add `receiver/` to the repo map and add the Node test command.

- [ ] **Step 4: Run all tests**

Run: `.venv/bin/python -m pytest tests -q && node --test receiver/tests/`
Expected: all pass.

- [ ] **Step 5: Commit**

```bash
git add receiver/tests/fixtures/make_chunk.mjs tests/test_capture_e2e.py fhir_server/README.md CLAUDE.md
git commit -m "test(receiver): chunk round trip through the real server, and run guide"
```

- [ ] **Step 6: Browser check with the simulator (spec Acceptance 2), in real Chrome**

Use a scratch database. Run the simulator for at least 60 s. Stop the server for about 15 s partway, while pending chunks grow, then restart it with the same database. Run a second capture, stop the server again, click Stop on the page, reload the tab with chunks pending, restart the server and paste the card again. Reload only after Stop: closing a tab mid-capture loses the unsaved partial chunk (up to 10 s), which is a known limit of this design.

Pass means:
- pending returns to 0 with no reload loop
- the Encounter's Observations hold every sample with sequential indexes
- no identifier appears twice
- the plot and SIMULATED banner are visible
- `note` says `SIMULATED`

Write the query as a small script in the scratchpad, and report the counts.

- [ ] **Step 7: Hardware smoke test (spec Acceptance 3), with the owner**

The owner connects the **spare blank board** with a data cable. Confirm which board it is before writing anything. Flash `arduino/radar_json/radar_json.ino` with `arduino-cli`, with `USB CDC On Boot` enabled. The owner clicks Connect and picks the port, since the picker needs a click.

Pass means lines reach the server as Observations. Report this as a data path check only, because the pins are placeholders and the values are not radar signal. If it cannot be run, report it as not done. Do not claim it passed.

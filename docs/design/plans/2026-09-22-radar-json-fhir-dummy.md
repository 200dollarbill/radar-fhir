# Radar JSON and FHIR Dummy Receiver Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build an Arduino-compatible ESP32-S3 sketch that emits newline-delimited radar/IMU JSON and a local Python receiver that converts valid packets into bounded FHIR-shaped dummy Observations with a tiny HTTP API.

**Architecture:** The board samples placeholder ADC inputs on GPIO 1 and GPIO 2, reads the available IMU, renders diagnostic status, and emits one JSON object per line over USB serial. The Python package separates validation/conversion, bounded storage, serial ingestion, and HTTP transport. The output follows FHIR R4 JSON structure but is explicitly local and non-publishable.

**Tech Stack:** Arduino CLI 1.5.1, ESP32 Arduino core, supported M5Stack libraries, Python 3 standard library, `pyserial`, and `http.server`.

**Spec:** `docs/.superpowers/specs/2026-09-22-radar-json-fhir-dummy-design.md`

## Global Constraints

- Emit one compact JSON object followed by `\\n` per sample at a nominal 100 Hz.
- Keep GPIO 1 as I and GPIO 2 as Q compile-time placeholders near the top of the sketch.
- Mirror the existing CSV fields: epoch, sample index, board time, sample rate, CRC/missed flags, I/Q, and IMU axes.
- Use host UTC receive time as `Observation.effectiveDateTime` until board time synchronization exists.
- Do not send data to SATUSEHAT or claim temporary Observations are SATUSEHAT-valid.
- Bind the dummy HTTP service to `127.0.0.1` by default and keep recent observations bounded.
- Continue after malformed JSON or invalid packet fields and increment counters.
- Display `ONLINE`, `SENDING`, `IDLE`, and `ERROR` without blocking sampling indefinitely.
- Do not upload hardware during verification. Do not stage or commit automatically.

## File Map

- `arduino/radar_json/radar_json.ino`: ADC/IMU sampling, JSON serialization, display, serial output.
- `arduino/radar_json/README.md`: board assumptions and Arduino CLI commands.
- `python_receiver/{__init__,models,store,receiver,server}.py`: model, storage, ingestion, and HTTP boundaries.
- `python_receiver/tests/test_{models,store,server}.py`: unit and endpoint tests.
- `python_receiver/requirements.txt`: runtime serial dependency.
- `docs/implementation/2026-09-22-radar-json-fhir-dummy-action-plan.md`: simple action plan and future footnotes.

---

### Task 1: Packet and Observation model

**Files:** Create `python_receiver/__init__.py`, `python_receiver/models.py`, and `python_receiver/tests/test_models.py`.

**Interfaces:** `RadarPacket.from_json_line(line: str) -> RadarPacket`; `RadarPacket.to_observation(received_at: datetime) -> dict[str, object]`; `PacketValidationError(ValueError)`.

- [ ] Write failing tests for valid CSV-shaped JSON, invalid JSON, missing `Q`, wrong `fs` type, conversion to one Observation with eight components, UTC formatting, and rejection of `crc_ok == false`.
- [ ] Run `python3 -m pytest python_receiver/tests/test_models.py -q`; expect failure because modules do not exist.
- [ ] Implement a frozen dataclass with all thirteen fields. Require integer fields `epoch_id`, `sample_idx`, `fs`, `missed`, boolean `crc_ok`, and numeric timestamp, I/Q, and six IMU axes. Reject booleans as numbers.
- [ ] Convert valid packets into `Observation` with `status: final`, HL7 `vital-signs` category, temporary component codes `radar-i`, `radar-q`, `accel-x/y/z`, `gyro-x/y/z`, temporary units `V`, `g`, and `deg/s`, and host UTC `effectiveDateTime`. Omit `subject`, `device`, and `identifier`.
- [ ] Run the focused tests and expect PASS.

### Task 2: Bounded store and serial ingestion

**Files:** Create `python_receiver/store.py`, `python_receiver/receiver.py`, `python_receiver/tests/test_store.py`, and `python_receiver/requirements.txt`.

**Interfaces:** `ObservationStore(max_size=1000)` with `add`, `recent`, `latest`, and `snapshot_health`; `SerialReceiver(port, baudrate, store)` with `process_line` and `run(stop_event)`.

- [ ] Write failing tests proving the oldest item is evicted, valid lines increment accepted count, malformed lines increment invalid count, and `process_line` does not raise.
- [ ] Run `python3 -m pytest python_receiver/tests/test_store.py -q`; expect failure.
- [ ] Implement `deque(maxlen=...)` protected by `threading.Lock`, counters for accepted/invalid/rejected-integrity, and copy-returning snapshots. Reject `max_size < 1`.
- [ ] Implement lazy `pyserial` import, line parsing, host UTC conversion, and a `run` loop with timeout, cleanup, and serial-error health reporting. Keep malformed input non-fatal.
- [ ] Pin `pyserial>=3.5,<4` in requirements and run all model/store tests.

### Task 3: Local HTTP service

**Files:** Create `python_receiver/server.py` and `python_receiver/tests/test_server.py`.

**Interfaces:** `create_server(store, host="127.0.0.1", port=8080) -> ThreadingHTTPServer`; `GET /health`; `GET /observations`; `GET /observations/latest`.

- [ ] Write failing tests for health 200, empty latest 404, latest 200 after adding data, observations Bundle JSON, and unknown-route 404.
- [ ] Run the focused test and expect failure.
- [ ] Implement a `ThreadingHTTPServer` handler factory with JSON content type, bounded output, correct status codes, loopback default, and quiet logging.
- [ ] Add `python3 -m python_receiver.server --serial-port ... --http-port ...`, daemon serial thread, clean `KeyboardInterrupt` shutdown, and documented invocation.
- [ ] Run all Python tests and expect PASS.

### Task 4: Arduino sketch and CLI verification

**Files:** Create `arduino/radar_json/radar_json.ino` and `arduino/radar_json/README.md`.

**Interfaces:** Constants `RADAR_I_PIN = 1`, `RADAR_Q_PIN = 2`, `SAMPLE_RATE_HZ = 100`; serial output at 115200; display states `ONLINE`, `SENDING`, `IDLE`, `ERROR`.

- [ ] Inspect installed packages with `arduino-cli core list`, `arduino-cli board listall`, and `arduino-cli lib search`; record the recognized ESP32-S3 FQBN rather than inventing an S3R identifier.
- [ ] Implement `setup` and `loop` with ADC resolution, supported display/IMU initialization, 100 Hz `micros()` scheduling, compact JSON lines, missed-count tracking, and rate-limited display updates.
- [ ] Keep I/Q pins and sample rate at the top. Document dummy AFE assumptions. If IMU initialization fails, show `ERROR` and use an explicit diagnostic behavior instead of silently claiming real readings.
- [ ] Document core installation, library installation, compile, board listing, and explicit upload commands. Upload is not run.
- [ ] Compile with the exact recorded FQBN. Record any missing dependency truthfully.

### Task 5: Action plan and final verification

**Files:** Create `docs/implementation/2026-09-22-radar-json-fhir-dummy-action-plan.md`; modify README only if verification changes assumptions.

- [ ] Document deliverable, placeholder wiring, packet flow, receiver setup, HTTP examples, test commands, CLI compilation, hardware-only checks, and the local/non-publishable FHIR warning.
- [ ] Add future footnotes for `Patient/{id}`, `Device/{id}`, facility identifier, terminology/UCUM units, device profile/extensions, synchronized time, encounter, performer, organization, and provenance references.
- [ ] Run `python3 -m pytest python_receiver/tests -q`, `python3 -m compileall -q python_receiver`, and `git diff --check`.
- [ ] Run the Arduino CLI compile command and report compile success or the exact dependency failure.
- [ ] Run `git status --short` and `git diff --stat`; do not stage or commit.

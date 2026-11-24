# Radar JSON and FHIR Dummy Receiver Design

**Date:** 2026-09-22
**Status:** Design approved in conversation; awaiting written-spec review

## Goal

Replace the current board-side CSV-oriented output with a newline-delimited JSON stream from an M5Stack ESP32-S3 board. The stream will contain placeholder ADC I/Q readings and IMU values and will be readable over USB serial. A local Python dummy receiver will parse the stream, convert each valid packet into a local FHIR-like R4 Observation, retain recent observations in memory, and expose a small localhost HTTP API.

This is a development stub. It is not an implementation of SATUSEHAT authentication, publishing, patient matching, or a complete FHIR server.

## Scope

### Included

- Arduino IDE-compatible sketch for an ESP32-S3/M5Stack board.
- Placeholder ADC inputs: GPIO 1 for I and GPIO 2 for Q.
- One compact JSON object per line at a nominal 100 Hz sample rate.
- Packet fields matching the existing CSV shape: epoch, sample index, board time, sample rate, CRC/missed indicators, I/Q, and IMU axes.
- Board display states for online, sending, idle, and fatal setup error.
- Python serial receiver with packet validation and non-fatal malformed-line handling.
- Conversion to a local FHIR-like `Observation` JSON object.
- Bounded in-memory storage.
- Local HTTP endpoints for health, recent observations, and the latest observation.
- Unit tests for Python parsing, conversion, storage bounds, and HTTP behavior.
- Arduino CLI compilation verification.
- A simple action plan in `docs/implementation/` with future-configuration footnotes.

### Excluded

- Actual radar AFE protocol implementation beyond placeholder ADC reads.
- Confirmed production GPIO assignments.
- Board upload, because the serial port is machine-specific.
- Patient registration, authentication, authorization, accounts, or UI.
- SATUSEHAT network calls, API keys, or hosted-platform registration.
- Persistent database storage.
- Complete FHIR validation or a general FHIR REST server.
- Claims that the temporary Observation is ready for SATUSEHAT submission.

## Architecture

```text
M5Stack ESP32-S3 board
  ADC GPIO 1 -> I
  ADC GPIO 2 -> Q
  built-in IMU -> ax ay az gx gy gz
  display -> diagnostic state
  USB serial -> newline-delimited JSON
                         |
                         v
              Python serial receiver
              parse -> validate -> convert
                         |
                         v
                  bounded memory store
                         |
                         v
                localhost HTTP endpoints
```

The Arduino sketch writes one JSON object followed by `\\n` for each sample. The Python receiver reads complete lines, so partial serial reads do not become packets. The receiver continues after malformed JSON or invalid fields and increments error counters.

## Packet contract

The initial packet uses the following fields:

| Field | Type | Meaning |
|---|---|---|
| `epoch_id` | integer | Board-side acquisition epoch identifier |
| `sample_idx` | integer | Monotonic sample index within the epoch |
| `t_host_unix` | number | Board elapsed-time placeholder until clock synchronization exists |
| `fs` | integer | Nominal sampling frequency, initially 100 Hz |
| `crc_ok` | boolean | Placeholder integrity status, initially true for local ADC samples |
| `missed` | integer | Missed sample count detected by the loop |
| `I`, `Q` | number | ADC-derived placeholder radar channels |
| `ax`, `ay`, `az` | number | Accelerometer axes |
| `gx`, `gy`, `gz` | number | Gyroscope axes |

The JSON keys intentionally mirror `data/rabits_Sep_15_1518.csv` so that the dummy stream can be compared with the existing output. The receiver's authoritative timestamp is its host UTC receive time, because the board clock is not synchronized in this first run.

## FHIR-like conversion

Each valid packet becomes one local Observation-shaped object:

- `resourceType`: `Observation`.
- `status`: `final`.
- `category`: `vital-signs` from the HL7 observation-category system.
- `code`: a clearly temporary local radar I/Q code, marked in the implementation comments as pending terminology selection.
- `effectiveDateTime`: host UTC receive timestamp.
- `component`: one component each for I, Q, ax, ay, az, gx, gy, and gz, each represented as a `valueQuantity` with a temporary unit policy.
- `subject` and `device`: omitted until configuration exists.
- `identifier`: omitted until a facility and local identifier policy exist.

The output follows the shape of FHIR R4 JSON but is not presented as SATUSEHAT-valid. The receiver must not send it to a hosted platform.

Future configuration footnotes must cover:

1. Assigning a real `Patient/{id}` subject.
2. Assigning a registered `Device/{id}` reference.
3. Adding a facility-scoped Observation identifier.
4. Selecting and documenting codes and UCUM units for the radar-derived data and IMU channels.
5. Deciding whether I/Q remains one Observation's components or becomes separate/derived resources.
6. Defining the device profile and its required extensions.
7. Establishing synchronized board time or explicitly retaining host receive time.
8. Adding any required encounter, performer, organization, and provenance references.

## HTTP interface

The dummy server binds to `127.0.0.1` by default.

| Method and path | Response |
|---|---|
| `GET /health` | Receiver state, packet counters, and latest receive time |
| `GET /observations` | Recent converted Observation objects, newest or oldest order documented by implementation |
| `GET /observations/latest` | Most recent Observation or a clear not-found response |

The HTTP layer is intentionally small and not a substitute for the later FHIR REST server. It should return JSON and use appropriate status codes for success, empty state, and invalid routes.

## Display state machine

- `ONLINE`: initialization completed and serial output is available.
- `SENDING`: a packet was emitted recently; show the current sample index.
- `IDLE`: no packet has been emitted within a configurable display timeout.
- `ERROR`: a fatal initialization problem occurred.

Display updates must not block the sample loop for an unbounded duration. Serial output remains the source of truth when the display cannot initialize.

## Board and build assumptions

The exact M5Stack S3R Arduino CLI board identifier and library API must be confirmed from the installed board package. The build instructions will use the recognized ESP32-S3 FQBN and explicitly record any M5Stack-specific assumption. GPIO 1 and GPIO 2 are placeholders and must be easy to change near the top of the sketch.

The sketch should prefer the board's supported display and IMU libraries. If the IMU library is unavailable in the local CLI environment, compilation must fail clearly rather than silently emitting fabricated sensor data. A documented compile-only fallback may be used only if it is visibly marked as a dummy mode.

## Error handling

- Malformed JSON: count and skip the line.
- Missing or wrongly typed required fields: count and skip the packet.
- `crc_ok == false`: retain packet parsing metadata but do not convert it to a final Observation; the policy must be explicit in code and tests.
- Serial disconnect: keep the HTTP process alive, report disconnected health state, and allow reconnect behavior if supported by the selected serial library.
- Empty observation store: return a JSON response with an appropriate not-found status for `/observations/latest`.
- Board setup failure: show `ERROR` and emit a diagnostic message where possible.

## Verification

Python tests will cover valid packets, malformed JSON, missing fields, wrong types, rejected integrity status, UTC conversion, bounded storage, health counters, latest-observation behavior, and HTTP responses.

Arduino CLI will compile the sketch with the selected FQBN and dependencies. Hardware-only behavior, including ADC values, IMU readings, display rendering, and USB serial output, will be documented as requiring a connected board. No upload or destructive device action is implied by the build step.

## Delivery layout

- `arduino/radar_json/radar_json.ino`: board sketch.
- `python_receiver/`: receiver package, HTTP service, and tests.
- `docs/implementation/`: simple action plan, setup, assumptions, and future-configuration footnotes.

Exact names may be adjusted during implementation if the existing repository structure requires it, but the boundaries and behavior above remain fixed.

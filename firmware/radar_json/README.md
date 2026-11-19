# Radar JSON sketch

This Arduino IDE sketch is a first-run dummy for an M5Stack ESP32-S3 board. It reads placeholder ADC inputs and emits one JSON object per line over USB serial.

## Assumptions

- `RADAR_I_PIN` is GPIO 7 (G7) and `RADAR_Q_PIN` is GPIO 8 (G8), as given by the owner on 2026-11-16. Both are ADC1 channels. Which pin carries I and which carries Q is an assumption; swap the two constants if the radar wiring says otherwise.
- The sample rate is 100 Hz, driven by a hardware timer in its own task, so serial and display work cannot delay it.
- `sample_idx` is the time slot since boot. Lost time shows up as a jump in `sample_idx`; samples are never replayed in a burst.
- `missed` is the running count of samples lost (skipped slots, full queue, or no room to send, such as when no host is reading).
- The board timestamp (`t_host_unix`) is uptime, not synchronized Unix time.
- `crc_ok` is true for locally sampled ADC data. It is not an AFE CRC implementation.
- IMU values are read through M5Unified. If the IMU cannot initialize, the display shows `ERROR` and the emitted axes are zero.
- **Board identity.** The board ID is the chip's factory MAC (12 upper-case hex digits, also on the screen as `ID ...` and in the `READY` line). On first boot the board makes a random 64-hex key and keeps it in NVS (`Preferences`, namespace `prata`); reflashing the sketch keeps it, a full flash erase does not (an admin then registers the board again). When the host sends the line `BOARD?`, the board answers `BOARD {"id":"...","key":"...","fw":"radar_json"}`. **Known weakness:** the key goes to anyone who asks over the port; see `docs/design/specs/2026-11-18-board-sessions-and-navigation-design.md`. Logic and host tests: `board.h`, `tests/firmware/board_test.cpp`.
- The board is an M5Stack AtomS3R, FQBN `m5stack:esp32:m5stack_atoms3r`. USB output needs `USB CDC On Boot` enabled, which is that board's default.

## Arduino CLI

The local tool reports Arduino CLI 1.5.1, ESP32 core 3.3.11, and M5Stack core 3.3.9. Install the display dependency and compile for the AtomS3R:

```bash
arduino-cli lib install M5Unified
arduino-cli core install esp32:esp32
arduino-cli compile --fqbn m5stack:esp32:m5stack_atoms3r firmware/radar_json
```

List the connected port before any upload:

```bash
arduino-cli board list
arduino-cli upload -p <serial-port> --fqbn m5stack:esp32:m5stack_atoms3r firmware/radar_json
```

The radar connects to G7 (I) and G8 (Q). With nothing attached the sketch only reads pin noise, which is not radar signal. The ADC reads 0 to about 3.1 V; keep the radar outputs inside that range.

## WiFi heart-rate ingest (config.h)

The sketch can POST heart-rate Observations to the local FHIR server over WiFi,
using the wire contract of `device_client/client.py` (same JSON, same endpoint,
same `Authorization: Bearer` header).

1. `cp firmware/radar_json/config.example.h firmware/radar_json/config.h` and fill
   in WiFi credentials and `SERVER_URL` (the machine running `python3 -m fhir_server serve`).
2. Obtain `DEVICE_TOKEN` from `python3 -m fhir_server seed` (its summary JSON) or
   `POST /fhir-r4/v1/Device/{id}/$provision` as an admin; `DEVICE_REF` and
   `PATIENT_REF` come from the same seed summary.
3. Set `ENCOUNTER_REF` to the encounter the doctor opened
   (`POST /fhir-r4/v1/Encounter` as the doctor, use the returned id).
4. `config.h` is gitignored — never commit real credentials.

`config.h` is compile-time: an empty `DEVICE_TOKEN` or `ENCOUNTER_REF` disables
ingest entirely and the sketch runs as the serial-only dummy.

The radar goes on G7/G8 (see Assumptions). The ingest path is compile-verified only; WiFi, NTP
and the POST itself require a connected board and a running server.

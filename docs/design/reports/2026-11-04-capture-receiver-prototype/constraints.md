Global constraints (verbatim from plan):
- Everything runs at http://127.0.0.1:8000. No Cloudflare, nginx or Bluetooth.
- Firmware is not changed. arduino/radar_json/radar_json.ino is the input format.
- Never label output as JVP, diagnosis, or a measurement. Simulated data carries "source":"SIMULATED" in note and "SIMULATED" on screen.
- Synthetic subjects only.
- Code system urn:prata:radar-signal. Top-level code raw-capture, display "Raw radar I/Q capture". Component codes i-voltage, q-voltage (UCUM V), accel-x, accel-y, accel-z (UCUM [g]), gyro-x, gyro-y, gyro-z (UCUM deg/s).
- Chunk limit 1000 samples at most. period = 1000/fs ms. No category on raw chunks.
- Serial baud 115200.
- End commit messages with the attribution line your own session reminder gives (R6).
- Commands: .venv/bin/python -m pytest tests -q and node --test "receiver/tests/*.test.js". Baseline 134 pytest pass.
- effectiveDateTime resolution is 1 s (canonicalize_datetimes truncates). Encounters are created arrived then PUT in-progress. captureId is cap-<uuid>.
Controller rulings:
- R1 Node test command is node --test "receiver/tests/*.test.js" (the plan's directory form fails on Node 22).
- R2 receiver/package.json {"private":true,"type":"module"}, no dependencies, added in Task 4.
- R3 simulatorLines and serialLines also take signal (AbortSignal); aborted means the generator ends.
- R4 Uploader onStatus({state:"idle"|"sending"|"retry"|"auth", confirmed:number, lastRejectedReason:string|null}); Capture onStatus(stats), stats {samples,gaps,rejected}.
- R5 make_chunk.mjs expected holds exact token strings ("1.65","E"), compared directly, no str_token.

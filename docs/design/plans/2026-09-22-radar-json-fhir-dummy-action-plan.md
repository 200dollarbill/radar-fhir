# Radar JSON and FHIR Dummy Action Plan

## Current run

1. Confirm the AFE wiring before using the placeholder pins.
2. Compile `arduino/radar_json` for the M5CoreS3-compatible ESP32-S3 target.
3. Upload only after the target port and pins are confirmed.
4. Connect the board by USB and verify newline-delimited JSON at 115200 baud.
5. Install Python dependency with `python3 -m pip install -r python_receiver/requirements.txt`.
6. Start the receiver with `python3 -m python_receiver.server --serial-port <port>`.
7. Inspect `http://127.0.0.1:8080/health`, `/observations`, and `/observations/latest`.

## Board output

Each line mirrors the existing CSV fields: epoch ID, sample index, uptime, sample rate, CRC/missed flags, I/Q, and accelerometer/gyroscope axes. The display reports `ONLINE`, `SENDING`, `IDLE`, or `ERROR`. GPIO 1 and GPIO 2 remain placeholders.

## Local conversion

The Python dummy validates each line and converts accepted packets into one FHIR-shaped R4 `Observation` with I/Q, accelerometer, and gyroscope components. It stores only a bounded recent window and binds its HTTP API to localhost. This is not a complete FHIR server and must not be sent to SATUSEHAT.

## Verification

```bash
python3 -m pytest python_receiver/tests -q
python3 -m compileall -q python_receiver
arduino-cli compile --fqbn m5stack:esp32:m5stack_cores3 arduino/radar_json
```

Hardware-only checks include ADC wiring, actual IMU readings, display rendering, USB serial continuity, and sample timing. The local test run cannot prove those behaviors without the board.

## Future configuration footnotes

1. Configure a real `Patient/{id}` subject after patient registration exists.
2. Configure a registered `Device/{id}` reference after device setup exists.
3. Add the facility-scoped Observation identifier.
4. Replace temporary radar and IMU codes and units with approved terminology and UCUM policy.
5. Decide whether I/Q stays as components or becomes separate or derived Observations.
6. Define and package the standalone device profile and any extensions.
7. Add synchronized device time or document host receive time as authoritative.
8. Add configured encounter, performer, organization, and provenance references.

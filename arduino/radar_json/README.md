# Radar JSON sketch

This Arduino IDE sketch is a first-run dummy for an M5Stack ESP32-S3 board. It reads placeholder ADC inputs and emits one JSON object per line over USB serial.

## Assumptions

- `RADAR_I_PIN` is GPIO 1.
- `RADAR_Q_PIN` is GPIO 2.
- The nominal sample rate is 100 Hz.
- The board timestamp is uptime, not synchronized Unix time.
- `crc_ok` is true for locally sampled ADC data. It is not an AFE CRC implementation.
- IMU values are read through M5Unified. If the IMU cannot initialize, the display shows `ERROR` and the emitted axes are zero.
- The board is treated as an M5CoreS3-compatible ESP32-S3 target because no exact S3R FQBN was present in the installed CLI index. Confirm the exact hardware before upload.

## Arduino CLI

The local tool reports Arduino CLI 1.5.1, ESP32 core 3.3.11, and M5Stack core 3.3.9. Install the display dependency and compile with the recognized M5CoreS3 target:

```bash
arduino-cli lib install M5Unified
arduino-cli core install esp32:esp32
arduino-cli compile --fqbn m5stack:esp32:m5stack_cores3 arduino/radar_json
```

List the connected port before any upload:

```bash
arduino-cli board list
arduino-cli upload -p <serial-port> --fqbn m5stack:esp32:m5stack_cores3 arduino/radar_json
```

Do not upload until GPIO 1 and GPIO 2 are confirmed against the AFE wiring.

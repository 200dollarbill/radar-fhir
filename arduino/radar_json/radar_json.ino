#include <Arduino.h>
#include <M5Unified.h>
#include "ingest.h"

// Placeholder pins. Confirm the AFE wiring before connecting the radar.
constexpr int RADAR_I_PIN = 1;
constexpr int RADAR_Q_PIN = 2;
constexpr uint32_t SAMPLE_RATE_HZ = 100;
constexpr uint32_t SAMPLE_PERIOD_US = 1000000UL / SAMPLE_RATE_HZ;
constexpr uint32_t DISPLAY_REFRESH_MS = 250;
constexpr uint32_t IDLE_TIMEOUT_MS = 1500;
constexpr float ADC_REFERENCE_V = 3.3f;
constexpr float ADC_MAX_COUNTS = 4095.0f;

uint32_t epochId = 1;
uint32_t sampleIndex = 0;
uint32_t nextSampleUs = 0;
uint32_t missedSamples = 0;
uint32_t lastSentMs = 0;
uint32_t lastDisplayMs = 0;
bool imuOk = false;

void drawStatus(const char* state) {
  if (millis() - lastDisplayMs < DISPLAY_REFRESH_MS) return;
  lastDisplayMs = millis();
  M5.Display.fillScreen(BLACK);
  M5.Display.setCursor(8, 8);
  M5.Display.setTextSize(2);
  M5.Display.println("Pra-TA radar");
  M5.Display.setTextSize(3);
  M5.Display.println(state);
  M5.Display.setTextSize(2);
  M5.Display.printf("sample: %lu\n", static_cast<unsigned long>(sampleIndex));
  M5.Display.printf("I pin: %d  Q pin: %d\n", RADAR_I_PIN, RADAR_Q_PIN);
  M5.Display.printf("IMU: %s\n", imuOk ? "OK" : "ERROR");
}

float adcVoltage(int pin) {
  return static_cast<float>(analogRead(pin)) * ADC_REFERENCE_V / ADC_MAX_COUNTS;
}

void emitSample() {
  float ax = 0, ay = 0, az = 0, gx = 0, gy = 0, gz = 0;
  if (imuOk) {
    M5.Imu.getAccelData(&ax, &ay, &az);
    M5.Imu.getGyroData(&gx, &gy, &gz);
  }
  const float iValue = adcVoltage(RADAR_I_PIN);
  const float qValue = adcVoltage(RADAR_Q_PIN);
  const uint32_t nowMs = millis();
  Serial.printf(
      "{\"epoch_id\":%lu,\"sample_idx\":%lu,\"t_host_unix\":%.3f,"
      "\"fs\":%lu,\"crc_ok\":%s,\"missed\":%lu,\"I\":%.6f,\"Q\":%.6f,"
      "\"ax\":%.6f,\"ay\":%.6f,\"az\":%.6f,\"gx\":%.6f,\"gy\":%.6f,\"gz\":%.6f}\n",
      static_cast<unsigned long>(epochId), static_cast<unsigned long>(sampleIndex),
      static_cast<double>(nowMs) / 1000.0, static_cast<unsigned long>(SAMPLE_RATE_HZ),
      imuOk ? "true" : "true", static_cast<unsigned long>(missedSamples),
      static_cast<double>(iValue), static_cast<double>(qValue), static_cast<double>(ax),
      static_cast<double>(ay), static_cast<double>(az), static_cast<double>(gx),
      static_cast<double>(gy), static_cast<double>(gz));
  ++sampleIndex;
  lastSentMs = nowMs;
}

void setup() {
  auto config = M5.config();
  M5.begin(config);
  Serial.begin(115200);
  analogReadResolution(12);
  pinMode(RADAR_I_PIN, INPUT);
  pinMode(RADAR_Q_PIN, INPUT);
  imuOk = M5.Imu.begin();
  nextSampleUs = micros();
  lastSentMs = millis();
  Serial.printf("READY radar_json i_pin=%d q_pin=%d fs=%lu imu_ok=%s\n",
                RADAR_I_PIN, RADAR_Q_PIN, static_cast<unsigned long>(SAMPLE_RATE_HZ),
                imuOk ? "true" : "false");
  if (ingestConfigured()) {
    WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
    configTime(0, 0, "pool.ntp.org");  // UTC for effectiveDateTime
  }
  drawStatus(imuOk ? "ONLINE" : "ERROR");
}

void loop() {
  M5.update();
  const uint32_t nowUs = micros();
  if (static_cast<int32_t>(nowUs - nextSampleUs) >= 0) {
    if (nowUs - nextSampleUs > SAMPLE_PERIOD_US) {
      missedSamples += (nowUs - nextSampleUs) / SAMPLE_PERIOD_US;
    }
    nextSampleUs += SAMPLE_PERIOD_US;
    emitSample();
  }
  static uint32_t lastIngest = 0;
  if (ingestConfigured() && WiFi.status() == WL_CONNECTED
      && millis() - lastIngest >= INGEST_PERIOD_MS) {
    lastIngest = millis();
    float placeholderHr = 72.0f;  // placeholder until radar pipeline exists
    int code = postHeartRate(placeholderHr);
    Serial.printf("ingest POST -> %d\n", code);
  }
  const char* state = !imuOk ? "ERROR" : (millis() - lastSentMs > IDLE_TIMEOUT_MS ? "IDLE" : "SENDING");
  drawStatus(state);
}

#include <Arduino.h>
#include <M5Unified.h>
#include <atomic>
#include <esp_timer.h>
#include "ingest.h"
#include "sampling.h"

// Radar I/Q on G7 and G8 (ADC1 channels 6 and 7; the AtomS3R core names them ADC1/ADC2).
// Pins given by the owner on 2026-11-16. Which of the two carries I and which Q is assumed.
constexpr int RADAR_I_PIN = 7;
constexpr int RADAR_Q_PIN = 8;
constexpr uint32_t SAMPLE_RATE_HZ = 100;
constexpr uint32_t SAMPLE_PERIOD_US = 1000000UL / SAMPLE_RATE_HZ;
constexpr uint32_t DISPLAY_REFRESH_MS = 250;
constexpr uint32_t IDLE_TIMEOUT_MS = 1500;
constexpr float ADC_REFERENCE_V = 3.3f;
constexpr float ADC_MAX_COUNTS = 4095.0f;

struct Sample {
  uint32_t index;
  uint32_t ms;
  float i, q, ax, ay, az, gx, gy, gz;
};

constexpr UBaseType_t SAMPLE_QUEUE_DEPTH = 64;  // 640 ms at 100 Hz
constexpr size_t SERIAL_TX_BUFFER_BYTES = 8192;

uint32_t epochId = 1;
volatile uint32_t lastIndex = 0;
std::atomic<uint32_t> missedSamples{0};  // samples lost: skipped slots, full queue, no room to send
uint32_t lastSentMs = 0;
uint32_t lastDisplayMs = 0;
bool imuOk = false;
QueueHandle_t sampleQueue = nullptr;
TaskHandle_t samplerTask = nullptr;

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
  M5.Display.printf("sample: %lu\n", static_cast<unsigned long>(lastIndex));
  M5.Display.printf("I pin: %d  Q pin: %d\n", RADAR_I_PIN, RADAR_Q_PIN);
  M5.Display.printf("IMU: %s\n", imuOk ? "OK" : "ERROR");
}

float adcVoltage(int pin) {
  return static_cast<float>(analogRead(pin)) * ADC_REFERENCE_V / ADC_MAX_COUNTS;
}

// Sampling runs in its own high-priority task so serial and display work cannot delay it.
void samplerLoop(void*) {
  SampleClock clock(esp_timer_get_time(), SAMPLE_PERIOD_US);
  for (;;) {
    ulTaskNotifyTake(pdTRUE, portMAX_DELAY);
    const SampleTick tick = clock.tick(esp_timer_get_time());
    if (!tick.emit) continue;
    if (tick.skipped) missedSamples += tick.skipped;
    Sample s{};
    s.index = tick.index;
    s.ms = static_cast<uint32_t>(esp_timer_get_time() / 1000);
    s.i = adcVoltage(RADAR_I_PIN);
    s.q = adcVoltage(RADAR_Q_PIN);
    if (imuOk) {
      M5.Imu.getAccelData(&s.ax, &s.ay, &s.az);
      M5.Imu.getGyroData(&s.gx, &s.gy, &s.gz);
    }
    if (xQueueSend(sampleQueue, &s, 0) != pdTRUE) ++missedSamples;
  }
}

void onSampleTimer(void*) {
  xTaskNotifyGive(samplerTask);
}

void sendSample(const Sample& s) {
  lastIndex = s.index;
  char line[320];
  const int n = snprintf(
      line, sizeof(line),
      "{\"epoch_id\":%lu,\"sample_idx\":%lu,\"t_host_unix\":%.3f,"
      "\"fs\":%lu,\"crc_ok\":%s,\"missed\":%lu,\"I\":%.6f,\"Q\":%.6f,"
      "\"ax\":%.6f,\"ay\":%.6f,\"az\":%.6f,\"gx\":%.6f,\"gy\":%.6f,\"gz\":%.6f}\n",
      static_cast<unsigned long>(epochId), static_cast<unsigned long>(s.index),
      static_cast<double>(s.ms) / 1000.0, static_cast<unsigned long>(SAMPLE_RATE_HZ),
      imuOk ? "true" : "true", static_cast<unsigned long>(missedSamples.load()),
      static_cast<double>(s.i), static_cast<double>(s.q), static_cast<double>(s.ax),
      static_cast<double>(s.ay), static_cast<double>(s.az), static_cast<double>(s.gx),
      static_cast<double>(s.gy), static_cast<double>(s.gz));
  if (n <= 0 || n >= static_cast<int>(sizeof(line)) || !lineFits(Serial.availableForWrite(), n)) {
    ++missedSamples;
    return;
  }
  Serial.write(reinterpret_cast<const uint8_t*>(line), n);
  lastSentMs = s.ms;
}

void setup() {
  auto config = M5.config();
  M5.begin(config);
  Serial.setTxBufferSize(SERIAL_TX_BUFFER_BYTES);
  Serial.begin(115200);
  Serial.setTxTimeoutMs(0);  // never block when no host is reading
  analogReadResolution(12);
  pinMode(RADAR_I_PIN, INPUT);
  pinMode(RADAR_Q_PIN, INPUT);
  imuOk = M5.Imu.begin();
  lastSentMs = millis();
  Serial.printf("READY radar_json i_pin=%d q_pin=%d fs=%lu imu_ok=%s\n",
                RADAR_I_PIN, RADAR_Q_PIN, static_cast<unsigned long>(SAMPLE_RATE_HZ),
                imuOk ? "true" : "false");
  if (ingestConfigured()) {
    WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
    configTime(0, 0, "pool.ntp.org");  // UTC for effectiveDateTime
  }
  drawStatus(imuOk ? "ONLINE" : "ERROR");
  sampleQueue = xQueueCreate(SAMPLE_QUEUE_DEPTH, sizeof(Sample));
  xTaskCreatePinnedToCore(samplerLoop, "sampler", 4096, nullptr, configMAX_PRIORITIES - 2,
                          &samplerTask, 1);
  esp_timer_handle_t timer;
  const esp_timer_create_args_t timerArgs = {.callback = onSampleTimer, .name = "sample"};
  ESP_ERROR_CHECK(esp_timer_create(&timerArgs, &timer));
  ESP_ERROR_CHECK(esp_timer_start_periodic(timer, SAMPLE_PERIOD_US));
}

void loop() {
  Sample s;
  if (xQueueReceive(sampleQueue, &s, pdMS_TO_TICKS(5)) == pdTRUE) {
    sendSample(s);
    while (xQueueReceive(sampleQueue, &s, 0) == pdTRUE) sendSample(s);
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

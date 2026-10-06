// WiFi heart-rate ingest. Wire contract mirrors device_client/client.py
// (build_observation): same JSON fields, same endpoint, same auth header.
#pragma once
#include <Arduino.h>
#include <WiFi.h>
#include <HTTPClient.h>
#include <time.h>
#include "config.h"

inline bool ingestConfigured() {
  return WIFI_SSID[0] != '\0' && DEVICE_TOKEN[0] != '\0'
      && ENCOUNTER_REF[0] != '\0' && PATIENT_REF[0] != '\0'
      && DEVICE_REF[0] != '\0';
}

inline String utcNowIso() {
  struct tm t;
  if (!getLocalTime(&t, 100)) return String("1970-01-01T00:00:00+00:00");
  char buf[32];
  strftime(buf, sizeof(buf), "%Y-%m-%dT%H:%M:%S+00:00", &t);
  return String(buf);
}

// Returns HTTP status on success, -1 when WiFi is down, -2 on connect error.
inline int postHeartRate(float bpm) {
  if (WiFi.status() != WL_CONNECTED) return -1;
  String body = String(
    "{\"resourceType\":\"Observation\",\"status\":\"final\","
    "\"category\":[{\"coding\":[{\"system\":"
    "\"http://terminology.hl7.org/CodeSystem/observation-category\","
    "\"code\":\"vital-signs\",\"display\":\"Vital Signs\"}]}],"
    "\"code\":{\"coding\":[{\"system\":\"http://loinc.org\","
    "\"code\":\"8867-4\",\"display\":\"Heart rate\"}]},"
    "\"subject\":{\"reference\":\"") + PATIENT_REF +
    "\"},\"encounter\":{\"reference\":\"" + ENCOUNTER_REF +
    "\"},\"effectiveDateTime\":\"" + utcNowIso() +
    "\"},\"valueQuantity\":{\"value\":" + String(bpm, 1) +
    ",\"unit\":\"beats/minute\",\"system\":\"http://unitsofmeasure.org\","
    "\"code\":\"/min\"},\"device\":{\"reference\":\"" + DEVICE_REF +
    "\"},\"identifier\":[{\"system\":\"http://sys-ids.kemkes.go.id/organization/" +
    ORG_IHS + "\",\"value\":\"radar-1\"}]}";
  HTTPClient http;
  http.begin(String(SERVER_URL) + "/fhir-r4/v1/Observation");
  http.addHeader("Content-Type", "application/json");
  http.addHeader("Authorization", String("Bearer ") + DEVICE_TOKEN);
  http.setTimeout(2000);
  int code = http.POST(body);
  http.end();
  return code;
}

// arduino/radar_json/config.example.h  — copy to config.h and fill in.
// config.h is gitignored: never commit real credentials.
#pragma once
#define WIFI_SSID     "your-wifi"
#define WIFI_PASSWORD "your-password"
#define SERVER_URL    "http://192.168.1.10:8000"   // FHIR server base URL
#define DEVICE_TOKEN  ""    // from $provision response; empty disables ingest
#define DEVICE_REF    "Device/REPLACE"             // this device's reference
#define PATIENT_REF   "Patient/REPLACE"            // assigned patient
#define ENCOUNTER_REF ""    // set to the doctor-opened visit, or fill in
#define ORG_IHS       "100000001"
#define INGEST_PERIOD_MS 1000

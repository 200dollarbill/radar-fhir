import json
import urllib.error
import urllib.request


def _default_post(url, *, headers, data):
    req = urllib.request.Request(url, data=data, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req) as resp:
            body = resp.read().decode()
            status = resp.status
    except urllib.error.HTTPError as exc:
        body = exc.read().decode()
        status = exc.code

    class R:
        pass

    r = R()
    r.status_code = status
    r.json = lambda: json.loads(body)
    return r


def build_observation(*, patient, encounter, device, bpm, effective_datetime,
                      identifier_value=None):
    ident = [{"system": "http://sys-ids.kemkes.go.id/organization/100000001",
              "value": identifier_value or "radar-1"}]
    return {
        "resourceType": "Observation",
        "status": "final",
        "category": [{"coding": [{
            "system": "http://terminology.hl7.org/CodeSystem/observation-category",
            "code": "vital-signs", "display": "Vital Signs"}]}],
        "code": {"coding": [{"system": "http://loinc.org", "code": "8867-4",
                             "display": "Heart rate"}]},
        "subject": {"reference": patient},
        "encounter": {"reference": encounter},
        "effectiveDateTime": effective_datetime,
        "valueQuantity": {"value": bpm, "unit": "beats/minute",
                          "system": "http://unitsofmeasure.org", "code": "/min"},
        "device": {"reference": device},
        "identifier": ident,
    }


def submit_heart_rate(base_url, device_token, *, patient, encounter, device,
                      bpm, effective_datetime, identifier_value=None,
                      post_fn=None):
    post = post_fn or _default_post
    doc = build_observation(patient=patient, encounter=encounter, device=device,
                            bpm=bpm, effective_datetime=effective_datetime,
                            identifier_value=identifier_value)
    r = post(f"{base_url.rstrip('/')}/fhir-r4/v1/Observation",
             headers={"Authorization": f"Bearer {device_token}",
                      "Content-Type": "application/json"},
             data=json.dumps(doc).encode())
    return r.status_code, r.json()


def login(base_url, username, password, *, post_fn=None):
    post = post_fn or _default_post
    r = post(f"{base_url.rstrip('/')}/auth/token",
             headers={"Content-Type": "application/json"},
             data=json.dumps({"username": username,
                              "password": password}).encode())
    if r.status_code != 200:
        raise RuntimeError(f"login failed: {r.status_code}")
    return r.json()["access_token"]

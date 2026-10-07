import pytest
from fhir_server import db
from fhir_server.auth.jwt import Principal
from fhir_server.config import Settings
from fhir_server.repositories import resources
from fhir_server.validation.rules_patient import NIK_SYSTEM
from fhir_server.services.fhir_service import FhirService, FhirError

ADMIN = Principal(kind="admin", role="admin", account_id="a")
DEV = Principal(kind="device", device_id="dev-1",
                patient_id="Patient/P11111111111")


@pytest.fixture
def svc(db_path):
    conn = db.connect(db_path); db.init(conn)
    settings = Settings(db_path=db_path, jwt_secret="x" * 40)
    s = FhirService(conn, settings)
    resources.put(conn, "Organization", "100000001",
                  {"resourceType": "Organization", "id": "100000001",
                   "name": "Klinik Demo"})
    resources.put(conn, "Location", "loc-1",
                  {"resourceType": "Location", "id": "loc-1", "status": "active",
                   "name": "Poli 1"})
    resources.put(conn, "Device", "dev-1",
                  {"resourceType": "Device", "id": "dev-1", "status": "active"})
    resources.put(conn, "Patient", "P11111111111",
                  {"resourceType": "Patient", "id": "P11111111111"})
    return s


def org_payload():
    return {"resourceType": "Organization",
            "identifier": [{"use": "official",
                            "system": "http://sys-ids.kemkes.go.id/organization/100000001",
                            "value": "X"}],
            "name": "Klinik Satu"}


def test_create_assigns_id_and_version(svc):
    pid, doc, ver = svc.create(ADMIN, "Organization", org_payload())
    assert doc["id"] == pid and ver == 1
    assert svc.read(ADMIN, "Organization", pid)["name"] == "Klinik Satu"


def test_failed_validation_writes_nothing(svc):
    before = len(resources.list(svc.conn, "Patient"))
    with pytest.raises(FhirError) as e:
        svc.create(ADMIN, "Patient", {"resourceType": "Patient", "name": []})
    assert e.value.status == 400
    assert len(resources.list(svc.conn, "Patient")) == before


def test_unresolvable_reference_400(svc):
    with pytest.raises(FhirError) as e:
        svc.create(ADMIN, "Encounter", {
            "resourceType": "Encounter",
            "identifier": [{"use": "official",
                            "system": "http://sys-ids.kemkes.go.id/encounter/100000001",
                            "value": "K-1"}],
            "status": "arrived",
            "statusHistory": [{"status": "arrived",
                               "period": {"start": "2026-01-10T10:00:00+00:00"}}],
            "class": {"system": "http://terminology.hl7.org/CodeSystem/v3-ActCode",
                      "code": "AMB"},
            "subject": {"reference": "Patient/PDoesNotExist"},
            "period": {"start": "2026-01-10T10:00:00+00:00"},
            "location": [{"location": {"reference": "Location/loc-1"}}],
            "serviceProvider": {"reference": "Organization/100000001"}})
    assert e.value.status == 400


def test_read_missing_404(svc):
    with pytest.raises(FhirError) as e:
        svc.read(ADMIN, "Patient", "P404")
    assert e.value.status == 404


def test_update_bumps_version(svc):
    svc.create(ADMIN, "Organization", org_payload())
    orgs = resources.list(svc.conn, "Organization")
    target = [o for o in orgs if o["name"] == "Klinik Satu"][0]
    payload = dict(target); payload["name"] = "Klinik Dua"
    _, doc, ver = svc.update(ADMIN, "Organization", target["id"], payload)
    assert ver == 2 and doc["name"] == "Klinik Dua"


def test_device_cannot_create_foreign_observation(svc):
    with pytest.raises(FhirError) as e:
        svc.create(DEV, "Observation", {
            "resourceType": "Observation", "status": "final",
            "code": {"coding": [{"system": "http://loinc.org", "code": "8867-4"}]},
            "subject": {"reference": "Patient/P99999999999"},
            "encounter": {"reference": "Encounter/nope"},
            "device": {"reference": "Device/dev-1"},
            "valueQuantity": {"value": 70, "code": "/min",
                              "system": "http://unitsofmeasure.org"}})
    assert e.value.status == 403


def test_create_canonicalizes_offsets_to_utc(svc):
    payload = {
        "resourceType": "Encounter",
        "identifier": [{"use": "official",
                        "system": "http://sys-ids.kemkes.go.id/encounter/100000001",
                        "value": "K-UTC"}],
        "status": "arrived",
        "statusHistory": [{"status": "arrived",
                           "period": {"start": "2026-01-10T17:00:00+07:00"}}],
        "class": {"system": "http://terminology.hl7.org/CodeSystem/v3-ActCode",
                  "code": "AMB"},
        "subject": {"reference": "Patient/P11111111111"},
        "period": {"start": "2026-01-10T17:00:00+07:00"},
        "location": [{"location": {"reference": "Location/loc-1"}}],
        "serviceProvider": {"reference": "Organization/100000001"}}
    _, doc, _ = svc.create(ADMIN, "Encounter", payload)
    assert doc["period"]["start"] == "2026-01-10T10:00:00+00:00"


def test_update_unresolvable_reference_writes_nothing(svc):
    enc = {
        "resourceType": "Encounter",
        "identifier": [{"use": "official",
                        "system": "http://sys-ids.kemkes.go.id/encounter/100000001",
                        "value": "K-UPDATE-REF"}],
        "status": "arrived",
        "statusHistory": [{"status": "arrived",
                           "period": {"start": "2026-01-10T10:00:00+00:00"}}],
        "class": {"system": "http://terminology.hl7.org/CodeSystem/v3-ActCode",
                  "code": "AMB"},
        "subject": {"reference": "Patient/P11111111111"},
        "period": {"start": "2026-01-10T10:00:00+00:00"},
        "location": [{"location": {"reference": "Location/loc-1"}}],
        "serviceProvider": {"reference": "Organization/100000001"}}
    enc_id, original, _ = svc.create(ADMIN, "Encounter", enc)
    invalid = dict(original)
    invalid["subject"] = {"reference": "Patient/P00000000000"}
    with pytest.raises(FhirError) as e:
        svc.update(ADMIN, "Encounter", enc_id, invalid)
    assert e.value.status == 400
    assert svc.read(ADMIN, "Encounter", enc_id) == original


def _patient_with_nik(name_text):
    return {
        "resourceType": "Patient",
        "identifier": [{"use": "official", "system": NIK_SYSTEM,
                        "value": "3175061001900001"}],
        "name": [{"use": "official", "text": name_text, "family": name_text,
                  "given": [name_text]}],
        "gender": "male", "birthDate": "1990-01-01",
        "multipleBirthBoolean": False,
        "address": [{
            "use": "home", "line": ["Jl. Melati 1"], "city": "Jakarta",
            "postalCode": "10110", "country": "ID",
            "extension": [{
                "url": "https://fhir.kemkes.go.id/r4/StructureDefinition/"
                       "administrativeCode",
                "extension": [
                    {"url": "province", "valueCode": "31"},
                    {"url": "city", "valueCode": "3171"},
                    {"url": "district", "valueCode": "317101"},
                    {"url": "village", "valueCode": "317101001"},
                    {"url": "rt", "valueCode": "001"},
                    {"url": "rw", "valueCode": "001"}]}]}]}


def test_duplicate_nik_rejected_by_service(svc):
    svc.create(ADMIN, "Patient", _patient_with_nik("Budi"))
    with pytest.raises(FhirError) as exc:
        svc.create(ADMIN, "Patient", _patient_with_nik("Siti"))
    assert exc.value.status == 409
    assert any(i.code == "duplicate" for i in exc.value.issues)
    assert len([p for p in resources.list(svc.conn, "Patient")
                if any(i.get("system") == NIK_SYSTEM
                       and i.get("value") == "3175061001900001"
                       for i in p.get("identifier", []))]) == 1


DOC1 = Principal(kind="doctor", role="doctor", ref="Practitioner/N11111111")
DOC2 = Principal(kind="doctor", role="doctor", ref="Practitioner/N22222222")
DEV_P = Principal(kind="device", device_id="dev-1",
                  patient_id="Patient/P11111111111")


def _encounter_doc(value="K-LINK"):
    return {
        "resourceType": "Encounter",
        "identifier": [{"use": "official",
                        "system": "http://sys-ids.kemkes.go.id/encounter/100000001",
                        "value": value}],
        "status": "arrived",
        "statusHistory": [{"status": "arrived",
                           "period": {"start": "2026-01-10T10:00:00+00:00"}}],
        "class": {"system": "http://terminology.hl7.org/CodeSystem/v3-ActCode",
                  "code": "AMB"},
        "subject": {"reference": "Patient/P11111111111"},
        "period": {"start": "2026-01-10T10:00:00+00:00"},
        "location": [{"location": {"reference": "Location/loc-1"}}],
        "serviceProvider": {"reference": "Organization/100000001"}}


def test_doctor_cannot_hijack_encounter_participation(svc):
    # a doctor opening a visit is the spec's sanctioned care-link (D9/D10),
    # but a DIFFERENT doctor must not inject themselves via update
    eid, doc, _ = svc.create(DOC1, "Encounter", _encounter_doc())
    hijack = dict(doc)
    hijack["participant"] = list(doc.get("participant") or []) + [
        {"individual": {"reference": DOC2.ref}}]
    with pytest.raises(FhirError) as exc:
        svc.update(DOC2, "Encounter", eid, hijack)
    assert exc.value.status == 403
    assert svc.read(ADMIN, "Encounter", eid).get("participant") == \
        doc.get("participant")


def test_device_observation_requires_inprogress_subject_match(svc):
    resources.put(svc.conn, "Encounter", "enc-foreign", {
        "resourceType": "Encounter", "id": "enc-foreign",
        "status": "finished",
        "subject": {"reference": "Patient/P99999999999"},
        "serviceProvider": {"reference": "Organization/100000001"}})
    obs = {
        "resourceType": "Observation", "status": "final",
        "category": [{"coding": [{
            "system": "http://terminology.hl7.org/CodeSystem/observation-category",
            "code": "vital-signs"}]}],
        "code": {"coding": [{"system": "http://loinc.org", "code": "8867-4"}]},
        "subject": {"reference": "Patient/P11111111111"},
        "encounter": {"reference": "Encounter/enc-foreign"},
        "effectiveDateTime": "2026-09-29T10:06:00+00:00",
        "valueQuantity": {"value": 72, "unit": "beats/minute",
                          "system": "http://unitsofmeasure.org", "code": "/min"},
        "device": {"reference": "Device/dev-1"}}
    with pytest.raises(FhirError) as exc:
        svc.create(DEV_P, "Observation", obs)
    assert exc.value.status == 400
    assert any(i.rule_number in (20005, 10124, 20002) for i in exc.value.issues)
    # and an in-progress encounter of the RIGHT subject is required too
    resources.put(svc.conn, "Encounter", "enc-other", {
        "resourceType": "Encounter", "id": "enc-other",
        "status": "in-progress",
        "subject": {"reference": "Patient/P99999999999"},
        "serviceProvider": {"reference": "Organization/100000001"}})
    obs2 = dict(obs, encounter={"reference": "Encounter/enc-other"})
    with pytest.raises(FhirError) as exc:
        svc.create(DEV_P, "Observation", obs2)
    assert exc.value.status == 400


def test_id_collision_never_overwrites(svc, monkeypatch):
    pid, first, _ = svc.create(ADMIN, "Organization", org_payload())
    monkeypatch.setattr("fhir_server.ids.mint", lambda rt: pid)
    with pytest.raises(FhirError) as exc:
        svc.create(ADMIN, "Organization", dict(org_payload(),
                                               name="Colliding"))
    assert exc.value.status == 409
    assert svc.read(ADMIN, "Organization", pid)["name"] == "Klinik Satu"

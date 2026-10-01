from fhir_server.validation.rules_patient import validate_patient


def base(**kw):
    p = {
        "resourceType": "Patient",
        "identifier": [
            {"use": "official", "system": "https://fhir.kemkes.go.id/id/nik",
             "value": "3175061001900001"},
            {"use": "official", "system": "https://fhir.kemkes.go.id/id/ihs-number",
             "value": "P00000000001"}],
        "name": [{"use": "official", "text": "Budi", "family": "Budi",
                  "given": ["Budi"]}],
        "gender": "male",
        "birthDate": "1990-01-01",
        "multipleBirthBoolean": False,
        "address": [{
            "use": "home", "line": ["Jl. Melati 1"], "city": "Jakarta",
            "postalCode": "10110", "country": "ID",
            "extension": [{
                "url": "https://fhir.kemkes.go.id/r4/StructureDefinition/administrativeCode",
                "extension": [
                    {"url": "province", "valueCode": "31"},
                    {"url": "city", "valueCode": "3171"},
                    {"url": "district", "valueCode": "317101"},
                    {"url": "village", "valueCode": "317101001"},
                    {"url": "rt", "valueCode": "001"},
                    {"url": "rw", "valueCode": "001"}]}]}],
    }
    p.update(kw)
    return p


def test_valid_patient_create_passes_without_client_ihs():
    p = base()
    p["identifier"] = [p["identifier"][0]]  # NIK only on create
    assert validate_patient(p, is_create=True) == []


def test_nik_required():
    p = base(); p["identifier"] = []
    assert any(i.rule_number == 10117 for i in validate_patient(p, is_create=True))


def test_nik_must_be_16_digits():
    p = base()
    p["identifier"] = [{"use": "official", "system": "https://fhir.kemkes.go.id/id/nik",
                        "value": "123"}]
    assert any(i.rule_number == 20004 for i in validate_patient(p, is_create=True))


def test_client_sent_ihs_rejected_on_create():
    assert any(i.rule_number == 20004
               for i in validate_patient(base(), is_create=True))


def test_missing_name_wajib():
    p = base(name=None)
    assert any(i.rule_number == 10263 for i in validate_patient(p, is_create=True))


def test_gender_limited_and_required():
    p = base(gender="other")
    assert any(i.rule_number == 20004 for i in validate_patient(p, is_create=True))
    p2 = base(); del p2["gender"]
    assert any(i.rule_number == 20004 for i in validate_patient(p2, is_create=True))


def test_missing_birthdate_fails():
    p = base(); del p["birthDate"]
    assert any(i.rule_number == 20004 for i in validate_patient(p, is_create=True))


def test_missing_address_fails():
    p = base(); p["address"] = []
    assert any(i.rule_number == 20004 for i in validate_patient(p, is_create=True))


def test_address_needs_administrative_code():
    p = base(); p["address"][0] = {"use": "home", "line": ["x"]}
    assert any(i.rule_number == 20004 for i in validate_patient(p, is_create=True))


def test_multiple_birth_wajib():
    p = base()
    for k in ("multipleBirthBoolean", "multipleBirthInteger"):
        p.pop(k, None)
    assert any(i.rule_number == 10263 for i in validate_patient(p, is_create=True))


def test_gender_family_wrong_type_is_structural_not_here():
    p = base(gender="unknown")
    assert any(i.rule_number == 20004 for i in validate_patient(p, is_create=True))

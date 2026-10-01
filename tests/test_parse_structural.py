from fhir_server.validation.parse import structural_issues


def valid_patient():
    return {
        "resourceType": "Patient",
        "active": True,
        "gender": "female",
        "birthDate": "1990-04-02",
        "name": [{"text": "Siti", "family": "Siti", "given": ["Siti"]}],
    }


def test_valid_patient_no_issues():
    issues, model = structural_issues("Patient", valid_patient())
    assert issues == [] and model is not None


def test_rejects_quoted_boolean():
    p = valid_patient(); p["active"] = "false"
    issues, model = structural_issues("Patient", p)
    assert model is None
    assert any(i.expression == "Patient.active" for i in issues)


def test_rejects_quoted_integer():
    issues, model = structural_issues("Patient", {"resourceType": "Patient",
        "multipleBirthInteger": "3"})
    assert model is None and issues


def test_rejects_array_on_scalar():
    p = valid_patient(); p["gender"] = ["female"]
    issues, model = structural_issues("Patient", p)
    assert model is None
    assert any(i.expression == "Patient.gender" for i in issues)


def test_rejects_scalar_where_array_expected():
    p = valid_patient(); p["name"] = {"text": "Siti"}
    issues, model = structural_issues("Patient", p)
    assert model is None


def test_rejects_unknown_element():
    p = valid_patient(); p["bogusField"] = 1
    issues, model = structural_issues("Patient", p)
    assert model is None
    assert any(i.expression == "Patient.bogusField" for i in issues)


def test_rejects_bad_date_format():
    p = valid_patient(); p["birthDate"] = "02-04-1990"
    issues, model = structural_issues("Patient", p)
    assert model is None
    assert any(i.code == "format" for i in issues)


def test_rejects_non_object_payload():
    issues, model = structural_issues("Patient", ["nope"])
    assert model is None and issues


def test_wrong_resource_type_key():
    issues, model = structural_issues("Patient", {"resourceType": "Observation"})
    assert model is None and issues

from .issues import Issue, R_BAD_IDENTIFIER_SYSTEM, R_WAJIB_MISSING, \
    L_PATIENT_IDENTITY

NIK_SYSTEM = "https://fhir.kemkes.go.id/id/nik"
IHS_SYSTEM = "https://fhir.kemkes.go.id/id/ihs-number"
ADMIN_CODE_URL = ("https://fhir.kemkes.go.id/r4/StructureDefinition/"
                  "administrativeCode")
_ADMIN_SUBS = ("province", "city", "district", "village", "rt", "rw")


def _issue(text, rule, expr="Patient"):
    return Issue(code="value", details_text=text, expression=expr,
                 rule_number=rule)


def validate_patient(payload, *, is_create: bool):
    out = []
    identifiers = payload.get("identifier") or []
    nik = [i for i in identifiers if i.get("system") == NIK_SYSTEM]
    if not identifiers:
        # missing NIK identifier system entirely
        out.append(_issue(f"Invalid identifier system: {NIK_SYSTEM} is required",
                          R_BAD_IDENTIFIER_SYSTEM, "Patient.identifier"))
    elif not nik:
        out.append(_issue(f"Missing NIK identifier system {NIK_SYSTEM}",
                          L_PATIENT_IDENTITY, "Patient.identifier"))
    else:
        value = nik[0].get("value") or ""
        if not (value.isdigit() and len(value) == 16):
            out.append(_issue(f"NIK must be 16 digits, got '{value}'",
                              L_PATIENT_IDENTITY, "Patient.identifier[0].value"))
    if is_create:
        if any(i.get("system") == IHS_SYSTEM for i in identifiers):
            out.append(_issue(
                "ihs-number identifier is server-issued; client may not send it",
                L_PATIENT_IDENTITY, "Patient.identifier"))
        if payload.get("id"):
            out.append(_issue("Patient.id is server-issued",
                              L_PATIENT_IDENTITY, "Patient.id"))
    if not payload.get("name"):
        out.append(_issue("Wajib element missing: Patient.name",
                          R_WAJIB_MISSING, "Patient.name"))
    if not payload.get("birthDate"):
        out.append(_issue("MPI requires birthDate for NIK patients",
                          L_PATIENT_IDENTITY, "Patient.birthDate"))
    if payload.get("gender") not in ("male", "female"):
        out.append(_issue("MPI requires gender male or female",
                          L_PATIENT_IDENTITY, "Patient.gender"))
    addresses = payload.get("address") or []
    if not addresses:
        out.append(_issue("MPI requires address for NIK patients",
                          L_PATIENT_IDENTITY, "Patient.address"))
    else:
        admin = [e for e in (addresses[0].get("extension") or [])
                 if e.get("url") == ADMIN_CODE_URL]
        subs = {e.get("url") for e in admin[0].get("extension") or []} \
            if admin else set()
        if not admin or not set(_ADMIN_SUBS) <= subs:
            out.append(_issue(
                "address requires administrativeCode with"
                " province/city/district/village/rt/rw",
                L_PATIENT_IDENTITY, "Patient.address[0].extension"))
    if "multipleBirthBoolean" not in payload \
            and "multipleBirthInteger" not in payload:
        out.append(_issue("Wajib element missing: Patient.multipleBirth[x]",
                          R_WAJIB_MISSING, "Patient.multipleBirth[x]"))
    return out

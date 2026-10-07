import datetime as dt
import re

from .issues import (Issue, R_DATETIME, R_EMPTY_TEXT, R_BAD_CODING_SYSTEM,
                     R_MISSING_REFERENCE, L_EARLIEST_DATE,
                     L_UNRESOLVABLE_REFERENCE)

ALLOWED_SYSTEMS = {
    "http://loinc.org",
    "http://unitsofmeasure.org",
    "http://hl7.org/fhir/administrative-gender",
    "http://hl7.org/fhir/observation-status",
    "http://hl7.org/fhir/encounter-status",
    "http://hl7.org/fhir/location-status",
    "http://hl7.org/fhir/device-status",
    "http://hl7.org/fhir/identifier-use",
    "http://hl7.org/fhir/name-use",
    "http://hl7.org/fhir/address-use",
    "http://hl7.org/fhir/address-type",
    "http://hl7.org/fhir/contact-point-system",
    "http://hl7.org/fhir/contact-point-use",
    "http://terminology.hl7.org/CodeSystem/observation-category",
    "http://terminology.hl7.org/CodeSystem/v3-ActCode",
    "http://terminology.hl7.org/CodeSystem/v3-ParticipationType",
    "http://terminology.hl7.org/CodeSystem/v3-ActState",
    "http://terminology.hl7.org/CodeSystem/organization-type",
    "http://terminology.hl7.org/CodeSystem/contactentity-type",
    "http://terminology.hl7.org/CodeSystem/encounter-type",
    "http://terminology.hl7.org/CodeSystem/v2-0131",
    "http://terminology.hl7.org/CodeSystem/v3-RoleCode",
    "http://terminology.hl7.org/CodeSystem/location-physical-type",
    "http://terminology.hl7.org/CodeSystem/v3-MaritalStatus",
    "http://terminology.hl7.org/CodeSystem/data-absent-reason",
    "http://terminology.hl7.org/CodeSystem/observation-interpretation",
    "urn:ietf:bcp:47",
    "https://fhir.kemkes.go.id/id/nik",
    "https://fhir.kemkes.go.id/id/nik-ibu",
    "https://fhir.kemkes.go.id/id/ihs-number",
    "https://fhir.kemkes.go.id/id/paspor",
    "https://fhir.kemkes.go.id/id/kk",
    "https://fhir.kemkes.go.id/r4/StructureDefinition/administrativeCode",
    "http://sys-ids.kemkes.go.id/organization",
    "http://sys-ids.kemkes.go.id/location",
    "http://sys-ids.kemkes.go.id/encounter",
    "http://sys-ids.kemkes.go.id/observation",
    "http://sys-ids.kemkes.go.id/device",
    "http://sys-ids.kemkes.go.id/practitioner",
    "http://terminology.hl7.org/CodeSystem/v2-0116",
    "http://terminology.hl7.org/CodeSystem/admit-source",
    "http://terminology.hl7.org/CodeSystem/discharge-disposition",
    "http://terminology.hl7.org/CodeSystem/service-type",
    "http://terminology.hl7.org/CodeSystem/v3-ActPriority",
    "http://terminology.hl7.org/CodeSystem/diagnosis-role",
    "http://terminology.hl7.org/CodeSystem/encounter-reason",
    "http://terminology.hl7.org/CodeSystem/referencerange-meaning",
    "http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation",
    "http://sys-ids.kemkes.go.id/kfa",
}

_DATE_ONLY = re.compile(r"^\d{4}(-\d{2}(-\d{2})?)?$")
_DATE_SHAPED = re.compile(r"^\d{4}-\d{2}")
_FLOOR_DEFAULT = "2014-06-03"
_GRACE = dt.timedelta(minutes=1)


def _walk(node, path=""):
    if isinstance(node, dict):
        for k, v in node.items():
            yield from _walk(v, f"{path}.{k}" if path else k)
    elif isinstance(node, list):
        for idx, v in enumerate(node):
            yield from _walk(v, f"{path}[{idx}]")
    else:
        yield path, node


def _is_date_shaped(value) -> bool:
    return isinstance(value, str) and bool(_DATE_SHAPED.match(value))


def check_datetimes(payload, resource_type, earliest_date=_FLOOR_DEFAULT):
    issues = []
    now = dt.datetime.now(dt.timezone.utc)
    floor = dt.date.fromisoformat(earliest_date)
    for path, value in _walk(payload):
        if not _is_date_shaped(value):
            continue
        try:
            parsed = dt.datetime.fromisoformat(value.replace("Z", "+00:00"))
        except ValueError:
            issues.append(Issue(code="format",
                                details_text=f"Invalid date time format : {value}"
                                             f". Format allowed : YYYY-MM-DDThh:mm:ss+00:00",
                                expression=f"{resource_type}.{path}",
                                rule_number=R_DATETIME))
            continue
        date_only = bool(_DATE_ONLY.match(value))
        if not date_only and parsed.utcoffset() is None:
            issues.append(Issue(code="format",
                                details_text=f"Invalid date time format : {value}"
                                             f". Format allowed : YYYY-MM-DDThh:mm:ss+00:00",
                                expression=f"{resource_type}.{path}",
                                rule_number=R_DATETIME))
            continue
        as_date = (parsed.astimezone(dt.timezone.utc).date()
                   if parsed.utcoffset() is not None else parsed.date())
        # S4's floor is about record event dates, not demographic dates: a
        # Patient's birthDate may precede 2014 (final review issue 11).
        is_birth = path.split(".")[-1].split("[")[0] == "birthDate"
        if as_date < floor and not is_birth:
            issues.append(Issue(code="value",
                                details_text=f"Date {value} earlier than allowed"
                                             f" earliest {earliest_date}",
                                expression=f"{resource_type}.{path}",
                                rule_number=L_EARLIEST_DATE))
        if not path.endswith("period.end"):
            if date_only:
                if as_date > now.date() + _GRACE:
                    issues.append(Issue(code="value",
                                        details_text=f"Invalid date value : {value}"
                                                     f" Not Allowed : Future Date",
                                        expression=f"{resource_type}.{path}",
                                        rule_number=R_DATETIME))
            elif parsed > now + _GRACE:
                issues.append(Issue(code="value",
                                    details_text=f"Invalid date time value : {value}"
                                                 f" Not Allowed : Future Date",
                                    expression=f"{resource_type}.{path}",
                                    rule_number=R_DATETIME))
    return issues


def canonicalize_datetimes(payload, resource_type="Resource"):
    """Return a copy with every date-shaped string normalized to +00:00 UTC
    (spec: emit canonical UTC). Date-only values pass through unchanged."""
    def walk(node, path=""):
        if isinstance(node, dict):
            return {k: walk(v, f"{path}.{k}" if path else k)
                    for k, v in node.items()}
        if isinstance(node, list):
            return [walk(v, f"{path}[{idx}]") for idx, v in enumerate(node)]
        if _is_date_shaped(node) and not _DATE_ONLY.match(node):
            try:
                parsed = dt.datetime.fromisoformat(node.replace("Z", "+00:00"))
            except ValueError:
                return node
            if parsed.utcoffset() is None:
                return node
            return parsed.astimezone(dt.timezone.utc).strftime(
                "%Y-%m-%dT%H:%M:%S+00:00")
        return node
    return walk(payload)


def check_empty_strings(payload, resource_type):
    return [Issue(code="value", details_text=f"Text is empty: '{value}'",
                  expression=f"{resource_type}.{path}",
                  rule_number=R_EMPTY_TEXT)
            for path, value in _walk(payload)
            if isinstance(value, str) and value.strip() == ""]


def normalize_system(system: str) -> tuple[str, bool]:
    for prefix in ("https://www.hl7.org/fhir/Codesystem",
                   "http://www.hl7.org/fhir/Codesystem",
                   "https://www.hl7.org/fhir/CodeSystem"):
        if system.startswith(prefix):
            tail = system.rsplit("/", 1)[-1]
            return f"http://terminology.hl7.org/CodeSystem/{tail}", True
    return system, False


def check_coding_systems(payload, resource_type):
    issues = []

    def walk(node, path=""):
        if isinstance(node, dict):
            if isinstance(node.get("coding"), list):
                for idx, c in enumerate(node["coding"]):
                    if isinstance(c, dict) and "system" in c:
                        sys_ = c["system"]
                        norm, _ = normalize_system(sys_)
                        if norm not in ALLOWED_SYSTEMS:
                            issues.append(Issue(
                                code="value",
                                details_text=f"Invalid coding system: {sys_}",
                                expression=f"{resource_type}.{path}.coding[{idx}].system",
                                rule_number=R_BAD_CODING_SYSTEM))
            for k, v in node.items():
                walk(v, f"{path}.{k}" if path else k)
        elif isinstance(node, list):
            for idx, v in enumerate(node):
                walk(v, f"{path}[{idx}]")

    walk(payload)
    return issues


def check_references(payload, resource_type, exists_fn):
    issues = []

    def walk(node, path=""):
        if isinstance(node, dict):
            if not node and path:
                issues.append(Issue(
                    code="value",
                    details_text=f"Reference is mandatory : {resource_type}.{path}",
                    expression=f"{resource_type}.{path}",
                    rule_number=R_MISSING_REFERENCE))
                return
            if "reference" in node:
                ref = node["reference"]
                if not isinstance(ref, str) or "/" not in ref:
                    issues.append(Issue(
                        code="value",
                        details_text=f"Reference is mandatory : {resource_type}.{path}",
                        expression=f"{resource_type}.{path}",
                        rule_number=R_MISSING_REFERENCE))
                else:
                    t, _, rid = ref.partition("/")
                    if not t or not rid:
                        issues.append(Issue(
                            code="value",
                            details_text=f"Reference is mandatory : {resource_type}.{path}",
                            expression=f"{resource_type}.{path}",
                            rule_number=R_MISSING_REFERENCE))
                    elif not exists_fn(t, rid):
                        issues.append(Issue(
                            code="value",
                            details_text=f"Unresolvable reference: {ref}",
                            expression=f"{resource_type}.{path}",
                            rule_number=L_UNRESOLVABLE_REFERENCE))
            for k, v in node.items():
                walk(v, f"{path}.{k}" if path else k)
        elif isinstance(node, list):
            for idx, v in enumerate(node):
                walk(v, f"{path}[{idx}]")

    walk(payload)
    return issues

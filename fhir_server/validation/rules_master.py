from .issues import (Issue, R_BAD_IDENTIFIER_SYSTEM, R_WAJIB_MISSING,
                     L_DEVICE_RULE, L_LOCATION_POSITION)


def _identifier_system_issue(payload, prefix):
    out = []
    for idx, ident in enumerate(payload.get("identifier") or []):
        system = ident.get("system")
        if system is not None and not system.startswith(prefix):
            out.append(Issue(code="value",
                             details_text=f"Invalid identifier system: {system}",
                             expression=f"{payload.get('resourceType', 'X')}"
                                        f".identifier[{idx}].system",
                             rule_number=R_BAD_IDENTIFIER_SYSTEM))
    return out


def validate_organization(payload):
    out = _identifier_system_issue(
        payload, "http://sys-ids.kemkes.go.id/organization/")
    for idx, contact in enumerate(payload.get("contact") or []):
        purpose = contact.get("purpose")
        if not purpose:
            out.append(Issue(code="value",
                             details_text="Wajib element missing:"
                                          " Organization.contact.purpose",
                             expression=f"Organization.contact[{idx}].purpose",
                             rule_number=R_WAJIB_MISSING))
        elif not purpose.get("coding"):
            out.append(Issue(code="value",
                             details_text="Wajib element missing:"
                                          " Organization.contact.purpose.coding",
                             expression=f"Organization.contact[{idx}].purpose.coding",
                             rule_number=R_WAJIB_MISSING))
    return out


def validate_location(payload):
    out = _identifier_system_issue(
        payload, "http://sys-ids.kemkes.go.id/location/")
    pos = payload.get("position")
    if isinstance(pos, dict):
        missing = [k for k in ("longitude", "latitude") if k not in pos]
        if missing:
            out.append(Issue(code="value",
                             details_text="Wajib element missing:"
                                          f" Location.position.{'/'.join(missing)}",
                             expression="Location.position",
                             rule_number=L_LOCATION_POSITION))
    return out


def validate_practitioner(payload):
    out = []
    for idx, qual in enumerate(payload.get("qualification") or []):
        if not (qual.get("code") or {}).get("coding"):
            out.append(Issue(code="value",
                             details_text="Wajib element missing:"
                                          " Practitioner.qualification.code.coding",
                             expression=f"Practitioner.qualification[{idx}]"
                                        f".code.coding",
                             rule_number=R_WAJIB_MISSING))
    return out


def validate_device(payload):
    allowed = {"active", "inactive", "entered-in-error"}
    status = payload.get("status")
    if status is not None and status not in allowed:
        return [Issue(code="value",
                      details_text=f"Invalid device status: {status}",
                      expression="Device.status",
                      rule_number=L_DEVICE_RULE)]
    return []

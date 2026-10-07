from .auth.jwt import Principal
from .repositories import resources as res
from .validation.issues import Issue, L_AUTH


class AuthzError(Exception):
    def __init__(self, message="Access denied"):
        super().__init__(message)
        self.issues = [Issue(code="forbidden", details_text=message,
                             rule_number=L_AUTH)]
        self.status = 403


_DOCTOR_READABLE = {"Organization", "Location", "Practitioner", "Patient",
                    "Device", "Encounter", "Observation"}
_PATIENT_READABLE = {"Patient", "Encounter", "Observation"}


def _own_id(principal: Principal) -> str | None:
    if principal.ref and "/" in principal.ref:
        return principal.ref.split("/", 1)[1]
    return None


def participates_in_patient(conn, practitioner_ref, patient_id) -> bool:
    for enc in res.list(conn, "Encounter"):
        if (enc.get("subject") or {}).get("reference") != f"Patient/{patient_id}":
            continue
        for p in enc.get("participant") or []:
            if (p.get("individual") or {}).get("reference") == practitioner_ref:
                return True
    return False


def _doctor_reads_patient(conn, principal, resource) -> bool:
    pid = resource.get("id")
    return bool(pid) and participates_in_patient(conn, principal.ref, pid)


def doctor_reads_encounter(resource, principal) -> bool:
    for p in resource.get("participant") or []:
        if (p.get("individual") or {}).get("reference") == principal.ref:
            return True
    return False


def doctor_reads_observation(conn, principal, resource) -> bool:
    enc_ref = (resource.get("encounter") or {}).get("reference", "")
    if not enc_ref or "/" not in enc_ref:
        return False
    enc = res.get(conn, "Encounter", enc_ref.split("/", 1)[1])
    if not enc:
        return False
    return doctor_reads_encounter(enc, principal)


def check(principal, action, resource_type, resource=None, *, conn=None):
    if principal.kind == "admin":
        return None
    if principal.kind == "doctor":
        if action == "delete":
            raise AuthzError("Doctors cannot delete resources")
        if action in ("create", "update"):
            if resource_type == "Encounter":
                if action == "update" and not doctor_reads_encounter(
                        resource or {}, principal):
                    raise AuthzError("Doctor is not a participant of this Encounter")
                return None
            raise AuthzError(f"Doctors cannot {action} {resource_type}")
        if resource_type not in _DOCTOR_READABLE:
            raise AuthzError(f"Doctors cannot read {resource_type}")
        if resource_type == "Patient":
            if not _doctor_reads_patient(conn, principal, resource):
                raise AuthzError("Doctor is not a participant for this patient")
        elif resource_type == "Encounter":
            if not doctor_reads_encounter(resource or {}, principal):
                raise AuthzError(
                    "Doctor is not a participant of this Encounter")
        elif resource_type == "Observation":
            if not doctor_reads_observation(conn, principal, resource):
                raise AuthzError(
                    "Doctor has no participated encounter for this Observation")
        return None
    if principal.kind == "patient":
        if action != "read":
            raise AuthzError("Patients are read-only")
        if resource_type not in _PATIENT_READABLE:
            raise AuthzError(f"Patients cannot read {resource_type}")
        own = _own_id(principal)
        if resource_type == "Patient":
            if resource.get("id") != own:
                raise AuthzError("Patients may read only their own record")
        else:
            subj = (resource.get("subject") or {}).get("reference") or ""
            if not subj.endswith(f"/{own}"):
                raise AuthzError("Patients may read only their own records")
        return None
    if principal.kind == "device":
        if action == "create" and resource_type == "Observation":
            subj = (resource.get("subject") or {}).get("reference")
            dev = (resource.get("device") or {}).get("reference")
            if subj != principal.patient_id or dev != f"Device/{principal.device_id}":
                raise AuthzError("Device token not authorized for this Observation")
            return None
        if action == "read" and resource_type == "Observation":
            dev = (resource.get("device") or {}).get("reference")
            if dev != f"Device/{principal.device_id}":
                raise AuthzError("Device may read only its own Observations")
            return None
        if (action == "read" and resource_type == "Device"
                and resource.get("id") == principal.device_id):
            return None
        raise AuthzError("Device token not authorized for this action")
    raise AuthzError("Unknown principal kind")


def filter_search(principal, resource_type, params, conn) -> dict:
    params = dict(params)
    if principal.kind == "admin":
        return params
    if principal.kind == "patient":
        own_id = _own_id(principal)
        if own_id is None:
            raise AuthzError("Patient account has no subject reference")
        if resource_type == "Patient":
            if "identifier" in params:
                if not str(params["identifier"]).endswith(own_id):
                    raise AuthzError("Patients may search only their own record")
                params.pop("identifier")
            if "id" in params and params["id"] != own_id:
                raise AuthzError("Patients may search only their own record")
            params["id"] = own_id
            return params
        if resource_type not in ("Encounter", "Observation"):
            raise AuthzError(f"Patients cannot search {resource_type}")
        subject = params.get("subject") or params.get("patient")
        if subject is None:
            params["subject"] = principal.ref
        elif subject != principal.ref:
            raise AuthzError("Patients may search only their own records")
        return params
    if principal.kind == "doctor":
        if resource_type == "Patient":
            # post-filter by participation in the service (marker keyed
            # to the search post-filter, see FhirService.search)
            params["_scope_participant"] = principal.ref
            return params
        if resource_type in ("Encounter", "Observation"):
            subject = params.get("subject") or params.get("patient")
            if subject:
                pid = subject.split("/", 1)[1] if "/" in subject else subject
                if not participates_in_patient(conn, principal.ref, pid):
                    raise AuthzError(
                        "Doctor has no participated encounter for this patient")
            # rows are still post-filtered by participation: one patient can
            # have encounters this doctor is not on (final review issue 4)
            params["_scope_participant"] = principal.ref
            return params
        if resource_type in ("Organization", "Location", "Practitioner", "Device"):
            return params
        raise AuthzError(f"Doctors cannot search {resource_type}")
    if principal.kind == "device":
        if resource_type == "Observation":
            subject = params.get("subject") or params.get("patient")
            if subject and subject != principal.patient_id:
                raise AuthzError("Device may search only its assigned patient")
            params["subject"] = principal.patient_id
            return params
        raise AuthzError(f"Devices cannot search {resource_type}")
    raise AuthzError("Unknown principal kind")

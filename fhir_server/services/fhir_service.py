import secrets

from .. import authz, ids
from ..auth.jwt import Principal
from ..authz import AuthzError
from ..repositories import devices as devices_repo
from ..repositories import resources as res
from ..validation import parse, rules_common, rules_encounter, rules_master, \
    rules_observation, rules_patient
from ..validation.issues import Issue


class FhirError(Exception):
    def __init__(self, issues, status):
        super().__init__(issues[0].details_text if issues else "error")
        self.issues = issues
        self.status = status


def _as_fhir_error(exc: AuthzError) -> FhirError:
    return FhirError(exc.issues, exc.status)


def _ensure_participant(doc, principal):
    """D10: a doctor creating/updating an Encounter is a participant of it,
    so their read access derives from the resource itself."""
    if principal.kind != "doctor" or not principal.ref:
        return doc
    participants = list(doc.get("participant") or [])
    if any((p.get("individual") or {}).get("reference") == principal.ref
           for p in participants):
        return doc
    participants.append({"individual": {"reference": principal.ref}})
    doc = dict(doc)
    doc["participant"] = participants
    return doc


class FhirService:
    def __init__(self, conn, settings):
        self.conn = conn
        self.settings = settings

    @property
    def org_id(self) -> str:
        orgs = res.list(self.conn, "Organization")
        return orgs[0].get("id", "") if orgs else ""

    def _exists(self, t, i):
        return res.exists(self.conn, t, i)

    def _rule_sets(self, resource_type, payload, *, existing=None,
                   principal=None, for_update=False):
        org = self.org_id
        out = []
        out += rules_common.check_datetimes(payload, resource_type,
                                            self.settings.earliest_date)
        out += rules_common.check_empty_strings(payload, resource_type)
        out += rules_common.check_coding_systems(payload, resource_type)
        if resource_type == "Organization":
            out += rules_master.validate_organization(payload)
        elif resource_type == "Location":
            out += rules_master.validate_location(payload)
        elif resource_type == "Practitioner":
            out += rules_master.validate_practitioner(payload)
        elif resource_type == "Device":
            out += rules_master.validate_device(payload)
        elif resource_type == "Patient":
            def nik_exists(value):
                for p_ in res.list(self.conn, "Patient"):
                    for ident in p_.get("identifier") or []:
                        if (ident.get("system") == rules_patient.NIK_SYSTEM
                                and ident.get("value") == value):
                            return True
                return False
            out += rules_patient.validate_patient(
                payload, is_create=existing is None,
                nik_exists_fn=nik_exists if existing is None else None)
        elif resource_type == "Encounter":
            def dup(value):
                for e in res.list(self.conn, "Encounter"):
                    for ident in e.get("identifier") or []:
                        if ident.get("value") == value:
                            return True
                return False
            out += rules_encounter.validate_encounter(
                payload, existing=existing, org_id=org, duplicate_fn=dup)
        elif resource_type == "Observation":
            device_ref, assigned = None, None
            if principal is not None and principal.kind == "device":
                device_ref = f"Device/{principal.device_id}"
                assigned = principal.patient_id
            def encounter_getter(ref):
                if ref and "/" in ref:
                    return res.get(self.conn, "Encounter", ref.split("/", 1)[1])
                return None
            out += rules_observation.validate_observation(
                payload, org_id=org, device_ref=device_ref,
                assigned_patient=assigned,
                encounter_getter=encounter_getter if principal is not None
                and principal.kind == "device" else None)
        # (final review issue 5) references are checked on update too
        out += rules_common.check_references(payload, resource_type,
                                             self._exists)
        return out

    @staticmethod
    def _raise(issues):
        status = 409 if any(i.code == "duplicate" for i in issues) else 400
        raise FhirError(issues, status)

    def _validated(self, principal, resource_type, payload, *, existing=None,
                   for_update=False):
        issues, _ = parse.structural_issues(resource_type, payload)
        if not issues:
            issues = self._rule_sets(resource_type, payload, existing=existing,
                                     principal=principal,
                                     for_update=for_update)
        if issues:
            self._raise(issues)
        return rules_common.canonicalize_datetimes(payload, resource_type)

    def _mint(self, resource_type, doc, org):
        new_id = ids.mint(resource_type)
        doc = dict(doc)
        doc["id"] = new_id
        if resource_type == "Patient":
            idents = list(doc.get("identifier") or [])
            idents.append({"use": "official",
                           "system": "https://fhir.kemkes.go.id/id/ihs-number",
                           "value": new_id})
            doc["identifier"] = idents
        if resource_type == "Observation":
            idents = []
            for i in doc.get("identifier") or []:
                i = dict(i)
                if str(i.get("system", "")).startswith(
                        "http://sys-ids.kemkes.go.id/organization/"):
                    i["system"] = f"http://sys-ids.kemkes.go.id/observation/{org}"
                idents.append(i)
            if not idents:
                idents = [{"use": "usual",
                           "system": f"http://sys-ids.kemkes.go.id/observation/{org}",
                           "value": new_id}]
            doc["identifier"] = idents
        return new_id, doc

    def create(self, principal, resource_type, payload):
        try:
            authz.check(principal, "create", resource_type, payload,
                        conn=self.conn)
        except AuthzError as exc:
            raise _as_fhir_error(exc) from exc
        doc = self._validated(principal, resource_type, payload)
        new_id, doc = self._mint(resource_type, doc, self.org_id)
        if resource_type == "Encounter":
            doc = _ensure_participant(doc, principal)
        if res.exists(self.conn, resource_type, new_id):
            raise FhirError([Issue(
                code="duplicate",
                details_text=f"Id collision: {resource_type}/{new_id}"
                             " already exists (refusing to overwrite)")], 409)
        res.put(self.conn, resource_type, new_id, doc)
        return new_id, res.get(self.conn, resource_type, new_id), 1

    def read(self, principal, resource_type, id_):
        doc = res.get(self.conn, resource_type, id_)
        if doc is None:
            raise FhirError([Issue(code="not-found",
                                   details_text=f"{resource_type}/{id_} not found")],
                            404)
        try:
            authz.check(principal, "read", resource_type, doc, conn=self.conn)
        except AuthzError as exc:
            raise _as_fhir_error(exc) from exc
        return doc

    def update(self, principal, resource_type, id_, payload):
        existing = res.get(self.conn, resource_type, id_)
        if existing is None:
            raise FhirError([Issue(code="not-found",
                                   details_text=f"{resource_type}/{id_} not found")],
                            404)
        try:
            # (final review issue 3) participation is a fact the server holds,
            # not a claim in the payload: authorize against the stored row
            authz.check(principal, "update", resource_type, existing,
                        conn=self.conn)
        except AuthzError as exc:
            raise _as_fhir_error(exc) from exc
        doc = self._validated(principal, resource_type, payload,
                              existing=existing, for_update=True)
        doc = dict(doc)
        doc["id"] = id_
        if resource_type == "Encounter":
            doc = _ensure_participant(doc, principal)
        version = res.put(self.conn, resource_type, id_, doc)
        return id_, res.get(self.conn, resource_type, id_), version

    def delete(self, principal, resource_type, id_):
        try:
            authz.check(principal, "delete", resource_type, conn=self.conn)
        except AuthzError as exc:
            raise _as_fhir_error(exc) from exc
        if not res.delete(self.conn, resource_type, id_):
            raise FhirError([Issue(code="not-found",
                                   details_text=f"{resource_type}/{id_} not found")],
                            404)

    def provision_device(self, principal, device_id, patient_ref):
        if principal.kind != "admin":
            raise FhirError([Issue(code="forbidden",
                                   details_text="Only admins may provision devices",
                                   rule_number=20007)], 403)
        if not res.exists(self.conn, "Device", device_id):
            raise FhirError([Issue(code="not-found",
                                   details_text="Device not found")], 404)
        pid = patient_ref.split("/", 1)[-1] if "/" in patient_ref else patient_ref
        if not res.exists(self.conn, "Patient", pid):
            raise FhirError([Issue(code="not-found",
                                   details_text="Patient not found")], 404)
        token = secrets.token_urlsafe(32)
        devices_repo.create_token(self.conn, device_id, patient_ref, token)
        return token


SUPPORTED_PARAMS = {
    "Patient": {"identifier", "name", "birthdate", "gender", "id"},
    "Practitioner": {"identifier", "name", "id"},
    "Organization": {"name", "id"},
    "Location": {"name", "organization", "id"},
    "Encounter": {"subject", "patient", "status", "participant", "id"},
    "Observation": {"subject", "encounter", "code", "date", "id"},
    "Device": {"identifier", "patient", "id"},
}


class _BadParam(Exception):
    pass


def _matches_identifier(doc, value):
    raw = str(value)
    if "|" not in raw:  # R4 token search allows value-only
        want_system, want_value = "", raw
    else:
        want_system, _, want_value = raw.partition("|")
    for ident in doc.get("identifier") or []:
        if want_value and ident.get("value") != want_value:
            continue
        if want_system and ident.get("system") != want_system:
            continue
        if want_value or want_system:
            return True
    return False


def _matches_name(doc, needle):
    needle = needle.lower()
    for n in doc.get("name") or []:
        fields = [n.get("text"), n.get("family")] + list(n.get("given") or [])
        if any(f and needle in f.lower() for f in fields):
            return True
    return False


def _search_impl(self, principal, resource_type, params):
    from ..validation.issues import L_SEARCH_PARAM

    def bad_param(message, expr):
        return FhirError([Issue(code="value", details_text=message,
                                expression=expr,
                                rule_number=L_SEARCH_PARAM)], 400)

    supported = SUPPORTED_PARAMS.get(resource_type)
    if supported is None:
        raise FhirError([Issue(code="not-found",
                               details_text=f"Unsupported resource type"
                                            f" {resource_type}")], 404)
    unknown = [k for k in params if k not in supported and k != "_count"]
    if unknown:
        raise bad_param(f"Unknown search parameter: {unknown[0]}",
                        f"{resource_type}.{unknown[0]}")
    if "name" in params and len(params["name"]) < 3:
        raise bad_param("name needs >= 3 characters", f"{resource_type}.name")
    try:
        effective = authz.filter_search(principal, resource_type, params,
                                        self.conn)
    except AuthzError as exc:
        raise _as_fhir_error(exc) from exc
    marker = effective.pop("_scope_participant", None)
    docs = res.list(self.conn, resource_type)
    try:
        matched = [d for d in docs
                   if all(self._param_match(resource_type, d, k, v)
                          for k, v in effective.items())]
    except _BadParam as exc:
        raise bad_param(str(exc), resource_type) from exc
    if principal.kind == "doctor":
        if resource_type == "Encounter":
            matched = [d for d in matched
                       if authz.doctor_reads_encounter(d, principal)]
        elif resource_type == "Observation":
            matched = [d for d in matched
                       if authz.doctor_reads_observation(self.conn, principal, d)]
        elif resource_type == "Patient":
            matched = [d for d in matched
                       if authz.participates_in_patient(
                           self.conn, principal.ref, d.get("id"))]
    try:
        count = int(effective.get("_count", 50))
    except (TypeError, ValueError):
        raise bad_param("_count must be an integer", f"{resource_type}._count")
    count = max(0, min(count, 100))
    bundle = {"resourceType": "Bundle", "type": "searchset",
              "total": len(matched)}
    if matched and count > 0:
        bundle["entry"] = [{"resource": d} for d in matched[:count]]
    return bundle


def _param_match(self, resource_type, doc, key, value):
    if key == "_count":
        return True
    if key == "id":
        return doc.get("id") == value
    if key in ("subject", "patient"):
        if resource_type == "Device":
            return (doc.get("patient") or {}).get("reference") == value
        return (doc.get("subject") or {}).get("reference") == value
    if key == "identifier":
        return _matches_identifier(doc, value)
    if key == "name":
        return _matches_name(doc, value)
    if key == "gender":
        return doc.get("gender") == value
    if key == "birthdate":
        return doc.get("birthDate") == value
    if key == "status":
        return doc.get("status") == value
    if key == "code":
        raw = str(value)
        if "|" not in raw:
            want_system, want_code = "", raw
        else:
            want_system, _, want_code = raw.partition("|")
        codings = (doc.get("code") or {}).get("coding") or []
        return any((not want_system or c.get("system") == want_system)
                   and c.get("code") == want_code for c in codings)
    if key == "encounter":
        return (doc.get("encounter") or {}).get("reference") == value
    if key == "participant":
        return any((p.get("individual") or {}).get("reference") == value
                   for p in doc.get("participant") or [])
    if key == "date":
        eff = doc.get("effectiveDateTime")
        if not eff:
            return False
        if "/" in value:
            start, _, end = value.partition("/")
            return start <= eff <= end
        return eff[:len(value)] == value
    if key == "organization":
        if resource_type == "Location":
            return (doc.get("managingOrganization") or {}).get("reference") == value
        return False
    raise _BadParam(f"Unsupported search parameter: {key}")


FhirService.search = _search_impl
FhirService._param_match = _param_match

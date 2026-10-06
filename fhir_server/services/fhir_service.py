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
                   principal=None):
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
            out += rules_patient.validate_patient(payload,
                                                  is_create=existing is None)
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
            out += rules_observation.validate_observation(
                payload, org_id=org, device_ref=device_ref,
                assigned_patient=assigned)
        if existing is None:
            out += rules_common.check_references(payload, resource_type,
                                                 self._exists)
        return out

    @staticmethod
    def _raise(issues):
        status = 409 if any(i.code == "duplicate" for i in issues) else 400
        raise FhirError(issues, status)

    def _validated(self, principal, resource_type, payload, *, existing=None):
        issues, _ = parse.structural_issues(resource_type, payload)
        if not issues:
            issues = self._rule_sets(resource_type, payload, existing=existing,
                                     principal=principal)
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
            authz.check(principal, "update", resource_type, payload,
                        conn=self.conn)
        except AuthzError as exc:
            raise _as_fhir_error(exc) from exc
        doc = self._validated(principal, resource_type, payload, existing=existing)
        doc = dict(doc)
        doc["id"] = id_
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

"""Boards, test patients and capture sessions for the dashboard.

Spec: docs/design/specs/2026-11-18-board-sessions-and-navigation-design.md.
FHIR writes go through FhirService, so the normal validation rules apply.
"""
import re
import secrets
import sqlite3
from datetime import datetime, timezone

from .. import authz
from ..auth.jwt import Principal
from ..repositories import boards as boards_repo
from ..repositories import resources as res
from ..validation.issues import Issue
from .fhir_service import FhirError, FhirService

BOARD_ID = re.compile(r"[0-9A-F]{12}|SIM-[0-9A-F]{8}")
BOARD_KEY = re.compile(r"[0-9a-f]{64}")
LABEL = re.compile(r"[A-Za-z0-9-]{1,32}")
ADMIN = Principal(kind="admin")


def _err(status, text, code="value"):
    return FhirError([Issue(code=code, details_text=text)], status)


def _now():
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def _id(ref):
    return ref.split("/", 1)[1] if ref and "/" in ref else ref


def _name(doc):
    names = (doc or {}).get("name") or []
    return names[0].get("text") if names else None


def check_label(label):
    if not isinstance(label, str) or not LABEL.fullmatch(label):
        raise _err(400, "label must be 1 to 32 letters, digits or hyphens")


def make_test_patient(svc: FhirService, label):
    """Synthetic patient 'Sesi <label>' with a generated 9900... NIK."""
    check_label(label)
    for _ in range(10):
        nik = "9900" + "".join(secrets.choice("0123456789") for _ in range(12))
        try:
            _, patient, _ = svc.create(ADMIN, "Patient", {
                "resourceType": "Patient",
                "identifier": [{"use": "official",
                                "system": "https://fhir.kemkes.go.id/id/nik",
                                "value": nik}],
                "name": [{"use": "official", "text": f"Sesi {label}"}],
                "gender": "male", "birthDate": "1990-01-01",
                "multipleBirthBoolean": False,
                "address": [{
                    "use": "home", "line": ["Sesi capture"],
                    "city": "Jakarta Pusat", "postalCode": "10110",
                    "country": "ID",
                    "extension": [{
                        "url": "https://fhir.kemkes.go.id/r4/StructureDefinition/"
                               "administrativeCode",
                        "extension": [
                            {"url": "province", "valueCode": "31"},
                            {"url": "city", "valueCode": "3171"},
                            {"url": "district", "valueCode": "317101"},
                            {"url": "village", "valueCode": "317101001"},
                            {"url": "rt", "valueCode": "001"},
                            {"url": "rw", "valueCode": "001"}]}]}]})
            return patient
        except FhirError as exc:
            if exc.status != 409:
                raise
    raise _err(500, "could not allocate a unique synthetic NIK", "exception")


def open_visit(svc: FhirService, principal, patient_id, practitioner_ref, label):
    """An Encounter created as arrived and moved to in-progress. Returns its id."""
    org = (res.list(svc.conn, "Organization") or [None])[0]
    loc = (res.list(svc.conn, "Location") or [None])[0]
    if not org or not loc:
        raise _err(409, 'database not seeded: run "seed" first', "not-found")
    now = _now()
    enc_id, enc, _ = svc.create(principal, "Encounter", {
        "resourceType": "Encounter",
        "identifier": [{"use": "official",
                        "system": f"http://sys-ids.kemkes.go.id/encounter/{org['id']}",
                        "value": f"capture-{label}-{secrets.token_hex(4)}"}],
        "status": "arrived",
        "statusHistory": [{"status": "arrived", "period": {"start": now}}],
        "class": {"system": "http://terminology.hl7.org/CodeSystem/v3-ActCode",
                  "code": "AMB", "display": "ambulatory"},
        "subject": {"reference": f"Patient/{patient_id}"},
        "participant": [{"individual": {"reference": practitioner_ref}}],
        "period": {"start": now},
        "location": [{"location": {"reference": f"Location/{loc['id']}"}}],
        "serviceProvider": {"reference": f"Organization/{org['id']}"},
    })
    enc = dict(enc)
    enc["status"] = "in-progress"
    enc["statusHistory"] = list(enc["statusHistory"]) + [
        {"status": "in-progress", "period": {"start": now}}]
    svc.update(principal, "Encounter", enc_id, enc)
    return enc_id


def finish_visit(svc: FhirService, principal, encounter_id):
    enc = res.get(svc.conn, "Encounter", encounter_id)
    if not enc or enc.get("status") != "in-progress":
        return
    now = _now()
    enc = dict(enc)
    enc["status"] = "finished"
    enc["statusHistory"] = list(enc["statusHistory"]) + [
        {"status": "finished", "period": {"start": now, "end": now}}]
    enc["period"] = {**enc["period"], "end": now}
    svc.update(principal, "Encounter", encounter_id, enc)


class SessionService:
    def __init__(self, conn, settings):
        self.conn = conn
        self.fhir = FhirService(conn, settings)

    # --- who may do what (spec B7) ---
    @staticmethod
    def _staff(principal):
        if principal.kind not in ("admin", "doctor"):
            raise authz.AuthzError("Only admins and doctors may manage sessions")

    @staticmethod
    def _admin(principal, what):
        if principal.kind != "admin":
            raise authz.AuthzError(f"Only admins may {what}")

    # --- boards ---
    def register_board(self, principal, serial, key):
        self._admin(principal, "register boards")
        if not isinstance(serial, str) or not BOARD_ID.fullmatch(serial):
            raise _err(400, "id must be 12 upper-case hex digits or SIM- and 8")
        if not isinstance(key, str) or not BOARD_KEY.fullmatch(key):
            raise _err(400, "key must be 64 lower-case hex digits")
        known = boards_repo.get(self.conn, serial)
        if known:
            boards_repo.register(self.conn, serial, known["device_id"], key)
            return False, known["device_id"]
        simulated = serial.startswith("SIM-")
        dev_id, _, _ = self.fhir.create(ADMIN, "Device", {
            "resourceType": "Device", "status": "active",
            "identifier": [{"system": "urn:prata:board", "value": serial}],
            "serialNumber": serial, "manufacturer": "PRATA",
            "deviceName": [{"name": ("Simulated board " if simulated else
                                     "Radar board ") + serial,
                            "type": "user-friendly-name"}]})
        boards_repo.register(self.conn, serial, dev_id, key)
        return True, dev_id

    def list_boards(self, principal):
        self._staff(principal)
        out = []
        for b in boards_repo.list(self.conn):
            sess = boards_repo.open_session(self.conn, b["serial"])
            out.append({"id": b["serial"], "device": f"Device/{b['device_id']}",
                        "registered": b["registered"],
                        "session": self._view(sess) if sess else None})
        return out

    def board_session(self, key, serial):
        """The card the capture page needs, for the board holding `key`."""
        board = boards_repo.by_key(self.conn, key or "")
        if not board or board["serial"] != serial:
            raise FhirError([Issue(code="security", rule_number=20007,
                                   details_text="Unknown board or wrong key")], 401)
        sess = boards_repo.open_session(self.conn, serial)
        if not sess:
            raise _err(404, f"Board {serial} has no open session. Open one on"
                            " the Sessions page.", "not-found")
        org = (res.list(self.conn, "Organization") or [{}])[0].get("id", "")
        patient = res.get(self.conn, "Patient", _id(sess["patient_ref"]))
        return {"board": serial, "device": f"Device/{board['device_id']}",
                "patient": sess["patient_ref"], "patientName": _name(patient),
                "encounter": sess["encounter_ref"], "org": org,
                "label": sess["label"], "session": sess["id"]}

    # --- patients ---
    def create_test_patient(self, principal, label):
        self._admin(principal, "create test patients")
        p = make_test_patient(self.fhir, label)
        return {"patient": f"Patient/{p['id']}", "name": _name(p)}

    # --- sessions ---
    def _view(self, s):
        patient = res.get(self.conn, "Patient", _id(s["patient_ref"]))
        prac = res.get(self.conn, "Practitioner", _id(s["practitioner_ref"]))
        return {"id": s["id"], "label": s["label"], "board": s["serial"],
                "device": f"Device/{s['device_id']}", "patient": s["patient_ref"],
                "patientName": _name(patient), "encounter": s["encounter_ref"],
                "practitioner": s["practitioner_ref"],
                "practitionerName": _name(prac), "started": s["started"],
                "ended": s["ended"]}

    def list_sessions(self, principal, open_only=False):
        self._staff(principal)
        rows = boards_repo.sessions(self.conn, open_only=open_only)
        if principal.kind == "doctor":
            rows = [r for r in rows if r["practitioner_ref"] == principal.ref]
        return [self._view(r) for r in rows]

    def open_session(self, principal, serial, patient_ref, label, practitioner=None):
        self._staff(principal)
        check_label(label)
        board = boards_repo.get(self.conn, serial or "")
        if not board:
            raise _err(404, f"Board {serial} is not registered", "not-found")
        pid = _id(patient_ref or "")
        if not pid or not res.exists(self.conn, "Patient", pid):
            raise _err(404, f"Patient {patient_ref} not found", "not-found")
        if principal.kind == "doctor":
            if not authz.participates_in_patient(self.conn, principal.ref, pid):
                raise authz.AuthzError("Doctor is not a participant for this patient")
            prac_ref = principal.ref
        else:
            if practitioner:
                prac_ref = practitioner
            else:
                first = (res.list(self.conn, "Practitioner") or [None])[0]
                if not first:
                    raise _err(409, "no Practitioner exists", "not-found")
                prac_ref = f"Practitioner/{first['id']}"
            if not res.exists(self.conn, "Practitioner", _id(prac_ref)):
                raise _err(404, f"{prac_ref} not found", "not-found")
        if boards_repo.open_session(self.conn, serial):
            raise _err(409, f"Board {serial} already has an open session", "conflict")
        enc_id = open_visit(self.fhir, principal, pid, prac_ref, label)
        try:
            sid = boards_repo.start_session(
                self.conn, serial=serial, device_id=board["device_id"],
                patient_ref=f"Patient/{pid}", encounter_ref=f"Encounter/{enc_id}",
                practitioner_ref=prac_ref, label=label)
        except sqlite3.IntegrityError:
            finish_visit(self.fhir, ADMIN, enc_id)  # lost a race; close the visit
            raise _err(409, f"Board {serial} already has an open session",
                       "conflict") from None
        return self._view(boards_repo.get_session(self.conn, sid))

    def end_session(self, principal, session_id):
        self._staff(principal)
        s = boards_repo.get_session(self.conn, session_id)
        if not s:
            raise _err(404, "Session not found", "not-found")
        if principal.kind == "doctor" and s["practitioner_ref"] != principal.ref:
            raise authz.AuthzError("Doctors may end only their own sessions")
        if s["ended"]:
            raise _err(409, "Session already ended", "conflict")
        finish_visit(self.fhir, principal, _id(s["encounter_ref"]))
        boards_repo.end_session(self.conn, session_id)
        return self._view(boards_repo.get_session(self.conn, session_id))

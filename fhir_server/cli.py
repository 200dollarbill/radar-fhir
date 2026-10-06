import argparse
import json
import os
import secrets
import sys


def _load_dotenv():
    # isfile, not exists: the repo has a directory named .env/ (notes.env)
    if os.path.isfile(".env"):
        with open(".env") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    k, _, v = line.partition("=")
                    os.environ.setdefault(k.strip(), v.strip())


def _ensure_secret():
    if os.environ.get("FHIR_JWT_SECRET"):
        return
    secret = secrets.token_urlsafe(32)
    try:
        with open(".env", "a") as f:
            f.write(f"FHIR_JWT_SECRET={secret}\n")
    except OSError as exc:
        print(f"warning: could not persist FHIR_JWT_SECRET ({exc});"
              " this process only", file=sys.stderr)
    os.environ["FHIR_JWT_SECRET"] = secret


def cmd_init_db(args):
    from . import db as db_mod
    conn = db_mod.connect(args.db)
    db_mod.init(conn)
    print(f"initialized {args.db}")


def cmd_seed(args):
    from . import db as db_mod, ids
    from .auth.passwords import hash_password
    from .repositories import accounts, devices, resources

    if args.reset and os.path.exists(args.db):
        os.remove(args.db)
    conn = db_mod.connect(args.db)
    db_mod.init(conn)

    admin_password = os.environ.get("FHIR_ADMIN_PASSWORD") \
        or secrets.token_urlsafe(12)
    accounts.create(conn, "admin", hash_password(admin_password), "admin", None)

    org_id = "100000001"
    resources.put(conn, "Organization", org_id, {
        "resourceType": "Organization", "id": org_id,
        "name": os.environ.get("FHIR_ORG_NAME", "Klinik Demo"),
        "identifier": [{"use": "official",
                        "system": f"http://sys-ids.kemkes.go.id/organization/{org_id}",
                        "value": org_id}]})
    loc_id = "loc-poliklinik-1"
    resources.put(conn, "Location", loc_id, {
        "resourceType": "Location", "id": loc_id, "status": "active",
        "mode": "instance", "name": "Poli Jantung",
        "managingOrganization": {"reference": f"Organization/{org_id}"}})

    doc_id = "N10000000"
    resources.put(conn, "Practitioner", doc_id, {
        "resourceType": "Practitioner", "id": doc_id,
        "identifier": [{"system": "https://fhir.kemkes.go.id/id/nik",
                        "value": "3175061001900099"}],
        "name": [{"use": "official", "text": "drg. Contoh, Sp.JP",
                  "family": "Contoh", "given": ["Contoh"]}],
        "gender": "male", "birthDate": "1980-05-05"})
    doctor_password = os.environ.get("FHIR_DOCTOR_PASSWORD", "doctor-pw")
    accounts.create(conn, "doctor", hash_password(doctor_password), "doctor",
                    f"Practitioner/{doc_id}")

    pat_id = "P10000000001"
    resources.put(conn, "Patient", pat_id, {
        "resourceType": "Patient", "id": pat_id,
        "identifier": [
            {"use": "official", "system": "https://fhir.kemkes.go.id/id/nik",
             "value": "3175061001900001"},
            {"use": "official", "system": "https://fhir.kemkes.go.id/id/ihs-number",
             "value": pat_id}],
        "name": [{"use": "official", "text": "Budi Santoso",
                  "family": "Santoso", "given": ["Budi"]}],
        "gender": "male", "birthDate": "1990-02-14",
        "multipleBirthBoolean": False,
        "address": [{
            "use": "home", "line": ["Jl. Melati No. 1"],
            "city": "Jakarta Pusat", "postalCode": "10110", "country": "ID",
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
    patient_password = os.environ.get("FHIR_PATIENT_PASSWORD", "patient-pw")
    accounts.create(conn, "patient", hash_password(patient_password), "patient",
                    f"Patient/{pat_id}")

    dev_id = ids.mint("Device")
    resources.put(conn, "Device", dev_id, {
        "resourceType": "Device", "id": dev_id, "status": "active",
        "manufacturer": "PRATA",
        "deviceName": [{"name": "Radar JVP dummy", "type": "model-name"}]})
    device_token = secrets.token_urlsafe(32)
    devices.create_token(conn, dev_id, f"Patient/{pat_id}", device_token)

    # last stdout line must be the machine-readable summary
    print(json.dumps({
        "admin_password": admin_password,
        "doctor_password": doctor_password,
        "patient_password": patient_password,
        "device_token": device_token,
        "org_id": org_id, "location_id": loc_id,
        "practitioner_id": doc_id, "patient_id": pat_id, "device_id": dev_id,
    }))


def main(argv=None):
    _load_dotenv()
    _ensure_secret()
    parser = argparse.ArgumentParser(prog="fhir_server")
    parser.add_argument("--db",
                        default=os.environ.get("FHIR_DB_PATH", "fhir_server.db"))
    sub = parser.add_subparsers(dest="cmd", required=True)
    sub.add_parser("init-db").set_defaults(fn=cmd_init_db)
    seed = sub.add_parser("seed")
    seed.add_argument("--reset", action="store_true")
    seed.set_defaults(fn=cmd_seed)
    args = parser.parse_args(argv)
    args.fn(args)


if __name__ == "__main__":
    main()

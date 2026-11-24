import argparse
import getpass
import json
import os
import re
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
    doctor_password = os.environ.get("FHIR_DOCTOR_PASSWORD") \
        or secrets.token_urlsafe(12)
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
    patient_password = os.environ.get("FHIR_PATIENT_PASSWORD") \
        or secrets.token_urlsafe(12)
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


def cmd_capture_session(args):
    from . import db as db_mod
    from .auth.jwt import Principal
    from .config import Settings
    from .repositories import resources
    from .services.fhir_service import FhirError, FhirService
    from .services.sessions import make_test_patient, open_visit

    label = args.label
    if not re.fullmatch(r"[A-Za-z0-9-]{1,32}", label):
        print("invalid label: use 1-32 letters, digits or hyphens",
              file=sys.stderr)
        sys.exit(2)
    conn = db_mod.connect(args.db)
    db_mod.init(conn)
    first = {t: (resources.list(conn, t) or [None])[0]
             for t in ("Organization", "Location", "Practitioner", "Device")}
    if not all(first.values()):
        print('database not seeded: run "seed" first', file=sys.stderr)
        sys.exit(1)
    org, prac, dev = first["Organization"], first["Practitioner"], first["Device"]
    svc = FhirService(conn, Settings.from_env(db_path=args.db))
    admin = Principal(kind="admin")
    try:
        patient = make_test_patient(svc, label)
    except FhirError as exc:
        print(str(exc), file=sys.stderr)
        sys.exit(1)
    enc_id = open_visit(svc, admin, patient["id"], f"Practitioner/{prac['id']}",
                        label)
    token = svc.provision_device(admin, dev["id"], f"Patient/{patient['id']}")
    print(json.dumps({
        "token": token, "patient": f"Patient/{patient['id']}",
        "encounter": f"Encounter/{enc_id}", "device": f"Device/{dev['id']}",
        "org": org["id"], "label": label}))


def cmd_set_password(args):
    """Seed reads FHIR_ADMIN_PASSWORD only once; this changes a password later
    without wiping the database. The password comes from an environment
    variable so it never appears in the shell history or the output."""
    from . import db as db_mod
    from .auth.passwords import hash_password
    from .repositories import accounts

    password = os.environ.get(args.from_env)
    if not password:
        print(f"environment variable {args.from_env} is not set or empty",
              file=sys.stderr)
        sys.exit(2)
    conn = db_mod.connect(args.db)
    db_mod.init(conn)
    if not accounts.set_password(conn, args.username, hash_password(password)):
        print(f"no active account named {args.username}", file=sys.stderr)
        sys.exit(1)
    print(f"password updated for {args.username}")


USERNAME = re.compile(r"[A-Za-z0-9._-]{3,32}")


def _usage(message):
    print(message, file=sys.stderr)
    sys.exit(2)


def _new_password(from_env):
    """From an environment variable, or typed twice at a hidden prompt.
    Never from the command line, so it stays out of shell history."""
    if from_env:
        password = os.environ.get(from_env)
        if not password:
            _usage(f"environment variable {from_env} is not set or empty")
        return password
    password = getpass.getpass("Password: ")
    if getpass.getpass("Repeat password: ") != password:
        _usage("passwords do not match")
    if not password:
        _usage("empty password")
    return password


def cmd_add_account(args):
    from . import db as db_mod
    from .auth.passwords import hash_password
    from .config import Settings
    from .repositories import accounts, resources
    from .services.fhir_service import FhirError, FhirService
    from .services.sessions import make_test_practitioner

    if not USERNAME.fullmatch(args.username):
        _usage("invalid username: use 3 to 32 letters, digits, dots,"
               " underscores or hyphens")
    conn = db_mod.connect(args.db)
    db_mod.init(conn)
    if any(a["username"] == args.username for a in accounts.list_all(conn)):
        print(f"account {args.username} already exists", file=sys.stderr)
        sys.exit(1)
    needs = {"admin": set(), "doctor": {"name"}, "patient": {"ref"}}[args.role]
    for opt in ("name", "ref"):
        given = bool(getattr(args, opt))
        if opt in needs and not given:
            _usage(f"--role {args.role} needs --{opt}")
        if opt not in needs and given:
            _usage(f"--role {args.role} does not take --{opt}")
    ref = None
    if args.role == "patient":
        if not args.ref.startswith("Patient/"):
            _usage("--ref must be Patient/<id>")
        if not resources.get(conn, "Patient", args.ref.split("/", 1)[1]):
            print(f"no {args.ref}", file=sys.stderr)
            sys.exit(1)
        ref = args.ref
    password = _new_password(args.from_env)
    if args.role == "doctor":
        svc = FhirService(conn, Settings.from_env(db_path=args.db))
        try:
            ref = f"Practitioner/{make_test_practitioner(svc, args.name)['id']}"
        except FhirError as exc:
            print(str(exc), file=sys.stderr)
            sys.exit(1)
    accounts.create(conn, args.username, hash_password(password), args.role, ref)
    print(f"created {args.role} {args.username}" + (f" ({ref})" if ref else ""))


def cmd_list_accounts(args):
    from . import db as db_mod
    from .repositories import accounts
    conn = db_mod.connect(args.db)
    db_mod.init(conn)
    print("username\trole\tref\tactive")
    for a in accounts.list_all(conn):
        print("\t".join([a["username"], a["role"], a["subject_ref"] or "-",
                         "yes" if a["active"] else "no"]))


def cmd_disable_account(args):
    from . import db as db_mod
    from .repositories import accounts
    conn = db_mod.connect(args.db)
    db_mod.init(conn)
    if not accounts.set_active(conn, args.username, False):
        print(f"no account named {args.username}", file=sys.stderr)
        sys.exit(1)
    print(f"disabled {args.username}")


def cmd_serve(args):
    import uvicorn

    from .app import create_app
    from .config import Settings
    uvicorn.run(create_app(Settings.from_env(db_path=args.db)),
                host="127.0.0.1", port=args.port)


def main(argv=None):
    _load_dotenv()
    _ensure_secret()
    parser = argparse.ArgumentParser(prog="fhir_server")
    parser.add_argument("--db",
                        default=os.environ.get("FHIR_DB_PATH", "data/fhir_server.db"))
    sub = parser.add_subparsers(dest="cmd", required=True)
    sub.add_parser("init-db").set_defaults(fn=cmd_init_db)
    seed = sub.add_parser("seed")
    seed.add_argument("--reset", action="store_true")
    seed.set_defaults(fn=cmd_seed)
    cap = sub.add_parser("capture-session")
    cap.add_argument("--label", required=True)
    cap.set_defaults(fn=cmd_capture_session)
    pw = sub.add_parser("set-password")
    pw.add_argument("--username", required=True)
    pw.add_argument("--from-env", default="FHIR_ADMIN_PASSWORD",
                    help="environment variable holding the new password")
    pw.set_defaults(fn=cmd_set_password)
    add = sub.add_parser("add-account", help="create a login (admin, doctor, patient)")
    add.add_argument("--role", required=True, choices=["admin", "doctor", "patient"])
    add.add_argument("--username", required=True)
    add.add_argument("--name", help="doctor's display name (doctor only)")
    add.add_argument("--ref", help="Patient/<id> the login belongs to (patient only)")
    add.add_argument("--from-env", default=None,
                     help="environment variable holding the password"
                          " (default: ask twice at a hidden prompt)")
    add.set_defaults(fn=cmd_add_account)
    sub.add_parser("list-accounts").set_defaults(fn=cmd_list_accounts)
    dis = sub.add_parser("disable-account")
    dis.add_argument("--username", required=True)
    dis.set_defaults(fn=cmd_disable_account)
    serve = sub.add_parser("serve")
    serve.add_argument("--port", type=int, default=8000)
    serve.set_defaults(fn=cmd_serve)
    args = parser.parse_args(argv)
    args.fn(args)


if __name__ == "__main__":
    main()

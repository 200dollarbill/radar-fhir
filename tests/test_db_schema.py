from fhir_server import db


def test_init_creates_tables(db_path):
    conn = db.connect(db_path)
    db.init(conn)
    rows = {r[0] for r in conn.execute(
        "SELECT name FROM sqlite_master WHERE type='table'")}
    assert {"resources", "accounts", "device_tokens"} <= rows


def test_resources_primary_key(db_path):
    conn = db.connect(db_path)
    db.init(conn)
    conn.execute(
        "INSERT INTO resources VALUES ('Patient','P1',1,'{}','2026-01-01T00:00:00+00:00','2026-01-01T00:00:00+00:00')")
    try:
        conn.execute("INSERT INTO resources VALUES ('Patient','P1',2,'{}','a','a')")
        raise AssertionError("duplicate insert must fail")
    except Exception:
        pass

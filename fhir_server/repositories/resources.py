import datetime as dt
import json


def _now() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S+00:00")


def get(conn, type_, id_):
    row = conn.execute("SELECT json FROM resources WHERE type=? AND id=?",
                       (type_, id_)).fetchone()
    return json.loads(row["json"]) if row else None


def put(conn, type_, id_, doc) -> int:
    existing = conn.execute(
        "SELECT version FROM resources WHERE type=? AND id=?",
        (type_, id_)).fetchone()
    version = (existing["version"] + 1) if existing else 1
    now = _now()
    doc = dict(doc)
    doc["id"] = id_
    conn.execute(
        "INSERT INTO resources VALUES (?,?,?,?,?,?) "
        "ON CONFLICT(type,id) DO UPDATE SET json=excluded.json,"
        " version=excluded.version, updated=excluded.updated",
        (type_, id_, version, json.dumps(doc, separators=(",", ":")), now, now))
    conn.commit()
    return version


def get_version(conn, type_, id_):
    row = conn.execute("SELECT version FROM resources WHERE type=? AND id=?",
                       (type_, id_)).fetchone()
    return row["version"] if row else None


def delete(conn, type_, id_) -> bool:
    cur = conn.execute("DELETE FROM resources WHERE type=? AND id=?", (type_, id_))
    conn.commit()
    return cur.rowcount > 0


def list(conn, type_):
    return [json.loads(r["json"]) for r in
            conn.execute("SELECT json FROM resources WHERE type=?", (type_,))]


def exists(conn, type_, id_) -> bool:
    return conn.execute("SELECT 1 FROM resources WHERE type=? AND id=?",
                        (type_, id_)).fetchone() is not None

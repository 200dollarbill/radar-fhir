"""Registered radar boards and their capture sessions.

A board proves who it is with a key it made itself (spec B2); only the key's
SHA-256 is stored. A session ties one board to one patient's in-progress
Encounter; at most one session per board is open (unique index)."""
import datetime as dt
import hashlib
import uuid


def _now() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S+00:00")


def _sha(key: str) -> str:
    return hashlib.sha256(key.encode()).hexdigest()


def register(conn, serial, device_id, key) -> bool:
    """Create the board, or replace the key of a known one. True if created."""
    if get(conn, serial):
        conn.execute("UPDATE boards SET key_sha256=? WHERE serial=?",
                     (_sha(key), serial))
        conn.commit()
        return False
    conn.execute("INSERT INTO boards VALUES (?,?,?,?)",
                 (serial, device_id, _sha(key), _now()))
    conn.commit()
    return True


def get(conn, serial):
    row = conn.execute("SELECT * FROM boards WHERE serial=?", (serial,)).fetchone()
    return dict(row) if row else None


def by_key(conn, key):
    row = conn.execute("SELECT * FROM boards WHERE key_sha256=?",
                       (_sha(key),)).fetchone()
    return dict(row) if row else None


def list(conn):
    return [dict(r) for r in conn.execute("SELECT * FROM boards ORDER BY serial")]


def start_session(conn, *, serial, device_id, patient_ref, encounter_ref,
                  practitioner_ref, label) -> str:
    sid = str(uuid.uuid4())
    conn.execute(
        "INSERT INTO board_sessions VALUES (?,?,?,?,?,?,?,?,NULL)",
        (sid, serial, device_id, patient_ref, encounter_ref, practitioner_ref,
         label, _now()))
    conn.commit()
    return sid


def get_session(conn, session_id):
    row = conn.execute("SELECT * FROM board_sessions WHERE id=?",
                       (session_id,)).fetchone()
    return dict(row) if row else None


def open_session(conn, serial):
    row = conn.execute(
        "SELECT * FROM board_sessions WHERE serial=? AND ended IS NULL",
        (serial,)).fetchone()
    return dict(row) if row else None


def end_session(conn, session_id) -> bool:
    cur = conn.execute(
        "UPDATE board_sessions SET ended=? WHERE id=? AND ended IS NULL",
        (_now(), session_id))
    conn.commit()
    return cur.rowcount > 0


def sessions(conn, open_only=False):
    sql = "SELECT * FROM board_sessions"
    if open_only:
        sql += " WHERE ended IS NULL"
    return [dict(r) for r in conn.execute(sql + " ORDER BY started DESC, rowid DESC")]

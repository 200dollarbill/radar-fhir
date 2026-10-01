import datetime as dt
import hashlib
import uuid


def _now() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S+00:00")


def create_token(conn, device_id, patient_id, token_text) -> str:
    token_id = str(uuid.uuid4())
    sha = hashlib.sha256(token_text.encode()).hexdigest()
    conn.execute("INSERT INTO device_tokens VALUES (?,?,?,?,?,0)",
                 (token_id, device_id, patient_id, sha, _now()))
    conn.commit()
    return token_id


def resolve_token(conn, token_text):
    sha = hashlib.sha256(token_text.encode()).hexdigest()
    row = conn.execute(
        "SELECT * FROM device_tokens WHERE token_sha256=? AND revoked=0",
        (sha,)).fetchone()
    return dict(row) if row else None


def revoke(conn, token_id) -> bool:
    cur = conn.execute("UPDATE device_tokens SET revoked=1 WHERE id=?", (token_id,))
    conn.commit()
    return cur.rowcount > 0


def tokens_for_device(conn, device_id):
    return [dict(r) for r in conn.execute(
        "SELECT * FROM device_tokens WHERE device_id=?", (device_id,))]

import uuid


def create(conn, username, password_hash, role, subject_ref) -> str:
    account_id = str(uuid.uuid4())
    conn.execute("INSERT INTO accounts VALUES (?,?,?,?,?,1)",
                 (account_id, username, password_hash, role, subject_ref))
    conn.commit()
    return account_id


def get_by_username(conn, username):
    row = conn.execute("SELECT * FROM accounts WHERE username=? AND active=1",
                       (username,)).fetchone()
    return dict(row) if row else None


def get(conn, account_id):
    row = conn.execute("SELECT * FROM accounts WHERE id=? AND active=1",
                       (account_id,)).fetchone()
    return dict(row) if row else None


def list(conn):
    return [dict(r) for r in conn.execute(
        "SELECT * FROM accounts WHERE active=1")]


def set_password(conn, username, password_hash) -> bool:
    cur = conn.execute(
        "UPDATE accounts SET password_hash=? WHERE username=? AND active=1",
        (password_hash, username))
    conn.commit()
    return cur.rowcount > 0


def list_all(conn):
    """Every account, active or not, ordered by username."""
    return [dict(r) for r in conn.execute(
        "SELECT * FROM accounts ORDER BY username")]


def set_active(conn, username, active) -> bool:
    cur = conn.execute("UPDATE accounts SET active=? WHERE username=?",
                       (1 if active else 0, username))
    conn.commit()
    return cur.rowcount > 0

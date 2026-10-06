import sqlite3

SCHEMA = """
CREATE TABLE IF NOT EXISTS resources (
    type TEXT NOT NULL, id TEXT NOT NULL, version INTEGER NOT NULL,
    json TEXT NOT NULL, created TEXT NOT NULL, updated TEXT NOT NULL,
    PRIMARY KEY (type, id));
CREATE TABLE IF NOT EXISTS accounts (
    id TEXT PRIMARY KEY, username TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL, role TEXT NOT NULL,
    subject_ref TEXT, active INTEGER NOT NULL DEFAULT 1);
CREATE TABLE IF NOT EXISTS device_tokens (
    id TEXT PRIMARY KEY, device_id TEXT NOT NULL, patient_id TEXT NOT NULL,
    token_sha256 TEXT NOT NULL UNIQUE, created TEXT NOT NULL,
    revoked INTEGER NOT NULL DEFAULT 0);
"""


def connect(db_path: str) -> sqlite3.Connection:
    # One shared connection for the app's single event loop; FastAPI serves
    # routes on a different thread than create_app ran on, so pinning to the
    # creating thread would raise ProgrammingError.
    conn = sqlite3.connect(db_path, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init(conn: sqlite3.Connection) -> None:
    conn.executescript(SCHEMA)
    conn.commit()

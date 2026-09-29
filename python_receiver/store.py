"""Thread-safe bounded storage and receiver health counters."""
from __future__ import annotations
from collections import deque
from datetime import datetime, timezone
from threading import Lock
from typing import Any


class ObservationStore:
    def __init__(self, max_size: int = 1000):
        if max_size < 1:
            raise ValueError("max_size must be at least 1")
        self._items = deque(maxlen=max_size)
        self._lock = Lock()
        self._accepted = self._invalid = self._rejected_integrity = 0
        self._last_received: str | None = None
        self._serial_error: str | None = None

    def add(self, observation: dict[str, Any]) -> None:
        with self._lock:
            self._items.append(dict(observation))
            self._accepted += 1
            self._last_received = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")

    def record_invalid(self) -> None:
        with self._lock:
            self._invalid += 1

    def record_rejected_integrity(self) -> None:
        with self._lock:
            self._rejected_integrity += 1

    def record_serial_error(self, message: str) -> None:
        with self._lock:
            self._serial_error = message

    def recent(self, limit: int | None = None) -> list[dict[str, Any]]:
        with self._lock:
            items = list(self._items)
        if limit is not None:
            if limit < 0:
                raise ValueError("limit must not be negative")
            items = items[-limit:] if limit else []
        return [dict(item) for item in items]

    def latest(self) -> dict[str, Any] | None:
        items = self.recent(1)
        return items[0] if items else None

    def snapshot_health(self) -> dict[str, Any]:
        with self._lock:
            return {
                "accepted_packets": self._accepted,
                "invalid_packets": self._invalid,
                "rejected_integrity_packets": self._rejected_integrity,
                "stored_observations": len(self._items),
                "last_received_at": self._last_received,
                "serial_error": self._serial_error,
            }

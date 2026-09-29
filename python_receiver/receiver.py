"""Serial line ingestion for the dummy receiver."""
from __future__ import annotations
from datetime import datetime, timezone
import threading
from .models import PacketValidationError, RadarPacket
from .store import ObservationStore


class SerialReceiver:
    def __init__(self, port: str, baudrate: int, store: ObservationStore):
        self.port, self.baudrate, self.store = port, baudrate, store

    def process_line(self, line: str) -> bool:
        try:
            packet = RadarPacket.from_json_line(line)
            observation = packet.to_observation(datetime.now(timezone.utc))
        except PacketValidationError as exc:
            if "crc_ok is false" in str(exc):
                self.store.record_rejected_integrity()
            else:
                self.store.record_invalid()
            return False
        self.store.add(observation)
        return True

    def run(self, stop_event: threading.Event) -> None:
        try:
            import serial
            with serial.Serial(self.port, self.baudrate, timeout=1) as connection:
                self.store.record_serial_error("")
                while not stop_event.is_set():
                    raw = connection.readline()
                    if raw:
                        self.process_line(raw.decode("utf-8", errors="replace"))
        except Exception as exc:
            self.store.record_serial_error(str(exc))

"""Tiny localhost HTTP API for converted observations."""
from __future__ import annotations
import argparse
import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import threading
from .receiver import SerialReceiver
from .store import ObservationStore


def create_server(store: ObservationStore, host: str = "127.0.0.1", port: int = 8080) -> ThreadingHTTPServer:
    class Handler(BaseHTTPRequestHandler):
        def _send(self, status: int, payload: dict) -> None:
            body = json.dumps(payload, separators=(",", ":")).encode()
            self.send_response(status)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def do_GET(self) -> None:
            if self.path == "/health":
                self._send(200, store.snapshot_health())
            elif self.path == "/observations":
                self._send(200, {"resourceType": "Bundle", "type": "history",
                                 "entry": [{"resource": item} for item in store.recent()]})
            elif self.path == "/observations/latest":
                latest = store.latest()
                self._send(200, latest) if latest else self._send(404, {"error": "no observations"})
            else:
                self._send(404, {"error": "not found"})

        def log_message(self, format: str, *args: object) -> None:
            return

    return ThreadingHTTPServer((host, port), Handler)


def main() -> None:
    parser = argparse.ArgumentParser(description="Read radar JSON over USB and expose local observations")
    parser.add_argument("--serial-port", required=True)
    parser.add_argument("--baudrate", type=int, default=115200)
    parser.add_argument("--http-host", default="127.0.0.1")
    parser.add_argument("--http-port", type=int, default=8080)
    args = parser.parse_args()
    store = ObservationStore()
    stop = threading.Event()
    receiver = SerialReceiver(args.serial_port, args.baudrate, store)
    thread = threading.Thread(target=receiver.run, args=(stop,), daemon=True)
    thread.start()
    server = create_server(store, args.http_host, args.http_port)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        stop.set()
        server.shutdown()
        thread.join(timeout=2)
        server.server_close()


if __name__ == "__main__":
    main()

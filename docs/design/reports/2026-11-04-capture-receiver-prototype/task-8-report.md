# Task 8 report: capture page

Implemented: receiver/index.html, app.js (thin wiring), src/serial.js (serialLines with signal, TextDecoderStream, LineSplitter, reader.cancel on abort, port closed in finally), src/plot.js (Trace + draw), /capture static mount in fhir_server/app.py (after routers, html=True). IndexedDbStore only; no MemoryStore. Quota message adds "The unsaved partial chunk was lost." Capture.run rejection shown in error area. Stop aborts the AbortController passed to simulatorLines/serialLines (R3). Card kept in sessionStorage only (try/catch). Pending chunks at load are reported and upload starts when a card is used.

TDD RED: `.venv/bin/python -m pytest tests/test_routes.py -q -k capture` -> 2 failed (404 == 200); `node --test receiver/tests/plot.test.js` -> ERR_MODULE_NOT_FOUND plot.js. Expected, nothing existed.
GREEN: `.venv/bin/python -m pytest tests -q` -> 183 passed; `node --test "receiver/tests/*.test.js"` -> pass 80, fail 0. `node --check` passes on app.js, serial.js, plot.js.

Self-review: Trace scales each series separately to its own min/max (constant -> mid height); x spacing uses capacity so partial traces fill from the left. Added a fourth plot test (empty). Not browser-tested.
Concerns: app.js/serial.js/draw untested in a browser (later task). When a new card is pasted for a different session while capturing, the capture keeps its old card until restarted. Auth error message clears only on next error/useCard.

## Fix report (review findings)
1. serial.js: pipeTo promise kept (`piped`, errors caught); after reader.cancel() we `await piped` before port.close(), so the lock is released first.
2. New src/coalesce.js (`coalesce(fn, ms, {setTimer})`): at most one run per 250 ms, never two concurrent, calls during a run collapse into one later run. app.js routes every refresh (per-sample status, upload status, card, capture end) through scheduleRefresh = coalesce(refresh, 250).
Tests: receiver/tests/coalesce.test.js (2 tests: 100 calls -> one run; no overlap, one follow-up run). The serial fix is browser-only, not unit tested.
Command: `.venv/bin/python -m pytest tests -q` -> 183 passed; `node --test "receiver/tests/*.test.js"` -> pass 82, fail 0; node --check app.js/serial.js ok.

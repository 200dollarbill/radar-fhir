# Task 7 report
Implemented receiver/src/card.js (parseCard) and receiver/src/capture.js (Capture), tests in receiver/tests/card.test.js and capture.test.js. Commit c22bf64.

- parseCard: messages for empty, non-JSON, non-object, missing field (names it, e.g. "missing field token" for seed JSON), non-string, and Patient/Encounter/Device prefix. Returns only the six card keys.
- Capture.run: parseLine -> Chunker; chunks written via a sequential promise chain; onSample/onStatus(stats) per line; live gap stat mirrors the chunker (gap 1..999, same fs). Iterable throw -> flush, "disconnected". QuotaExceededError (by err.name) stops reading, no flush, returns "quota"; other store errors rethrow. Loop break calls the iterator's return. Chain awaited before resolve. New captureId per run.

TDD: RED `node --test "tests/*.test.js"` (in receiver/): ERR_MODULE_NOT_FOUND for card.js and capture.js (expected, files absent). GREEN from repo root `node --test "receiver/tests/*.test.js"`: pass 75, fail 0.
Note: run from inside receiver/, the pre-existing "FIELDS match radar_json.ino" test fails due to a cwd-relative path; unrelated, passes from root.

Self-review: no node: imports in src; gaps stat duplicates the chunker's gap rule (small coupling). Quota test uses DOMException (Node global).

## Fix report (review finding: bare catch)
Capture.run now drives the iterator manually. Only a throw from it.next() returns "disconnected". Errors from parseLine, Chunker, onSample or onStatus are caught, the partial chunk is flushed, the outbox chain awaited, the source closed via it.return(), then the error is rethrown so run() rejects. Added test "a throwing onSample rejects run() instead of reporting disconnected" (also checks the partial chunk was flushed); the iterable-throwing test still passes.
Command: node --test "receiver/tests/*.test.js" (repo root). Output: see below.
# pass 76
# fail 0

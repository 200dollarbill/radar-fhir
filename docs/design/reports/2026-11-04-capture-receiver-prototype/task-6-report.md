# Task 6 report
Commit: e646f8d feat(receiver): durable outbox and retrying uploader

## Implemented
- receiver/src/outbox.js: sessionKey, MemoryStore, IndexedDbStore (auto-increment key, navigator.storage.persist() once on open, refusal ignored), Outbox (async add/nextFor/remove/markRejected/counts). Rejected records stay in store with rejected=true and reason.
- receiver/src/uploader.js: Uploader with step/start/stop/resume. Delete only on 200/201. 401/403 set paused, keep records, step returns "auth" without sending until resume(card), which swaps card (token and sessionKey) and resets backoff. 5xx/fetch throw: retry, sleeps 1,2,4,8,16,30,30 s inside step, reset on success. Other 4xx: markRejected with first issue[].details.text, else "HTTP <status>". onStatus per R4: {state, confirmed, lastRejectedReason}.
## Tests
outbox.test.js (6) and uploader.test.js (11) added. Full suite: node --test "receiver/tests/*.test.js" -> 62 pass, 0 fail.
## TDD
RED: same command before implementing: ERR_MODULE_NOT_FOUND for receiver/src/outbox.js from both new test files (pass 44, fail 2), expected since modules absent.
GREEN: same command after: pass 62, fail 0.
## Files
receiver/src/outbox.js, receiver/src/uploader.js, receiver/tests/outbox.test.js, receiver/tests/uploader.test.js
## Self-review
Diff matches brief. Python suite not run (no Python changes). IndexedDbStore untested here (Task 9 manual check). Sleep happens inside step on retry; idle/auth polling sleep (500 ms) is only in start() loop.
## Concerns
Store methods are async-tolerant, so Outbox methods return promises (callers must await). Unexpected statuses (e.g. 3xx) are treated as rejected.

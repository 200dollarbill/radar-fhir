
# Final fix report (13 findings)

1. uploader.start loop wraps step in try/catch: reports state "error" via onStatus (guarded), backs off, continues. Tests: storage throw and throwing onStatus both recover.
2. app.js: new Trace per startCapture; SIMULATED banner set only when a capture starts, kept after Stop.
3. CLAUDE.md status and fhir_server/README.md verification line updated.
4. IndexedDbStore._tx rejects with tx.error ?? req.error ?? Error; capture.js coerces a falsy failure into an Error. Test: add() throwing null makes run() reject.
5. app.js opens the port inside startCapture's try ("Could not open serial port: <msg>"); serialLines now takes an opened port (contract documented), still closes it.
6. SERIAL_OPTIONS {baudRate:115200, bufferSize:65536}; draw coalesced to one per requestAnimationFrame.
7. Uploader.step snapshots this.card. Test added (note: it passed before as well, since the token was read synchronously; the snapshot is defensive).
8. Use card disabled while a capture runs.
9. 408 and 429 retry. Test added.
10. refresh() derives connection notes from uploader state: auth "Token invalid. Paste a new card."; retry "Server unreachable, retrying."; error "Local storage error while uploading, retrying."
11. Quota message: unsaved data (up to about 10 s) was lost.
12. autocomplete="off" on the card textarea (spellcheck already false).
13. Spec: command, status, three Known limits added.

Tests: first run of new tests showed 4 failures (capture null, 408/429, two loop tests); after fixes node --test "receiver/tests/*.test.js" = 87 pass, 0 fail; .venv/bin/python -m pytest tests -q = 184 passed. node --check app.js and src/serial.js OK.

Browser check (headless Chrome, scratch db and ports 8766/9334 in scratchpad/bc-final, processes cleaned): sim run, server killed 0.5 s in, after 16 s notes = "Server unreachable, retrying." with 1 pending; use-card disabled=true while running; after restart pending drained, notes empty; after Stop banner still visible, use-card re-enabled; second run fine. DB: 6 observations, 6 unique identifiers, no duplicates, chunks contiguous, 4188 + 199 samples all stored. Zero page exceptions; only console network-load logs for refused connections and favicon 404. Not verifiable headless: Web Serial (open options, bufferSize, open-error message), and Token invalid message (not exercised in browser; derived by same code path as retry).

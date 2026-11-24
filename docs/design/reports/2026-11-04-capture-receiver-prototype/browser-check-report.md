# Browser acceptance check (final run, run 3)

Scripts/data: /tmp/claude-1000/-mnt-Data-yep-Kuliah-Tugas-Semester-7-ntr-lagi-lulus-PRATA/21310f83-83c2-47de-92fe-98c8fec84819/scratchpad/browser-check (drive.mjs, verify.py, driver.log, errors.json, scratch.db, server.log). Chrome headless=new, CDP via Node 22, server on 127.0.0.1:8765, scratch DB, FHIR_JWT_SECRET via env. Earlier runs 1 and 2 are in run1/ and run2/ (driver script defects, not page bugs: run 1 tried to reload the tab while the server was down, so Chrome showed an error page; run 2 read status 40 ms after Use card, before the page refreshed).

## Steps
- A: seed, capture-session --label BROWSER1. Garbage in card box: error "The session card is not valid JSON.", no label set. Incomplete JSON: "Session card is missing field token." Valid card: "Using card: BROWSER1", no error. No observation exists that is not accounted for below, so nothing was uploaded by the garbage attempts. PASS
- B: simulator started; t=20 s server SIGKILLed; t=35 pending 2, confirmed 1; server restarted ~t=36; t=70 confirmed 6 pending 1; Stop; pending 0, confirmed 8, page samples 7024. PASS
- C: second simulator run, same card; t=15 s server killed; Stop; pending 1, samples 1507. Deviation: a tab cannot be reloaded while the server (which serves the page) is down, so the server was restarted, sessionStorage cleared (as a reopened tab would have it), then reload. After reload: "1 chunks are waiting from an earlier session. Paste a card to send them." Pasted card, Use card: confirmed 1, pending 0, notes cleared. PASS (with deviation)
- SIMULATED banner and plot: screenshot /tmp/claude-1000/-mnt-Data-yep-Kuliah-Tugas-Semester-7-ntr-lagi-lulus-PRATA/21310f83-83c2-47de-92fe-98c8fec84819/scratchpad/browser-check/sim-screenshot.png. Red SIMULATED banner visible, I/Q traces drawn as a sweeping plot, status line live. PASS. Other screenshots: sim-server-down.png, sim-late.png, after-reload.png.

## DB check (verify.py)
- Observations: 10, identifiers unique: 10 (no duplicates). All notes parse, source SIMULATED x10.
- Capture cap-b6f15673 (B): 8 chunks, indexes 0..7 contiguous, chunk sizes [1000 x7, 24], all 8 components equal length, max 1000. Samples 7024 = page 7024.
- Capture cap-0665c2e7 (C): 2 chunks, indexes 0..1, sizes [1000, 507], samples 1507 = page 1507.
- E tokens: 0. Gaps 0, rejected lines 0 on page.
PASS for all.

## Console
10 entries, all Chrome network "Failed to load resource": one favicon.ico 404, one ERR_CONNECTION_RESET and eight-ish ERR_CONNECTION_REFUSED to POST /fhir-r4/v1/Observation while the server was deliberately down. No uncaught exceptions, no module load errors, no app console.error. PASS

## Overall: PASS
Notes: Web Serial not tested (headless). Page does not show the pending-chunks note after reload when a card is still in sessionStorage (card auto-reused); only observed the note in the cleared-sessionStorage case.

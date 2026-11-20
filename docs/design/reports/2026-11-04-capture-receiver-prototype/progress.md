# SDD ledger — plan: docs/.superpowers/plans/2026-11-04-capture-receiver-prototype.md
Spec: docs/.superpowers/specs/2026-11-04-capture-receiver-prototype-design.md
Branch: feat/capture-receiver (from docs/cdss-topic-update @ 0bd32f0). Baseline 134 pytest pass.

Ruling: work in place on new branch feat/capture-receiver, no worktree — .venv stays usable and owner sees files in checkout; user said go without worktree preference — costs: no isolation; `git checkout` back undoes it.

## Preflight scan
| Pair / task | Produces vs consumes | Finding |
|---|---|---|
| T1 → T2 | raw rule; T2 tests post raw chunks | ok |
| T1 → T3 | card test posts raw chunk | ok |
| T2 → T8/T2 app.py | T2 capability edit, T8 mount, same file | ok, different regions |
| T2 → T9 | 201 then 200 | ok |
| T3 → T7 | card fields {token,patient,encounter,device,org,label} vs parseCard | ok |
| T4 → T5 | Sample shape | ok |
| T4 → T7/T8 | simulatorLines has no stop path, T7 says caller ends source | gap: R3 |
| T5 → T6/T7 | identifierValue, buildObservation | ok |
| T6 → T7/T8 | Uploader/Capture onStatus shape unspecified | gap: R4 |
| T8 → T6 | IndexedDbStore | ok |
| T9 → T4,T5 | expected tokens compare vs str_token | gap: R5 |
| T1 self | ok | |
| T2 self | ok | |
| T3 self | ok | |
| T4 self | `node --test receiver/tests/` fails on Node 22 | R1 |
| T5 self | ok | |
| T6 self | ok | |
| T7 self | ok | |
| T8 self | ok | |
| T9 self | fixture under receiver/tests/fixtures must not run as a test | R1 covers |
| All JS | .js ESM without package.json relies on syntax detection | R2 |

Ruling: R1 use `node --test "receiver/tests/*.test.js"` everywhere the plan says `node --test receiver/tests/` — verified the directory form fails on Node 22.23 and the glob works, also excludes fixtures — costs little if wrong.
Ruling: R2 add `receiver/package.json` {"private":true,"type":"module"} in Task 4, no dependencies — explicit ESM, not relying on detection — costs a harmless served file.
Ruling: R3 simulatorLines also takes `signal` (AbortSignal), ending when aborted; serialLines takes `signal` too, cancelling the reader — Stop needs a way to end the source; the plan left simulator without one — costs a parameter.
Ruling: R4 Uploader onStatus({state:"idle"|"sending"|"retry"|"auth", confirmed:number, lastRejectedReason:string|null}); Capture onStatus(stats) with stats {samples,gaps,rejected} — T8 needs stable shapes — costs a rename.
Ruling: R5 make_chunk.mjs `expected` holds exact token strings ("1.65","E"), compared directly, no str_token — JS and Python format floats differently, so string compare is the real contract — costs nothing.

Ruling: R6 subagents end commits with the attribution their own session reminder gives, not a fixed line — the trailer should name the model that wrote the commit; f49227b says Opus though Sonnet wrote it — costs one slightly wrong trailer, not rewritten.
Task 1: minor (deferred): redundant valueQuantity check; non-dict component elements assume dicts (structural parse runs first in _validated, so unreachable via service); component with extra value[x] not rejected; origin units not validated; has_obs_issue assertions broad.
Task 1: complete (commits 0bd32f0..f49227b, review clean)
Task 2: minor (deferred): create and key insert commit separately, a crash between duplicates on retry; If-None-Exist not URL-decoded; hit returns stored record without comparing body; `or 1` version fallback unneeded.
Task 2: complete (commits f49227b..45bc75d, review clean)
Task 3: minor (deferred): duplicate raw-chunk body in tests; unseeded run creates empty db file; address shape duplicated from seed; orphan Patient on mid-failure; test imports from sibling modules.
Task 3: complete (commits 45bc75d..3d3644e, review clean)
Task 4: minor (deferred): simulator noise not injectable; spin if custom sleep never advances; oversized line tail emitted as a fragment (harmless unless it starts with {).
Task 4: complete (commits 3d3644e..0997823, review clean)
Task 5: minor (deferred): rambling comments in chunker.test.js:174-176; fill-only chunk reports next sample's missed; MAX_FILL hard-coded vs configurable chunkSize. Warnings (validator acceptance, Sample shape) are confirmed by Task 9 e2e using real parser/builder/server.
Task 5: complete (commits 0997823..59518e4, review clean)
Task 6: minor (deferred): uploader start() loop has no catch, an IndexedDB error kills uploads silently (uploader.js:201-206); store.all() on every poll is quadratic on backlog; 408/429/3xx classed as rejected; _open() can double-open; resume during in-flight step mixes cards. Warnings: IndexedDbStore → Task 9 manual; quota stop → Task 7.
Task 6: complete (commits 59518e4..e646f8d, review clean)
Task 7: fix round 1/5 (1 addressed, 0 open; commits c22bf64..aace663)
Task 7: minor (deferred): on quota the partial chunk is dropped (reported as quota; UI should mention); card prefix tests only cover patient; no test that quota calls iterator return; gap rule duplicated from chunker; run() no longer accepts sync iterables; flush error could replace procError.
Task 7: complete (commits e646f8d..aace663, review clean)
Task 8: fix round 1/5 (2 addressed, 0 open; commits 54f8aba..e092b36)
Ruling: R7 coalesce.js added to receiver/src beyond plan's file list — the reviewer's throttle finding needed a testable helper — costs one small file.
Task 8: minor (deferred): serialLines lazy so port.open failure shows as Disconnected; app.js:134 reaches into outbox.store.all(); no-Web-Serial message cleared by next action; canvas aspect distortion; mount serves receiver/tests and package.json; coalesce fn throw is unhandled rejection; card pasted mid-capture applies to next capture; token-invalid message lingers.
Task 8: complete (commits aace663..e092b36, review clean)
Task 9: minor (deferred): make_chunk.mjs hard-codes identifier system; e2e imports fixtures from another test module; no assert on note/gap_samples.
Task 9: steps 1-5 complete (commits e092b36..d421d3f, review clean)
Task 9 step 6: browser check PASS in headless Chrome, simulator only: 10 Observations, 10 unique ids; B 7024 samples = page; C 1507 = page; 0 E tokens; no uncaught exceptions. Deviation: reload with server restarted first and sessionStorage cleared, since the server serves the page. Web Serial NOT tested. Report browser-check-report.md.
Task 9 step 7: hardware smoke NOT DONE — needs owner.
Final review: ready with fixes, findings in final-findings.md (fix wave). Other deferred minors triaged Defer by final reviewer.
Final fix wave: 13 addressed, 0 open (commit 6cce071). Re-review minors deferred: pipeTo setup before try in serial.js can leak an open port; startCapture constructors outside try; Connect not disabled while requestPort/open pending.

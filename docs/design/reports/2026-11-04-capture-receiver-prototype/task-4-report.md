# Task 4 report: line parsing and simulator

Commit: 0997823 feat(receiver): parse serial lines and simulate the device

## Implemented
- receiver/package.json (R2), receiver/src/jsonlines.js (parseLine, FIELDS, LineSplitter), receiver/src/simulator.js (simulatorLines, formatLine). No node: imports in src.
- parseLine mirrors python_receiver/models.py (ints, bool crc_ok, finite numbers) plus sample_idx >= 0, fs > 0; crc_ok:false rejected with reason "crc_ok is false"; non-"{" lines ignored.
- LineSplitter strips CRLF, buffers partials, emits and resets the buffer when more than 4096 chars arrive without a newline.
- simulatorLines({fs, now, sleep, signal}): each tick yields floor(elapsed*fs) - emitted lines; ends when signal aborts (R3); default sleep (20 ms) also wakes on abort. IMU fixed az=1.

## Tests
`node --test "receiver/tests/*.test.js"`: 22 pass, 0 fail (20 spec'd tests plus 2 abort tests).

## TDD
- RED: same command before src existed: ERR_MODULE_NOT_FOUND for receiver/src/jsonlines.js (expected, module absent).
- A first GREEN run had 1 failure in my own catch-up test (ticks=1 aborted during the first sleep, so 0 lines, not 250). Test harness error, fixed with ticks=2; implementation unchanged.
- GREEN: 22 tests, 22 pass.

## Files
receiver/package.json, receiver/src/{jsonlines,simulator}.js, receiver/tests/{jsonlines,simulator}.test.js

## Self-review
- Contract test reads arduino/radar_json/radar_json.ino and matches FIELDS (passes).
- Simulator output carries no SIMULATED marker; that belongs to the note/UI layer per global constraints.
- Simulated t_host_unix is 0.000 and epoch_id 0 (not used in Sample).

## Concerns
- Noise uses Math.random, so values are non-deterministic (bounds tested only).
- A stray sed warning about permissions appeared; the edit applied.

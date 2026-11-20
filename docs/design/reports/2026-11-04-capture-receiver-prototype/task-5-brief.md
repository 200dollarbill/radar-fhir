### Task 5: Chunker and Observation builder

**Files:**
- Create: `receiver/src/chunker.js`, `receiver/src/observation.js`
- Test: `receiver/tests/chunker.test.js`, `receiver/tests/observation.test.js`

**Interfaces:**
- Consumes: `Sample` from Task 4.
- Produces:
  - `class Chunker { constructor({chunkSize=1000, now=Date.now, onChunk}); addSample(sample); noteRejected(); flush() }`
  - `Chunk = {segment, chunkIndex, fs, startTimeMs, channels:{I,Q,ax,ay,az,gx,gy,gz}, gapSamples, rejectedLines, deviceMissed}`. Channel arrays hold numbers or `"E"`.
  - `identifierValue(captureId, chunk) -> string`, `<captureId>-<segment>-<chunkIndex>`
  - `buildObservation(chunk, card, {captureId, source}) -> object`. `source` is `"serial"` or `"SIMULATED"`.

- [ ] **Step 1: Write failing tests**

```js
// chunker.test.js
test("1000 samples emit one chunk; chunk 2 gets index 1")
test("gap of 3 fills 3 E in every channel and counts gapSamples 3")
test("gap crossing a chunk boundary: both chunks 1000 long, none lost")  // Review Focus 4
test("gap of 999 fills; gap of 1000 starts a new segment")
test("sample_idx going backwards flushes and starts segment+1, chunkIndex 0")  // Review Focus 4
test("repeated sample_idx starts a new segment")
test("fs change flushes and starts a new segment")
test("first sample at any index causes no gap")
test("flush emits a partial chunk; flush with nothing emits nothing")
test("noteRejected counts on the next emitted chunk, then resets")
test("rejected count survives an empty flush")
test("all channels have equal length in every emitted chunk")
test("deviceMissed is the latest sample's missed")
test("startTimeMs back-dates by leading gap entries")  // period × entries before the real sample

// observation.test.js
test("code, identifier, references and component order match the spec")
test("note parses to {source, gap_samples, rejected_lines, device_missed}")
test("period is 10 at fs 100 and 4 at fs 250")
test("data joins numbers and E with single spaces")
test("origin unit and UCUM code per channel: V, [g], deg/s")
test("effectiveDateTime has the form YYYY-MM-DDThh:mm:ss+00:00")
test("no category and no top-level value")
test("SIMULATED source appears in note")
```

- [ ] **Step 2: Run to verify failure**

Run: `node --test receiver/tests/`
Expected: FAIL with module not found for the new files.

- [ ] **Step 3: Implement.** With `gap = idx − lastIdx − 1`: `0` append, `1..999` fill then append, `>= 1000` new segment, negative or `idx == lastIdx` new segment. Spec D4: never read `epoch_id`. After each append, emit when the channel length reaches `chunkSize`, including during gap fill.

When a chunk's first entry is added, `startTimeMs = now() − (fill entries remaining before the current real sample) × (1000 / fs)`.

- [ ] **Step 4: Run to verify pass**

Run: `node --test receiver/tests/`
Expected: all pass.

- [ ] **Step 5: Commit**

```bash
git add receiver/src/chunker.js receiver/src/observation.js receiver/tests/
git commit -m "feat(receiver): group samples into chunks and build Observations"
```

---


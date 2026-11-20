### Task 4: Line parsing and simulator

**Files:**
- Create: `receiver/src/jsonlines.js`, `receiver/src/simulator.js`
- Test: `receiver/tests/jsonlines.test.js`, `receiver/tests/simulator.test.js`

**Interfaces:**
- Produces:
  - `parseLine(line: string) -> {kind:"ignored"} | {kind:"rejected", reason:string} | {kind:"sample", sample:Sample}`
  - `Sample = {sampleIdx, fs, missed, I, Q, ax, ay, az, gx, gy, gz}`, all numbers
  - `FIELDS`: the 14 serial field names
  - `class LineSplitter { push(text: string) -> string[] }`
  - `simulatorLines({fs=100, now=Date.now, sleep}) -> AsyncGenerator<string>`
  - `formatLine(sampleIdx, fs, values) -> string`

- [ ] **Step 1: Write failing tests**

```js
// jsonlines.test.js
test("valid firmware line gives a sample")
test("READY banner and ingest text are ignored, not rejected")
test("blank line is ignored")
test("broken {json is rejected")
test("missing field is rejected, naming it")
test("non-integer sample_idx or fs is rejected")
test("negative sample_idx and fs of 0 are rejected")
test("string I value is rejected")
test("crc_ok:false is rejected with reason crc_ok")
test("JSON array starting [ is ignored")  // does not start with {

// Contract: the firmware's printf keys equal FIELDS
test("FIELDS match radar_json.ino", () => {
  const ino = readFileSync("arduino/radar_json/radar_json.ino", "utf8");
  const keys = [...ino.matchAll(/\\"(\w+)\\":/g)].map(m => m[1]);
  assert.deepEqual(keys, FIELDS);
});

// LineSplitter, Review Focus 3
test("a line split across pushes comes out once, whole")
test("two lines in one push come out in order")
test("CRLF is stripped")
test("a partial line stays buffered")
test("a mid-line start parses as ignored")  // '":1.2,"Q":3}\n'
test("over 4096 chars without newline is emitted and the buffer resets")

// simulator.test.js
test("each line parses to a sample with consecutive sampleIdx")
test("I and Q stay inside 0 to 3.3 V")
test("emits elapsed×fs lines after a long sleep, catching up")  // fake clock
```

- [ ] **Step 2: Run to verify failure**

Run: `node --test receiver/tests/`
Expected: FAIL with module not found.

- [ ] **Step 3: Implement.** Field rules mirror `python_receiver/models.py` plus `sample_idx >= 0` and `fs > 0`. A trimmed line not starting with `{` is `ignored`.

Simulator signal, from the app's `SimRadar`: `I = 1.65 + 0.4·cos(phase + 0.6)`, `Q = 1.65 + 0.4·sin(phase + 0.6)`, phase = respiration sine + pulse + small noise. IMU values fixed at `az = 1`, others 0. Each tick, yield `floor(elapsed × fs) − emitted` lines so a throttled background tab catches up.

- [ ] **Step 4: Run to verify pass**

Run: `node --test receiver/tests/`
Expected: all pass. Run from the repo root, because the contract test reads a repo path.

- [ ] **Step 5: Commit**

```bash
git add receiver/src/jsonlines.js receiver/src/simulator.js receiver/tests/
git commit -m "feat(receiver): parse serial lines and simulate the device"
```

---


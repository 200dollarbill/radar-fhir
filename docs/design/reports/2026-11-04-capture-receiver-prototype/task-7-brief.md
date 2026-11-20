### Task 7: Session card and capture controller

**Files:**
- Create: `receiver/src/card.js`, `receiver/src/capture.js`
- Test: `receiver/tests/card.test.js`, `receiver/tests/capture.test.js`

**Interfaces:**
- Consumes: Tasks 4 to 6.
- Produces:
  - `parseCard(text: string) -> Card`, throwing `Error` with a user-readable message
  - `class Capture { constructor({outbox, sessionKey, card, source, onSample, onStatus, newId=() => "cap-"+crypto.randomUUID()}); async run(lines: AsyncIterable<string>) -> "ended"|"disconnected"|"quota"; stats -> {samples, gaps, rejected} }`

`Capture.run` feeds lines through `parseLine` and `Chunker`, and writes each chunk to the outbox through a sequential promise chain, so chunk order is kept.

- [ ] **Step 1: Write failing tests**

```js
// card.test.js, Review Focus 5
test("a valid card parses")
test("empty string gives a message saying to paste a card")
test("non-JSON text gives a message saying it is not valid JSON")
test("seed summary JSON is rejected, naming the missing field")
test("patient without the Patient/ prefix is rejected")

// capture.test.js
test("lines reach onSample and the outbox")
test("every chunk is in the outbox before run resolves")
test("ending the iterable flushes the partial chunk and returns ended")
test("the iterable throwing flushes and returns disconnected")
test("store quota error stops reading and returns quota")
test("each run has a new captureId")
test("stats count samples, gaps and rejected lines")
test("rejected line followed by the next index produces an E gap")
```

- [ ] **Step 2: Run to verify failure**

Run: `node --test receiver/tests/`
Expected: FAIL with module not found for the new files.

- [ ] **Step 3: Implement** to the signatures above. Stop is done by the caller ending the line source, so `Capture` has no separate stop path.

- [ ] **Step 4: Run to verify pass**

Run: `node --test receiver/tests/`
Expected: all pass.

- [ ] **Step 5: Commit**

```bash
git add receiver/src/card.js receiver/src/capture.js receiver/tests/
git commit -m "feat(receiver): session card parsing and capture controller"
```

---


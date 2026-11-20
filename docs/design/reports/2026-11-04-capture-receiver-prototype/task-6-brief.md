### Task 6: Outbox and uploader

**Files:**
- Create: `receiver/src/outbox.js`, `receiver/src/uploader.js`
- Test: `receiver/tests/outbox.test.js`, `receiver/tests/uploader.test.js`

**Interfaces:**
- Consumes: Observation and `identifierValue` from Task 5.
- Produces:
  - `sessionKey(card) -> string`, `"<patient>|<device>"`
  - Store interface: `put(record) -> id`, `update(record)`, `delete(id)`, `all() -> record[]` in id order. `class MemoryStore`, `class IndexedDbStore(dbName="prata-capture")`.
  - `class Outbox { constructor(store); add({identifier, sessionKey, observation}); nextFor(sessionKey) -> record|null; remove(id); markRejected(id, reason); counts(sessionKey) -> {pending, rejected, otherSession} }`
  - `class Uploader { constructor({outbox, fetchFn, card, sleep, onStatus, baseUrl="/fhir-r4/v1"}); step() -> "idle"|"sent"|"rejected"|"retry"|"auth"; start(); stop(); resume(card) }`

- [ ] **Step 1: Write failing tests** (`MemoryStore`, fake `fetchFn`, fake `sleep`)

```js
// outbox.test.js
test("nextFor returns the oldest pending record of that session")
test("records survive into a new Outbox on the same store")
test("markRejected keeps the record, excluded from nextFor, counted as rejected")
test("add rejects with QuotaExceededError when the store throws it")

// uploader.test.js
test("POST sends Authorization, If-None-Exist: identifier=<value>, fhir+json")
test("201 and 200 both delete the record")
test("record stays until the response arrives")  // inspect the store during fetch
test("fetch throwing keeps the record and returns retry")
test("500 keeps the record and returns retry")
test("backoff goes 1,2,4,8,16,30,30 s, and resets after success")
test("401 and 403 return auth, keep the record, and stop sending until resume")
test("400 marks rejected with OperationOutcome text and moves to next")
test("400 with a non-JSON body gives reason 'HTTP 400'")
test("chunks are sent oldest first, one at a time")
test("other session's chunks are skipped and counted")  // Review Focus 1
test("resume with their card sends them")  // Review Focus 1
```

- [ ] **Step 2: Run to verify failure**

Run: `node --test receiver/tests/`
Expected: FAIL with module not found for the new files.

- [ ] **Step 3: Implement.** The reason text is the first `issue[].details.text` in the OperationOutcome. `IndexedDbStore` is a thin wrapper with an auto-increment key, covered by the manual check in Task 9. It calls `navigator.storage.persist()` once on open and ignores a refusal.

- [ ] **Step 4: Run to verify pass**

Run: `node --test receiver/tests/`
Expected: all pass.

- [ ] **Step 5: Commit**

```bash
git add receiver/src/outbox.js receiver/src/uploader.js receiver/tests/
git commit -m "feat(receiver): durable outbox and retrying uploader"
```

---


### Task 8: The page

**Files:**
- Create: `receiver/index.html`, `receiver/app.js`, `receiver/src/serial.js`, `receiver/src/plot.js`
- Modify: `fhir_server/app.py`
- Test: `receiver/tests/plot.test.js`, `tests/test_routes.py`

**Interfaces:**
- Consumes: all receiver modules.
- Produces:
  - `/capture/` static route
  - `serialLines(port, {baudRate=115200}) -> AsyncGenerator<string>`
  - `class Trace { constructor(capacity=1000); push(i, q); points(width, height) -> {i:[x,y][], q:[x,y][]} }`, plus `draw(canvas, trace)`

- [ ] **Step 1: Write failing tests**

```python
# tests/test_routes.py
def test_capture_page_served(client):
    r = client.get("/capture/")
    assert r.status_code == 200 and "Raw signal" in r.text

def test_capture_module_has_js_mime(client):
    r = client.get("/capture/src/jsonlines.js")
    assert r.status_code == 200 and "javascript" in r.headers["content-type"]
```

```js
// plot.test.js
test("capacity keeps only the last 1000 points")
test("a constant signal gives finite y values")  // no divide by zero
test("points stay inside width and height")
```

- [ ] **Step 2: Run to verify failure**

Run: `.venv/bin/python -m pytest tests/test_routes.py -q -k capture ; node --test receiver/tests/plot.test.js`
Expected: `404` and module not found.

- [ ] **Step 3: Implement.**

`app.py`: mount `StaticFiles(directory=<repo>/receiver, html=True)` at `/capture`, after the routers.

`index.html` has:
- heading "Raw signal capture" and a fixed line: "Raw signal only. Not a measurement result or a clinical finding."
- card paste box and Use card button
- Connect serial, Start simulator and Stop buttons
- canvas
- status line showing samples received, chunks confirmed, chunks pending, gaps, rejected lines
- an error area, and a large SIMULATED banner while the simulator runs

`app.js` keeps the card in `sessionStorage` only, wrapped in try/catch, and connects:

| Condition | Message or action |
|---|---|
| `navigator.serial` missing | Disable Connect: "This browser has no Web Serial. Use Chrome or Edge." The simulator stays usable. |
| Run returned `disconnected` | "Disconnected. Click Connect to resume." No auto-reconnect |
| Run returned `quota` | "Browser storage is full. Capture stopped." |
| Uploader status `auth` | "Token invalid. Paste a new card." |
| Rejected chunks | Show count and latest reason |
| `otherSession > 0` | "N chunks belong to another session. Paste that session's card to send them." |
| Load with pending chunks | Report them and start uploading once a card is set |

`serial.js`: `port.open({baudRate})`, `TextDecoderStream`, `LineSplitter`. Stop calls `reader.cancel()`, and the port is closed in `finally`. A device-lost read error propagates to `Capture.run`.

- [ ] **Step 4: Run to verify pass**

Run: `.venv/bin/python -m pytest tests -q && node --test receiver/tests/`
Expected: all pass.

- [ ] **Step 5: Commit**

```bash
git add receiver/index.html receiver/app.js receiver/src/serial.js receiver/src/plot.js receiver/tests/plot.test.js fhir_server/app.py tests/test_routes.py
git commit -m "feat(receiver): capture page served at /capture"
```

---


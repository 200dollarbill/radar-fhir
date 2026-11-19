### Task 9: End-to-end test, docs and browser check

**Files:**
- Create: `receiver/tests/fixtures/make_chunk.mjs`, `tests/test_capture_e2e.py`
- Modify: `fhir_server/README.md`, `CLAUDE.md`

**Interfaces:**
- Consumes: everything above.
- Produces: `node receiver/tests/fixtures/make_chunk.mjs '<card JSON>'` prints `{"observation":..., "identifier":..., "expected":{"I":[...], ...}}`. Lines come from `formatLine`, go through the real parser, chunker and builder, and include one gap.

- [ ] **Step 1: Write the failing test**

```python
def test_chunk_round_trip(tmp_path):
    # seed and capture-session via CLI, make_chunk.mjs via subprocess
    r1 = post(obs, identifier); assert r1.status_code == 201
    r2 = post(obs, identifier); assert r2.status_code == 200
    assert r2.json()["id"] == r1.json()["id"]
    stored = client.get(f"/fhir-r4/v1/Observation/{r1.json()['id']}", headers=auth).json()
    for comp in stored["component"]:
        got = comp["valueSampledData"]["data"].split(" ")
        assert got == [str_token(v) for v in expected[channel(comp)]]
```

If `node` is missing, the test fails rather than skips, so a silent skip cannot hide the contract.

- [ ] **Step 2: Run to verify failure**

Run: `.venv/bin/python -m pytest tests/test_capture_e2e.py -q`
Expected: FAIL because the fixture script does not exist.

- [ ] **Step 3: Write the fixture.** Add a run guide section to `fhir_server/README.md`: `seed`, `capture-session`, `serve`, open `http://127.0.0.1:8000/capture/` in Chrome. In `CLAUDE.md`, update Status, add `receiver/` to the repo map and add the Node test command.

- [ ] **Step 4: Run all tests**

Run: `.venv/bin/python -m pytest tests -q && node --test receiver/tests/`
Expected: all pass.

- [ ] **Step 5: Commit**

```bash
git add receiver/tests/fixtures/make_chunk.mjs tests/test_capture_e2e.py fhir_server/README.md CLAUDE.md
git commit -m "test(receiver): chunk round trip through the real server, and run guide"
```

- [ ] **Step 6: Browser check with the simulator (spec Acceptance 2), in real Chrome**

Use a scratch database. Run the simulator for at least 60 s. Stop the server for about 15 s partway, while pending chunks grow, then restart it with the same database. Run a second capture, stop the server again, click Stop on the page, reload the tab with chunks pending, restart the server and paste the card again. Reload only after Stop: closing a tab mid-capture loses the unsaved partial chunk (up to 10 s), which is a known limit of this design.

Pass means:
- pending returns to 0 with no reload loop
- the Encounter's Observations hold every sample with sequential indexes
- no identifier appears twice
- the plot and SIMULATED banner are visible
- `note` says `SIMULATED`

Write the query as a small script in the scratchpad, and report the counts.

- [ ] **Step 7: Hardware smoke test (spec Acceptance 3), with the owner**

The owner connects the **spare blank board** with a data cable. Confirm which board it is before writing anything. Flash `arduino/radar_json/radar_json.ino` with `arduino-cli`, with `USB CDC On Boot` enabled. The owner clicks Connect and picks the port, since the picker needs a click.

Pass means lines reach the server as Observations. Report this as a data path check only, because the pins are placeholders and the values are not radar signal. If it cannot be run, report it as not done. Do not claim it passed.

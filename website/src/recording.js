// Load a saved recording into { fs, I, Q } for the review page and the evaluation.
// Two formats: the firmware CSV (as in data/rabits_*.csv) and a FHIR searchset
// Bundle of raw-capture Observations (as saved with the run guide's curl command).

export function parseCsv(text) {
  const rows = text.trim().split(/\r?\n/);
  const head = rows[0].split(",").map((h) => h.trim());
  const col = (name) => head.indexOf(name);
  const [ci, cq, cf] = [col("I"), col("Q"), col("fs")];
  if (ci < 0 || cq < 0) throw new Error("CSV needs I and Q columns");
  const I = [];
  const Q = [];
  let fs = 100;
  for (const row of rows.slice(1)) {
    const cells = row.split(",");
    if (cells.length < head.length) continue;
    I.push(Number(cells[ci]));
    Q.push(Number(cells[cq]));
    if (cf >= 0 && Number(cells[cf]) > 0) fs = Number(cells[cf]);
  }
  return { fs, I, Q };
}

const isRaw = (r) => r?.resourceType === "Observation"
  && (r.code?.coding ?? []).some((c) => c.code === "raw-capture");

const tokens = (data) => data.trim().split(/\s+/).map((t) => (/^[ELU]$/.test(t) ? NaN : Number(t)));

// identifier value is "<captureId>-<segment>-<chunk>"; captureId may itself hold hyphens.
function key(obs) {
  const parts = (obs.identifier?.[0]?.value ?? "").split("-");
  const chunk = Number(parts.pop());
  const segment = Number(parts.pop());
  return { capture: parts.join("-"), segment, chunk, time: obs.effectiveDateTime ?? "" };
}

export function parseBundle(bundle) {
  const obs = (bundle.entry ?? []).map((e) => e.resource).filter(isRaw);
  if (obs.length === 0) throw new Error("Bundle has no raw-capture Observations");
  const keyed = obs.map((o) => ({ o, k: key(o) }));
  const firstTime = new Map();
  for (const { k } of keyed) {
    const t = firstTime.get(k.capture);
    if (t === undefined || k.time < t) firstTime.set(k.capture, k.time);
  }
  keyed.sort((a, b) =>
    (firstTime.get(a.k.capture) < firstTime.get(b.k.capture) ? -1 : firstTime.get(a.k.capture) > firstTime.get(b.k.capture) ? 1 : 0)
    || (a.k.capture < b.k.capture ? -1 : a.k.capture > b.k.capture ? 1 : 0)
    || a.k.segment - b.k.segment
    || a.k.chunk - b.k.chunk);
  const I = [];
  const Q = [];
  let fs = 100;
  for (const { o } of keyed) {
    const comp = (code) => o.component.find((c) => c.code.coding.some((x) => x.code === code));
    const ci = comp("i-voltage");
    const cq = comp("q-voltage");
    I.push(...tokens(ci.valueSampledData.data));
    Q.push(...tokens(cq.valueSampledData.data));
    fs = 1000 / ci.valueSampledData.period;
  }
  return { fs, I, Q };
}

export function parseRecording(text) {
  return text.trimStart().startsWith("{") ? parseBundle(JSON.parse(text)) : parseCsv(text);
}

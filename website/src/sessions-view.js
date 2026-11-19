// Pure helpers for the Sessions page.

const resources = (bundle) => (bundle?.entry ?? []).map((e) => e.resource).filter(Boolean);
const nameOf = (r) => (r.name ?? [])[0]?.text ?? null;

export function patientOptions(bundle) {
  return resources(bundle)
    .map((p) => ({ value: `Patient/${p.id}`, label: `${nameOf(p) ?? "(no name)"} · ${p.id}`, sort: nameOf(p) ?? "" }))
    .sort((a, b) => a.sort.localeCompare(b.sort) || a.value.localeCompare(b.value))
    .map(({ value, label }) => ({ value, label }));
}

export function practitionerOptions(bundle) {
  return resources(bundle).map((p) => ({ value: `Practitioner/${p.id}`, label: nameOf(p) ?? p.id }));
}

export function freeBoards(boards) {
  return boards.filter((b) => !b.session);
}

export function fmtTime(iso) {
  if (!iso) return "—";
  const d = new Date(iso);
  return Number.isNaN(d.getTime()) ? iso : d.toLocaleString(undefined, { dateStyle: "medium", timeStyle: "short" });
}

export async function apiError(res) {
  try {
    const oo = JSON.parse(await res.text());
    const text = (oo.issue ?? []).map((i) => i?.details?.text).find((t) => typeof t === "string" && t);
    if (text) return text;
  } catch { /* not an OperationOutcome */ }
  return `HTTP ${res.status}`;
}

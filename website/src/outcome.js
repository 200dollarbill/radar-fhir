// The text a person should see for a failed API answer: the server's own
// OperationOutcome message, or the bare status when the body has none.

export async function apiError(res) {
  try {
    const oo = JSON.parse(await res.text());
    const text = (oo.issue ?? []).map((i) => i?.details?.text).find((t) => typeof t === "string" && t);
    if (text) return text;
  } catch { /* not an OperationOutcome */ }
  return `HTTP ${res.status}`;
}

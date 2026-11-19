// Parse the session card printed by the server's capture-session command.

const REQUIRED = ["token", "patient", "encounter", "device", "org", "label"];
const PREFIXES = { patient: "Patient/", encounter: "Encounter/", device: "Device/" };

export function parseCard(text) {
  if (typeof text !== "string" || text.trim() === "") {
    throw new Error("Paste the session card printed by the server first.");
  }
  let card;
  try {
    card = JSON.parse(text);
  } catch {
    throw new Error("The session card is not valid JSON.");
  }
  if (card === null || typeof card !== "object" || Array.isArray(card)) {
    throw new Error("The session card must be a JSON object.");
  }
  for (const f of REQUIRED) {
    if (!(f in card)) throw new Error(`Session card is missing field ${f}.`);
    if (typeof card[f] !== "string" || card[f] === "") {
      throw new Error(`Session card field ${f} must be a non-empty string.`);
    }
  }
  for (const [f, prefix] of Object.entries(PREFIXES)) {
    if (!card[f].startsWith(prefix) || card[f].length === prefix.length) {
      throw new Error(`Session card field ${f} must start with ${prefix}`);
    }
  }
  const { token, patient, encounter, device, org, label } = card;
  return { token, patient, encounter, device, org, label };
}

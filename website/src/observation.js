// Build the FHIR R4 raw-capture Observation for one chunk.
// Numbers use JavaScript number-to-string; "E" marks a filled gap.

const SYSTEM = "urn:prata:radar-signal";
const UCUM = "http://unitsofmeasure.org";

const COMPONENTS = [
  ["I", "i-voltage", "V"], ["Q", "q-voltage", "V"],
  ["ax", "accel-x", "[g]"], ["ay", "accel-y", "[g]"], ["az", "accel-z", "[g]"],
  ["gx", "gyro-x", "deg/s"], ["gy", "gyro-y", "deg/s"], ["gz", "gyro-z", "deg/s"],
];

export function identifierValue(captureId, chunk) {
  return `${captureId}-${chunk.segment}-${chunk.chunkIndex}`;
}

function isoSeconds(ms) {
  return new Date(Math.floor(ms / 1000) * 1000).toISOString().replace(/\.\d+Z$/, "+00:00");
}

export function buildObservation(chunk, card, { captureId, source }) {
  const period = 1000 / chunk.fs;
  return {
    resourceType: "Observation",
    status: "final",
    identifier: [{
      system: `http://sys-ids.kemkes.go.id/organization/${card.org}`,
      value: identifierValue(captureId, chunk),
    }],
    code: { coding: [{ system: SYSTEM, code: "raw-capture", display: "Raw radar I/Q capture" }] },
    subject: { reference: card.patient },
    encounter: { reference: card.encounter },
    device: { reference: card.device },
    effectiveDateTime: isoSeconds(chunk.startTimeMs),
    note: [{
      text: JSON.stringify({
        source,
        gap_samples: chunk.gapSamples,
        rejected_lines: chunk.rejectedLines,
        device_missed: chunk.deviceMissed,
      }),
    }],
    component: COMPONENTS.map(([ch, code, unit]) => ({
      code: { coding: [{ system: SYSTEM, code }] },
      valueSampledData: {
        origin: { value: 0, unit, system: UCUM, code: unit },
        period,
        dimensions: 1,
        data: chunk.channels[ch].map(String).join(" "),
      },
    })),
  };
}

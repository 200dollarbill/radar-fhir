// One line under the waveform saying which method ran and why.
import { GUARD } from "./demod.js";

const SIGN = " The sign of the waveform is arbitrary for this method.";

function whyNotCircle(c) {
  if (!c || !c.ok || !(c.r > 0)) return "the circle fit failed";
  const spread = Math.round((100 * c.residualSd) / c.r);
  if (c.residualSd >= GUARD.maxResidualFrac * c.r) {
    return `the I/Q points are not on a circle (spread ${spread} % of radius, limit ${Math.round(100 * GUARD.maxResidualFrac)} %)`;
  }
  return `the arc of ${Math.round(c.spanDeg)}° is under ${GUARD.minSpanDeg}°`;
}

export function describeInfo(info, method) {
  if (info.reason === "too-short") return "Waiting for 2 s of samples.";
  if (info.flat) return "No movement in this window (I and Q are flat). Check the radar wiring and aim.";
  if (method === "hybrid" && info.used === "pca") {
    return `hybrid used linear projection, because ${whyNotCircle(info.circle)}.${SIGN}`;
  }
  if (method === "hybrid") return `hybrid used arctangent around the fitted circle (arc ${Math.round(info.circle.spanDeg)}°).`;
  return `${method}.` + (method === "single" || method === "pca" ? SIGN : "");
}

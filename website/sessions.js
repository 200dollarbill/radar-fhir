// Sessions page wiring. Logic lives in src/.
import { login, saveAuth, loadAuth, clearAuth, authHeaders } from "./src/auth.js";
import { renderNav } from "./src/nav.js";
import { patientOptions, practitionerOptions, freeBoards, fmtTime, apiError } from "./src/sessions-view.js";

const $ = (id) => document.getElementById(id);
const auth = () => loadAuth(localStorage);

function nav() {
  renderNav($("topnav"), { path: location.pathname, auth: auth(), onLogout: logout });
}

function logout(message = "") {
  clearAuth(localStorage);
  nav();
  show();
  $("login-error").textContent = message;
}

window.addEventListener("storage", () => { nav(); show(); });

// fetch with the login; an expired or refused login sends the user back to the form.
async function api(path, init = {}) {
  const a = auth();
  if (!a) { logout("Logged out: session expired."); throw new Error("logged out"); }
  const res = await fetch(path, {
    ...init,
    headers: { ...authHeaders(a), ...(init.body ? { "Content-Type": "application/json" } : {}), ...(init.headers ?? {}) },
  });
  if (res.status === 401) { logout("Logged out: session expired."); throw new Error("logged out"); }
  return res;
}

function fill(select, options, empty) {
  select.replaceChildren();
  if (options.length === 0) {
    const o = document.createElement("option");
    o.value = "";
    o.textContent = empty;
    select.append(o);
    select.disabled = true;
    return;
  }
  select.disabled = false;
  for (const { value, label } of options) {
    const o = document.createElement("option");
    o.value = value;
    o.textContent = label;
    select.append(o);
  }
}

function cell(tr, text, cls) {
  const td = document.createElement("td");
  td.textContent = text;
  if (cls) td.className = cls;
  tr.append(td);
  return td;
}

function endButton(session) {
  const b = document.createElement("button");
  b.className = "danger";
  b.textContent = "End";
  b.addEventListener("click", async () => {
    if (b.dataset.armed !== "1") { // two clicks instead of a blocking dialog
      b.dataset.armed = "1";
      b.textContent = "Confirm end";
      setTimeout(() => { b.dataset.armed = ""; b.textContent = "End"; }, 4000);
      return;
    }
    b.disabled = true;
    const res = await api(`/api/sessions/${encodeURIComponent(session.id)}/end`, { method: "POST" });
    if (!res.ok) $("error").textContent = `Could not end ${session.label}: ${await apiError(res)}`;
    await load();
  });
  return b;
}

async function load() {
  $("error").textContent = "";
  const a = auth();
  const admin = a.role === "admin";
  try {
    const [sessionsRes, boardsRes, patientsRes, pracRes] = await Promise.all([
      api("/api/sessions"),
      api("/api/boards"),
      api("/fhir-r4/v1/Patient?_count=100"),
      admin ? api("/fhir-r4/v1/Practitioner?_count=100") : Promise.resolve(null),
    ]);
    for (const r of [sessionsRes, boardsRes, patientsRes, pracRes]) {
      if (r && !r.ok) throw new Error(await apiError(r));
    }
    const sessions = await sessionsRes.json();
    const boards = await boardsRes.json();
    const patients = patientOptions(await patientsRes.json());

    const open = sessions.filter((s) => !s.ended);
    const ended = sessions.filter((s) => s.ended);
    $("open-rows").replaceChildren(...open.map((s) => {
      const tr = document.createElement("tr");
      cell(tr, s.label);
      cell(tr, s.patientName ?? s.patient);
      cell(tr, s.board, "mono");
      cell(tr, s.practitionerName ?? s.practitioner);
      cell(tr, fmtTime(s.started));
      cell(tr, "").append(endButton(s));
      return tr;
    }));
    $("open-empty").hidden = open.length > 0;
    $("ended-rows").replaceChildren(...ended.slice(0, 20).map((s) => {
      const tr = document.createElement("tr");
      cell(tr, s.label);
      cell(tr, s.patientName ?? s.patient);
      cell(tr, s.board, "mono");
      cell(tr, s.practitionerName ?? s.practitioner);
      cell(tr, fmtTime(s.started));
      cell(tr, fmtTime(s.ended));
      return tr;
    }));
    $("ended-empty").hidden = ended.length > 0;

    $("board-rows").replaceChildren(...boards.map((b) => {
      const tr = document.createElement("tr");
      cell(tr, b.id, "mono");
      cell(tr, b.id.startsWith("SIM-") ? "Simulated" : "Radar board");
      cell(tr, fmtTime(b.registered));
      cell(tr, b.session ? `${b.session.label} · ${b.session.patientName ?? b.session.patient}` : "Free");
      return tr;
    }));
    $("boards-empty").hidden = boards.length > 0;

    fill($("patient"), patients, admin ? "No patients: create a test patient" : "No patients you take part in");
    fill($("board"), freeBoards(boards).map((b) => ({ value: b.id, label: b.id })), "No free board");
    if (admin && pracRes) fill($("doctor"), practitionerOptions(await pracRes.json()), "No doctors");
  } catch (e) {
    if (e.message !== "logged out") $("error").textContent = `Could not load: ${e.message}`;
  }
}

function show() {
  const a = auth();
  const staff = a && (a.role === "admin" || a.role === "doctor");
  $("login-panel").hidden = !!a;
  $("not-staff").hidden = !a || staff;
  $("dashboard").hidden = !staff;
  if (!staff) return;
  $("patients-panel").hidden = a.role !== "admin";
  $("doctor-field").hidden = a.role !== "admin";
  load();
}

$("login-form").addEventListener("submit", async (ev) => {
  ev.preventDefault();
  $("login-error").textContent = "";
  try {
    saveAuth(localStorage, await login((...x) => fetch(...x), $("username").value, $("password").value));
    $("password").value = "";
    nav();
    show();
  } catch (e) {
    $("login-error").textContent = e.message;
  }
});

$("session-form").addEventListener("submit", async (ev) => {
  ev.preventDefault();
  $("session-msg").textContent = "";
  const body = { board: $("board").value, patient: $("patient").value, label: $("label").value };
  if (auth()?.role === "admin" && $("doctor").value) body.practitioner = $("doctor").value;
  const res = await api("/api/sessions", { method: "POST", body: JSON.stringify(body) });
  if (!res.ok) { $("session-msg").textContent = `Not opened: ${await apiError(res)}`; return; }
  const s = await res.json();
  $("session-msg").textContent = `Opened ${s.label} on board ${s.board}. On the Capture page, click Check again or connect the board.`;
  $("label").value = "";
  await load();
});

$("patient-form").addEventListener("submit", async (ev) => {
  ev.preventDefault();
  const res = await api("/api/patients", { method: "POST", body: JSON.stringify({ label: $("patient-label").value }) });
  if (!res.ok) { $("patient-msg").textContent = `Not created: ${await apiError(res)}`; return; }
  const p = await res.json();
  $("patient-msg").textContent = `Created ${p.name} (${p.patient}).`;
  $("patient-label").value = "";
  await load();
  $("patient").value = p.patient;
});

nav();
show();

window.prataLoaded = true;

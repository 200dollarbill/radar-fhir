# PRATA: proposal-planning brief

This guide compiles the project's goals, the work already completed, and the
methodological basis you can draw on when writing your own proposal. It is a
briefing source, not the proposal itself: formulate the research question,
contribution, evaluation plan, and institutional framing in your own terms.

**Project shorthand:** Pra-TA radar-based cardiac monitoring, wrapped in a
local, SATUSEHAT-compatible FHIR R4 clinical-record server.

## 1. Project goal and intended contribution

The project is developing a **standalone, locally operated FHIR R4 server** for
a device-assisted clinical workflow in Indonesian healthcare. The long-range
goal has three connected parts:

1. **Device-to-clinic data path:** a radar-derived vital sign—initially heart
   rate / carotid pulse—can enter a FHIR record as a device-sourced
   `Observation`.
2. **Clinician review:** a doctor opens an `Encounter`, receives measurements
   associated with that patient and visit, and can read them in context.
3. **Patient access:** the patient can read their own record through a
   role-scoped API (a web UI is a later phase).

The differentiating standards contribution is not merely to serialize sensor
values as JSON. It is to define the **resource semantics, terminology, profile
constraints, provenance/device identity, and access boundaries** that make a
new measurement device interoperable with a FHIR-based clinical workflow.

**Important claim boundary:** the current server is a walking skeleton and
research prototype. It is SATUSEHAT-compatible in selected profiles,
identifiers, terminology, and OperationOutcome conventions; it is not a
certified SATUSEHAT implementation, a production medical device, a validated
clinical decision-support system, or a substitute for clinical validation.

## 2. SATUSEHAT and FHIR: relationship and scope

### FHIR R4 is the technical base

FHIR (Fast Healthcare Interoperability Resources) R4, version **4.0.1**, defines
the resource shapes and REST interactions. The project uses FHIR resources to
represent identity, facilities, visits, devices, and observations:

- `Patient`: subject of care and patient identifiers.
- `Practitioner`: clinician identity.
- `Organization` and `Location`: facility and care location.
- `Device`: the measuring instrument.
- `Encounter`: the visit that gives a reading clinical context.
- `Observation`: a time-stamped measurement, initially heart rate.
- `OperationOutcome`: machine-readable validation and request errors.
- Future conformance artifacts: `StructureDefinition`, `ValueSet`, `CodeSystem`,
  and `ImplementationGuide`.

The server declares `fhirVersion: 4.0.1`. Do not use the R6 CI build at
`build.fhir.org` as an authority for resource rules; the binding base is R4 at
`hl7.org/fhir/R4/`.

### SATUSEHAT supplies national compatibility constraints

SATUSEHAT is Indonesia's national health-data exchange platform and publishes
FHIR-shaped profiles, identifiers, terminology choices, API conventions, and
use-case guidance. The project uses those materials as compatibility inputs:

- Indonesian patient identifiers (NIK, IHS number, and related systems).
- Kementerian Kesehatan `sys-ids` patterns for facility-scoped identifiers.
- LOINC and UCUM choices for vital-sign observations and units.
- SATUSEHAT `wajib` (= mandatory) markers and use-case requirements.
- SATUSEHAT-style `OperationOutcome` responses with `RuleNumber` messages.

**Local-only boundary:** this project does **not** call the hosted SATUSEHAT
platform. No production/sandbox credentials, registration, API-key exchange,
Postman workflow, or outbound clinical-data transmission to Kemenkes is in
scope. “SATUSEHAT-compatible” means following selected published shapes and
terminology while serving data locally.

### Evidence and conflict handling

The reference compilation separates primary scraped evidence from the authored
reference views:

```text
docs/reference/raw/       upstream snapshots; never hand-edit
docs/reference/claude/    dense, traceable technical summaries
docs/reference/human/     readable guides for proposal/project writing
```

Start with `docs/reference/claude/INDEX.md`; it maps questions to the relevant
technical summary. Every summary ends with `## Sources` pointing back to its
raw evidence. The project also has a claim-by-claim validity review:

- `docs/reference/claude/VALIDITY-REVIEW.md`
- `docs/reference/claude/VALIDITY-REVIEW-claims.md`

The review found confirmed rules, SATUSEHAT-specific tightenings, R4 conflicts,
unverifiable claims, and systemic contradictions. A proposal should describe
the **ruling method**, not present contradictory source statements as settled
facts: trace claim → authored view → raw source; compare to normative R4; record
the chosen implementation rule and its rationale. Examples affecting design:

| Topic | Evidence conflict / gap | Project ruling or handling |
|---|---|---|
| FHIR version | SATUSEHAT pages imply R4; `build.fhir.org` is R6 CI | R4 4.0.1 is binding |
| Content-Type | playbook says `application/json`; R4 says FHIR JSON media type | accept both on input; emit `application/fhir+json` |
| Blood pressure | SATUSEHAT uses separate systolic/diastolic Observations; R4 vital-sign profile uses a panel | future storage/export mapping must be explicit |
| Encounter location | playbook examples flatten it; R4 uses BackboneElement `location.location` | serialize/validate R4 shape |
| Resource/type gaps | playbook mentions R5-only constructs or absent R4 resources | do not silently treat them as R4 |
| Device profile | no SATUSEHAT Device profile was found | derive a local profile from base R4 Device |
| Observation performer | profile page and use-case material differ | device-feed Observation can omit performer; outpatient profile may require it |
| Earliest date | profile pages and API rule text disagree | implementation chooses a configurable event-date floor; demographic birthDate is exempt |

## 3. Clinical and device-data rationale

The clinical motivation comes from the Pra-TA research direction on contactless
jugular venous pulse (JVP) / carotid pulse measurement using radar. The repository
contains related papers under `docs/papers/` (and earlier material under
`PraTAPapers/` where present); cite the individual papers only after checking
their methods, populations, limitations, and clinical claims directly.

The present firmware is a **placeholder transport/demo**, not a validated
signal-processing pipeline:

- the ESP32-S3 sketch still emits a serial JSON diagnostic stream;
- current HTTP/WebSocket integration work may use placeholder HR values until
  radar signal processing is connected;
- GPIO assignments and AFE integration remain hardware assumptions;
- compile success proves C++ buildability, not sensor accuracy, WiFi operation,
  clinical validity, or hardware safety.

A defensible proposal should separate the stages: sensor acquisition → signal
processing/feature extraction → physiological measurement validation → FHIR
mapping → clinician interpretation. Do not describe placeholder values as
radar-derived clinical measurements.

## 4. Resource and workflow model

### Walking-skeleton scenario

The implemented proving path is:

1. An admin provisions a flat Organization, Location, practitioner/patient
   accounts, Device, and device token.
2. A doctor opens an Encounter for the patient; the Encounter starts at
   `arrived`, moves to `in-progress`, and may later finish.
3. The attached device submits a heart-rate Observation linked to the
   Patient, Encounter, and Device.
4. The doctor reads the Observation through an encounter-participant access
   rule.
5. The patient reads only their own Patient/Encounter/Observation resources.

The workflow uses the following codes for the initial slice:

- Observation code: LOINC `8867-4` (Heart rate).
- Quantity unit: UCUM `/min` (`http://unitsofmeasure.org`).
- Observation category: `vital-signs` from the HL7 observation-category system.
- Encounter class: `AMB` from the v3 ActCode system.

The initial slice does **not** implement the full Rawat Jalan resource set,
Condition/Procedure breadth, CareTeam, PractitionerRole, patient UI, FHIR
transactions, PATCH, or terminology operations. Those are roadmap items, not
current capabilities.

### Authorization

- Admin: manages/provisions resources and accounts.
- Doctor: reads patients only where they participate in an Encounter; creates
  visits and reads linked observations. Updates are authorized against stored
  participation, not a caller-supplied participant list.
- Patient: read-only access to their own record.
- Device: writes only for its provisioned patient/device and an eligible
  in-progress encounter; token is opaque and stored hashed.

These are prototype authorization rules; a production deployment needs a
formal threat model, secure secrets management, audit controls, operational
access policies, and clinical/privacy review.

## 5. Validation and conformance methodology

### Layered validation

The server's current validation pipeline is:

```text
JSON request
  → fhir.resources R4B model parse + strict JSON primitive pre-walk
  → base resource structure and primitive checks
  → per-resource SATUSEHAT/local constraints
  → reference and workflow checks
  → persist only after all checks pass
  → OperationOutcome on rejection
```

The strict pre-walk exists because generated FHIR model validators may coerce
quoted JSON primitive values. It rejects cases such as quoted booleans/numbers
and arrays where a scalar is expected before the model parse can silently
normalize them. Tests specifically cover nested depth as well as root fields.

SATUSEHAT validation uses printed RuleNumbers where the meaning matches; local
rules use a distinct range. A validation failure is returned as an
`OperationOutcome` with issue severity/code/details and element expression. The
persistence order is **processor then server**: validation failure means no
resource write; failed update leaves the prior resource unchanged.

### Conformance test strategy

- Unit tests for identifiers, date rules, profile-specific constraints,
  OperationOutcome construction, sequence handling, and role checks.
- Integration tests for HTTP status/media types, JWT/device-token handling,
  cross-patient denial, and the full admin→doctor→device→patient story.
- Regression tests based on the validity review's known traps (wrong R4 JSON
  shapes, quoted primitives, identifier contradictions, date boundaries).
- Independent build check for firmware; compilation is not hardware validation.
- Final review surfaced and fixed bugs that green tests had missed, including
  malformed firmware JSON, nested primitive coercion, and authorization paths.
  The method lesson: adversarially test the *actual boundary* (e.g. parse the
  literal firmware payload), not just the Python helper that mirrors it.

## 6. Future profile-creation methodology

A FHIR profile is a `StructureDefinition` with `derivation = constraint` over a
base resource. It narrows the base; it cannot rename elements, add arbitrary
resource fields, or change the base element's meaning. Since no SATUSEHAT Device
profile was found, the device profile is a project-authored conformance artifact
based on **FHIR R4 Device**.

### The 13-step Device-profile checklist

1. Create a `StructureDefinition`: canonical `url`, `name`, `status`,
   `kind=resource`, `abstract=false`, `type=Device`, R4 Device
   `baseDefinition`, `derivation=constraint`.
2. Write a sparse `differential` containing only constrained elements, in base
   element order, with exact `id` and `path`.
3. Use only paths present on base R4 Device.
4. Tighten cardinality only in legal directions (e.g. `0..1 → 1..1` or `0..0`).
5. Choose `fixed[x]` for exact values or `pattern[x]` for matching required
   properties; not both on one element.
6. Bind only supported element types and never weaken binding strength.
7. Constrain Reference targets with `type.targetProfile`.
8. Slice repeating elements when identity/meaning must be distinguished;
   declare discriminator and slicing rules, then named slices.
9. Define a separate Extension `StructureDefinition` for data with no base
   element; slice `Device.extension` by URL. Use modifier extensions only when
   ignoring the data would alter interpretation.
10. Mark `mustSupport` only for elements every conformant implementation must
    actually use; define what “support” means.
11. Add invariants with key, severity, human text, and FHIRPath expression;
    retain all base constraints.
12. Generate a complete `snapshot` (definitions, min/max, base on every element).
13. Package profile/extensions in an `ImplementationGuide`, declare supported
    profiles in `CapabilityStatement`, stamp instance `meta.profile`, and
    support `_profile` search.

Reference guide: `docs/reference/human/14-fhir-profiling-a-new-device.md`.
Technical authority: `docs/reference/claude/fhir-profiling.md` and its Sources.

### Profile contents still to decide

The checklist is method, not a pre-decided profile. A later design must decide:

- which Device identifiers and serial/manufacturer/model fields are required;
- how Device relates to the Patient and the measurement Observation;
- whether calibration/configuration metadata needs a formal extension;
- profile URL/canonical namespace owned by the project;
- Observation profile details and whether a radar waveform belongs in
  `SampledData`, a separate resource, or an external attachment;
- terminology bindings, UCUM units, and how derived JVP/carotid metrics are
  distinguished from direct heart rate;
- conformance examples and negative tests, including the exact rule numbers.

## 7. Project status and roadmap

### Completed

- Reference compilation: 93 scraped source pages; 31 technical reference views;
  13 human-oriented guides; validity review of SATUSEHAT claims against R4.
- Walking-skeleton FHIR R4 server: local FastAPI + SQLite; seven resource types;
  role/device auth; Observation validation; test suite and CLI seed/serve.
- Firmware HTTP/WebSocket demo is compile-gated; actual hardware behavior and
  clinical measurement accuracy are **not** established by compile/test results.

### In progress / planned

1. Public deployment and request-history UI behind Cloudflare Access + Tunnel,
   nginx on loopback. Latest design: `docs/.superpowers/specs/2026-10-08-public-exposure-request-history-design.md`.
2. Continuous WebSocket heart-rate stream with persisted sequence index and UTC
   timestamps; gap detection, duplicate handling, reconnect replay.
3. Formal Device and Observation profiles, extensions as needed, IG packaging.
4. Web UI for clinician worklist and patient view.
5. Broader Encounter/Condition/Procedure/Rawat Jalan resources, Bundles/PATCH,
   organization hierarchy, profile-driven validation.
6. Replace placeholder heart rate with validated radar-derived signal processing;
   later decide SpO₂ terminology if the device expands.
7. Operational production-hardening, privacy/security review, and clinical
   validation (not implied by the walking skeleton).

## 8. Repository map and useful starting points

| Need | Start here |
|---|---|
| Project instructions/status | `CLAUDE.md` |
| FHIR/SATUSEHAT reference map | `docs/reference/claude/INDEX.md` |
| Contradictions and rulings | `docs/reference/claude/VALIDITY-REVIEW.md`, `VALIDITY-REVIEW-claims.md` |
| R4 REST/search | `docs/reference/claude/fhir-rest-api.md` |
| Security/roles | `docs/reference/claude/fhir-security.md` |
| Observation/vitals | `docs/reference/claude/fhir-observation.md`, `satusehat-observation.md` |
| Device base resource | `docs/reference/claude/fhir-device.md` |
| Profiles/StructureDefinition | `docs/reference/claude/fhir-profiling.md` |
| SATUSEHAT identifiers | `docs/reference/claude/satusehat-identifiers-and-master-data.md` |
| Walking-skeleton design | `docs/.superpowers/specs/2026-09-29-fhir-r4-server-walking-skeleton-design.md` |
| Walking-skeleton plan | `docs/.superpowers/plans/2026-09-29-fhir-r4-server-walking-skeleton.md` |
| Server run guide | `fhir_server/README.md` |
| Server source/tests | `fhir_server/`, `tests/` |
| Firmware and serial assumptions | `arduino/radar_json/README.md`, `arduino/radar_json/radar_json.ino` |
| Research papers | `docs/papers/`, `PraTAPapers/` (verify/cite individual papers directly) |

### Verification commands

```bash
.venv/bin/python -m pytest tests -q
python3 -m pytest .tools/scrape/tests -q
python3 .tools/scrape/lint_views.py
arduino-cli compile --fqbn m5stack:esp32:m5stack_cores3 arduino/radar_json
```

## 9. Proposal-writing prompts (for the project owner)

Use this brief to draft your proposal; these are prompts, not claims to copy:

1. **Problem statement:** what measurement problem does radar-based contactless
   pulse/JVP monitoring address, for which clinical setting and population?
2. **Research question:** are you evaluating signal-processing accuracy,
   interoperability/profile design, workflow usability, or an integrated system?
   Separate these objectives if necessary.
3. **Contribution:** what is novel relative to existing radar vital-sign work,
   SATUSEHAT/FHIR integrations, and device profiles?
4. **Methods:** what hardware, signal-processing pipeline, reference instrument,
   participant protocol, clinical ground truth, statistical agreement metrics,
   and safety/ethics approvals are required?
5. **Interoperability evaluation:** which R4 resources/profiles, terminology,
   identifiers, validation rules, and conformance tests demonstrate the mapping?
6. **System evaluation:** how will access control, data integrity, timing,
   sequence-gap recovery, latency, loss, and end-to-end workflow be measured?
7. **Limitations:** state plainly that the current values/firmware are placeholders
   until measurement validation; compilation is not clinical evidence.
8. **Deployment and privacy:** define local-vs-public deployment, data retention,
   consent, pseudonymization, access audit, threat model, and institutional policy.

## Sources

- `CLAUDE.md` (project goals/status and constraints)
- `docs/reference/human/README.md` and guides 01–15
- `docs/reference/claude/INDEX.md` and cited technical summaries
- `docs/.superpowers/specs/2026-09-29-fhir-r4-server-walking-skeleton-design.md`
- `docs/.superpowers/specs/2026-10-08-public-exposure-request-history-design.md`
- `fhir_server/README.md`
- `arduino/radar_json/README.md`

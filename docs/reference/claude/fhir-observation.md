# FHIR R4 — Observation (incl. Vital Signs profile)

Purpose: "Measurements and simple assertions made about a patient, device or other subject." Observation is Normative (from v4.0.0), an *event* resource in the workflow sense, security category Patient, in the Device / Encounter / Patient / Practitioner / RelatedPerson compartments. The page states that implementations expressing vital signs as structured data **SHALL** conform to the core Vital Signs profile (`observation-vitalsigns`, status Informative).

Flags column as printed in the structure table: `Σ` = in summary, `?!` = modifier element, `I` = has/affected by invariants, `TU` = trial use, `N` = normative.

## Elements (summary table)
Root `Observation` is a `DomainResource` (inherits `id`, `meta`, `implicitRules`, `language`, `text`, `contained`, `extension`, `modifierExtension`); the root carries rules obs-6 and obs-7 (below).

| Element | Flags | Card. | Type | Notes |
|---|---|---|---|---|
| `Observation.identifier` | Σ | 0..* | Identifier | Business Identifier for observation |
| `Observation.basedOn` | Σ | 0..* | Reference(CarePlan \| DeviceRequest \| ImmunizationRecommendation \| MedicationRequest \| NutritionOrder \| ServiceRequest) | Fulfills plan, proposal or order |
| `Observation.partOf` | Σ | 0..* | Reference(MedicationAdministration \| MedicationDispense \| MedicationStatement \| Procedure \| Immunization \| ImagingStudy) | Part of referenced event |
| `Observation.status` | ?!Σ | 1..1 | code | registered \| preliminary \| final \| amended + (as printed); ObservationStatus (Required) |
| `Observation.category` |  | 0..* | CodeableConcept | Classification of type of observation; Observation Category Codes (Preferred) |
| `Observation.code` | Σ | 1..1 | CodeableConcept | Type of observation (code / type); LOINC Codes (Example) |
| `Observation.subject` | Σ | 0..1 | Reference(Patient \| Group \| Device \| Location) | Who and/or what the observation is about |
| `Observation.focus` | ΣTU | 0..* | Reference(Any) | What the observation is about, when it is not about the subject of record |
| `Observation.encounter` | Σ | 0..1 | Reference(Encounter) | Healthcare event during which this observation is made |
| `Observation.effective[x]` | Σ | 0..1 | dateTime \| Period \| Timing \| instant | Clinically relevant time/time-period for observation (`effectiveDateTime`, `effectivePeriod`, `effectiveTiming`, `effectiveInstant`) |
| `Observation.issued` | Σ | 0..1 | instant | Date/Time this version was made available |
| `Observation.performer` | Σ | 0..* | Reference(Practitioner \| PractitionerRole \| Organization \| CareTeam \| Patient \| RelatedPerson) | Who is responsible for the observation |
| `Observation.value[x]` | ΣI | 0..1 | Quantity \| CodeableConcept \| string \| boolean \| integer \| Range \| Ratio \| SampledData \| time \| dateTime \| Period | Actual result (`valueQuantity`, `valueCodeableConcept`, `valueString`, `valueBoolean`, `valueInteger`, `valueRange`, `valueRatio`, `valueSampledData`, `valueTime`, `valueDateTime`, `valuePeriod`) |
| `Observation.dataAbsentReason` | I | 0..1 | CodeableConcept | Why the result is missing; DataAbsentReason (Extensible) |
| `Observation.interpretation` |  | 0..* | CodeableConcept | High, low, normal, etc.; Observation Interpretation Codes (Extensible) |
| `Observation.note` |  | 0..* | Annotation | Comments about the observation |
| `Observation.bodySite` |  | 0..1 | CodeableConcept | Observed body part; SNOMED CT Body Structures (Example) |
| `Observation.method` |  | 0..1 | CodeableConcept | How it was done; Observation Methods (Example) |
| `Observation.specimen` |  | 0..1 | Reference(Specimen) | Specimen used for this observation |
| `Observation.device` |  | 0..1 | Reference(Device \| DeviceMetric) | (Measurement) Device |
| `Observation.referenceRange` | I | 0..* | BackboneElement | Provides guide for interpretation + Rule: Must have at least a low or a high or text (obs-3) |
| `Observation.referenceRange.low` | I | 0..1 | SimpleQuantity | Low Range, if relevant |
| `Observation.referenceRange.high` | I | 0..1 | SimpleQuantity | High Range, if relevant |
| `Observation.referenceRange.type` |  | 0..1 | CodeableConcept | Reference range qualifier; Observation Reference Range Meaning Codes (Preferred) |
| `Observation.referenceRange.appliesTo` |  | 0..* | CodeableConcept | Reference range population; Observation Reference Range Applies To Codes (Example) |
| `Observation.referenceRange.age` |  | 0..1 | Range | Applicable age range, if relevant |
| `Observation.referenceRange.text` |  | 0..1 | string | Text based reference range in an observation |
| `Observation.hasMember` | Σ | 0..* | Reference(Observation \| QuestionnaireResponse \| MolecularSequence) | Related resource that belongs to the Observation group |
| `Observation.derivedFrom` | Σ | 0..* | Reference(DocumentReference \| ImagingStudy \| Media \| QuestionnaireResponse \| Observation \| MolecularSequence) | Related measurements the observation is made from |
| `Observation.component` | Σ | 0..* | BackboneElement | Component results |
| `Observation.component.code` | Σ | 1..1 | CodeableConcept | Type of component observation (code / type); LOINC Codes (Example) |
| `Observation.component.value[x]` | Σ | 0..1 | same 11 types as `Observation.value[x]` | Actual component result (`valueQuantity` … `valuePeriod`) |
| `Observation.component.dataAbsentReason` | I | 0..1 | CodeableConcept | Why the component result is missing; DataAbsentReason (Extensible) |
| `Observation.component.interpretation` |  | 0..* | CodeableConcept | High, low, normal, etc.; Observation Interpretation Codes (Extensible) |
| `Observation.component.referenceRange` |  | 0..* | see `referenceRange` | Provides guide for interpretation of component result |

### Terminology bindings (as printed)
| Path | Strength | Value set |
|---|---|---|
| `Observation.status` | Required | ObservationStatus |
| `Observation.category` | Preferred | ObservationCategoryCodes |
| `Observation.code`, `Observation.component.code` | Example | LOINCCodes |
| `Observation.dataAbsentReason`, `Observation.component.dataAbsentReason` | Extensible | DataAbsentReason |
| `Observation.interpretation`, `Observation.component.interpretation` | Extensible | ObservationInterpretationCodes |
| `Observation.bodySite` | Example | SNOMEDCTBodyStructures |
| `Observation.method` | Example | ObservationMethods |
| `Observation.referenceRange.type` | Preferred | ObservationReferenceRangeMeaningCodes |
| `Observation.referenceRange.appliesTo` | Example | ObservationReferenceRangeAppliesToCodes |

## Search parameters
All are marked `TU` on the page. "In common" = number of resources sharing the parameter, as printed.

| Name | Type | Expression |
|---|---|---|
| based-on | reference | `Observation.basedOn` (CarePlan, MedicationRequest, NutritionOrder, DeviceRequest, ServiceRequest, ImmunizationRecommendation) |
| category | token | `Observation.category` |
| code | token | `Observation.code` (13 Resources) |
| code-value-concept | composite | On Observation: `code`: code; `value-concept`: `value.as(CodeableConcept)` |
| code-value-date | composite | On Observation: `code`: code; `value-date`: `value.as(DateTime) \| value.as(Period)` |
| code-value-quantity | composite | On Observation: `code`: code; `value-quantity`: `value.as(Quantity)` |
| code-value-string | composite | On Observation: `code`: code; `value-string`: `value.as(string)` |
| combo-code | token | `Observation.code \| Observation.component.code` |
| combo-code-value-concept | composite | On `Observation \| Observation.component`: `combo-code`: code; `combo-value-concept`: `value.as(CodeableConcept)` |
| combo-code-value-quantity | composite | On `Observation \| Observation.component`: `combo-code`: code; `combo-value-quantity`: `value.as(Quantity)` |
| combo-data-absent-reason | token | `Observation.dataAbsentReason \| Observation.component.dataAbsentReason` |
| combo-value-concept | token | `(Observation.value as CodeableConcept) \| (Observation.component.value as CodeableConcept)` |
| combo-value-quantity | quantity | `(Observation.value as Quantity) \| (Observation.value as SampledData) \| (Observation.component.value as Quantity) \| (Observation.component.value as SampledData)` |
| component-code | token | `Observation.component.code` |
| component-code-value-concept | composite | On `Observation.component`: `component-code`: code; `component-value-concept`: `value.as(CodeableConcept)` |
| component-code-value-quantity | composite | On `Observation.component`: `component-code`: code; `component-value-quantity`: `value.as(Quantity)` |
| component-data-absent-reason | token | `Observation.component.dataAbsentReason` |
| component-value-concept | token | `(Observation.component.value as CodeableConcept)` |
| component-value-quantity | quantity | `(Observation.component.value as Quantity) \| (Observation.component.value as SampledData)` |
| data-absent-reason | token | `Observation.dataAbsentReason` |
| date | date | `Observation.effective` (17 Resources) — "if the obtained element is a period, a date that falls in the period" |
| derived-from | reference | `Observation.derivedFrom` (Media, Observation, ImagingStudy, MolecularSequence, QuestionnaireResponse, DocumentReference) |
| device | reference | `Observation.device` (Device, DeviceMetric) |
| encounter | reference | `Observation.encounter` (Encounter) (12 Resources) |
| focus | reference | `Observation.focus` (Any) |
| has-member | reference | `Observation.hasMember` (Observation, MolecularSequence, QuestionnaireResponse) |
| identifier | token | `Observation.identifier` (30 Resources) |
| method | token | `Observation.method` |
| part-of | reference | `Observation.partOf` (Immunization, MedicationDispense, MedicationAdministration, Procedure, ImagingStudy, MedicationStatement) |
| patient | reference | `Observation.subject.where(resolve() is Patient)` (Patient) (33 Resources) |
| performer | reference | `Observation.performer` (Practitioner, Organization, CareTeam, Patient, PractitionerRole, RelatedPerson) |
| specimen | reference | `Observation.specimen` (Specimen) |
| status | token | `Observation.status` |
| subject | reference | `Observation.subject` (Group, Device, Patient, Location) |
| value-concept | token | `(Observation.value as CodeableConcept)` |
| value-date | date | `(Observation.value as dateTime) \| (Observation.value as Period)` |
| value-quantity | quantity | `(Observation.value as Quantity) \| (Observation.value as SampledData)` — "just search on the bounds of the values in sampled data" |
| value-string | string | `(Observation.value as string) \| (Observation.value as CodeableConcept).text` |

The page adds: "There is no standard parameter for searching values of type Ratio." Operations defined: `$lastn` (most recent / last-known Observations for a subject) and `$stats` (statistics over `valueQuantity` with UCUM codes); both detailed on the un-scraped operations page.

## Invariants / constraints
- obs-3 (Rule, `Observation.referenceRange`): Must have at least a low or a high or text — `low.exists() or high.exists() or text.exists()`
- obs-6 (Rule, base): dataAbsentReason SHALL only be present if Observation.value[x] is not present — `dataAbsentReason.empty() or value.empty()`
- obs-7 (Rule, base): If Observation.code is the same as an Observation.component.code then the value element associated with the code SHALL NOT be present — `value.empty() or component.code.where(coding.intersect(%resource.code.coding).exists()).empty()`

## Relationships
- references: CarePlan, DeviceRequest, ImmunizationRecommendation, MedicationRequest, NutritionOrder, ServiceRequest (`basedOn`); MedicationAdministration, MedicationDispense, MedicationStatement, Procedure, Immunization, ImagingStudy (`partOf`); Patient, Group, Device, Location (`subject`); Any (`focus`); Encounter; Practitioner, PractitionerRole, Organization, CareTeam, Patient, RelatedPerson (`performer`); Specimen; Device, DeviceMetric (`device`); Observation, QuestionnaireResponse, MolecularSequence (`hasMember`); DocumentReference, ImagingStudy, Media, QuestionnaireResponse, Observation, MolecularSequence (`derivedFrom`).
- referenced by: AdverseEvent, Appointment, CarePlan, ChargeItem, ClinicalImpression, Communication, CommunicationRequest, Condition, Contract, DeviceRequest, DeviceUseStatement, DiagnosticReport, Encounter, FamilyMemberHistory, Goal, GuidanceResponse, ImagingStudy, Immunization, MedicationAdministration, MedicationRequest, MedicationStatement, MolecularSequence, itself, Procedure, QuestionnaireResponse, RequestGroup, RiskAssessment, ServiceRequest and SupplyRequest.
- Boundaries: not for diagnoses (Condition / ClinicalImpression), allergies (AllergyIntolerance), medications (MedicationStatement), family history, procedures, questionnaire answers, or audio/video/image values (Media); DiagnosticReport gives the clinical context and references Observations for atomic results.

## Grouping rules (page §10.1.4.3)
| Structure | Use when (as stated) |
|---|---|
| `DiagnosticReport.result` | Report relates to an order; `DiagnosticReport.code` names the panel; `result` references the individual observations |
| `Observation.component` | Supporting results that "cannot reasonably be interpreted and used outside the scope of the Observation"; "only be used when there is only one method, one observation, one performer, one device, and one time"; e.g. systolic + diastolic BP as one Blood pressure panel, Apgar with five components; BMI should **not** contain height/weight components |
| `Observation.hasMember` | Panel/battery grouping: `code` = panel code, `value[x]` typically absent, members listed in `hasMember`; members are usable on their own and may differ in method/performer/device/time |
| `Observation.derivedFrom` | Both `code` and `value[x]` present; linked source observations (e.g. BMI derived from height and weight) |

Other page rules: `effectiveDateTime`/`effectivePeriod` is the "physiologically relevant time" (for BP the start/end of the observation process, usually one point in time); below/above detection limit → `valueQuantity` with `comparator` (`<`); error → `dataAbsentReason` code `error` or `NaN` (system `http://terminology.hl7.org/CodeSystem/data-absent-reason`); cancelled measurements → `status` "cancelled" plus `dataAbsentReason`/`valueCodeableConcept`; `valueBoolean` is discouraged (use CodeableConcept from v2-0136 instead); more than one `referenceRange` SHOULD differ in `appliesTo`/`age`.

## Vital Signs profile (`observation-vitalsigns`)
Status: Informative; originally from the DAF project, updated for Argonaut. "Sets minimum expectations for the Observation resource to record, search and fetch the vital signs associated with a patient".

### Mandatory content ("Each Observation must have", as printed)
| # | Requirement | Element it lands on |
|---|---|---|
| 1 | a status | `Observation.status` |
| 2 | a category code of `vital-signs` | `Observation.category` |
| 3 | a "magic value" which tells you what is being measured — LOINC, "can be treated as simply a fixed core set of common codes" | `Observation.code` |
| 4 | a patient | `Observation.subject` |
| 5 | a time indicating when the measurement was taken | `Observation.effective[x]` |
| 6 | a numeric result value and standard UCUM unit taken from the Unit Code column; "if there is no numeric result then you have to supply a reason" | `Observation.valueQuantity` / `dataAbsentReason` |

Formal invariants (`vs-1` …) and the profile StructureDefinition element table are **not** on the scraped page (they live on the linked profile-definition page, not fetched); the page only gives the human-readable list above. Do not cite `vs-N` ids from this reference.

### Vital-sign codes (the "magic values")
"These are extensible bindings and require that when a system supports any of these vital signs concepts, they must represent them using these codes." If a more specific / other code system is used, "implementers must support both the values (LOINC) listed below and the translated code".

| Profile name | LOINC | LOINC name / comments (abridged) | UCUM unit code |
|---|---|---|---|
| Vital Signs Panel | 85353-1 | *Vital signs, weight, height, head circumference, oxygen saturation and BMI panel*; members optional; `valueQuantity` not present, members referenced via `hasMember`; replaces deprecated 8716-3 | — |
| Respiratory Rate | 9279-1 | *Respiratory Rate* | `/min` |
| Heart rate | 8867-4 | *Heart rate*; 8887-2 *Heart rate device type* MAY be an additional observation | `/min` |
| Oxygen saturation | 2708-6 | *Oxygen saturation in Arterial blood*; replaces 59408-5 (by Pulse oximetry), which MAY be included as an additional code | `%` |
| Body temperature | 8310-5 | *Body temperature*; 8327-9 measurement site, 8326-1 device type MAY be additional observations | `Cel`, `[degF]` |
| Body height | 8302-2 | *Body height*; 8306-3 *Body height - lying* MAY be an additional code | `cm`, `[in_i]` |
| Head circumference | 9843-4 | *Head Occipital-frontal circumference* | `cm`, `[in_i]` |
| Body weight | 29463-7 | *Body weight*; 8352-7 clothing worn, 8361-8 body position MAY be additional codes | `g`, `kg`, `[lb_av]` |
| Body mass index | 39156-5 | *Body mass index (BMI) [Ratio]* | `kg/m2` |
| Blood pressure systolic and diastolic | 85354-9 | *Blood pressure panel with all children optional*; a component observation — no `valueQuantity`, at least one component; 8478-0 mean BP, 8357-6 method, 41904-4 site, 8358-4 cuff size, 41901-0 device type MAY be additional observations | `-` |
| Systolic blood pressure | 8480-6 | *Systolic blood pressure* — `Observation.component` code | `mm[Hg]` |
| Diastolic blood pressure | 8462-4 | *Diastolic blood pressure* — `Observation.component` code | `mm[Hg]` |

### Blood-pressure `component` rule
"If you have a blood pressure observation, you must have both a systolic and a diastolic component, though one or both may have dataAbsentReason instead of a value." Search note: the `code` parameter searches only `Observation.code`, so a BP resource is returned for `code=85354-9`, **not** for `8480-6`/`8462-4`; use `combo-code` to search `code` and `component.code` together.

### Quick Start (required search / read)
| Query | Support |
|---|---|
| `GET [base]/Observation?patient=[id]&category=vital-signs` | Mandatory (search by category) |
| `GET [base]/Observation?patient=[id]&category=vital-signs&date=[date]{&date=[date]}` | Mandatory (category + date) |
| `GET [base]/Observation?patient=[id]&code=[vital sign LOINC{,LOINC2,LOINC3,...}]` | Mandatory (one or more LOINC codes; example `code=8867-4,9279-1,85354-9`) |
| `GET [base]/Observation?patient=[id]&code=[LOINC{,LOINC2...}]vital-signs&date=[date]{&date=[date]}` | SHOULD (codes + date range) — URL printed verbatim, including the odd `]vital-signs` |

Response classes listed: 200 successful, 400 invalid parameter, 401/4xx unauthorized, 403 insufficient scope. Server statements: every request includes `Authorization: Bearer {server-specific-token-here}`; unauthorized requests get HTTP 401.

## Notes for our server
- `Observation.status` (1..1, Required binding ObservationStatus) and `Observation.code` (1..1) are the only mandatory base elements — reject a POST missing either with `400`/`422`; `status` is a modifier element (`?!`) so it must be honored when displaying/filtering (e.g. hide `entered-in-error`).
- Enforce obs-6 (no `dataAbsentReason` alongside `value[x]`), obs-3 (referenceRange needs low/high/text) and obs-7 (no `value[x]` when `code` equals a `component.code`) at validation time — all three are Rules, not warnings.
- Device-sourced vital signs: populate `category = vital-signs`, `code` = LOINC magic value from the table, `subject = Patient/…`, `effectiveDateTime`, `valueQuantity` with `system = http://unitsofmeasure.org` and the UCUM code column (`/min`, `%`, `Cel`, `kg`, `cm`, `kg/m2`, `mm[Hg]`), and `device = Device/…` (0..1 Reference(Device | DeviceMetric)) so the reading is traceable to our profiled device.
- Blood pressure: one Observation with `code = 85354-9`, no `valueQuantity`, and two `component` entries (`8480-6`, `8462-4`, both `mm[Hg]`); a missing side gets `component.dataAbsentReason` rather than being omitted. BMI must be a separate Observation (optionally `derivedFrom` height/weight), not a component set.
- Search engine must support at least `patient`, `category`, `code` (comma OR list), `date` (with `ge`/`le` prefixes), plus `combo-code`, `component-code`, `value-quantity`, `device`, `encounter`, `subject`, `status`, `identifier`; composite `code-value-quantity` is what `code=…$lt60` style queries need; `patient` resolves `subject` only when it is a Patient.
- SATUSEHAT (see satusehat-observation.md) additionally makes `subject`, `encounter` and `code.coding` wajib; base FHIR has `encounter` 0..1 — our profile should tighten it to 1..1 for the outpatient flow.
- Consider `$lastn` for the patient dashboard ("last 5 temperatures") — an operation, so declare it in CapabilityStatement `rest.resource.operation` if implemented.

## Sources
- raw/fhir-r4/observation.md
- raw/fhir-r4/observation-vitalsigns.md

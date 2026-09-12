# FHIR R4 — Procedure

Purpose: "An action that is being or was performed on a patient" — "current and historical procedures performed on or for a patient" (surgical, diagnostic, endoscopic, biopsies, counseling, physiotherapy, support services, transport …); an *event* resource in the workflow sense, giving summary information, "not intended to provide real-time snapshots". Trial Use, maturity 3, security category Patient, compartments Encounter / Patient / Practitioner / RelatedPerson. Flags: `Σ` summary, `?!` modifier, `TU` trial use.

## Elements (summary table)
Root `Procedure` (TU) is a DomainResource. No constraints table is printed on the page.

| Element | Flags | Card. | Type | Notes |
|---|---|---|---|---|
| `Procedure.identifier` | Σ | 0..* | Identifier | External Identifiers for this procedure |
| `Procedure.instantiatesCanonical` | Σ | 0..* | canonical(PlanDefinition \| ActivityDefinition \| Measure \| OperationDefinition \| Questionnaire) | Instantiates FHIR protocol or definition |
| `Procedure.instantiatesUri` | Σ | 0..* | uri | Instantiates external protocol or definition |
| `Procedure.basedOn` | Σ | 0..* | Reference(CarePlan \| ServiceRequest) | A request for this procedure |
| `Procedure.partOf` | Σ | 0..* | Reference(Procedure \| Observation \| MedicationAdministration) | Part of referenced event |
| `Procedure.status` | ?!Σ | 1..1 | code | preparation \| in-progress \| not-done \| on-hold \| stopped \| completed \| entered-in-error \| unknown; EventStatus (Required) |
| `Procedure.statusReason` | Σ | 0..1 | CodeableConcept | Reason for current status; Procedure Not Performed Reason (SNOMED-CT) (Example) |
| `Procedure.category` | Σ | 0..1 | CodeableConcept | Classification of the procedure; Procedure Category Codes (SNOMED CT) (Example) |
| `Procedure.code` | Σ | 0..1 | CodeableConcept | Identification of the procedure; Procedure Codes (SNOMED CT) (Example) |
| `Procedure.subject` | Σ | 1..1 | Reference(Patient \| Group) | Who the procedure was performed on |
| `Procedure.encounter` | Σ | 0..1 | Reference(Encounter) | Encounter created as part of |
| `Procedure.performed[x]` | Σ | 0..1 | dateTime \| Period \| string \| Age \| Range | When the procedure was performed (`performedDateTime`, `performedPeriod`, `performedString`, `performedAge`, `performedRange`) |
| `Procedure.recorder` | Σ | 0..1 | Reference(Patient \| RelatedPerson \| Practitioner \| PractitionerRole) | Who recorded the procedure |
| `Procedure.asserter` | Σ | 0..1 | Reference(Patient \| RelatedPerson \| Practitioner \| PractitionerRole) | Person who asserts this procedure |
| `Procedure.performer` | Σ | 0..* | BackboneElement | The people who performed the procedure |
| `Procedure.performer.function` | Σ | 0..1 | CodeableConcept | Type of performance; Procedure Performer Role Codes (Example) |
| `Procedure.performer.actor` | Σ | 1..1 | Reference(Practitioner \| PractitionerRole \| Organization \| Patient \| RelatedPerson \| Device) | The reference to the practitioner |
| `Procedure.performer.onBehalfOf` |  | 0..1 | Reference(Organization) | Organization the device or practitioner was acting for |
| `Procedure.location` | Σ | 0..1 | Reference(Location) | Where the procedure happened |
| `Procedure.reasonCode` | Σ | 0..* | CodeableConcept | Coded reason procedure performed; Procedure Reason Codes (Example) |
| `Procedure.reasonReference` | Σ | 0..* | Reference(Condition \| Observation \| Procedure \| DiagnosticReport \| DocumentReference) | The justification that the procedure was performed |
| `Procedure.bodySite` | Σ | 0..* | CodeableConcept | Target body sites; SNOMED CT Body Structures (Example) |
| `Procedure.outcome` | Σ | 0..1 | CodeableConcept | The result of procedure; Procedure Outcome Codes (SNOMED CT) (Example) |
| `Procedure.report` |  | 0..* | Reference(DiagnosticReport \| DocumentReference \| Composition) | Any report resulting from the procedure |
| `Procedure.complication` |  | 0..* | CodeableConcept | Complication following the procedure; Condition/Problem/Diagnosis Codes (Example) |
| `Procedure.complicationDetail` |  | 0..* | Reference(Condition) | A condition that is a result of the procedure |
| `Procedure.followUp` |  | 0..* | CodeableConcept | Instructions for follow up; Procedure Follow up Codes (SNOMED CT) (Example) |
| `Procedure.note` |  | 0..* | Annotation | Additional information about the procedure |
| `Procedure.focalDevice` |  | 0..* | BackboneElement | Manipulated, implanted, or removed device |
| `Procedure.focalDevice.action` |  | 0..1 | CodeableConcept | Kind of change to device; Procedure Device Action Codes (Preferred) |
| `Procedure.focalDevice.manipulated` |  | 1..1 | Reference(Device) | Device that was changed |
| `Procedure.usedReference` |  | 0..* | Reference(Device \| Medication \| Substance) | Items used during procedure |
| `Procedure.usedCode` |  | 0..* | CodeableConcept | Coded items used during the procedure; FHIR Device Types (Example) |

### Terminology bindings (as printed)
| Path | Strength | Value set |
|---|---|---|
| `Procedure.status` | Required | EventStatus |
| `Procedure.statusReason` | Example | ProcedureNotPerformedReason(SNOMED-CT) |
| `Procedure.category` | Example | ProcedureCategoryCodes(SNOMEDCT) |
| `Procedure.code` | Example | ProcedureCodes(SNOMEDCT) |
| `Procedure.performer.function` | Example | ProcedurePerformerRoleCodes |
| `Procedure.reasonCode` | Example | ProcedureReasonCodes |
| `Procedure.bodySite` | Example | SNOMEDCTBodyStructures |
| `Procedure.outcome` | Example | ProcedureOutcomeCodes(SNOMEDCT) |
| `Procedure.complication` | Example | Condition/Problem/DiagnosisCodes |
| `Procedure.followUp` | Example | ProcedureFollowUpCodes(SNOMEDCT) |
| `Procedure.focalDevice.action` | Preferred | ProcedureDeviceActionCodes |
| `Procedure.usedCode` | Example | FHIRDeviceTypes |

## Search parameters
| Name | Type | Expression |
|---|---|---|
| based-on | reference | `Procedure.basedOn` (CarePlan, ServiceRequest) |
| category | token | `Procedure.category` |
| code | token | `Procedure.code` (13 Resources) |
| date | date | `Procedure.performed` (17 Resources) |
| encounter | reference | `Procedure.encounter` (Encounter) (12 Resources) |
| identifier | token | `Procedure.identifier` (30 Resources) |
| instantiates-canonical | reference | `Procedure.instantiatesCanonical` (Questionnaire, Measure, PlanDefinition, OperationDefinition, ActivityDefinition) |
| instantiates-uri | uri | `Procedure.instantiatesUri` |
| location | reference | `Procedure.location` (Location) |
| part-of | reference | `Procedure.partOf` (Observation, Procedure, MedicationAdministration) |
| patient | reference | `Procedure.subject.where(resolve() is Patient)` (Patient) (33 Resources) |
| performer | reference | `Procedure.performer.actor` (Practitioner, Organization, Device, Patient, PractitionerRole, RelatedPerson) |
| reason-code | token | `Procedure.reasonCode` |
| reason-reference | reference | `Procedure.reasonReference` (Condition, Observation, Procedure, DiagnosticReport, DocumentReference) |
| status | token | `Procedure.status` — preparation \| in-progress \| not-done \| on-hold \| stopped \| completed \| entered-in-error \| unknown |
| subject | reference | `Procedure.subject` (Group, Patient) |

## Invariants / constraints
- None printed (the page has no Constraints table).

## Relationships
- references: PlanDefinition, ActivityDefinition, Measure, OperationDefinition, Questionnaire (`instantiatesCanonical`); CarePlan, ServiceRequest (`basedOn`); Procedure, Observation, MedicationAdministration (`partOf`); Patient, Group (`subject`); Encounter; Patient, RelatedPerson, Practitioner, PractitionerRole (`recorder`, `asserter`); Practitioner, PractitionerRole, Organization, Patient, RelatedPerson, Device (`performer.actor`); Organization (`performer.onBehalfOf`); Location; Condition, Observation, Procedure, DiagnosticReport, DocumentReference (`reasonReference`); DiagnosticReport, DocumentReference, Composition (`report`); Condition (`complicationDetail`); Device (`focalDevice.manipulated`); Device, Medication, Substance (`usedReference`).
- referenced by: AdverseEvent, Appointment, ChargeItem, Claim, DeviceUseStatement, Encounter, ExplanationOfBenefit, Flag, ImagingStudy, MedicationAdministration, MedicationDispense, MedicationStatement, Observation, itself and QuestionnaireResponse.

## Boundaries and usage rules (page §9.3.2–9.3.3.3)
| Topic | As stated |
|---|---|
| More specific resources win | Not for immunizations, drug administrations, communications |
| Procedure vs Communication | Communication = "mere disclosure of information"; Procedure = intent to change the patient's mind-set, verify comprehension, or change mental state (training, counseling) |
| Diagnostic procedures | Many generate Observations/DiagnosticReports without needing a Procedure; record a Procedure only "when there is a need to capture information about the physical intervention" (anesthetic, incision, scope size …) |
| Procedure vs Task | Task = workflow step (cancel/fulfil/sign an order, admit a patient); Procedure = action intended to cause a physical or mental change; a Task may request fulfilment of a ServiceRequest ordering a Procedure |
| Inherent relationships | `category`, `bodySite`, even indication may be inferable from `code` (or `code.text`); population varies by implementation; avoid nonsense like "name=amputation, bodySite=heart" |
| `used*` vs focal device | `usedReference`/`usedCode` = incidental devices (scalpels, gauze, endoscopes); devices that are the focus go in `focalDevice` (page text says "Procedure.device") |
| Performers | May be a professional, service provider, friend/relative, or the patient |

## Notes for our server
- Mandatory in base R4: `status` (1..1, Required EventStatus) and `subject` (1..1); inside backbones `performer.actor` (1..1) and `focalDevice.manipulated` (1..1). `code` is only 0..1 — the SATUSEHAT profile (satusehat-procedure.md) makes `status`, `code` (ICD-9 CM), `subject`, `encounter` and `performer.actor` wajib, so our profile raises `code`, `encounter` to 1..1 and restricts `subject` to Patient and `performer.actor` to Practitioner/PractitionerRole.
- `status` is a modifier (`?!`): exclude `entered-in-error` and `not-done` from the patient's procedure history by default; `not-done` needs `statusReason`.
- Doctor workflow: POST Procedure with `performedDateTime`/`performedPeriod`, `reasonReference = Condition/…` (links the action to the visit's diagnosis), `performer.actor = Practitioner/…`, optionally `location`; then the Encounter may list it via `Encounter.diagnosis.condition` (which accepts Procedure) or `reasonReference`.
- Do not create a Procedure for every device vital-sign reading — the page says an Observation normally "does not require an explicit representation of the procedure"; reserve Procedure for real interventions. If a device is involved in an intervention, it goes in `focalDevice.manipulated` or `usedReference`, both `Reference(Device)`.
- Search index: `patient`/`subject`, `encounter`, `code`, `date` (`performed[x]`, period-aware), `status`, `performer`, `reason-reference`, `location`, `identifier`; Procedure is in the Patient and Encounter compartments.

## Sources
- raw/fhir-r4/procedure.md

# FHIR R4 — Condition

Purpose: "Detailed information about conditions, problems or diagnoses" — a point-in-time diagnosis in an encounter, a Problem-List item, or a concern; an *event* resource in the workflow sense. Trial Use, maturity 3, security category Patient, compartments Encounter / Patient / Practitioner / RelatedPerson. Flags: `Σ` summary, `?!` modifier, `I` invariant, `TU` trial use.

## Elements (summary table)
Root `Condition` (ITU) is a DomainResource carrying con-3 (guideline), con-4 and con-5.

| Element | Flags | Card. | Type | Notes |
|---|---|---|---|---|
| `Condition.identifier` | Σ | 0..* | Identifier | External Ids for this condition |
| `Condition.clinicalStatus` | ?!ΣI | 0..1 | CodeableConcept | active \| recurrence \| relapse \| inactive \| remission \| resolved; Condition Clinical Status Codes (Required) |
| `Condition.verificationStatus` | ?!ΣI | 0..1 | CodeableConcept | unconfirmed \| provisional \| differential \| confirmed \| refuted \| entered-in-error; ConditionVerificationStatus (Required) |
| `Condition.category` |  | 0..* | CodeableConcept | problem-list-item \| encounter-diagnosis; Condition Category Codes (Extensible) |
| `Condition.severity` |  | 0..1 | CodeableConcept | Subjective severity of condition; Condition/Diagnosis Severity (Preferred) |
| `Condition.code` | Σ | 0..1 | CodeableConcept | Identification of the condition, problem or diagnosis; Condition/Problem/Diagnosis Codes (Example) |
| `Condition.bodySite` | Σ | 0..* | CodeableConcept | Anatomical location, if relevant; SNOMED CT Body Structures (Example) |
| `Condition.subject` | Σ | 1..1 | Reference(Patient \| Group) | Who has the condition? |
| `Condition.encounter` | Σ | 0..1 | Reference(Encounter) | Encounter created as part of |
| `Condition.onset[x]` | Σ | 0..1 | dateTime \| Age \| Period \| Range \| string | Estimated or actual date, date-time, or age (`onsetDateTime`, `onsetAge`, `onsetPeriod`, `onsetRange`, `onsetString`) |
| `Condition.abatement[x]` | I | 0..1 | dateTime \| Age \| Period \| Range \| string | When in resolution/remission (`abatementDateTime`, `abatementAge`, `abatementPeriod`, `abatementRange`, `abatementString`) |
| `Condition.recordedDate` | Σ | 0..1 | dateTime | Date record was first recorded |
| `Condition.recorder` | Σ | 0..1 | Reference(Practitioner \| PractitionerRole \| Patient \| RelatedPerson) | Who recorded the condition |
| `Condition.asserter` | Σ | 0..1 | Reference(Practitioner \| PractitionerRole \| Patient \| RelatedPerson) | Person who asserts this condition |
| `Condition.stage` | I | 0..* | BackboneElement | Stage/grade, usually assessed formally + Rule con-1 |
| `Condition.stage.summary` | I | 0..1 | CodeableConcept | Simple summary (disease specific); Condition Stage (Example) |
| `Condition.stage.assessment` | I | 0..* | Reference(ClinicalImpression \| DiagnosticReport \| Observation) | Formal record of assessment |
| `Condition.stage.type` |  | 0..1 | CodeableConcept | Kind of staging; Condition Stage Type (Example) |
| `Condition.evidence` | I | 0..* | BackboneElement | Supporting evidence + Rule con-2 |
| `Condition.evidence.code` | ΣI | 0..* | CodeableConcept | Manifestation/symptom; Manifestation and Symptom Codes (Example) |
| `Condition.evidence.detail` | ΣI | 0..* | Reference(Any) | Supporting information found elsewhere |
| `Condition.note` |  | 0..* | Annotation | Additional information about the Condition |

### Terminology bindings (as printed)
| Path | Strength | Value set |
|---|---|---|
| `Condition.clinicalStatus` | Required | ConditionClinicalStatusCodes (`http://terminology.hl7.org/CodeSystem/condition-clinical` in con-4) |
| `Condition.verificationStatus` | Required | ConditionVerificationStatus (`http://terminology.hl7.org/CodeSystem/condition-ver-status` in con-3/5) |
| `Condition.category` | Extensible | ConditionCategoryCodes |
| `Condition.severity` | Preferred | Condition/DiagnosisSeverity |
| `Condition.code` | Example | Condition/Problem/DiagnosisCodes |
| `Condition.bodySite` | Example | SNOMEDCTBodyStructures |
| `Condition.stage.summary` | Example | ConditionStage |
| `Condition.stage.type` | Example | ConditionStageType |
| `Condition.evidence.code` | Example | ManifestationAndSymptomCodes |

## Search parameters
| Name | Type | Expression |
|---|---|---|
| abatement-date | date | `Condition.abatement.as(dateTime) \| Condition.abatement.as(Period)` |
| abatement-string | string | `Condition.abatement.as(string)` |
| asserter | reference | `Condition.asserter` (Practitioner, Patient, PractitionerRole, RelatedPerson) |
| body-site | token | `Condition.bodySite` |
| category | token | `Condition.category` |
| clinical-status | token | `Condition.clinicalStatus` |
| code | token | `Condition.code` (13 Resources) |
| encounter | reference | `Condition.encounter` (Encounter) |
| evidence | token | `Condition.evidence.code` |
| evidence-detail | reference | `Condition.evidence.detail` (Any) |
| identifier | token | `Condition.identifier` (30 Resources) |
| onset-age | quantity | `Condition.onset.as(Age) \| Condition.onset.as(Range)` |
| onset-date | date | `Condition.onset.as(dateTime) \| Condition.onset.as(Period)` |
| onset-info | string | `Condition.onset.as(string)` |
| patient | reference | `Condition.subject.where(resolve() is Patient)` (Patient) (33 Resources) |
| recorded-date | date | `Condition.recordedDate` |
| severity | token | `Condition.severity` |
| stage | token | `Condition.stage.summary` |
| subject | reference | `Condition.subject` (Group, Patient) |
| verification-status | token | `Condition.verificationStatus` — unconfirmed \| provisional \| differential \| confirmed \| refuted \| entered-in-error |

## Invariants / constraints
- con-1 (Rule, `Condition.stage`): Stage SHALL have summary or assessment — `summary.exists() or assessment.exists()`
- con-2 (Rule, `Condition.evidence`): evidence SHALL have code or details — `code.exists() or detail.exists()`
- con-3 (**Guideline**, base): Condition.clinicalStatus SHALL be present if verificationStatus is not entered-in-error and category is problem-list-item — `clinicalStatus.exists() or verificationStatus.coding.where(system='http://terminology.hl7.org/CodeSystem/condition-ver-status' and code = 'entered-in-error').exists() or category.select($this='problem-list-item').empty()`. Page: "(only) a best practice guideline because: Most systems will expect a clinicalStatus to be valued for problem-list-items that are managed over time, but might not need a clinicalStatus for point in time encounter-diagnosis."
- con-4 (Rule, base): If condition is abated, then clinicalStatus must be either inactive, resolved, or remission — `abatement.empty() or clinicalStatus.coding.where(system='http://terminology.hl7.org/CodeSystem/condition-clinical' and (code='resolved' or code='remission' or code='inactive')).exists()`
- con-5 (Rule, base): Condition.clinicalStatus SHALL NOT be present if verification Status is entered-in-error — `verificationStatus.coding.where(system='http://terminology.hl7.org/CodeSystem/condition-ver-status' and code='entered-in-error').empty() or clinicalStatus.empty()`

## Relationships
- references: Patient, Group (`subject`); Encounter; Practitioner, PractitionerRole, Patient, RelatedPerson (`recorder`, `asserter`); ClinicalImpression, DiagnosticReport, Observation (`stage.assessment`); Any (`evidence.detail`).
- referenced by: AdverseEvent, Appointment, CarePlan, CareTeam, Claim, ClinicalImpression, Communication, CommunicationRequest, Contract, CoverageEligibilityRequest, DeviceRequest, DeviceUseStatement, Encounter, EpisodeOfCare, ExplanationOfBenefit, FamilyMemberHistory, Goal, GuidanceResponse, ImagingStudy, Immunization, MedicationAdministration, MedicationRequest, MedicationStatement, Procedure, RequestGroup, RiskAssessment, ServiceRequest and SupplyRequest.
- Boundaries: Condition is referenced as the "reason" for MedicationRequest / Procedure / ServiceRequest; signs and symptoms are Observations — use Observation "when a symptom is resolved without long term management" or "contributes to the establishment of a condition", Condition "when a symptom requires long term management, tracking, or is used as a proxy for a diagnosis"; allergies need AllergyIntolerance to be actionable. Known issue: circular references with ClinicalImpression.

## Usage rules stated on the page (§9.2.3.3–9.2.3.10)
| Topic | As stated |
|---|---|
| `code` | May encode stage, location or causality (esp. SNOMED CT); may express "history of X", "good health", "risk of", "fear of", "no known problems", negations; when `code` carries such properties, the other elements are left empty and "the value must be understood from the Condition.code" |
| Not reviewed / not asked | Use `List.emptyReason.code = "notasked"` |
| Reviewed, none identified | `List.emptyReason`, or preferably a "no known problems" code (SNOMED CT 160245001) so the data stays queryable in Condition; remove the negation record when a real condition is added (Trial-Use note: feedback sought on the preferred approach) |
| Patient denies | Annotate in `note` |
| Absence assertions | Only a `refuted` Condition when a prior belief was disproved; pre-admission checklist answers ("are you pregnant") go in QuestionnaireResponse or Observation, NOT Condition |
| `evidence` | "provides the basis for whatever is present in Condition.code" |
| `abatementRange` | Age period of the subject at abatement |
| `asserter` vs data enterer | A nurse entering for a physician → Provenance on the Condition; `asserter` = the physician taking responsibility |
| `clinicalStatus` ↔ `stage` | May be interdependent (cancer stage differs in remission) |
| Role / rank in an Encounter | Use `Encounter.diagnosis.role` (the Encounter table names it `use`) and `Encounter.diagnosis.rank` for admission/discharge role and primary/secondary rank — not Condition |

## Notes for our server
- Only `subject` (1..1) is mandatory in base R4; `code` is 0..1 — the SATUSEHAT profile (satusehat-condition.md) makes `code` (one ICD-10 coding), `subject` and `encounter` wajib, so our profile sets `code` 1..1 and `encounter` 1..1 and restricts `subject` to `Reference(Patient)`.
- Enforce con-1, con-2, con-4, con-5 as hard rules; treat con-3 as a warning (`OperationOutcome.issue.severity = warning`) since the page marks it a Guideline and encounter-diagnoses may legitimately omit `clinicalStatus`.
- `clinicalStatus` and `verificationStatus` are modifier elements (`?!`): hide `verificationStatus = entered-in-error` and `refuted` from the patient-facing diagnosis list; `category = encounter-diagnosis` is what the outpatient flow records, `problem-list-item` for ongoing problems.
- Doctor workflow: POST Condition (`category = encounter-diagnosis`, `code` ICD-10, `subject`, `encounter`, `recordedDate`, `asserter = Practitioner/…`), then PUT the Encounter adding `diagnosis.condition` + `rank` — role/rank never live on the Condition.
- Search index: `patient`/`subject`, `encounter`, `code`, `category`, `clinical-status`, `verification-status`, `onset-date`, `recorded-date`, `asserter`, `identifier`; Condition is in the Patient and Encounter compartments, so `Patient/[id]/Condition` and `Encounter/[id]/Condition` must resolve.
- Do not store "patient has no diagnosis" as an empty Condition; if needed, use the SNOMED "no known problems" code or a List with `emptyReason`.

## Sources
- raw/fhir-r4/condition.md

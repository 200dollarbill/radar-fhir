# FHIR R4 — Encounter

Purpose: "An interaction between a patient and healthcare provider(s) for the purpose of providing healthcare service(s) or assessing the health status of a patient." Trial Use, maturity 2, security category Patient, compartments Encounter / Patient / Practitioner / RelatedPerson. Covers pre-admission, the actual encounter (ambulatory) and admission/stay/discharge (inpatient); `class` distinguishes the setting and "is required"; admission-related detail lives in the `hospitalization` component; encounters nest via `partOf`. Flags: `Σ` summary, `?!` modifier, `TU` trial use.

## Elements (summary table)
Root `Encounter` (TU) is a DomainResource. No constraints table is printed on the page.

| Element | Flags | Card. | Type | Notes |
|---|---|---|---|---|
| `Encounter.identifier` | Σ | 0..* | Identifier | Identifier(s) by which this encounter is known |
| `Encounter.status` | ?!Σ | 1..1 | code | planned \| arrived \| triaged \| in-progress \| onleave \| finished \| cancelled +; EncounterStatus (Required) |
| `Encounter.statusHistory` |  | 0..* | BackboneElement | List of past encounter statuses |
| `Encounter.statusHistory.status` |  | 1..1 | code | same value set as `status`; EncounterStatus (Required) |
| `Encounter.statusHistory.period` |  | 1..1 | Period | The time that the episode was in the specified status |
| `Encounter.class` | Σ | 1..1 | Coding | Classification of patient encounter; V3 Value Set ActEncounterCode (Extensible) |
| `Encounter.classHistory` |  | 0..* | BackboneElement | List of past encounter classes |
| `Encounter.classHistory.class` |  | 1..1 | Coding | inpatient \| outpatient \| ambulatory \| emergency +; V3 Value Set ActEncounterCode (Extensible) |
| `Encounter.classHistory.period` |  | 1..1 | Period | The time that the episode was in the specified class |
| `Encounter.type` | Σ | 0..* | CodeableConcept | Specific type of encounter; Encounter type (Example) |
| `Encounter.serviceType` | Σ | 0..1 | CodeableConcept | Specific type of service; Service type (Example) |
| `Encounter.priority` |  | 0..1 | CodeableConcept | Indicates the urgency of the encounter; v3 ActPriority (Example) |
| `Encounter.subject` | Σ | 0..1 | Reference(Patient \| Group) | The patient or group present at the encounter |
| `Encounter.episodeOfCare` | Σ | 0..* | Reference(EpisodeOfCare) | Episode(s) of care that this encounter should be recorded against |
| `Encounter.basedOn` |  | 0..* | Reference(ServiceRequest) | The ServiceRequest that initiated this encounter |
| `Encounter.participant` | Σ | 0..* | BackboneElement | List of participants involved in the encounter |
| `Encounter.participant.type` | Σ | 0..* | CodeableConcept | Role of participant in encounter; Participant type (Extensible) |
| `Encounter.participant.period` |  | 0..1 | Period | Period of time during the encounter that the participant participated |
| `Encounter.participant.individual` | Σ | 0..1 | Reference(Practitioner \| PractitionerRole \| RelatedPerson) | Persons involved in the encounter other than the patient |
| `Encounter.appointment` | Σ | 0..* | Reference(Appointment) | The appointment that scheduled this encounter |
| `Encounter.period` |  | 0..1 | Period | The start and end time of the encounter |
| `Encounter.length` |  | 0..1 | Duration | Quantity of time the encounter lasted (less time absent) |
| `Encounter.reasonCode` | Σ | 0..* | CodeableConcept | Coded reason the encounter takes place; Encounter Reason Codes (Preferred) |
| `Encounter.reasonReference` | Σ | 0..* | Reference(Condition \| Procedure \| Observation \| ImmunizationRecommendation) | Reason the encounter takes place (reference) |
| `Encounter.diagnosis` | Σ | 0..* | BackboneElement | The list of diagnosis relevant to this encounter |
| `Encounter.diagnosis.condition` | Σ | 1..1 | Reference(Condition \| Procedure) | The diagnosis or procedure relevant to the encounter |
| `Encounter.diagnosis.use` |  | 0..1 | CodeableConcept | Role that this diagnosis has within the encounter (e.g. admission, billing, discharge …); DiagnosisRole (Preferred) |
| `Encounter.diagnosis.rank` |  | 0..1 | positiveInt | Ranking of the diagnosis (for each role type) |
| `Encounter.account` |  | 0..* | Reference(Account) | The set of accounts that may be used for billing for this Encounter |
| `Encounter.hospitalization` |  | 0..1 | BackboneElement | Details about the admission to a healthcare service |
| `Encounter.hospitalization.preAdmissionIdentifier` |  | 0..1 | Identifier | Pre-admission identifier |
| `Encounter.hospitalization.origin` |  | 0..1 | Reference(Location \| Organization) | The location/organization from which the patient came before admission |
| `Encounter.hospitalization.admitSource` |  | 0..1 | CodeableConcept | From where patient was admitted (physician referral, transfer); Admit source (Preferred) |
| `Encounter.hospitalization.reAdmission` |  | 0..1 | CodeableConcept | Type of hospital re-admission (if any); absent = not a readmission; v2 RE-ADMISSION INDICATOR (Example) |
| `Encounter.hospitalization.dietPreference` |  | 0..* | CodeableConcept | Diet preferences reported by the patient; Diet (Example) |
| `Encounter.hospitalization.specialCourtesy` |  | 0..* | CodeableConcept | Special courtesies (VIP, board member); Special courtesy (Preferred) |
| `Encounter.hospitalization.specialArrangement` |  | 0..* | CodeableConcept | Wheelchair, translator, stretcher, etc.; Special arrangements (Preferred) |
| `Encounter.hospitalization.destination` |  | 0..1 | Reference(Location \| Organization) | Location/organization to which the patient is discharged |
| `Encounter.hospitalization.dischargeDisposition` |  | 0..1 | CodeableConcept | Category or kind of location after discharge; Discharge disposition (Example) |
| `Encounter.location` |  | 0..* | BackboneElement | List of locations where the patient has been |
| `Encounter.location.location` |  | 1..1 | Reference(Location) | Location the encounter takes place |
| `Encounter.location.status` |  | 0..1 | code | planned \| active \| reserved \| completed; EncounterLocationStatus (Required) |
| `Encounter.location.physicalType` |  | 0..1 | CodeableConcept | Physical type of the location (usually the level in the hierarchy — bed, room, ward etc.); Location type (Example) |
| `Encounter.location.period` |  | 0..1 | Period | Time period during which the patient was present at the location |
| `Encounter.serviceProvider` |  | 0..1 | Reference(Organization) | The organization (facility) responsible for this encounter |
| `Encounter.partOf` |  | 0..1 | Reference(Encounter) | Another Encounter this encounter is part of |

### Terminology bindings (as printed)
| Path | Strength | Value set |
|---|---|---|
| `Encounter.status`, `Encounter.statusHistory.status` | Required | EncounterStatus |
| `Encounter.class`, `Encounter.classHistory.class` | Extensible | v3.ActEncounterCode |
| `Encounter.type` | Example | EncounterType |
| `Encounter.serviceType` | Example | ServiceType |
| `Encounter.priority` | Example | v3.ActPriority |
| `Encounter.participant.type` | Extensible | ParticipantType |
| `Encounter.reasonCode` | Preferred | EncounterReasonCodes |
| `Encounter.diagnosis.use` | Preferred | DiagnosisRole |
| `Encounter.hospitalization.admitSource` | Preferred | AdmitSource |
| `Encounter.hospitalization.reAdmission` | Example | v2.0092 |
| `Encounter.hospitalization.dietPreference` | Example | Diet |
| `Encounter.hospitalization.specialCourtesy` | Preferred | SpecialCourtesy |
| `Encounter.hospitalization.specialArrangement` | Preferred | SpecialArrangements |
| `Encounter.hospitalization.dischargeDisposition` | Example | DischargeDisposition |
| `Encounter.location.status` | Required | EncounterLocationStatus |
| `Encounter.location.physicalType` | Example | LocationType |

## Search parameters
| Name | Type | Expression |
|---|---|---|
| appointment | reference | `Encounter.appointment` (Appointment) |
| based-on | reference | `Encounter.basedOn` (ServiceRequest) |
| class | token | `Encounter.class` |
| date | date | `Encounter.period` — "a date within the period the Encounter lasted" (17 Resources) |
| diagnosis | reference | `Encounter.diagnosis.condition` (Condition, Procedure) |
| episode-of-care | reference | `Encounter.episodeOfCare` (EpisodeOfCare) |
| identifier | token | `Encounter.identifier` (30 Resources) |
| length | quantity | `Encounter.length` — "Length of encounter in days" |
| location | reference | `Encounter.location.location` (Location) |
| location-period | date | `Encounter.location.period` |
| part-of | reference | `Encounter.partOf` (Encounter) |
| participant | reference | `Encounter.participant.individual` (Practitioner, PractitionerRole, RelatedPerson) |
| participant-type | token | `Encounter.participant.type` |
| patient | reference | `Encounter.subject.where(resolve() is Patient)` (Patient) (33 Resources) |
| practitioner | reference | `Encounter.participant.individual.where(resolve() is Practitioner)` (Practitioner) |
| reason-code | token | `Encounter.reasonCode` |
| reason-reference | reference | `Encounter.reasonReference` (Condition, Observation, Procedure, ImmunizationRecommendation) |
| service-provider | reference | `Encounter.serviceProvider` (Organization) |
| special-arrangement | token | `Encounter.hospitalization.specialArrangement` |
| status | token | `Encounter.status` — planned \| arrived \| triaged \| in-progress \| onleave \| finished \| cancelled + |
| subject | reference | `Encounter.subject` (Group, Patient) |
| type | token | `Encounter.type` (5 Resources) |

## Invariants / constraints
- None printed (the page has no Constraints table).

## Relationships
- references: Patient, Group (`subject`); EpisodeOfCare; ServiceRequest (`basedOn`); Practitioner, PractitionerRole, RelatedPerson (`participant.individual`); Appointment; Condition, Procedure, Observation, ImmunizationRecommendation (`reasonReference`); Condition, Procedure (`diagnosis.condition`); Account; Location, Organization (`hospitalization.origin`/`destination`); Location (`location.location`); Organization (`serviceProvider`); Encounter (`partOf`).
- referenced by: AdverseEvent, AllergyIntolerance, CarePlan, CareTeam, ChargeItem, Claim, ClinicalImpression, Communication, CommunicationRequest, Composition, Condition, Contract, DeviceRequest, DiagnosticReport, DocumentReference, itself, ExplanationOfBenefit, Flag, GuidanceResponse, ImagingStudy, Immunization, List, Media, MedicationAdministration, MedicationDispense, MedicationRequest, MedicationStatement, NutritionOrder, Observation, Procedure, QuestionnaireResponse, RequestGroup, RiskAssessment, ServiceRequest, Task and VisionPrescription.
- Boundaries: Appointment holds scheduling; Encounter is "the patient showing up" — a `planned` Encounter is not the Appointment; Communication is for non-contact interactions; Procedure ↔ Encounter references should point to *different* procedures (`Procedure.encounter` for the one performed during the visit, `Encounter.indication` — as the page names it — for a follow-up visit caused by an earlier procedure); resources without an encounter element use the standard extension "Associated Encounter".

## Status and lifecycle rules (page §8.11.1.1, §8.11.5)
| Rule | As stated |
|---|---|
| Typical order | planned → in-progress → finished/cancelled; pre-admission instances use `status = planned` |
| `statusHistory` | Included so the status timeline can be read without scanning resource versions "or where a system doesn't support resource histories" |
| Admitted? | Not derivable from `status` alone; "arrived", "triaged" or "in progress" could be the start of admission; "At a minimum, we do believe that a patient IS admitted when the status is in-progress" |
| `hospitalization` | Always the same period as the encounter; a different period → another Encounter `partOf` this one |
| `class` | Required because it selects the business rules/validation for the setting |
| Nesting | One overarching Encounter per stay; location moves and short team visits may be separate Encounters `partOf` the overarching one; profiles are expected to limit this flexibility per use case |

## Notes for our server
- Mandatory on POST: `status` (1..1, Required binding) and `class` (1..1 `Coding`, Extensible v3 ActEncounterCode) — reject otherwise. Every nested BackboneElement has its own 1..1 leaf: `statusHistory.status`+`period`, `classHistory.class`+`period`, `diagnosis.condition`, `location.location` — validate those when the parent is present.
- `status` is a modifier element (`?!`); implement the transition planned/arrived → in-progress → finished as server-side state, and append a `statusHistory` entry (with a closed `period`) on every transition instead of relying on `_history` — the page explicitly offers `statusHistory` for servers without version history. SATUSEHAT's arrived → in-progress → finished flow (satusehat-encounter.md) is a subset of this value set.
- `subject` is only 0..1 in base R4 and can be a Group; our profile should force `Reference(Patient)` 1..1, plus `serviceProvider` (Organization) and `location.location` 1..*, matching the SATUSEHAT wajib list.
- Encounter is the reference hub: Observation.encounter, Condition.encounter, Procedure.encounter all point here; `diagnosis.condition` + `diagnosis.use`/`rank` is where the doctor role records the visit's diagnoses (Condition first, then PUT the Encounter).
- Search index: `patient`/`subject`, `status`, `class`, `date` (period-aware), `identifier`, `service-provider`, `location`, `participant`/`practitioner` (for the doctor's worklist), `part-of`, `diagnosis`, `type`. `length` is a quantity parameter "in days".
- Patient role reads its own Encounters via compartment `Patient/[id]/Encounter` (Encounter is in the Patient compartment); doctor role via `practitioner=` on `participant.individual`.

## Sources
- raw/fhir-r4/encounter.md

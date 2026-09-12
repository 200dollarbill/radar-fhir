# FHIR R4 — Workflow patterns and the Clinical Module

Summary: the `workflow` page (FHIR Infrastructure WG, maturity 2, Trial Use) "defines three categories of resources that are involved in activities - requests, events and definitions", each with a "pattern" of standard elements that resources "are encouraged to adhere to" ("Strict adherence is not required"). FHIR "does not need to be used for the execution of workflow" — the patterns standardise the *data elements* that link orders, results and protocols even when the process is driven outside FHIR. The `clinicalsummary-module` page (Patient Care WG, Informative) is the index of the Clinical Module (core clinical resources incl. Condition and Procedure; Observation belongs to the Diagnostics Module).

## The three patterns (`workflow` §12.5.1.3–12.5.1.5)
| Category | Definition as printed | Pattern note |
|---|---|---|
| Definitions | "Resources that define something that can potentially happen in a patient and time-independent manner" — "activities that could be performed in a time and subject-independent manner such as a protocol, order set, clinical guideline, etc." | Definition pattern = common elements of definition resources |
| Requests | "Resources that ask for or express a desire/intention for something to be done" — "the proposal, plan or order for an activity to occur" | "All requests with an intent of 'order' authorize something"; a request may not be "fully specified" (e.g. MedicationRequest without strength/route); its existence "doesn't necessarily imply that fulfillment will be requested immediately - or even ever" |
| Events | "Resources that express that something has been done and which can potentially be done because of a request" — "the ongoing or completed execution of some activity or observation. For example, a clinical procedure, a financial transaction, the recording of a diagnosis, etc." | Event pattern = common elements of event resources |

Workflow definition is handled by a pair of resources: `PlanDefinition` ("the interrelationships of steps and the rules around their execution") and `ActivityDefinition` ("an activity to be performed as a single step"). Execution is supported by REST, Messaging and Services; "The Document paradigm does not directly support driving behavior".

## Which resources fall where (`workflow` §12.5.1.1, as the page's lists state)
| Category | Resources listed on the page |
|---|---|
| Definitions (5) | ActivityDefinition, Measure, OperationDefinition, PlanDefinition, Questionnaire |
| Requests (16) | Appointment\*, AppointmentResponse\*, CarePlan, Claim, CommunicationRequest, Contract, CoverageEligibilityRequest, DeviceRequest, EnrollmentRequest, ImmunizationRecommendation, MedicationRequest, NutritionOrder, ServiceRequest, Task‡, SupplyRequest, VisionPrescription |
| Events (34) | ChargeItem, ClaimResponse, ClinicalImpression, Communication, Composition, **Condition** (aka Problem), Consent, Coverage, CoverageEligibilityResponse, DeviceUseStatement, DiagnosticReport, DocumentManifest, DocumentReference, **Encounter**, EnrollmentResponse, EpisodeOfCare, ExplanationOfBenefit, FamilyMemberHistory, GuidanceResponse, ImagingStudy, Immunization, MeasureReport, Media, MedicationAdministration, MedicationDispense, MedicationStatement, **Observation**, PaymentNotice, PaymentReconciliation, **Procedure**, QuestionnaireResponse, RiskAssessment, SupplyDelivery, Task‡ |

\* "The Appointment and AppointmentResponse resources do not follow the same sort of request/response pattern … Their design is based on iCal conventions". ‡ "The Task resource takes on characteristics of both 'requests' and 'events'".

Our resources against these lists:
| Resource | Category on the page | Confirmed on its own page |
|---|---|---|
| Observation | Event | "This resource is an *event resource* from a FHIR workflow perspective" (`observation`) |
| Procedure | Event | "Procedure is one of the event resources in the FHIR workflow specification" (`procedure`) |
| Condition | Event (aka Problem) | "Condition is one of the event resources in the FHIR workflow specification" (`condition`) |
| Encounter | Event | listed only on the workflow page |
| Device, DeviceMetric, DeviceDefinition, Patient, Practitioner, PractitionerRole, Organization, Location, RelatedPerson, Person | **not in any list** — "many are used to describe entities and roles (patients, medications, etc.) or infrastructure" and are "not … related to workflow" | — |
| DeviceRequest | Request | (request for a device; not in our scope) |
| DeviceUseStatement | Event | (not in our scope) |

Pairings (§12.5.1.1): "requests, events and definitions don't exist in a 1:1:1 relationship" — SupplyRequest ↔ SupplyDelivery, EnrollmentRequest ↔ EnrollmentResponse pair obviously; "A ServiceRequest might be responded to by an Encounter, DiagnosticReport, Procedure, RiskAssessment, etc. Similarly, a Procedure might be triggered by a ServiceRequest." The response types "will be governed by the Request.code, any workflow definitions/protocols referenced and local convention".

## Standard relationships (`workflow` §12.5.1.2)
The page lists four standardised relationships (not exhaustive):
| Relationship as printed | Elements that realise it on our resources (from the resource pages) |
|---|---|
| "requests, events and definitions can point to their respective definitions" | `Procedure.instantiatesCanonical` 0..\* canonical(PlanDefinition \| ActivityDefinition \| Measure \| OperationDefinition \| Questionnaire), `Procedure.instantiatesUri` 0..\* uri; Observation, Condition, Encounter have no `instantiates*` element |
| "events and requests can point to the proposals, plans or orders they are based on" | `Observation.basedOn` 0..\* Reference(CarePlan \| DeviceRequest \| ImmunizationRecommendation \| MedicationRequest \| NutritionOrder \| ServiceRequest); `Procedure.basedOn` 0..\* Reference(CarePlan \| ServiceRequest); `Encounter.basedOn` 0..\* Reference(ServiceRequest); Condition has no `basedOn` |
| "events and definitions can be organized into parent-child relationships of parents and components" | `Observation.partOf` 0..\* Reference(MedicationAdministration \| MedicationDispense \| MedicationStatement \| Procedure \| Immunization \| ImagingStudy); `Procedure.partOf` 0..\* Reference(Procedure \| Observation \| MedicationAdministration); `Encounter.partOf` 0..1 Reference(Encounter); Condition has no `partOf` |
| "definitions and requests can both replace prior versions of the same type of artifact" | none of our event resources carry a `replaces` element |

Element-level linkage rules recorded on the resource pages (`observation`, `procedure`, `encounter`, `condition`; see the per-resource views for context):
| Element | Card. | Type / rule |
|---|---|---|
| `Observation.focus` (TU) | 0..\* | Reference(Any) — "What the observation is about, when it is not about the subject of record" |
| `Observation.hasMember` | 0..\* | Reference(Observation \| QuestionnaireResponse \| MolecularSequence) — group/panel members |
| `Observation.derivedFrom` | 0..\* | Reference(DocumentReference \| ImagingStudy \| Media \| QuestionnaireResponse \| Observation \| MolecularSequence) — source measurements |
| `Observation.encounter` / `Procedure.encounter` / `Condition.encounter` | 0..1 | Reference(Encounter) — the event's healthcare-event context ("Encounter created as part of") |
| `Procedure.reasonReference` | 0..\* | Reference(Condition \| Observation \| Procedure \| DiagnosticReport \| DocumentReference) |
| `Encounter.reasonReference` | 0..\* | Reference(Condition \| Procedure \| Observation \| ImmunizationRecommendation) |
| `Procedure.recorder` / `asserter`, `Condition.recorder` / `asserter` | 0..1 | Reference(Patient \| RelatedPerson \| Practitioner \| PractitionerRole) |

The generic Request/Event/Definition pattern element tables (`Request.basedOn`, `Event.partOf`, `Definition.derivedFromCanonical` …) are on separate pattern pages that were not scraped — n/s here; the `workflow` page itself only states the four relationship sentences above. `focus` is not mentioned on the workflow page.

## Open issues on the page (§12.5.2, STU Notes)
- MessageHeader portions could be replaced by a reference to Task (consistency of asynchronous requests across REST and messaging vs added complexity).
- Whether OperationDefinition should define task types and their parameter sets.
- "The SupplyRequest, DeviceRequest and VisionPrescription resources have a significant degree of overlap. Should they remain distinct resources?"

## Clinical Module (`clinicalsummary-module` §9.0)
| Item | What the page states |
|---|---|
| Scope | "the FHIR Resources that represent core clinical information for a patient … frequently documented, created or retrieved by healthcare providers during the course of clinical care"; diagnostic-study resources are in the Diagnostics Module; medication ordering/administration in the Medications Module |
| Index (11) | AllergyIntolerance, Condition (Problem), Procedure, FamilyMemberHistory; CarePlan, Goal, CareTeam, ClinicalImpression; AdverseEvent, DetectedIssue, RiskAssessment (the ClinicalImpression tooltip: assessments "are often 1:1 with a clinical consultation / encounter, but this varies greatly"; named ClinicalImpression "to avoid confusion with the recording of assessment tools such as Apgar score") |
| Complexity advice | start with "lower complexity, core Resources such as Patient, Condition, and FamilyMemberHistory before addressing a high complexity Resource such as CarePlan" |
| Security | "The clinical resources often represent patient-related data, and as such are susceptible to data breaching. Necessary privacy and security provision must be in place for searching and fetching this information" (→ fhir-security.md) |
| Common use cases | "Documenting a patient's condition" — Condition "is used extensively throughout FHIR Resources to associate information and activities with specific conditions" and "is broadly defined to include problems, diagnoses and health concerns"; "Retrieving the patient's problems"; allergies (AllergyIntolerance, incl. absence of an allergy); Family History (pedigrees); Care Plans — "a problem based care plan with references to other Resources including CareTeam, Condition, Goal, and activities such as ServiceRequest" |
| Roadmap | more widespread implementation of core resources such as Condition; CarePlan matures more gradually; ServiceRequest needs clinician use cases |

What the module says about Condition / Procedure / Observation together: Condition and Procedure are both Clinical-Module index resources; Observation is *not* in this module (diagnostic studies → Diagnostics Module) and the page does not describe an Observation–Condition–Procedure relationship. The only cross-links the page states are Condition as the anchor other resources "associate information and activities with", and CarePlan referencing Condition, Goal, CareTeam and ServiceRequest. Linkages between the three come from their own pages: `Procedure.reasonReference → Condition | Observation`, `Procedure.partOf → Observation`, `Observation.partOf → Procedure`, `Encounter.reasonReference → Condition | Procedure | Observation`, and `Encounter.diagnosis.condition` (see fhir-encounter.md, fhir-condition.md).

## Notes for our server
- Model the visit as event resources only: Encounter (hub) ← Observation / Condition / Procedure via their `encounter` 0..1 reference; we need no Request or Definition resources for the admin/doctor/patient scope, and Device/Patient/Practitioner/Organization/Location are entity resources outside the workflow patterns.
- Device-sourced vital signs: `Observation.device` (fhir-observation.md) plus optional `Observation.basedOn → DeviceRequest` only if we later add ordering; `Observation.partOf → Procedure` when a reading is taken during a recorded procedure; `hasMember` for panels, `derivedFrom` for computed values (e.g. BMI).
- Doctor flow: Condition first (`encounter`, `asserter`), then Procedure with `reasonReference → Condition/…` and `encounter`, then PUT Encounter adding `diagnosis.condition`/`reasonReference`; validate that every `encounter`, `partOf`, `basedOn`, `reasonReference` target exists (reference resolution per fhir-datamodel-basics.md).
- Keep `Encounter.partOf` 0..1 (single parent) and `Observation.focus` unused unless a reading is about something other than the patient (e.g. a device self-test) — it is TU.
- Clinical-module security note applies: every search/fetch of Condition, Procedure, Observation is PHI — role checks and audit per fhir-security.md.

## Sources
- raw/fhir-r4/workflow.md
- raw/fhir-r4/clinicalsummary-module.md
- raw/fhir-r4/observation.md
- raw/fhir-r4/procedure.md
- raw/fhir-r4/encounter.md
- raw/fhir-r4/condition.md

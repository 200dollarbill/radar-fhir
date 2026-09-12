# FHIR R4 — Patient, Person, RelatedPerson

Purpose: `Patient` = "Demographics and other administrative information about an individual or animal receiving care or other health-related services" (Normative from v4.0.0, security category Patient, compartments Patient / Practitioner / RelatedPerson). `Person` = "A generic person record" that links Patient / Practitioner / RelatedPerson / Person instances believed to be the same individual (Trial Use, maturity 2; "an advanced feature"). `RelatedPerson` = "A person that is related to a patient, but who is not a direct target of care", used "primarily for attribution of information" (Trial Use, maturity 2, compartments Patient / RelatedPerson). Flags: `Σ` summary, `?!` modifier, `I` invariant, `N` normative, `TU` trial use.

## Patient — elements
Root `Patient` (N) is a DomainResource.

| Element | Flags | Card. | Type | Notes |
|---|---|---|---|---|
| `Patient.identifier` | Σ | 0..* | Identifier | An identifier for this patient |
| `Patient.active` | ?!Σ | 0..1 | boolean | Whether this patient's record is in active use |
| `Patient.name` | Σ | 0..* | HumanName | A name associated with the patient |
| `Patient.telecom` | Σ | 0..* | ContactPoint | A contact detail for the individual |
| `Patient.gender` | Σ | 0..1 | code | male \| female \| other \| unknown; AdministrativeGender (Required) |
| `Patient.birthDate` | Σ | 0..1 | date | The date of birth for the individual |
| `Patient.deceased[x]` | ?!Σ | 0..1 | boolean \| dateTime | Indicates if the individual is deceased or not (`deceasedBoolean`, `deceasedDateTime`) |
| `Patient.address` | Σ | 0..* | Address | An address for the individual |
| `Patient.maritalStatus` |  | 0..1 | CodeableConcept | Marital (civil) status of a patient; MaritalStatus (Extensible) |
| `Patient.multipleBirth[x]` |  | 0..1 | boolean \| integer | Whether patient is part of a multiple birth (`multipleBirthBoolean`, `multipleBirthInteger` = birth order) |
| `Patient.photo` |  | 0..* | Attachment | Image of the patient |
| `Patient.contact` | I | 0..* | BackboneElement | A contact party (e.g. guardian, partner, friend) for the patient + Rule pat-1 |
| `Patient.contact.relationship` |  | 0..* | CodeableConcept | The kind of relationship; Patient Contact Relationship (Extensible) |
| `Patient.contact.name` |  | 0..1 | HumanName | A name associated with the contact person |
| `Patient.contact.telecom` |  | 0..* | ContactPoint | A contact detail for the person |
| `Patient.contact.address` |  | 0..1 | Address | Address for the contact person |
| `Patient.contact.gender` |  | 0..1 | code | male \| female \| other \| unknown; AdministrativeGender (Required) |
| `Patient.contact.organization` | I | 0..1 | Reference(Organization) | Organization that is associated with the contact |
| `Patient.contact.period` |  | 0..1 | Period | Period during which this contact is valid to be contacted relating to this patient |
| `Patient.communication` |  | 0..* | BackboneElement | A language which may be used to communicate with the patient about his or her health |
| `Patient.communication.language` |  | 1..1 | CodeableConcept | The language; Common Languages (Preferred but limited to AllLanguages) |
| `Patient.communication.preferred` |  | 0..1 | boolean | Language preference indicator |
| `Patient.generalPractitioner` |  | 0..* | Reference(Organization \| Practitioner \| PractitionerRole) | Patient's nominated primary care provider |
| `Patient.managingOrganization` | Σ | 0..1 | Reference(Organization) | Organization that is the custodian of the patient record |
| `Patient.link` | ?!Σ | 0..* | BackboneElement | Link to another patient resource that concerns the same actual person |
| `Patient.link.other` | Σ | 1..1 | Reference(Patient \| RelatedPerson) | The other patient or related person resource that the link refers to |
| `Patient.link.type` | Σ | 1..1 | code | replaced-by \| replaces \| refer \| seealso; LinkType (Required) |

Bindings: `gender`/`contact.gender` Required AdministrativeGender; `maritalStatus` Extensible Marital Status Codes; `contact.relationship` Extensible PatientContactRelationship; `communication.language` Preferred (limited to AllLanguages) CommonLanguages; `link.type` Required LinkType.

### Patient — search parameters (all `TU`)
| Name | Type | Expression |
|---|---|---|
| active | token | `Patient.active` |
| address | string | `Patient.address` — may match any string field of the Address (3 Resources) |
| address-city | string | `Patient.address.city` |
| address-country | string | `Patient.address.country` |
| address-postalcode | string | `Patient.address.postalCode` |
| address-state | string | `Patient.address.state` |
| address-use | token | `Patient.address.use` |
| birthdate | date | `Patient.birthDate` (2 Resources) |
| death-date | date | `(Patient.deceased as dateTime)` |
| deceased | token | `Patient.deceased.exists() and Patient.deceased != false` |
| email | token | `Patient.telecom.where(system='email')` (4 Resources) |
| family | string | `Patient.name.family` |
| gender | token | `Patient.gender` (3 Resources) |
| general-practitioner | reference | `Patient.generalPractitioner` (Practitioner, Organization, PractitionerRole) |
| given | string | `Patient.name.given` |
| identifier | token | `Patient.identifier` |
| language | token | `Patient.communication.language` |
| link | reference | `Patient.link.other` (Patient, RelatedPerson) |
| name | string | `Patient.name` — may match family, given, prefix, suffix, text |
| organization | reference | `Patient.managingOrganization` (Organization) |
| phone | token | `Patient.telecom.where(system='phone')` |
| phonetic | string | `Patient.name` (phonetic matching algorithm) |
| telecom | token | `Patient.telecom` |

### Patient — rules stated in the notes
| Topic | As stated |
|---|---|
| Resource id vs MRN | "A Patient record's Resource Id can never change"; MRN/UR go in `Patient.identifier`, never as the resource id; an auto-assigned MRN can be requested by posting an identifier with system/type but *no value* |
| `active` | Only two states: in use (`active=true`) / not in use (`active=false`); set false for duplicates or records created in error; a record need not be linked to be inactivated |
| `contact` | pat-1; `contact.organization` is for guardians / business contacts; contact travels with the Patient and "cannot be used as the target of a reference" — referenced people must be RelatedPerson; the primary care provider goes in `generalPractitioner` |
| `communication` | Only one preferred language per mode of expression |
| `gender` | Administrative gender only; clinical sex/gender are Observations (LOINC 76691-5 clinical gender, 76689-9 sex assigned at birth), gender identity via the `genderIdentity` extension |
| Merging | Not specified; duplicates are *linked*; servers MAY migrate data but it is not mandated |
| `$match` | `POST [base]/Patient/$match` with a Parameters body holding a (possibly partial, need-not-validate) Patient; returns a searchset ordered most→least likely, each entry with `search.score` 0–1 and extension `http://hl7.org/fhir/StructureDefinition/match-grade` = `certain` \| `probable` \| `possible` \| `certainly-not`; no matches → empty searchset, no error |

### `Patient.link` (page §8.1.4–8.1.5)
"Used to assert that two or more Patient resources are both about the same actual patient." Scenarios as printed:

| `link.type` | Scenario |
|---|---|
| `replaced-by` | Duplicate record: the record holding the link is marked a duplicate and points forward to the record to use instead (which may itself forward again) |
| `replaces` | The replacing record *may* point back to the old record |
| `refer` | Patient-index record pointing to servers holding the authoritative record; the referred record does not point back; linked records may contradict each other |
| `seealso` (prose: "see also"; example XML uses `see-also`) | Distributed records about the same patient, none more authoritative; links need not be bilateral |

`Patient.link` is only for Patient (and RelatedPerson, per `link.other`); Linkage is not appropriate because a linked/merged Patient "needs to have an internal indication that there is another patient resource that should be considered" — otherwise related clinical records may not be discovered. Mother/newborn: RelatedPerson (mother, `patient = Patient/child`) + mother's Patient with `link.other = rp-mom`, `type = see-also`; child's Encounter `partOf` the mother's Encounter.

## Person — elements
Root `Person` (TU) is a DomainResource. No constraints table printed.

| Element | Flags | Card. | Type | Notes |
|---|---|---|---|---|
| `Person.identifier` |  | 0..* | Identifier | A human identifier for this person |
| `Person.name` | Σ | 0..* | HumanName | A name associated with the person |
| `Person.telecom` | Σ | 0..* | ContactPoint | A contact detail for the person |
| `Person.gender` | Σ | 0..1 | code | male \| female \| other \| unknown; AdministrativeGender (Required) |
| `Person.birthDate` | Σ | 0..1 | date | The date on which the person was born |
| `Person.address` |  | 0..* | Address | One or more addresses for the person |
| `Person.photo` |  | 0..1 | Attachment | Image of the person |
| `Person.managingOrganization` | Σ | 0..1 | Reference(Organization) | The organization that is the custodian of the person record |
| `Person.active` | ?!Σ | 0..1 | boolean | This person's record is in active use |
| `Person.link` |  | 0..* | BackboneElement | Link to a resource that concerns the same actual person |
| `Person.link.target` |  | 1..1 | Reference(Patient \| Practitioner \| RelatedPerson \| Person) | The resource to which this actual person is associated |
| `Person.link.assurance` |  | 0..1 | code | level1 \| level2 \| level3 \| level4; IdentityAssuranceLevel (Required) — "based on NIST Authentication Levels" |

### Person — search parameters
| Name | Type | Expression |
|---|---|---|
| address | string | `Person.address` (any Address string field) (3 Resources) |
| address-city / address-country / address-postalcode / address-state | string | `Person.address.city` / `.country` / `.postalCode` / `.state` |
| address-use | token | `Person.address.use` |
| birthdate | date | `Person.birthDate` |
| email | token | `Person.telecom.where(system='email')` |
| gender | token | `Person.gender` |
| identifier | token | `Person.identifier` |
| link | reference | `Person.link.target` (Practitioner, Patient, Person, RelatedPerson) |
| name | string | `Person.name` |
| organization | reference | `Person.managingOrganization` (Organization) |
| patient | reference | `Person.link.target.where(resolve() is Patient)` (Patient) |
| phone | token | `Person.telecom.where(system='phone')` |
| phonetic | string | `Person.name` |
| practitioner | reference | `Person.link.target.where(resolve() is Practitioner)` (Practitioner) |
| relatedperson | reference | `Person.link.target.where(resolve() is RelatedPerson)` (RelatedPerson) |
| telecom | token | `Person.telecom` |

### `Person.link` (page §8.18.2, 8.18.5–8.18.9)
- Person links assert that Patient / RelatedPerson / Practitioner / Person records "relate to the same individual"; linkage may also be indirect through business identifiers (Master Person Index without FHIR references).
- Person "SHALL NOT be referenced by any other clinical or administrative resources" — never an actor, subject, List/Group member; only the focus of an operation/message or a Bundle entry. Referenced by: itself only.
- `link.assurance` qualifies confidence: e.g. `level1` for a probabilistic match, `level3` for a government-issued photo ID.
- The page says the Patient `link` element "cannot be used to link to RelatedPerson entries, so we can use a Person resource" (recorded as printed; the Patient table itself allows `Reference(Patient | RelatedPerson)`).
- Uses listed: de-normalized demographics kept in sync across roles; Master Person Index; cross-domain patient directory; provider directory; access-monitoring (Practitioner D = Patient A → scrutinize D's access to A); client portal (consumer sees own Patient records via `link` Patient entries and data they entered via `link` RelatedPerson entries).
- Security: identifying information; the link itself can expose that a person has a record at a sensitive clinic — mitigate with stricter access control, sparse population, masking.

## RelatedPerson — elements
Root `RelatedPerson` (TU) is a DomainResource. No constraints table printed.

| Element | Flags | Card. | Type | Notes |
|---|---|---|---|---|
| `RelatedPerson.identifier` | Σ | 0..* | Identifier | A human identifier for this person |
| `RelatedPerson.active` | ?!Σ | 0..1 | boolean | Whether this related person's record is in active use |
| `RelatedPerson.patient` | Σ | 1..1 | Reference(Patient) | The patient this person is related to |
| `RelatedPerson.relationship` | Σ | 0..* | CodeableConcept | The nature of the relationship; Patient relationship type (Preferred) |
| `RelatedPerson.name` | Σ | 0..* | HumanName | A name associated with the person |
| `RelatedPerson.telecom` | Σ | 0..* | ContactPoint | A contact detail for the person |
| `RelatedPerson.gender` | Σ | 0..1 | code | male \| female \| other \| unknown; AdministrativeGender (Required) |
| `RelatedPerson.birthDate` | Σ | 0..1 | date | The date on which the related person was born |
| `RelatedPerson.address` | Σ | 0..* | Address | Address where the related person can be contacted or visited |
| `RelatedPerson.photo` |  | 0..* | Attachment | Image of the person |
| `RelatedPerson.period` |  | 0..1 | Period | Period of time that this relationship is considered valid |
| `RelatedPerson.communication` |  | 0..* | BackboneElement | A language which may be used to communicate with about the patient's health |
| `RelatedPerson.communication.language` |  | 1..1 | CodeableConcept | Common Languages (Preferred but limited to AllLanguages) |
| `RelatedPerson.communication.preferred` |  | 0..1 | boolean | Language preference indicator |

Bindings: `relationship` Preferred PatientRelationshipType; `gender` Required AdministrativeGender; `communication.language` Preferred (AllLanguages) CommonLanguages.

### RelatedPerson — search parameters
| Name | Type | Expression |
|---|---|---|
| active | token | `RelatedPerson.active` |
| address | string | `RelatedPerson.address` |
| address-city / address-country / address-postalcode / address-state | string | `RelatedPerson.address.city` / `.country` / `.postalCode` / `.state` |
| address-use | token | `RelatedPerson.address.use` |
| birthdate | date | `RelatedPerson.birthDate` |
| email | token | `RelatedPerson.telecom.where(system='email')` |
| gender | token | `RelatedPerson.gender` |
| identifier | token | `RelatedPerson.identifier` |
| name | string | `RelatedPerson.name` |
| patient | reference | `RelatedPerson.patient` (Patient) |
| phone | token | `RelatedPerson.telecom.where(system='phone')` |
| phonetic | string | `RelatedPerson.name` |
| relationship | token | `RelatedPerson.relationship` |
| telecom | token | `RelatedPerson.telecom` |

Practitioner vs RelatedPerson (page §8.2.2): Practitioner "operates on behalf of the care delivery organization over multiple patients"; RelatedPerson "is not associated with the organization, and instead is allocated tasks specifically for the RelatedPerson's Patient". Examples: spouse, relatives/friends, a neighbour bringing the patient, attorney or guardian, a guide dog. Someone may be both a `Patient.contact` and a RelatedPerson.

## Invariants / constraints
- pat-1 (Rule, `Patient.contact`): SHALL at least contain a contact's details or a reference to an organization — `name.exists() or telecom.exists() or address.exists() or organization.exists()`
- Person, RelatedPerson: none printed.

## Relationships
- Patient references: Organization (`contact.organization`, `managingOrganization`, `generalPractitioner`), Practitioner, PractitionerRole (`generalPractitioner`), Patient, RelatedPerson (`link.other`).
- Patient referenced by: Annotation, Signature, Account, AdverseEvent, AllergyIntolerance, Appointment, AppointmentResponse, AuditEvent, Basic, BiologicallyDerivedProduct, BodyStructure, CarePlan, CareTeam, ChargeItem, Claim, ClaimResponse, ClinicalImpression, Communication, CommunicationRequest, Composition, Condition, Consent, Contract, Coverage, CoverageEligibilityRequest, CoverageEligibilityResponse, DetectedIssue, Device, DeviceRequest, DeviceUseStatement, DiagnosticReport, DocumentManifest, DocumentReference, Encounter, EnrollmentRequest, EpisodeOfCare, ExplanationOfBenefit, FamilyMemberHistory, Flag, Goal, Group, GuidanceResponse, ImagingStudy, Immunization, ImmunizationEvaluation, ImmunizationRecommendation, Invoice, List, MeasureReport, Media, MedicationAdministration, MedicationDispense, MedicationRequest, MedicationStatement, MolecularSequence, NutritionOrder, Observation, itself, Person, Procedure, Provenance, QuestionnaireResponse, RelatedPerson, RequestGroup, ResearchSubject, RiskAssessment, Schedule, ServiceRequest, Specimen, SupplyDelivery, SupplyRequest, Task and VisionPrescription.
- Person references: Organization, Patient, Practitioner, RelatedPerson, Person. Referenced by: itself.
- RelatedPerson references: Patient. Referenced by: Annotation, Signature, Account, AdverseEvent, AllergyIntolerance, Appointment, AppointmentResponse, AuditEvent, Basic, CarePlan, CareTeam, ChargeItem, Claim, Communication, CommunicationRequest, Composition, Condition, Consent, Contract, Coverage, DeviceRequest, DeviceUseStatement, DocumentManifest, DocumentReference, Encounter, ExplanationOfBenefit, Goal, Group, ImagingStudy, Invoice, MeasureReport, Media, MedicationAdministration, MedicationDispense, MedicationRequest, MedicationStatement, Observation, Patient, Person, Procedure, Provenance, QuestionnaireResponse, RequestGroup, Schedule, ServiceRequest, SupplyRequest and Task.

## Notes for our server
- Base Patient has **no** mandatory element; the SATUSEHAT profile (satusehat-patient.md) supplies the wajib set (identifier NIK/IHS, name, gender, birthDate …). Our profile must add `min=1` on those; base validation only enforces pat-1 and the Required `gender`/`link.type` codes.
- Never expose the NIK/MRN as the resource `id`; keep them in `Patient.identifier` (the id "can never change") and search with `identifier=[system]|[value]` (token).
- `active`, `deceased[x]` and `link` are modifier elements (`?!`): searches and the patient-role login must skip `active=false` records and follow `link.type=replaced-by` to the surviving record instead of merging rows; the spec does not mandate data migration.
- Patient-role accounts map 1:1 to a Patient; guardians (parents of newborns, per satusehat-related-person.md) map to RelatedPerson with `patient` 1..1 — the only mandatory RelatedPerson element — and `relationship` codes; keep `Patient.contact` for phone-book data only, since it cannot be referenced.
- Person is optional and "SHALL NOT be referenced" by clinical resources; only adopt it if one login must span a Patient record and a RelatedPerson record (client-portal pattern with `link.target` + `assurance`). Otherwise omit Person from the CapabilityStatement.
- Search index for Patient: `identifier`, `name`/`family`/`given` (string, starts-with), `birthdate` (date), `gender`, `phone`/`email`/`telecom` (token with `system=` filter), `address-*`, `organization`, `link`; `deceased` is a boolean-ish token computed from `deceased[x]`. For RelatedPerson: `patient`, `identifier`, `name`, `relationship`.
- If we ever run an MPI-style lookup, implement `POST Patient/$match` returning `search.score` + `match-grade`; an ordinary `Patient?identifier=` search is sufficient for NIK-based lookups.

## Sources
- raw/fhir-r4/patient.md
- raw/fhir-r4/person.md
- raw/fhir-r4/relatedperson.md

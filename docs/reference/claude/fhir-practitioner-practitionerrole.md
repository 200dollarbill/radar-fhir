# FHIR R4 — Practitioner, PractitionerRole

Purpose: `Practitioner` = "A person with a formal responsibility in the provisioning of healthcare or related services", used "for attribution of activities and responsibilities" (Trial Use, maturity 3, security category Individual, compartment Practitioner). `PractitionerRole` = "Roles/organizations the practitioner is associated with" — "the location and types of services that Practitioners are able to provide for an organization" (Trial Use, maturity 2, Individual, compartment Practitioner). Flags: `Σ` summary, `TU` trial use. Neither page prints a constraints table or a modifier (`?!`) flag.

## Practitioner — elements
Root `Practitioner` (TU) is a DomainResource.

| Element | Flags | Card. | Type | Notes |
|---|---|---|---|---|
| `Practitioner.identifier` | Σ | 0..* | Identifier | An identifier for the person as this agent |
| `Practitioner.active` | Σ | 0..1 | boolean | Whether this practitioner's record is in active use |
| `Practitioner.name` | Σ | 0..* | HumanName | The name(s) associated with the practitioner |
| `Practitioner.telecom` | Σ | 0..* | ContactPoint | A contact detail for the practitioner (that apply to all roles) |
| `Practitioner.address` | Σ | 0..* | Address | Address(es) of the practitioner that are not role specific (typically home address) |
| `Practitioner.gender` | Σ | 0..1 | code | male \| female \| other \| unknown; AdministrativeGender (Required) |
| `Practitioner.birthDate` | Σ | 0..1 | date | The date on which the practitioner was born |
| `Practitioner.photo` |  | 0..* | Attachment | Image of the person |
| `Practitioner.qualification` |  | 0..* | BackboneElement | Certification, licenses, or training pertaining to the provision of care |
| `Practitioner.qualification.identifier` |  | 0..* | Identifier | An identifier for this qualification for the practitioner |
| `Practitioner.qualification.code` |  | 1..1 | CodeableConcept | Coded representation of the qualification; v2 table 0360, Version 2.7 (Example) |
| `Practitioner.qualification.period` |  | 0..1 | Period | Period during which the qualification is valid |
| `Practitioner.qualification.issuer` |  | 0..1 | Reference(Organization) | Organization that regulates and issues the qualification |
| `Practitioner.communication` |  | 0..* | CodeableConcept | A language the practitioner can use in patient communication; Common Languages (Preferred but limited to AllLanguages) |

Bindings: `gender` Required AdministrativeGender; `qualification.code` Example v2.0360.2.7; `communication` Preferred (AllLanguages) CommonLanguages.

Page notes: Practitioner "SHALL NOT be used for persons involved without a formal responsibility" (friends, relatives, neighbours → `Patient.contact`, or RelatedPerson when referenced). Practitioner = operates on behalf of the care-delivery organization over multiple patients; RelatedPerson = not associated with the organization, tasks specific to one patient. Qualifications "are acquired by the practitioner independent of any organization or role, and do not imply that they are allowed/authorized to perform roles" at any specific Organization/Location. A practitioner may hold different roles in the same or different organizations; a jurisdiction may keep one Practitioner per role or one with multiple roles; the represented organization "need not necessarily be the (direct) employer". Examples listed include physicians, nurses, receptionists handling registration, IT personnel merging patient records, service animals (extension `animalSpecies`).

### Practitioner — search parameters
| Name | Type | Expression |
|---|---|---|
| active | token | `Practitioner.active` |
| address | string | `Practitioner.address` (any Address string field) (3 Resources) |
| address-city / address-country / address-postalcode / address-state | string | `Practitioner.address.city` / `.country` / `.postalCode` / `.state` |
| address-use | token | `Practitioner.address.use` |
| communication | token | `Practitioner.communication` |
| email | token | `Practitioner.telecom.where(system='email')` (4 Resources) |
| family | string | `Practitioner.name.family` |
| gender | token | `Practitioner.gender` |
| given | string | `Practitioner.name.given` |
| identifier | token | `Practitioner.identifier` |
| name | string | `Practitioner.name` (family, given, prefix, suffix, text) |
| phone | token | `Practitioner.telecom.where(system='phone')` |
| phonetic | string | `Practitioner.name` (phonetic matching) |
| telecom | token | `Practitioner.telecom` |

## PractitionerRole — elements
Root `PractitionerRole` (TU) is a DomainResource.

| Element | Flags | Card. | Type | Notes |
|---|---|---|---|---|
| `PractitionerRole.identifier` | Σ | 0..* | Identifier | Business Identifiers that are specific to a role/location |
| `PractitionerRole.active` | Σ | 0..1 | boolean | Whether this practitioner role record is in active use |
| `PractitionerRole.period` | Σ | 0..1 | Period | The period during which the practitioner is authorized to perform in these role(s) |
| `PractitionerRole.practitioner` | Σ | 0..1 | Reference(Practitioner) | Practitioner that is able to provide the defined services for the organization |
| `PractitionerRole.organization` | Σ | 0..1 | Reference(Organization) | Organization where the roles are available |
| `PractitionerRole.code` | Σ | 0..* | CodeableConcept | Roles which this practitioner may perform; Practitioner role (Example) |
| `PractitionerRole.specialty` | Σ | 0..* | CodeableConcept | Specific specialty of the practitioner; Practice Setting Code Value Set (Preferred) |
| `PractitionerRole.location` | Σ | 0..* | Reference(Location) | The location(s) at which this practitioner provides care |
| `PractitionerRole.healthcareService` |  | 0..* | Reference(HealthcareService) | Healthcare services this worker provides for this role's Organization/Location(s) |
| `PractitionerRole.telecom` | Σ | 0..* | ContactPoint | Contact details that are specific to the role/location/service |
| `PractitionerRole.availableTime` |  | 0..* | BackboneElement | Times the Service Site is available |
| `PractitionerRole.availableTime.daysOfWeek` |  | 0..* | code | mon \| tue \| wed \| thu \| fri \| sat \| sun; DaysOfWeek (Required) |
| `PractitionerRole.availableTime.allDay` |  | 0..1 | boolean | Always available? e.g. 24 hour service |
| `PractitionerRole.availableTime.availableStartTime` |  | 0..1 | time | Opening time of day (ignored if allDay = true) |
| `PractitionerRole.availableTime.availableEndTime` |  | 0..1 | time | Closing time of day (ignored if allDay = true) |
| `PractitionerRole.notAvailable` |  | 0..* | BackboneElement | Not available during this time due to provided reason |
| `PractitionerRole.notAvailable.description` |  | 1..1 | string | Reason presented to the user explaining why time not available |
| `PractitionerRole.notAvailable.during` |  | 0..1 | Period | Service not available from this date |
| `PractitionerRole.availabilityExceptions` |  | 0..1 | string | Description of availability exceptions |
| `PractitionerRole.endpoint` |  | 0..* | Reference(Endpoint) | Technical endpoints providing access to services operated for the practitioner with this role |

Bindings: `code` Example PractitionerRole; `specialty` Preferred PracticeSettingCodeValueSet; `availableTime.daysOfWeek` Required DaysOfWeek.

Page notes: no `address` on PractitionerRole — the referenced Location carries it. `code`, `specialty`, `location`, `telecom`, `healthcareService` may repeat, but when one instance lists several locations/specialties "all details apply to all locations" (one contact number, one availability); different values per location need separate instances, and existing references must then be re-pointed. The page therefore expects it "will be common to profile the location element down to a single location". Qualifications do not imply a role but may inform allocation (e.g. expiry tracking). CareTeam is finer-grained and patient-scoped; PractitionerRole covers "all the places that the practitioner is allocated to work".

### PractitionerRole — search parameters
| Name | Type | Expression |
|---|---|---|
| active | token | `PractitionerRole.active` |
| date | date | `PractitionerRole.period` |
| email | token | `PractitionerRole.telecom.where(system='email')` |
| endpoint | reference | `PractitionerRole.endpoint` (Endpoint) |
| identifier | token | `PractitionerRole.identifier` |
| location | reference | `PractitionerRole.location` (Location) |
| organization | reference | `PractitionerRole.organization` (Organization) |
| phone | token | `PractitionerRole.telecom.where(system='phone')` |
| practitioner | reference | `PractitionerRole.practitioner` (Practitioner) |
| role | token | `PractitionerRole.code` |
| service | reference | `PractitionerRole.healthcareService` (HealthcareService) |
| specialty | token | `PractitionerRole.specialty` |
| telecom | token | `PractitionerRole.telecom` |

## Invariants / constraints
- None printed for either resource.

## Relationships
- Practitioner references: Organization (`qualification.issuer`).
- Practitioner referenced by: Annotation, Signature, Account, AdverseEvent, AllergyIntolerance, Appointment, AppointmentResponse, AuditEvent, Basic, BiologicallyDerivedProduct, CarePlan, CareTeam, CatalogEntry, ChargeItem, Claim, ClaimResponse, ClinicalImpression, Communication, CommunicationRequest, Composition, Condition, Consent, Contract, CoverageEligibilityRequest, CoverageEligibilityResponse, DetectedIssue, DeviceRequest, DeviceUseStatement, DiagnosticReport, DocumentManifest, DocumentReference, Encounter, EnrollmentRequest, EnrollmentResponse, EpisodeOfCare, ExplanationOfBenefit, Flag, Goal, Group, ImagingStudy, Immunization, Invoice, Linkage, List, MeasureReport, Media, MedicationAdministration, MedicationDispense, MedicationRequest, MedicationStatement, MessageHeader, NutritionOrder, Observation, Patient, PaymentNotice, PaymentReconciliation, Person, PractitionerRole, Procedure, Provenance, QuestionnaireResponse, RequestGroup, ResearchStudy, RiskAssessment, Schedule, ServiceRequest, Specimen, SupplyDelivery, SupplyRequest, Task, VerificationResult and VisionPrescription.
- PractitionerRole references: Practitioner, Organization, Location, HealthcareService, Endpoint.
- PractitionerRole referenced by: same list as Practitioner except it omits Annotation, Person and PractitionerRole and adds MedicinalProduct (as printed: Signature, Account, AdverseEvent, … Observation, Patient, … Procedure, … VisionPrescription).

## Notes for our server
- Doctor accounts map to a Practitioner (identity, `identifier` e.g. NIK/IHS per satusehat-practitioner.md, `name`, `gender`, `qualification.code` 1..1 inside each qualification) plus one PractitionerRole per organisation/location assignment (`practitioner`, `organization`, `code`, `specialty`, `location`, `period`). Authorization ("may this doctor act at this facility?") belongs to PractitionerRole, not to Practitioner qualifications — the page says qualifications imply no authorization.
- Base R4 makes nothing mandatory on either resource (only `qualification.code` and `notAvailable.description` are 1..1 within their backbone); our profile should require `Practitioner.identifier`, `Practitioner.name`, `PractitionerRole.practitioner`, `PractitionerRole.organization` so `Encounter.participant.individual` and `Observation.performer` resolve to a known doctor at a known facility.
- Profile `PractitionerRole.location` to at most one Location (the page anticipates this) so availability/telecom are unambiguous; put the address on Location, never on the role.
- `active` is *not* a modifier flag here (unlike Patient.active) but still drives login: deny doctor-role tokens whose Practitioner or PractitionerRole is `active=false` or whose `period` has ended.
- Search index: Practitioner `identifier`, `name`/`family`/`given`, `phone`/`email`; PractitionerRole `practitioner`, `organization`, `location`, `role`, `specialty`, `date` (period) — enough for the admin "staff at facility X" and doctor-worklist lookups; support `_include=PractitionerRole:practitioner`.
- SATUSEHAT treats Practitioner as read-only master data (satusehat-practitioner.md); locally we create/update it, but keep the IHS practitioner number in `identifier` so outbound references use `Practitioner/{ihs-number}`.

## Sources
- raw/fhir-r4/practitioner.md
- raw/fhir-r4/practitionerrole.md

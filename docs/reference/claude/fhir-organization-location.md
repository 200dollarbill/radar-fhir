# FHIR R4 — Organization, Location

Purpose: `Organization` = "A grouping of people or organizations with a common purpose" — the *conceptual* hierarchy (hospital → department → ward) via `partOf` (Trial Use, maturity 3, security category Business, no compartments). `Location` = "Details and position information for a physical place" — the *physical* hierarchy (building → wing → room → bed) via `partOf`; "Locations are always used for recording where a service occurs, and hence where encounters and observations are associated" (Trial Use, maturity 3, Business, no compartments). Flags: `Σ` summary, `?!` modifier, `I` invariant, `TU` trial use.

## Organization — elements
Root `Organization` (ITU) is a DomainResource carrying rule org-1.

| Element | Flags | Card. | Type | Notes |
|---|---|---|---|---|
| `Organization.identifier` | ΣI | 0..* | Identifier | Identifies this organization across multiple systems |
| `Organization.active` | ?!Σ | 0..1 | boolean | Whether the organization's record is still in active use |
| `Organization.type` | Σ | 0..* | CodeableConcept | Kind of organization; Organization type (Example) |
| `Organization.name` | ΣI | 0..1 | string | Name used for the organization |
| `Organization.alias` |  | 0..* | string | Alternate names the organization is or was known as |
| `Organization.telecom` | I | 0..* | ContactPoint | A contact detail for the organization + Rule: can never be of use 'home' (org-3) |
| `Organization.address` | I | 0..* | Address | An address for the organization + Rule: can never be of use 'home' (org-2) |
| `Organization.partOf` | Σ | 0..1 | Reference(Organization) | The organization of which this organization forms a part |
| `Organization.contact` |  | 0..* | BackboneElement | Contact for the organization for a certain purpose |
| `Organization.contact.purpose` |  | 0..1 | CodeableConcept | The type of contact; Contact entity type (Extensible) |
| `Organization.contact.name` |  | 0..1 | HumanName | A name associated with the contact |
| `Organization.contact.telecom` |  | 0..* | ContactPoint | Contact details (telephone, email, etc.) for a contact |
| `Organization.contact.address` |  | 0..1 | Address | Visiting or postal addresses for the contact |
| `Organization.endpoint` |  | 0..* | Reference(Endpoint) | Technical endpoints providing access to services operated for the organization |

Bindings: `type` Example OrganizationType; `contact.purpose` Extensible ContactEntityType.

Page notes: usable as a shared registry or merely as support for references (document, message, contained); several registries may exist per organization type/level. Organization vs Group: Group is a collection "gathered for the purpose of analysis or acting upon, but are not expected to act themselves". Two contact places: `telecom`/`address` on the Organization = generic public point of contact; `contact` (ContactEntity) = a designated person/party for a specific purpose. Example hierarchy (all `partOf`): Burgers University Medical Center → Eastern Services (prov) → Emergency Dept, Oncology Dept, Maternity Ward, … ; "physical structures of this hierarchy are not present - these are defined by a Location hierarchy".

### Organization — search parameters
| Name | Type | Expression |
|---|---|---|
| active | token | `Organization.active` |
| address | string | `Organization.address` (any Address string field) |
| address-city / address-country / address-postalcode / address-state | string | `Organization.address.city` / `.country` / `.postalCode` / `.state` |
| address-use | token | `Organization.address.use` |
| endpoint | reference | `Organization.endpoint` (Endpoint) |
| identifier | token | `Organization.identifier` — "not the accreditation issuer's identifier" |
| name | string | `Organization.name \| Organization.alias` |
| partof | reference | `Organization.partOf` (Organization) |
| phonetic | string | `Organization.name` (phonetic matching) |
| type | token | `Organization.type` |

## Location — elements
Root `Location` (TU) is a DomainResource. No constraints table printed.

| Element | Flags | Card. | Type | Notes |
|---|---|---|---|---|
| `Location.identifier` | Σ | 0..* | Identifier | Unique code or number identifying the location to its users |
| `Location.status` | ?!Σ | 0..1 | code | active \| suspended \| inactive; LocationStatus (Required) |
| `Location.operationalStatus` | Σ | 0..1 | Coding | Operational status (typically only for a bed/room); v2 BED STATUS (Preferred) |
| `Location.name` | Σ | 0..1 | string | Name of the location as used by humans |
| `Location.alias` |  | 0..* | string | Alternate names the location is or was known as |
| `Location.description` | Σ | 0..1 | string | Additional details to identify the location beyond its name |
| `Location.mode` | Σ | 0..1 | code | instance \| kind; LocationMode (Required) |
| `Location.type` | Σ | 0..* | CodeableConcept | Type of function performed; V3 ServiceDeliveryLocationRoleType (Extensible) |
| `Location.telecom` |  | 0..* | ContactPoint | Contact details of the location |
| `Location.address` |  | 0..1 | Address | Physical location |
| `Location.physicalType` | Σ | 0..1 | CodeableConcept | Physical form of the location; Location type (Example) |
| `Location.position` |  | 0..1 | BackboneElement | The absolute geographic location |
| `Location.position.longitude` |  | 1..1 | decimal | Longitude with WGS84 datum |
| `Location.position.latitude` |  | 1..1 | decimal | Latitude with WGS84 datum |
| `Location.position.altitude` |  | 0..1 | decimal | Altitude with WGS84 datum |
| `Location.managingOrganization` | Σ | 0..1 | Reference(Organization) | Organization responsible for provisioning and upkeep |
| `Location.partOf` |  | 0..1 | Reference(Location) | Another Location this one is physically a part of |
| `Location.hoursOfOperation` |  | 0..* | BackboneElement | What days/times during a week is this location usually open |
| `Location.hoursOfOperation.daysOfWeek` |  | 0..* | code | mon \| tue \| wed \| thu \| fri \| sat \| sun; DaysOfWeek (Required) |
| `Location.hoursOfOperation.allDay` |  | 0..1 | boolean | The Location is open all day |
| `Location.hoursOfOperation.openingTime` |  | 0..1 | time | Time that the Location opens |
| `Location.hoursOfOperation.closingTime` |  | 0..1 | time | Time that the Location closes |
| `Location.availabilityExceptions` |  | 0..1 | string | Description of availability exceptions |
| `Location.endpoint` |  | 0..* | Reference(Endpoint) | Technical endpoints providing access to services operated for the location |

Bindings: `status` Required LocationStatus; `operationalStatus` Preferred v2.0116; `mode` Required LocationMode; `type` Extensible v3.ServiceDeliveryLocationRoleType; `physicalType` Example LocationType; `hoursOfOperation.daysOfWeek` Required DaysOfWeek.

### Location — rules stated on the page
| Topic | As stated |
|---|---|
| Scope | Incidental or dedicated places: building, ward, corridor, room, bed, mobile clinic, freezer, vehicle, home, road, ambulance, patient's home, jurisdiction (nation, province, business scope) — not body sites |
| Address | Valid without an address (geo-coded remote areas, recorded by a device, `mode = kind`) |
| `mode` | `instance` = a specific (potentially identifiable) Location; `kind` = a class of Locations for orders/scheduling/plans ("an isolation room", "an ambulance"). Unknown-which-ambulance is `instance` with a missing identifier, **not** `kind`. Elements only relevant for `instance`: `identifier`, `telecom`, `address`, `position`, `status`, `managingOrganization` |
| Hierarchy | `partOf` relates smaller Locations to their container (building → wing → level → room → bed; trolleys "move about"); wards/departments are *not* in this structure — they are Organizations |
| Providers | Which Organizations/Practitioners serve at a Location is kept on Organization/PractitionerRole, not on Location |
| `position` | Same syntax, datum and reference system as Google Earth KML |
| Org ↔ Location | Each point in the location hierarchy links to the appropriate level of the Organization hierarchy, not necessarily the top; the Organization on a clinical resource "might not be the location where the service took place" |

### Location — search parameters
| Name | Type | Expression |
|---|---|---|
| address | string | `Location.address` — "A (part of the) address of the location" |
| address-city / address-country / address-postalcode / address-state | string | `Location.address.city` / `.country` / `.postalCode` / `.state` |
| address-use | token | `Location.address.use` |
| endpoint | reference | `Location.endpoint` (Endpoint) |
| identifier | token | `Location.identifier` |
| name | string | `Location.name \| Location.alias` |
| near | special | `Location.position` — value `[latitude]\|[longitude]\|[distance]\|[units]` (WGS84); units omitted → km; distance omitted → server's discretion; description still says "Requires the near-distance parameter to be provided also" although the notes say near-distance was deprecated (recorded as printed) |
| operational-status | token | `Location.operationalStatus` |
| organization | reference | `Location.managingOrganization` (Organization) |
| partof | reference | `Location.partOf` (Location) |
| status | token | `Location.status` |
| type | token | `Location.type` |

Positional search example: `GET [base]/Location?near=-83.694810|42.256500|11.20|km`; results may carry the distance in `entry.search.extension` url `http://hl7.org/fhir/StructureDefinition/location-distance` (`valueDistance` value + unit) because the distance depends on the query point and cannot live inside the resource.

## Invariants / constraints
- org-1 (Rule, base): The organization SHALL at least have a name or an identifier, and possibly more than one — `(identifier.count() + name.count()) > 0`
- org-2 (Rule, `Organization.address`): An address of an organization can never be of use 'home' — `where(use = 'home').empty()`
- org-3 (Rule, `Organization.telecom`): The telecom of an organization can never be of use 'home' — `where(use = 'home').empty()`
- Location: none printed.

## Relationships
- Organization references: Organization (`partOf`), Endpoint.
- Organization referenced by: Annotation, Identifier, Signature, UsageContext, Account, AuditEvent, Basic, BiologicallyDerivedProduct, CapabilityStatement, CarePlan, CareTeam, CatalogEntry, ChargeItem, Claim, ClaimResponse, Communication, CommunicationRequest, Composition, Consent, Contract, Coverage, CoverageEligibilityRequest, CoverageEligibilityResponse, Device, DeviceDefinition, DeviceRequest, DiagnosticReport, DocumentManifest, DocumentReference, Encounter, Endpoint, EnrollmentRequest, EnrollmentResponse, EpisodeOfCare, ExplanationOfBenefit, Flag, Goal, Group, HealthcareService, ImagingStudy, Immunization, ImmunizationEvaluation, ImmunizationRecommendation, InsurancePlan, Invoice, Linkage, Location, MeasureReport, Media, Medication, MedicationDispense, MedicationKnowledge, MedicationRequest, MedicationStatement, MedicinalProduct, MedicinalProductAuthorization, MedicinalProductIngredient, MedicinalProductManufactured, MedicinalProductPackaged, MessageHeader, MolecularSequence, Observation, itself, OrganizationAffiliation, Patient, PaymentNotice, PaymentReconciliation, Person, Practitioner, PractitionerRole, Procedure, Provenance, QuestionnaireResponse, ResearchStudy, ServiceRequest, SupplyDelivery, SupplyRequest, Task and VerificationResult.
- Location references: Organization (`managingOrganization`), Location (`partOf`), Endpoint.
- Location referenced by: UsageContext, Account, ActivityDefinition, AdverseEvent, Appointment, AppointmentResponse, AuditEvent, CarePlan, Claim, ClaimResponse, Contract, CoverageEligibilityRequest, Device, DeviceRequest, DiagnosticReport, Encounter, ExplanationOfBenefit, Flag, HealthcareService, ImagingStudy, Immunization, InsurancePlan, List, itself, MeasureReport, Media, MedicationDispense, Observation, OrganizationAffiliation, PractitionerRole, Procedure, Provenance, ResearchStudy, Schedule, ServiceRequest, Specimen, SupplyDelivery, SupplyRequest and Task.

## Notes for our server
- Validate org-1 on every Organization write (`identifier` or `name` must be present) and reject `use = home` on `Organization.address`/`telecom` (org-2/org-3). Location has no base invariants, but `position.longitude`/`latitude` are 1..1 whenever `position` is sent.
- Admin role seeds two trees: Organization `partOf` for facility → departments (SATUSEHAT suborganisation hierarchy, satusehat-organization-location.md) and Location `partOf` for building → room/bed, each Location pointing at its department via `managingOrganization`. Encounter.serviceProvider references the Organization; Encounter.location.location and Device.location reference the Location — never the other way round.
- `Organization.active` and `Location.status` are modifier elements (`?!`); filter `active=false` / `status=inactive|suspended` out of pick-lists and refuse new Encounters against them.
- Use `Location.mode = instance` for every real room/bed; reserve `kind` for scheduling templates only; `physicalType` distinguishes bed vs room vs ward for `Encounter.location.physicalType`.
- Search index: Organization `identifier`, `name` (+alias), `type`, `partof`, `address-city`; Location `identifier`, `name`, `organization`, `partof`, `status`, `type`, `physicalType` is *not* a standard parameter. `near` is a `special` type — only implement if we store `position`; otherwise omit it from the CapabilityStatement.
- Support `_include=Location:organization` and `Organization:partof` chaining so the patient/doctor UIs can render "Room 1a, Poli Umum, RS X" from one query.

## Sources
- raw/fhir-r4/organization.md
- raw/fhir-r4/location.md

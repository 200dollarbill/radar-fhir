---
id: practitionerrole
title: PractitionerRole
source_url: https://hl7.org/fhir/R4/practitionerrole.html
group: fhir-r4
fhir_version: R4
fetched_at: '2026-09-11T13:22:34Z'
sha256: 5c44bf5c82dd3b212c2ff59d4b438eb0c638e14b6d1306cd92ae8313afa68230
---
This page is part of the FHIR Specification (v4.0.1: R4 - Mixed [Normative](https://confluence.hl7.org/display/HL7/HL7+Balloting "Normative Standard") and [STU](https://confluence.hl7.org/display/HL7/HL7+Balloting "Standard for Trial-Use")) in it's permanent home (it will always be available at this URL). The current version which supercedes this version is [5.0.0](http://hl7.org/fhir/index.html). For a full list of available versions, see the [Directory of published versions ![](external.png)](http://hl7.org/fhir/directory.html). Page versions: [R5](http://hl7.org/fhir/R5/practitionerrole.html) [R4B](http://hl7.org/fhir/R4B/practitionerrole.html) **R4** [R3](http://hl7.org/fhir/STU3/practitionerrole.html)

- [Content](#)
- [Examples](practitionerrole-examples.html)
- [Detailed Descriptions](practitionerrole-definitions.html)
- [Mappings](practitionerrole-mappings.html)
- [Profiles & Extensions](practitionerrole-profiles.html)
- [R3 Conversions](practitionerrole-version-maps.html)

# 8.5 Resource PractitionerRole - Content

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [Patient Administration](http://www.hl7.org/Special/committees/pafm/index.cfm)  Work Group | [Maturity Level](versions.html#maturity): 2 | [Trial Use](versions.html#std-process "Standard Status") | [Security Category](security.html#SecPrivConsiderations): Individual | [Compartments](compartmentdefinition.html): [Practitioner](compartmentdefinition-practitioner.html) |

A specific set of Roles/Locations/specialties/services that a practitioner may perform at an organization for a period of time.

## 8.5.1 Scope and Usage

PractitionerRole covers the recording of the location and types of services that Practitioners are able to provide
for an organization.

The role, specialty, Location telecom and HealthcareService properties can be repeated if required in other instances
of the PractitionerRole. Some systems record a collection of service values for a single location, others record the
single service and the list of locations it is available. Both are acceptable options for representing this data.  
Where availability, telecom, or other details are not the same across all healthcareservices, or locations
a seperate PractitionerRole instance should be created.

## 8.5.2 Boundaries and Relationships

Qualifications (from the Practitioner resource) do not imply a Role, but might be considered when an Organization
allocates practitioners to roles within their organization, and could provide useful information (such as expiry information)
which could need to be tracked in some situations to ensure they continue to be eligible for a specific role.

The [CareTeam](careteam.html) resource is also often used to provide details of a role that a practitioner is
allocated to perform, but is usually scoped to a much finer granularity of care, and often within the specific context
of a [Patient](patient.html), or functional role (e.g. Crisis planning team). In contrast the PractitionerRole
is used in a more general sense to cover all the places that the practitioner is allocated to work (and specific details
relevant to that role - such as a specific contact number, or electronic services endpoint).

## 8.5.3 Background and Context

Practitioner performs different roles within the same or even different organizations. Depending on jurisdiction and custom,
it may be necessary to maintain a specific Practitioner Resource for each such role or have a single Practitioner with multiple roles.
The role can be limited to a specific period, after which authorization for this role ends. Note that the represented organization
need not necessarily be the (direct) employer of a Practitioner.

This resource is referenced by [Signature](datatypes.html#Signature), [Account](account.html#Account), [AdverseEvent](adverseevent.html#AdverseEvent), [AllergyIntolerance](allergyintolerance.html#AllergyIntolerance), [Appointment](appointment.html#Appointment), [AppointmentResponse](appointmentresponse.html#AppointmentResponse), [AuditEvent](auditevent.html#AuditEvent), [Basic](basic.html#Basic), [BiologicallyDerivedProduct](biologicallyderivedproduct.html#BiologicallyDerivedProduct), [CarePlan](careplan.html#CarePlan), [CareTeam](careteam.html#CareTeam), [CatalogEntry](catalogentry.html#CatalogEntry), [ChargeItem](chargeitem.html#ChargeItem), [Claim](claim.html#Claim), [ClaimResponse](claimresponse.html#ClaimResponse), [ClinicalImpression](clinicalimpression.html#ClinicalImpression), [Communication](communication.html#Communication), [CommunicationRequest](communicationrequest.html#CommunicationRequest), [Composition](composition.html#Composition), [Condition](condition.html#Condition), [Consent](consent.html#Consent), [Contract](contract.html#Contract), [CoverageEligibilityRequest](coverageeligibilityrequest.html#CoverageEligibilityRequest), [CoverageEligibilityResponse](coverageeligibilityresponse.html#CoverageEligibilityResponse), [DetectedIssue](detectedissue.html#DetectedIssue), [DeviceRequest](devicerequest.html#DeviceRequest), [DeviceUseStatement](deviceusestatement.html#DeviceUseStatement), [DiagnosticReport](diagnosticreport.html#DiagnosticReport), [DocumentManifest](documentmanifest.html#DocumentManifest), [DocumentReference](documentreference.html#DocumentReference), [Encounter](encounter.html#Encounter), [EnrollmentRequest](enrollmentrequest.html#EnrollmentRequest), [EnrollmentResponse](enrollmentresponse.html#EnrollmentResponse), [EpisodeOfCare](episodeofcare.html#EpisodeOfCare), [ExplanationOfBenefit](explanationofbenefit.html#ExplanationOfBenefit), [Flag](flag.html#Flag), [Goal](goal.html#Goal), [Group](group.html#Group), [ImagingStudy](imagingstudy.html#ImagingStudy), [Immunization](immunization.html#Immunization), [Invoice](invoice.html#Invoice), [Linkage](linkage.html#Linkage), [List](list.html#List), [MeasureReport](measurereport.html#MeasureReport), [Media](media.html#Media), [MedicationAdministration](medicationadministration.html#MedicationAdministration), [MedicationDispense](medicationdispense.html#MedicationDispense), [MedicationRequest](medicationrequest.html#MedicationRequest), [MedicationStatement](medicationstatement.html#MedicationStatement), [MedicinalProduct](medicinalproduct.html#MedicinalProduct), [MessageHeader](messageheader.html#MessageHeader), [NutritionOrder](nutritionorder.html#NutritionOrder), [Observation](observation.html#Observation), [Patient](patient.html#Patient), [PaymentNotice](paymentnotice.html#PaymentNotice), [PaymentReconciliation](paymentreconciliation.html#PaymentReconciliation), [Procedure](procedure.html#Procedure), [Provenance](provenance.html#Provenance), [QuestionnaireResponse](questionnaireresponse.html#QuestionnaireResponse), [RequestGroup](requestgroup.html#RequestGroup), [ResearchStudy](researchstudy.html#ResearchStudy), [RiskAssessment](riskassessment.html#RiskAssessment), [Schedule](schedule.html#Schedule), [ServiceRequest](servicerequest.html#ServiceRequest), [Specimen](specimen.html#Specimen), [SupplyDelivery](supplydelivery.html#SupplyDelivery), [SupplyRequest](supplyrequest.html#SupplyRequest), [Task](task.html#Task), [VerificationResult](verificationresult.html#VerificationResult) and [VisionPrescription](visionprescription.html#VisionPrescription)

## 8.5.4 Resource Content

- [Structure](#tabs-struc)
- [UML](#tabs-uml)
- [XML](#tabs-xml)
- [JSON](#tabs-json)
- [Turtle](#tabs-ttl)
- [R3 Diff](#tabs-diff)
- [All](#tabs-all)

**Structure**

| [Name](formats.html#table "The logical name of the element") | [Flags](formats.html#table "Information about the use of the element") | [Card.](formats.html#table "Minimum and Maximum # of times the the element can appear in the instance") | [Type](formats.html#table "Reference to the type of the element") | [Description & Constraints](formats.html#table "Additional information about the element")[doco](formats.html#table "Legend for this format") |
| --- | --- | --- | --- | --- |
| .. [PractitionerRole](practitionerrole-definitions.html#PractitionerRole "PractitionerRole : A specific set of Roles/Locations/specialties/services that a practitioner may perform at an organization for a period of time.") | [TU](versions.html#std-process "Standards Status = Trial Use") |  | [DomainResource](domainresource.html) | Roles/organizations the practitioner is associated with Elements defined in Ancestors: [id](resource.html#Resource "The logical id of the resource, as used in the URL for the resource. Once assigned, this value never changes."), [meta](resource.html#Resource "The metadata about the resource. This is content that is maintained by the infrastructure. Changes to the content might not always be associated with version changes to the resource."), [implicitRules](resource.html#Resource "A reference to a set of rules that were followed when the resource was constructed, and which must be understood when processing the content. Often, this is a reference to an implementation guide that defines the special rules along with other profiles etc."), [language](resource.html#Resource "The base language in which the resource is written."), [text](domainresource.html#DomainResource "A human-readable narrative that contains a summary of the resource and can be used to represent the content of the resource to a human. The narrative need not encode all the structured data, but is required to contain sufficient detail to make it \"clinically safe\" for a human to just read the narrative. Resource definitions may define what content should be represented in the narrative to ensure clinical safety."), [contained](domainresource.html#DomainResource "These resources do not have an independent existence apart from the resource that contains them - they cannot be identified independently, and nor can they have their own independent transaction scope."), [extension](domainresource.html#DomainResource "May be used to represent additional information that is not part of the basic definition of the resource. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension."), [modifierExtension](domainresource.html#DomainResource "May be used to represent additional information that is not part of the basic definition of the resource and that modifies the understanding of the element that contains it and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer is allowed to define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.  Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).") |
| ... [identifier](practitionerrole-definitions.html#PractitionerRole.identifier "PractitionerRole.identifier : Business Identifiers that are specific to a role/location.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [Identifier](datatypes.html#Identifier) | Business Identifiers that are specific to a role/location |
| ... [active](practitionerrole-definitions.html#PractitionerRole.active "PractitionerRole.active : Whether this practitioner role record is in active use.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [boolean](datatypes.html#boolean) | Whether this practitioner role record is in active use |
| ... [period](practitionerrole-definitions.html#PractitionerRole.period "PractitionerRole.period : The period during which the person is authorized to act as a practitioner in these role(s) for the organization.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [Period](datatypes.html#Period) | The period during which the practitioner is authorized to perform in these role(s) |
| ... [practitioner](practitionerrole-definitions.html#PractitionerRole.practitioner "PractitionerRole.practitioner : Practitioner that is able to provide the defined services for the organization.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [Reference](references.html#Reference)([Practitioner](practitioner.html)) | Practitioner that is able to provide the defined services for the organization |
| ... [organization](practitionerrole-definitions.html#PractitionerRole.organization "PractitionerRole.organization : The organization where the Practitioner performs the roles associated.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [Reference](references.html#Reference)([Organization](organization.html)) | Organization where the roles are available |
| ... [code](practitionerrole-definitions.html#PractitionerRole.code "PractitionerRole.code : Roles which this practitioner is authorized to perform for the organization.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [CodeableConcept](datatypes.html#CodeableConcept) | Roles which this practitioner may perform [Practitioner role](valueset-practitioner-role.html "The role a person plays representing an organization.") ([Example](terminologies.html#example "Instances are not expected or even encouraged to draw from the specified value set.  The value set merely provides examples of the types of concepts intended to be included.")) |
| ... [specialty](practitionerrole-definitions.html#PractitionerRole.specialty "PractitionerRole.specialty : Specific specialty of the practitioner.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [CodeableConcept](datatypes.html#CodeableConcept) | Specific specialty of the practitioner [Practice Setting Code Value Set](valueset-c80-practice-codes.html "Specific specialty associated with the agency.") ([Preferred](terminologies.html#preferred "Instances are encouraged to draw from the specified codes for interoperability purposes but are not required to do so to be considered conformant.")) |
| ... [location](practitionerrole-definitions.html#PractitionerRole.location "PractitionerRole.location : The location(s) at which this practitioner provides care.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [Reference](references.html#Reference)([Location](location.html)) | The location(s) at which this practitioner provides care |
| ... [healthcareService](practitionerrole-definitions.html#PractitionerRole.healthcareService "PractitionerRole.healthcareService : The list of healthcare services that this worker provides for this role's Organization/Location(s).") |  | 0..\* | [Reference](references.html#Reference)([HealthcareService](healthcareservice.html)) | The list of healthcare services that this worker provides for this role's Organization/Location(s) |
| ... [telecom](practitionerrole-definitions.html#PractitionerRole.telecom "PractitionerRole.telecom : Contact details that are specific to the role/location/service.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [ContactPoint](datatypes.html#ContactPoint) | Contact details that are specific to the role/location/service |
| ... [availableTime](practitionerrole-definitions.html#PractitionerRole.availableTime "PractitionerRole.availableTime : A collection of times the practitioner is available or performing this role at the location and/or healthcareservice.") |  | 0..\* | [BackboneElement](backboneelement.html) | Times the Service Site is available |
| .... [daysOfWeek](practitionerrole-definitions.html#PractitionerRole.availableTime.daysOfWeek "PractitionerRole.availableTime.daysOfWeek : Indicates which days of the week are available between the start and end Times.") |  | 0..\* | [code](datatypes.html#code) | mon | tue | wed | thu | fri | sat | sun [DaysOfWeek](valueset-days-of-week.html "The days of the week.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| .... [allDay](practitionerrole-definitions.html#PractitionerRole.availableTime.allDay "PractitionerRole.availableTime.allDay : Is this always available? (hence times are irrelevant) e.g. 24 hour service.") |  | 0..1 | [boolean](datatypes.html#boolean) | Always available? e.g. 24 hour service |
| .... [availableStartTime](practitionerrole-definitions.html#PractitionerRole.availableTime.availableStartTime "PractitionerRole.availableTime.availableStartTime : The opening time of day. Note: If the AllDay flag is set, then this time is ignored.") |  | 0..1 | [time](datatypes.html#time) | Opening time of day (ignored if allDay = true) |
| .... [availableEndTime](practitionerrole-definitions.html#PractitionerRole.availableTime.availableEndTime "PractitionerRole.availableTime.availableEndTime : The closing time of day. Note: If the AllDay flag is set, then this time is ignored.") |  | 0..1 | [time](datatypes.html#time) | Closing time of day (ignored if allDay = true) |
| ... [notAvailable](practitionerrole-definitions.html#PractitionerRole.notAvailable "PractitionerRole.notAvailable : The practitioner is not available or performing this role during this period of time due to the provided reason.") |  | 0..\* | [BackboneElement](backboneelement.html) | Not available during this time due to provided reason |
| .... [description](practitionerrole-definitions.html#PractitionerRole.notAvailable.description "PractitionerRole.notAvailable.description : The reason that can be presented to the user as to why this time is not available.") |  | 1..1 | [string](datatypes.html#string) | Reason presented to the user explaining why time not available |
| .... [during](practitionerrole-definitions.html#PractitionerRole.notAvailable.during "PractitionerRole.notAvailable.during : Service is not available (seasonally or for a public holiday) from this date.") |  | 0..1 | [Period](datatypes.html#Period) | Service not available from this date |
| ... [availabilityExceptions](practitionerrole-definitions.html#PractitionerRole.availabilityExceptions "PractitionerRole.availabilityExceptions : A description of site availability exceptions, e.g. public holiday availability. Succinctly describing all possible exceptions to normal site availability as details in the available Times and not available Times.") |  | 0..1 | [string](datatypes.html#string) | Description of availability exceptions |
| ... [endpoint](practitionerrole-definitions.html#PractitionerRole.endpoint "PractitionerRole.endpoint : Technical endpoints providing access to services operated for the practitioner with this role.") |  | 0..\* | [Reference](references.html#Reference)([Endpoint](endpoint.html)) | Technical endpoints providing access to services operated for the practitioner with this role |
| [doco Documentation for this format](formats.html#table "Legend for this format") | | | | |

**UML Diagram** ([Legend](formats.html#uml))

**XML Template**

```

<PractitionerRole xmlns="http://hl7.org/fhir"> ![doco](help.png)
 <!-- from Resource: id, meta, implicitRules, and language -->
 <!-- from DomainResource: text, contained, extension, and modifierExtension -->
 <identifier><!-- 0..* Identifier Business Identifiers that are specific to a role/location --></identifier>
 <active value="[boolean]"/><!-- 0..1 Whether this practitioner role record is in active use -->
 <period><!-- 0..1 Period The period during which the practitioner is authorized to perform in these role(s) --></period>
 <practitioner><!-- 0..1 Reference(Practitioner) Practitioner that is able to provide the defined services for the organization --></practitioner>
 <organization><!-- 0..1 Reference(Organization) Organization where the roles are available --></organization>
 <code><!-- 0..* CodeableConcept Roles which this practitioner may perform --></code>
 <specialty><!-- 0..* CodeableConcept Specific specialty of the practitioner --></specialty>
 <location><!-- 0..* Reference(Location) The location(s) at which this practitioner provides care --></location>
 <healthcareService><!-- 0..* Reference(HealthcareService) The list of healthcare services that this worker provides for this role's Organization/Location(s) --></healthcareService>
 <telecom><!-- 0..* ContactPoint Contact details that are specific to the role/location/service --></telecom>
 <availableTime>  <!-- 0..* Times the Service Site is available -->
  <daysOfWeek value="[code]"/><!-- 0..* mon | tue | wed | thu | fri | sat | sun -->
  <allDay value="[boolean]"/><!-- 0..1 Always available? e.g. 24 hour service -->
  <availableStartTime value="[time]"/><!-- 0..1 Opening time of day (ignored if allDay = true) -->
  <availableEndTime value="[time]"/><!-- 0..1 Closing time of day (ignored if allDay = true) -->
 </availableTime>
 <notAvailable>  <!-- 0..* Not available during this time due to provided reason -->
  <description value="[string]"/><!-- 1..1 Reason presented to the user explaining why time not available -->
  <during><!-- 0..1 Period Service not available from this date --></during>
 </notAvailable>
 <availabilityExceptions value="[string]"/><!-- 0..1 Description of availability exceptions -->
 <endpoint><!-- 0..* Reference(Endpoint) Technical endpoints providing access to services operated for the practitioner with this role --></endpoint>
</PractitionerRole>
```

**JSON Template**

```

{![doco](help.png)
  "resourceType" : "PractitionerRole",
  // from Resource: id, meta, implicitRules, and language
  // from DomainResource: text, contained, extension, and modifierExtension
  "identifier" : [{ Identifier }], // Business Identifiers that are specific to a role/location
  "active" : <boolean>, // Whether this practitioner role record is in active use
  "period" : { Period }, // The period during which the practitioner is authorized to perform in these role(s)
  "practitioner" : { Reference(Practitioner) }, // Practitioner that is able to provide the defined services for the organization
  "organization" : { Reference(Organization) }, // Organization where the roles are available
  "code" : [{ CodeableConcept }], // Roles which this practitioner may perform
  "specialty" : [{ CodeableConcept }], // Specific specialty of the practitioner
  "location" : [{ Reference(Location) }], // The location(s) at which this practitioner provides care
  "healthcareService" : [{ Reference(HealthcareService) }], // The list of healthcare services that this worker provides for this role's Organization/Location(s)
  "telecom" : [{ ContactPoint }], // Contact details that are specific to the role/location/service
  "availableTime" : [{ // Times the Service Site is available
    "daysOfWeek" : ["<code>"], // mon | tue | wed | thu | fri | sat | sun
    "allDay" : <boolean>, // Always available? e.g. 24 hour service
    "availableStartTime" : "<time>", // Opening time of day (ignored if allDay = true)
    "availableEndTime" : "<time>" // Closing time of day (ignored if allDay = true)
  }],
  "notAvailable" : [{ // Not available during this time due to provided reason
    "description" : "<string>", // R!  Reason presented to the user explaining why time not available
    "during" : { Period } // Service not available from this date
  }],
  "availabilityExceptions" : "<string>", // Description of availability exceptions
  "endpoint" : [{ Reference(Endpoint) }] // Technical endpoints providing access to services operated for the practitioner with this role
}
```

**Turtle Template**

```

@prefix fhir: <http://hl7.org/fhir/> .![doco](help.png)


[ a fhir:PractitionerRole;
  fhir:nodeRole fhir:treeRoot; # if this is the parser root

  # from Resource: .id, .meta, .implicitRules, and .language
  # from DomainResource: .text, .contained, .extension, and .modifierExtension
  fhir:PractitionerRole.identifier [ Identifier ], ... ; # 0..* Business Identifiers that are specific to a role/location
  fhir:PractitionerRole.active [ boolean ]; # 0..1 Whether this practitioner role record is in active use
  fhir:PractitionerRole.period [ Period ]; # 0..1 The period during which the practitioner is authorized to perform in these role(s)
  fhir:PractitionerRole.practitioner [ Reference(Practitioner) ]; # 0..1 Practitioner that is able to provide the defined services for the organization
  fhir:PractitionerRole.organization [ Reference(Organization) ]; # 0..1 Organization where the roles are available
  fhir:PractitionerRole.code [ CodeableConcept ], ... ; # 0..* Roles which this practitioner may perform
  fhir:PractitionerRole.specialty [ CodeableConcept ], ... ; # 0..* Specific specialty of the practitioner
  fhir:PractitionerRole.location [ Reference(Location) ], ... ; # 0..* The location(s) at which this practitioner provides care
  fhir:PractitionerRole.healthcareService [ Reference(HealthcareService) ], ... ; # 0..* The list of healthcare services that this worker provides for this role's Organization/Location(s)
  fhir:PractitionerRole.telecom [ ContactPoint ], ... ; # 0..* Contact details that are specific to the role/location/service
  fhir:PractitionerRole.availableTime [ # 0..* Times the Service Site is available
    fhir:PractitionerRole.availableTime.daysOfWeek [ code ], ... ; # 0..* mon | tue | wed | thu | fri | sat | sun
    fhir:PractitionerRole.availableTime.allDay [ boolean ]; # 0..1 Always available? e.g. 24 hour service
    fhir:PractitionerRole.availableTime.availableStartTime [ time ]; # 0..1 Opening time of day (ignored if allDay = true)
    fhir:PractitionerRole.availableTime.availableEndTime [ time ]; # 0..1 Closing time of day (ignored if allDay = true)
  ], ...;
  fhir:PractitionerRole.notAvailable [ # 0..* Not available during this time due to provided reason
    fhir:PractitionerRole.notAvailable.description [ string ]; # 1..1 Reason presented to the user explaining why time not available
    fhir:PractitionerRole.notAvailable.during [ Period ]; # 0..1 Service not available from this date
  ], ...;
  fhir:PractitionerRole.availabilityExceptions [ string ]; # 0..1 Description of availability exceptions
  fhir:PractitionerRole.endpoint [ Reference(Endpoint) ], ... ; # 0..* Technical endpoints providing access to services operated for the practitioner with this role
]
```

**Changes since R3**

|  |  |
| --- | --- |
| [PractitionerRole](practitionerrole.html#PractitionerRole) |  |
| PractitionerRole.active | - Default Value "true" removed |
| PractitionerRole.availableTime.daysOfWeek | - Change value set from http://hl7.org/fhir/ValueSet/days-of-week to http://hl7.org/fhir/ValueSet/days-of-week|4.0.1 |

See the [Full Difference](diff.html) for further information

This analysis is available as [XML](practitionerrole.diff.xml) or [JSON](practitionerrole.diff.json).

See [R3 <--> R4 Conversion Maps](practitionerrole-version-maps.html) (status = 1 test that all execute ok. All tests pass round-trip testing and all r3 resources are valid.)

**Structure**

| [Name](formats.html#table "The logical name of the element") | [Flags](formats.html#table "Information about the use of the element") | [Card.](formats.html#table "Minimum and Maximum # of times the the element can appear in the instance") | [Type](formats.html#table "Reference to the type of the element") | [Description & Constraints](formats.html#table "Additional information about the element")[doco](formats.html#table "Legend for this format") |
| --- | --- | --- | --- | --- |
| .. [PractitionerRole](practitionerrole-definitions.html#PractitionerRole "PractitionerRole : A specific set of Roles/Locations/specialties/services that a practitioner may perform at an organization for a period of time.") | [TU](versions.html#std-process "Standards Status = Trial Use") |  | [DomainResource](domainresource.html) | Roles/organizations the practitioner is associated with Elements defined in Ancestors: [id](resource.html#Resource "The logical id of the resource, as used in the URL for the resource. Once assigned, this value never changes."), [meta](resource.html#Resource "The metadata about the resource. This is content that is maintained by the infrastructure. Changes to the content might not always be associated with version changes to the resource."), [implicitRules](resource.html#Resource "A reference to a set of rules that were followed when the resource was constructed, and which must be understood when processing the content. Often, this is a reference to an implementation guide that defines the special rules along with other profiles etc."), [language](resource.html#Resource "The base language in which the resource is written."), [text](domainresource.html#DomainResource "A human-readable narrative that contains a summary of the resource and can be used to represent the content of the resource to a human. The narrative need not encode all the structured data, but is required to contain sufficient detail to make it \"clinically safe\" for a human to just read the narrative. Resource definitions may define what content should be represented in the narrative to ensure clinical safety."), [contained](domainresource.html#DomainResource "These resources do not have an independent existence apart from the resource that contains them - they cannot be identified independently, and nor can they have their own independent transaction scope."), [extension](domainresource.html#DomainResource "May be used to represent additional information that is not part of the basic definition of the resource. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension."), [modifierExtension](domainresource.html#DomainResource "May be used to represent additional information that is not part of the basic definition of the resource and that modifies the understanding of the element that contains it and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer is allowed to define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.  Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).") |
| ... [identifier](practitionerrole-definitions.html#PractitionerRole.identifier "PractitionerRole.identifier : Business Identifiers that are specific to a role/location.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [Identifier](datatypes.html#Identifier) | Business Identifiers that are specific to a role/location |
| ... [active](practitionerrole-definitions.html#PractitionerRole.active "PractitionerRole.active : Whether this practitioner role record is in active use.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [boolean](datatypes.html#boolean) | Whether this practitioner role record is in active use |
| ... [period](practitionerrole-definitions.html#PractitionerRole.period "PractitionerRole.period : The period during which the person is authorized to act as a practitioner in these role(s) for the organization.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [Period](datatypes.html#Period) | The period during which the practitioner is authorized to perform in these role(s) |
| ... [practitioner](practitionerrole-definitions.html#PractitionerRole.practitioner "PractitionerRole.practitioner : Practitioner that is able to provide the defined services for the organization.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [Reference](references.html#Reference)([Practitioner](practitioner.html)) | Practitioner that is able to provide the defined services for the organization |
| ... [organization](practitionerrole-definitions.html#PractitionerRole.organization "PractitionerRole.organization : The organization where the Practitioner performs the roles associated.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [Reference](references.html#Reference)([Organization](organization.html)) | Organization where the roles are available |
| ... [code](practitionerrole-definitions.html#PractitionerRole.code "PractitionerRole.code : Roles which this practitioner is authorized to perform for the organization.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [CodeableConcept](datatypes.html#CodeableConcept) | Roles which this practitioner may perform [Practitioner role](valueset-practitioner-role.html "The role a person plays representing an organization.") ([Example](terminologies.html#example "Instances are not expected or even encouraged to draw from the specified value set.  The value set merely provides examples of the types of concepts intended to be included.")) |
| ... [specialty](practitionerrole-definitions.html#PractitionerRole.specialty "PractitionerRole.specialty : Specific specialty of the practitioner.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [CodeableConcept](datatypes.html#CodeableConcept) | Specific specialty of the practitioner [Practice Setting Code Value Set](valueset-c80-practice-codes.html "Specific specialty associated with the agency.") ([Preferred](terminologies.html#preferred "Instances are encouraged to draw from the specified codes for interoperability purposes but are not required to do so to be considered conformant.")) |
| ... [location](practitionerrole-definitions.html#PractitionerRole.location "PractitionerRole.location : The location(s) at which this practitioner provides care.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [Reference](references.html#Reference)([Location](location.html)) | The location(s) at which this practitioner provides care |
| ... [healthcareService](practitionerrole-definitions.html#PractitionerRole.healthcareService "PractitionerRole.healthcareService : The list of healthcare services that this worker provides for this role's Organization/Location(s).") |  | 0..\* | [Reference](references.html#Reference)([HealthcareService](healthcareservice.html)) | The list of healthcare services that this worker provides for this role's Organization/Location(s) |
| ... [telecom](practitionerrole-definitions.html#PractitionerRole.telecom "PractitionerRole.telecom : Contact details that are specific to the role/location/service.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [ContactPoint](datatypes.html#ContactPoint) | Contact details that are specific to the role/location/service |
| ... [availableTime](practitionerrole-definitions.html#PractitionerRole.availableTime "PractitionerRole.availableTime : A collection of times the practitioner is available or performing this role at the location and/or healthcareservice.") |  | 0..\* | [BackboneElement](backboneelement.html) | Times the Service Site is available |
| .... [daysOfWeek](practitionerrole-definitions.html#PractitionerRole.availableTime.daysOfWeek "PractitionerRole.availableTime.daysOfWeek : Indicates which days of the week are available between the start and end Times.") |  | 0..\* | [code](datatypes.html#code) | mon | tue | wed | thu | fri | sat | sun [DaysOfWeek](valueset-days-of-week.html "The days of the week.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| .... [allDay](practitionerrole-definitions.html#PractitionerRole.availableTime.allDay "PractitionerRole.availableTime.allDay : Is this always available? (hence times are irrelevant) e.g. 24 hour service.") |  | 0..1 | [boolean](datatypes.html#boolean) | Always available? e.g. 24 hour service |
| .... [availableStartTime](practitionerrole-definitions.html#PractitionerRole.availableTime.availableStartTime "PractitionerRole.availableTime.availableStartTime : The opening time of day. Note: If the AllDay flag is set, then this time is ignored.") |  | 0..1 | [time](datatypes.html#time) | Opening time of day (ignored if allDay = true) |
| .... [availableEndTime](practitionerrole-definitions.html#PractitionerRole.availableTime.availableEndTime "PractitionerRole.availableTime.availableEndTime : The closing time of day. Note: If the AllDay flag is set, then this time is ignored.") |  | 0..1 | [time](datatypes.html#time) | Closing time of day (ignored if allDay = true) |
| ... [notAvailable](practitionerrole-definitions.html#PractitionerRole.notAvailable "PractitionerRole.notAvailable : The practitioner is not available or performing this role during this period of time due to the provided reason.") |  | 0..\* | [BackboneElement](backboneelement.html) | Not available during this time due to provided reason |
| .... [description](practitionerrole-definitions.html#PractitionerRole.notAvailable.description "PractitionerRole.notAvailable.description : The reason that can be presented to the user as to why this time is not available.") |  | 1..1 | [string](datatypes.html#string) | Reason presented to the user explaining why time not available |
| .... [during](practitionerrole-definitions.html#PractitionerRole.notAvailable.during "PractitionerRole.notAvailable.during : Service is not available (seasonally or for a public holiday) from this date.") |  | 0..1 | [Period](datatypes.html#Period) | Service not available from this date |
| ... [availabilityExceptions](practitionerrole-definitions.html#PractitionerRole.availabilityExceptions "PractitionerRole.availabilityExceptions : A description of site availability exceptions, e.g. public holiday availability. Succinctly describing all possible exceptions to normal site availability as details in the available Times and not available Times.") |  | 0..1 | [string](datatypes.html#string) | Description of availability exceptions |
| ... [endpoint](practitionerrole-definitions.html#PractitionerRole.endpoint "PractitionerRole.endpoint : Technical endpoints providing access to services operated for the practitioner with this role.") |  | 0..\* | [Reference](references.html#Reference)([Endpoint](endpoint.html)) | Technical endpoints providing access to services operated for the practitioner with this role |
| [doco Documentation for this format](formats.html#table "Legend for this format") | | | | |

**UML Diagram** ([Legend](formats.html#uml))

**XML Template**

```

<PractitionerRole xmlns="http://hl7.org/fhir"> ![doco](help.png)
 <!-- from Resource: id, meta, implicitRules, and language -->
 <!-- from DomainResource: text, contained, extension, and modifierExtension -->
 <identifier><!-- 0..* Identifier Business Identifiers that are specific to a role/location --></identifier>
 <active value="[boolean]"/><!-- 0..1 Whether this practitioner role record is in active use -->
 <period><!-- 0..1 Period The period during which the practitioner is authorized to perform in these role(s) --></period>
 <practitioner><!-- 0..1 Reference(Practitioner) Practitioner that is able to provide the defined services for the organization --></practitioner>
 <organization><!-- 0..1 Reference(Organization) Organization where the roles are available --></organization>
 <code><!-- 0..* CodeableConcept Roles which this practitioner may perform --></code>
 <specialty><!-- 0..* CodeableConcept Specific specialty of the practitioner --></specialty>
 <location><!-- 0..* Reference(Location) The location(s) at which this practitioner provides care --></location>
 <healthcareService><!-- 0..* Reference(HealthcareService) The list of healthcare services that this worker provides for this role's Organization/Location(s) --></healthcareService>
 <telecom><!-- 0..* ContactPoint Contact details that are specific to the role/location/service --></telecom>
 <availableTime>  <!-- 0..* Times the Service Site is available -->
  <daysOfWeek value="[code]"/><!-- 0..* mon | tue | wed | thu | fri | sat | sun -->
  <allDay value="[boolean]"/><!-- 0..1 Always available? e.g. 24 hour service -->
  <availableStartTime value="[time]"/><!-- 0..1 Opening time of day (ignored if allDay = true) -->
  <availableEndTime value="[time]"/><!-- 0..1 Closing time of day (ignored if allDay = true) -->
 </availableTime>
 <notAvailable>  <!-- 0..* Not available during this time due to provided reason -->
  <description value="[string]"/><!-- 1..1 Reason presented to the user explaining why time not available -->
  <during><!-- 0..1 Period Service not available from this date --></during>
 </notAvailable>
 <availabilityExceptions value="[string]"/><!-- 0..1 Description of availability exceptions -->
 <endpoint><!-- 0..* Reference(Endpoint) Technical endpoints providing access to services operated for the practitioner with this role --></endpoint>
</PractitionerRole>
```

**JSON Template**

```

{![doco](help.png)
  "resourceType" : "PractitionerRole",
  // from Resource: id, meta, implicitRules, and language
  // from DomainResource: text, contained, extension, and modifierExtension
  "identifier" : [{ Identifier }], // Business Identifiers that are specific to a role/location
  "active" : <boolean>, // Whether this practitioner role record is in active use
  "period" : { Period }, // The period during which the practitioner is authorized to perform in these role(s)
  "practitioner" : { Reference(Practitioner) }, // Practitioner that is able to provide the defined services for the organization
  "organization" : { Reference(Organization) }, // Organization where the roles are available
  "code" : [{ CodeableConcept }], // Roles which this practitioner may perform
  "specialty" : [{ CodeableConcept }], // Specific specialty of the practitioner
  "location" : [{ Reference(Location) }], // The location(s) at which this practitioner provides care
  "healthcareService" : [{ Reference(HealthcareService) }], // The list of healthcare services that this worker provides for this role's Organization/Location(s)
  "telecom" : [{ ContactPoint }], // Contact details that are specific to the role/location/service
  "availableTime" : [{ // Times the Service Site is available
    "daysOfWeek" : ["<code>"], // mon | tue | wed | thu | fri | sat | sun
    "allDay" : <boolean>, // Always available? e.g. 24 hour service
    "availableStartTime" : "<time>", // Opening time of day (ignored if allDay = true)
    "availableEndTime" : "<time>" // Closing time of day (ignored if allDay = true)
  }],
  "notAvailable" : [{ // Not available during this time due to provided reason
    "description" : "<string>", // R!  Reason presented to the user explaining why time not available
    "during" : { Period } // Service not available from this date
  }],
  "availabilityExceptions" : "<string>", // Description of availability exceptions
  "endpoint" : [{ Reference(Endpoint) }] // Technical endpoints providing access to services operated for the practitioner with this role
}
```

**Turtle Template**

```

@prefix fhir: <http://hl7.org/fhir/> .![doco](help.png)


[ a fhir:PractitionerRole;
  fhir:nodeRole fhir:treeRoot; # if this is the parser root

  # from Resource: .id, .meta, .implicitRules, and .language
  # from DomainResource: .text, .contained, .extension, and .modifierExtension
  fhir:PractitionerRole.identifier [ Identifier ], ... ; # 0..* Business Identifiers that are specific to a role/location
  fhir:PractitionerRole.active [ boolean ]; # 0..1 Whether this practitioner role record is in active use
  fhir:PractitionerRole.period [ Period ]; # 0..1 The period during which the practitioner is authorized to perform in these role(s)
  fhir:PractitionerRole.practitioner [ Reference(Practitioner) ]; # 0..1 Practitioner that is able to provide the defined services for the organization
  fhir:PractitionerRole.organization [ Reference(Organization) ]; # 0..1 Organization where the roles are available
  fhir:PractitionerRole.code [ CodeableConcept ], ... ; # 0..* Roles which this practitioner may perform
  fhir:PractitionerRole.specialty [ CodeableConcept ], ... ; # 0..* Specific specialty of the practitioner
  fhir:PractitionerRole.location [ Reference(Location) ], ... ; # 0..* The location(s) at which this practitioner provides care
  fhir:PractitionerRole.healthcareService [ Reference(HealthcareService) ], ... ; # 0..* The list of healthcare services that this worker provides for this role's Organization/Location(s)
  fhir:PractitionerRole.telecom [ ContactPoint ], ... ; # 0..* Contact details that are specific to the role/location/service
  fhir:PractitionerRole.availableTime [ # 0..* Times the Service Site is available
    fhir:PractitionerRole.availableTime.daysOfWeek [ code ], ... ; # 0..* mon | tue | wed | thu | fri | sat | sun
    fhir:PractitionerRole.availableTime.allDay [ boolean ]; # 0..1 Always available? e.g. 24 hour service
    fhir:PractitionerRole.availableTime.availableStartTime [ time ]; # 0..1 Opening time of day (ignored if allDay = true)
    fhir:PractitionerRole.availableTime.availableEndTime [ time ]; # 0..1 Closing time of day (ignored if allDay = true)
  ], ...;
  fhir:PractitionerRole.notAvailable [ # 0..* Not available during this time due to provided reason
    fhir:PractitionerRole.notAvailable.description [ string ]; # 1..1 Reason presented to the user explaining why time not available
    fhir:PractitionerRole.notAvailable.during [ Period ]; # 0..1 Service not available from this date
  ], ...;
  fhir:PractitionerRole.availabilityExceptions [ string ]; # 0..1 Description of availability exceptions
  fhir:PractitionerRole.endpoint [ Reference(Endpoint) ], ... ; # 0..* Technical endpoints providing access to services operated for the practitioner with this role
]
```

**Changes since Release 3**

|  |  |
| --- | --- |
| [PractitionerRole](practitionerrole.html#PractitionerRole) |  |
| PractitionerRole.active | - Default Value "true" removed |
| PractitionerRole.availableTime.daysOfWeek | - Change value set from http://hl7.org/fhir/ValueSet/days-of-week to http://hl7.org/fhir/ValueSet/days-of-week|4.0.1 |

See the [Full Difference](diff.html) for further information

This analysis is available as [XML](practitionerrole.diff.xml) or [JSON](practitionerrole.diff.json).

See [R3 <--> R4 Conversion Maps](practitionerrole-version-maps.html) (status = 1 test that all execute ok. All tests pass round-trip testing and all r3 resources are valid.)

See the [Profiles & Extensions](practitionerrole-profiles.html) and the alternate definitions:
Master Definition [XML](practitionerrole.profile.xml.html) + [JSON](practitionerrole.profile.json.html),
[XML](xml.html) [Schema](practitionerrole.xsd)/[Schematron](practitionerrole.sch) + [JSON](json.html)
[Schema](practitionerrole.schema.json.html), [ShEx](practitionerrole.shex.html) (for [Turtle](rdf.html)) + [see the extensions](practitionerrole-profiles.html) & the [dependency analysis](practitionerrole-dependencies.html)

### 8.5.4.1 Terminology Bindings

| Path | Definition | Type | Reference |
| --- | --- | --- | --- |
| PractitionerRole.code | The role a person plays representing an organization. | [Example](terminologies.html#example) | [PractitionerRole](valueset-practitioner-role.html) |
| PractitionerRole.specialty | Specific specialty associated with the agency. | [Preferred](terminologies.html#preferred) | [PracticeSettingCodeValueSet](valueset-c80-practice-codes.html) |
| PractitionerRole.availableTime.daysOfWeek | The days of the week. | [Required](terminologies.html#required) | [DaysOfWeek](valueset-days-of-week.html) |

## 8.5.5 Notes

- There is no address on the PractitionerRole as the location that is defined here contains the address.  
  This prevents having to duplicate the address values across multiple resources.

## 8.5.6 Multiple Locations in a PractitionerRole

As briefly noted in the boundaries and relationships section the PractitionerRole resource can be used
to represent multiple locations in the one resource instance, however this should be done with care.
When representing multiple locations in an instance, and/or multiple specialties, all details apply
to all locations. Using that approach you cannot differentiate a different contact number, different
availabilities, or different services at each location.  
Hence maintaining these records needs to ensure that when changing a value, such as availability,
it applies to all locations. If different values are required for the different locations, then a new
instance will need to be created, and then split as appropriate. Existing resources referencing the
original PractitionerRole instance will need to be updated to refer to the appropriate record.  
For this reason we expect that it will be common to profile the location element down to a single location,
simplifying overall usage, and the availabilities are clear that they apply to this location, and any
referenced healthcare services.

## 8.5.7 Search Parameters

Search parameters for this resource. The [common parameters](search.html#all) also apply. See [Searching](search.html) for more information about searching in REST, messaging, and services.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Name** | **Type** | **Description** | **Expression** | **In Common** |
| active | [token](search.html#token) | Whether this practitioner role record is in active use | PractitionerRole.active |  |
| date | [date](search.html#date) | The period during which the practitioner is authorized to perform in these role(s) | PractitionerRole.period |  |
| email | [token](search.html#token) | A value in an email contact | PractitionerRole.telecom.where(system='email') | [4 Resources](searchparameter-registry.html#individual-email) |
| endpoint | [reference](search.html#reference) | Technical endpoints providing access to services operated for the practitioner with this role | PractitionerRole.endpoint ([Endpoint](endpoint.html)) |  |
| identifier | [token](search.html#token) | A practitioner's Identifier | PractitionerRole.identifier |  |
| location | [reference](search.html#reference) | One of the locations at which this practitioner provides care | PractitionerRole.location ([Location](location.html)) |  |
| organization | [reference](search.html#reference) | The identity of the organization the practitioner represents / acts on behalf of | PractitionerRole.organization ([Organization](organization.html)) |  |
| phone | [token](search.html#token) | A value in a phone contact | PractitionerRole.telecom.where(system='phone') | [4 Resources](searchparameter-registry.html#individual-phone) |
| practitioner | [reference](search.html#reference) | Practitioner that is able to provide the defined services for the organization | PractitionerRole.practitioner ([Practitioner](practitioner.html)) |  |
| role | [token](search.html#token) | The practitioner can perform this role at for the organization | PractitionerRole.code |  |
| service | [reference](search.html#reference) | The list of healthcare services that this worker provides for this role's Organization/Location(s) | PractitionerRole.healthcareService ([HealthcareService](healthcareservice.html)) |  |
| specialty | [token](search.html#token) | The practitioner has this specialty at an organization | PractitionerRole.specialty |  |
| telecom | [token](search.html#token) | The value in any kind of contact | PractitionerRole.telecom | [4 Resources](searchparameter-registry.html#individual-telecom) |

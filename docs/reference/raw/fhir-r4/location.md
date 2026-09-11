---
id: location
title: Location
source_url: https://hl7.org/fhir/R4/location.html
group: fhir-r4
fhir_version: R4
fetched_at: '2026-09-11T13:22:43Z'
sha256: ddf0521abc1645e3badd52021657cb6a4cc301253d76697798eb9420e75c7480
---
This page is part of the FHIR Specification (v4.0.1: R4 - Mixed [Normative](https://confluence.hl7.org/display/HL7/HL7+Balloting "Normative Standard") and [STU](https://confluence.hl7.org/display/HL7/HL7+Balloting "Standard for Trial-Use")) in it's permanent home (it will always be available at this URL). The current version which supercedes this version is [5.0.0](http://hl7.org/fhir/index.html). For a full list of available versions, see the [Directory of published versions ![](external.png)](http://hl7.org/fhir/directory.html). Page versions: [R5](http://hl7.org/fhir/R5/location.html) [R4B](http://hl7.org/fhir/R4B/location.html) **R4** [R3](http://hl7.org/fhir/STU3/location.html) [R2](http://hl7.org/fhir/DSTU2/location.html)

- [Content](#)
- [Examples](location-examples.html)
- [Detailed Descriptions](location-definitions.html)
- [Mappings](location-mappings.html)
- [Profiles & Extensions](location-profiles.html)
- [R3 Conversions](location-version-maps.html)

# 8.7 Resource Location - Content

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [Patient Administration](http://www.hl7.org/Special/committees/pafm/index.cfm)  Work Group | [Maturity Level](versions.html#maturity): 3 | [Trial Use](versions.html#std-process "Standard Status") | [Security Category](security.html#SecPrivConsiderations): Business | [Compartments](compartmentdefinition.html): Not linked to any defined compartments |

Details and position information for a physical place where services are provided and resources and participants may be stored, found, contained, or accommodated.

## 8.7.1 Scope and Usage

A Location includes both incidental locations (a place which is used for healthcare without prior designation or authorization) and
dedicated, formally appointed locations. Locations may be private, public, mobile or fixed and scale from small
freezers to full hospital buildings or parking garages.

Examples of Locations are:

- Building, ward, corridor, room or bed
- Mobile Clinic
- Freezer, incubator
- Vehicle or lift
- Home, shed, or a garage
- Road, parking place, a park
- Ambulance (generic)
- Ambulance (specific)
- Patient's Home (generic)
- Jurisdiction

These locations are not intended to cover locations on a patient where something occurred
(i.e. a patient's broken leg), but can happily cover the location where the patient broke the leg (the playground)

## 8.7.2 Boundaries and Relationships

Locations and Organizations are very closely related resources and can often be mixed/matched/confused.  
The Location is intended to describe the more physical structures managed/operated by an organization, whereas the Organization is intended to
represent the more conceptual hierarchies, such as a ward.

A Location is valid without an address in cases where it could be purely described by
a geo-coded location in remote areas, or when recorded by a device. Locations with a mode = "kind" would
also likely not have an address, as they are just a type of location, but could also have an address where
they can be found at the address.

Another use of location could be for describing a Jurisdiction. This jurisdiction may be considered a classified boundary
which could be a combination of a physical boundary, and some other discriminator(s):

- Nation - Country-wide community or Federal Government (Ministry of Health)
- Province or State (community or Government)
- Business (throughout an enterprise)
- Business scope (CDC/FDA)
- Business segment (UK Pharmacy)

This resource is referenced by [UsageContext](metadatatypes.html#UsageContext), [Account](account.html#Account), [ActivityDefinition](activitydefinition.html#ActivityDefinition), [AdverseEvent](adverseevent.html#AdverseEvent), [Appointment](appointment.html#Appointment), [AppointmentResponse](appointmentresponse.html#AppointmentResponse), [AuditEvent](auditevent.html#AuditEvent), [CarePlan](careplan.html#CarePlan), [Claim](claim.html#Claim), [ClaimResponse](claimresponse.html#ClaimResponse), [Contract](contract.html#Contract), [CoverageEligibilityRequest](coverageeligibilityrequest.html#CoverageEligibilityRequest), [Device](device.html#Device), [DeviceRequest](devicerequest.html#DeviceRequest), [DiagnosticReport](diagnosticreport.html#DiagnosticReport), [Encounter](encounter.html#Encounter), [ExplanationOfBenefit](explanationofbenefit.html#ExplanationOfBenefit), [Flag](flag.html#Flag), [HealthcareService](healthcareservice.html#HealthcareService), [ImagingStudy](imagingstudy.html#ImagingStudy), [Immunization](immunization.html#Immunization), [InsurancePlan](insuranceplan.html#InsurancePlan), [List](list.html#List), itself, [MeasureReport](measurereport.html#MeasureReport), [Media](media.html#Media), [MedicationDispense](medicationdispense.html#MedicationDispense), [Observation](observation.html#Observation), [OrganizationAffiliation](organizationaffiliation.html#OrganizationAffiliation), [PractitionerRole](practitionerrole.html#PractitionerRole), [Procedure](procedure.html#Procedure), [Provenance](provenance.html#Provenance), [ResearchStudy](researchstudy.html#ResearchStudy), [Schedule](schedule.html#Schedule), [ServiceRequest](servicerequest.html#ServiceRequest), [Specimen](specimen.html#Specimen), [SupplyDelivery](supplydelivery.html#SupplyDelivery), [SupplyRequest](supplyrequest.html#SupplyRequest) and [Task](task.html#Task)

## 8.7.3 Resource Content

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
| .. [Location](location-definitions.html#Location "Location : Details and position information for a physical place where services are provided and resources and participants may be stored, found, contained, or accommodated.") | [TU](versions.html#std-process "Standards Status = Trial Use") |  | [DomainResource](domainresource.html) | Details and position information for a physical place Elements defined in Ancestors: [id](resource.html#Resource "The logical id of the resource, as used in the URL for the resource. Once assigned, this value never changes."), [meta](resource.html#Resource "The metadata about the resource. This is content that is maintained by the infrastructure. Changes to the content might not always be associated with version changes to the resource."), [implicitRules](resource.html#Resource "A reference to a set of rules that were followed when the resource was constructed, and which must be understood when processing the content. Often, this is a reference to an implementation guide that defines the special rules along with other profiles etc."), [language](resource.html#Resource "The base language in which the resource is written."), [text](domainresource.html#DomainResource "A human-readable narrative that contains a summary of the resource and can be used to represent the content of the resource to a human. The narrative need not encode all the structured data, but is required to contain sufficient detail to make it \"clinically safe\" for a human to just read the narrative. Resource definitions may define what content should be represented in the narrative to ensure clinical safety."), [contained](domainresource.html#DomainResource "These resources do not have an independent existence apart from the resource that contains them - they cannot be identified independently, and nor can they have their own independent transaction scope."), [extension](domainresource.html#DomainResource "May be used to represent additional information that is not part of the basic definition of the resource. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension."), [modifierExtension](domainresource.html#DomainResource "May be used to represent additional information that is not part of the basic definition of the resource and that modifies the understanding of the element that contains it and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer is allowed to define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.  Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).") |
| ... [identifier](location-definitions.html#Location.identifier "Location.identifier : Unique code or number identifying the location to its users.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [Identifier](datatypes.html#Identifier) | Unique code or number identifying the location to its users |
| ... [status](location-definitions.html#Location.status "Location.status : The status property covers the general availability of the resource, not the current value which may be covered by the operationStatus, or by a schedule/slots if they are configured for the location.") | [?!](conformance-rules.html#isModifier "This element is a modifier element")[Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [code](datatypes.html#code) | active | suspended | inactive [LocationStatus](valueset-location-status.html "Indicates whether the location is still in use.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ... [operationalStatus](location-definitions.html#Location.operationalStatus "Location.operationalStatus : The operational status covers operation values most relevant to beds (but can also apply to rooms/units/chairs/etc. such as an isolation unit/dialysis chair). This typically covers concepts such as contamination, housekeeping, and other activities like maintenance.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [Coding](datatypes.html#Coding) | The operational status of the location (typically only for a bed/room) [v2 BED STATUS](v2/0116/index.html "The operational status if the location (where typically a bed/room).") ([Preferred](terminologies.html#preferred "Instances are encouraged to draw from the specified codes for interoperability purposes but are not required to do so to be considered conformant.")) |
| ... [name](location-definitions.html#Location.name "Location.name : Name of the location as used by humans. Does not need to be unique.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | Name of the location as used by humans |
| ... [alias](location-definitions.html#Location.alias "Location.alias : A list of alternate names that the location is known as, or was known as, in the past.") |  | 0..\* | [string](datatypes.html#string) | A list of alternate names that the location is known as, or was known as, in the past |
| ... [description](location-definitions.html#Location.description "Location.description : Description of the Location, which helps in finding or referencing the place.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | Additional details about the location that could be displayed as further information to identify the location beyond its name |
| ... [mode](location-definitions.html#Location.mode "Location.mode : Indicates whether a resource instance represents a specific location or a class of locations.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [code](datatypes.html#code) | instance | kind [LocationMode](valueset-location-mode.html "Indicates whether a resource instance represents a specific location or a class of locations.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ... [type](location-definitions.html#Location.type "Location.type : Indicates the type of function performed at the location.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [CodeableConcept](datatypes.html#CodeableConcept) | Type of function performed [V3 Value SetServiceDeliveryLocationRoleType](v3/ServiceDeliveryLocationRoleType/vs.html "Indicates the type of function performed at the location.") ([Extensible](terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept (based on human review), alternate codings (or, data type allowing, text) may be included instead.")) |
| ... [telecom](location-definitions.html#Location.telecom "Location.telecom : The contact details of communication devices available at the location. This can include phone numbers, fax numbers, mobile numbers, email addresses and web sites.") |  | 0..\* | [ContactPoint](datatypes.html#ContactPoint) | Contact details of the location |
| ... [address](location-definitions.html#Location.address "Location.address : Physical location.") |  | 0..1 | [Address](datatypes.html#Address) | Physical location |
| ... [physicalType](location-definitions.html#Location.physicalType "Location.physicalType : Physical form of the location, e.g. building, room, vehicle, road.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Physical form of the location [Location type](valueset-location-physical-type.html "Physical form of the location.") ([Example](terminologies.html#example "Instances are not expected or even encouraged to draw from the specified value set.  The value set merely provides examples of the types of concepts intended to be included.")) |
| ... [position](location-definitions.html#Location.position "Location.position : The absolute geographic location of the Location, expressed using the WGS84 datum (This is the same co-ordinate system used in KML).") |  | 0..1 | [BackboneElement](backboneelement.html) | The absolute geographic location |
| .... [longitude](location-definitions.html#Location.position.longitude "Location.position.longitude : Longitude. The value domain and the interpretation are the same as for the text of the longitude element in KML (see notes below).") |  | 1..1 | [decimal](datatypes.html#decimal) | Longitude with WGS84 datum |
| .... [latitude](location-definitions.html#Location.position.latitude "Location.position.latitude : Latitude. The value domain and the interpretation are the same as for the text of the latitude element in KML (see notes below).") |  | 1..1 | [decimal](datatypes.html#decimal) | Latitude with WGS84 datum |
| .... [altitude](location-definitions.html#Location.position.altitude "Location.position.altitude : Altitude. The value domain and the interpretation are the same as for the text of the altitude element in KML (see notes below).") |  | 0..1 | [decimal](datatypes.html#decimal) | Altitude with WGS84 datum |
| ... [managingOrganization](location-definitions.html#Location.managingOrganization "Location.managingOrganization : The organization responsible for the provisioning and upkeep of the location.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [Reference](references.html#Reference)([Organization](organization.html)) | Organization responsible for provisioning and upkeep |
| ... [partOf](location-definitions.html#Location.partOf "Location.partOf : Another Location of which this Location is physically a part of.") |  | 0..1 | [Reference](references.html#Reference)([Location](location.html)) | Another Location this one is physically a part of |
| ... [hoursOfOperation](location-definitions.html#Location.hoursOfOperation "Location.hoursOfOperation : What days/times during a week is this location usually open.") |  | 0..\* | [BackboneElement](backboneelement.html) | What days/times during a week is this location usually open |
| .... [daysOfWeek](location-definitions.html#Location.hoursOfOperation.daysOfWeek "Location.hoursOfOperation.daysOfWeek : Indicates which days of the week are available between the start and end Times.") |  | 0..\* | [code](datatypes.html#code) | mon | tue | wed | thu | fri | sat | sun [DaysOfWeek](valueset-days-of-week.html "The days of the week.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| .... [allDay](location-definitions.html#Location.hoursOfOperation.allDay "Location.hoursOfOperation.allDay : The Location is open all day.") |  | 0..1 | [boolean](datatypes.html#boolean) | The Location is open all day |
| .... [openingTime](location-definitions.html#Location.hoursOfOperation.openingTime "Location.hoursOfOperation.openingTime : Time that the Location opens.") |  | 0..1 | [time](datatypes.html#time) | Time that the Location opens |
| .... [closingTime](location-definitions.html#Location.hoursOfOperation.closingTime "Location.hoursOfOperation.closingTime : Time that the Location closes.") |  | 0..1 | [time](datatypes.html#time) | Time that the Location closes |
| ... [availabilityExceptions](location-definitions.html#Location.availabilityExceptions "Location.availabilityExceptions : A description of when the locations opening ours are different to normal, e.g. public holiday availability. Succinctly describing all possible exceptions to normal site availability as detailed in the opening hours Times.") |  | 0..1 | [string](datatypes.html#string) | Description of availability exceptions |
| ... [endpoint](location-definitions.html#Location.endpoint "Location.endpoint : Technical endpoints providing access to services operated for the location.") |  | 0..\* | [Reference](references.html#Reference)([Endpoint](endpoint.html)) | Technical endpoints providing access to services operated for the location |
| [doco Documentation for this format](formats.html#table "Legend for this format") | | | | |

**UML Diagram** ([Legend](formats.html#uml))

**XML Template**

```

<Location xmlns="http://hl7.org/fhir"> ![doco](help.png)
 <!-- from Resource: id, meta, implicitRules, and language -->
 <!-- from DomainResource: text, contained, extension, and modifierExtension -->
 <identifier><!-- 0..* Identifier Unique code or number identifying the location to its users --></identifier>
 <status value="[code]"/><!-- 0..1 active | suspended | inactive -->
 <operationalStatus><!-- 0..1 Coding The operational status of the location (typically only for a bed/room) --></operationalStatus>
 <name value="[string]"/><!-- 0..1 Name of the location as used by humans -->
 <alias value="[string]"/><!-- 0..* A list of alternate names that the location is known as, or was known as, in the past -->
 <description value="[string]"/><!-- 0..1 Additional details about the location that could be displayed as further information to identify the location beyond its name -->
 <mode value="[code]"/><!-- 0..1 instance | kind -->
 <type><!-- 0..* CodeableConcept Type of function performed --></type>
 <telecom><!-- 0..* ContactPoint Contact details of the location --></telecom>
 <address><!-- 0..1 Address Physical location --></address>
 <physicalType><!-- 0..1 CodeableConcept Physical form of the location --></physicalType>
 <position>  <!-- 0..1 The absolute geographic location -->
  <longitude value="[decimal]"/><!-- 1..1 Longitude with WGS84 datum -->
  <latitude value="[decimal]"/><!-- 1..1 Latitude with WGS84 datum -->
  <altitude value="[decimal]"/><!-- 0..1 Altitude with WGS84 datum -->
 </position>
 <managingOrganization><!-- 0..1 Reference(Organization) Organization responsible for provisioning and upkeep --></managingOrganization>
 <partOf><!-- 0..1 Reference(Location) Another Location this one is physically a part of --></partOf>
 <hoursOfOperation>  <!-- 0..* What days/times during a week is this location usually open -->
  <daysOfWeek value="[code]"/><!-- 0..* mon | tue | wed | thu | fri | sat | sun -->
  <allDay value="[boolean]"/><!-- 0..1 The Location is open all day -->
  <openingTime value="[time]"/><!-- 0..1 Time that the Location opens -->
  <closingTime value="[time]"/><!-- 0..1 Time that the Location closes -->
 </hoursOfOperation>
 <availabilityExceptions value="[string]"/><!-- 0..1 Description of availability exceptions -->
 <endpoint><!-- 0..* Reference(Endpoint) Technical endpoints providing access to services operated for the location --></endpoint>
</Location>
```

**JSON Template**

```

{![doco](help.png)
  "resourceType" : "Location",
  // from Resource: id, meta, implicitRules, and language
  // from DomainResource: text, contained, extension, and modifierExtension
  "identifier" : [{ Identifier }], // Unique code or number identifying the location to its users
  "status" : "<code>", // active | suspended | inactive
  "operationalStatus" : { Coding }, // The operational status of the location (typically only for a bed/room)
  "name" : "<string>", // Name of the location as used by humans
  "alias" : ["<string>"], // A list of alternate names that the location is known as, or was known as, in the past
  "description" : "<string>", // Additional details about the location that could be displayed as further information to identify the location beyond its name
  "mode" : "<code>", // instance | kind
  "type" : [{ CodeableConcept }], // Type of function performed
  "telecom" : [{ ContactPoint }], // Contact details of the location
  "address" : { Address }, // Physical location
  "physicalType" : { CodeableConcept }, // Physical form of the location
  "position" : { // The absolute geographic location
    "longitude" : <decimal>, // R!  Longitude with WGS84 datum
    "latitude" : <decimal>, // R!  Latitude with WGS84 datum
    "altitude" : <decimal> // Altitude with WGS84 datum
  },
  "managingOrganization" : { Reference(Organization) }, // Organization responsible for provisioning and upkeep
  "partOf" : { Reference(Location) }, // Another Location this one is physically a part of
  "hoursOfOperation" : [{ // What days/times during a week is this location usually open
    "daysOfWeek" : ["<code>"], // mon | tue | wed | thu | fri | sat | sun
    "allDay" : <boolean>, // The Location is open all day
    "openingTime" : "<time>", // Time that the Location opens
    "closingTime" : "<time>" // Time that the Location closes
  }],
  "availabilityExceptions" : "<string>", // Description of availability exceptions
  "endpoint" : [{ Reference(Endpoint) }] // Technical endpoints providing access to services operated for the location
}
```

**Turtle Template**

```

@prefix fhir: <http://hl7.org/fhir/> .![doco](help.png)


[ a fhir:Location;
  fhir:nodeRole fhir:treeRoot; # if this is the parser root

  # from Resource: .id, .meta, .implicitRules, and .language
  # from DomainResource: .text, .contained, .extension, and .modifierExtension
  fhir:Location.identifier [ Identifier ], ... ; # 0..* Unique code or number identifying the location to its users
  fhir:Location.status [ code ]; # 0..1 active | suspended | inactive
  fhir:Location.operationalStatus [ Coding ]; # 0..1 The operational status of the location (typically only for a bed/room)
  fhir:Location.name [ string ]; # 0..1 Name of the location as used by humans
  fhir:Location.alias [ string ], ... ; # 0..* A list of alternate names that the location is known as, or was known as, in the past
  fhir:Location.description [ string ]; # 0..1 Additional details about the location that could be displayed as further information to identify the location beyond its name
  fhir:Location.mode [ code ]; # 0..1 instance | kind
  fhir:Location.type [ CodeableConcept ], ... ; # 0..* Type of function performed
  fhir:Location.telecom [ ContactPoint ], ... ; # 0..* Contact details of the location
  fhir:Location.address [ Address ]; # 0..1 Physical location
  fhir:Location.physicalType [ CodeableConcept ]; # 0..1 Physical form of the location
  fhir:Location.position [ # 0..1 The absolute geographic location
    fhir:Location.position.longitude [ decimal ]; # 1..1 Longitude with WGS84 datum
    fhir:Location.position.latitude [ decimal ]; # 1..1 Latitude with WGS84 datum
    fhir:Location.position.altitude [ decimal ]; # 0..1 Altitude with WGS84 datum
  ];
  fhir:Location.managingOrganization [ Reference(Organization) ]; # 0..1 Organization responsible for provisioning and upkeep
  fhir:Location.partOf [ Reference(Location) ]; # 0..1 Another Location this one is physically a part of
  fhir:Location.hoursOfOperation [ # 0..* What days/times during a week is this location usually open
    fhir:Location.hoursOfOperation.daysOfWeek [ code ], ... ; # 0..* mon | tue | wed | thu | fri | sat | sun
    fhir:Location.hoursOfOperation.allDay [ boolean ]; # 0..1 The Location is open all day
    fhir:Location.hoursOfOperation.openingTime [ time ]; # 0..1 Time that the Location opens
    fhir:Location.hoursOfOperation.closingTime [ time ]; # 0..1 Time that the Location closes
  ], ...;
  fhir:Location.availabilityExceptions [ string ]; # 0..1 Description of availability exceptions
  fhir:Location.endpoint [ Reference(Endpoint) ], ... ; # 0..* Technical endpoints providing access to services operated for the location
]
```

**Changes since R3**

|  |  |
| --- | --- |
| [Location](location.html#Location) |  |
| Location.status | - Change value set from http://hl7.org/fhir/ValueSet/location-status to http://hl7.org/fhir/ValueSet/location-status|4.0.1 |
| Location.mode | - Change value set from http://hl7.org/fhir/ValueSet/location-mode to http://hl7.org/fhir/ValueSet/location-mode|4.0.1 - No longer marked as Modifier |
| Location.type | - Max Cardinality changed from 1 to \* |
| Location.hoursOfOperation | - Added Element |
| Location.hoursOfOperation.daysOfWeek | - Added Element |
| Location.hoursOfOperation.allDay | - Added Element |
| Location.hoursOfOperation.openingTime | - Added Element |
| Location.hoursOfOperation.closingTime | - Added Element |
| Location.availabilityExceptions | - Added Element |

See the [Full Difference](diff.html) for further information

This analysis is available as [XML](location.diff.xml) or [JSON](location.diff.json).

See [R3 <--> R4 Conversion Maps](location-version-maps.html) (status = 6 tests that all execute ok. All tests pass round-trip testing and 1 r3 resources are invalid (0 errors).)

**Structure**

| [Name](formats.html#table "The logical name of the element") | [Flags](formats.html#table "Information about the use of the element") | [Card.](formats.html#table "Minimum and Maximum # of times the the element can appear in the instance") | [Type](formats.html#table "Reference to the type of the element") | [Description & Constraints](formats.html#table "Additional information about the element")[doco](formats.html#table "Legend for this format") |
| --- | --- | --- | --- | --- |
| .. [Location](location-definitions.html#Location "Location : Details and position information for a physical place where services are provided and resources and participants may be stored, found, contained, or accommodated.") | [TU](versions.html#std-process "Standards Status = Trial Use") |  | [DomainResource](domainresource.html) | Details and position information for a physical place Elements defined in Ancestors: [id](resource.html#Resource "The logical id of the resource, as used in the URL for the resource. Once assigned, this value never changes."), [meta](resource.html#Resource "The metadata about the resource. This is content that is maintained by the infrastructure. Changes to the content might not always be associated with version changes to the resource."), [implicitRules](resource.html#Resource "A reference to a set of rules that were followed when the resource was constructed, and which must be understood when processing the content. Often, this is a reference to an implementation guide that defines the special rules along with other profiles etc."), [language](resource.html#Resource "The base language in which the resource is written."), [text](domainresource.html#DomainResource "A human-readable narrative that contains a summary of the resource and can be used to represent the content of the resource to a human. The narrative need not encode all the structured data, but is required to contain sufficient detail to make it \"clinically safe\" for a human to just read the narrative. Resource definitions may define what content should be represented in the narrative to ensure clinical safety."), [contained](domainresource.html#DomainResource "These resources do not have an independent existence apart from the resource that contains them - they cannot be identified independently, and nor can they have their own independent transaction scope."), [extension](domainresource.html#DomainResource "May be used to represent additional information that is not part of the basic definition of the resource. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension."), [modifierExtension](domainresource.html#DomainResource "May be used to represent additional information that is not part of the basic definition of the resource and that modifies the understanding of the element that contains it and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer is allowed to define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.  Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).") |
| ... [identifier](location-definitions.html#Location.identifier "Location.identifier : Unique code or number identifying the location to its users.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [Identifier](datatypes.html#Identifier) | Unique code or number identifying the location to its users |
| ... [status](location-definitions.html#Location.status "Location.status : The status property covers the general availability of the resource, not the current value which may be covered by the operationStatus, or by a schedule/slots if they are configured for the location.") | [?!](conformance-rules.html#isModifier "This element is a modifier element")[Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [code](datatypes.html#code) | active | suspended | inactive [LocationStatus](valueset-location-status.html "Indicates whether the location is still in use.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ... [operationalStatus](location-definitions.html#Location.operationalStatus "Location.operationalStatus : The operational status covers operation values most relevant to beds (but can also apply to rooms/units/chairs/etc. such as an isolation unit/dialysis chair). This typically covers concepts such as contamination, housekeeping, and other activities like maintenance.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [Coding](datatypes.html#Coding) | The operational status of the location (typically only for a bed/room) [v2 BED STATUS](v2/0116/index.html "The operational status if the location (where typically a bed/room).") ([Preferred](terminologies.html#preferred "Instances are encouraged to draw from the specified codes for interoperability purposes but are not required to do so to be considered conformant.")) |
| ... [name](location-definitions.html#Location.name "Location.name : Name of the location as used by humans. Does not need to be unique.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | Name of the location as used by humans |
| ... [alias](location-definitions.html#Location.alias "Location.alias : A list of alternate names that the location is known as, or was known as, in the past.") |  | 0..\* | [string](datatypes.html#string) | A list of alternate names that the location is known as, or was known as, in the past |
| ... [description](location-definitions.html#Location.description "Location.description : Description of the Location, which helps in finding or referencing the place.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | Additional details about the location that could be displayed as further information to identify the location beyond its name |
| ... [mode](location-definitions.html#Location.mode "Location.mode : Indicates whether a resource instance represents a specific location or a class of locations.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [code](datatypes.html#code) | instance | kind [LocationMode](valueset-location-mode.html "Indicates whether a resource instance represents a specific location or a class of locations.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ... [type](location-definitions.html#Location.type "Location.type : Indicates the type of function performed at the location.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [CodeableConcept](datatypes.html#CodeableConcept) | Type of function performed [V3 Value SetServiceDeliveryLocationRoleType](v3/ServiceDeliveryLocationRoleType/vs.html "Indicates the type of function performed at the location.") ([Extensible](terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept (based on human review), alternate codings (or, data type allowing, text) may be included instead.")) |
| ... [telecom](location-definitions.html#Location.telecom "Location.telecom : The contact details of communication devices available at the location. This can include phone numbers, fax numbers, mobile numbers, email addresses and web sites.") |  | 0..\* | [ContactPoint](datatypes.html#ContactPoint) | Contact details of the location |
| ... [address](location-definitions.html#Location.address "Location.address : Physical location.") |  | 0..1 | [Address](datatypes.html#Address) | Physical location |
| ... [physicalType](location-definitions.html#Location.physicalType "Location.physicalType : Physical form of the location, e.g. building, room, vehicle, road.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Physical form of the location [Location type](valueset-location-physical-type.html "Physical form of the location.") ([Example](terminologies.html#example "Instances are not expected or even encouraged to draw from the specified value set.  The value set merely provides examples of the types of concepts intended to be included.")) |
| ... [position](location-definitions.html#Location.position "Location.position : The absolute geographic location of the Location, expressed using the WGS84 datum (This is the same co-ordinate system used in KML).") |  | 0..1 | [BackboneElement](backboneelement.html) | The absolute geographic location |
| .... [longitude](location-definitions.html#Location.position.longitude "Location.position.longitude : Longitude. The value domain and the interpretation are the same as for the text of the longitude element in KML (see notes below).") |  | 1..1 | [decimal](datatypes.html#decimal) | Longitude with WGS84 datum |
| .... [latitude](location-definitions.html#Location.position.latitude "Location.position.latitude : Latitude. The value domain and the interpretation are the same as for the text of the latitude element in KML (see notes below).") |  | 1..1 | [decimal](datatypes.html#decimal) | Latitude with WGS84 datum |
| .... [altitude](location-definitions.html#Location.position.altitude "Location.position.altitude : Altitude. The value domain and the interpretation are the same as for the text of the altitude element in KML (see notes below).") |  | 0..1 | [decimal](datatypes.html#decimal) | Altitude with WGS84 datum |
| ... [managingOrganization](location-definitions.html#Location.managingOrganization "Location.managingOrganization : The organization responsible for the provisioning and upkeep of the location.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [Reference](references.html#Reference)([Organization](organization.html)) | Organization responsible for provisioning and upkeep |
| ... [partOf](location-definitions.html#Location.partOf "Location.partOf : Another Location of which this Location is physically a part of.") |  | 0..1 | [Reference](references.html#Reference)([Location](location.html)) | Another Location this one is physically a part of |
| ... [hoursOfOperation](location-definitions.html#Location.hoursOfOperation "Location.hoursOfOperation : What days/times during a week is this location usually open.") |  | 0..\* | [BackboneElement](backboneelement.html) | What days/times during a week is this location usually open |
| .... [daysOfWeek](location-definitions.html#Location.hoursOfOperation.daysOfWeek "Location.hoursOfOperation.daysOfWeek : Indicates which days of the week are available between the start and end Times.") |  | 0..\* | [code](datatypes.html#code) | mon | tue | wed | thu | fri | sat | sun [DaysOfWeek](valueset-days-of-week.html "The days of the week.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| .... [allDay](location-definitions.html#Location.hoursOfOperation.allDay "Location.hoursOfOperation.allDay : The Location is open all day.") |  | 0..1 | [boolean](datatypes.html#boolean) | The Location is open all day |
| .... [openingTime](location-definitions.html#Location.hoursOfOperation.openingTime "Location.hoursOfOperation.openingTime : Time that the Location opens.") |  | 0..1 | [time](datatypes.html#time) | Time that the Location opens |
| .... [closingTime](location-definitions.html#Location.hoursOfOperation.closingTime "Location.hoursOfOperation.closingTime : Time that the Location closes.") |  | 0..1 | [time](datatypes.html#time) | Time that the Location closes |
| ... [availabilityExceptions](location-definitions.html#Location.availabilityExceptions "Location.availabilityExceptions : A description of when the locations opening ours are different to normal, e.g. public holiday availability. Succinctly describing all possible exceptions to normal site availability as detailed in the opening hours Times.") |  | 0..1 | [string](datatypes.html#string) | Description of availability exceptions |
| ... [endpoint](location-definitions.html#Location.endpoint "Location.endpoint : Technical endpoints providing access to services operated for the location.") |  | 0..\* | [Reference](references.html#Reference)([Endpoint](endpoint.html)) | Technical endpoints providing access to services operated for the location |
| [doco Documentation for this format](formats.html#table "Legend for this format") | | | | |

**UML Diagram** ([Legend](formats.html#uml))

**XML Template**

```

<Location xmlns="http://hl7.org/fhir"> ![doco](help.png)
 <!-- from Resource: id, meta, implicitRules, and language -->
 <!-- from DomainResource: text, contained, extension, and modifierExtension -->
 <identifier><!-- 0..* Identifier Unique code or number identifying the location to its users --></identifier>
 <status value="[code]"/><!-- 0..1 active | suspended | inactive -->
 <operationalStatus><!-- 0..1 Coding The operational status of the location (typically only for a bed/room) --></operationalStatus>
 <name value="[string]"/><!-- 0..1 Name of the location as used by humans -->
 <alias value="[string]"/><!-- 0..* A list of alternate names that the location is known as, or was known as, in the past -->
 <description value="[string]"/><!-- 0..1 Additional details about the location that could be displayed as further information to identify the location beyond its name -->
 <mode value="[code]"/><!-- 0..1 instance | kind -->
 <type><!-- 0..* CodeableConcept Type of function performed --></type>
 <telecom><!-- 0..* ContactPoint Contact details of the location --></telecom>
 <address><!-- 0..1 Address Physical location --></address>
 <physicalType><!-- 0..1 CodeableConcept Physical form of the location --></physicalType>
 <position>  <!-- 0..1 The absolute geographic location -->
  <longitude value="[decimal]"/><!-- 1..1 Longitude with WGS84 datum -->
  <latitude value="[decimal]"/><!-- 1..1 Latitude with WGS84 datum -->
  <altitude value="[decimal]"/><!-- 0..1 Altitude with WGS84 datum -->
 </position>
 <managingOrganization><!-- 0..1 Reference(Organization) Organization responsible for provisioning and upkeep --></managingOrganization>
 <partOf><!-- 0..1 Reference(Location) Another Location this one is physically a part of --></partOf>
 <hoursOfOperation>  <!-- 0..* What days/times during a week is this location usually open -->
  <daysOfWeek value="[code]"/><!-- 0..* mon | tue | wed | thu | fri | sat | sun -->
  <allDay value="[boolean]"/><!-- 0..1 The Location is open all day -->
  <openingTime value="[time]"/><!-- 0..1 Time that the Location opens -->
  <closingTime value="[time]"/><!-- 0..1 Time that the Location closes -->
 </hoursOfOperation>
 <availabilityExceptions value="[string]"/><!-- 0..1 Description of availability exceptions -->
 <endpoint><!-- 0..* Reference(Endpoint) Technical endpoints providing access to services operated for the location --></endpoint>
</Location>
```

**JSON Template**

```

{![doco](help.png)
  "resourceType" : "Location",
  // from Resource: id, meta, implicitRules, and language
  // from DomainResource: text, contained, extension, and modifierExtension
  "identifier" : [{ Identifier }], // Unique code or number identifying the location to its users
  "status" : "<code>", // active | suspended | inactive
  "operationalStatus" : { Coding }, // The operational status of the location (typically only for a bed/room)
  "name" : "<string>", // Name of the location as used by humans
  "alias" : ["<string>"], // A list of alternate names that the location is known as, or was known as, in the past
  "description" : "<string>", // Additional details about the location that could be displayed as further information to identify the location beyond its name
  "mode" : "<code>", // instance | kind
  "type" : [{ CodeableConcept }], // Type of function performed
  "telecom" : [{ ContactPoint }], // Contact details of the location
  "address" : { Address }, // Physical location
  "physicalType" : { CodeableConcept }, // Physical form of the location
  "position" : { // The absolute geographic location
    "longitude" : <decimal>, // R!  Longitude with WGS84 datum
    "latitude" : <decimal>, // R!  Latitude with WGS84 datum
    "altitude" : <decimal> // Altitude with WGS84 datum
  },
  "managingOrganization" : { Reference(Organization) }, // Organization responsible for provisioning and upkeep
  "partOf" : { Reference(Location) }, // Another Location this one is physically a part of
  "hoursOfOperation" : [{ // What days/times during a week is this location usually open
    "daysOfWeek" : ["<code>"], // mon | tue | wed | thu | fri | sat | sun
    "allDay" : <boolean>, // The Location is open all day
    "openingTime" : "<time>", // Time that the Location opens
    "closingTime" : "<time>" // Time that the Location closes
  }],
  "availabilityExceptions" : "<string>", // Description of availability exceptions
  "endpoint" : [{ Reference(Endpoint) }] // Technical endpoints providing access to services operated for the location
}
```

**Turtle Template**

```

@prefix fhir: <http://hl7.org/fhir/> .![doco](help.png)


[ a fhir:Location;
  fhir:nodeRole fhir:treeRoot; # if this is the parser root

  # from Resource: .id, .meta, .implicitRules, and .language
  # from DomainResource: .text, .contained, .extension, and .modifierExtension
  fhir:Location.identifier [ Identifier ], ... ; # 0..* Unique code or number identifying the location to its users
  fhir:Location.status [ code ]; # 0..1 active | suspended | inactive
  fhir:Location.operationalStatus [ Coding ]; # 0..1 The operational status of the location (typically only for a bed/room)
  fhir:Location.name [ string ]; # 0..1 Name of the location as used by humans
  fhir:Location.alias [ string ], ... ; # 0..* A list of alternate names that the location is known as, or was known as, in the past
  fhir:Location.description [ string ]; # 0..1 Additional details about the location that could be displayed as further information to identify the location beyond its name
  fhir:Location.mode [ code ]; # 0..1 instance | kind
  fhir:Location.type [ CodeableConcept ], ... ; # 0..* Type of function performed
  fhir:Location.telecom [ ContactPoint ], ... ; # 0..* Contact details of the location
  fhir:Location.address [ Address ]; # 0..1 Physical location
  fhir:Location.physicalType [ CodeableConcept ]; # 0..1 Physical form of the location
  fhir:Location.position [ # 0..1 The absolute geographic location
    fhir:Location.position.longitude [ decimal ]; # 1..1 Longitude with WGS84 datum
    fhir:Location.position.latitude [ decimal ]; # 1..1 Latitude with WGS84 datum
    fhir:Location.position.altitude [ decimal ]; # 0..1 Altitude with WGS84 datum
  ];
  fhir:Location.managingOrganization [ Reference(Organization) ]; # 0..1 Organization responsible for provisioning and upkeep
  fhir:Location.partOf [ Reference(Location) ]; # 0..1 Another Location this one is physically a part of
  fhir:Location.hoursOfOperation [ # 0..* What days/times during a week is this location usually open
    fhir:Location.hoursOfOperation.daysOfWeek [ code ], ... ; # 0..* mon | tue | wed | thu | fri | sat | sun
    fhir:Location.hoursOfOperation.allDay [ boolean ]; # 0..1 The Location is open all day
    fhir:Location.hoursOfOperation.openingTime [ time ]; # 0..1 Time that the Location opens
    fhir:Location.hoursOfOperation.closingTime [ time ]; # 0..1 Time that the Location closes
  ], ...;
  fhir:Location.availabilityExceptions [ string ]; # 0..1 Description of availability exceptions
  fhir:Location.endpoint [ Reference(Endpoint) ], ... ; # 0..* Technical endpoints providing access to services operated for the location
]
```

**Changes since Release 3**

|  |  |
| --- | --- |
| [Location](location.html#Location) |  |
| Location.status | - Change value set from http://hl7.org/fhir/ValueSet/location-status to http://hl7.org/fhir/ValueSet/location-status|4.0.1 |
| Location.mode | - Change value set from http://hl7.org/fhir/ValueSet/location-mode to http://hl7.org/fhir/ValueSet/location-mode|4.0.1 - No longer marked as Modifier |
| Location.type | - Max Cardinality changed from 1 to \* |
| Location.hoursOfOperation | - Added Element |
| Location.hoursOfOperation.daysOfWeek | - Added Element |
| Location.hoursOfOperation.allDay | - Added Element |
| Location.hoursOfOperation.openingTime | - Added Element |
| Location.hoursOfOperation.closingTime | - Added Element |
| Location.availabilityExceptions | - Added Element |

See the [Full Difference](diff.html) for further information

This analysis is available as [XML](location.diff.xml) or [JSON](location.diff.json).

See [R3 <--> R4 Conversion Maps](location-version-maps.html) (status = 6 tests that all execute ok. All tests pass round-trip testing and 1 r3 resources are invalid (0 errors).)

See the [Profiles & Extensions](location-profiles.html) and the alternate definitions:
Master Definition [XML](location.profile.xml.html) + [JSON](location.profile.json.html),
[XML](xml.html) [Schema](location.xsd)/[Schematron](location.sch) + [JSON](json.html)
[Schema](location.schema.json.html), [ShEx](location.shex.html) (for [Turtle](rdf.html)) + [see the extensions](location-profiles.html) & the [dependency analysis](location-dependencies.html)

### 8.7.3.1 Terminology Bindings

| Path | Definition | Type | Reference |
| --- | --- | --- | --- |
| Location.status | Indicates whether the location is still in use. | [Required](terminologies.html#required) | [LocationStatus](valueset-location-status.html) |
| Location.operationalStatus | The operational status if the location (where typically a bed/room). | [Preferred](terminologies.html#preferred) | [v2.0116](v2/0116/index.html) |
| Location.mode | Indicates whether a resource instance represents a specific location or a class of locations. | [Required](terminologies.html#required) | [LocationMode](valueset-location-mode.html) |
| Location.type | Indicates the type of function performed at the location. | [Extensible](terminologies.html#extensible) | [v3.ServiceDeliveryLocationRoleType](v3/ServiceDeliveryLocationRoleType/vs.html) |
| Location.physicalType | Physical form of the location. | [Example](terminologies.html#example) | [LocationType](valueset-location-physical-type.html) |
| Location.hoursOfOperation.daysOfWeek | The days of the week. | [Required](terminologies.html#required) | [DaysOfWeek](valueset-days-of-week.html) |

## 8.7.4 Notes

- Multiple Organizations or Practitioners may provide services at a Location. These references are not kept in Location, but can be found
  in the models for [Organization](organization.html) and [Practitioner](practitioner.html) instead.
- Locations may range from whole buildings to cabinets; it is possible to relate smaller Locations to their containing bigger Location
  using the Location.partOf element.
- Location.position is expressed using the same syntax, datum and reference system as used in Google Earth's KML files,
  see [Google/OGS's KML ![](external.png)](http://www.opengeospatial.org/standards/kml).

### 8.7.4.1 Location Mode

The Location.mode element can be used to indicate whether a Location resource represents a specific (potentially identifiable) Location ('instance'),
or a class of Locations ('kind'). Especially Resources capturing orders, resource scheduling, plans and definitions may refer to Locations in 'kind' mode.
For these domains, it is often not necessary to refer to a specific Location, but rather to a class of Locations. An example of this is found in planning,
where we need to allocate an "isolation room" for a patient, or need to dispatch "an ambulance" at a certain time. In these cases it is not important
to identify exactly which isolation room or ambulance is allocated, it is sufficient to just indicate a 'kind' of Location.

Note that 'kind' should not be used to represent Locations where an actual instance of a Location was involved, but by identifying missing information.
E.g. when a patient arrived 'by ambulance', but it is not known by which ambulance, this should be represented using a Location in 'instance' mode with a
missing identifier, not a Location of 'kind' ambulance.

Some of Location's data elements are only relevant when mode is 'instance' and should not be used when mode is 'kind':  
*(however this information could still be included if was relevant, such as when it is a generic item,
but not globally generic, e.g. a Burgers Medical Centre ambulance)*

- Location.identifier
- Location.telecom
- Location.address
- Location.position
- Location.status
- Location.managingOrganization

## 8.7.5 Example Location Hierarchy

An example location hierarchy should help give some guidance as to one example
of how a location hierarchy could look within a fictitious Hospital.  
*(The nesting here would be the "part-of" structure of the location)*

```

Hospital A Building C (instance)
    East Wing (instance)
        Level 1 (instance)
            Reception (instance)
            Nurses Station EM-ns1 (instance)
                Medication Cupboard A (instance)
            Room 1 (instance)
                Room 1a (instance) - space in room separatable via a curtain
                    Bed 1a (instance) - always in this room
                Room 1b (instance)
                    Trolley 43 (instance) - moves about
                Room 1d (instance)
                    Trolley 19 (instance) - moves about
                Room 2 (instance)
                    ...
            Theatre EM-TA (instance)
            Coridor (generic)
        Level 2 (instance)
            Reception (instance)
                ...
            Nurses Station EM-ns1 (instance)
                Medication Cupboard A (instance)
            Coridor (generic)
Mobile Services (kind)
    Ambulance (kind)
        Ambulance AMB1 (instance)
        Ambulance AMB2 (instance)
	
```

*Note: Wards/departments are not part of this structure - these would form part of the Organizational Hierarchy.*

### 8.7.5.1 Positional Searching

Searching for locations often require that a facility is within a specified distance of a specified point.
For example, to locate healthcare facilities within 11.2 kms of a client's home, or the current geo-coded
position of a practitioner travelling between patients (read from a mobile phone or device).

```

 GET [base]/Location?near=-83.694810|42.256500|11.20|km...
```

The distance and distance unit parameter components are optional, if the units are missing, kms are to be assumed.
If the distance parameter component is missing, then the server may choose its own interpretation
of what near enough is to be included in the search results.

Note: The STU3 version of this functionality did not support the multiple
separator  `,`  or chaining. The update to this format now supports both of these use cases.  
(And the near-distance was deprecated as a result of this change too)

The distance between the location and the provided point is often used as one of the
determining factors for selection of the location. So this value is included in the results.  
However the value cannot be inside the Location resource as it is different depending on the
point of reference in the search. So the distance between is included in the search section
of the bundle entry. Where multiple near positions are included, the distance to the closest
point provided may be included.

```

<entry> 
    <resource>
        <Location>
            <!-- location details -->
        </Location>
    </resource>
    <search>
        <extension url="http://hl7.org/fhir/StructureDefinition/location-distance">
            <valueDistance >
                <!-- The distance that this location resource is from the provided point in the query -->
                <value value="10.5"/>
                <unit value="km"/>
            </valueDistance>
        </extension>
    </search>
</entry> 
```

## 8.7.6 Search Parameters

Search parameters for this resource. The [common parameters](search.html#all) also apply. See [Searching](search.html) for more information about searching in REST, messaging, and services.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Name** | **Type** | **Description** | **Expression** | **In Common** |
| address | [string](search.html#string) | A (part of the) address of the location | Location.address |  |
| address-city | [string](search.html#string) | A city specified in an address | Location.address.city |  |
| address-country | [string](search.html#string) | A country specified in an address | Location.address.country |  |
| address-postalcode | [string](search.html#string) | A postal code specified in an address | Location.address.postalCode |  |
| address-state | [string](search.html#string) | A state specified in an address | Location.address.state |  |
| address-use | [token](search.html#token) | A use code specified in an address | Location.address.use |  |
| endpoint | [reference](search.html#reference) | Technical endpoints providing access to services operated for the location | Location.endpoint ([Endpoint](endpoint.html)) |  |
| identifier | [token](search.html#token) | An identifier for the location | Location.identifier |  |
| name | [string](search.html#string) | A portion of the location's name or alias | Location.name | Location.alias |  |
| near | [special](search.html#special) | Search for locations where the location.position is near to, or within a specified distance of, the provided coordinates expressed as [latitude]|[longitude]|[distance]|[units] (using the WGS84 datum, see notes). If the units are omitted, then kms should be assumed. If the distance is omitted, then the server can use its own discretion as to what distances should be considered near (and units are irrelevant) Servers may search using various techniques that might have differing accuracies, depending on implementation efficiency. Requires the near-distance parameter to be provided also | Location.position |  |
| operational-status | [token](search.html#token) | Searches for locations (typically bed/room) that have an operational status (e.g. contaminated, housekeeping) | Location.operationalStatus |  |
| organization | [reference](search.html#reference) | Searches for locations that are managed by the provided organization | Location.managingOrganization ([Organization](organization.html)) |  |
| partof | [reference](search.html#reference) | A location of which this location is a part | Location.partOf ([Location](location.html)) |  |
| status | [token](search.html#token) | Searches for locations with a specific kind of status | Location.status |  |
| type | [token](search.html#token) | A code for the type of location | Location.type |  |

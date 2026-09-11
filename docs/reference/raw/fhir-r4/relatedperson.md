---
id: relatedperson
title: RelatedPerson
source_url: https://hl7.org/fhir/R4/relatedperson.html
group: fhir-r4
fhir_version: R4
fetched_at: '2026-09-11T13:23:11Z'
sha256: 2f558709f7f0f5e94fb0c87af19ca333fa4ee0cc9974611a990308698a237f05
---
This page is part of the FHIR Specification (v4.0.1: R4 - Mixed [Normative](https://confluence.hl7.org/display/HL7/HL7+Balloting "Normative Standard") and [STU](https://confluence.hl7.org/display/HL7/HL7+Balloting "Standard for Trial-Use")) in it's permanent home (it will always be available at this URL). The current version which supercedes this version is [5.0.0](http://hl7.org/fhir/index.html). For a full list of available versions, see the [Directory of published versions ![](external.png)](http://hl7.org/fhir/directory.html). Page versions: [R5](http://hl7.org/fhir/R5/relatedperson.html) [R4B](http://hl7.org/fhir/R4B/relatedperson.html) **R4** [R3](http://hl7.org/fhir/STU3/relatedperson.html) [R2](http://hl7.org/fhir/DSTU2/relatedperson.html)

- [Content](#)
- [Examples](relatedperson-examples.html)
- [Detailed Descriptions](relatedperson-definitions.html)
- [Mappings](relatedperson-mappings.html)
- [Profiles & Extensions](relatedperson-profiles.html)
- [R3 Conversions](relatedperson-version-maps.html)

# 8.2 Resource RelatedPerson - Content

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [Patient Administration](http://www.hl7.org/Special/committees/pafm/index.cfm)  Work Group | [Maturity Level](versions.html#maturity): 2 | [Trial Use](versions.html#std-process "Standard Status") | [Security Category](security.html#SecPrivConsiderations): Patient | [Compartments](compartmentdefinition.html): [Patient](compartmentdefinition-patient.html), [RelatedPerson](compartmentdefinition-relatedperson.html) |

Information about a person that is involved in the care for a patient, but who is not the target of healthcare, nor has a formal responsibility in the care process.

## 8.2.1 Scope and Usage

RelatedPersons typically have a personal or non-healthcare-specific professional relationship to the patient. A RelatedPerson
resource is primarily used for attribution of information,
since RelatedPersons are often a source of information about the patient.
For keeping information about people for contact purposes for a patient, use a Patient's Contact element.
Some individuals may serve as both a Patient's Contact and a Related Person.

Example RelatedPersons are:

- A patient's wife or husband
- A patient's relatives or friends
- A neighbor bringing a patient to the hospital
- The owner or trainer of a horse
- A patient's attorney or guardian
- A Guide Dog

## 8.2.2 Boundaries and Relationships

The primary distinction between a Practitioner and a RelatedPerson is based on whether:

- The person/animal operates on behalf of the care delivery organization over multiple patients (Practitioner) or,
- Where the person/animal is not associated with the organization, and instead is
  allocated tasks specifically for the RelatedPerson's Patient (RelatedPerson).

A standard extension [animalSpecies](extension-practitioner-animalspecies.html) can be used to indicate the species of a service animal.

This resource is referenced by [Annotation](datatypes.html#Annotation), [Signature](datatypes.html#Signature), [Account](account.html#Account), [AdverseEvent](adverseevent.html#AdverseEvent), [AllergyIntolerance](allergyintolerance.html#AllergyIntolerance), [Appointment](appointment.html#Appointment), [AppointmentResponse](appointmentresponse.html#AppointmentResponse), [AuditEvent](auditevent.html#AuditEvent), [Basic](basic.html#Basic), [CarePlan](careplan.html#CarePlan), [CareTeam](careteam.html#CareTeam), [ChargeItem](chargeitem.html#ChargeItem), [Claim](claim.html#Claim), [Communication](communication.html#Communication), [CommunicationRequest](communicationrequest.html#CommunicationRequest), [Composition](composition.html#Composition), [Condition](condition.html#Condition), [Consent](consent.html#Consent), [Contract](contract.html#Contract), [Coverage](coverage.html#Coverage), [DeviceRequest](devicerequest.html#DeviceRequest), [DeviceUseStatement](deviceusestatement.html#DeviceUseStatement), [DocumentManifest](documentmanifest.html#DocumentManifest), [DocumentReference](documentreference.html#DocumentReference), [Encounter](encounter.html#Encounter), [ExplanationOfBenefit](explanationofbenefit.html#ExplanationOfBenefit), [Goal](goal.html#Goal), [Group](group.html#Group), [ImagingStudy](imagingstudy.html#ImagingStudy), [Invoice](invoice.html#Invoice), [MeasureReport](measurereport.html#MeasureReport), [Media](media.html#Media), [MedicationAdministration](medicationadministration.html#MedicationAdministration), [MedicationDispense](medicationdispense.html#MedicationDispense), [MedicationRequest](medicationrequest.html#MedicationRequest), [MedicationStatement](medicationstatement.html#MedicationStatement), [Observation](observation.html#Observation), [Patient](patient.html#Patient), [Person](person.html#Person), [Procedure](procedure.html#Procedure), [Provenance](provenance.html#Provenance), [QuestionnaireResponse](questionnaireresponse.html#QuestionnaireResponse), [RequestGroup](requestgroup.html#RequestGroup), [Schedule](schedule.html#Schedule), [ServiceRequest](servicerequest.html#ServiceRequest), [SupplyRequest](supplyrequest.html#SupplyRequest) and [Task](task.html#Task)

## 8.2.3 Resource Content

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
| .. [RelatedPerson](relatedperson-definitions.html#RelatedPerson "RelatedPerson : Information about a person that is involved in the care for a patient, but who is not the target of healthcare, nor has a formal responsibility in the care process.") | [TU](versions.html#std-process "Standards Status = Trial Use") |  | [DomainResource](domainresource.html) | A person that is related to a patient, but who is not a direct target of care Elements defined in Ancestors: [id](resource.html#Resource "The logical id of the resource, as used in the URL for the resource. Once assigned, this value never changes."), [meta](resource.html#Resource "The metadata about the resource. This is content that is maintained by the infrastructure. Changes to the content might not always be associated with version changes to the resource."), [implicitRules](resource.html#Resource "A reference to a set of rules that were followed when the resource was constructed, and which must be understood when processing the content. Often, this is a reference to an implementation guide that defines the special rules along with other profiles etc."), [language](resource.html#Resource "The base language in which the resource is written."), [text](domainresource.html#DomainResource "A human-readable narrative that contains a summary of the resource and can be used to represent the content of the resource to a human. The narrative need not encode all the structured data, but is required to contain sufficient detail to make it \"clinically safe\" for a human to just read the narrative. Resource definitions may define what content should be represented in the narrative to ensure clinical safety."), [contained](domainresource.html#DomainResource "These resources do not have an independent existence apart from the resource that contains them - they cannot be identified independently, and nor can they have their own independent transaction scope."), [extension](domainresource.html#DomainResource "May be used to represent additional information that is not part of the basic definition of the resource. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension."), [modifierExtension](domainresource.html#DomainResource "May be used to represent additional information that is not part of the basic definition of the resource and that modifies the understanding of the element that contains it and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer is allowed to define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.  Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).") |
| ... [identifier](relatedperson-definitions.html#RelatedPerson.identifier "RelatedPerson.identifier : Identifier for a person within a particular scope.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [Identifier](datatypes.html#Identifier) | A human identifier for this person |
| ... [active](relatedperson-definitions.html#RelatedPerson.active "RelatedPerson.active : Whether this related person record is in active use.") | [?!](conformance-rules.html#isModifier "This element is a modifier element")[Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [boolean](datatypes.html#boolean) | Whether this related person's record is in active use |
| ... [patient](relatedperson-definitions.html#RelatedPerson.patient "RelatedPerson.patient : The patient this person is related to.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [Reference](references.html#Reference)([Patient](patient.html)) | The patient this person is related to |
| ... [relationship](relatedperson-definitions.html#RelatedPerson.relationship "RelatedPerson.relationship : The nature of the relationship between a patient and the related person.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [CodeableConcept](datatypes.html#CodeableConcept) | The nature of the relationship [Patient relationship type](valueset-relatedperson-relationshiptype.html "The nature of the relationship between a patient and the related person.") ([Preferred](terminologies.html#preferred "Instances are encouraged to draw from the specified codes for interoperability purposes but are not required to do so to be considered conformant.")) |
| ... [name](relatedperson-definitions.html#RelatedPerson.name "RelatedPerson.name : A name associated with the person.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [HumanName](datatypes.html#HumanName) | A name associated with the person |
| ... [telecom](relatedperson-definitions.html#RelatedPerson.telecom "RelatedPerson.telecom : A contact detail for the person, e.g. a telephone number or an email address.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [ContactPoint](datatypes.html#ContactPoint) | A contact detail for the person |
| ... [gender](relatedperson-definitions.html#RelatedPerson.gender "RelatedPerson.gender : Administrative Gender - the gender that the person is considered to have for administration and record keeping purposes.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [code](datatypes.html#code) | male | female | other | unknown [AdministrativeGender](valueset-administrative-gender.html "The gender of a person used for administrative purposes.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ... [birthDate](relatedperson-definitions.html#RelatedPerson.birthDate "RelatedPerson.birthDate : The date on which the related person was born.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [date](datatypes.html#date) | The date on which the related person was born |
| ... [address](relatedperson-definitions.html#RelatedPerson.address "RelatedPerson.address : Address where the related person can be contacted or visited.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [Address](datatypes.html#Address) | Address where the related person can be contacted or visited |
| ... [photo](relatedperson-definitions.html#RelatedPerson.photo "RelatedPerson.photo : Image of the person.") |  | 0..\* | [Attachment](datatypes.html#Attachment) | Image of the person |
| ... [period](relatedperson-definitions.html#RelatedPerson.period "RelatedPerson.period : The period of time during which this relationship is or was active. If there are no dates defined, then the interval is unknown.") |  | 0..1 | [Period](datatypes.html#Period) | Period of time that this relationship is considered valid |
| ... [communication](relatedperson-definitions.html#RelatedPerson.communication "RelatedPerson.communication : A language which may be used to communicate with about the patient's health.") |  | 0..\* | [BackboneElement](backboneelement.html) | A language which may be used to communicate with about the patient's health |
| .... [language](relatedperson-definitions.html#RelatedPerson.communication.language "RelatedPerson.communication.language : The ISO-639-1 alpha 2 code in lower case for the language, optionally followed by a hyphen and the ISO-3166-1 alpha 2 code for the region in upper case; e.g. \"en\" for English, or \"en-US\" for American English versus \"en-EN\" for England English.") |  | 1..1 | [CodeableConcept](datatypes.html#CodeableConcept) | The language which can be used to communicate with the patient about his or her health [Common Languages](valueset-languages.html "A human language.") ([Preferred](terminologies.html#preferred "Instances are encouraged to draw from the specified codes for interoperability purposes but are not required to do so to be considered conformant.") but limited to [AllLanguages](valueset-all-languages.html)) |
| .... [preferred](relatedperson-definitions.html#RelatedPerson.communication.preferred "RelatedPerson.communication.preferred : Indicates whether or not the patient prefers this language (over other languages he masters up a certain level).") |  | 0..1 | [boolean](datatypes.html#boolean) | Language preference indicator |
| [doco Documentation for this format](formats.html#table "Legend for this format") | | | | |

**UML Diagram** ([Legend](formats.html#uml))

**XML Template**

```

<RelatedPerson xmlns="http://hl7.org/fhir"> ![doco](help.png)
 <!-- from Resource: id, meta, implicitRules, and language -->
 <!-- from DomainResource: text, contained, extension, and modifierExtension -->
 <identifier><!-- 0..* Identifier A human identifier for this person --></identifier>
 <active value="[boolean]"/><!-- 0..1 Whether this related person's record is in active use -->
 <patient><!-- 1..1 Reference(Patient) The patient this person is related to --></patient>
 <relationship><!-- 0..* CodeableConcept The nature of the relationship --></relationship>
 <name><!-- 0..* HumanName A name associated with the person --></name>
 <telecom><!-- 0..* ContactPoint A contact detail for the person --></telecom>
 <gender value="[code]"/><!-- 0..1 male | female | other | unknown -->
 <birthDate value="[date]"/><!-- 0..1 The date on which the related person was born -->
 <address><!-- 0..* Address Address where the related person can be contacted or visited --></address>
 <photo><!-- 0..* Attachment Image of the person --></photo>
 <period><!-- 0..1 Period Period of time that this relationship is considered valid --></period>
 <communication>  <!-- 0..* A language which may be used to communicate with about the patient's health -->
  <language><!-- 1..1 CodeableConcept The language which can be used to communicate with the patient about his or her health --></language>
  <preferred value="[boolean]"/><!-- 0..1 Language preference indicator -->
 </communication>
</RelatedPerson>
```

**JSON Template**

```

{![doco](help.png)
  "resourceType" : "RelatedPerson",
  // from Resource: id, meta, implicitRules, and language
  // from DomainResource: text, contained, extension, and modifierExtension
  "identifier" : [{ Identifier }], // A human identifier for this person
  "active" : <boolean>, // Whether this related person's record is in active use
  "patient" : { Reference(Patient) }, // R!  The patient this person is related to
  "relationship" : [{ CodeableConcept }], // The nature of the relationship
  "name" : [{ HumanName }], // A name associated with the person
  "telecom" : [{ ContactPoint }], // A contact detail for the person
  "gender" : "<code>", // male | female | other | unknown
  "birthDate" : "<date>", // The date on which the related person was born
  "address" : [{ Address }], // Address where the related person can be contacted or visited
  "photo" : [{ Attachment }], // Image of the person
  "period" : { Period }, // Period of time that this relationship is considered valid
  "communication" : [{ // A language which may be used to communicate with about the patient's health
    "language" : { CodeableConcept }, // R!  The language which can be used to communicate with the patient about his or her health
    "preferred" : <boolean> // Language preference indicator
  }]
}
```

**Turtle Template**

```

@prefix fhir: <http://hl7.org/fhir/> .![doco](help.png)


[ a fhir:RelatedPerson;
  fhir:nodeRole fhir:treeRoot; # if this is the parser root

  # from Resource: .id, .meta, .implicitRules, and .language
  # from DomainResource: .text, .contained, .extension, and .modifierExtension
  fhir:RelatedPerson.identifier [ Identifier ], ... ; # 0..* A human identifier for this person
  fhir:RelatedPerson.active [ boolean ]; # 0..1 Whether this related person's record is in active use
  fhir:RelatedPerson.patient [ Reference(Patient) ]; # 1..1 The patient this person is related to
  fhir:RelatedPerson.relationship [ CodeableConcept ], ... ; # 0..* The nature of the relationship
  fhir:RelatedPerson.name [ HumanName ], ... ; # 0..* A name associated with the person
  fhir:RelatedPerson.telecom [ ContactPoint ], ... ; # 0..* A contact detail for the person
  fhir:RelatedPerson.gender [ code ]; # 0..1 male | female | other | unknown
  fhir:RelatedPerson.birthDate [ date ]; # 0..1 The date on which the related person was born
  fhir:RelatedPerson.address [ Address ], ... ; # 0..* Address where the related person can be contacted or visited
  fhir:RelatedPerson.photo [ Attachment ], ... ; # 0..* Image of the person
  fhir:RelatedPerson.period [ Period ]; # 0..1 Period of time that this relationship is considered valid
  fhir:RelatedPerson.communication [ # 0..* A language which may be used to communicate with about the patient's health
    fhir:RelatedPerson.communication.language [ CodeableConcept ]; # 1..1 The language which can be used to communicate with the patient about his or her health
    fhir:RelatedPerson.communication.preferred [ boolean ]; # 0..1 Language preference indicator
  ], ...;
]
```

**Changes since R3**

|  |  |
| --- | --- |
| [RelatedPerson](relatedperson.html#RelatedPerson) |  |
| RelatedPerson.active | - Default Value "true" removed |
| RelatedPerson.relationship | - Max Cardinality changed from 1 to \* |
| RelatedPerson.gender | - Change value set from http://hl7.org/fhir/ValueSet/administrative-gender to http://hl7.org/fhir/ValueSet/administrative-gender|4.0.1 |
| RelatedPerson.communication | - Added Element |
| RelatedPerson.communication.language | - **Added Mandatory Element** |
| RelatedPerson.communication.preferred | - Added Element |

See the [Full Difference](diff.html) for further information

This analysis is available as [XML](relatedperson.diff.xml) or [JSON](relatedperson.diff.json).

See [R3 <--> R4 Conversion Maps](relatedperson-version-maps.html) (status = 4 tests that all execute ok. All tests pass round-trip testing and all r3 resources are valid.)

**Structure**

| [Name](formats.html#table "The logical name of the element") | [Flags](formats.html#table "Information about the use of the element") | [Card.](formats.html#table "Minimum and Maximum # of times the the element can appear in the instance") | [Type](formats.html#table "Reference to the type of the element") | [Description & Constraints](formats.html#table "Additional information about the element")[doco](formats.html#table "Legend for this format") |
| --- | --- | --- | --- | --- |
| .. [RelatedPerson](relatedperson-definitions.html#RelatedPerson "RelatedPerson : Information about a person that is involved in the care for a patient, but who is not the target of healthcare, nor has a formal responsibility in the care process.") | [TU](versions.html#std-process "Standards Status = Trial Use") |  | [DomainResource](domainresource.html) | A person that is related to a patient, but who is not a direct target of care Elements defined in Ancestors: [id](resource.html#Resource "The logical id of the resource, as used in the URL for the resource. Once assigned, this value never changes."), [meta](resource.html#Resource "The metadata about the resource. This is content that is maintained by the infrastructure. Changes to the content might not always be associated with version changes to the resource."), [implicitRules](resource.html#Resource "A reference to a set of rules that were followed when the resource was constructed, and which must be understood when processing the content. Often, this is a reference to an implementation guide that defines the special rules along with other profiles etc."), [language](resource.html#Resource "The base language in which the resource is written."), [text](domainresource.html#DomainResource "A human-readable narrative that contains a summary of the resource and can be used to represent the content of the resource to a human. The narrative need not encode all the structured data, but is required to contain sufficient detail to make it \"clinically safe\" for a human to just read the narrative. Resource definitions may define what content should be represented in the narrative to ensure clinical safety."), [contained](domainresource.html#DomainResource "These resources do not have an independent existence apart from the resource that contains them - they cannot be identified independently, and nor can they have their own independent transaction scope."), [extension](domainresource.html#DomainResource "May be used to represent additional information that is not part of the basic definition of the resource. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension."), [modifierExtension](domainresource.html#DomainResource "May be used to represent additional information that is not part of the basic definition of the resource and that modifies the understanding of the element that contains it and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer is allowed to define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.  Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).") |
| ... [identifier](relatedperson-definitions.html#RelatedPerson.identifier "RelatedPerson.identifier : Identifier for a person within a particular scope.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [Identifier](datatypes.html#Identifier) | A human identifier for this person |
| ... [active](relatedperson-definitions.html#RelatedPerson.active "RelatedPerson.active : Whether this related person record is in active use.") | [?!](conformance-rules.html#isModifier "This element is a modifier element")[Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [boolean](datatypes.html#boolean) | Whether this related person's record is in active use |
| ... [patient](relatedperson-definitions.html#RelatedPerson.patient "RelatedPerson.patient : The patient this person is related to.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [Reference](references.html#Reference)([Patient](patient.html)) | The patient this person is related to |
| ... [relationship](relatedperson-definitions.html#RelatedPerson.relationship "RelatedPerson.relationship : The nature of the relationship between a patient and the related person.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [CodeableConcept](datatypes.html#CodeableConcept) | The nature of the relationship [Patient relationship type](valueset-relatedperson-relationshiptype.html "The nature of the relationship between a patient and the related person.") ([Preferred](terminologies.html#preferred "Instances are encouraged to draw from the specified codes for interoperability purposes but are not required to do so to be considered conformant.")) |
| ... [name](relatedperson-definitions.html#RelatedPerson.name "RelatedPerson.name : A name associated with the person.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [HumanName](datatypes.html#HumanName) | A name associated with the person |
| ... [telecom](relatedperson-definitions.html#RelatedPerson.telecom "RelatedPerson.telecom : A contact detail for the person, e.g. a telephone number or an email address.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [ContactPoint](datatypes.html#ContactPoint) | A contact detail for the person |
| ... [gender](relatedperson-definitions.html#RelatedPerson.gender "RelatedPerson.gender : Administrative Gender - the gender that the person is considered to have for administration and record keeping purposes.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [code](datatypes.html#code) | male | female | other | unknown [AdministrativeGender](valueset-administrative-gender.html "The gender of a person used for administrative purposes.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ... [birthDate](relatedperson-definitions.html#RelatedPerson.birthDate "RelatedPerson.birthDate : The date on which the related person was born.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [date](datatypes.html#date) | The date on which the related person was born |
| ... [address](relatedperson-definitions.html#RelatedPerson.address "RelatedPerson.address : Address where the related person can be contacted or visited.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [Address](datatypes.html#Address) | Address where the related person can be contacted or visited |
| ... [photo](relatedperson-definitions.html#RelatedPerson.photo "RelatedPerson.photo : Image of the person.") |  | 0..\* | [Attachment](datatypes.html#Attachment) | Image of the person |
| ... [period](relatedperson-definitions.html#RelatedPerson.period "RelatedPerson.period : The period of time during which this relationship is or was active. If there are no dates defined, then the interval is unknown.") |  | 0..1 | [Period](datatypes.html#Period) | Period of time that this relationship is considered valid |
| ... [communication](relatedperson-definitions.html#RelatedPerson.communication "RelatedPerson.communication : A language which may be used to communicate with about the patient's health.") |  | 0..\* | [BackboneElement](backboneelement.html) | A language which may be used to communicate with about the patient's health |
| .... [language](relatedperson-definitions.html#RelatedPerson.communication.language "RelatedPerson.communication.language : The ISO-639-1 alpha 2 code in lower case for the language, optionally followed by a hyphen and the ISO-3166-1 alpha 2 code for the region in upper case; e.g. \"en\" for English, or \"en-US\" for American English versus \"en-EN\" for England English.") |  | 1..1 | [CodeableConcept](datatypes.html#CodeableConcept) | The language which can be used to communicate with the patient about his or her health [Common Languages](valueset-languages.html "A human language.") ([Preferred](terminologies.html#preferred "Instances are encouraged to draw from the specified codes for interoperability purposes but are not required to do so to be considered conformant.") but limited to [AllLanguages](valueset-all-languages.html)) |
| .... [preferred](relatedperson-definitions.html#RelatedPerson.communication.preferred "RelatedPerson.communication.preferred : Indicates whether or not the patient prefers this language (over other languages he masters up a certain level).") |  | 0..1 | [boolean](datatypes.html#boolean) | Language preference indicator |
| [doco Documentation for this format](formats.html#table "Legend for this format") | | | | |

**UML Diagram** ([Legend](formats.html#uml))

**XML Template**

```

<RelatedPerson xmlns="http://hl7.org/fhir"> ![doco](help.png)
 <!-- from Resource: id, meta, implicitRules, and language -->
 <!-- from DomainResource: text, contained, extension, and modifierExtension -->
 <identifier><!-- 0..* Identifier A human identifier for this person --></identifier>
 <active value="[boolean]"/><!-- 0..1 Whether this related person's record is in active use -->
 <patient><!-- 1..1 Reference(Patient) The patient this person is related to --></patient>
 <relationship><!-- 0..* CodeableConcept The nature of the relationship --></relationship>
 <name><!-- 0..* HumanName A name associated with the person --></name>
 <telecom><!-- 0..* ContactPoint A contact detail for the person --></telecom>
 <gender value="[code]"/><!-- 0..1 male | female | other | unknown -->
 <birthDate value="[date]"/><!-- 0..1 The date on which the related person was born -->
 <address><!-- 0..* Address Address where the related person can be contacted or visited --></address>
 <photo><!-- 0..* Attachment Image of the person --></photo>
 <period><!-- 0..1 Period Period of time that this relationship is considered valid --></period>
 <communication>  <!-- 0..* A language which may be used to communicate with about the patient's health -->
  <language><!-- 1..1 CodeableConcept The language which can be used to communicate with the patient about his or her health --></language>
  <preferred value="[boolean]"/><!-- 0..1 Language preference indicator -->
 </communication>
</RelatedPerson>
```

**JSON Template**

```

{![doco](help.png)
  "resourceType" : "RelatedPerson",
  // from Resource: id, meta, implicitRules, and language
  // from DomainResource: text, contained, extension, and modifierExtension
  "identifier" : [{ Identifier }], // A human identifier for this person
  "active" : <boolean>, // Whether this related person's record is in active use
  "patient" : { Reference(Patient) }, // R!  The patient this person is related to
  "relationship" : [{ CodeableConcept }], // The nature of the relationship
  "name" : [{ HumanName }], // A name associated with the person
  "telecom" : [{ ContactPoint }], // A contact detail for the person
  "gender" : "<code>", // male | female | other | unknown
  "birthDate" : "<date>", // The date on which the related person was born
  "address" : [{ Address }], // Address where the related person can be contacted or visited
  "photo" : [{ Attachment }], // Image of the person
  "period" : { Period }, // Period of time that this relationship is considered valid
  "communication" : [{ // A language which may be used to communicate with about the patient's health
    "language" : { CodeableConcept }, // R!  The language which can be used to communicate with the patient about his or her health
    "preferred" : <boolean> // Language preference indicator
  }]
}
```

**Turtle Template**

```

@prefix fhir: <http://hl7.org/fhir/> .![doco](help.png)


[ a fhir:RelatedPerson;
  fhir:nodeRole fhir:treeRoot; # if this is the parser root

  # from Resource: .id, .meta, .implicitRules, and .language
  # from DomainResource: .text, .contained, .extension, and .modifierExtension
  fhir:RelatedPerson.identifier [ Identifier ], ... ; # 0..* A human identifier for this person
  fhir:RelatedPerson.active [ boolean ]; # 0..1 Whether this related person's record is in active use
  fhir:RelatedPerson.patient [ Reference(Patient) ]; # 1..1 The patient this person is related to
  fhir:RelatedPerson.relationship [ CodeableConcept ], ... ; # 0..* The nature of the relationship
  fhir:RelatedPerson.name [ HumanName ], ... ; # 0..* A name associated with the person
  fhir:RelatedPerson.telecom [ ContactPoint ], ... ; # 0..* A contact detail for the person
  fhir:RelatedPerson.gender [ code ]; # 0..1 male | female | other | unknown
  fhir:RelatedPerson.birthDate [ date ]; # 0..1 The date on which the related person was born
  fhir:RelatedPerson.address [ Address ], ... ; # 0..* Address where the related person can be contacted or visited
  fhir:RelatedPerson.photo [ Attachment ], ... ; # 0..* Image of the person
  fhir:RelatedPerson.period [ Period ]; # 0..1 Period of time that this relationship is considered valid
  fhir:RelatedPerson.communication [ # 0..* A language which may be used to communicate with about the patient's health
    fhir:RelatedPerson.communication.language [ CodeableConcept ]; # 1..1 The language which can be used to communicate with the patient about his or her health
    fhir:RelatedPerson.communication.preferred [ boolean ]; # 0..1 Language preference indicator
  ], ...;
]
```

**Changes since Release 3**

|  |  |
| --- | --- |
| [RelatedPerson](relatedperson.html#RelatedPerson) |  |
| RelatedPerson.active | - Default Value "true" removed |
| RelatedPerson.relationship | - Max Cardinality changed from 1 to \* |
| RelatedPerson.gender | - Change value set from http://hl7.org/fhir/ValueSet/administrative-gender to http://hl7.org/fhir/ValueSet/administrative-gender|4.0.1 |
| RelatedPerson.communication | - Added Element |
| RelatedPerson.communication.language | - **Added Mandatory Element** |
| RelatedPerson.communication.preferred | - Added Element |

See the [Full Difference](diff.html) for further information

This analysis is available as [XML](relatedperson.diff.xml) or [JSON](relatedperson.diff.json).

See [R3 <--> R4 Conversion Maps](relatedperson-version-maps.html) (status = 4 tests that all execute ok. All tests pass round-trip testing and all r3 resources are valid.)

See the [Profiles & Extensions](relatedperson-profiles.html) and the alternate definitions:
Master Definition [XML](relatedperson.profile.xml.html) + [JSON](relatedperson.profile.json.html),
[XML](xml.html) [Schema](relatedperson.xsd)/[Schematron](relatedperson.sch) + [JSON](json.html)
[Schema](relatedperson.schema.json.html), [ShEx](relatedperson.shex.html) (for [Turtle](rdf.html)) + [see the extensions](relatedperson-profiles.html) & the [dependency analysis](relatedperson-dependencies.html)

### 8.2.3.1 Terminology Bindings

| Path | Definition | Type | Reference |
| --- | --- | --- | --- |
| RelatedPerson.relationship | The nature of the relationship between a patient and the related person. | [Preferred](terminologies.html#preferred) | [PatientRelationshipType](valueset-relatedperson-relationshiptype.html) |
| RelatedPerson.gender | The gender of a person used for administrative purposes. | [Required](terminologies.html#required) | [AdministrativeGender](valueset-administrative-gender.html) |
| RelatedPerson.communication.language | A human language. | [Preferred](terminologies.html#preferred), but limited to [AllLanguages](valueset-all-languages.html) | [CommonLanguages](valueset-languages.html) |

## 8.2.4 Search Parameters

Search parameters for this resource. The [common parameters](search.html#all) also apply. See [Searching](search.html) for more information about searching in REST, messaging, and services.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Name** | **Type** | **Description** | **Expression** | **In Common** |
| active | [token](search.html#token) | Indicates if the related person record is active | RelatedPerson.active |  |
| address | [string](search.html#string) | A server defined search that may match any of the string fields in the Address, including line, city, district, state, country, postalCode, and/or text | RelatedPerson.address | [3 Resources](searchparameter-registry.html#individual-address) |
| address-city | [string](search.html#string) | A city specified in an address | RelatedPerson.address.city | [3 Resources](searchparameter-registry.html#individual-address-city) |
| address-country | [string](search.html#string) | A country specified in an address | RelatedPerson.address.country | [3 Resources](searchparameter-registry.html#individual-address-country) |
| address-postalcode | [string](search.html#string) | A postal code specified in an address | RelatedPerson.address.postalCode | [3 Resources](searchparameter-registry.html#individual-address-postalcode) |
| address-state | [string](search.html#string) | A state specified in an address | RelatedPerson.address.state | [3 Resources](searchparameter-registry.html#individual-address-state) |
| address-use | [token](search.html#token) | A use code specified in an address | RelatedPerson.address.use | [3 Resources](searchparameter-registry.html#individual-address-use) |
| birthdate | [date](search.html#date) | The Related Person's date of birth | RelatedPerson.birthDate | [2 Resources](searchparameter-registry.html#individual-birthdate) |
| email | [token](search.html#token) | A value in an email contact | RelatedPerson.telecom.where(system='email') | [4 Resources](searchparameter-registry.html#individual-email) |
| gender | [token](search.html#token) | Gender of the related person | RelatedPerson.gender | [3 Resources](searchparameter-registry.html#individual-gender) |
| identifier | [token](search.html#token) | An Identifier of the RelatedPerson | RelatedPerson.identifier |  |
| name | [string](search.html#string) | A server defined search that may match any of the string fields in the HumanName, including family, give, prefix, suffix, suffix, and/or text | RelatedPerson.name |  |
| patient | [reference](search.html#reference) | The patient this related person is related to | RelatedPerson.patient ([Patient](patient.html)) |  |
| phone | [token](search.html#token) | A value in a phone contact | RelatedPerson.telecom.where(system='phone') | [4 Resources](searchparameter-registry.html#individual-phone) |
| phonetic | [string](search.html#string) | A portion of name using some kind of phonetic matching algorithm | RelatedPerson.name | [3 Resources](searchparameter-registry.html#individual-phonetic) |
| relationship | [token](search.html#token) | The relationship between the patient and the relatedperson | RelatedPerson.relationship |  |
| telecom | [token](search.html#token) | The value in any kind of contact | RelatedPerson.telecom | [4 Resources](searchparameter-registry.html#individual-telecom) |

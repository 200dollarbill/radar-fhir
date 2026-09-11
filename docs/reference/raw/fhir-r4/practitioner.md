---
id: practitioner
title: Practitioner
source_url: https://hl7.org/fhir/R4/practitioner.html
group: fhir-r4
fhir_version: R4
fetched_at: '2026-09-11T13:22:32Z'
sha256: 00dbcd88f7ccf9c483d5b318e78386bdbb14cf8d017dc8bde99e070a1d0d2504
---
This page is part of the FHIR Specification (v4.0.1: R4 - Mixed [Normative](https://confluence.hl7.org/display/HL7/HL7+Balloting "Normative Standard") and [STU](https://confluence.hl7.org/display/HL7/HL7+Balloting "Standard for Trial-Use")) in it's permanent home (it will always be available at this URL). The current version which supercedes this version is [5.0.0](http://hl7.org/fhir/index.html). For a full list of available versions, see the [Directory of published versions ![](external.png)](http://hl7.org/fhir/directory.html). Page versions: [R5](http://hl7.org/fhir/R5/practitioner.html) [R4B](http://hl7.org/fhir/R4B/practitioner.html) **R4** [R3](http://hl7.org/fhir/STU3/practitioner.html) [R2](http://hl7.org/fhir/DSTU2/practitioner.html)

- [Content](#)
- [Examples](practitioner-examples.html)
- [Detailed Descriptions](practitioner-definitions.html)
- [Mappings](practitioner-mappings.html)
- [Profiles & Extensions](practitioner-profiles.html)
- [R3 Conversions](practitioner-version-maps.html)

# 8.4 Resource Practitioner - Content

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [Patient Administration](http://www.hl7.org/Special/committees/pafm/index.cfm)  Work Group | [Maturity Level](versions.html#maturity): 3 | [Trial Use](versions.html#std-process "Standard Status") | [Security Category](security.html#SecPrivConsiderations): Individual | [Compartments](compartmentdefinition.html): [Practitioner](compartmentdefinition-practitioner.html) |

A person who is directly or indirectly involved in the provisioning of healthcare.

## 8.4.1 Scope and Usage

Practitioner covers all individuals who are engaged in the healthcare process and healthcare-related services as part of their formal
responsibilities and this Resource is used for attribution of activities and responsibilities to these individuals.
Practitioners include (but are not limited to):

- physicians, dentists, pharmacists
- physician assistants, nurses, scribes
- midwives, dietitians, therapists, optometrists, paramedics
- medical technicians, laboratory scientists, prosthetic technicians, radiographers
- social workers, professional homecare providers, official volunteers
- receptionists handling patient registration
- IT personnel merging or unmerging patient records
- Service animal (e.g., ward assigned dog capable of detecting cancer in patients)

## 8.4.2 Boundaries and Relationships

The Resource SHALL NOT be used for persons involved without a formal responsibility like individuals taking care for friends,
relatives or neighbors. These can be registered as a Patient's Contact. If performing some action or being referenced by another
resource, use the [RelatedPerson](relatedperson.html) resource.

The primary distinction between a Practitioner and a RelatedPerson is based on whether:

- The person/animal operates on behalf of the care delivery organization over multiple patients (Practitioner) or,
- Where the person/animal is not associated with the organization, and instead is
  allocated tasks specifically for the RelatedPerson's Patient (RelatedPerson).

A standard extension [animalSpecies](extension-practitioner-animalspecies.html) can be used to indicate the species of a service animal.

The [PractitionerRole](practitionerrole.html) resource provides the details of roles that the practitioner
is approved to perform for which organizations (and at which locations, and optionally what services too).

Practitioners are also often grouped into [CareTeams](careteam.html) independently of roles, where the CareTeam
defines what specific role that they are fulfilling within the team, and might or might not have actual practitioner role resources
created for the practitioner (and in the care team context, the organization the practitioner is representing)

## 8.4.3 Background and Context

Practitioner performs different roles within the same or even different organizations. Depending on jurisdiction and custom,
it may be necessary to maintain a specific Practitioner Resource for each such role or have a single Practitioner with multiple roles.
The role can be limited to a specific period, after which authorization for this role ends. Note that the represented organization
need not necessarily be the (direct) employer of a Practitioner.

This resource is referenced by [Annotation](datatypes.html#Annotation), [Signature](datatypes.html#Signature), [Account](account.html#Account), [AdverseEvent](adverseevent.html#AdverseEvent), [AllergyIntolerance](allergyintolerance.html#AllergyIntolerance), [Appointment](appointment.html#Appointment), [AppointmentResponse](appointmentresponse.html#AppointmentResponse), [AuditEvent](auditevent.html#AuditEvent), [Basic](basic.html#Basic), [BiologicallyDerivedProduct](biologicallyderivedproduct.html#BiologicallyDerivedProduct), [CarePlan](careplan.html#CarePlan), [CareTeam](careteam.html#CareTeam), [CatalogEntry](catalogentry.html#CatalogEntry), [ChargeItem](chargeitem.html#ChargeItem), [Claim](claim.html#Claim), [ClaimResponse](claimresponse.html#ClaimResponse), [ClinicalImpression](clinicalimpression.html#ClinicalImpression), [Communication](communication.html#Communication), [CommunicationRequest](communicationrequest.html#CommunicationRequest), [Composition](composition.html#Composition), [Condition](condition.html#Condition), [Consent](consent.html#Consent), [Contract](contract.html#Contract), [CoverageEligibilityRequest](coverageeligibilityrequest.html#CoverageEligibilityRequest), [CoverageEligibilityResponse](coverageeligibilityresponse.html#CoverageEligibilityResponse), [DetectedIssue](detectedissue.html#DetectedIssue), [DeviceRequest](devicerequest.html#DeviceRequest), [DeviceUseStatement](deviceusestatement.html#DeviceUseStatement), [DiagnosticReport](diagnosticreport.html#DiagnosticReport), [DocumentManifest](documentmanifest.html#DocumentManifest), [DocumentReference](documentreference.html#DocumentReference), [Encounter](encounter.html#Encounter), [EnrollmentRequest](enrollmentrequest.html#EnrollmentRequest), [EnrollmentResponse](enrollmentresponse.html#EnrollmentResponse), [EpisodeOfCare](episodeofcare.html#EpisodeOfCare), [ExplanationOfBenefit](explanationofbenefit.html#ExplanationOfBenefit), [Flag](flag.html#Flag), [Goal](goal.html#Goal), [Group](group.html#Group), [ImagingStudy](imagingstudy.html#ImagingStudy), [Immunization](immunization.html#Immunization), [Invoice](invoice.html#Invoice), [Linkage](linkage.html#Linkage), [List](list.html#List), [MeasureReport](measurereport.html#MeasureReport), [Media](media.html#Media), [MedicationAdministration](medicationadministration.html#MedicationAdministration), [MedicationDispense](medicationdispense.html#MedicationDispense), [MedicationRequest](medicationrequest.html#MedicationRequest), [MedicationStatement](medicationstatement.html#MedicationStatement), [MessageHeader](messageheader.html#MessageHeader), [NutritionOrder](nutritionorder.html#NutritionOrder), [Observation](observation.html#Observation), [Patient](patient.html#Patient), [PaymentNotice](paymentnotice.html#PaymentNotice), [PaymentReconciliation](paymentreconciliation.html#PaymentReconciliation), [Person](person.html#Person), [PractitionerRole](practitionerrole.html#PractitionerRole), [Procedure](procedure.html#Procedure), [Provenance](provenance.html#Provenance), [QuestionnaireResponse](questionnaireresponse.html#QuestionnaireResponse), [RequestGroup](requestgroup.html#RequestGroup), [ResearchStudy](researchstudy.html#ResearchStudy), [RiskAssessment](riskassessment.html#RiskAssessment), [Schedule](schedule.html#Schedule), [ServiceRequest](servicerequest.html#ServiceRequest), [Specimen](specimen.html#Specimen), [SupplyDelivery](supplydelivery.html#SupplyDelivery), [SupplyRequest](supplyrequest.html#SupplyRequest), [Task](task.html#Task), [VerificationResult](verificationresult.html#VerificationResult) and [VisionPrescription](visionprescription.html#VisionPrescription)

## 8.4.4 Resource Content

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
| .. [Practitioner](practitioner-definitions.html#Practitioner "Practitioner : A person who is directly or indirectly involved in the provisioning of healthcare.") | [TU](versions.html#std-process "Standards Status = Trial Use") |  | [DomainResource](domainresource.html) | A person with a formal responsibility in the provisioning of healthcare or related services Elements defined in Ancestors: [id](resource.html#Resource "The logical id of the resource, as used in the URL for the resource. Once assigned, this value never changes."), [meta](resource.html#Resource "The metadata about the resource. This is content that is maintained by the infrastructure. Changes to the content might not always be associated with version changes to the resource."), [implicitRules](resource.html#Resource "A reference to a set of rules that were followed when the resource was constructed, and which must be understood when processing the content. Often, this is a reference to an implementation guide that defines the special rules along with other profiles etc."), [language](resource.html#Resource "The base language in which the resource is written."), [text](domainresource.html#DomainResource "A human-readable narrative that contains a summary of the resource and can be used to represent the content of the resource to a human. The narrative need not encode all the structured data, but is required to contain sufficient detail to make it \"clinically safe\" for a human to just read the narrative. Resource definitions may define what content should be represented in the narrative to ensure clinical safety."), [contained](domainresource.html#DomainResource "These resources do not have an independent existence apart from the resource that contains them - they cannot be identified independently, and nor can they have their own independent transaction scope."), [extension](domainresource.html#DomainResource "May be used to represent additional information that is not part of the basic definition of the resource. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension."), [modifierExtension](domainresource.html#DomainResource "May be used to represent additional information that is not part of the basic definition of the resource and that modifies the understanding of the element that contains it and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer is allowed to define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.  Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).") |
| ... [identifier](practitioner-definitions.html#Practitioner.identifier "Practitioner.identifier : An identifier that applies to this person in this role.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [Identifier](datatypes.html#Identifier) | An identifier for the person as this agent |
| ... [active](practitioner-definitions.html#Practitioner.active "Practitioner.active : Whether this practitioner's record is in active use.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [boolean](datatypes.html#boolean) | Whether this practitioner's record is in active use |
| ... [name](practitioner-definitions.html#Practitioner.name "Practitioner.name : The name(s) associated with the practitioner.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [HumanName](datatypes.html#HumanName) | The name(s) associated with the practitioner |
| ... [telecom](practitioner-definitions.html#Practitioner.telecom "Practitioner.telecom : A contact detail for the practitioner, e.g. a telephone number or an email address.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [ContactPoint](datatypes.html#ContactPoint) | A contact detail for the practitioner (that apply to all roles) |
| ... [address](practitioner-definitions.html#Practitioner.address "Practitioner.address : Address(es) of the practitioner that are not role specific (typically home address).  Work addresses are not typically entered in this property as they are usually role dependent.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [Address](datatypes.html#Address) | Address(es) of the practitioner that are not role specific (typically home address) |
| ... [gender](practitioner-definitions.html#Practitioner.gender "Practitioner.gender : Administrative Gender - the gender that the person is considered to have for administration and record keeping purposes.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [code](datatypes.html#code) | male | female | other | unknown [AdministrativeGender](valueset-administrative-gender.html "The gender of a person used for administrative purposes.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ... [birthDate](practitioner-definitions.html#Practitioner.birthDate "Practitioner.birthDate : The date of birth for the practitioner.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [date](datatypes.html#date) | The date on which the practitioner was born |
| ... [photo](practitioner-definitions.html#Practitioner.photo "Practitioner.photo : Image of the person.") |  | 0..\* | [Attachment](datatypes.html#Attachment) | Image of the person |
| ... [qualification](practitioner-definitions.html#Practitioner.qualification "Practitioner.qualification : The official certifications, training, and licenses that authorize or otherwise pertain to the provision of care by the practitioner.  For example, a medical license issued by a medical board authorizing the practitioner to practice medicine within a certian locality.") |  | 0..\* | [BackboneElement](backboneelement.html) | Certification, licenses, or training pertaining to the provision of care |
| .... [identifier](practitioner-definitions.html#Practitioner.qualification.identifier "Practitioner.qualification.identifier : An identifier that applies to this person's qualification in this role.") |  | 0..\* | [Identifier](datatypes.html#Identifier) | An identifier for this qualification for the practitioner |
| .... [code](practitioner-definitions.html#Practitioner.qualification.code "Practitioner.qualification.code : Coded representation of the qualification.") |  | 1..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Coded representation of the qualification [v2 table 0360, Version 2.7](v2/0360/2.7/index.html "Specific qualification the practitioner has to provide a service.") ([Example](terminologies.html#example "Instances are not expected or even encouraged to draw from the specified value set.  The value set merely provides examples of the types of concepts intended to be included.")) |
| .... [period](practitioner-definitions.html#Practitioner.qualification.period "Practitioner.qualification.period : Period during which the qualification is valid.") |  | 0..1 | [Period](datatypes.html#Period) | Period during which the qualification is valid |
| .... [issuer](practitioner-definitions.html#Practitioner.qualification.issuer "Practitioner.qualification.issuer : Organization that regulates and issues the qualification.") |  | 0..1 | [Reference](references.html#Reference)([Organization](organization.html)) | Organization that regulates and issues the qualification |
| ... [communication](practitioner-definitions.html#Practitioner.communication "Practitioner.communication : A language the practitioner can use in patient communication.") |  | 0..\* | [CodeableConcept](datatypes.html#CodeableConcept) | A language the practitioner can use in patient communication [Common Languages](valueset-languages.html "A human language.") ([Preferred](terminologies.html#preferred "Instances are encouraged to draw from the specified codes for interoperability purposes but are not required to do so to be considered conformant.") but limited to [AllLanguages](valueset-all-languages.html)) |
| [doco Documentation for this format](formats.html#table "Legend for this format") | | | | |

**UML Diagram** ([Legend](formats.html#uml))

**XML Template**

```

<Practitioner xmlns="http://hl7.org/fhir"> ![doco](help.png)
 <!-- from Resource: id, meta, implicitRules, and language -->
 <!-- from DomainResource: text, contained, extension, and modifierExtension -->
 <identifier><!-- 0..* Identifier An identifier for the person as this agent --></identifier>
 <active value="[boolean]"/><!-- 0..1 Whether this practitioner's record is in active use -->
 <name><!-- 0..* HumanName The name(s) associated with the practitioner --></name>
 <telecom><!-- 0..* ContactPoint A contact detail for the practitioner (that apply to all roles) --></telecom>
 <address><!-- 0..* Address Address(es) of the practitioner that are not role specific (typically home address) --></address>
 <gender value="[code]"/><!-- 0..1 male | female | other | unknown -->
 <birthDate value="[date]"/><!-- 0..1 The date  on which the practitioner was born -->
 <photo><!-- 0..* Attachment Image of the person --></photo>
 <qualification>  <!-- 0..* Certification, licenses, or training pertaining to the provision of care -->
  <identifier><!-- 0..* Identifier An identifier for this qualification for the practitioner --></identifier>
  <code><!-- 1..1 CodeableConcept Coded representation of the qualification --></code>
  <period><!-- 0..1 Period Period during which the qualification is valid --></period>
  <issuer><!-- 0..1 Reference(Organization) Organization that regulates and issues the qualification --></issuer>
 </qualification>
 <communication><!-- 0..* CodeableConcept A language the practitioner can use in patient communication --></communication>
</Practitioner>
```

**JSON Template**

```

{![doco](help.png)
  "resourceType" : "Practitioner",
  // from Resource: id, meta, implicitRules, and language
  // from DomainResource: text, contained, extension, and modifierExtension
  "identifier" : [{ Identifier }], // An identifier for the person as this agent
  "active" : <boolean>, // Whether this practitioner's record is in active use
  "name" : [{ HumanName }], // The name(s) associated with the practitioner
  "telecom" : [{ ContactPoint }], // A contact detail for the practitioner (that apply to all roles)
  "address" : [{ Address }], // Address(es) of the practitioner that are not role specific (typically home address)
  "gender" : "<code>", // male | female | other | unknown
  "birthDate" : "<date>", // The date  on which the practitioner was born
  "photo" : [{ Attachment }], // Image of the person
  "qualification" : [{ // Certification, licenses, or training pertaining to the provision of care
    "identifier" : [{ Identifier }], // An identifier for this qualification for the practitioner
    "code" : { CodeableConcept }, // R!  Coded representation of the qualification
    "period" : { Period }, // Period during which the qualification is valid
    "issuer" : { Reference(Organization) } // Organization that regulates and issues the qualification
  }],
  "communication" : [{ CodeableConcept }] // A language the practitioner can use in patient communication
}
```

**Turtle Template**

```

@prefix fhir: <http://hl7.org/fhir/> .![doco](help.png)


[ a fhir:Practitioner;
  fhir:nodeRole fhir:treeRoot; # if this is the parser root

  # from Resource: .id, .meta, .implicitRules, and .language
  # from DomainResource: .text, .contained, .extension, and .modifierExtension
  fhir:Practitioner.identifier [ Identifier ], ... ; # 0..* An identifier for the person as this agent
  fhir:Practitioner.active [ boolean ]; # 0..1 Whether this practitioner's record is in active use
  fhir:Practitioner.name [ HumanName ], ... ; # 0..* The name(s) associated with the practitioner
  fhir:Practitioner.telecom [ ContactPoint ], ... ; # 0..* A contact detail for the practitioner (that apply to all roles)
  fhir:Practitioner.address [ Address ], ... ; # 0..* Address(es) of the practitioner that are not role specific (typically home address)
  fhir:Practitioner.gender [ code ]; # 0..1 male | female | other | unknown
  fhir:Practitioner.birthDate [ date ]; # 0..1 The date  on which the practitioner was born
  fhir:Practitioner.photo [ Attachment ], ... ; # 0..* Image of the person
  fhir:Practitioner.qualification [ # 0..* Certification, licenses, or training pertaining to the provision of care
    fhir:Practitioner.qualification.identifier [ Identifier ], ... ; # 0..* An identifier for this qualification for the practitioner
    fhir:Practitioner.qualification.code [ CodeableConcept ]; # 1..1 Coded representation of the qualification
    fhir:Practitioner.qualification.period [ Period ]; # 0..1 Period during which the qualification is valid
    fhir:Practitioner.qualification.issuer [ Reference(Organization) ]; # 0..1 Organization that regulates and issues the qualification
  ], ...;
  fhir:Practitioner.communication [ CodeableConcept ], ... ; # 0..* A language the practitioner can use in patient communication
]
```

**Changes since R3**

|  |  |
| --- | --- |
| [Practitioner](practitioner.html#Practitioner) |  |
| Practitioner.active | - Default Value "true" removed |
| Practitioner.gender | - Change value set from http://hl7.org/fhir/ValueSet/administrative-gender to http://hl7.org/fhir/ValueSet/administrative-gender|4.0.1 |
| Practitioner.communication | - Change binding strength from extensible to preferred |

See the [Full Difference](diff.html) for further information

This analysis is available as [XML](practitioner.diff.xml) or [JSON](practitioner.diff.json).

See [R3 <--> R4 Conversion Maps](practitioner-version-maps.html) (status = 14 tests that all execute ok. All tests pass round-trip testing and all r3 resources are valid.)

**Structure**

| [Name](formats.html#table "The logical name of the element") | [Flags](formats.html#table "Information about the use of the element") | [Card.](formats.html#table "Minimum and Maximum # of times the the element can appear in the instance") | [Type](formats.html#table "Reference to the type of the element") | [Description & Constraints](formats.html#table "Additional information about the element")[doco](formats.html#table "Legend for this format") |
| --- | --- | --- | --- | --- |
| .. [Practitioner](practitioner-definitions.html#Practitioner "Practitioner : A person who is directly or indirectly involved in the provisioning of healthcare.") | [TU](versions.html#std-process "Standards Status = Trial Use") |  | [DomainResource](domainresource.html) | A person with a formal responsibility in the provisioning of healthcare or related services Elements defined in Ancestors: [id](resource.html#Resource "The logical id of the resource, as used in the URL for the resource. Once assigned, this value never changes."), [meta](resource.html#Resource "The metadata about the resource. This is content that is maintained by the infrastructure. Changes to the content might not always be associated with version changes to the resource."), [implicitRules](resource.html#Resource "A reference to a set of rules that were followed when the resource was constructed, and which must be understood when processing the content. Often, this is a reference to an implementation guide that defines the special rules along with other profiles etc."), [language](resource.html#Resource "The base language in which the resource is written."), [text](domainresource.html#DomainResource "A human-readable narrative that contains a summary of the resource and can be used to represent the content of the resource to a human. The narrative need not encode all the structured data, but is required to contain sufficient detail to make it \"clinically safe\" for a human to just read the narrative. Resource definitions may define what content should be represented in the narrative to ensure clinical safety."), [contained](domainresource.html#DomainResource "These resources do not have an independent existence apart from the resource that contains them - they cannot be identified independently, and nor can they have their own independent transaction scope."), [extension](domainresource.html#DomainResource "May be used to represent additional information that is not part of the basic definition of the resource. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension."), [modifierExtension](domainresource.html#DomainResource "May be used to represent additional information that is not part of the basic definition of the resource and that modifies the understanding of the element that contains it and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer is allowed to define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.  Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).") |
| ... [identifier](practitioner-definitions.html#Practitioner.identifier "Practitioner.identifier : An identifier that applies to this person in this role.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [Identifier](datatypes.html#Identifier) | An identifier for the person as this agent |
| ... [active](practitioner-definitions.html#Practitioner.active "Practitioner.active : Whether this practitioner's record is in active use.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [boolean](datatypes.html#boolean) | Whether this practitioner's record is in active use |
| ... [name](practitioner-definitions.html#Practitioner.name "Practitioner.name : The name(s) associated with the practitioner.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [HumanName](datatypes.html#HumanName) | The name(s) associated with the practitioner |
| ... [telecom](practitioner-definitions.html#Practitioner.telecom "Practitioner.telecom : A contact detail for the practitioner, e.g. a telephone number or an email address.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [ContactPoint](datatypes.html#ContactPoint) | A contact detail for the practitioner (that apply to all roles) |
| ... [address](practitioner-definitions.html#Practitioner.address "Practitioner.address : Address(es) of the practitioner that are not role specific (typically home address).  Work addresses are not typically entered in this property as they are usually role dependent.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [Address](datatypes.html#Address) | Address(es) of the practitioner that are not role specific (typically home address) |
| ... [gender](practitioner-definitions.html#Practitioner.gender "Practitioner.gender : Administrative Gender - the gender that the person is considered to have for administration and record keeping purposes.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [code](datatypes.html#code) | male | female | other | unknown [AdministrativeGender](valueset-administrative-gender.html "The gender of a person used for administrative purposes.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ... [birthDate](practitioner-definitions.html#Practitioner.birthDate "Practitioner.birthDate : The date of birth for the practitioner.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [date](datatypes.html#date) | The date on which the practitioner was born |
| ... [photo](practitioner-definitions.html#Practitioner.photo "Practitioner.photo : Image of the person.") |  | 0..\* | [Attachment](datatypes.html#Attachment) | Image of the person |
| ... [qualification](practitioner-definitions.html#Practitioner.qualification "Practitioner.qualification : The official certifications, training, and licenses that authorize or otherwise pertain to the provision of care by the practitioner.  For example, a medical license issued by a medical board authorizing the practitioner to practice medicine within a certian locality.") |  | 0..\* | [BackboneElement](backboneelement.html) | Certification, licenses, or training pertaining to the provision of care |
| .... [identifier](practitioner-definitions.html#Practitioner.qualification.identifier "Practitioner.qualification.identifier : An identifier that applies to this person's qualification in this role.") |  | 0..\* | [Identifier](datatypes.html#Identifier) | An identifier for this qualification for the practitioner |
| .... [code](practitioner-definitions.html#Practitioner.qualification.code "Practitioner.qualification.code : Coded representation of the qualification.") |  | 1..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Coded representation of the qualification [v2 table 0360, Version 2.7](v2/0360/2.7/index.html "Specific qualification the practitioner has to provide a service.") ([Example](terminologies.html#example "Instances are not expected or even encouraged to draw from the specified value set.  The value set merely provides examples of the types of concepts intended to be included.")) |
| .... [period](practitioner-definitions.html#Practitioner.qualification.period "Practitioner.qualification.period : Period during which the qualification is valid.") |  | 0..1 | [Period](datatypes.html#Period) | Period during which the qualification is valid |
| .... [issuer](practitioner-definitions.html#Practitioner.qualification.issuer "Practitioner.qualification.issuer : Organization that regulates and issues the qualification.") |  | 0..1 | [Reference](references.html#Reference)([Organization](organization.html)) | Organization that regulates and issues the qualification |
| ... [communication](practitioner-definitions.html#Practitioner.communication "Practitioner.communication : A language the practitioner can use in patient communication.") |  | 0..\* | [CodeableConcept](datatypes.html#CodeableConcept) | A language the practitioner can use in patient communication [Common Languages](valueset-languages.html "A human language.") ([Preferred](terminologies.html#preferred "Instances are encouraged to draw from the specified codes for interoperability purposes but are not required to do so to be considered conformant.") but limited to [AllLanguages](valueset-all-languages.html)) |
| [doco Documentation for this format](formats.html#table "Legend for this format") | | | | |

**UML Diagram** ([Legend](formats.html#uml))

**XML Template**

```

<Practitioner xmlns="http://hl7.org/fhir"> ![doco](help.png)
 <!-- from Resource: id, meta, implicitRules, and language -->
 <!-- from DomainResource: text, contained, extension, and modifierExtension -->
 <identifier><!-- 0..* Identifier An identifier for the person as this agent --></identifier>
 <active value="[boolean]"/><!-- 0..1 Whether this practitioner's record is in active use -->
 <name><!-- 0..* HumanName The name(s) associated with the practitioner --></name>
 <telecom><!-- 0..* ContactPoint A contact detail for the practitioner (that apply to all roles) --></telecom>
 <address><!-- 0..* Address Address(es) of the practitioner that are not role specific (typically home address) --></address>
 <gender value="[code]"/><!-- 0..1 male | female | other | unknown -->
 <birthDate value="[date]"/><!-- 0..1 The date  on which the practitioner was born -->
 <photo><!-- 0..* Attachment Image of the person --></photo>
 <qualification>  <!-- 0..* Certification, licenses, or training pertaining to the provision of care -->
  <identifier><!-- 0..* Identifier An identifier for this qualification for the practitioner --></identifier>
  <code><!-- 1..1 CodeableConcept Coded representation of the qualification --></code>
  <period><!-- 0..1 Period Period during which the qualification is valid --></period>
  <issuer><!-- 0..1 Reference(Organization) Organization that regulates and issues the qualification --></issuer>
 </qualification>
 <communication><!-- 0..* CodeableConcept A language the practitioner can use in patient communication --></communication>
</Practitioner>
```

**JSON Template**

```

{![doco](help.png)
  "resourceType" : "Practitioner",
  // from Resource: id, meta, implicitRules, and language
  // from DomainResource: text, contained, extension, and modifierExtension
  "identifier" : [{ Identifier }], // An identifier for the person as this agent
  "active" : <boolean>, // Whether this practitioner's record is in active use
  "name" : [{ HumanName }], // The name(s) associated with the practitioner
  "telecom" : [{ ContactPoint }], // A contact detail for the practitioner (that apply to all roles)
  "address" : [{ Address }], // Address(es) of the practitioner that are not role specific (typically home address)
  "gender" : "<code>", // male | female | other | unknown
  "birthDate" : "<date>", // The date  on which the practitioner was born
  "photo" : [{ Attachment }], // Image of the person
  "qualification" : [{ // Certification, licenses, or training pertaining to the provision of care
    "identifier" : [{ Identifier }], // An identifier for this qualification for the practitioner
    "code" : { CodeableConcept }, // R!  Coded representation of the qualification
    "period" : { Period }, // Period during which the qualification is valid
    "issuer" : { Reference(Organization) } // Organization that regulates and issues the qualification
  }],
  "communication" : [{ CodeableConcept }] // A language the practitioner can use in patient communication
}
```

**Turtle Template**

```

@prefix fhir: <http://hl7.org/fhir/> .![doco](help.png)


[ a fhir:Practitioner;
  fhir:nodeRole fhir:treeRoot; # if this is the parser root

  # from Resource: .id, .meta, .implicitRules, and .language
  # from DomainResource: .text, .contained, .extension, and .modifierExtension
  fhir:Practitioner.identifier [ Identifier ], ... ; # 0..* An identifier for the person as this agent
  fhir:Practitioner.active [ boolean ]; # 0..1 Whether this practitioner's record is in active use
  fhir:Practitioner.name [ HumanName ], ... ; # 0..* The name(s) associated with the practitioner
  fhir:Practitioner.telecom [ ContactPoint ], ... ; # 0..* A contact detail for the practitioner (that apply to all roles)
  fhir:Practitioner.address [ Address ], ... ; # 0..* Address(es) of the practitioner that are not role specific (typically home address)
  fhir:Practitioner.gender [ code ]; # 0..1 male | female | other | unknown
  fhir:Practitioner.birthDate [ date ]; # 0..1 The date  on which the practitioner was born
  fhir:Practitioner.photo [ Attachment ], ... ; # 0..* Image of the person
  fhir:Practitioner.qualification [ # 0..* Certification, licenses, or training pertaining to the provision of care
    fhir:Practitioner.qualification.identifier [ Identifier ], ... ; # 0..* An identifier for this qualification for the practitioner
    fhir:Practitioner.qualification.code [ CodeableConcept ]; # 1..1 Coded representation of the qualification
    fhir:Practitioner.qualification.period [ Period ]; # 0..1 Period during which the qualification is valid
    fhir:Practitioner.qualification.issuer [ Reference(Organization) ]; # 0..1 Organization that regulates and issues the qualification
  ], ...;
  fhir:Practitioner.communication [ CodeableConcept ], ... ; # 0..* A language the practitioner can use in patient communication
]
```

**Changes since Release 3**

|  |  |
| --- | --- |
| [Practitioner](practitioner.html#Practitioner) |  |
| Practitioner.active | - Default Value "true" removed |
| Practitioner.gender | - Change value set from http://hl7.org/fhir/ValueSet/administrative-gender to http://hl7.org/fhir/ValueSet/administrative-gender|4.0.1 |
| Practitioner.communication | - Change binding strength from extensible to preferred |

See the [Full Difference](diff.html) for further information

This analysis is available as [XML](practitioner.diff.xml) or [JSON](practitioner.diff.json).

See [R3 <--> R4 Conversion Maps](practitioner-version-maps.html) (status = 14 tests that all execute ok. All tests pass round-trip testing and all r3 resources are valid.)

See the [Profiles & Extensions](practitioner-profiles.html) and the alternate definitions:
Master Definition [XML](practitioner.profile.xml.html) + [JSON](practitioner.profile.json.html),
[XML](xml.html) [Schema](practitioner.xsd)/[Schematron](practitioner.sch) + [JSON](json.html)
[Schema](practitioner.schema.json.html), [ShEx](practitioner.shex.html) (for [Turtle](rdf.html)) + [see the extensions](practitioner-profiles.html) & the [dependency analysis](practitioner-dependencies.html)

### 8.4.4.1 Terminology Bindings

| Path | Definition | Type | Reference |
| --- | --- | --- | --- |
| Practitioner.gender | The gender of a person used for administrative purposes. | [Required](terminologies.html#required) | [AdministrativeGender](valueset-administrative-gender.html) |
| Practitioner.qualification.code | Specific qualification the practitioner has to provide a service. | [Example](terminologies.html#example) | [v2.0360.2.7](v2/0360/2.7/index.html) |
| Practitioner.communication | A human language. | [Preferred](terminologies.html#preferred), but limited to [AllLanguages](valueset-all-languages.html) | [CommonLanguages](valueset-languages.html) |

## 8.4.5 Notes:

- The practitioner's Qualifications are acquired by the practitioner independent of any organization or role,
  and do not imply that they are allowed/authorized to perform roles relevant to the qualification at any specific Organization/Location.

## 8.4.6 Search Parameters

Search parameters for this resource. The [common parameters](search.html#all) also apply. See [Searching](search.html) for more information about searching in REST, messaging, and services.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Name** | **Type** | **Description** | **Expression** | **In Common** |
| active | [token](search.html#token) | Whether the practitioner record is active | Practitioner.active |  |
| address | [string](search.html#string) | A server defined search that may match any of the string fields in the Address, including line, city, district, state, country, postalCode, and/or text | Practitioner.address | [3 Resources](searchparameter-registry.html#individual-address) |
| address-city | [string](search.html#string) | A city specified in an address | Practitioner.address.city | [3 Resources](searchparameter-registry.html#individual-address-city) |
| address-country | [string](search.html#string) | A country specified in an address | Practitioner.address.country | [3 Resources](searchparameter-registry.html#individual-address-country) |
| address-postalcode | [string](search.html#string) | A postalCode specified in an address | Practitioner.address.postalCode | [3 Resources](searchparameter-registry.html#individual-address-postalcode) |
| address-state | [string](search.html#string) | A state specified in an address | Practitioner.address.state | [3 Resources](searchparameter-registry.html#individual-address-state) |
| address-use | [token](search.html#token) | A use code specified in an address | Practitioner.address.use | [3 Resources](searchparameter-registry.html#individual-address-use) |
| communication | [token](search.html#token) | One of the languages that the practitioner can communicate with | Practitioner.communication |  |
| email | [token](search.html#token) | A value in an email contact | Practitioner.telecom.where(system='email') | [4 Resources](searchparameter-registry.html#individual-email) |
| family | [string](search.html#string) | A portion of the family name | Practitioner.name.family | [1 Resources](searchparameter-registry.html#individual-family) |
| gender | [token](search.html#token) | Gender of the practitioner | Practitioner.gender | [3 Resources](searchparameter-registry.html#individual-gender) |
| given | [string](search.html#string) | A portion of the given name | Practitioner.name.given | [1 Resources](searchparameter-registry.html#individual-given) |
| identifier | [token](search.html#token) | A practitioner's Identifier | Practitioner.identifier |  |
| name | [string](search.html#string) | A server defined search that may match any of the string fields in the HumanName, including family, give, prefix, suffix, suffix, and/or text | Practitioner.name |  |
| phone | [token](search.html#token) | A value in a phone contact | Practitioner.telecom.where(system='phone') | [4 Resources](searchparameter-registry.html#individual-phone) |
| phonetic | [string](search.html#string) | A portion of either family or given name using some kind of phonetic matching algorithm | Practitioner.name | [3 Resources](searchparameter-registry.html#individual-phonetic) |
| telecom | [token](search.html#token) | The value in any kind of contact | Practitioner.telecom | [4 Resources](searchparameter-registry.html#individual-telecom) |

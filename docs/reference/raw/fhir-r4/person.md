---
id: person
title: Person
source_url: https://hl7.org/fhir/R4/person.html
group: fhir-r4
fhir_version: R4
fetched_at: '2026-09-11T13:23:08Z'
sha256: 77171581b64af9585560e7772f3f63902114dacbb29bd820c13e206d326ccb32
---
This page is part of the FHIR Specification (v4.0.1: R4 - Mixed [Normative](https://confluence.hl7.org/display/HL7/HL7+Balloting "Normative Standard") and [STU](https://confluence.hl7.org/display/HL7/HL7+Balloting "Standard for Trial-Use")) in it's permanent home (it will always be available at this URL). The current version which supercedes this version is [5.0.0](http://hl7.org/fhir/index.html). For a full list of available versions, see the [Directory of published versions ![](external.png)](http://hl7.org/fhir/directory.html). Page versions: [R5](http://hl7.org/fhir/R5/person.html) [R4B](http://hl7.org/fhir/R4B/person.html) **R4** [R3](http://hl7.org/fhir/STU3/person.html) [R2](http://hl7.org/fhir/DSTU2/person.html)

- [Content](#)
- [Examples](person-examples.html)
- [Detailed Descriptions](person-definitions.html)
- [Mappings](person-mappings.html)
- [Profiles & Extensions](person-profiles.html)
- [R3 Conversions](person-version-maps.html)

# 8.18 Resource Person - Content

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [Patient Administration](http://www.hl7.org/Special/committees/pafm/index.cfm)  Work Group | [Maturity Level](versions.html#maturity): 2 | [Trial Use](versions.html#std-process "Standard Status") | [Security Category](security.html#SecPrivConsiderations): Patient | [Compartments](compartmentdefinition.html): [Patient](compartmentdefinition-patient.html), [Practitioner](compartmentdefinition-practitioner.html), [RelatedPerson](compartmentdefinition-relatedperson.html) |

Demographics and administrative information about a person independent of a specific health-related context.

## 8.18.1 Scope and Usage

The Person resource serves as a linkage resource that may provide a reference set of common demographics
for an individual (human or animal) across multiple roles.  
This linkage can be direct to role-specific FHIR resources (Patient, Practitioner and RelatedPerson)
residing on the same or possibly distinct FHIR systems/applications, or indirectly through the use of
business identifiers.

The Person resource may be used in many situations/contexts, including:

- A set of demographics that can be used to co-ordinate the maintenance of this
  de-normalized information across practitioners, patients and/or related persons  
  *e.g. link known resources of the different types together within a system*
- A state/network based Master Person Index  
  *e.g. A National Identifier Index or a Network membership/subscriber list*
- A central register that links patient resources from multiple servers, indicating they
  all correspond to the same individual  
  *e.g. Within a large organization with many systems to be able to link the various records,
  without having to modify the source information with external links*
- A support for access monitoring software that is able to assert what practitioner,
  patient and related person records correspond to the same human being to assist in
  detecting improper querying.  
  *e.g. asserting that a Patient A is the same individual as a RelatedPerson B who is
  related to Patient C, who is also Practitioner D. As such, monitoring for Practitioner
  D’s accesses to Patient A’s records should be carefully scrutinized.*
- Local record(s) on a mobile device listing links to remote server patient resources  
  *e.g. A mobile phone application storing references to the hospitals they have access to*

> **Note:** The Person resource is an advanced feature. Many systems don’t have a way
> to relate information across resource types, or systems, especially from Patient to
> Practitioner, and therefore might not implement this functionality. Some do have ways
> of relating the Patient and RelatedPerson resource types. FHIR is also able to do this
> without the Person resource, utilizing the Patient.link property
> [(as shown in the Mother and newborn relationship example)](patient.html#maternity)

## 8.18.2 Boundaries and Relationships

Person resources may have references to Patient, RelatedPerson and/or Practitioner resources.
These linkages assert that all the records relate to the same individual.

Person instances are never directly referenced as actors (authors, subjects, performers, etc.)
Individual actors are always identified as either Patient, Practitioner or RelatedPerson, depending on the role
of the individual when undertaking the action. Therefore this resource SHALL NOT be referenced by any
other clinical or administrative resources.
E.g. it can be the focus of an operation or message or included in a Bundle,
but cannot be a member of a List or Group, the subject of an Observation, or other similar non-infrastructural usage.

In some use cases the linkages will be indirect, and through business Identifiers, such as in the case of
the various types of Master Person Indexes, where the records are not there for the purpose of healthcare,
but simply describing a population of people, and has other purposes and not just to represent a population patients.

This resource is referenced by itself

## 8.18.3 Resource Content

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
| .. [Person](person-definitions.html#Person "Person : Demographics and administrative information about a person independent of a specific health-related context.") | [TU](versions.html#std-process "Standards Status = Trial Use") |  | [DomainResource](domainresource.html) | A generic person record Elements defined in Ancestors: [id](resource.html#Resource "The logical id of the resource, as used in the URL for the resource. Once assigned, this value never changes."), [meta](resource.html#Resource "The metadata about the resource. This is content that is maintained by the infrastructure. Changes to the content might not always be associated with version changes to the resource."), [implicitRules](resource.html#Resource "A reference to a set of rules that were followed when the resource was constructed, and which must be understood when processing the content. Often, this is a reference to an implementation guide that defines the special rules along with other profiles etc."), [language](resource.html#Resource "The base language in which the resource is written."), [text](domainresource.html#DomainResource "A human-readable narrative that contains a summary of the resource and can be used to represent the content of the resource to a human. The narrative need not encode all the structured data, but is required to contain sufficient detail to make it \"clinically safe\" for a human to just read the narrative. Resource definitions may define what content should be represented in the narrative to ensure clinical safety."), [contained](domainresource.html#DomainResource "These resources do not have an independent existence apart from the resource that contains them - they cannot be identified independently, and nor can they have their own independent transaction scope."), [extension](domainresource.html#DomainResource "May be used to represent additional information that is not part of the basic definition of the resource. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension."), [modifierExtension](domainresource.html#DomainResource "May be used to represent additional information that is not part of the basic definition of the resource and that modifies the understanding of the element that contains it and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer is allowed to define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.  Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).") |
| ... [identifier](person-definitions.html#Person.identifier "Person.identifier : Identifier for a person within a particular scope.") |  | 0..\* | [Identifier](datatypes.html#Identifier) | A human identifier for this person |
| ... [name](person-definitions.html#Person.name "Person.name : A name associated with the person.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [HumanName](datatypes.html#HumanName) | A name associated with the person |
| ... [telecom](person-definitions.html#Person.telecom "Person.telecom : A contact detail for the person, e.g. a telephone number or an email address.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [ContactPoint](datatypes.html#ContactPoint) | A contact detail for the person |
| ... [gender](person-definitions.html#Person.gender "Person.gender : Administrative Gender.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [code](datatypes.html#code) | male | female | other | unknown [AdministrativeGender](valueset-administrative-gender.html "The gender of a person used for administrative purposes.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ... [birthDate](person-definitions.html#Person.birthDate "Person.birthDate : The birth date for the person.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [date](datatypes.html#date) | The date on which the person was born |
| ... [address](person-definitions.html#Person.address "Person.address : One or more addresses for the person.") |  | 0..\* | [Address](datatypes.html#Address) | One or more addresses for the person |
| ... [photo](person-definitions.html#Person.photo "Person.photo : An image that can be displayed as a thumbnail of the person to enhance the identification of the individual.") |  | 0..1 | [Attachment](datatypes.html#Attachment) | Image of the person |
| ... [managingOrganization](person-definitions.html#Person.managingOrganization "Person.managingOrganization : The organization that is the custodian of the person record.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [Reference](references.html#Reference)([Organization](organization.html)) | The organization that is the custodian of the person record |
| ... [active](person-definitions.html#Person.active "Person.active : Whether this person's record is in active use.") | [?!](conformance-rules.html#isModifier "This element is a modifier element")[Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [boolean](datatypes.html#boolean) | This person's record is in active use |
| ... [link](person-definitions.html#Person.link "Person.link : Link to a resource that concerns the same actual person.") |  | 0..\* | [BackboneElement](backboneelement.html) | Link to a resource that concerns the same actual person |
| .... [target](person-definitions.html#Person.link.target "Person.link.target : The resource to which this actual person is associated.") |  | 1..1 | [Reference](references.html#Reference)([Patient](patient.html) | [Practitioner](practitioner.html) | [RelatedPerson](relatedperson.html) | [Person](person.html)) | The resource to which this actual person is associated |
| .... [assurance](person-definitions.html#Person.link.assurance "Person.link.assurance : Level of assurance that this link is associated with the target resource.") |  | 0..1 | [code](datatypes.html#code) | level1 | level2 | level3 | level4 [IdentityAssuranceLevel](valueset-identity-assuranceLevel.html "The level of confidence that this link represents the same actual person, based on NIST Authentication Levels.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| [doco Documentation for this format](formats.html#table "Legend for this format") | | | | |

**UML Diagram** ([Legend](formats.html#uml))

**XML Template**

```

<Person xmlns="http://hl7.org/fhir"> ![doco](help.png)
 <!-- from Resource: id, meta, implicitRules, and language -->
 <!-- from DomainResource: text, contained, extension, and modifierExtension -->
 <identifier><!-- 0..* Identifier A human identifier for this person --></identifier>
 <name><!-- 0..* HumanName A name associated with the person --></name>
 <telecom><!-- 0..* ContactPoint A contact detail for the person --></telecom>
 <gender value="[code]"/><!-- 0..1 male | female | other | unknown -->
 <birthDate value="[date]"/><!-- 0..1 The date on which the person was born -->
 <address><!-- 0..* Address One or more addresses for the person --></address>
 <photo><!-- 0..1 Attachment Image of the person --></photo>
 <managingOrganization><!-- 0..1 Reference(Organization) The organization that is the custodian of the person record --></managingOrganization>
 <active value="[boolean]"/><!-- 0..1 This person's record is in active use -->
 <link>  <!-- 0..* Link to a resource that concerns the same actual person -->
  <target><!-- 1..1 Reference(Patient|Practitioner|RelatedPerson|Person) The resource to which this actual person is associated --></target>
  <assurance value="[code]"/><!-- 0..1 level1 | level2 | level3 | level4 -->
 </link>
</Person>
```

**JSON Template**

```

{![doco](help.png)
  "resourceType" : "Person",
  // from Resource: id, meta, implicitRules, and language
  // from DomainResource: text, contained, extension, and modifierExtension
  "identifier" : [{ Identifier }], // A human identifier for this person
  "name" : [{ HumanName }], // A name associated with the person
  "telecom" : [{ ContactPoint }], // A contact detail for the person
  "gender" : "<code>", // male | female | other | unknown
  "birthDate" : "<date>", // The date on which the person was born
  "address" : [{ Address }], // One or more addresses for the person
  "photo" : { Attachment }, // Image of the person
  "managingOrganization" : { Reference(Organization) }, // The organization that is the custodian of the person record
  "active" : <boolean>, // This person's record is in active use
  "link" : [{ // Link to a resource that concerns the same actual person
    "target" : { Reference(Patient|Practitioner|RelatedPerson|Person) }, // R!  The resource to which this actual person is associated
    "assurance" : "<code>" // level1 | level2 | level3 | level4
  }]
}
```

**Turtle Template**

```

@prefix fhir: <http://hl7.org/fhir/> .![doco](help.png)


[ a fhir:Person;
  fhir:nodeRole fhir:treeRoot; # if this is the parser root

  # from Resource: .id, .meta, .implicitRules, and .language
  # from DomainResource: .text, .contained, .extension, and .modifierExtension
  fhir:Person.identifier [ Identifier ], ... ; # 0..* A human identifier for this person
  fhir:Person.name [ HumanName ], ... ; # 0..* A name associated with the person
  fhir:Person.telecom [ ContactPoint ], ... ; # 0..* A contact detail for the person
  fhir:Person.gender [ code ]; # 0..1 male | female | other | unknown
  fhir:Person.birthDate [ date ]; # 0..1 The date on which the person was born
  fhir:Person.address [ Address ], ... ; # 0..* One or more addresses for the person
  fhir:Person.photo [ Attachment ]; # 0..1 Image of the person
  fhir:Person.managingOrganization [ Reference(Organization) ]; # 0..1 The organization that is the custodian of the person record
  fhir:Person.active [ boolean ]; # 0..1 This person's record is in active use
  fhir:Person.link [ # 0..* Link to a resource that concerns the same actual person
    fhir:Person.link.target [ Reference(Patient|Practitioner|RelatedPerson|Person) ]; # 1..1 The resource to which this actual person is associated
    fhir:Person.link.assurance [ code ]; # 0..1 level1 | level2 | level3 | level4
  ], ...;
]
```

**Changes since R3**

|  |  |
| --- | --- |
| [Person](person.html#Person) |  |
| Person.gender | - Change value set from http://hl7.org/fhir/ValueSet/administrative-gender to http://hl7.org/fhir/ValueSet/administrative-gender|4.0.1 |
| Person.link.assurance | - Change value set from http://hl7.org/fhir/ValueSet/identity-assuranceLevel to http://hl7.org/fhir/ValueSet/identity-assuranceLevel|4.0.1 |

See the [Full Difference](diff.html) for further information

This analysis is available as [XML](person.diff.xml) or [JSON](person.diff.json).

See [R3 <--> R4 Conversion Maps](person-version-maps.html) (status = 5 tests that all execute ok. All tests pass round-trip testing and all r3 resources are valid.)

**Structure**

| [Name](formats.html#table "The logical name of the element") | [Flags](formats.html#table "Information about the use of the element") | [Card.](formats.html#table "Minimum and Maximum # of times the the element can appear in the instance") | [Type](formats.html#table "Reference to the type of the element") | [Description & Constraints](formats.html#table "Additional information about the element")[doco](formats.html#table "Legend for this format") |
| --- | --- | --- | --- | --- |
| .. [Person](person-definitions.html#Person "Person : Demographics and administrative information about a person independent of a specific health-related context.") | [TU](versions.html#std-process "Standards Status = Trial Use") |  | [DomainResource](domainresource.html) | A generic person record Elements defined in Ancestors: [id](resource.html#Resource "The logical id of the resource, as used in the URL for the resource. Once assigned, this value never changes."), [meta](resource.html#Resource "The metadata about the resource. This is content that is maintained by the infrastructure. Changes to the content might not always be associated with version changes to the resource."), [implicitRules](resource.html#Resource "A reference to a set of rules that were followed when the resource was constructed, and which must be understood when processing the content. Often, this is a reference to an implementation guide that defines the special rules along with other profiles etc."), [language](resource.html#Resource "The base language in which the resource is written."), [text](domainresource.html#DomainResource "A human-readable narrative that contains a summary of the resource and can be used to represent the content of the resource to a human. The narrative need not encode all the structured data, but is required to contain sufficient detail to make it \"clinically safe\" for a human to just read the narrative. Resource definitions may define what content should be represented in the narrative to ensure clinical safety."), [contained](domainresource.html#DomainResource "These resources do not have an independent existence apart from the resource that contains them - they cannot be identified independently, and nor can they have their own independent transaction scope."), [extension](domainresource.html#DomainResource "May be used to represent additional information that is not part of the basic definition of the resource. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension."), [modifierExtension](domainresource.html#DomainResource "May be used to represent additional information that is not part of the basic definition of the resource and that modifies the understanding of the element that contains it and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer is allowed to define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.  Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).") |
| ... [identifier](person-definitions.html#Person.identifier "Person.identifier : Identifier for a person within a particular scope.") |  | 0..\* | [Identifier](datatypes.html#Identifier) | A human identifier for this person |
| ... [name](person-definitions.html#Person.name "Person.name : A name associated with the person.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [HumanName](datatypes.html#HumanName) | A name associated with the person |
| ... [telecom](person-definitions.html#Person.telecom "Person.telecom : A contact detail for the person, e.g. a telephone number or an email address.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [ContactPoint](datatypes.html#ContactPoint) | A contact detail for the person |
| ... [gender](person-definitions.html#Person.gender "Person.gender : Administrative Gender.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [code](datatypes.html#code) | male | female | other | unknown [AdministrativeGender](valueset-administrative-gender.html "The gender of a person used for administrative purposes.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ... [birthDate](person-definitions.html#Person.birthDate "Person.birthDate : The birth date for the person.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [date](datatypes.html#date) | The date on which the person was born |
| ... [address](person-definitions.html#Person.address "Person.address : One or more addresses for the person.") |  | 0..\* | [Address](datatypes.html#Address) | One or more addresses for the person |
| ... [photo](person-definitions.html#Person.photo "Person.photo : An image that can be displayed as a thumbnail of the person to enhance the identification of the individual.") |  | 0..1 | [Attachment](datatypes.html#Attachment) | Image of the person |
| ... [managingOrganization](person-definitions.html#Person.managingOrganization "Person.managingOrganization : The organization that is the custodian of the person record.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [Reference](references.html#Reference)([Organization](organization.html)) | The organization that is the custodian of the person record |
| ... [active](person-definitions.html#Person.active "Person.active : Whether this person's record is in active use.") | [?!](conformance-rules.html#isModifier "This element is a modifier element")[Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [boolean](datatypes.html#boolean) | This person's record is in active use |
| ... [link](person-definitions.html#Person.link "Person.link : Link to a resource that concerns the same actual person.") |  | 0..\* | [BackboneElement](backboneelement.html) | Link to a resource that concerns the same actual person |
| .... [target](person-definitions.html#Person.link.target "Person.link.target : The resource to which this actual person is associated.") |  | 1..1 | [Reference](references.html#Reference)([Patient](patient.html) | [Practitioner](practitioner.html) | [RelatedPerson](relatedperson.html) | [Person](person.html)) | The resource to which this actual person is associated |
| .... [assurance](person-definitions.html#Person.link.assurance "Person.link.assurance : Level of assurance that this link is associated with the target resource.") |  | 0..1 | [code](datatypes.html#code) | level1 | level2 | level3 | level4 [IdentityAssuranceLevel](valueset-identity-assuranceLevel.html "The level of confidence that this link represents the same actual person, based on NIST Authentication Levels.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| [doco Documentation for this format](formats.html#table "Legend for this format") | | | | |

**UML Diagram** ([Legend](formats.html#uml))

**XML Template**

```

<Person xmlns="http://hl7.org/fhir"> ![doco](help.png)
 <!-- from Resource: id, meta, implicitRules, and language -->
 <!-- from DomainResource: text, contained, extension, and modifierExtension -->
 <identifier><!-- 0..* Identifier A human identifier for this person --></identifier>
 <name><!-- 0..* HumanName A name associated with the person --></name>
 <telecom><!-- 0..* ContactPoint A contact detail for the person --></telecom>
 <gender value="[code]"/><!-- 0..1 male | female | other | unknown -->
 <birthDate value="[date]"/><!-- 0..1 The date on which the person was born -->
 <address><!-- 0..* Address One or more addresses for the person --></address>
 <photo><!-- 0..1 Attachment Image of the person --></photo>
 <managingOrganization><!-- 0..1 Reference(Organization) The organization that is the custodian of the person record --></managingOrganization>
 <active value="[boolean]"/><!-- 0..1 This person's record is in active use -->
 <link>  <!-- 0..* Link to a resource that concerns the same actual person -->
  <target><!-- 1..1 Reference(Patient|Practitioner|RelatedPerson|Person) The resource to which this actual person is associated --></target>
  <assurance value="[code]"/><!-- 0..1 level1 | level2 | level3 | level4 -->
 </link>
</Person>
```

**JSON Template**

```

{![doco](help.png)
  "resourceType" : "Person",
  // from Resource: id, meta, implicitRules, and language
  // from DomainResource: text, contained, extension, and modifierExtension
  "identifier" : [{ Identifier }], // A human identifier for this person
  "name" : [{ HumanName }], // A name associated with the person
  "telecom" : [{ ContactPoint }], // A contact detail for the person
  "gender" : "<code>", // male | female | other | unknown
  "birthDate" : "<date>", // The date on which the person was born
  "address" : [{ Address }], // One or more addresses for the person
  "photo" : { Attachment }, // Image of the person
  "managingOrganization" : { Reference(Organization) }, // The organization that is the custodian of the person record
  "active" : <boolean>, // This person's record is in active use
  "link" : [{ // Link to a resource that concerns the same actual person
    "target" : { Reference(Patient|Practitioner|RelatedPerson|Person) }, // R!  The resource to which this actual person is associated
    "assurance" : "<code>" // level1 | level2 | level3 | level4
  }]
}
```

**Turtle Template**

```

@prefix fhir: <http://hl7.org/fhir/> .![doco](help.png)


[ a fhir:Person;
  fhir:nodeRole fhir:treeRoot; # if this is the parser root

  # from Resource: .id, .meta, .implicitRules, and .language
  # from DomainResource: .text, .contained, .extension, and .modifierExtension
  fhir:Person.identifier [ Identifier ], ... ; # 0..* A human identifier for this person
  fhir:Person.name [ HumanName ], ... ; # 0..* A name associated with the person
  fhir:Person.telecom [ ContactPoint ], ... ; # 0..* A contact detail for the person
  fhir:Person.gender [ code ]; # 0..1 male | female | other | unknown
  fhir:Person.birthDate [ date ]; # 0..1 The date on which the person was born
  fhir:Person.address [ Address ], ... ; # 0..* One or more addresses for the person
  fhir:Person.photo [ Attachment ]; # 0..1 Image of the person
  fhir:Person.managingOrganization [ Reference(Organization) ]; # 0..1 The organization that is the custodian of the person record
  fhir:Person.active [ boolean ]; # 0..1 This person's record is in active use
  fhir:Person.link [ # 0..* Link to a resource that concerns the same actual person
    fhir:Person.link.target [ Reference(Patient|Practitioner|RelatedPerson|Person) ]; # 1..1 The resource to which this actual person is associated
    fhir:Person.link.assurance [ code ]; # 0..1 level1 | level2 | level3 | level4
  ], ...;
]
```

**Changes since Release 3**

|  |  |
| --- | --- |
| [Person](person.html#Person) |  |
| Person.gender | - Change value set from http://hl7.org/fhir/ValueSet/administrative-gender to http://hl7.org/fhir/ValueSet/administrative-gender|4.0.1 |
| Person.link.assurance | - Change value set from http://hl7.org/fhir/ValueSet/identity-assuranceLevel to http://hl7.org/fhir/ValueSet/identity-assuranceLevel|4.0.1 |

See the [Full Difference](diff.html) for further information

This analysis is available as [XML](person.diff.xml) or [JSON](person.diff.json).

See [R3 <--> R4 Conversion Maps](person-version-maps.html) (status = 5 tests that all execute ok. All tests pass round-trip testing and all r3 resources are valid.)

See the [Profiles & Extensions](person-profiles.html) and the alternate definitions:
Master Definition [XML](person.profile.xml.html) + [JSON](person.profile.json.html),
[XML](xml.html) [Schema](person.xsd)/[Schematron](person.sch) + [JSON](json.html)
[Schema](person.schema.json.html), [ShEx](person.shex.html) (for [Turtle](rdf.html)) + [see the extensions](person-profiles.html) & the [dependency analysis](person-dependencies.html)

### 8.18.3.1 Terminology Bindings

| Path | Definition | Type | Reference |
| --- | --- | --- | --- |
| Person.gender | The gender of a person used for administrative purposes. | [Required](terminologies.html#required) | [AdministrativeGender](valueset-administrative-gender.html) |
| Person.link.assurance | The level of confidence that this link represents the same actual person, based on NIST Authentication Levels. | [Required](terminologies.html#required) | [IdentityAssuranceLevel](valueset-identity-assuranceLevel.html) |

## 8.18.4 De-normalized Data

Most of the properties of the Person resource are replicated within the other resources that they
are shared with. This is intentional and highlights the loose coupling of the resources.

Not many systems implement a shared Person record, and as such the values DO become out of
sync with each other. The inclusion of this resource does permit a capability for systems to identify
other instances of this actual person's data via a centralized registry that can assist in keeping things
up to date.

## 8.18.5 Person and Linking

The *link* element is used to relate resources under a common person record.
This element supports two primary scenarios where other resources refer to the same person resource.

The *link* element cannot be used to link to RelatedPerson entries, so we can use a Person
resource to relate these elements together identifying them as the same individual.

## 8.18.6 Cross-Domain Patient Directory

In a data sharing network, finding the location of patient records across different systems is a
necessary pre-requisite for accessing external patient data. Using the *link* element, systems associate
patient resources from different organizations. The assuranceLevel associated with the *link* provides
a way for a system to qualify its confidence in the asserted *link*. For example, a relationship from
the person to a patient using a probabilistic matching algorithm may be represented using a *link* with
an assurance level of level1, while a relationship established using a government-issued photo ID may
be created with an assurance level of level3.

## 8.18.7 Cross-Domain Provider Directory

Similarly, providers working in multiple healthcare service settings may be linked across different
organizations using the *link* element. The various practitioner resources can be related using a common
person resource with a *link* for each of the practitioner resources located in other organizations.

## 8.18.8 Person Master Index

Many national and state programs maintain a central register of people, and their key Identifiers.
These systems do not store any health related information, they are purely a validated set data, often
provided by government departments. These may contain identifiers for patients, practitioners from various
departments for various purposes. Access to these systems typically requires some form of professional
role or permission, such as those in healthcare, law enforcement, or other internal government uses.

These may also operate outside of government in the private sector, such as associations or networks
that a person may be involved with and may work in the same was as they do inside government.
The usage of the data into the healthcare environment is not the only use of the register.

> **Note:** This style of system may use the Person resource without any FHIR references
> to Patient or Practitioner resources. In these environments the Master Index is likely to
> have a master identifier that performs this logical linking.  
> This style of usage has fewer security implications, as it doesn’t disclose where the
> information is being used.

## 8.18.9 Client Portal

Client Portals provide consumer access to a window of their data locked up in healthcare systems.
In many cases these systems are externally integrated and do not have access to the legacy CIS/PAS systems.

In contrast to most systems where a user has access to multiple patients depending on their roles and permissions,
a client portal provides a consumer with direct access to their data (with permissions applied).
This can also include not just their data (via the Person.link Patient entries), but also to information that they
have entered, or were involved with (via the Person.link RelatedPerson entries), such as observations that they
entered.  
With appropriate permissions/consent applied, the user could have access to other Patient records linked via
a RelatedPerson.

## 8.18.10 Security and Privacy Considerations

The Person resource may contain identifying and demographic information about an individual, therefore it must
be protected as Identifying Information.

The Person resource may contain references to the individual's other various Patient, Practitioner,
and RelatedPerson resources, where the referenced record might be to very sensitive information.
The access to the linked sensitive Resource may be protected, but the link itself may expose information.  
For example where a Practitioner and Patient resource are linked through a Person resource, inspecting the
Patient URL could reveal that the Practitioner has a record at a sensitive medical health clinic (e.g. Drug Rehabilitation Clinic).

When implementing the Person resource consideration should be given to the security and privacy
of this information. Some mitigations to these risks include higher access control protections, filling
out the Person resource as sparsely as practical for the given use-cases, and masking some data elements for
certain users of the information. Additional security guidance can be found on the [security page](security.html).

## 8.18.11 Search Parameters

Search parameters for this resource. The [common parameters](search.html#all) also apply. See [Searching](search.html) for more information about searching in REST, messaging, and services.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Name** | **Type** | **Description** | **Expression** | **In Common** |
| address | [string](search.html#string) | A server defined search that may match any of the string fields in the Address, including line, city, district, state, country, postalCode, and/or text | Person.address | [3 Resources](searchparameter-registry.html#individual-address) |
| address-city | [string](search.html#string) | A city specified in an address | Person.address.city | [3 Resources](searchparameter-registry.html#individual-address-city) |
| address-country | [string](search.html#string) | A country specified in an address | Person.address.country | [3 Resources](searchparameter-registry.html#individual-address-country) |
| address-postalcode | [string](search.html#string) | A postal code specified in an address | Person.address.postalCode | [3 Resources](searchparameter-registry.html#individual-address-postalcode) |
| address-state | [string](search.html#string) | A state specified in an address | Person.address.state | [3 Resources](searchparameter-registry.html#individual-address-state) |
| address-use | [token](search.html#token) | A use code specified in an address | Person.address.use | [3 Resources](searchparameter-registry.html#individual-address-use) |
| birthdate | [date](search.html#date) | The person's date of birth | Person.birthDate | [2 Resources](searchparameter-registry.html#individual-birthdate) |
| email | [token](search.html#token) | A value in an email contact | Person.telecom.where(system='email') | [4 Resources](searchparameter-registry.html#individual-email) |
| gender | [token](search.html#token) | The gender of the person | Person.gender | [3 Resources](searchparameter-registry.html#individual-gender) |
| identifier | [token](search.html#token) | A person Identifier | Person.identifier |  |
| link | [reference](search.html#reference) | Any link has this Patient, Person, RelatedPerson or Practitioner reference | Person.link.target ([Practitioner](practitioner.html), [Patient](patient.html), [Person](person.html), [RelatedPerson](relatedperson.html)) |  |
| name | [string](search.html#string) | A server defined search that may match any of the string fields in the HumanName, including family, give, prefix, suffix, suffix, and/or text | Person.name |  |
| organization | [reference](search.html#reference) | The organization at which this person record is being managed | Person.managingOrganization ([Organization](organization.html)) |  |
| patient | [reference](search.html#reference) | The Person links to this Patient | Person.link.target.where(resolve() is Patient) ([Patient](patient.html)) |  |
| phone | [token](search.html#token) | A value in a phone contact | Person.telecom.where(system='phone') | [4 Resources](searchparameter-registry.html#individual-phone) |
| phonetic | [string](search.html#string) | A portion of name using some kind of phonetic matching algorithm | Person.name | [3 Resources](searchparameter-registry.html#individual-phonetic) |
| practitioner | [reference](search.html#reference) | The Person links to this Practitioner | Person.link.target.where(resolve() is Practitioner) ([Practitioner](practitioner.html)) |  |
| relatedperson | [reference](search.html#reference) | The Person links to this RelatedPerson | Person.link.target.where(resolve() is RelatedPerson) ([RelatedPerson](relatedperson.html)) |  |
| telecom | [token](search.html#token) | The value in any kind of contact | Person.telecom | [4 Resources](searchparameter-registry.html#individual-telecom) |

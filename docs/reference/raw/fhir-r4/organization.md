---
id: organization
title: Organization
source_url: https://hl7.org/fhir/R4/organization.html
group: fhir-r4
fhir_version: R4
fetched_at: '2026-09-11T13:22:37Z'
sha256: 4d221fdead869eb7956873c8abeb70eaa98e8847293152b48f6e68d091b102dc
---
This page is part of the FHIR Specification (v4.0.1: R4 - Mixed [Normative](https://confluence.hl7.org/display/HL7/HL7+Balloting "Normative Standard") and [STU](https://confluence.hl7.org/display/HL7/HL7+Balloting "Standard for Trial-Use")) in it's permanent home (it will always be available at this URL). The current version which supercedes this version is [5.0.0](http://hl7.org/fhir/index.html). For a full list of available versions, see the [Directory of published versions ![](external.png)](http://hl7.org/fhir/directory.html). Page versions: [R5](http://hl7.org/fhir/R5/organization.html) [R4B](http://hl7.org/fhir/R4B/organization.html) **R4** [R3](http://hl7.org/fhir/STU3/organization.html) [R2](http://hl7.org/fhir/DSTU2/organization.html)

- [Content](#)
- [Examples](organization-examples.html)
- [Detailed Descriptions](organization-definitions.html)
- [Mappings](organization-mappings.html)
- [Profiles & Extensions](organization-profiles.html)
- [R3 Conversions](organization-version-maps.html)

# 8.6 Resource Organization - Content

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [Patient Administration](http://www.hl7.org/Special/committees/pafm/index.cfm)  Work Group | [Maturity Level](versions.html#maturity): 3 | [Trial Use](versions.html#std-process "Standard Status") | [Security Category](security.html#SecPrivConsiderations): Business | [Compartments](compartmentdefinition.html): Not linked to any defined compartments |

A formally or informally recognized grouping of people or organizations formed for the purpose of achieving some form of collective action. Includes companies, institutions, corporations, departments, community groups, healthcare practice groups, payer/insurer, etc.

## 8.6.1 Scope and Usage

This resource may be used in a shared registry of contact and other information for various organizations or it can be used merely as a support
for other resources that need to reference organizations, perhaps as a [document](documents.html), [message](messaging.html) or
as a [contained](references.html#contained) resource. If using a registry approach, it's entirely possible for multiple registries to exist, each dealing
with different types or levels of organization.

## 8.6.2 Boundaries and Relationships

The Organization resource is used for collections of people that have come together to achieve an objective.
The [Group](group.html) resource is used to identify a collection of people (or animals, devices, etc.)
that are gathered for the purpose of analysis or acting upon, but are not expected to act themselves.

The Organization resource often exists as a hierarchy of organization resources, using the *part-of* property to provide
the association of the child to its parent organization.  
This organizational hierarchy helps communicate the conceptual structure, whereas the Location resource provides the physical
representation of the hierarchy.  
The linkage between Organization and Location is from each point in the location hierarchy to the appropriate level in the
Organization hierarchy. These links don't all have to be to the top level Organization.  
When populating the organization and location hierarchies there is often not a clear distinction between these 2, however
to assist in making the decision, Locations are always used for recording where a service occurs, and hence where encounters
and observations are associated. The Organization property on these resources might not be the location where the service took place.

This resource is referenced by [Annotation](datatypes.html#Annotation), [Identifier](datatypes.html#Identifier), [Signature](datatypes.html#Signature), [UsageContext](metadatatypes.html#UsageContext), [Account](account.html#Account), [AuditEvent](auditevent.html#AuditEvent), [Basic](basic.html#Basic), [BiologicallyDerivedProduct](biologicallyderivedproduct.html#BiologicallyDerivedProduct), [CapabilityStatement](capabilitystatement.html#CapabilityStatement), [CarePlan](careplan.html#CarePlan), [CareTeam](careteam.html#CareTeam), [CatalogEntry](catalogentry.html#CatalogEntry), [ChargeItem](chargeitem.html#ChargeItem), [Claim](claim.html#Claim), [ClaimResponse](claimresponse.html#ClaimResponse), [Communication](communication.html#Communication), [CommunicationRequest](communicationrequest.html#CommunicationRequest), [Composition](composition.html#Composition), [Consent](consent.html#Consent), [Contract](contract.html#Contract), [Coverage](coverage.html#Coverage), [CoverageEligibilityRequest](coverageeligibilityrequest.html#CoverageEligibilityRequest), [CoverageEligibilityResponse](coverageeligibilityresponse.html#CoverageEligibilityResponse), [Device](device.html#Device), [DeviceDefinition](devicedefinition.html#DeviceDefinition), [DeviceRequest](devicerequest.html#DeviceRequest), [DiagnosticReport](diagnosticreport.html#DiagnosticReport), [DocumentManifest](documentmanifest.html#DocumentManifest), [DocumentReference](documentreference.html#DocumentReference), [Encounter](encounter.html#Encounter), [Endpoint](endpoint.html#Endpoint), [EnrollmentRequest](enrollmentrequest.html#EnrollmentRequest), [EnrollmentResponse](enrollmentresponse.html#EnrollmentResponse), [EpisodeOfCare](episodeofcare.html#EpisodeOfCare), [ExplanationOfBenefit](explanationofbenefit.html#ExplanationOfBenefit), [Flag](flag.html#Flag), [Goal](goal.html#Goal), [Group](group.html#Group), [HealthcareService](healthcareservice.html#HealthcareService), [ImagingStudy](imagingstudy.html#ImagingStudy), [Immunization](immunization.html#Immunization), [ImmunizationEvaluation](immunizationevaluation.html#ImmunizationEvaluation), [ImmunizationRecommendation](immunizationrecommendation.html#ImmunizationRecommendation), [InsurancePlan](insuranceplan.html#InsurancePlan), [Invoice](invoice.html#Invoice), [Linkage](linkage.html#Linkage), [Location](location.html#Location), [MeasureReport](measurereport.html#MeasureReport), [Media](media.html#Media), [Medication](medication.html#Medication), [MedicationDispense](medicationdispense.html#MedicationDispense), [MedicationKnowledge](medicationknowledge.html#MedicationKnowledge), [MedicationRequest](medicationrequest.html#MedicationRequest), [MedicationStatement](medicationstatement.html#MedicationStatement), [MedicinalProduct](medicinalproduct.html#MedicinalProduct), [MedicinalProductAuthorization](medicinalproductauthorization.html#MedicinalProductAuthorization), [MedicinalProductIngredient](medicinalproductingredient.html#MedicinalProductIngredient), [MedicinalProductManufactured](medicinalproductmanufactured.html#MedicinalProductManufactured), [MedicinalProductPackaged](medicinalproductpackaged.html#MedicinalProductPackaged), [MessageHeader](messageheader.html#MessageHeader), [MolecularSequence](molecularsequence.html#MolecularSequence), [Observation](observation.html#Observation), itself, [OrganizationAffiliation](organizationaffiliation.html#OrganizationAffiliation), [Patient](patient.html#Patient), [PaymentNotice](paymentnotice.html#PaymentNotice), [PaymentReconciliation](paymentreconciliation.html#PaymentReconciliation), [Person](person.html#Person), [Practitioner](practitioner.html#Practitioner), [PractitionerRole](practitionerrole.html#PractitionerRole), [Procedure](procedure.html#Procedure), [Provenance](provenance.html#Provenance), [QuestionnaireResponse](questionnaireresponse.html#QuestionnaireResponse), [ResearchStudy](researchstudy.html#ResearchStudy), [ServiceRequest](servicerequest.html#ServiceRequest), [SupplyDelivery](supplydelivery.html#SupplyDelivery), [SupplyRequest](supplyrequest.html#SupplyRequest), [Task](task.html#Task) and [VerificationResult](verificationresult.html#VerificationResult)

## 8.6.3 Resource Content

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
| .. [Organization](organization-definitions.html#Organization "Organization : A formally or informally recognized grouping of people or organizations formed for the purpose of achieving some form of collective action.  Includes companies, institutions, corporations, departments, community groups, healthcare practice groups, payer/insurer, etc.") | [I](conformance-rules.html#constraints "This element has or is affected by some invariants")[TU](versions.html#std-process "Standards Status = Trial Use") |  | [DomainResource](domainresource.html) | A grouping of people or organizations with a common purpose + Rule: The organization SHALL at least have a name or an identifier, and possibly more than one Elements defined in Ancestors: [id](resource.html#Resource "The logical id of the resource, as used in the URL for the resource. Once assigned, this value never changes."), [meta](resource.html#Resource "The metadata about the resource. This is content that is maintained by the infrastructure. Changes to the content might not always be associated with version changes to the resource."), [implicitRules](resource.html#Resource "A reference to a set of rules that were followed when the resource was constructed, and which must be understood when processing the content. Often, this is a reference to an implementation guide that defines the special rules along with other profiles etc."), [language](resource.html#Resource "The base language in which the resource is written."), [text](domainresource.html#DomainResource "A human-readable narrative that contains a summary of the resource and can be used to represent the content of the resource to a human. The narrative need not encode all the structured data, but is required to contain sufficient detail to make it \"clinically safe\" for a human to just read the narrative. Resource definitions may define what content should be represented in the narrative to ensure clinical safety."), [contained](domainresource.html#DomainResource "These resources do not have an independent existence apart from the resource that contains them - they cannot be identified independently, and nor can they have their own independent transaction scope."), [extension](domainresource.html#DomainResource "May be used to represent additional information that is not part of the basic definition of the resource. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension."), [modifierExtension](domainresource.html#DomainResource "May be used to represent additional information that is not part of the basic definition of the resource and that modifies the understanding of the element that contains it and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer is allowed to define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.  Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).") |
| ... [identifier](organization-definitions.html#Organization.identifier "Organization.identifier : Identifier for the organization that is used to identify the organization across multiple disparate systems.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..\* | [Identifier](datatypes.html#Identifier) | Identifies this organization across multiple systems |
| ... [active](organization-definitions.html#Organization.active "Organization.active : Whether the organization's record is still in active use.") | [?!](conformance-rules.html#isModifier "This element is a modifier element")[Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [boolean](datatypes.html#boolean) | Whether the organization's record is still in active use |
| ... [type](organization-definitions.html#Organization.type "Organization.type : The kind(s) of organization that this is.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [CodeableConcept](datatypes.html#CodeableConcept) | Kind of organization [Organization type](valueset-organization-type.html "Used to categorize the organization.") ([Example](terminologies.html#example "Instances are not expected or even encouraged to draw from the specified value set.  The value set merely provides examples of the types of concepts intended to be included.")) |
| ... [name](organization-definitions.html#Organization.name "Organization.name : A name associated with the organization.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..1 | [string](datatypes.html#string) | Name used for the organization |
| ... [alias](organization-definitions.html#Organization.alias "Organization.alias : A list of alternate names that the organization is known as, or was known as in the past.") |  | 0..\* | [string](datatypes.html#string) | A list of alternate names that the organization is known as, or was known as in the past |
| ... [telecom](organization-definitions.html#Organization.telecom "Organization.telecom : A contact detail for the organization.") | [I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..\* | [ContactPoint](datatypes.html#ContactPoint) | A contact detail for the organization + Rule: The telecom of an organization can never be of use 'home' |
| ... [address](organization-definitions.html#Organization.address "Organization.address : An address for the organization.") | [I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..\* | [Address](datatypes.html#Address) | An address for the organization + Rule: An address of an organization can never be of use 'home' |
| ... [partOf](organization-definitions.html#Organization.partOf "Organization.partOf : The organization of which this organization forms a part.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [Reference](references.html#Reference)([Organization](organization.html)) | The organization of which this organization forms a part |
| ... [contact](organization-definitions.html#Organization.contact "Organization.contact : Contact for the organization for a certain purpose.") |  | 0..\* | [BackboneElement](backboneelement.html) | Contact for the organization for a certain purpose |
| .... [purpose](organization-definitions.html#Organization.contact.purpose "Organization.contact.purpose : Indicates a purpose for which the contact can be reached.") |  | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | The type of contact [Contact entity type](valueset-contactentity-type.html "The purpose for which you would contact a contact party.") ([Extensible](terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept (based on human review), alternate codings (or, data type allowing, text) may be included instead.")) |
| .... [name](organization-definitions.html#Organization.contact.name "Organization.contact.name : A name associated with the contact.") |  | 0..1 | [HumanName](datatypes.html#HumanName) | A name associated with the contact |
| .... [telecom](organization-definitions.html#Organization.contact.telecom "Organization.contact.telecom : A contact detail (e.g. a telephone number or an email address) by which the party may be contacted.") |  | 0..\* | [ContactPoint](datatypes.html#ContactPoint) | Contact details (telephone, email, etc.) for a contact |
| .... [address](organization-definitions.html#Organization.contact.address "Organization.contact.address : Visiting or postal addresses for the contact.") |  | 0..1 | [Address](datatypes.html#Address) | Visiting or postal addresses for the contact |
| ... [endpoint](organization-definitions.html#Organization.endpoint "Organization.endpoint : Technical endpoints providing access to services operated for the organization.") |  | 0..\* | [Reference](references.html#Reference)([Endpoint](endpoint.html)) | Technical endpoints providing access to services operated for the organization |
| [doco Documentation for this format](formats.html#table "Legend for this format") | | | | |

**UML Diagram** ([Legend](formats.html#uml))

**XML Template**

```

<Organization xmlns="http://hl7.org/fhir"> ![doco](help.png)
 <!-- from Resource: id, meta, implicitRules, and language -->
 <!-- from DomainResource: text, contained, extension, and modifierExtension -->
 <identifier><!-- ![??](lock.png) 0..* Identifier Identifies this organization  across multiple systems --></identifier>
 <active value="[boolean]"/><!-- 0..1 Whether the organization's record is still in active use -->
 <type><!-- 0..* CodeableConcept Kind of organization --></type>
 <name value="[string]"/><!-- ![??](lock.png) 0..1 Name used for the organization -->
 <alias value="[string]"/><!-- 0..* A list of alternate names that the organization is known as, or was known as in the past -->
 <telecom><!-- ![??](lock.png) 0..* ContactPoint A contact detail for the organization --></telecom>
 <address><!-- ![??](lock.png) 0..* Address An address for the organization --></address>
 <partOf><!-- 0..1 Reference(Organization) The organization of which this organization forms a part --></partOf>
 <contact>  <!-- 0..* Contact for the organization for a certain purpose -->
  <purpose><!-- 0..1 CodeableConcept The type of contact --></purpose>
  <name><!-- 0..1 HumanName A name associated with the contact --></name>
  <telecom><!-- 0..* ContactPoint Contact details (telephone, email, etc.)  for a contact --></telecom>
  <address><!-- 0..1 Address Visiting or postal addresses for the contact --></address>
 </contact>
 <endpoint><!-- 0..* Reference(Endpoint) Technical endpoints providing access to services operated for the organization --></endpoint>
</Organization>
```

**JSON Template**

```

{![doco](help.png)
  "resourceType" : "Organization",
  // from Resource: id, meta, implicitRules, and language
  // from DomainResource: text, contained, extension, and modifierExtension
  "identifier" : [{ Identifier }], // C? Identifies this organization  across multiple systems
  "active" : <boolean>, // Whether the organization's record is still in active use
  "type" : [{ CodeableConcept }], // Kind of organization
  "name" : "<string>", // C? Name used for the organization
  "alias" : ["<string>"], // A list of alternate names that the organization is known as, or was known as in the past
  "telecom" : [{ ContactPoint }], // C? A contact detail for the organization
  "address" : [{ Address }], // C? An address for the organization
  "partOf" : { Reference(Organization) }, // The organization of which this organization forms a part
  "contact" : [{ // Contact for the organization for a certain purpose
    "purpose" : { CodeableConcept }, // The type of contact
    "name" : { HumanName }, // A name associated with the contact
    "telecom" : [{ ContactPoint }], // Contact details (telephone, email, etc.)  for a contact
    "address" : { Address } // Visiting or postal addresses for the contact
  }],
  "endpoint" : [{ Reference(Endpoint) }] // Technical endpoints providing access to services operated for the organization
}
```

**Turtle Template**

```

@prefix fhir: <http://hl7.org/fhir/> .![doco](help.png)


[ a fhir:Organization;
  fhir:nodeRole fhir:treeRoot; # if this is the parser root

  # from Resource: .id, .meta, .implicitRules, and .language
  # from DomainResource: .text, .contained, .extension, and .modifierExtension
  fhir:Organization.identifier [ Identifier ], ... ; # 0..* Identifies this organization  across multiple systems
  fhir:Organization.active [ boolean ]; # 0..1 Whether the organization's record is still in active use
  fhir:Organization.type [ CodeableConcept ], ... ; # 0..* Kind of organization
  fhir:Organization.name [ string ]; # 0..1 Name used for the organization
  fhir:Organization.alias [ string ], ... ; # 0..* A list of alternate names that the organization is known as, or was known as in the past
  fhir:Organization.telecom [ ContactPoint ], ... ; # 0..* A contact detail for the organization
  fhir:Organization.address [ Address ], ... ; # 0..* An address for the organization
  fhir:Organization.partOf [ Reference(Organization) ]; # 0..1 The organization of which this organization forms a part
  fhir:Organization.contact [ # 0..* Contact for the organization for a certain purpose
    fhir:Organization.contact.purpose [ CodeableConcept ]; # 0..1 The type of contact
    fhir:Organization.contact.name [ HumanName ]; # 0..1 A name associated with the contact
    fhir:Organization.contact.telecom [ ContactPoint ], ... ; # 0..* Contact details (telephone, email, etc.)  for a contact
    fhir:Organization.contact.address [ Address ]; # 0..1 Visiting or postal addresses for the contact
  ], ...;
  fhir:Organization.endpoint [ Reference(Endpoint) ], ... ; # 0..* Technical endpoints providing access to services operated for the organization
]
```

**Changes since R3**

|  |  |
| --- | --- |
| [Organization](organization.html#Organization) |  |
| Organization.active | - Default Value "true" removed |
| Organization.contact.purpose | - Change code system for extensibly bound codes from "http://hl7.org/fhir/contactentity-type" to "http://terminology.hl7.org/CodeSystem/contactentity-type" |

See the [Full Difference](diff.html) for further information

This analysis is available as [XML](organization.diff.xml) or [JSON](organization.diff.json).

See [R3 <--> R4 Conversion Maps](organization-version-maps.html) (status = 11 tests that all execute ok. All tests pass round-trip testing and 1 r3 resources are invalid (0 errors).)

**Structure**

| [Name](formats.html#table "The logical name of the element") | [Flags](formats.html#table "Information about the use of the element") | [Card.](formats.html#table "Minimum and Maximum # of times the the element can appear in the instance") | [Type](formats.html#table "Reference to the type of the element") | [Description & Constraints](formats.html#table "Additional information about the element")[doco](formats.html#table "Legend for this format") |
| --- | --- | --- | --- | --- |
| .. [Organization](organization-definitions.html#Organization "Organization : A formally or informally recognized grouping of people or organizations formed for the purpose of achieving some form of collective action.  Includes companies, institutions, corporations, departments, community groups, healthcare practice groups, payer/insurer, etc.") | [I](conformance-rules.html#constraints "This element has or is affected by some invariants")[TU](versions.html#std-process "Standards Status = Trial Use") |  | [DomainResource](domainresource.html) | A grouping of people or organizations with a common purpose + Rule: The organization SHALL at least have a name or an identifier, and possibly more than one Elements defined in Ancestors: [id](resource.html#Resource "The logical id of the resource, as used in the URL for the resource. Once assigned, this value never changes."), [meta](resource.html#Resource "The metadata about the resource. This is content that is maintained by the infrastructure. Changes to the content might not always be associated with version changes to the resource."), [implicitRules](resource.html#Resource "A reference to a set of rules that were followed when the resource was constructed, and which must be understood when processing the content. Often, this is a reference to an implementation guide that defines the special rules along with other profiles etc."), [language](resource.html#Resource "The base language in which the resource is written."), [text](domainresource.html#DomainResource "A human-readable narrative that contains a summary of the resource and can be used to represent the content of the resource to a human. The narrative need not encode all the structured data, but is required to contain sufficient detail to make it \"clinically safe\" for a human to just read the narrative. Resource definitions may define what content should be represented in the narrative to ensure clinical safety."), [contained](domainresource.html#DomainResource "These resources do not have an independent existence apart from the resource that contains them - they cannot be identified independently, and nor can they have their own independent transaction scope."), [extension](domainresource.html#DomainResource "May be used to represent additional information that is not part of the basic definition of the resource. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension."), [modifierExtension](domainresource.html#DomainResource "May be used to represent additional information that is not part of the basic definition of the resource and that modifies the understanding of the element that contains it and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer is allowed to define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.  Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).") |
| ... [identifier](organization-definitions.html#Organization.identifier "Organization.identifier : Identifier for the organization that is used to identify the organization across multiple disparate systems.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..\* | [Identifier](datatypes.html#Identifier) | Identifies this organization across multiple systems |
| ... [active](organization-definitions.html#Organization.active "Organization.active : Whether the organization's record is still in active use.") | [?!](conformance-rules.html#isModifier "This element is a modifier element")[Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [boolean](datatypes.html#boolean) | Whether the organization's record is still in active use |
| ... [type](organization-definitions.html#Organization.type "Organization.type : The kind(s) of organization that this is.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [CodeableConcept](datatypes.html#CodeableConcept) | Kind of organization [Organization type](valueset-organization-type.html "Used to categorize the organization.") ([Example](terminologies.html#example "Instances are not expected or even encouraged to draw from the specified value set.  The value set merely provides examples of the types of concepts intended to be included.")) |
| ... [name](organization-definitions.html#Organization.name "Organization.name : A name associated with the organization.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..1 | [string](datatypes.html#string) | Name used for the organization |
| ... [alias](organization-definitions.html#Organization.alias "Organization.alias : A list of alternate names that the organization is known as, or was known as in the past.") |  | 0..\* | [string](datatypes.html#string) | A list of alternate names that the organization is known as, or was known as in the past |
| ... [telecom](organization-definitions.html#Organization.telecom "Organization.telecom : A contact detail for the organization.") | [I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..\* | [ContactPoint](datatypes.html#ContactPoint) | A contact detail for the organization + Rule: The telecom of an organization can never be of use 'home' |
| ... [address](organization-definitions.html#Organization.address "Organization.address : An address for the organization.") | [I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..\* | [Address](datatypes.html#Address) | An address for the organization + Rule: An address of an organization can never be of use 'home' |
| ... [partOf](organization-definitions.html#Organization.partOf "Organization.partOf : The organization of which this organization forms a part.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [Reference](references.html#Reference)([Organization](organization.html)) | The organization of which this organization forms a part |
| ... [contact](organization-definitions.html#Organization.contact "Organization.contact : Contact for the organization for a certain purpose.") |  | 0..\* | [BackboneElement](backboneelement.html) | Contact for the organization for a certain purpose |
| .... [purpose](organization-definitions.html#Organization.contact.purpose "Organization.contact.purpose : Indicates a purpose for which the contact can be reached.") |  | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | The type of contact [Contact entity type](valueset-contactentity-type.html "The purpose for which you would contact a contact party.") ([Extensible](terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept (based on human review), alternate codings (or, data type allowing, text) may be included instead.")) |
| .... [name](organization-definitions.html#Organization.contact.name "Organization.contact.name : A name associated with the contact.") |  | 0..1 | [HumanName](datatypes.html#HumanName) | A name associated with the contact |
| .... [telecom](organization-definitions.html#Organization.contact.telecom "Organization.contact.telecom : A contact detail (e.g. a telephone number or an email address) by which the party may be contacted.") |  | 0..\* | [ContactPoint](datatypes.html#ContactPoint) | Contact details (telephone, email, etc.) for a contact |
| .... [address](organization-definitions.html#Organization.contact.address "Organization.contact.address : Visiting or postal addresses for the contact.") |  | 0..1 | [Address](datatypes.html#Address) | Visiting or postal addresses for the contact |
| ... [endpoint](organization-definitions.html#Organization.endpoint "Organization.endpoint : Technical endpoints providing access to services operated for the organization.") |  | 0..\* | [Reference](references.html#Reference)([Endpoint](endpoint.html)) | Technical endpoints providing access to services operated for the organization |
| [doco Documentation for this format](formats.html#table "Legend for this format") | | | | |

**UML Diagram** ([Legend](formats.html#uml))

**XML Template**

```

<Organization xmlns="http://hl7.org/fhir"> ![doco](help.png)
 <!-- from Resource: id, meta, implicitRules, and language -->
 <!-- from DomainResource: text, contained, extension, and modifierExtension -->
 <identifier><!-- ![??](lock.png) 0..* Identifier Identifies this organization  across multiple systems --></identifier>
 <active value="[boolean]"/><!-- 0..1 Whether the organization's record is still in active use -->
 <type><!-- 0..* CodeableConcept Kind of organization --></type>
 <name value="[string]"/><!-- ![??](lock.png) 0..1 Name used for the organization -->
 <alias value="[string]"/><!-- 0..* A list of alternate names that the organization is known as, or was known as in the past -->
 <telecom><!-- ![??](lock.png) 0..* ContactPoint A contact detail for the organization --></telecom>
 <address><!-- ![??](lock.png) 0..* Address An address for the organization --></address>
 <partOf><!-- 0..1 Reference(Organization) The organization of which this organization forms a part --></partOf>
 <contact>  <!-- 0..* Contact for the organization for a certain purpose -->
  <purpose><!-- 0..1 CodeableConcept The type of contact --></purpose>
  <name><!-- 0..1 HumanName A name associated with the contact --></name>
  <telecom><!-- 0..* ContactPoint Contact details (telephone, email, etc.)  for a contact --></telecom>
  <address><!-- 0..1 Address Visiting or postal addresses for the contact --></address>
 </contact>
 <endpoint><!-- 0..* Reference(Endpoint) Technical endpoints providing access to services operated for the organization --></endpoint>
</Organization>
```

**JSON Template**

```

{![doco](help.png)
  "resourceType" : "Organization",
  // from Resource: id, meta, implicitRules, and language
  // from DomainResource: text, contained, extension, and modifierExtension
  "identifier" : [{ Identifier }], // C? Identifies this organization  across multiple systems
  "active" : <boolean>, // Whether the organization's record is still in active use
  "type" : [{ CodeableConcept }], // Kind of organization
  "name" : "<string>", // C? Name used for the organization
  "alias" : ["<string>"], // A list of alternate names that the organization is known as, or was known as in the past
  "telecom" : [{ ContactPoint }], // C? A contact detail for the organization
  "address" : [{ Address }], // C? An address for the organization
  "partOf" : { Reference(Organization) }, // The organization of which this organization forms a part
  "contact" : [{ // Contact for the organization for a certain purpose
    "purpose" : { CodeableConcept }, // The type of contact
    "name" : { HumanName }, // A name associated with the contact
    "telecom" : [{ ContactPoint }], // Contact details (telephone, email, etc.)  for a contact
    "address" : { Address } // Visiting or postal addresses for the contact
  }],
  "endpoint" : [{ Reference(Endpoint) }] // Technical endpoints providing access to services operated for the organization
}
```

**Turtle Template**

```

@prefix fhir: <http://hl7.org/fhir/> .![doco](help.png)


[ a fhir:Organization;
  fhir:nodeRole fhir:treeRoot; # if this is the parser root

  # from Resource: .id, .meta, .implicitRules, and .language
  # from DomainResource: .text, .contained, .extension, and .modifierExtension
  fhir:Organization.identifier [ Identifier ], ... ; # 0..* Identifies this organization  across multiple systems
  fhir:Organization.active [ boolean ]; # 0..1 Whether the organization's record is still in active use
  fhir:Organization.type [ CodeableConcept ], ... ; # 0..* Kind of organization
  fhir:Organization.name [ string ]; # 0..1 Name used for the organization
  fhir:Organization.alias [ string ], ... ; # 0..* A list of alternate names that the organization is known as, or was known as in the past
  fhir:Organization.telecom [ ContactPoint ], ... ; # 0..* A contact detail for the organization
  fhir:Organization.address [ Address ], ... ; # 0..* An address for the organization
  fhir:Organization.partOf [ Reference(Organization) ]; # 0..1 The organization of which this organization forms a part
  fhir:Organization.contact [ # 0..* Contact for the organization for a certain purpose
    fhir:Organization.contact.purpose [ CodeableConcept ]; # 0..1 The type of contact
    fhir:Organization.contact.name [ HumanName ]; # 0..1 A name associated with the contact
    fhir:Organization.contact.telecom [ ContactPoint ], ... ; # 0..* Contact details (telephone, email, etc.)  for a contact
    fhir:Organization.contact.address [ Address ]; # 0..1 Visiting or postal addresses for the contact
  ], ...;
  fhir:Organization.endpoint [ Reference(Endpoint) ], ... ; # 0..* Technical endpoints providing access to services operated for the organization
]
```

**Changes since Release 3**

|  |  |
| --- | --- |
| [Organization](organization.html#Organization) |  |
| Organization.active | - Default Value "true" removed |
| Organization.contact.purpose | - Change code system for extensibly bound codes from "http://hl7.org/fhir/contactentity-type" to "http://terminology.hl7.org/CodeSystem/contactentity-type" |

See the [Full Difference](diff.html) for further information

This analysis is available as [XML](organization.diff.xml) or [JSON](organization.diff.json).

See [R3 <--> R4 Conversion Maps](organization-version-maps.html) (status = 11 tests that all execute ok. All tests pass round-trip testing and 1 r3 resources are invalid (0 errors).)

See the [Profiles & Extensions](organization-profiles.html) and the alternate definitions:
Master Definition [XML](organization.profile.xml.html) + [JSON](organization.profile.json.html),
[XML](xml.html) [Schema](organization.xsd)/[Schematron](organization.sch) + [JSON](json.html)
[Schema](organization.schema.json.html), [ShEx](organization.shex.html) (for [Turtle](rdf.html)) + [see the extensions](organization-profiles.html) & the [dependency analysis](organization-dependencies.html)

### 8.6.3.1 Terminology Bindings

| Path | Definition | Type | Reference |
| --- | --- | --- | --- |
| Organization.type | Used to categorize the organization. | [Example](terminologies.html#example) | [OrganizationType](valueset-organization-type.html) |
| Organization.contact.purpose | The purpose for which you would contact a contact party. | [Extensible](terminologies.html#extensible) | [ContactEntityType](valueset-contactentity-type.html) |

### 8.6.3.2 Constraints

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **id** | **Level** | **Location** | **Description** | **[Expression](fhirpath.html)** |
| **org-1** | [Rule](conformance-rules.html#rule) | (base) | The organization SHALL at least have a name or an identifier, and possibly more than one | (identifier.count() + name.count()) > 0 |
| **org-2** | [Rule](conformance-rules.html#rule) | Organization.address | An address of an organization can never be of use 'home' | where(use = 'home').empty() |
| **org-3** | [Rule](conformance-rules.html#rule) | Organization.telecom | The telecom of an organization can never be of use 'home' | where(use = 'home').empty() |

## 8.6.4 Notes:

- There are two places for contact information: one on Organization itself and zero or more using the ContactEntity construct.
  The first one is to be used for the generic, public organization point of contact. The ContactEntity is to be used for
  reaching a person or party that has been designated by the organization to be contacted for a specific purpose or goal.

## 8.6.5 Example Organization Hierarchy:

An example organization hierarchy should help give some guidance as to one example
of how a location hierarchy could look within a fictitious Medical Organization.  
*(The nesting here would be the "part-of" structure of the Organization resource)*

```

Burgers University Medical Center
    Eastern Services (prov)
        Emergency Dept
        Oncology Dept
            Nuclear Medicine Research Trials (edu)
        Maternity Ward
        Childrens Ward
        Day Procedures Unit
    Mobile Services (Ambulance)
    Research Center (edu)
        Nuclear Medicine  (edu)
    Burgers University (edu)
        Nuclear Medicine Faculty (edu)
        Undergraduate Medicine (edu)
        ...
	
```

*Note that physical structures of this hierarchy are not present - these are defined by a Location hierarchy.*

## 8.6.6 Search Parameters

Search parameters for this resource. The [common parameters](search.html#all) also apply. See [Searching](search.html) for more information about searching in REST, messaging, and services.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Name** | **Type** | **Description** | **Expression** | **In Common** |
| active | [token](search.html#token) | Is the Organization record active | Organization.active |  |
| address | [string](search.html#string) | A server defined search that may match any of the string fields in the Address, including line, city, district, state, country, postalCode, and/or text | Organization.address |  |
| address-city | [string](search.html#string) | A city specified in an address | Organization.address.city |  |
| address-country | [string](search.html#string) | A country specified in an address | Organization.address.country |  |
| address-postalcode | [string](search.html#string) | A postal code specified in an address | Organization.address.postalCode |  |
| address-state | [string](search.html#string) | A state specified in an address | Organization.address.state |  |
| address-use | [token](search.html#token) | A use code specified in an address | Organization.address.use |  |
| endpoint | [reference](search.html#reference) | Technical endpoints providing access to services operated for the organization | Organization.endpoint ([Endpoint](endpoint.html)) |  |
| identifier | [token](search.html#token) | Any identifier for the organization (not the accreditation issuer's identifier) | Organization.identifier |  |
| name | [string](search.html#string) | A portion of the organization's name or alias | Organization.name | Organization.alias |  |
| partof | [reference](search.html#reference) | An organization of which this organization forms a part | Organization.partOf ([Organization](organization.html)) |  |
| phonetic | [string](search.html#string) | A portion of the organization's name using some kind of phonetic matching algorithm | Organization.name |  |
| type | [token](search.html#token) | A code for the type of organization | Organization.type |  |

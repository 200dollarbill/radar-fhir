---
id: conformance-rules
title: Conformance Rules
source_url: https://hl7.org/fhir/R4/conformance-rules.html
group: fhir-r4
fhir_version: R4
fetched_at: '2026-09-11T13:23:29Z'
sha256: 5da28aef60406fab874115f9887cac5286a1d794538a84ec50a9ee950bbf8095
---
This page is part of the FHIR Specification (v4.0.1: R4 - Mixed [Normative](https://confluence.hl7.org/display/HL7/HL7+Balloting "Normative Standard") and [STU](https://confluence.hl7.org/display/HL7/HL7+Balloting "Standard for Trial-Use")) in it's permanent home (it will always be available at this URL). The current version which supercedes this version is [5.0.0](http://hl7.org/fhir/index.html). For a full list of available versions, see the [Directory of published versions ![](external.png)](http://hl7.org/fhir/directory.html). Page versions: [R5](http://hl7.org/fhir/R5/conformance-rules.html) [R4B](http://hl7.org/fhir/R4B/conformance-rules.html) **R4** [R3](http://hl7.org/fhir/STU3/conformance-rules.html) [R2](http://hl7.org/fhir/DSTU2/conformance-rules.html)

## 2.1.0 Conformance

|  |  |  |
| --- | --- | --- |
| [FHIR Infrastructure](http://www.hl7.org/Special/committees/fiwg/index.cfm)  Work Group | [Maturity Level](versions.html#maturity): Normative | [Standards Status](versions.html#std-process): [Normative](versions.html#std-process) |

|  |  |
| --- | --- |
|  | This page has been approved as part of an [ANSI](https://www.ansi.org/)  standard. See the [Infrastructure](ansi-infrastructure.html) Package for further details. |

The FHIR specification describes a set of [resources](resource.html)
and several different frameworks for exchanging resources between different systems.
Because of its general nature and wide applicability, the rules made in this
specification are fairly loose. As a consequence, this specification
allows that different applications might not be able to interoperate because of
how they use optional features. Applications claiming
conformance to this specification make the claim in respect of a specific
exchange framework, and in regard to specific details about their usage of
those frameworks and resource contents.

Applications claim conformance to one (or more) of the following exchange
frameworks:

- "RESTful FHIR": the [RESTful API](http.html)
- "FHIR messaging": [Message based exchange](messaging.html)
- "FHIR documents": [Document based exchange](documents.html)

To provide details about specific usage of the frameworks and resource
contents, FHIR provides a [conformance layer](profiling.html) that implementers,
national/regional programs, and other profiling organizations such as IHE, can use to provide a computable statement about
how the resources and their exchange paradigms are used to solve particular use cases.
The conformance layer itself is implemented using the following key resources:

|  |  |
| --- | --- |
| [Value Set](valueset.html) | Defines a set of coded values (see "[Using Codes](terminologies.html)" for more details) |
| [StructureDefinition](structuredefinition.html) | Makes rules about how a resource (or type) and its data elements are used in a particular context, including defining how extensions are used. A structure definition references value sets for the coded elements in a resource |
| [CapabilityStatement](capabilitystatement.html) | A statement of the kinds of resources and operations provided and/or consumed by an application. The Capability Statement references profiles to describe specific use of resources by the application |
| [Implementation Guide](implementationguide.html) | A single coherent collection of capability statements, profiles, extensions, value sets, and documentation describing a set of interoperable applications |

The specification also [provides a number of tools that can assist with enforcing technical conformance](validation.html)
to this base specification.

FHIR is a *closed* specification. The specification defines what is possible and required for those portions
of an API or exchange framework that wish to declare themselves as FHIR conformant, and that includes exchange
resources that conform to the documented requirements of this specification. Systems may choose to
support capabilities beyond those defined by FHIR (e.g. by adding additional end points/services with other
names), but those portions of their interfaces that extend beyond what FHIR explicitly allows cannot be
considered or described as "FHIR conformant".

Conformance with this specification does not provide any guarantee of patient or data safety.
However, choosing to not conform to this specification carries additional risk in
two ways:

- FHIR has been subject to a level of review and vetting unlikely to be received by any non-conformant variation; variations may result in introduction of undetected risks
- FHIR-like solutions (based on FHIR, but not conformant) may set expectations by trading partners which are not met due to the non-conformance of the system and these un-met expectations may also result in risk

Systems can only claim FHIR Conformance for functionality described in the applicable [CapabilityStatement](capabilitystatement.html).

### 2.1.0.1 Conformance Language

This specification uses the conformance verbs SHALL, SHOULD, and MAY as defined in RFC 2119. Unlike RFC 2119, however, this specification allows that different applications might not be able to interoperate because of how they use optional features. In particular:

1. SHALL: an absolute requirement for all implementations
2. SHALL NOT: an absolute prohibition against inclusion for all implementations
3. SHOULD/SHOULD NOT: A best practice or recommendation to be considered by implementers within the context of their particular implementation; there may be valid reasons to ignore an item, but the full implications must be understood and carefully weighed before choosing a different course
4. MAY: This is truly optional language for an implementation; can be included or omitted as the implementer decides with no implications

### 2.1.0.2 Base Conformance Rules

The contents of a resource and the formats used to represent resources SHALL
conform to the rules described in this specification, as defined in the
narrative of the specification, and as controlled by the conformance
properties defined below.

Data elements defined in resources and data types have 3 properties that are
directly related to conformance: Cardinality, Is-Modifier, and MustSupport.
These interact to place conformance requirements on implementations.

### 2.1.0.3 Cardinality

All attributes defined in FHIR have cardinality as part of their definition - a minimum number
of required appearances and a maximum number. These numbers specify the number of times
the attribute may appear in any instance of the resource type. This specification
only defines the following cardinalities: 0..1, 0..\*, 1..1, and 1..\*. Profiles
that describe specific use cases may use other values for cardinality within the limits
of the cardinality defined by the base resource.

Note that when present, elements cannot be empty - they SHALL have a value attribute,
child elements, or extensions. This means that setting an element to a minimum cardinality
of 1 does not ensure that valid data will be present; specific FHIRPath constraints are required
to ensure that the required data will be present.

In this specification, very few elements have a minimum cardinality of 1.
Resources are used in many contexts, often quite removed from their primary
use case, and sometimes even basic information is quite incomplete. For this reason,
the only elements that have a minimum cardinality of 1 are those where they
are necessary to any understanding of the resource or element that contains them.
The minimum cardinalities should not be taken as a guide to what elements
are expected to be present in any particular use of the resource, including their normal/primary usage purpose.
In some cases, this specification publishes additional profiles that define which elements are required in
particular situations. Similar profiles are published by jurisdictions, vendors, profiling organizations, or projects.

For elements that have cardinality > 1, the order in which they appear may have meaning.
Unless the element definition (either in this specification or the extension) defines a meaning
to the order explicitly (using [ElementDefinition.orderMeaning](elementdefinition.html)),
the meaning of the order is not defined, and implementations are allowed to reorder the elements.
Note that it is not possible to define a meaning for the order of the elements in
a [profile](profiling.html) using a [StructureDefinition](structuredefinition.html).
When there is no definition of the meaning of the order, implementations that need to choose a
single element from a list of elements for some use SHALL do so based on the semantics
of the content of the element that repeats. Profiles and Implementation guides may often make
rules about this selection process.

Clients should not depend on servers maintaining ordering of elements, unless the retrieved
resource conforms to a profile which mandates maintenance of ordering. If a server cannot
maintain ordering, it must strip off known profile tags which require maintenance of
ordering, and strip off unknown profiles (since they might require maintenance of ordering).

### 2.1.0.4 Is-modifier

Is-Modifier is a boolean property that is assigned when an element is defined, either as part of
the base resource contents in this specification, or when [extensions are defined](structuredefinition.html).

An element is a modifier if and only if it cannot be safely ignored because its value, or its [meaning if missing](elementdefinition.html#missing), may
cause the interpretation of the containing element or one of its descendants to no longer conform to the stated
definition for the element. Typical examples of elements that are labeled "Is-Modifier" are elements such as
"status", "active", "refuted", or "certainty" that invert or negate the meaning of the resource (or element)
that contains them.

Modifier is not an indication of the degree of importance for a particular piece of information or whether
the element ought to be ignored when the resource is used for common use-cases. It is expected that if you
ignore an element you may miss an important piece of computable meaning.

For example, consider Observation:

- `Observation.status` allows the `entered-in-error` code, which indicates
  that no actual Observation occurred at all. The definition of Observation indicates that it is a measurement that has
  been made - and doesn't allow for the possibility of a measurement that wasn't made. As a result, if the status
  element were ignored and an Observation were interpreted at face value based on its definition, a system or user
  would infer that an Observation had occurred, which would be false
- If an application ignores the `Observation.subject` element, it wouldn't know who or what was observed, which
  would make the remaining information largely useless for most usage.
  However, any system that ignores the subject would not have a false understanding of the Observation as it's
  defined. The system would understand what type of observation was made, when and what was found, just not who it was about
- Even something as critical as `Observation.code` is not a modifier element. While the Observation would have
  little utility without the code, the understanding when ignoring the element that “some” Observation had been
  made on the specified subject at the specified date and time would still be true when the element was
  reintroduced. The only exception would be if a value expressed in the Observation.code element could
  somehow convey that the Observation had not occurred or otherwise cause the instance to diverge from
  the defined meaning of Observation when ignoring the element

The definition of `is-modifier` has a corollary: any element that meets the requirement that it could
cause the interpretation of the containing element or its descendants to diverge from their definition
SHALL explicitly declare how such divergence could occur and must be marked as a modifier element.
Any element not marked `is-modifier` and without that explanation SHALL NOT be used by an implementer in such a
manner as to make the element behave as a modifier. For example, using a special "name" on a patient
to indicate that the subject isn’t a real patient, but is instead an artificial structure used for
non-patient tests would be non-conformant with FHIR because Patient.name is not a modifier element

Whether an element is a modifier cannot be changed when element usage is described in a
constraining [Structure Definition](structuredefinition.html).
When an element is labeled as Is-Modifier, the documentation must be clear about why
it is a modifier.

A typical example of a modifier element is one that negates the element that contains it. For
instance, in the following fragment of a resource definition:

| [Name](formats.html#table "The logical name of the element") | [Flags](formats.html#table "Information about the use of the element") | [Card.](formats.html#table "Minimum and Maximum # of times the element can appear in the instance") | [Type](formats.html#table "Reference to the type of the element") | [Description & Constraints](formats.html#table "Additional information about the element")[doco](formats.html#table "Legend for this format") |
| --- | --- | --- | --- | --- |
| .. [AllergyIntolerance](allergyintolerance-definitions.html#AllergyIntolerance "AllergyIntolerance : Risk of harmful or undesirable, physiological response which is unique to an individual and associated with exposure to a substance.") |  |  | [DomainResource](domainresource.html) | Allergy or Intolerance (generally: Risk of Adverse reaction to a substance) |
| ... [onset](allergyintolerance-definitions.html#AllergyIntolerance.onset_x_ "AllergyIntolerance.onset : Record of the date and/or time of the onset of the Allergy or Intolerance.") | Σ | 0..1 | [dateTime](datatypes.html#dateTime) | Date(/time) when manifestations showed |
| ... [patient](allergyintolerance-definitions.html#AllergyIntolerance.patient "AllergyIntolerance.patient : The patient who has the allergy or intolerance.") | Σ | 1..1 | [Reference](references.html)([Patient](patient.html)) | Who the sensitivity is for |
| ... [verificationStatus](allergyintolerance-definitions.html#AllergyIntolerance.verificationStatus "AllergyIntolerance.verificationStatus : Assertion about certainty associated with the propensity, or potential risk, of a reaction to the identified Substance.") | ?! Σ | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | unconfirmed | confirmed | refuted | entered-in-error [AllergyIntoleranceVerificationStatus](valueset-allergyintolerance-verification.html "Assertion about certainty associated with a propensity, or potential risk, of a reaction to the identified Substance") ([Required](terminologies.html#required "To be conformant, codes in this element SHALL be from the specified value set")) |
| ... [criticality](allergyintolerance-definitions.html#AllergyIntolerance.criticality "AllergyIntolerance.criticality : Estimate of the potential clinical harm, or seriousness, of the reaction to the identified Substance.") | Σ | 0..1 | [code](datatypes.html#code) | CRITL | CRITH | CRITU [AllergyIntoleranceCriticality](valueset-allergy-intolerance-criticality.html "Estimate of the potential clinical harm, or seriousness, of a reaction to an identified Substance") ([Required](terminologies.html#required "To be conformant, codes in this element SHALL be from the specified value set")) |

The definition of an AllergyIntolerance is that it contains information about "Risk of harmful or undesirable,
physiological response which is unique to an individual and associated with exposure to a substance".
If the value of the 'verificationStatus' element is set to `entered-in-error`, the
entire resource does not actually contain valid information about any risk of exposure, and
it is not safe for applications to ignore this element. As a consequence, it is labeled as 'is modifier = true'. In this tabular representation of the resource,
this shows as the flag '?!'. The [JSON](json.html) and [XML](xml.html) representations
of a resource definition have their own representation of 'is modifier = true' status, and
it is defined directly in a [ElementDefinition](elementdefinition-definitions.html#ElementDefinition.isModifier).

If a narrative summary is present, and the status is `generated`, Is-Modifier elements SHALL be represented in the narrative summary of the resource.
If Narrative is present with some other status Is-modifier elements SHOULD be represented.

If the value of a modifier element is not explicit in the instance, or known by the context,
the resource might not be able to be safely understood. Wherever possible, elements labeled
"Is-Modifier = true" also have a minimum cardinality of 1, in order to introduce certainty in
their handling. However, sometimes this is not possible - much legacy data is not well
described. Implementations producing resources SHOULD ensure that appropriate values for
isModifier elements are provided at all times.

Implementations processing the data in resources SHALL understand the impact of the element when using the data.
Implementations are not required to "support" the element in any meaningful way - they
may achieve this understanding by rejecting instances that contain values outside those they support (for instance,
an application may refuse to accept observations with a reliability other than "ok"). Alternatively,
implementations may be able to be sure that, due to their implementation environment, such values
will never occur. However applications SHOULD always check the value irrespective of this.

Note that processing the data of a resource typically means
copying or filtering data out of a resource for use in another
context (display to a human, decision support, exchange in another
format where not all information is included or storing it for this kind of use).
Servers and background processes that simply move whole resources around unchanged
are not "processing the data of the resource", and therefore these applications
are not required to check Is-Modifier elements.

Every element in the base resource has a value of "true" or "false" for the Is-Modifier flag.
The value of the flag cannot be changed by profiles on the resource, in either direction.
When a StructureDefinition defines an extension, it labels the extension with the Is-Modifier flag,
and this cannot be changed in other profiles. Note that extensions that have is-Modifier = true
are represented differently in resource instances ("modifierExtension" instead of "extension"),
and there are [additional rules about how they are handled](extensibility.html#modifierExtension).

Most `status` elements are marked as modifiers because of the presence of the `entered-in-error` status.
Other modifiers are defined:

- [Address.use](datatypes-definitions.html#Address.use)
- [ContactPoint.use](datatypes-definitions.html#ContactPoint.use)
- [HumanName.use](datatypes-definitions.html#HumanName.use)
- [Identifier.use](datatypes-definitions.html#Identifier.use)
- [Quantity.comparator](datatypes-definitions.html#Quantity.comparator)
- [BackboneElement.modifierExtension](backboneelement-definitions.html#BackboneElement.modifierExtension)
- [DomainResource.modifierExtension](domainresource-definitions.html#DomainResource.modifierExtension)
- [Resource.implicitRules](resource-definitions.html#Resource.implicitRules)
- [ActivityDefinition.doNotPerform](activitydefinition-definitions.html#ActivityDefinition.doNotPerform)
- [AdverseEvent.actuality](adverseevent-definitions.html#AdverseEvent.actuality)
- [AllergyIntolerance.clinicalStatus](allergyintolerance-definitions.html#AllergyIntolerance.clinicalStatus)
- [AllergyIntolerance.verificationStatus](allergyintolerance-definitions.html#AllergyIntolerance.verificationStatus)
- [AppointmentResponse.participantStatus](appointmentresponse-definitions.html#AppointmentResponse.participantStatus)
- [Basic.code](basic-definitions.html#Basic.code)
- [BodyStructure.active](bodystructure-definitions.html#BodyStructure.active)
- [CarePlan.intent](careplan-definitions.html#CarePlan.intent)
- [CarePlan.activity.detail.doNotPerform](careplan-definitions.html#CarePlan.activity.detail.doNotPerform)
- [CommunicationRequest.doNotPerform](communicationrequest-definitions.html#CommunicationRequest.doNotPerform)
- [ConceptMap.group.element.target.equivalence](conceptmap-definitions.html#ConceptMap.group.element.target.equivalence)
- [Condition.clinicalStatus](condition-definitions.html#Condition.clinicalStatus)
- [Condition.verificationStatus](condition-definitions.html#Condition.verificationStatus)
- [Consent.scope](consent-definitions.html#Consent.scope)
- [Contract.term.action.doNotPerform](contract-definitions.html#Contract.term.action.doNotPerform)
- [DeviceRequest.intent](devicerequest-definitions.html#DeviceRequest.intent)
- [Goal.lifecycleStatus](goal-definitions.html#Goal.lifecycleStatus)
- [HealthcareService.active](healthcareservice-definitions.html#HealthcareService.active)
- [Immunization.isSubpotent](immunization-definitions.html#Immunization.isSubpotent)
- [ImmunizationRecommendation.recommendation.forecastStatus](immunizationrecommendation-definitions.html#ImmunizationRecommendation.recommendation.forecastStatus)
- [List.mode](list-definitions.html#List.mode)
- [List.entry.deleted](list-definitions.html#List.entry.deleted)
- [MeasureReport.improvementNotation](measurereport-definitions.html#MeasureReport.improvementNotation)
- [MedicationRequest.intent](medicationrequest-definitions.html#MedicationRequest.intent)
- [MedicationRequest.doNotPerform](medicationrequest-definitions.html#MedicationRequest.doNotPerform)
- [MedicinalProductIngredient.specifiedSubstance.strength.presentationLowLimit](medicinalproductingredient-definitions.html#MedicinalProductIngredient.specifiedSubstance.strength.presentationLowLimit)
- [MedicinalProductIngredient.specifiedSubstance.strength.concentrationLowLimit](medicinalproductingredient-definitions.html#MedicinalProductIngredient.specifiedSubstance.strength.concentrationLowLimit)
- [NutritionOrder.intent](nutritionorder-definitions.html#NutritionOrder.intent)
- [Organization.active](organization-definitions.html#Organization.active)
- [Patient.active](patient-definitions.html#Patient.active)
- [Patient.deceased[x]](patient-definitions.html#Patient.deceased[x])
- [Patient.link](patient-definitions.html#Patient.link)
- [Person.active](person-definitions.html#Person.active)
- [Questionnaire.item.enableWhen](questionnaire-definitions.html#Questionnaire.item.enableWhen)
- [RelatedPerson.active](relatedperson-definitions.html#RelatedPerson.active)
- [RequestGroup.intent](requestgroup-definitions.html#RequestGroup.intent)
- [Schedule.active](schedule-definitions.html#Schedule.active)
- [ServiceRequest.intent](servicerequest-definitions.html#ServiceRequest.intent)
- [ServiceRequest.doNotPerform](servicerequest-definitions.html#ServiceRequest.doNotPerform)

### 2.1.0.5 MustSupport

Labeling an element MustSupport means that implementations that produce or consume resources SHALL
provide "support" for the element in some meaningful way. Because the base FHIR specification is intended
to be independent of any particular implementation context, no elements are flagged as `mustSupport`=true as
part of the base specification. This flag is intended for use in profiles that have a defined implementation context.

For this reason, the specification itself never labels any elements as MustSupport.
This is done in [StructureDefinitions](profiling.html#mustsupport), where the profile
labels an element as mustSupport=true. When a profile does this, it SHALL also make clear
exactly what kind of "support" is required, as this could involve expectations around what
a system must store, display, allow data capture of, include in decision logic, pass on to
other data consumers, etc.

Note that an element that has the property IsModifier is not necessarily a "key" element (e.g. one of
the important elements to make use of the resource), nor is it automatically mustSupport - however both
of these things are more likely to be true for IsModifier elements than for other elements.

### 2.1.0.6 Constraints

All elements may have constraints attached to them (also known as 'invariants').
Constraints defined on an element have the following properties:

|  |  |
| --- | --- |
| **Key** | Identifies the constraint uniquely amongst all the constraints in the context - typically, this is used to refer to the constraint in an error message |
| **Requirements** | An explanation of why the constraint has been applied - what harmful conditions are being avoided |
| **Severity** | The severity of the invariant - see below |
| **Human Description** | A human description of the rule intended to be shown as the explanation for a message when the constraint is not met |
| **Expression** | A [FHIRPath](fhirpath.html) expression that must evaluate to true when run on the element |
| **XPath** | An XPath expression that must evaluate to true when run on the element in the XML representation |

Many constraints are defined in the base specification. In addition, additional
constraints may be defined in [profiles](profiling.html) that apply
to resources. Systems are not required to evaluate the constraints, just as they
are not required to check for conformance, or schema validity. However, systems
SHOULD always ensure that all resources are valid against all applicable constraints.

Constraints have a severity level:

|  |  |
| --- | --- |
| **Error (rule)** | A rule that all resources must conform to. Validators should report it as an error if the rule is violated, and applications processing the content can reject it as an invalid resource |
| **Warning** | Report this as a warning that there may be a problem with the resource, but it is considered valid and can be processed normally |
| **Guideline** | A warning marked with an extension ([http://hl7.org/fhir/StructureDefinition/elementdefinition-bestpractice](extension-elementdefinition-bestpractice.html)) that indicates that it should be a treated as an error if the implementation context asks a validator to enforce best practice rules. See [Best Practices](best-practices.html) for a full list |

Elements can also be explicitly associated with constraints defined elsewhere. This is
a notification to implementers that the element is affected by the constraint. It has no meaning when the constraints are evaluated.

[Profiles](profiling.html) may define additional constraints that
apply to an element, but they cannot alter or remove constraints that are already
applied.

### 2.1.0.7 Other Metadata

In addition to the conformance metadata, each element has other metadata properties defined in the [ElementDefinition](elementdefinition.html):

- **isSummary** - How the element behaves in [Summary Searches](search.html#summary)
- **meaningWhenMissing** - What it [means when an element is missing](elementdefinition.html#missing)
- **maxLength** - How long the representation of the primitive value is allowed to be (not including XML or JSON escaping)

### 2.1.0.8 Examples and Reference Implementations

This specification includes many examples. While every effort has been made to ensure that the examples
are fully conformant to the specification, if the examples disagree with the specification, the specification
is considered correct and normative, not the examples. This same rule applies to the reference implementations.

The examples reflected in this specification do \*not\* represent actual people. Any resemblance to real people - alive
or dead - is entirely coincidental. In some cases, examples may be drawn from real clinical data.
However, if this has occurred, the content has been scrubbed to remove any identifying information.

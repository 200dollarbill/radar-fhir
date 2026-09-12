---
id: references
title: Resource References
source_url: https://hl7.org/fhir/R4/references.html
group: fhir-r4
fhir_version: R4
fetched_at: '2026-09-11T13:22:22Z'
sha256: a68474d0757a519f92814686d7df30c45ea81c81594ffb19bcf70473c713cee8
---
This page is part of the FHIR Specification (v4.0.1: R4 - Mixed [Normative](https://confluence.hl7.org/display/HL7/HL7+Balloting "Normative Standard") and [STU](https://confluence.hl7.org/display/HL7/HL7+Balloting "Standard for Trial-Use")) in it's permanent home (it will always be available at this URL). The current version which supercedes this version is [5.0.0](http://hl7.org/fhir/index.html). For a full list of available versions, see the [Directory of published versions ![](external.png)](http://hl7.org/fhir/directory.html). Page versions: [R5](http://hl7.org/fhir/R5/references.html) [R4B](http://hl7.org/fhir/R4B/references.html) **R4** [R3](http://hl7.org/fhir/STU3/references.html) [R2](http://hl7.org/fhir/DSTU2/references.html)

- [References](#)
- [Detailed Descriptions](references-definitions.html)

## 2.3.0 Resource References

|  |  |  |
| --- | --- | --- |
| [FHIR Infrastructure](http://www.hl7.org/Special/committees/fiwg/index.cfm)  Work Group | [Maturity Level](versions.html#maturity): Normative | [Standards Status](versions.html#std-process): [Normative](versions.html#std-process) |

|  |  |
| --- | --- |
|  | This page has been approved as part of an [ANSI](https://www.ansi.org/)  standard. See the [Infrastructure](ansi-infrastructure.html) Package for further details. |

Many of the defined elements in a resource are references to other resources. Using these
references, the resources combine to build a web of information about healthcare.

References are always defined and represented in one direction - from one resource (source) to another (target).
The corresponding reverse relationship from the target to the source exists in a logical sense, but is
not typically represented explicitly in the target resource. For external references, navigating these reverse relationships requires some
external infrastructure to track the relationship between resources (the [REST API](http.html) provides one such
infrastructure by providing the ability to [search](http.html#search) the reverse relationship by naming
search parameters for the references and by providing support for [reverse includes](search.html#revinclude)).

Because resources are processed independently, relationships are not considered to be transitive.
For example, if a [Procedure](procedure.html) resource references a [Patient](patient.html) as its subject, and has a
[Procedure](procedure.html) resource as its reason, there is no automatic rule or implication that the condition
has the same patient for its subject. Instead, the subject of the condition must be established
directly in the Condition resource itself. Another way to state this is that the context of the
subject is not "inherited", nor does it "conduct" along the relationship to condition.
The only exception to this is the case of contained resources (see below). Note that in
practice, the relationships need to describe a logical and coherent record, and in the
case of the Condition and Procedure described here, they would usually be required to have
the same patient for their subjects. Profiles and/or implementation guides may make rules
about this (also see [GraphDefinition](graphdefinition.html)).

This specification describes the use of references to other resources that have the same FHIR version as the source of the reference.
Expected behavior for references across FHIR versions is presently undefined.

References are made to resource based on their identity; there are [several different identities](resource.html#id) to refer to.

Resources contain two types of references to other resources:

- **Resource references** - general references between resources
- **Canonical references** - references to resources by their canonical URL (see [below](#canonical))

For canonical references, see below. The general references are handled by the `Reference` type.
which contains at least one of a `reference` (literal reference),
an `identifier` (logical reference), and a `display` (text description of target).
In addition, it may contain a target `type`.

- [Structure](#tabs-Reference-struc)
- [UML](#tabs-Reference-uml)
- [XML](#tabs-Reference-xml)
- [JSON](#tabs-Reference-json)
- [Turtle](#tabs-Reference-ttl)
- [R3 Diff](#tabs-Reference-diff)
- [All](#tabs-Reference-all)

**Structure**

| [Name](formats.html#table "The logical name of the element") | [Flags](formats.html#table "Information about the use of the element") | [Card.](formats.html#table "Minimum and Maximum # of times the the element can appear in the instance") | [Type](formats.html#table "Reference to the type of the element") | [Description & Constraints](formats.html#table "Additional information about the element")[doco](formats.html#table "Legend for this format") |
| --- | --- | --- | --- | --- |
| .. [Reference](references-definitions.html#Reference "Reference : A reference from one resource to another.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants")[N](versions.html#std-process "Standards Status = Normative") |  | [Element](element.html) | A reference from one resource to another + Rule: SHALL have a contained resource if a local reference is provided Elements defined in Ancestors: [id](element.html#Element "Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces."), [extension](element.html#Element "May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.") |
| ... [reference](references-definitions.html#Reference.reference "Reference.reference : A reference to a location at which the other resource is found. The reference may be a relative reference, in which case it is relative to the service base URL, or an absolute URL that resolves to the location where the resource is found. The reference may be version specific or not. If the reference is not to a FHIR RESTful server, then it should be assumed to be version specific. Internal fragment references (start with '#') refer to contained resources.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..1 | [string](datatypes.html#string) | Literal reference, Relative, internal or absolute URL |
| ... [type](references-definitions.html#Reference.type "Reference.type : The expected type of the target of the reference. If both Reference.type and Reference.reference are populated and Reference.reference is a FHIR URL, both SHALL be consistent.  The type is the Canonical URL of Resource Definition that is the type this reference refers to. References are URLs that are relative to http://hl7.org/fhir/StructureDefinition/ e.g. \"Patient\" is a reference to http://hl7.org/fhir/StructureDefinition/Patient. Absolute URLs are only allowed for logical models (and can only be used in references in logical models, not resources).") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [uri](datatypes.html#uri) | Type the reference refers to (e.g. "Patient") [ResourceType](valueset-resource-types.html "Aa resource (or, for logical models, the URI of the logical model).") ([Extensible](terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept (based on human review), alternate codings (or, data type allowing, text) may be included instead.")) |
| ... [identifier](references-definitions.html#Reference.identifier "Reference.identifier : An identifier for the target resource. This is used when there is no way to reference the other resource directly, either because the entity it represents is not available through a FHIR server, or because there is no way for the author of the resource to convert a known identifier to an actual location. There is no requirement that a Reference.identifier point to something that is actually exposed as a FHIR instance, but it SHALL point to a business concept that would be expected to be exposed as a FHIR instance, and that instance would need to be of a FHIR resource type allowed by the reference.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [Identifier](datatypes.html#Identifier) | Logical reference, when literal reference is not known |
| ... [display](references-definitions.html#Reference.display "Reference.display : Plain text narrative that identifies the resource in addition to the resource reference.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | Text alternative for the resource |
| [doco Documentation for this format](formats.html#table "Legend for this format") | | | | |

**UML Diagram** ([Legend](formats.html#uml))

**XML Template**

```

<[name] xmlns="http://hl7.org/fhir">
 <!-- from Element: extension -->
 <reference value="[string]"/><!-- ![??](lock.png) 0..1 Literal reference, Relative, internal or absolute URL -->
 <type value="[uri]"/><!-- 0..1 Type the reference refers to (e.g. "Patient") -->
 <identifier><!-- 0..1 Identifier Logical reference, when literal reference is not known --></identifier>
 <display value="[string]"/><!-- 0..1 Text alternative for the resource -->
</[name]>
```

**JSON Template**

```

{![doco](help.png)
  // from Element: extension
  "reference" : "<string>", // C? Literal reference, Relative, internal or absolute URL
  "type" : "<uri>", // Type the reference refers to (e.g. "Patient")
  "identifier" : { Identifier }, // Logical reference, when literal reference is not known
  "display" : "<string>" // Text alternative for the resource
}
```

**Turtle Template**

```

@prefix fhir: <http://hl7.org/fhir/> .

[
 # from Element: Element.extension
  fhir:Reference.reference [ string ]; # 0..1 Literal reference, Relative, internal or absolute URL
  fhir:Reference.type [ uri ]; # 0..1 Type the reference refers to (e.g. "Patient")
  fhir:Reference.identifier [ Identifier ]; # 0..1 Logical reference, when literal reference is not known
  fhir:Reference.display [ string ]; # 0..1 Text alternative for the resource
]
```

**Changes since Release 3**

|  |  |
| --- | --- |
| [Reference](references.html#Reference) |  |
| Reference.type | - Added Element |

See the [Full Difference](diff.html) for further information

**Structure**

| [Name](formats.html#table "The logical name of the element") | [Flags](formats.html#table "Information about the use of the element") | [Card.](formats.html#table "Minimum and Maximum # of times the the element can appear in the instance") | [Type](formats.html#table "Reference to the type of the element") | [Description & Constraints](formats.html#table "Additional information about the element")[doco](formats.html#table "Legend for this format") |
| --- | --- | --- | --- | --- |
| .. [Reference](references-definitions.html#Reference "Reference : A reference from one resource to another.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants")[N](versions.html#std-process "Standards Status = Normative") |  | [Element](element.html) | A reference from one resource to another + Rule: SHALL have a contained resource if a local reference is provided Elements defined in Ancestors: [id](element.html#Element "Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces."), [extension](element.html#Element "May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.") |
| ... [reference](references-definitions.html#Reference.reference "Reference.reference : A reference to a location at which the other resource is found. The reference may be a relative reference, in which case it is relative to the service base URL, or an absolute URL that resolves to the location where the resource is found. The reference may be version specific or not. If the reference is not to a FHIR RESTful server, then it should be assumed to be version specific. Internal fragment references (start with '#') refer to contained resources.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..1 | [string](datatypes.html#string) | Literal reference, Relative, internal or absolute URL |
| ... [type](references-definitions.html#Reference.type "Reference.type : The expected type of the target of the reference. If both Reference.type and Reference.reference are populated and Reference.reference is a FHIR URL, both SHALL be consistent.  The type is the Canonical URL of Resource Definition that is the type this reference refers to. References are URLs that are relative to http://hl7.org/fhir/StructureDefinition/ e.g. \"Patient\" is a reference to http://hl7.org/fhir/StructureDefinition/Patient. Absolute URLs are only allowed for logical models (and can only be used in references in logical models, not resources).") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [uri](datatypes.html#uri) | Type the reference refers to (e.g. "Patient") [ResourceType](valueset-resource-types.html "Aa resource (or, for logical models, the URI of the logical model).") ([Extensible](terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept (based on human review), alternate codings (or, data type allowing, text) may be included instead.")) |
| ... [identifier](references-definitions.html#Reference.identifier "Reference.identifier : An identifier for the target resource. This is used when there is no way to reference the other resource directly, either because the entity it represents is not available through a FHIR server, or because there is no way for the author of the resource to convert a known identifier to an actual location. There is no requirement that a Reference.identifier point to something that is actually exposed as a FHIR instance, but it SHALL point to a business concept that would be expected to be exposed as a FHIR instance, and that instance would need to be of a FHIR resource type allowed by the reference.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [Identifier](datatypes.html#Identifier) | Logical reference, when literal reference is not known |
| ... [display](references-definitions.html#Reference.display "Reference.display : Plain text narrative that identifies the resource in addition to the resource reference.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | Text alternative for the resource |
| [doco Documentation for this format](formats.html#table "Legend for this format") | | | | |

**UML Diagram** ([Legend](formats.html#uml))

**XML Template**

```

<[name] xmlns="http://hl7.org/fhir">
 <!-- from Element: extension -->
 <reference value="[string]"/><!-- ![??](lock.png) 0..1 Literal reference, Relative, internal or absolute URL -->
 <type value="[uri]"/><!-- 0..1 Type the reference refers to (e.g. "Patient") -->
 <identifier><!-- 0..1 Identifier Logical reference, when literal reference is not known --></identifier>
 <display value="[string]"/><!-- 0..1 Text alternative for the resource -->
</[name]>
```

**JSON Template**

```

{![doco](help.png)
  // from Element: extension
  "reference" : "<string>", // C? Literal reference, Relative, internal or absolute URL
  "type" : "<uri>", // Type the reference refers to (e.g. "Patient")
  "identifier" : { Identifier }, // Logical reference, when literal reference is not known
  "display" : "<string>" // Text alternative for the resource
}
```

**Turtle Template**

```

@prefix fhir: <http://hl7.org/fhir/> .

[
 # from Element: Element.extension
  fhir:Reference.reference [ string ]; # 0..1 Literal reference, Relative, internal or absolute URL
  fhir:Reference.type [ uri ]; # 0..1 Type the reference refers to (e.g. "Patient")
  fhir:Reference.identifier [ Identifier ]; # 0..1 Logical reference, when literal reference is not known
  fhir:Reference.display [ string ]; # 0..1 Text alternative for the resource
]
```

**Changes since Release 3**

|  |  |
| --- | --- |
| [Reference](references.html#Reference) |  |
| Reference.type | - Added Element |

See the [Full Difference](diff.html) for further information

**Constraints**

At least one of `reference`, `identifier` and `display` SHALL be present (unless an extension is provided).

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **id** | **Level** | **Location** | **Description** | **[Expression](fhirpath.html)** |
| **ref-1** | [Rule](conformance-rules.html#rule) | (base) | SHALL have a contained resource if a local reference is provided | reference.startsWith('#').not() or (reference.substring(1).trace('url') in %rootResource.contained.id.trace('ids')) |

### 2.3.0.1 Target Type

In resources, a `Reference` always point to another resource, which has
a fixed and known type. If appropriate, this type can be specified in the reference
itself. In principle, the type of the target reference can be determined by resolving
the reference (using the approaches described below), and examining the content
returned to determine the type; for this reason, specifying the type is almost always
duplication of information. However, resolving references may be a very slow
operation, or impossible in practice due to various practical concerns. For this
reason, the reference may indicate directly the target resource type:

```

 "subject": {
   "reference" : "http://someserver/some-path",
   "type" : "Patient"
 }
```

When the type is provided directly, it SHALL agree with the type determined by resolving
the resource.

Note that in practice, it is often not necessary to know the type of the target resource is,
unless it's going to be resolved anyway, so in many cases, specifying the type of the
target resource is unnecessary.

In order to support [Logical Models](structuredefinition.html#logical),
the `type` element has the type of "uri". Whenever `type`
appears in resources, the uri is represented relative to the base URI
`http://hl7.org/fhir/StructureDefinition/`. For resources, then, the
value is simply a code that is the type of resource - e.g. "Patient".

### 2.3.0.2 Literal References

The `reference` is the key element - resources are identified and addressed by their URL. It
contains a URL that is either

- an absolute URL
- a relative URL, which is relative to the [Service Base URL](http.html#root), or, if processing a resource from a bundle,
  which is relative to the base URL implied by the `Bundle.entry.fullUrl` (see [Resolving References in Bundles](bundle.html#references))
- an internal fragment reference (see "Contained Resources" below)

Notes:

- Using absolute URLs provides a stable, scalable approach suitable for a cloud/web context, while using relative/logical references provides a
  flexible approach suitable for use when trading across closed ecosystem boundaries. (see ["Managing Resource Identity"](managing.html) for further discussion)
- Absolute URLs do not need to point to a [FHIR RESTful server](http.html), though this is the preferred approach.
  Whether or not the reference is to a FHIR RESTful server, the reference SHALL point to a Resource as defined by this specification.
    
  Note that This regex is true if the reference to a resource is consistent with a FHIR API:

  ```
  
     ((http|https):\/\/([A-Za-z0-9\-\\\.\:\%\$]*\/)+)?(Account|ActivityDefinition|AdverseEvent|AllergyIntolerance|Appointment|AppointmentResponse|AuditEvent|Basic|Binary|BiologicallyDerivedProduct|BodyStructure|Bundle|CapabilityStatement|CarePlan|CareTeam|CatalogEntry|ChargeItem|ChargeItemDefinition|Claim|ClaimResponse|ClinicalImpression|CodeSystem|Communication|CommunicationRequest|CompartmentDefinition|Composition|ConceptMap|Condition|Consent|Contract|Coverage|CoverageEligibilityRequest|CoverageEligibilityResponse|DetectedIssue|Device|DeviceDefinition|DeviceMetric|DeviceRequest|DeviceUseStatement|DiagnosticReport|DocumentManifest|DocumentReference|EffectEvidenceSynthesis|Encounter|Endpoint|EnrollmentRequest|EnrollmentResponse|EpisodeOfCare|EventDefinition|Evidence|EvidenceVariable|ExampleScenario|ExplanationOfBenefit|FamilyMemberHistory|Flag|Goal|GraphDefinition|Group|GuidanceResponse|HealthcareService|ImagingStudy|Immunization|ImmunizationEvaluation|ImmunizationRecommendation|ImplementationGuide|InsurancePlan|Invoice|Library|Linkage|List|Location|Measure|MeasureReport|Media|Medication|MedicationAdministration|MedicationDispense|MedicationKnowledge|MedicationRequest|MedicationStatement|MedicinalProduct|MedicinalProductAuthorization|MedicinalProductContraindication|MedicinalProductIndication|MedicinalProductIngredient|MedicinalProductInteraction|MedicinalProductManufactured|MedicinalProductPackaged|MedicinalProductPharmaceutical|MedicinalProductUndesirableEffect|MessageDefinition|MessageHeader|MolecularSequence|NamingSystem|NutritionOrder|Observation|ObservationDefinition|OperationDefinition|OperationOutcome|Organization|OrganizationAffiliation|Patient|PaymentNotice|PaymentReconciliation|Person|PlanDefinition|Practitioner|PractitionerRole|Procedure|Provenance|Questionnaire|QuestionnaireResponse|RelatedPerson|RequestGroup|ResearchDefinition|ResearchElementDefinition|ResearchStudy|ResearchSubject|RiskAssessment|RiskEvidenceSynthesis|Schedule|SearchParameter|ServiceRequest|Slot|Specimen|SpecimenDefinition|StructureDefinition|StructureMap|Subscription|Substance|SubstanceNucleicAcid|SubstancePolymer|SubstanceProtein|SubstanceReferenceInformation|SubstanceSourceMaterial|SubstanceSpecification|SupplyDelivery|SupplyRequest|Task|TerminologyCapabilities|TestReport|TestScript|ValueSet|VerificationResult|VisionPrescription)\/[A-Za-z0-9\-\.]{1,64}(\/_history\/[A-Za-z0-9\-\.]{1,64})?
  ```

    
  However, conformance with this regex is no guarantee that the end-point is a FHIR server
- URLs are always considered to be case-sensitive
- The URL may contain a reference to a canonical URL (see below) and applications can use the canonical URL resolution methods they support when resolving references, though the `|[version]` syntax part of the canonical reference is not supported
- References SHALL be a reference to an actual FHIR resource, and SHALL be resolvable (given that access control works, there is no temporary unavailability, etc.). Resolution can be either by retrieval from the URL, or, where applicable by resource type, by treating an absolute reference as a canonical URL ([see below](#canonical)) and looking it up in a local registry/repository

A relative reference to the [Patient](patient.html) "034AB16" in an element named `subject` on a FHIR RESTful server:

```

  <subject>
    <reference value="Patient/034AB16" />
  </subject>
```

An absolute reference to a [Structure Definition](structuredefinition.html) in an element named `profile`:

```

{
  "profile" : {
    "reference" : "http://fhir.hl7.org/svc/StructureDefinition/c8973a22-2b5b-4e76-9c66-00639c99e61b"
  }
}
```

Note that in a bundle during a [transaction](http.html#transaction), reference URLs may actually contain
logical URIs (e.g. OIDs or UUIDSs) that resolve within the transaction. When processing the transaction, the server
replaces the logical URL with what is the correct literal URL at the completion of the transaction.

References can be version specific - that is, a reference may point to a specific version of a resource. e.g.:

```

  <target>
    <reference value="http://example.org/fhir/Observation/1x2/_history/2" />
  </target>
```

This is usually associated with audit trail or provenance information where it is important to
reference a specific version of a record, not the most current information.

### 2.3.0.3 Logical References

In many contexts where FHIR is used, applications building a resource may know an identifier for the target
of the reference, but there is no way for the application to convert this to a literal reference that
directly references an actual resource. This situation may arise for several reasons:

- There is no server exposing any such resource. This is often the case with national identifiers (e.g. US SSN or NPI), and such identifiers are widely used
- The server that exposes the resource is not available to the source application, so it has no way to resolve an identifier to a reference
- The application is not in a RESTful environment - it is creating a message or a document

For further discussion of the use of identifiers on resources, see [Consistent Resource Identification](managing.html#consistency).
In these cases, the source application may provide the identifier as a logical reference to the
entity that the target resource would describe.

A logical reference to the [Patient](patient.html) with an SSN of 000111111:

```

  <patient>
    <identifier>
      <system value="http://hl7.org/fhir/sid/us-ssn" />
      <value value="000111111" />
    </identifier>
  </patient>
```

There is no requirement that a Reference.identifier point to something that is actually exposed or
exists as a FHIR instance (except, of course, that the reference will need to be resolved to a
target resource if any information from it is required in a FHIR context).
The reference SHALL point to a business concept that would be expected to be exposed as a
FHIR instance, and that instance would need to be of a FHIR resource type allowed by the reference
For example, it would not be legitimate to send the identifier for a drug prescription if
the type were Reference(Observation|DiagnosticReport). One of the use-cases for
`Reference.identifier` is the situation where no FHIR representation exists
(where the type is Reference (Any).

When processing a resource, an application
may be able to use the identifier directly, on the grounds that all it needs is the identifier,
or it may be able to resolve the identifier directly. Alternatively, it may be able to use
a server to resolve the logical reference to a literal reference to a resource.

Irrespective of how the resolution occurs, any system processing a logical reference will only be
able to resolve the identifier to a reference if it understands the business context in which the
identifier is used. Sometimes this is global (e.g. a national identifier) but often it is not.

For this reason, none of the useful mechanisms described for working with references (e.g.
[chaining](search.html#chaining), [includes](search.html#include)) are
possible, nor should servers be expected to be able to automatically resolve the reference.
Servers may accept an identifier based reference untouched, resolve it, and/or reject it - see
[CapabilityStatement.rest.resource.referencePolicy](capabilitystatement-definitions.html#CapabilityStatement.rest.resource.referencePolicy).

When both logical and literal references are provided, the literal reference is preferred.
Applications processing the resource are allowed - but not required - to check that the identifier
matches the literal reference, if they understand how to resolve the logical reference.

Applications converting a logical reference to a literal reference may choose to leave the
logical reference present; or may remove it.

### 2.3.0.4 Reference Description

Irrespective of whether a literal and/or logical reference is provided, or neither, the
`display` element may be used to provide a very short description of the
target resource.

```

  <custodian>
    <reference value="Organization/123" />
    <display value="HL7, Inc" />
  </custodian>
```

This text can be used by any application that cannot resolve the reference
to fill out the text portion of a hyperlink referring to the target resource, for instance.
It can also save time fetching a target resource and determining how to convert it to
a very short textual description.

In general, the `display`, if populated, does not have identical content
to the Resource.text of the referenced resource. The purpose is to identify what's
being referenced, not to more fully describe it.

### 2.3.0.5 Canonical URLs

Many resource types have a defined element "url" which is the canonical URL that always identifies the
resource across all contexts of use. Typically, [terminology](terminology-module.html),
[conformance](conformance-module.html) or [knowledge](clinicalreasoning-module.html)
resources have canonical URLs. The canonical URL **is the preferred way to reference a resource instance**
for the resource types on which it is defined. See [Canonical Resource
Identity](resource.html#canonical) for further information.

References to canonical URLs use the [`canonical`](datatypes.html#canonical) type to refer to
the `url` element on the conformance/knowledge resources (which has the type [uri](datatypes.html#uri)):

```

<valueSet value="http://hl7.org/fhir/ValueSet/my-valueset"/>
```

References of type `canonical` may include a version, in order be precise about which version of the
resource is being referred to. To do this, append the version to the reference with a '|' like this:

```

<valueSet value="http://hl7.org/fhir/ValueSet/my-valueset|0.8"/>
```

This is a version specific reference to a value set. Note that this refers to the `ValueSet.version`
not the `ValueSet.meta.versionId`. Searching for this on a FHIR server would look like this:

```

GET fhir/ValueSet?url=http://hl7.org/fhir/ValueSet/my-valueset&version=0.8
```

Note that if a References to a canonical URL does not have a version, and the server finds multiple
versions for the value set, the system using the reference should pick the latest version
of the target resource and use that. Servers SHOULD support version specific searching for canonical
URLs by automatically detecting the presence of a |[version] and performing the appropriate
search. Additional notes about searching on versioned references to canonical URLs:

- Search only regards the latest version for each different logical id
- If there is no match (either because .version is empty or is different), the instance will not be matched, and will not appear in the result bundle
- This search only works for specific data elements of type of uri that act as canonical URL's (see list below)

Systems resolving references to canonical URLs SHOULD first try to resolve the reference using
the canonical reference (e.g. search on a known registry of terminology, conformance, or knowledge
resources as appropriate), and then fall back to direct resolution using the URL as
a literal reference if a local version of the canonical resource cannot be found.
This approach is safe because the approaches must refer to the same
artifact, though implementations will need to make appropriate arrangements regarding
the version and/or currency of their local copy of the artifact.

The following resources have canonical URLs and are allowed to be the target of a references to a canonical URLs:

- [ActivityDefinition](activitydefinition.html)
- [CapabilityStatement](capabilitystatement.html)
- [ChargeItemDefinition](chargeitemdefinition.html)
- [CodeSystem](codesystem.html)
- [CompartmentDefinition](compartmentdefinition.html)
- [ConceptMap](conceptmap.html)
- [EffectEvidenceSynthesis](effectevidencesynthesis.html)
- [EventDefinition](eventdefinition.html)
- [Evidence](evidence.html)
- [EvidenceVariable](evidencevariable.html)
- [ExampleScenario](examplescenario.html)
- [GraphDefinition](graphdefinition.html)
- [ImplementationGuide](implementationguide.html)
- [Library](library.html)
- [Measure](measure.html)
- [MessageDefinition](messagedefinition.html)
- [NamingSystem](namingsystem.html)
- [OperationDefinition](operationdefinition.html)
- [PlanDefinition](plandefinition.html)
- [Questionnaire](questionnaire.html)
- [ResearchDefinition](researchdefinition.html)
- [ResearchElementDefinition](researchelementdefinition.html)
- [RiskEvidenceSynthesis](riskevidencesynthesis.html)
- [SearchParameter](searchparameter.html)
- [StructureDefinition](structuredefinition.html)
- [StructureMap](structuremap.html)
- [TerminologyCapabilities](terminologycapabilities.html)
- [TestScript](testscript.html)
- [ValueSet](valueset.html)

A few elements that have references to canonical URLs have a [targetProfile](elementdefinition-definitions.html#ElementDefinition.type.targetProfile) of `http://hl7.org/fhir/StructureDefinition/Resource`,
which is shown as canonical(Any) in this specification. Such references SHALL only reference one of these types of resources.

### 2.3.0.6 Canonical Reference and Fragments

Canonical references may include a fragment when the reference is to a contained resource.
When the target of a canonical reference is a contained resource, the
canonical reference will have a fragment as part of the URL:

```

  <valueSet value="http://fhir.acme.com/Questionnaire/example|1.0#vs1"/>
```

This is a reference to the value set with id "vs1" in version 1.0 of the identified questionnaire.
The common case for this is internal references:

```

  <answerValueSet value="#vs1"/>
```

Which is the form for references to the contained value set inside the above example questionnaire.

### 2.3.0.7 Rendering References in Resource Narratives

References between resources create a challenge when rendering resource
narratives: the narrative includes information from the target resources. As an example,
consider an Observation with a patient reference:

```

{
  "resourceType" : "Observation",
  "subject" : {
    "reference" : "Patient/example"
  }
}
```

When represented in XHTML, this reference will generally become something like:

```

  ...
  <p>Patient: <a href="Patient/example">Peter James CHALMERS (12345)</a></p>  ...
```

This implies that the system generating the resource narrative will need
to resolve the reference and generate a summary, or that the reference will
contain the information (generated by an application that is able to resolve
the reference):

```

{
  "resourceType" : "Observation",
  "subject" : {
    "reference" : "Patient/example",
    "display" : "Peter James CHALMERS (12345)"
  }
}
```

Narrative that contains information derived from other resources like this
is still regarded as 'generated' (for [Narrative.status](narrative-definitions.html#Narrative.status)).

It's not mandatory to generate narrative this way. Narrative may
be generated like this:

```

  ...
  <p>Patient: <a href="Patient/example">(link)</a></p>  ...
```

However, users generally prefer a more informative narrative, so this
is not always acceptable.

Applications (and networks of applications) will need some kind of
systematic approach for resolving references and/or maintaining the
currency of narratives as the resources they reference are changed.
The exact details of this are out of scope for the FHIR standard.

Applications are encouraged to use the `Reference.display` element
to store a user presentable representation of the resource for when the
resource cannot be resolved (e.g. due to network errors). The `canonical`
type does not have a display element because applications are generally expected
to carry cached copies of the resources that are the target of the canonical
references. If this functionality is still needed or desired anyway, the
[Rendered Value extension](extension-rendered-value.html) can be
used.

### 2.3.0.8 Contained Resources

In some circumstances, the content referred to in the resource reference does not have an independent
existence apart from the resource that contains it - it cannot be identified independently, and nor
can it have its own independent transaction scope. Typically, such circumstances arise where resources
are being assembled by a secondary user of the source data, such as a middleware engine. If the data available
when the resource is constructed does not include record keys or absolute identification information, then
a properly identified resource cannot be assembled, and even if an arbitrary identification was associated
with it, the resource could never be the subject of a transaction outside the context of the resource that
refers to it.

For example, consider a situation where an interface engine is creating a [Condition](condition.html)
record on a patient from an [HL7 v2 ![](external.png)](http://www.hl7.org/implement/standards/product_brief.cfm?product_id=185) message, and the only information about the primary surgeon is her
first name and last name (REL-7.2 & REL-7.3). In the absence of a controlled practitioner directory,
this is not enough information to create an identified [Practitioner](practitioner.html)
resource since more than one practitioner might have the same name.

In these circumstances, the resource is placed directly in-line in the resource. **This SHOULD NOT be
done when the content can be identified properly, as once the identification is lost, it is extremely difficult
(and context dependent) to restore it again.** The FHIR version of a contained resource SHALL always be the
same as the resource that contains it.

An example of a contained resource:

```

 <Condition xmlns="http://hl7.org/fhir">
  <contained>
    <Practitioner>
      <id value="p1"/>
      <name>
        <family value="Person"/>
        <given value="Patricia"/>
      </name>
    </Practitioner>
  </contained>
  <!-- other attributes -->
  <asserter>
    <reference value="#p1" />
  </asserter>
  <!-- other attributes -->
 </Condition>
```

The same example in JSON:

```

{
  "resourceType" : "Condition",
  "contained": [
    {
      "resourceType" : "Practitioner",
      "id" : "p1",
      "name" : [{
        "family" : "Person",
        "given" : ["Patricia"]
      }]
	  }],
   "asserter" : {
     "reference" : "#p1"
  }
}
```

> **Implementation Note:**
> Contained resources are still a reference rather than being inlined directly
> into the element that is the reference (e.g. "custodian" above) to ensure that a
> single approach to resolving resource references can be used. Though direct containment
> would seem simpler, it would still be necessary to support internal references where the
> same contained resource is referenced more than once. In the end, all that it would achieve
> is creating additional options in the syntax. For users using XPath to process the resource,
> the following XPath fragment resolves the internal reference:
>
> ```
> 
> ancestor::f:*[not(parent::f:*)]/f:contained/*[@id=substring-after(current()/f:reference/@value, '#')]
> ```

Some notes about use and interpretation of contained resources:

- The `contained` element SHALL NOT have extensions on it (though contained resources can still contain extensions).
- The contained resource can be put in any resource that inherits from DomainResource. The contained element is then located at the
  beginning of the resource after any text narrative and before any extension.
- Contained resources share the same internal id resolution space as the parent resource (for id attributes, see [Narrative references](narrative.html#internal)).
- When resolving references, references are resolved by looking through the 'container' resource - the one that contains the other
  resources. Since there are no nested contained resources, there is only one container resource.
- References to contained resources are never resolved outside the container resource. Specifically, resolution stops at the elements
  Bundle.entry.resource and Parameters.parameter.resource, but not at DomainResource.contained.
- Both `Reference` and `canonical` types may refer to contained resources
- Contained resources SHALL NOT contain additional contained resources.
- Contained resources SHALL NOT contain `meta.versionId`, `meta.lastUpdated`, or `meta.security`.
- Contained resources MAY contain `meta.tag`, though there are many tags that do not make sense on contained resources.
- A contained resource SHALL only be included in a resource if something in that resource (potentially another contained resource) has a reference to it.

Like other resources, contained resources can contain narrative. However, when rendering the containing resource,
the narrative of the contained resources is ignored, so relevant information about contained resources SHALL
appear in the narrative of the containing resource.

Resources that are contained inline do not "inherit" context from their parent resource. For instance, if
the parent resource contains a "subject", and the contained resource also has a "subject" element defined,
there is no implication that the contained resource has the same subject as the parent resource.

Resources can only be contained in other resources if there is a reference from the resource to
the contained resource, or if the contained resource references the container resource.
This is intended to ensure that the meaning of the contained resource is clear, and that
there is no confusion as to its significance.

For a resource that references the container, the reference is "#", like this:

```

<Patient xmlns="http://hl7.org/fhir">
  <id value="something"/>
  <contained>
    <Provenance>
      <!-- no id necessary (though still allowed) -->
      <target>
        <reference value="#"/>
      </target>
    </Provenance>
  </contained>
  <!-- other attributes -->
</Patient>
```

> There is no way to search for contained resources that reference their container. Is this a problem?
>
> Feedback is welcome [here ![](external.png)](http://hl7.org/fhir-issues).

### 2.3.0.9 Circular Resource References

Some references are circular - that is, the reference points to another resource of the same type.
There are several reasons why a resource may refer to other resources of the same type:

- part-of: the resources describe a complex hierarchy composed of parts e.g. an organization structure
- builds-on: resources may add additional content to another resource by deriving from it e.g. extending type declarations
- replaces: one resource may be replaced by another due to changes over time e.g. replacing a prescription or to support patient merging
- uses/re-uses: a resource may use another resource in a modular arrangement e.g. library references or value sets including other value sets

For parameters where the relationship is a strict hierarchy (i.e. where it would be wrong to have circular
references, even transitively), there is [additional search support](search.html#recursive) for traversing the
hierarchy using :above and :below modifiers on the search parameters.

Hierarchical references with search parameters (can have :above and :below modifiers on search parameters):

- [CarePlan.basedOn](careplan-definitions.html#CarePlan.basedOn) (based-on)
- [CarePlan.replaces](careplan-definitions.html#CarePlan.replaces) (replaces)
- [CarePlan.partOf](careplan-definitions.html#CarePlan.partOf) (part-of)
- [Encounter.partOf](encounter-definitions.html#Encounter.partOf) (part-of)
- [Location.partOf](location-definitions.html#Location.partOf) (partof)
- [Organization.partOf](organization-definitions.html#Organization.partOf) (partof)
- [StructureDefinition.baseDefinition](structuredefinition-definitions.html#StructureDefinition.baseDefinition) (base)

References that may refer back to the source instance:

- [Patient.link.other](patient-definitions.html#Patient.link.other) (link)

References for which the hierarchical behavior is not specified:

- [Account.partOf](account-definitions.html#Account.partOf)
- [BiologicallyDerivedProduct.parent](biologicallyderivedproduct-definitions.html#BiologicallyDerivedProduct.parent)
- [CapabilityStatement.instantiates](capabilitystatement-definitions.html#CapabilityStatement.instantiates)
- [CapabilityStatement.imports](capabilitystatement-definitions.html#CapabilityStatement.imports)
- [CareTeam.participant.member](careteam-definitions.html#CareTeam.participant.member) (participant)
- [CatalogEntry.relatedEntry.item](catalogentry-definitions.html#CatalogEntry.relatedEntry.item)
- [ChargeItem.partOf](chargeitem-definitions.html#ChargeItem.partOf)
- [ChargeItemDefinition.partOf](chargeitemdefinition-definitions.html#ChargeItemDefinition.partOf)
- [ChargeItemDefinition.replaces](chargeitemdefinition-definitions.html#ChargeItemDefinition.replaces)
- [Claim.related.claim](claim-definitions.html#Claim.related.claim)
- [ClaimResponse.insurance.claimResponse](claimresponse-definitions.html#ClaimResponse.insurance.claimResponse)
- [ClinicalImpression.previous](clinicalimpression-definitions.html#ClinicalImpression.previous) (previous)
- [CodeSystem.supplements](codesystem-definitions.html#CodeSystem.supplements) (supplements)
- [Communication.inResponseTo](communication-definitions.html#Communication.inResponseTo)
- [CommunicationRequest.replaces](communicationrequest-definitions.html#CommunicationRequest.replaces) (replaces)
- [Composition.relatesTo.target[x]](composition-definitions.html#Composition.relatesTo.target[x])
- [ConceptMap.group.unmapped.url](conceptmap-definitions.html#ConceptMap.group.unmapped.url) (other)
- [Consent.source[x]](consent-definitions.html#Consent.source[x]) (source-reference)
- [Contract.instantiatesCanonical](contract-definitions.html#Contract.instantiatesCanonical)
- [Contract.legallyBinding[x]](contract-definitions.html#Contract.legallyBinding[x])
- [Device.parent](device-definitions.html#Device.parent)
- [DeviceDefinition.parentDevice](devicedefinition-definitions.html#DeviceDefinition.parentDevice) (parent)
- [DocumentReference.relatesTo.target](documentreference-definitions.html#DocumentReference.relatesTo.target) (relatesto)
- [ExampleScenario.workflow](examplescenario-definitions.html#ExampleScenario.workflow)
- [Group.member.entity](group-definitions.html#Group.member.entity) (member)
- [ImplementationGuide.dependsOn.uri](implementationguide-definitions.html#ImplementationGuide.dependsOn.uri) (depends-on)
- [Medication.ingredient.item[x]](medication-definitions.html#Medication.ingredient.item[x])
- [MedicationAdministration.partOf](medicationadministration-definitions.html#MedicationAdministration.partOf)
- [MedicationKnowledge.relatedMedicationKnowledge.reference](medicationknowledge-definitions.html#MedicationKnowledge.relatedMedicationKnowledge.reference)
- [MedicationRequest.basedOn](medicationrequest-definitions.html#MedicationRequest.basedOn)
- [MedicationRequest.priorPrescription](medicationrequest-definitions.html#MedicationRequest.priorPrescription)
- [MedicationStatement.partOf](medicationstatement-definitions.html#MedicationStatement.partOf) (part-of)
- [MessageDefinition.replaces](messagedefinition-definitions.html#MessageDefinition.replaces)
- [MessageDefinition.base](messagedefinition-definitions.html#MessageDefinition.base)
- [MessageDefinition.allowedResponse.message](messagedefinition-definitions.html#MessageDefinition.allowedResponse.message)
- [MolecularSequence.referenceSeq.referenceSeqPointer](molecularsequence-definitions.html#MolecularSequence.referenceSeq.referenceSeqPointer)
- [MolecularSequence.pointer](molecularsequence-definitions.html#MolecularSequence.pointer)
- [Observation.hasMember](observation-definitions.html#Observation.hasMember) (has-member)
- [Observation.derivedFrom](observation-definitions.html#Observation.derivedFrom) (derived-from)
- [OperationDefinition.base](operationdefinition-definitions.html#OperationDefinition.base) (base)
- [Person.link.target](person-definitions.html#Person.link.target) (link,patient,practitioner,relatedperson)
- [PlanDefinition.action.definition[x]](plandefinition-definitions.html#PlanDefinition.action.definition[x]) (definition)
- [Procedure.partOf](procedure-definitions.html#Procedure.partOf) (part-of)
- [Procedure.reasonReference](procedure-definitions.html#Procedure.reasonReference) (reason-reference)
- [Questionnaire.derivedFrom](questionnaire-definitions.html#Questionnaire.derivedFrom)
- [ResearchStudy.partOf](researchstudy-definitions.html#ResearchStudy.partOf) (partof)
- [SearchParameter.derivedFrom](searchparameter-definitions.html#SearchParameter.derivedFrom) (derived-from)
- [SearchParameter.component.definition](searchparameter-definitions.html#SearchParameter.component.definition) (component)
- [ServiceRequest.basedOn](servicerequest-definitions.html#ServiceRequest.basedOn) (based-on)
- [ServiceRequest.replaces](servicerequest-definitions.html#ServiceRequest.replaces) (replaces)
- [Specimen.parent](specimen-definitions.html#Specimen.parent) (parent)
- [StructureMap.import](structuremap-definitions.html#StructureMap.import)
- [Substance.ingredient.substance[x]](substance-definitions.html#Substance.ingredient.substance[x])
- [SubstanceSpecification.property.definingSubstance[x]](substancespecification-definitions.html#SubstanceSpecification.property.definingSubstance[x])
- [SubstanceSpecification.relationship.substance[x]](substancespecification-definitions.html#SubstanceSpecification.relationship.substance[x])
- [SupplyDelivery.partOf](supplydelivery-definitions.html#SupplyDelivery.partOf)
- [Task.partOf](task-definitions.html#Task.partOf) (part-of)
- [ValueSet.compose.include.valueSet](valueset-definitions.html#ValueSet.compose.include.valueSet)

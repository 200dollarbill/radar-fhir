---
id: codesystem
title: CodeSystem
source_url: https://hl7.org/fhir/R4/codesystem.html
group: fhir-r4
fhir_version: R4
fetched_at: '2026-09-11T13:23:40Z'
sha256: e5f39943cfbae7b115c785d32a9b5e1e1f22097fa38205277a9b55bf0f43ad2e
---
This page is part of the FHIR Specification (v4.0.1: R4 - Mixed [Normative](https://confluence.hl7.org/display/HL7/HL7+Balloting "Normative Standard") and [STU](https://confluence.hl7.org/display/HL7/HL7+Balloting "Standard for Trial-Use")) in it's permanent home (it will always be available at this URL). The current version which supercedes this version is [5.0.0](http://hl7.org/fhir/index.html). For a full list of available versions, see the [Directory of published versions ![](external.png)](http://hl7.org/fhir/directory.html). Page versions: [R5](http://hl7.org/fhir/R5/codesystem.html) [R4B](http://hl7.org/fhir/R4B/codesystem.html) **R4** [R3](http://hl7.org/fhir/STU3/codesystem.html)

- [Content](#)
- [Examples](codesystem-examples.html)
- [Detailed Descriptions](codesystem-definitions.html)
- [Mappings](codesystem-mappings.html)
- [Profiles & Extensions](codesystem-profiles.html)
- [Operations](codesystem-operations.html)
- [R3 Conversions](codesystem-version-maps.html)

# 4.8 Resource CodeSystem - Content

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [Vocabulary](http://www.hl7.org/Special/committees/Vocab/index.cfm)  Work Group | [Maturity Level](versions.html#maturity): [N](versions.html#std-process) | [Normative](versions.html#std-process "Standard Status") (from v4.0.0) | [Security Category](security.html#SecPrivConsiderations): Anonymous | [Compartments](compartmentdefinition.html): Not linked to any defined compartments |

|  |  |
| --- | --- |
|  | This page has been approved as part of an [ANSI](https://www.ansi.org/)  standard. See the [Conformance](ansi-conformance.html) Package for further details. |

The CodeSystem resource is used to declare the existence of and describe a code system or code system supplement and its key properties, and optionally define a part or all of its content.

## 4.8.1 Scope and Usage

The FHIR terminology specification is based on two key concepts, originally defined in [HL7 v3 Core Principles ![](external.png)](http://www.hl7.org/documentcenter/public/standards/V3/core_principles/infrastructure/coreprinciples/v3modelcoreprinciples.html):

- **code system** - declares the existence of and describes a code system or code system supplement and its key properties, and optionally defines a part or all of its content. Also known as Ontology, Terminology, or Enumeration
- **value set** - specifies a set of codes drawn from one or more code systems, intended for use in a particular context. Value sets link between `CodeSystem` definitions and their use in [coded elements](terminologies.html)

Code systems define which codes (symbols and/or expressions) exist, and how they are understood. Value sets
select a set of codes from one or more code systems to specify which codes can be used in a particular context.

The CodeSystem resource is used to declare the existence of a code system, and its key properties:

- Identifying URL and version
- Description, Copyright, publication date, and other metadata
- Some key properties of the code system itself - e.g. whether it exhibits concept permanence, whether it defines a compositional grammar, and whether the codes that it defines are case sensitive
- What filters can be used in value sets that use the code system in a ValueSet.compose element
- What concept properties are defined by the code system

In addition, the CodeSystem resource may list some or all of the concepts in the code system, along with
their basic properties (code, display, definition), designations, and additional properties. Code
System resources may also be used to define supplements, which extend an existing code system with
additional designations and properties.

The CodeSystem resource is not intended to support the process of maintaining code systems.
Instead, the focus is on publishing the properties and optionally the content of a code
system for use throughout the FHIR eco-system, such as to support value set expansion and
validation.
Note that the important existing (large) code systems (SNOMED CT, LOINC, RxNorm, ICD family, etc.)
all have their own maintenance systems and distribution formats, and CodeSystem is generally
not an efficient way to distribute their content, though it is used as one way of
declaring the filters and properties associated with those code systems.

## 4.8.2 Boundaries and Relationships

- Code systems are used in [ValueSet](valueset.html) resources
- The [Coding](datatypes.html#Coding) data type refers to CodeSystem resources by their canonical URL
- The CodeSystem resource design is based, in part, on the code system functionality described in
  the [HL7 CTS 2 ![](external.png)](http://www.omg.org/spec/CTS2/1.0/) specification.
  A CTS2 server can be used to maintain code systems which are then published using the CodeSystem resource
- The CodeSystem resource documents the inherent structure and capabilities of code system, whereas
  the [TerminologyCapabilities](terminologycapabilities.html) resource documents what a server hosting the code system is capable of

The `CodeSystem` resource declares the existence of a code system and its key properties including its preferred identifier.
The `NamingSystem` resource identifies the existence of a code or identifier system, and its possible and preferred identifiers.
The key difference between the resources is who creates and manages them - `CodeSystem` resources are managed
by the owner or publisher of the code system, who can properly define the code system features and content.
`NamingSystem` resources, on the other hand, are frequently defined by 3rd parties that encounter the
code system in use, and need to describe the use, but do not have the authority to define the features and content.
Additionally, there may be multiple authoritative `NamingSystem` resources for a code system, but ideally there
would be only one authoritative `CodeSystem` resource (identified by its canonical URL) that is provided by the code system publisher, with multiple copies distributed on additional FHIR servers or elsewhere and used where needed.

Both Code System supplements and [Concept Maps](conceptmap.html) may be used to define relationships between concepts
in different systems. ConceptMaps are assertions of the relationships between different concepts
that are associated with particular contexts of use, while CodeSystem supplements are used to
define inherent properties and semantics of the concepts in the code system

## 4.8.3 Background and Context

When using code systems and value sets, proper differentiation between a code system and a value set is important.
This is one very common area where significant clinical safety risks occur in practice. Implementers
should be familiar with the content in [Using Codes in Resources](terminologies.html).

### 4.8.3.1 CodeSystem Identification

A code system has three identifiers. The first two can be used to reference the code system in the FHIR context:

- `CodeSystem.id`: The [logical id](resource.html#id) on the system that holds the CodeSystem resource instance - this typically is expected to change as the resource moves from server to server. The location URI is constructed by appending the logical id to the server base address where the instance is found and the resource type. This URI should be a resolvable URL by which the resource instance may be retrieved, usually from a FHIR server, and it may be a relative reference typically to the server base URL.
- `CodeSystem.url`: The canonical URL that never changes for this code system - it is the same in every copy. The element is named `url` rather than `uri` for legacy reasons and to strongly encourage providing a resolvable URL as the identifier whenever possible. This canonical URL is used to refer to all instances of this particular code system across all servers and systems. Ideally, this URI should be a URL which resolves to the location of the master version of the code system, though this is not always possible.

> For example, the code systems published as part of the FHIR specification all have a location ("literal") URI which is the URL where they may be accessed in the FHIR specification itself. However, while a new version of the FHIR specification is being prepared, code systems that are published in the drafts will not be found in the current FHIR specification version.

Because it is common practice to copy (cache) code systems locally, most
references to code systems can use either the canonical URL or the location ("literal") URL.

The third code system identifier is used typically for external references to the code system outside of FHIR:

- `CodeSystem.identifier`: A system/value pair that is used to identify the code system in other contexts (such as an OID in an [HL7 v3 ![](external.png)](https://www.hl7.org/implement/standards/product_brief.cfm?product_id=186) specification)

For further information regarding resource identification, see [Resource Identity](resource.html#id).

This means that each code system has 2 different URIs that can be used to reference it -
its canonical URL (the `url` element), and its local location from which it may be retrieved (which includes the `id` element). Because it is common practice to copy (cache) code systems locally, most references to
code systems use the canonical URL.

Alternatively, the `identifier` and `version` elements may be used to reference this code system in a
design, a profile, a [CDA ![](external.png)](http://www.hl7.org/implement/standards/product_brief.cfm?product_id=7) template
or [HL7 v3 ![](external.png)](https://www.hl7.org/implement/standards/product_brief.cfm?product_id=186) message (in the CD data
type codeSystem and codeSystemVersion properties). These different contexts may make additional restrictions on the
possible values of these elements. The `identifier` is generally not needed when using code systems in
a FHIR context, where the canonical URL is always the focus.

This resource is referenced by [Coding](datatypes.html#Coding), itself, [ConceptMap](conceptmap.html#ConceptMap), [TerminologyCapabilities](terminologycapabilities.html#TerminologyCapabilities) and [ValueSet](valueset.html#ValueSet)

## 4.8.4 Resource Content

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
| .. [CodeSystem](codesystem-definitions.html#CodeSystem "CodeSystem : The CodeSystem resource is used to declare the existence of and describe a code system or code system supplement and its key properties, and optionally define a part or all of its content.") | [I](conformance-rules.html#constraints "This element has or is affected by some invariants")[N](versions.html#std-process "Standards Status = Normative") |  | [DomainResource](domainresource.html) | Declares the existence of and describes a code system or code system supplement + Warning: Name should be usable as an identifier for the module by machine processing applications such as code generation + Rule: Within a code system definition, all the codes SHALL be unique Elements defined in Ancestors: [id](resource.html#Resource "The logical id of the resource, as used in the URL for the resource. Once assigned, this value never changes."), [meta](resource.html#Resource "The metadata about the resource. This is content that is maintained by the infrastructure. Changes to the content might not always be associated with version changes to the resource."), [implicitRules](resource.html#Resource "A reference to a set of rules that were followed when the resource was constructed, and which must be understood when processing the content. Often, this is a reference to an implementation guide that defines the special rules along with other profiles etc."), [language](resource.html#Resource "The base language in which the resource is written."), [text](domainresource.html#DomainResource "A human-readable narrative that contains a summary of the resource and can be used to represent the content of the resource to a human. The narrative need not encode all the structured data, but is required to contain sufficient detail to make it \"clinically safe\" for a human to just read the narrative. Resource definitions may define what content should be represented in the narrative to ensure clinical safety."), [contained](domainresource.html#DomainResource "These resources do not have an independent existence apart from the resource that contains them - they cannot be identified independently, and nor can they have their own independent transaction scope."), [extension](domainresource.html#DomainResource "May be used to represent additional information that is not part of the basic definition of the resource. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension."), [modifierExtension](domainresource.html#DomainResource "May be used to represent additional information that is not part of the basic definition of the resource and that modifies the understanding of the element that contains it and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer is allowed to define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.  Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).") |
| ... [url](codesystem-definitions.html#CodeSystem.url "CodeSystem.url : An absolute URI that is used to identify this code system when it is referenced in a specification, model, design or an instance; also called its canonical identifier. This SHOULD be globally unique and SHOULD be a literal address at which at which an authoritative instance of this code system is (or will be) published. This URL can be the target of a canonical reference. It SHALL remain the same when the code system is stored on different servers. This is used in [Coding](datatypes.html#Coding).system.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [uri](datatypes.html#uri) | Canonical identifier for this code system, represented as a URI (globally unique) (Coding.system) |
| ... [identifier](codesystem-definitions.html#CodeSystem.identifier "CodeSystem.identifier : A formal identifier that is used to identify this code system when it is represented in other formats, or referenced in a specification, model, design or an instance.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [Identifier](datatypes.html#Identifier) | Additional identifier for the code system (business identifier) |
| ... [version](codesystem-definitions.html#CodeSystem.version "CodeSystem.version : The identifier that is used to identify this version of the code system when it is referenced in a specification, model, design or instance. This is an arbitrary value managed by the code system author and is not expected to be globally unique. For example, it might be a timestamp (e.g. yyyymmdd) if a managed version is not available. There is also no expectation that versions can be placed in a lexicographical sequence. This is used in [Coding](datatypes.html#Coding).version.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | Business version of the code system (Coding.version) |
| ... [name](codesystem-definitions.html#CodeSystem.name "CodeSystem.name : A natural language name identifying the code system. This name should be usable as an identifier for the module by machine processing applications such as code generation.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..1 | [string](datatypes.html#string) | Name for this code system (computer friendly) |
| ... [title](codesystem-definitions.html#CodeSystem.title "CodeSystem.title : A short, descriptive, user-friendly title for the code system.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | Name for this code system (human friendly) |
| ... [status](codesystem-definitions.html#CodeSystem.status "CodeSystem.status : The date (and optionally time) when the code system resource was created or revised.") | [?!](conformance-rules.html#isModifier "This element is a modifier element")[Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [code](datatypes.html#code) | draft | active | retired | unknown [PublicationStatus](valueset-publication-status.html "The lifecycle status of an artifact.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ... [experimental](codesystem-definitions.html#CodeSystem.experimental "CodeSystem.experimental : A Boolean value to indicate that this code system is authored for testing purposes (or education/evaluation/marketing) and is not intended to be used for genuine usage.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [boolean](datatypes.html#boolean) | For testing purposes, not real usage |
| ... [date](codesystem-definitions.html#CodeSystem.date "CodeSystem.date : The date  (and optionally time) when the code system was published. The date must change when the business version changes and it must change if the status code changes. In addition, it should change when the substantive content of the code system changes.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [dateTime](datatypes.html#dateTime) | Date last changed |
| ... [publisher](codesystem-definitions.html#CodeSystem.publisher "CodeSystem.publisher : The name of the organization or individual that published the code system.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | Name of the publisher (organization or individual) |
| ... [contact](codesystem-definitions.html#CodeSystem.contact "CodeSystem.contact : Contact details to assist a user in finding and communicating with the publisher.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [ContactDetail](metadatatypes.html#ContactDetail) | Contact details for the publisher |
| ... [description](codesystem-definitions.html#CodeSystem.description "CodeSystem.description : A free text natural language description of the code system from a consumer's perspective.") |  | 0..1 | [markdown](datatypes.html#markdown) | Natural language description of the code system |
| ... [useContext](codesystem-definitions.html#CodeSystem.useContext "CodeSystem.useContext : The content was developed with a focus and intent of supporting the contexts that are listed. These contexts may be general categories (gender, age, ...) or may be references to specific programs (insurance plans, studies, ...) and may be used to assist with indexing and searching for appropriate code system instances.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[TU](versions.html#std-process "Standards Status = Trial Use") | 0..\* | [UsageContext](metadatatypes.html#UsageContext) | The context that the content is intended to support |
| ... [jurisdiction](codesystem-definitions.html#CodeSystem.jurisdiction "CodeSystem.jurisdiction : A legal or geographic region in which the code system is intended to be used.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [CodeableConcept](datatypes.html#CodeableConcept) | Intended jurisdiction for code system (if applicable) [Jurisdiction](valueset-jurisdiction.html "Countries and regions within which this artifact is targeted for use.") ([Extensible](terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept (based on human review), alternate codings (or, data type allowing, text) may be included instead.")) |
| ... [purpose](codesystem-definitions.html#CodeSystem.purpose "CodeSystem.purpose : Explanation of why this code system is needed and why it has been designed as it has.") |  | 0..1 | [markdown](datatypes.html#markdown) | Why this code system is defined |
| ... [copyright](codesystem-definitions.html#CodeSystem.copyright "CodeSystem.copyright : A copyright statement relating to the code system and/or its contents. Copyright statements are generally legal restrictions on the use and publishing of the code system.") |  | 0..1 | [markdown](datatypes.html#markdown) | Use and/or publishing restrictions |
| ... [caseSensitive](codesystem-definitions.html#CodeSystem.caseSensitive "CodeSystem.caseSensitive : If code comparison is case sensitive when codes within this system are compared to each other.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [boolean](datatypes.html#boolean) | If code comparison is case sensitive |
| ... [valueSet](codesystem-definitions.html#CodeSystem.valueSet "CodeSystem.valueSet : Canonical reference to the value set that contains the entire code system.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [canonical](datatypes.html#canonical)([ValueSet](valueset.html)) | Canonical reference to the value set with entire code system |
| ... [hierarchyMeaning](codesystem-definitions.html#CodeSystem.hierarchyMeaning "CodeSystem.hierarchyMeaning : The meaning of the hierarchy of concepts as represented in this resource.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [code](datatypes.html#code) | grouped-by | is-a | part-of | classified-with [CodeSystemHierarchyMeaning](valueset-codesystem-hierarchy-meaning.html "The meaning of the hierarchy of concepts in a code system.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ... [compositional](codesystem-definitions.html#CodeSystem.compositional "CodeSystem.compositional : The code system defines a compositional (post-coordination) grammar.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [boolean](datatypes.html#boolean) | If code system defines a compositional grammar |
| ... [versionNeeded](codesystem-definitions.html#CodeSystem.versionNeeded "CodeSystem.versionNeeded : This flag is used to signify that the code system does not commit to concept permanence across versions. If true, a version must be specified when referencing this code system.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [boolean](datatypes.html#boolean) | If definitions are not stable |
| ... [content](codesystem-definitions.html#CodeSystem.content "CodeSystem.content : The extent of the content of the code system (the concepts and codes it defines) are represented in this resource instance.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [code](datatypes.html#code) | not-present | example | fragment | complete | supplement [CodeSystemContentMode](valueset-codesystem-content-mode.html "The extent of the content of the code system (the concepts and codes it defines) are represented in a code system resource.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ... [supplements](codesystem-definitions.html#CodeSystem.supplements "CodeSystem.supplements : The canonical URL of the code system that this code system supplement is adding designations and properties to.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [canonical](datatypes.html#canonical)([CodeSystem](codesystem.html)) | Canonical URL of Code System this adds designations and properties to |
| ... [count](codesystem-definitions.html#CodeSystem.count "CodeSystem.count : The total number of concepts defined by the code system. Where the code system has a compositional grammar, the basis of this count is defined by the system steward.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [unsignedInt](datatypes.html#unsignedInt) | Total concepts in the code system |
| ... [filter](codesystem-definitions.html#CodeSystem.filter "CodeSystem.filter : A filter that can be used in a value set compose statement when selecting concepts using a filter.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [BackboneElement](backboneelement.html) | Filter that can be used in a value set |
| .... [code](codesystem-definitions.html#CodeSystem.filter.code "CodeSystem.filter.code : The code that identifies this filter when it is used as a filter in [[[ValueSet]]].compose.include.filter.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [code](datatypes.html#code) | Code that identifies the filter |
| .... [description](codesystem-definitions.html#CodeSystem.filter.description "CodeSystem.filter.description : A description of how or why the filter is used.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | How or why the filter is used |
| .... [operator](codesystem-definitions.html#CodeSystem.filter.operator "CodeSystem.filter.operator : A list of operators that can be used with the filter.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..\* | [code](datatypes.html#code) | = | is-a | descendent-of | is-not-a | regex | in | not-in | generalizes | exists [FilterOperator](valueset-filter-operator.html "The kind of operation to perform as a part of a property based filter.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| .... [value](codesystem-definitions.html#CodeSystem.filter.value "CodeSystem.filter.value : A description of what the value for the filter should be.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [string](datatypes.html#string) | What to use for the value |
| ... [property](codesystem-definitions.html#CodeSystem.property "CodeSystem.property : A property defines an additional slot through which additional information can be provided about a concept.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [BackboneElement](backboneelement.html) | Additional information supplied about each concept |
| .... [code](codesystem-definitions.html#CodeSystem.property.code "CodeSystem.property.code : A code that is used to identify the property. The code is used internally (in CodeSystem.concept.property.code) and also externally, such as in property filters.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [code](datatypes.html#code) | Identifies the property on the concepts, and when referred to in operations |
| .... [uri](codesystem-definitions.html#CodeSystem.property.uri "CodeSystem.property.uri : Reference to the formal meaning of the property. One possible source of meaning is the [Concept Properties](codesystem-concept-properties.html) code system.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [uri](datatypes.html#uri) | Formal identifier for the property |
| .... [description](codesystem-definitions.html#CodeSystem.property.description "CodeSystem.property.description : A description of the property- why it is defined, and how its value might be used.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | Why the property is defined, and/or what it conveys |
| .... [type](codesystem-definitions.html#CodeSystem.property.type "CodeSystem.property.type : The type of the property value. Properties of type \"code\" contain a code defined by the code system (e.g. a reference to another defined concept).") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [code](datatypes.html#code) | code | Coding | string | integer | boolean | dateTime | decimal [PropertyType](valueset-concept-property-type.html "The type of a property value.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ... [concept](codesystem-definitions.html#CodeSystem.concept "CodeSystem.concept : Concepts that are in the code system. The concept definitions are inherently hierarchical, but the definitions must be consulted to determine what the meanings of the hierarchical relationships are.") |  | 0..\* | [BackboneElement](backboneelement.html) | Concepts in the code system |
| .... [code](codesystem-definitions.html#CodeSystem.concept.code "CodeSystem.concept.code : A code - a text symbol - that uniquely identifies the concept within the code system.") |  | 1..1 | [code](datatypes.html#code) | Code that identifies concept |
| .... [display](codesystem-definitions.html#CodeSystem.concept.display "CodeSystem.concept.display : A human readable string that is the recommended default way to present this concept to a user.") |  | 0..1 | [string](datatypes.html#string) | Text to display to the user |
| .... [definition](codesystem-definitions.html#CodeSystem.concept.definition "CodeSystem.concept.definition : The formal definition of the concept. The code system resource does not make formal definitions required, because of the prevalence of legacy systems. However, they are highly recommended, as without them there is no formal meaning associated with the concept.") |  | 0..1 | [string](datatypes.html#string) | Formal definition |
| .... [designation](codesystem-definitions.html#CodeSystem.concept.designation "CodeSystem.concept.designation : Additional representations for the concept - other languages, aliases, specialized purposes, used for particular purposes, etc.") |  | 0..\* | [BackboneElement](backboneelement.html) | Additional representations for the concept |
| ..... [language](codesystem-definitions.html#CodeSystem.concept.designation.language "CodeSystem.concept.designation.language : The language this designation is defined for.") |  | 0..1 | [code](datatypes.html#code) | Human language of the designation [Common Languages](valueset-languages.html "A human language.") ([Preferred](terminologies.html#preferred "Instances are encouraged to draw from the specified codes for interoperability purposes but are not required to do so to be considered conformant.") but limited to [AllLanguages](valueset-all-languages.html)) |
| ..... [use](codesystem-definitions.html#CodeSystem.concept.designation.use "CodeSystem.concept.designation.use : A code that details how this designation would be used.") |  | 0..1 | [Coding](datatypes.html#Coding) | Details how this designation would be used [Designation Use](valueset-designation-use.html "Details of how a designation would be used.") ([Extensible](terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept (based on human review), alternate codings (or, data type allowing, text) may be included instead.")) |
| ..... [value](codesystem-definitions.html#CodeSystem.concept.designation.value "CodeSystem.concept.designation.value : The text value for this designation.") |  | 1..1 | [string](datatypes.html#string) | The text value for this designation |
| .... [property](codesystem-definitions.html#CodeSystem.concept.property "CodeSystem.concept.property : A property value for this concept.") |  | 0..\* | [BackboneElement](backboneelement.html) | Property value for the concept |
| ..... [code](codesystem-definitions.html#CodeSystem.concept.property.code "CodeSystem.concept.property.code : A code that is a reference to CodeSystem.property.code.") |  | 1..1 | [code](datatypes.html#code) | Reference to CodeSystem.property.code |
| ..... [value[x]](codesystem-definitions.html#CodeSystem.concept.property.value_x_ "CodeSystem.concept.property.value[x] : The value of this property.") |  | 1..1 |  | Value of the property for this concept |
| ...... valueCode |  |  | [code](datatypes.html#code) |  |
| ...... valueCoding |  |  | [Coding](datatypes.html#Coding) |  |
| ...... valueString |  |  | [string](datatypes.html#string) |  |
| ...... valueInteger |  |  | [integer](datatypes.html#integer) |  |
| ...... valueBoolean |  |  | [boolean](datatypes.html#boolean) |  |
| ...... valueDateTime |  |  | [dateTime](datatypes.html#dateTime) |  |
| ...... valueDecimal |  |  | [decimal](datatypes.html#decimal) |  |
| .... [concept](codesystem-definitions.html#CodeSystem.concept.concept "CodeSystem.concept.concept : Defines children of a concept to produce a hierarchy of concepts. The nature of the relationships is variable (is-a/contains/categorizes) - see hierarchyMeaning.") |  | 0..\* | see [concept](#CodeSystem.concept "CodeSystem.concept") | Child Concepts (is-a/contains/categorizes) |
| [doco Documentation for this format](formats.html#table "Legend for this format") | | | | |

**UML Diagram** ([Legend](formats.html#uml))

**XML Template**

```

<CodeSystem xmlns="http://hl7.org/fhir"> ![doco](help.png)
 <!-- from Resource: id, meta, implicitRules, and language -->
 <!-- from DomainResource: text, contained, extension, and modifierExtension -->
 <url value="[uri]"/><!-- 0..1 Canonical identifier for this code system, represented as a URI (globally unique) (Coding.system) -->
 <identifier><!-- 0..* Identifier Additional identifier for the code system (business identifier) --></identifier>
 <version value="[string]"/><!-- 0..1 Business version of the code system (Coding.version) -->
 <name value="[string]"/><!-- ![??](lock.png) 0..1 Name for this code system (computer friendly) -->
 <title value="[string]"/><!-- 0..1 Name for this code system (human friendly) -->
 <status value="[code]"/><!-- 1..1 draft | active | retired | unknown -->
 <experimental value="[boolean]"/><!-- 0..1 For testing purposes, not real usage -->
 <date value="[dateTime]"/><!-- 0..1 Date last changed -->
 <publisher value="[string]"/><!-- 0..1 Name of the publisher (organization or individual) -->
 <contact><!-- 0..* ContactDetail Contact details for the publisher --></contact>
 <description value="[markdown]"/><!-- 0..1 Natural language description of the code system -->
 <useContext><!-- 0..* UsageContext The context that the content is intended to support --></useContext>
 <jurisdiction><!-- 0..* CodeableConcept Intended jurisdiction for code system (if applicable) --></jurisdiction>
 <purpose value="[markdown]"/><!-- 0..1 Why this code system is defined -->
 <copyright value="[markdown]"/><!-- 0..1 Use and/or publishing restrictions -->
 <caseSensitive value="[boolean]"/><!-- 0..1 If code comparison is case sensitive -->
 <valueSet><!-- 0..1 canonical(ValueSet) Canonical reference to the value set with entire code system --></valueSet>
 <hierarchyMeaning value="[code]"/><!-- 0..1 grouped-by | is-a | part-of | classified-with -->
 <compositional value="[boolean]"/><!-- 0..1 If code system defines a compositional grammar -->
 <versionNeeded value="[boolean]"/><!-- 0..1 If definitions are not stable -->
 <content value="[code]"/><!-- 1..1 not-present | example | fragment | complete | supplement -->
 <supplements><!-- 0..1 canonical(CodeSystem) Canonical URL of Code System this adds designations and properties to --></supplements>
 <count value="[unsignedInt]"/><!-- 0..1 Total concepts in the code system -->
 <filter>  <!-- 0..* Filter that can be used in a value set -->
  <code value="[code]"/><!-- 1..1 Code that identifies the filter -->
  <description value="[string]"/><!-- 0..1 How or why the filter is used -->
  <operator value="[code]"/><!-- 1..* = | is-a | descendent-of | is-not-a | regex | in | not-in | generalizes | exists -->
  <value value="[string]"/><!-- 1..1 What to use for the value -->
 </filter>
 <property>  <!-- 0..* Additional information supplied about each concept -->
  <code value="[code]"/><!-- 1..1 Identifies the property on the concepts, and when referred to in operations -->
  <uri value="[uri]"/><!-- 0..1 Formal identifier for the property -->
  <description value="[string]"/><!-- 0..1 Why the property is defined, and/or what it conveys -->
  <type value="[code]"/><!-- 1..1 code | Coding | string | integer | boolean | dateTime | decimal -->
 </property>
 <concept>  <!-- 0..* Concepts in the code system -->
  <code value="[code]"/><!-- 1..1 Code that identifies concept -->
  <display value="[string]"/><!-- 0..1 Text to display to the user -->
  <definition value="[string]"/><!-- 0..1 Formal definition -->
  <designation>  <!-- 0..* Additional representations for the concept -->
   <language value="[code]"/><!-- 0..1 Human language of the designation -->
   <use><!-- 0..1 Coding Details how this designation would be used --></use>
   <value value="[string]"/><!-- 1..1 The text value for this designation -->
  </designation>
  <property>  <!-- 0..* Property value for the concept -->
   <code value="[code]"/><!-- 1..1 Reference to CodeSystem.property.code -->
   <value[x]><!-- 1..1 code|Coding|string|integer|boolean|dateTime|decimal Value of the property for this concept --></value[x]>
  </property>
  <concept><!-- 0..* Content as for CodeSystem.concept Child Concepts (is-a/contains/categorizes) --></concept>
 </concept>
</CodeSystem>
```

**JSON Template**

```

{![doco](help.png)
  "resourceType" : "CodeSystem",
  // from Resource: id, meta, implicitRules, and language
  // from DomainResource: text, contained, extension, and modifierExtension
  "url" : "<uri>", // Canonical identifier for this code system, represented as a URI (globally unique) (Coding.system)
  "identifier" : [{ Identifier }], // Additional identifier for the code system (business identifier)
  "version" : "<string>", // Business version of the code system (Coding.version)
  "name" : "<string>", // C? Name for this code system (computer friendly)
  "title" : "<string>", // Name for this code system (human friendly)
  "status" : "<code>", // R!  draft | active | retired | unknown
  "experimental" : <boolean>, // For testing purposes, not real usage
  "date" : "<dateTime>", // Date last changed
  "publisher" : "<string>", // Name of the publisher (organization or individual)
  "contact" : [{ ContactDetail }], // Contact details for the publisher
  "description" : "<markdown>", // Natural language description of the code system
  "useContext" : [{ UsageContext }], // The context that the content is intended to support
  "jurisdiction" : [{ CodeableConcept }], // Intended jurisdiction for code system (if applicable)
  "purpose" : "<markdown>", // Why this code system is defined
  "copyright" : "<markdown>", // Use and/or publishing restrictions
  "caseSensitive" : <boolean>, // If code comparison is case sensitive
  "valueSet" : { canonical(ValueSet) }, // Canonical reference to the value set with entire code system
  "hierarchyMeaning" : "<code>", // grouped-by | is-a | part-of | classified-with
  "compositional" : <boolean>, // If code system defines a compositional grammar
  "versionNeeded" : <boolean>, // If definitions are not stable
  "content" : "<code>", // R!  not-present | example | fragment | complete | supplement
  "supplements" : { canonical(CodeSystem) }, // Canonical URL of Code System this adds designations and properties to
  "count" : "<unsignedInt>", // Total concepts in the code system
  "filter" : [{ // Filter that can be used in a value set
    "code" : "<code>", // R!  Code that identifies the filter
    "description" : "<string>", // How or why the filter is used
    "operator" : ["<code>"], // R!  = | is-a | descendent-of | is-not-a | regex | in | not-in | generalizes | exists
    "value" : "<string>" // R!  What to use for the value
  }],
  "property" : [{ // Additional information supplied about each concept
    "code" : "<code>", // R!  Identifies the property on the concepts, and when referred to in operations
    "uri" : "<uri>", // Formal identifier for the property
    "description" : "<string>", // Why the property is defined, and/or what it conveys
    "type" : "<code>" // R!  code | Coding | string | integer | boolean | dateTime | decimal
  }],
  "concept" : [{ // Concepts in the code system
    "code" : "<code>", // R!  Code that identifies concept
    "display" : "<string>", // Text to display to the user
    "definition" : "<string>", // Formal definition
    "designation" : [{ // Additional representations for the concept
      "language" : "<code>", // Human language of the designation
      "use" : { Coding }, // Details how this designation would be used
      "value" : "<string>" // R!  The text value for this designation
    }],
    "property" : [{ // Property value for the concept
      "code" : "<code>", // R!  Reference to CodeSystem.property.code
      // value[x]: Value of the property for this concept. One of these 7:
      "valueCode" : "<code>"
      "valueCoding" : { Coding }
      "valueString" : "<string>"
      "valueInteger" : <integer>
      "valueBoolean" : <boolean>
      "valueDateTime" : "<dateTime>"
      "valueDecimal" : <decimal>
    }],
    "concept" : [{ Content as for CodeSystem.concept }] // Child Concepts (is-a/contains/categorizes)
  }]
}
```

**Turtle Template**

```

@prefix fhir: <http://hl7.org/fhir/> .![doco](help.png)


[ a fhir:CodeSystem;
  fhir:nodeRole fhir:treeRoot; # if this is the parser root

  # from Resource: .id, .meta, .implicitRules, and .language
  # from DomainResource: .text, .contained, .extension, and .modifierExtension
  fhir:CodeSystem.url [ uri ]; # 0..1 Canonical identifier for this code system, represented as a URI (globally unique) (Coding.system)
  fhir:CodeSystem.identifier [ Identifier ], ... ; # 0..* Additional identifier for the code system (business identifier)
  fhir:CodeSystem.version [ string ]; # 0..1 Business version of the code system (Coding.version)
  fhir:CodeSystem.name [ string ]; # 0..1 Name for this code system (computer friendly)
  fhir:CodeSystem.title [ string ]; # 0..1 Name for this code system (human friendly)
  fhir:CodeSystem.status [ code ]; # 1..1 draft | active | retired | unknown
  fhir:CodeSystem.experimental [ boolean ]; # 0..1 For testing purposes, not real usage
  fhir:CodeSystem.date [ dateTime ]; # 0..1 Date last changed
  fhir:CodeSystem.publisher [ string ]; # 0..1 Name of the publisher (organization or individual)
  fhir:CodeSystem.contact [ ContactDetail ], ... ; # 0..* Contact details for the publisher
  fhir:CodeSystem.description [ markdown ]; # 0..1 Natural language description of the code system
  fhir:CodeSystem.useContext [ UsageContext ], ... ; # 0..* The context that the content is intended to support
  fhir:CodeSystem.jurisdiction [ CodeableConcept ], ... ; # 0..* Intended jurisdiction for code system (if applicable)
  fhir:CodeSystem.purpose [ markdown ]; # 0..1 Why this code system is defined
  fhir:CodeSystem.copyright [ markdown ]; # 0..1 Use and/or publishing restrictions
  fhir:CodeSystem.caseSensitive [ boolean ]; # 0..1 If code comparison is case sensitive
  fhir:CodeSystem.valueSet [ canonical(ValueSet) ]; # 0..1 Canonical reference to the value set with entire code system
  fhir:CodeSystem.hierarchyMeaning [ code ]; # 0..1 grouped-by | is-a | part-of | classified-with
  fhir:CodeSystem.compositional [ boolean ]; # 0..1 If code system defines a compositional grammar
  fhir:CodeSystem.versionNeeded [ boolean ]; # 0..1 If definitions are not stable
  fhir:CodeSystem.content [ code ]; # 1..1 not-present | example | fragment | complete | supplement
  fhir:CodeSystem.supplements [ canonical(CodeSystem) ]; # 0..1 Canonical URL of Code System this adds designations and properties to
  fhir:CodeSystem.count [ unsignedInt ]; # 0..1 Total concepts in the code system
  fhir:CodeSystem.filter [ # 0..* Filter that can be used in a value set
    fhir:CodeSystem.filter.code [ code ]; # 1..1 Code that identifies the filter
    fhir:CodeSystem.filter.description [ string ]; # 0..1 How or why the filter is used
    fhir:CodeSystem.filter.operator [ code ], ... ; # 1..* = | is-a | descendent-of | is-not-a | regex | in | not-in | generalizes | exists
    fhir:CodeSystem.filter.value [ string ]; # 1..1 What to use for the value
  ], ...;
  fhir:CodeSystem.property [ # 0..* Additional information supplied about each concept
    fhir:CodeSystem.property.code [ code ]; # 1..1 Identifies the property on the concepts, and when referred to in operations
    fhir:CodeSystem.property.uri [ uri ]; # 0..1 Formal identifier for the property
    fhir:CodeSystem.property.description [ string ]; # 0..1 Why the property is defined, and/or what it conveys
    fhir:CodeSystem.property.type [ code ]; # 1..1 code | Coding | string | integer | boolean | dateTime | decimal
  ], ...;
  fhir:CodeSystem.concept [ # 0..* Concepts in the code system
    fhir:CodeSystem.concept.code [ code ]; # 1..1 Code that identifies concept
    fhir:CodeSystem.concept.display [ string ]; # 0..1 Text to display to the user
    fhir:CodeSystem.concept.definition [ string ]; # 0..1 Formal definition
    fhir:CodeSystem.concept.designation [ # 0..* Additional representations for the concept
      fhir:CodeSystem.concept.designation.language [ code ]; # 0..1 Human language of the designation
      fhir:CodeSystem.concept.designation.use [ Coding ]; # 0..1 Details how this designation would be used
      fhir:CodeSystem.concept.designation.value [ string ]; # 1..1 The text value for this designation
    ], ...;
    fhir:CodeSystem.concept.property [ # 0..* Property value for the concept
      fhir:CodeSystem.concept.property.code [ code ]; # 1..1 Reference to CodeSystem.property.code
      # CodeSystem.concept.property.value[x] : 1..1 Value of the property for this concept. One of these 7
        fhir:CodeSystem.concept.property.valueCode [ code ]
        fhir:CodeSystem.concept.property.valueCoding [ Coding ]
        fhir:CodeSystem.concept.property.valueString [ string ]
        fhir:CodeSystem.concept.property.valueInteger [ integer ]
        fhir:CodeSystem.concept.property.valueBoolean [ boolean ]
        fhir:CodeSystem.concept.property.valueDateTime [ dateTime ]
        fhir:CodeSystem.concept.property.valueDecimal [ decimal ]
    ], ...;
    fhir:CodeSystem.concept.concept [ See CodeSystem.concept ], ... ; # 0..* Child Concepts (is-a/contains/categorizes)
  ], ...;
]
```

**Changes since R3**

|  |  |
| --- | --- |
| [CodeSystem](codesystem.html#CodeSystem) |  |
| CodeSystem.identifier | - Max Cardinality changed from 1 to \* |
| CodeSystem.status | - Change value set from http://hl7.org/fhir/ValueSet/publication-status to http://hl7.org/fhir/ValueSet/publication-status|4.0.1 |
| CodeSystem.experimental | - No longer marked as Modifier |
| CodeSystem.valueSet | - Type changed from uri to canonical(ValueSet) |
| CodeSystem.hierarchyMeaning | - Change value set from http://hl7.org/fhir/ValueSet/codesystem-hierarchy-meaning to http://hl7.org/fhir/ValueSet/codesystem-hierarchy-meaning|4.0.1 |
| CodeSystem.content | - Change value set from http://hl7.org/fhir/ValueSet/codesystem-content-mode to http://hl7.org/fhir/ValueSet/codesystem-content-mode|4.0.1 |
| CodeSystem.supplements | - Added Element |
| CodeSystem.filter.operator | - Change value set from http://hl7.org/fhir/ValueSet/filter-operator to http://hl7.org/fhir/ValueSet/filter-operator|4.0.1 |
| CodeSystem.property.type | - Change value set from http://hl7.org/fhir/ValueSet/concept-property-type to http://hl7.org/fhir/ValueSet/concept-property-type|4.0.1 |
| CodeSystem.concept.designation.language | - Change binding strength from extensible to preferred |
| CodeSystem.concept.property.value[x] | - Add Type decimal |

See the [Full Difference](diff.html) for further information

This analysis is available as [XML](codesystem.diff.xml) or [JSON](codesystem.diff.json).

See [R3 <--> R4 Conversion Maps](codesystem-version-maps.html) (status = 4 tests that all execute ok. All tests pass round-trip testing and 3 r3 resources are invalid (0 errors).)

**Structure**

| [Name](formats.html#table "The logical name of the element") | [Flags](formats.html#table "Information about the use of the element") | [Card.](formats.html#table "Minimum and Maximum # of times the the element can appear in the instance") | [Type](formats.html#table "Reference to the type of the element") | [Description & Constraints](formats.html#table "Additional information about the element")[doco](formats.html#table "Legend for this format") |
| --- | --- | --- | --- | --- |
| .. [CodeSystem](codesystem-definitions.html#CodeSystem "CodeSystem : The CodeSystem resource is used to declare the existence of and describe a code system or code system supplement and its key properties, and optionally define a part or all of its content.") | [I](conformance-rules.html#constraints "This element has or is affected by some invariants")[N](versions.html#std-process "Standards Status = Normative") |  | [DomainResource](domainresource.html) | Declares the existence of and describes a code system or code system supplement + Warning: Name should be usable as an identifier for the module by machine processing applications such as code generation + Rule: Within a code system definition, all the codes SHALL be unique Elements defined in Ancestors: [id](resource.html#Resource "The logical id of the resource, as used in the URL for the resource. Once assigned, this value never changes."), [meta](resource.html#Resource "The metadata about the resource. This is content that is maintained by the infrastructure. Changes to the content might not always be associated with version changes to the resource."), [implicitRules](resource.html#Resource "A reference to a set of rules that were followed when the resource was constructed, and which must be understood when processing the content. Often, this is a reference to an implementation guide that defines the special rules along with other profiles etc."), [language](resource.html#Resource "The base language in which the resource is written."), [text](domainresource.html#DomainResource "A human-readable narrative that contains a summary of the resource and can be used to represent the content of the resource to a human. The narrative need not encode all the structured data, but is required to contain sufficient detail to make it \"clinically safe\" for a human to just read the narrative. Resource definitions may define what content should be represented in the narrative to ensure clinical safety."), [contained](domainresource.html#DomainResource "These resources do not have an independent existence apart from the resource that contains them - they cannot be identified independently, and nor can they have their own independent transaction scope."), [extension](domainresource.html#DomainResource "May be used to represent additional information that is not part of the basic definition of the resource. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension."), [modifierExtension](domainresource.html#DomainResource "May be used to represent additional information that is not part of the basic definition of the resource and that modifies the understanding of the element that contains it and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer is allowed to define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.  Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).") |
| ... [url](codesystem-definitions.html#CodeSystem.url "CodeSystem.url : An absolute URI that is used to identify this code system when it is referenced in a specification, model, design or an instance; also called its canonical identifier. This SHOULD be globally unique and SHOULD be a literal address at which at which an authoritative instance of this code system is (or will be) published. This URL can be the target of a canonical reference. It SHALL remain the same when the code system is stored on different servers. This is used in [Coding](datatypes.html#Coding).system.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [uri](datatypes.html#uri) | Canonical identifier for this code system, represented as a URI (globally unique) (Coding.system) |
| ... [identifier](codesystem-definitions.html#CodeSystem.identifier "CodeSystem.identifier : A formal identifier that is used to identify this code system when it is represented in other formats, or referenced in a specification, model, design or an instance.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [Identifier](datatypes.html#Identifier) | Additional identifier for the code system (business identifier) |
| ... [version](codesystem-definitions.html#CodeSystem.version "CodeSystem.version : The identifier that is used to identify this version of the code system when it is referenced in a specification, model, design or instance. This is an arbitrary value managed by the code system author and is not expected to be globally unique. For example, it might be a timestamp (e.g. yyyymmdd) if a managed version is not available. There is also no expectation that versions can be placed in a lexicographical sequence. This is used in [Coding](datatypes.html#Coding).version.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | Business version of the code system (Coding.version) |
| ... [name](codesystem-definitions.html#CodeSystem.name "CodeSystem.name : A natural language name identifying the code system. This name should be usable as an identifier for the module by machine processing applications such as code generation.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..1 | [string](datatypes.html#string) | Name for this code system (computer friendly) |
| ... [title](codesystem-definitions.html#CodeSystem.title "CodeSystem.title : A short, descriptive, user-friendly title for the code system.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | Name for this code system (human friendly) |
| ... [status](codesystem-definitions.html#CodeSystem.status "CodeSystem.status : The date (and optionally time) when the code system resource was created or revised.") | [?!](conformance-rules.html#isModifier "This element is a modifier element")[Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [code](datatypes.html#code) | draft | active | retired | unknown [PublicationStatus](valueset-publication-status.html "The lifecycle status of an artifact.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ... [experimental](codesystem-definitions.html#CodeSystem.experimental "CodeSystem.experimental : A Boolean value to indicate that this code system is authored for testing purposes (or education/evaluation/marketing) and is not intended to be used for genuine usage.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [boolean](datatypes.html#boolean) | For testing purposes, not real usage |
| ... [date](codesystem-definitions.html#CodeSystem.date "CodeSystem.date : The date  (and optionally time) when the code system was published. The date must change when the business version changes and it must change if the status code changes. In addition, it should change when the substantive content of the code system changes.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [dateTime](datatypes.html#dateTime) | Date last changed |
| ... [publisher](codesystem-definitions.html#CodeSystem.publisher "CodeSystem.publisher : The name of the organization or individual that published the code system.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | Name of the publisher (organization or individual) |
| ... [contact](codesystem-definitions.html#CodeSystem.contact "CodeSystem.contact : Contact details to assist a user in finding and communicating with the publisher.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [ContactDetail](metadatatypes.html#ContactDetail) | Contact details for the publisher |
| ... [description](codesystem-definitions.html#CodeSystem.description "CodeSystem.description : A free text natural language description of the code system from a consumer's perspective.") |  | 0..1 | [markdown](datatypes.html#markdown) | Natural language description of the code system |
| ... [useContext](codesystem-definitions.html#CodeSystem.useContext "CodeSystem.useContext : The content was developed with a focus and intent of supporting the contexts that are listed. These contexts may be general categories (gender, age, ...) or may be references to specific programs (insurance plans, studies, ...) and may be used to assist with indexing and searching for appropriate code system instances.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[TU](versions.html#std-process "Standards Status = Trial Use") | 0..\* | [UsageContext](metadatatypes.html#UsageContext) | The context that the content is intended to support |
| ... [jurisdiction](codesystem-definitions.html#CodeSystem.jurisdiction "CodeSystem.jurisdiction : A legal or geographic region in which the code system is intended to be used.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [CodeableConcept](datatypes.html#CodeableConcept) | Intended jurisdiction for code system (if applicable) [Jurisdiction](valueset-jurisdiction.html "Countries and regions within which this artifact is targeted for use.") ([Extensible](terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept (based on human review), alternate codings (or, data type allowing, text) may be included instead.")) |
| ... [purpose](codesystem-definitions.html#CodeSystem.purpose "CodeSystem.purpose : Explanation of why this code system is needed and why it has been designed as it has.") |  | 0..1 | [markdown](datatypes.html#markdown) | Why this code system is defined |
| ... [copyright](codesystem-definitions.html#CodeSystem.copyright "CodeSystem.copyright : A copyright statement relating to the code system and/or its contents. Copyright statements are generally legal restrictions on the use and publishing of the code system.") |  | 0..1 | [markdown](datatypes.html#markdown) | Use and/or publishing restrictions |
| ... [caseSensitive](codesystem-definitions.html#CodeSystem.caseSensitive "CodeSystem.caseSensitive : If code comparison is case sensitive when codes within this system are compared to each other.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [boolean](datatypes.html#boolean) | If code comparison is case sensitive |
| ... [valueSet](codesystem-definitions.html#CodeSystem.valueSet "CodeSystem.valueSet : Canonical reference to the value set that contains the entire code system.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [canonical](datatypes.html#canonical)([ValueSet](valueset.html)) | Canonical reference to the value set with entire code system |
| ... [hierarchyMeaning](codesystem-definitions.html#CodeSystem.hierarchyMeaning "CodeSystem.hierarchyMeaning : The meaning of the hierarchy of concepts as represented in this resource.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [code](datatypes.html#code) | grouped-by | is-a | part-of | classified-with [CodeSystemHierarchyMeaning](valueset-codesystem-hierarchy-meaning.html "The meaning of the hierarchy of concepts in a code system.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ... [compositional](codesystem-definitions.html#CodeSystem.compositional "CodeSystem.compositional : The code system defines a compositional (post-coordination) grammar.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [boolean](datatypes.html#boolean) | If code system defines a compositional grammar |
| ... [versionNeeded](codesystem-definitions.html#CodeSystem.versionNeeded "CodeSystem.versionNeeded : This flag is used to signify that the code system does not commit to concept permanence across versions. If true, a version must be specified when referencing this code system.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [boolean](datatypes.html#boolean) | If definitions are not stable |
| ... [content](codesystem-definitions.html#CodeSystem.content "CodeSystem.content : The extent of the content of the code system (the concepts and codes it defines) are represented in this resource instance.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [code](datatypes.html#code) | not-present | example | fragment | complete | supplement [CodeSystemContentMode](valueset-codesystem-content-mode.html "The extent of the content of the code system (the concepts and codes it defines) are represented in a code system resource.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ... [supplements](codesystem-definitions.html#CodeSystem.supplements "CodeSystem.supplements : The canonical URL of the code system that this code system supplement is adding designations and properties to.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [canonical](datatypes.html#canonical)([CodeSystem](codesystem.html)) | Canonical URL of Code System this adds designations and properties to |
| ... [count](codesystem-definitions.html#CodeSystem.count "CodeSystem.count : The total number of concepts defined by the code system. Where the code system has a compositional grammar, the basis of this count is defined by the system steward.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [unsignedInt](datatypes.html#unsignedInt) | Total concepts in the code system |
| ... [filter](codesystem-definitions.html#CodeSystem.filter "CodeSystem.filter : A filter that can be used in a value set compose statement when selecting concepts using a filter.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [BackboneElement](backboneelement.html) | Filter that can be used in a value set |
| .... [code](codesystem-definitions.html#CodeSystem.filter.code "CodeSystem.filter.code : The code that identifies this filter when it is used as a filter in [[[ValueSet]]].compose.include.filter.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [code](datatypes.html#code) | Code that identifies the filter |
| .... [description](codesystem-definitions.html#CodeSystem.filter.description "CodeSystem.filter.description : A description of how or why the filter is used.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | How or why the filter is used |
| .... [operator](codesystem-definitions.html#CodeSystem.filter.operator "CodeSystem.filter.operator : A list of operators that can be used with the filter.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..\* | [code](datatypes.html#code) | = | is-a | descendent-of | is-not-a | regex | in | not-in | generalizes | exists [FilterOperator](valueset-filter-operator.html "The kind of operation to perform as a part of a property based filter.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| .... [value](codesystem-definitions.html#CodeSystem.filter.value "CodeSystem.filter.value : A description of what the value for the filter should be.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [string](datatypes.html#string) | What to use for the value |
| ... [property](codesystem-definitions.html#CodeSystem.property "CodeSystem.property : A property defines an additional slot through which additional information can be provided about a concept.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [BackboneElement](backboneelement.html) | Additional information supplied about each concept |
| .... [code](codesystem-definitions.html#CodeSystem.property.code "CodeSystem.property.code : A code that is used to identify the property. The code is used internally (in CodeSystem.concept.property.code) and also externally, such as in property filters.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [code](datatypes.html#code) | Identifies the property on the concepts, and when referred to in operations |
| .... [uri](codesystem-definitions.html#CodeSystem.property.uri "CodeSystem.property.uri : Reference to the formal meaning of the property. One possible source of meaning is the [Concept Properties](codesystem-concept-properties.html) code system.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [uri](datatypes.html#uri) | Formal identifier for the property |
| .... [description](codesystem-definitions.html#CodeSystem.property.description "CodeSystem.property.description : A description of the property- why it is defined, and how its value might be used.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | Why the property is defined, and/or what it conveys |
| .... [type](codesystem-definitions.html#CodeSystem.property.type "CodeSystem.property.type : The type of the property value. Properties of type \"code\" contain a code defined by the code system (e.g. a reference to another defined concept).") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [code](datatypes.html#code) | code | Coding | string | integer | boolean | dateTime | decimal [PropertyType](valueset-concept-property-type.html "The type of a property value.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ... [concept](codesystem-definitions.html#CodeSystem.concept "CodeSystem.concept : Concepts that are in the code system. The concept definitions are inherently hierarchical, but the definitions must be consulted to determine what the meanings of the hierarchical relationships are.") |  | 0..\* | [BackboneElement](backboneelement.html) | Concepts in the code system |
| .... [code](codesystem-definitions.html#CodeSystem.concept.code "CodeSystem.concept.code : A code - a text symbol - that uniquely identifies the concept within the code system.") |  | 1..1 | [code](datatypes.html#code) | Code that identifies concept |
| .... [display](codesystem-definitions.html#CodeSystem.concept.display "CodeSystem.concept.display : A human readable string that is the recommended default way to present this concept to a user.") |  | 0..1 | [string](datatypes.html#string) | Text to display to the user |
| .... [definition](codesystem-definitions.html#CodeSystem.concept.definition "CodeSystem.concept.definition : The formal definition of the concept. The code system resource does not make formal definitions required, because of the prevalence of legacy systems. However, they are highly recommended, as without them there is no formal meaning associated with the concept.") |  | 0..1 | [string](datatypes.html#string) | Formal definition |
| .... [designation](codesystem-definitions.html#CodeSystem.concept.designation "CodeSystem.concept.designation : Additional representations for the concept - other languages, aliases, specialized purposes, used for particular purposes, etc.") |  | 0..\* | [BackboneElement](backboneelement.html) | Additional representations for the concept |
| ..... [language](codesystem-definitions.html#CodeSystem.concept.designation.language "CodeSystem.concept.designation.language : The language this designation is defined for.") |  | 0..1 | [code](datatypes.html#code) | Human language of the designation [Common Languages](valueset-languages.html "A human language.") ([Preferred](terminologies.html#preferred "Instances are encouraged to draw from the specified codes for interoperability purposes but are not required to do so to be considered conformant.") but limited to [AllLanguages](valueset-all-languages.html)) |
| ..... [use](codesystem-definitions.html#CodeSystem.concept.designation.use "CodeSystem.concept.designation.use : A code that details how this designation would be used.") |  | 0..1 | [Coding](datatypes.html#Coding) | Details how this designation would be used [Designation Use](valueset-designation-use.html "Details of how a designation would be used.") ([Extensible](terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept (based on human review), alternate codings (or, data type allowing, text) may be included instead.")) |
| ..... [value](codesystem-definitions.html#CodeSystem.concept.designation.value "CodeSystem.concept.designation.value : The text value for this designation.") |  | 1..1 | [string](datatypes.html#string) | The text value for this designation |
| .... [property](codesystem-definitions.html#CodeSystem.concept.property "CodeSystem.concept.property : A property value for this concept.") |  | 0..\* | [BackboneElement](backboneelement.html) | Property value for the concept |
| ..... [code](codesystem-definitions.html#CodeSystem.concept.property.code "CodeSystem.concept.property.code : A code that is a reference to CodeSystem.property.code.") |  | 1..1 | [code](datatypes.html#code) | Reference to CodeSystem.property.code |
| ..... [value[x]](codesystem-definitions.html#CodeSystem.concept.property.value_x_ "CodeSystem.concept.property.value[x] : The value of this property.") |  | 1..1 |  | Value of the property for this concept |
| ...... valueCode |  |  | [code](datatypes.html#code) |  |
| ...... valueCoding |  |  | [Coding](datatypes.html#Coding) |  |
| ...... valueString |  |  | [string](datatypes.html#string) |  |
| ...... valueInteger |  |  | [integer](datatypes.html#integer) |  |
| ...... valueBoolean |  |  | [boolean](datatypes.html#boolean) |  |
| ...... valueDateTime |  |  | [dateTime](datatypes.html#dateTime) |  |
| ...... valueDecimal |  |  | [decimal](datatypes.html#decimal) |  |
| .... [concept](codesystem-definitions.html#CodeSystem.concept.concept "CodeSystem.concept.concept : Defines children of a concept to produce a hierarchy of concepts. The nature of the relationships is variable (is-a/contains/categorizes) - see hierarchyMeaning.") |  | 0..\* | see [concept](#CodeSystem.concept "CodeSystem.concept") | Child Concepts (is-a/contains/categorizes) |
| [doco Documentation for this format](formats.html#table "Legend for this format") | | | | |

**UML Diagram** ([Legend](formats.html#uml))

**XML Template**

```

<CodeSystem xmlns="http://hl7.org/fhir"> ![doco](help.png)
 <!-- from Resource: id, meta, implicitRules, and language -->
 <!-- from DomainResource: text, contained, extension, and modifierExtension -->
 <url value="[uri]"/><!-- 0..1 Canonical identifier for this code system, represented as a URI (globally unique) (Coding.system) -->
 <identifier><!-- 0..* Identifier Additional identifier for the code system (business identifier) --></identifier>
 <version value="[string]"/><!-- 0..1 Business version of the code system (Coding.version) -->
 <name value="[string]"/><!-- ![??](lock.png) 0..1 Name for this code system (computer friendly) -->
 <title value="[string]"/><!-- 0..1 Name for this code system (human friendly) -->
 <status value="[code]"/><!-- 1..1 draft | active | retired | unknown -->
 <experimental value="[boolean]"/><!-- 0..1 For testing purposes, not real usage -->
 <date value="[dateTime]"/><!-- 0..1 Date last changed -->
 <publisher value="[string]"/><!-- 0..1 Name of the publisher (organization or individual) -->
 <contact><!-- 0..* ContactDetail Contact details for the publisher --></contact>
 <description value="[markdown]"/><!-- 0..1 Natural language description of the code system -->
 <useContext><!-- 0..* UsageContext The context that the content is intended to support --></useContext>
 <jurisdiction><!-- 0..* CodeableConcept Intended jurisdiction for code system (if applicable) --></jurisdiction>
 <purpose value="[markdown]"/><!-- 0..1 Why this code system is defined -->
 <copyright value="[markdown]"/><!-- 0..1 Use and/or publishing restrictions -->
 <caseSensitive value="[boolean]"/><!-- 0..1 If code comparison is case sensitive -->
 <valueSet><!-- 0..1 canonical(ValueSet) Canonical reference to the value set with entire code system --></valueSet>
 <hierarchyMeaning value="[code]"/><!-- 0..1 grouped-by | is-a | part-of | classified-with -->
 <compositional value="[boolean]"/><!-- 0..1 If code system defines a compositional grammar -->
 <versionNeeded value="[boolean]"/><!-- 0..1 If definitions are not stable -->
 <content value="[code]"/><!-- 1..1 not-present | example | fragment | complete | supplement -->
 <supplements><!-- 0..1 canonical(CodeSystem) Canonical URL of Code System this adds designations and properties to --></supplements>
 <count value="[unsignedInt]"/><!-- 0..1 Total concepts in the code system -->
 <filter>  <!-- 0..* Filter that can be used in a value set -->
  <code value="[code]"/><!-- 1..1 Code that identifies the filter -->
  <description value="[string]"/><!-- 0..1 How or why the filter is used -->
  <operator value="[code]"/><!-- 1..* = | is-a | descendent-of | is-not-a | regex | in | not-in | generalizes | exists -->
  <value value="[string]"/><!-- 1..1 What to use for the value -->
 </filter>
 <property>  <!-- 0..* Additional information supplied about each concept -->
  <code value="[code]"/><!-- 1..1 Identifies the property on the concepts, and when referred to in operations -->
  <uri value="[uri]"/><!-- 0..1 Formal identifier for the property -->
  <description value="[string]"/><!-- 0..1 Why the property is defined, and/or what it conveys -->
  <type value="[code]"/><!-- 1..1 code | Coding | string | integer | boolean | dateTime | decimal -->
 </property>
 <concept>  <!-- 0..* Concepts in the code system -->
  <code value="[code]"/><!-- 1..1 Code that identifies concept -->
  <display value="[string]"/><!-- 0..1 Text to display to the user -->
  <definition value="[string]"/><!-- 0..1 Formal definition -->
  <designation>  <!-- 0..* Additional representations for the concept -->
   <language value="[code]"/><!-- 0..1 Human language of the designation -->
   <use><!-- 0..1 Coding Details how this designation would be used --></use>
   <value value="[string]"/><!-- 1..1 The text value for this designation -->
  </designation>
  <property>  <!-- 0..* Property value for the concept -->
   <code value="[code]"/><!-- 1..1 Reference to CodeSystem.property.code -->
   <value[x]><!-- 1..1 code|Coding|string|integer|boolean|dateTime|decimal Value of the property for this concept --></value[x]>
  </property>
  <concept><!-- 0..* Content as for CodeSystem.concept Child Concepts (is-a/contains/categorizes) --></concept>
 </concept>
</CodeSystem>
```

**JSON Template**

```

{![doco](help.png)
  "resourceType" : "CodeSystem",
  // from Resource: id, meta, implicitRules, and language
  // from DomainResource: text, contained, extension, and modifierExtension
  "url" : "<uri>", // Canonical identifier for this code system, represented as a URI (globally unique) (Coding.system)
  "identifier" : [{ Identifier }], // Additional identifier for the code system (business identifier)
  "version" : "<string>", // Business version of the code system (Coding.version)
  "name" : "<string>", // C? Name for this code system (computer friendly)
  "title" : "<string>", // Name for this code system (human friendly)
  "status" : "<code>", // R!  draft | active | retired | unknown
  "experimental" : <boolean>, // For testing purposes, not real usage
  "date" : "<dateTime>", // Date last changed
  "publisher" : "<string>", // Name of the publisher (organization or individual)
  "contact" : [{ ContactDetail }], // Contact details for the publisher
  "description" : "<markdown>", // Natural language description of the code system
  "useContext" : [{ UsageContext }], // The context that the content is intended to support
  "jurisdiction" : [{ CodeableConcept }], // Intended jurisdiction for code system (if applicable)
  "purpose" : "<markdown>", // Why this code system is defined
  "copyright" : "<markdown>", // Use and/or publishing restrictions
  "caseSensitive" : <boolean>, // If code comparison is case sensitive
  "valueSet" : { canonical(ValueSet) }, // Canonical reference to the value set with entire code system
  "hierarchyMeaning" : "<code>", // grouped-by | is-a | part-of | classified-with
  "compositional" : <boolean>, // If code system defines a compositional grammar
  "versionNeeded" : <boolean>, // If definitions are not stable
  "content" : "<code>", // R!  not-present | example | fragment | complete | supplement
  "supplements" : { canonical(CodeSystem) }, // Canonical URL of Code System this adds designations and properties to
  "count" : "<unsignedInt>", // Total concepts in the code system
  "filter" : [{ // Filter that can be used in a value set
    "code" : "<code>", // R!  Code that identifies the filter
    "description" : "<string>", // How or why the filter is used
    "operator" : ["<code>"], // R!  = | is-a | descendent-of | is-not-a | regex | in | not-in | generalizes | exists
    "value" : "<string>" // R!  What to use for the value
  }],
  "property" : [{ // Additional information supplied about each concept
    "code" : "<code>", // R!  Identifies the property on the concepts, and when referred to in operations
    "uri" : "<uri>", // Formal identifier for the property
    "description" : "<string>", // Why the property is defined, and/or what it conveys
    "type" : "<code>" // R!  code | Coding | string | integer | boolean | dateTime | decimal
  }],
  "concept" : [{ // Concepts in the code system
    "code" : "<code>", // R!  Code that identifies concept
    "display" : "<string>", // Text to display to the user
    "definition" : "<string>", // Formal definition
    "designation" : [{ // Additional representations for the concept
      "language" : "<code>", // Human language of the designation
      "use" : { Coding }, // Details how this designation would be used
      "value" : "<string>" // R!  The text value for this designation
    }],
    "property" : [{ // Property value for the concept
      "code" : "<code>", // R!  Reference to CodeSystem.property.code
      // value[x]: Value of the property for this concept. One of these 7:
      "valueCode" : "<code>"
      "valueCoding" : { Coding }
      "valueString" : "<string>"
      "valueInteger" : <integer>
      "valueBoolean" : <boolean>
      "valueDateTime" : "<dateTime>"
      "valueDecimal" : <decimal>
    }],
    "concept" : [{ Content as for CodeSystem.concept }] // Child Concepts (is-a/contains/categorizes)
  }]
}
```

**Turtle Template**

```

@prefix fhir: <http://hl7.org/fhir/> .![doco](help.png)


[ a fhir:CodeSystem;
  fhir:nodeRole fhir:treeRoot; # if this is the parser root

  # from Resource: .id, .meta, .implicitRules, and .language
  # from DomainResource: .text, .contained, .extension, and .modifierExtension
  fhir:CodeSystem.url [ uri ]; # 0..1 Canonical identifier for this code system, represented as a URI (globally unique) (Coding.system)
  fhir:CodeSystem.identifier [ Identifier ], ... ; # 0..* Additional identifier for the code system (business identifier)
  fhir:CodeSystem.version [ string ]; # 0..1 Business version of the code system (Coding.version)
  fhir:CodeSystem.name [ string ]; # 0..1 Name for this code system (computer friendly)
  fhir:CodeSystem.title [ string ]; # 0..1 Name for this code system (human friendly)
  fhir:CodeSystem.status [ code ]; # 1..1 draft | active | retired | unknown
  fhir:CodeSystem.experimental [ boolean ]; # 0..1 For testing purposes, not real usage
  fhir:CodeSystem.date [ dateTime ]; # 0..1 Date last changed
  fhir:CodeSystem.publisher [ string ]; # 0..1 Name of the publisher (organization or individual)
  fhir:CodeSystem.contact [ ContactDetail ], ... ; # 0..* Contact details for the publisher
  fhir:CodeSystem.description [ markdown ]; # 0..1 Natural language description of the code system
  fhir:CodeSystem.useContext [ UsageContext ], ... ; # 0..* The context that the content is intended to support
  fhir:CodeSystem.jurisdiction [ CodeableConcept ], ... ; # 0..* Intended jurisdiction for code system (if applicable)
  fhir:CodeSystem.purpose [ markdown ]; # 0..1 Why this code system is defined
  fhir:CodeSystem.copyright [ markdown ]; # 0..1 Use and/or publishing restrictions
  fhir:CodeSystem.caseSensitive [ boolean ]; # 0..1 If code comparison is case sensitive
  fhir:CodeSystem.valueSet [ canonical(ValueSet) ]; # 0..1 Canonical reference to the value set with entire code system
  fhir:CodeSystem.hierarchyMeaning [ code ]; # 0..1 grouped-by | is-a | part-of | classified-with
  fhir:CodeSystem.compositional [ boolean ]; # 0..1 If code system defines a compositional grammar
  fhir:CodeSystem.versionNeeded [ boolean ]; # 0..1 If definitions are not stable
  fhir:CodeSystem.content [ code ]; # 1..1 not-present | example | fragment | complete | supplement
  fhir:CodeSystem.supplements [ canonical(CodeSystem) ]; # 0..1 Canonical URL of Code System this adds designations and properties to
  fhir:CodeSystem.count [ unsignedInt ]; # 0..1 Total concepts in the code system
  fhir:CodeSystem.filter [ # 0..* Filter that can be used in a value set
    fhir:CodeSystem.filter.code [ code ]; # 1..1 Code that identifies the filter
    fhir:CodeSystem.filter.description [ string ]; # 0..1 How or why the filter is used
    fhir:CodeSystem.filter.operator [ code ], ... ; # 1..* = | is-a | descendent-of | is-not-a | regex | in | not-in | generalizes | exists
    fhir:CodeSystem.filter.value [ string ]; # 1..1 What to use for the value
  ], ...;
  fhir:CodeSystem.property [ # 0..* Additional information supplied about each concept
    fhir:CodeSystem.property.code [ code ]; # 1..1 Identifies the property on the concepts, and when referred to in operations
    fhir:CodeSystem.property.uri [ uri ]; # 0..1 Formal identifier for the property
    fhir:CodeSystem.property.description [ string ]; # 0..1 Why the property is defined, and/or what it conveys
    fhir:CodeSystem.property.type [ code ]; # 1..1 code | Coding | string | integer | boolean | dateTime | decimal
  ], ...;
  fhir:CodeSystem.concept [ # 0..* Concepts in the code system
    fhir:CodeSystem.concept.code [ code ]; # 1..1 Code that identifies concept
    fhir:CodeSystem.concept.display [ string ]; # 0..1 Text to display to the user
    fhir:CodeSystem.concept.definition [ string ]; # 0..1 Formal definition
    fhir:CodeSystem.concept.designation [ # 0..* Additional representations for the concept
      fhir:CodeSystem.concept.designation.language [ code ]; # 0..1 Human language of the designation
      fhir:CodeSystem.concept.designation.use [ Coding ]; # 0..1 Details how this designation would be used
      fhir:CodeSystem.concept.designation.value [ string ]; # 1..1 The text value for this designation
    ], ...;
    fhir:CodeSystem.concept.property [ # 0..* Property value for the concept
      fhir:CodeSystem.concept.property.code [ code ]; # 1..1 Reference to CodeSystem.property.code
      # CodeSystem.concept.property.value[x] : 1..1 Value of the property for this concept. One of these 7
        fhir:CodeSystem.concept.property.valueCode [ code ]
        fhir:CodeSystem.concept.property.valueCoding [ Coding ]
        fhir:CodeSystem.concept.property.valueString [ string ]
        fhir:CodeSystem.concept.property.valueInteger [ integer ]
        fhir:CodeSystem.concept.property.valueBoolean [ boolean ]
        fhir:CodeSystem.concept.property.valueDateTime [ dateTime ]
        fhir:CodeSystem.concept.property.valueDecimal [ decimal ]
    ], ...;
    fhir:CodeSystem.concept.concept [ See CodeSystem.concept ], ... ; # 0..* Child Concepts (is-a/contains/categorizes)
  ], ...;
]
```

**Changes since Release 3**

|  |  |
| --- | --- |
| [CodeSystem](codesystem.html#CodeSystem) |  |
| CodeSystem.identifier | - Max Cardinality changed from 1 to \* |
| CodeSystem.status | - Change value set from http://hl7.org/fhir/ValueSet/publication-status to http://hl7.org/fhir/ValueSet/publication-status|4.0.1 |
| CodeSystem.experimental | - No longer marked as Modifier |
| CodeSystem.valueSet | - Type changed from uri to canonical(ValueSet) |
| CodeSystem.hierarchyMeaning | - Change value set from http://hl7.org/fhir/ValueSet/codesystem-hierarchy-meaning to http://hl7.org/fhir/ValueSet/codesystem-hierarchy-meaning|4.0.1 |
| CodeSystem.content | - Change value set from http://hl7.org/fhir/ValueSet/codesystem-content-mode to http://hl7.org/fhir/ValueSet/codesystem-content-mode|4.0.1 |
| CodeSystem.supplements | - Added Element |
| CodeSystem.filter.operator | - Change value set from http://hl7.org/fhir/ValueSet/filter-operator to http://hl7.org/fhir/ValueSet/filter-operator|4.0.1 |
| CodeSystem.property.type | - Change value set from http://hl7.org/fhir/ValueSet/concept-property-type to http://hl7.org/fhir/ValueSet/concept-property-type|4.0.1 |
| CodeSystem.concept.designation.language | - Change binding strength from extensible to preferred |
| CodeSystem.concept.property.value[x] | - Add Type decimal |

See the [Full Difference](diff.html) for further information

This analysis is available as [XML](codesystem.diff.xml) or [JSON](codesystem.diff.json).

See [R3 <--> R4 Conversion Maps](codesystem-version-maps.html) (status = 4 tests that all execute ok. All tests pass round-trip testing and 3 r3 resources are invalid (0 errors).)

See the [Profiles & Extensions](codesystem-profiles.html) and the alternate definitions:
Master Definition [XML](codesystem.profile.xml.html) + [JSON](codesystem.profile.json.html),
[XML](xml.html) [Schema](codesystem.xsd)/[Schematron](codesystem.sch) + [JSON](json.html)
[Schema](codesystem.schema.json.html), [ShEx](codesystem.shex.html) (for [Turtle](rdf.html)) + [see the extensions](codesystem-profiles.html) & the [dependency analysis](codesystem-dependencies.html)

### 4.8.4.1 Terminology Bindings

| Path | Definition | Type | Reference |
| --- | --- | --- | --- |
| CodeSystem.status | The lifecycle status of an artifact. | [Required](terminologies.html#required) | [PublicationStatus](valueset-publication-status.html) |
| CodeSystem.jurisdiction | Countries and regions within which this artifact is targeted for use. | [Extensible](terminologies.html#extensible) | [Jurisdiction ValueSet](valueset-jurisdiction.html) |
| CodeSystem.hierarchyMeaning | The meaning of the hierarchy of concepts in a code system. | [Required](terminologies.html#required) | [CodeSystemHierarchyMeaning](valueset-codesystem-hierarchy-meaning.html) |
| CodeSystem.content | The extent of the content of the code system (the concepts and codes it defines) are represented in a code system resource. | [Required](terminologies.html#required) | [CodeSystemContentMode](valueset-codesystem-content-mode.html) |
| CodeSystem.filter.operator | The kind of operation to perform as a part of a property based filter. | [Required](terminologies.html#required) | [FilterOperator](valueset-filter-operator.html) |
| CodeSystem.property.type | The type of a property value. | [Required](terminologies.html#required) | [PropertyType](valueset-concept-property-type.html) |
| CodeSystem.concept.designation.language | A human language. | [Preferred](terminologies.html#preferred), but limited to [AllLanguages](valueset-all-languages.html) | [CommonLanguages](valueset-languages.html) |
| CodeSystem.concept.designation.use | Details of how a designation would be used. | [Extensible](terminologies.html#extensible) | [DesignationUse](valueset-designation-use.html) |

### 4.8.4.2 Constraints

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **id** | **Level** | **Location** | **Description** | **[Expression](fhirpath.html)** |
| **csd-0** | [Warning](conformance-rules.html#warning) | (base) | Name should be usable as an identifier for the module by machine processing applications such as code generation | name.matches('[A-Z]([A-Za-z0-9\_]){0,254}') |
| **csd-1** | [Rule](conformance-rules.html#rule) | (base) | Within a code system definition, all the codes SHALL be unique | concept.code.combine($this.descendants().concept.code).isDistinct() |

## 4.8.5 Versioning Code Systems

Most code systems evolve over time, due to corrections, clarifications, and changes to approach or underlying knowledge or reality.
If these changes lead to the meanings of existing codes changing significantly, then the interpretation of the code system becomes
version dependent. This significantly complicates implementation based on the code system, to the point where it is not clear that
safety can be assured, so changing the meaning of an existing code SHOULD be avoided whenever possible. It is preferable to assign a new identifier to a code system
when any concepts in it have a significant change in meaning (for example, the German diagnostic classification code system
ICD10GM2009 has a different *system* to ICD10GM2008), but this also can have substantial impact on implementation, so
is often not practical - for instance, [SNOMED CT](snomedct.html) has a complex version release framework, which
may lead to variations in meaning of concepts, but there is only one identifier for SNOMED CT.

For this reason, a code system MAY provide a version identifier which can be specified in `CodeSystem.version`. The version specific identifier SHOULD be
provided whenever there are potentially significant changes in meaning across multiple releases of a code system.
There is no particular format requirement for the version identifier, though HL7 recommends a date-based approach.

When the `CodeSystem.versionNeeded` is 'true', then the version identifier SHALL be used in [Coding](datatypes.html#coding) instances that refer to the code system.

Where the terminology does not clearly define what string should be used to identify code system versions, the recommendation is to use as the version string the date (expressed in FHIR date format) on which the version of the code system that is being used was officially published.

## 4.8.6 Multi-part Code Systems

The simple case for a code system is that the entire code system - all the concepts and their codes, designations and properties
are distributed in a single `CodeSystem` resource. However, for a variety of reasons, code systems may be distributed
by the code system authority in a set of fragments, and other authorities may issue additional designations and properties
in supplements.

## 4.8.7 Code System Fragments

If the `CodeSystem.content` value is `fragment`, then the resource
describes part of a code system.

Code Systems may be distributed in fragments for the following reasons:

- Different IP distribution rules for different parts of the code system
- Special purpose modules for specific purposes
- Distribution of proposed content for evaluation

The following rules apply to code system fragments:

- All fragments SHALL have the same CodeSystem.url
- Fragments can only be published by the code system authority, or according to a process defined by the authority, if they have defined one
- Fragments cannot contain any codes, concepts or properties that would not be found in a complete representation of the code system, if one exists
- Publishing a code system in multiple fragments can create confusion for terminology servers and terminology service consumers.
  Code System authorities that publish fragments should be careful and communicate their intent clearly

## 4.8.8 Code System Supplements

If the `CodeSystem.content` value is `supplement`, then the resource
describes a code system supplement. The following rules apply to code system supplements:

- The `CodeSystem.supplements` element SHALL have a value, which is the URL of the code system being supplemented
- The `CodeSystem.url` for a supplement SHALL never appear in a [Coding.system](datatypes.html#Coding)
- The `CodeSystem.url` for a supplement must be under the control of the authority creating or publishing the supplement
  (e.g. not in the same space as the code system being supplemented, unless the supplement is being issued by the same authority as the original code system
- A codesystem supplement cannot define any new CodeSystem.concept.code. i.e.: all CodeSystem.concept.code in the supplement must be a code from the "supplemented" code system

If a supplement needs to define new concepts/codes to use as property values, it can be paired with a new (possibly contained)
Code System and use the `Coding` type for the property values.

> The impact of Code System supplements on [value set expansion](valueset-operation-expand.html) - and therefore [value set validation](valueset-operation-validate-code.html) - is
> subject to ongoing experimentation and implementation testing, and further clarification and additional
> rules might be proposed in future versions of this specification.

## 4.8.9 Display, Definition and Designations

Concepts have both a `display` and a `definition`. The display is a short text that represents the meaning
of the concept to human users, while the definition is a more formal statement of the meaning of the concept, which
is often longer. All concepts SHOULD have a `display` and a `definition`, though it is not
mandatory because there are many cases where no such properties are provided, in spite of their utility and importance
for clear and safe communication.

In addition to the display and definition, a concept can have one or more `designation` elements.
The display is equivalent to a special designation with an implied `designation.use` meaning "primary code/designation"
and a language equal to the [Resource Language](resource.html#language). The designations can provide additional displays
for other language, as well as designations for other purposes.
When using concepts, applications use the `display` and `designation` unless the language or usage in context provides a reason
to use one of the designations.

## 4.8.10 Properties

Each code system can define one or more concept properties. Each concept defined by the code system
may have one or more values for each concept property defined by the code system. Typical uses for
properties include:

- Tracking administrative status (inactive, deprecation date)
- Providing additional statements about the meaning of the concept
- Defining structured relationships with other concepts in the code system
- Assigning scoring values to the concepts

Properties are identified by their master URI (`CodeSystem.property.uri`), and then, by their
code (`CodeSystem.property.code`), which is used both internally within the
code system resource (`CodeSystem.concept.property.code`) and also externally, in the following
places:

- [ConceptMap](conceptmap-definitions.html#ConceptMap.group.element.target.dependsOn.property): `ConceptMap.element.target.dependsOn.property` and `ConceptMap.element.target.product.property`
- [ValueSet](valueset-definitions.html#ValueSet.compose.include.filter.property): `ValueSet.compose.include.filter.property` can refer to any defined code system property
- [$lookup operation](codesystem-operations.html#lookup): In `Parameters.parameter.name` when returning information about a code
- [$translate operation](conceptmap-operations.html#translate): In `Parameters.parameter.part.name` for dependencies and products
- [$find-matches operation](codesystem-operations.html#compose): In `Parameters.parameter.name` when providing codes, and in `Parameters.parameter.name` when asking for codes

Properties are defined using the following elements:

|  |  |  |
| --- | --- | --- |
| **Name** | **Details** | **Description** |
| code | [code](datatypes.html#code) | Used to identify the property, in the places shown in the list immediately above this table |
| uri | optional [uri](datatypes.html#code) | Reference to the formal meaning of the property. One possible source of meaning is the [Concept Properties](codesystem-concept-properties.html) code system. This part of the definition is optional, but is recommended to provide an additional level of definitional consistency |
| description | optional [string](datatypes.html#code) | A description of the property- why it is defined, and how its value might be used |
| type | code | Coding | string | integer | boolean | dateTime | The type of the property value. Properties of type "code" contain a code defined by the code system (e.g. a reference to another defined concept) |

Note that properties provide a common view of concept relationships that is common across all code systems.
Some code systems define properties with more sophistication, such as groups of properties, or subsumption
relationships between properties (e.g. SNOMED CT). Servers providing support for these code systems will need
to know full details about the underlying relationships in order to provide the correct information about
concepts and their properties, but this information does not surface in the resources or operations defined
by the FHIR specification.

## 4.8.11 Concept Status

Many Code Systems have a 'status' associated with the concept. This may categorize the concept
as:

- Experimental - provided for trial, but may be removed in the future
- Active - in normal use
- Deprecated - planned to be removed from use
- Retired - still present for historical reasons, but no longer allowed to be used

There is wide variation in the life cycles supported by the different code systems, the words
they use to describe the various status values they use, and some code systems have additional
status values. HL7 uses Active and Retired. In addition to these status codes, concepts may also
be labeled as "Abstract' (not to be used in some circumstances), and have dates associated
with their retirement or deprecation. All this information is represented as properties of
the concepts. In order to assist with consistency between code systems, the following
basic property URIs are defined:

|  |  |
| --- | --- |
| http://hl7.org/fhir/concept-properties#status : code | A property that indicates the status of the concept. If the property is identified by this URL, then it SHALL use at least these status values (where appropriate):  - active - the concept is for normal use - experimental - provided for trial, but may be removed in the future - deprecated - planned to be removed from use - retired - still present for historical reasons, but no longer allowed to be used  The HL7 defined code systems (whether defined by the FHIR project, the V3 framework, or the V2 standard) all use this property to define their status. HL7 uses "active" (and considers this the default status), and deprecated and retired (= inactive) |
| http://hl7.org/fhir/concept-properties#retirementDate : date | Date Concept was retired |
| http://hl7.org/fhir/concept-properties#deprecationDate : date | Date Concept was deprecated |
| http://hl7.org/fhir/concept-properties#parent : code | An immediate parent of the concept in the hierarchy |
| http://hl7.org/fhir/concept-properties#child : code | An immediate child of the concept in the hierarchy |
| http://hl7.org/fhir/concept-properties#notSelectable : boolean | This concept is a grouping concept and not intended to be used in the normal use of the code system (though may be used for filters etc.). This is also known as 'Abstract' |

The parent and child properties are used when performing concept lookup (using the [$lookup](codesystem-operations.html#lookup) operation),
and when using properties to indicate parent/child relationships (see below).

## 4.8.12 Concept Hierarchy

Code systems may be presented hierarchically, using nested `concept` elements, where the
hierarchy has a defined meaning specified in [`hierarchyMeaning`](codesystem-definitions.html#CodeSystem.hierarchyMeaning).
The code system hierarchy is a single tree, where concepts have only one parent.

Some code systems define concepts that have multiple parents.
If a code system has concepts like this (typically, concepts that are subsumed by
more than one other concept), the code system SHOULD NOT be represented using the hierarchy structure in
the Code System resource, and the relationships between concepts should be defined using [properties](#properties).
If the hierarchy is used, implementers SHALL use a property to indicate
additional parents that are not represented in the structural (nested concepts) hierarchy.

Operations based on the codeSystem resource SHALL have the same result whether or not the
relationships are represented explicitly as properties or implicitly using the CodeSystem
resource hierarchy.

## 4.8.13 Subsumption Testing

The words 'subsume', 'subsumes', 'subsumed' and 'subsumption' are defined in relation to the type of hierarchy (i.e. the value of [CodeSystem.hierarchyMeaning](codesystem-definitions.html#CodeSystem.hierarchyMeaning)) identified for the code system that is being represented by the CodeSystem resource.
Concept A is considered to be subsumed by Concept B if it comes under Concept B in the hierarchy, or if a parent/child relationship is declared in the properties, and the hierarchyMeaning is "is-a").

Where a CodeSystem does not declare its hierarchy meaning directly, then the code system documentation must be consulted manually to determine how subsumption is determined. If there is no definition, none of the subsumption based features can be used with the code system.

Subsumption based logic arises explicitly or implicitly in the following places in the FHIR specification:

- [CodeSystem $subsumes operation](codesystem-operations.html#subsumes)
- [CodeSystem $lookup operation](codesystem-operations.html#lookup)
- [ConceptMap $closure operation](conceptmap-operations.html#closure)
- [Search by subsumption](search.html#subsumption)
- [ValueSet $expand operation](valueset-operations.html#expand)
- [ValueSet $validate-code operation](valueset-operations.html#validate-code)

## 4.8.14 Filters

The following filters are defined for all code systems:

| Property Name | Operation | Value | Definition | Notes |
| --- | --- | --- | --- | --- |
| [property] | = | [string] | Includes all codes that have a property value equal to the specified string, where [property] is the code for any [defined property](#properties) |  |
| [property] | in | [string,string...] | Includes all codes that have a property value equal to one of the specified strings, where [property] is the code for any [defined property](#properties) | The values cannot include ",", since it is being used as a delimiter |

This [draft section](versions.html#std-process "Draft Content") about the relationships between rich terminologies and structured content is still undergoing review.

## 4.8.15 Implicit Code Systems

Some other parts of the FHIR infrastructure define set of concepts that may also be treated
as code systems. This is most useful when mapping between systems using [Concept Maps](conceptmap.html),
but might also be useful for other code system related functionality (e.g. subsetting use [Value Sets](valueset.html)).
This table summarizes how to treat these items as a terminology:

|  |  |
| --- | --- |
| [StructureDefinition](structuredefinition.html) | The `StructureDefinition.url` (canonical URL) is the `system`. Each `.snapshot.element.id` in the snapshot is a code in the code system |
| [Questionnaire](questionnaire.html) | The `Questionnaire.url` (canonical URL) is the `system`. Each `.item.linkId` in the snapshot is a code in the code system. Items with no linkId cannot be addressed |
| [Medication](medication.html) | Medication resources are a bit different, since they don't have a canonical URL, and there are not multiple items in a resource. So to refer to a medication resource, the system is [base]/Medication, where base is the server address. The [Logical Id](resource.html#id) of the resource is the code |

The use of these implicit code systems is not yet well tested, so this section remains
informative.

For medications, the relationship between the code system and the medication resource
is complex. Many medication related code systems (e.g. RxNorm, DM+D, AMT, etc.) represent
more complex information than just code, display name and code system. These often
contain information about the content of the medication
A similar principle applies to observation definitions, which overlap significantly
with LOINC and other related code systems, which contain a set of observation
definitions, that contain methods, units, etc. Other similar arrangements exist
for [Location](location.html) and many other kinds of resource.

In FHIR, these are handled by splitting the concept into two distinct parts - the
Terminology, (**Code System** & `ValueSet` resources) is used to
manage the codes, display names and relationships. A separate "detail"
resource (e.g., [Medication resource instances](medication.html) for RxNorm code details,
[ObservationDefinition](observationdefinition.html) instances for LOINC code details, or
[Location](location.html), etc.) is used to convey detailed
information (dose form & strength, allowed data type or permitted values, address &
hours of operation, etc.). One "detail" resource instance is created for each code.

This division accomplishes several things:

- It allows generic systems that support terminology management to perform standard
  terminology operations on code systems dealing with complex structures - code lookup,
  validation, subsumption testing, mapping and translation.
- It allows information to be exchanged about individual medications, data elements
  and locations. Codes can't be retrieved individually in FHIR - it is necessary to
  retrieve the entire resource. By packaging the detailed information in separate
  resources, independent retrieval and update is possible.
- It supports use-cases for sharing medication, location, observation type and
  similar information in circumstances where the code may be unknown, unavailable or
  occasionally non-existent (e.g., custom compounds, non-registered locations). Having
  a distinct resource supports these capabilities, which would not be possible using
  `CodeSystem`/`ValueSet`.

Note that this division in FHIR does not imply that a similar division is required in
the internal representation used by systems exposing a FHIR interface. Similarly, some
systems may choose to only expose or maintain one aspect of such information types (i.e.
only the discrete resource instances or only the value set).

The linkage between the "detail" resource and the Terminology resources is accomplished via the
`code` element (or equivalent) on the detail resource. As well, the "name" or
"title" on the detail resource generally corresponds with the display name on the matching
code. Most detail resources will also have an "identifier" element. This *can* be
set to the same value and namespace as the code, but if the only identifier a resource has
is its defining code, it may be better to omit the identifier entirely. .

## 4.8.16 Search Parameters

Search parameters for this resource. The [common parameters](search.html#all) also apply. See [Searching](search.html) for more information about searching in REST, messaging, and services.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Name** | **Type** | **Description** | **Expression** | **In Common** |
| code [TU](versions.html#std-process "Trial Use Content") | [token](search.html#token) | A code defined in the code system | CodeSystem.concept.code |  |
| content-mode [TU](versions.html#std-process "Trial Use Content") | [token](search.html#token) | not-present | example | fragment | complete | supplement | CodeSystem.content |  |
| context [TU](versions.html#std-process "Trial Use Content") | [token](search.html#token) | A use context assigned to the code system | (CodeSystem.useContext.value as CodeableConcept) |  |
| context-quantity [TU](versions.html#std-process "Trial Use Content") | [quantity](search.html#quantity) | A quantity- or range-valued use context assigned to the code system | (CodeSystem.useContext.value as Quantity) | (CodeSystem.useContext.value as Range) |  |
| context-type [TU](versions.html#std-process "Trial Use Content") | [token](search.html#token) | A type of use context assigned to the code system | CodeSystem.useContext.code |  |
| context-type-quantity [TU](versions.html#std-process "Trial Use Content") | [composite](search.html#composite) | A use context type and quantity- or range-based value assigned to the code system | On CodeSystem.useContext:   context-type: code   context-quantity: value.as(Quantity) | value.as(Range) |  |
| context-type-value [TU](versions.html#std-process "Trial Use Content") | [composite](search.html#composite) | A use context type and value assigned to the code system | On CodeSystem.useContext:   context-type: code   context: value.as(CodeableConcept) |  |
| date [TU](versions.html#std-process "Trial Use Content") | [date](search.html#date) | The code system publication date | CodeSystem.date |  |
| description [TU](versions.html#std-process "Trial Use Content") | [string](search.html#string) | The description of the code system | CodeSystem.description |  |
| identifier [TU](versions.html#std-process "Trial Use Content") | [token](search.html#token) | External identifier for the code system | CodeSystem.identifier |  |
| jurisdiction [TU](versions.html#std-process "Trial Use Content") | [token](search.html#token) | Intended jurisdiction for the code system | CodeSystem.jurisdiction |  |
| language [TU](versions.html#std-process "Trial Use Content") | [token](search.html#token) | A language in which a designation is provided | CodeSystem.concept.designation.language |  |
| name [TU](versions.html#std-process "Trial Use Content") | [string](search.html#string) | Computationally friendly name of the code system | CodeSystem.name |  |
| publisher [TU](versions.html#std-process "Trial Use Content") | [string](search.html#string) | Name of the publisher of the code system | CodeSystem.publisher |  |
| status [TU](versions.html#std-process "Trial Use Content") | [token](search.html#token) | The current status of the code system | CodeSystem.status |  |
| supplements [TU](versions.html#std-process "Trial Use Content") | [reference](search.html#reference) | Find code system supplements for the referenced code system | CodeSystem.supplements ([CodeSystem](codesystem.html)) |  |
| system [TU](versions.html#std-process "Trial Use Content") | [uri](search.html#uri) | The system for any codes defined by this code system (same as 'url') | CodeSystem.url |  |
| title [TU](versions.html#std-process "Trial Use Content") | [string](search.html#string) | The human-friendly name of the code system | CodeSystem.title |  |
| url [TU](versions.html#std-process "Trial Use Content") | [uri](search.html#uri) | The uri that identifies the code system | CodeSystem.url |  |
| version [TU](versions.html#std-process "Trial Use Content") | [token](search.html#token) | The business version of the code system | CodeSystem.version |  |

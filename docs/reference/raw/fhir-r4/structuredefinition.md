---
id: structuredefinition
title: StructureDefinition
source_url: https://hl7.org/fhir/R4/structuredefinition.html
group: fhir-r4
fhir_version: R4
fetched_at: '2026-09-11T13:23:19Z'
sha256: 6d6d7906bff0896b25b6192235a7d0af46b490730fc124baecf354cb735b7cc6
---
This page is part of the FHIR Specification (v4.0.1: R4 - Mixed [Normative](https://confluence.hl7.org/display/HL7/HL7+Balloting "Normative Standard") and [STU](https://confluence.hl7.org/display/HL7/HL7+Balloting "Standard for Trial-Use")) in it's permanent home (it will always be available at this URL). The current version which supercedes this version is [5.0.0](http://hl7.org/fhir/index.html). For a full list of available versions, see the [Directory of published versions ![](external.png)](http://hl7.org/fhir/directory.html). Page versions: [R5](http://hl7.org/fhir/R5/structuredefinition.html) [R4B](http://hl7.org/fhir/R4B/structuredefinition.html) **R4** [R3](http://hl7.org/fhir/STU3/structuredefinition.html) [R2](http://hl7.org/fhir/DSTU2/structuredefinition.html)

- [Content](#)
- [Examples](structuredefinition-examples.html)
- [Detailed Descriptions](structuredefinition-definitions.html)
- [Mappings](structuredefinition-mappings.html)
- [Profiles & Extensions](structuredefinition-profiles.html)
- [Operations](structuredefinition-operations.html)
- [R3 Conversions](structuredefinition-version-maps.html)

# 5.3 Resource StructureDefinition - Content

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [FHIR Infrastructure](http://www.hl7.org/Special/committees/fiwg/index.cfm)  Work Group | [Maturity Level](versions.html#maturity): [N](versions.html#std-process) | [Normative](versions.html#std-process "Standard Status") (from v4.0.0) | [Security Category](security.html#SecPrivConsiderations): Anonymous | [Compartments](compartmentdefinition.html): Not linked to any defined compartments |

|  |  |
| --- | --- |
|  | This page has been approved as part of an [ANSI](https://www.ansi.org/)  standard. See the [Conformance](ansi-conformance.html) Package for further details. |

A definition of a FHIR structure. This resource is used to describe the underlying resources, data types defined in FHIR, and also for describing extensions and constraints on resources and data types.

## 5.3.1 Scope and Usage

The StructureDefinition resource describes a structure - a set of data element definitions, and their associated rules of usage.
These structure definitions are used to describe both the content defined in the FHIR specification
itself - Resources, data types, the underlying infrastructural types, and also are used to describe how
these structures are used in implementations.
This allows the definitions of the structures to be shared and published through
repositories of structure definitions, compared with each other, and used as the basis
for code, report and UI generation.

Note that as part of the specification itself, a [full
set of structure definitions](downloads.html#profiles) for all resources and data types is published.

## 5.3.2 Boundaries and Relationships

- StructureDefinitions are used by [CapabilityStatement](capabilitystatement.html) instances for specifying how resources are used
- StructureDefinitions use [Value Sets](valueset.html) to specify the content of coded elements

## 5.3.3 Background and Context

Implementers should be familiar with the
background and concepts described in [Profiling FHIR](profiling.html)
before working with this resource.

### 5.3.3.1 Metadata

The StructureDefinition resource has a set of metadata that is mostly shared with the [Value Set](valueset.html),
[CapabilityStatement](capabilitystatement.html) and other infrastructure resources. The metadata describes the structure and helps
find the structure when registered in repositories.

|  |  |
| --- | --- |
| url | The identifier that is used to identify this structure when it is referenced in a specification, model, design or an instance. This URL is where the structure can be accessed |
| identifier | Other identifiers that are used to identify this structure |
| version | The identifier that is used to identify this version of the structure when it is referenced in a specification, model, design or instance. This is an arbitrary value managed by the structure author manually and the value should be a timestamp.  Note that there may be multiple resource versions of the structure that have this same identifier. The resource will have updates that create new versions for technical reasons, whereas the stated version number needs to be under the author's control |
| name | A Computer-ready name (e.g. a token) that identifies the structure - suitable for code generation. Note that this name (and other names relevant for code generation, including element & slice names, codes etc) may collide with reserved words in the relevant target language, and code generators will need to handle this |
| title | A free text natural language name identifying the structure |
| status | The status of the structure allows filtering of StructureDefinitions that are appropriate for use vs. not. See the [Status Codes](valueset-publication-status.html) |
| experimental | This structure was authored for testing purposes (or education/evaluation/marketing), and is not intended for genuine usage |
| date | The date this version of the structure was published |
| publisher | Details of the individual or organization who accepts responsibility for publishing the structure. This helps establish the "authority/credibility" of the structure. |
| contact | Contact details to assist a user in finding and communicating with the publisher |
| description | A free text natural language description of the structure and its use |
| purpose | Why this structure was created - what the intent of it is |
| useContext & Jurisdiction | Computable details about purpose and scope of use |
| keyword | A set of terms from external terminologies that may be used to assist with indexing and searching of StructureDefinitionss |
| copyright | Use and/or publishing restrictions |
| fhirVersion | The version of the FHIR specification on which this structure is based. It is not necessary to specify the version, as most SructureDefinitions are valid across multiple versions, and the validity of a structure against a particular version of FHIR can easily be checked by tooling. |
| type | The type the structure describes. |
| contextType & context | For extensions, the types of contexts in which the extension can be used. For further details, see [Defining Extensions](defining-extensions.html) |

Notes:

- The name and title of the structure are not required to be globally unique, but the name amd title should have some scoping information (e.g. AcmeAllergies / Acme Inc. (USA), Allergy List)
- Multiple keywords may be assigned to the structure. These may either describe the structure, the focus of the structure or both. They are solely to help find the structure by searching for structured concepts
- The 3 status codes (draft, active, and retired) are the codes that are relevant to structure consumers. Authors may wish to use the [authoring-status](#author-status) extension to track the life cycle of a structure as it is prepared

This resource is referenced by [DataRequirement](metadatatypes.html#DataRequirement), [ElementDefinition](elementdefinition.html#ElementDefinition), [Meta](resource.html#Meta), [ParameterDefinition](metadatatypes.html#ParameterDefinition), [ActivityDefinition](activitydefinition.html#ActivityDefinition), [CapabilityStatement](capabilitystatement.html#CapabilityStatement), [GraphDefinition](graphdefinition.html#GraphDefinition), [ImplementationGuide](implementationguide.html#ImplementationGuide), [MessageDefinition](messagedefinition.html#MessageDefinition), [OperationDefinition](operationdefinition.html#OperationDefinition), itself and [StructureMap](structuremap.html#StructureMap)

## 5.3.4 Resource Content

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
| .. [StructureDefinition](structuredefinition-definitions.html#StructureDefinition "StructureDefinition : A definition of a FHIR structure. This resource is used to describe the underlying resources, data types defined in FHIR, and also for describing extensions and constraints on resources and data types.") | [I](conformance-rules.html#constraints "This element has or is affected by some invariants")[N](versions.html#std-process "Standards Status = Normative") |  | [DomainResource](domainresource.html) | Structural Definition + Warning: Name should be usable as an identifier for the module by machine processing applications such as code generation + Rule: Element paths must be unique unless the structure is a constraint + Rule: If the first element in a differential has no "." in the path and it's not a logical model, it has no type + Rule: If the structure is not abstract, then there SHALL be a baseDefinition + Rule: If the structure defines an extension then the structure must have context information + Rule: A structure must have either a differential, or a snapshot (or both) + Rule: In any snapshot or differential, no label, code or requirements on an element without a "." in the path (e.g. the first element) + Rule: If there's a type, its content must match the path name in the first element of a snapshot + Rule: All element definitions must have an id + Rule: The first element in a snapshot has no type unless model is a logical model. + Rule: All element definitions must have unique ids (snapshot) + Rule: All element definitions must have unique ids (diff) + Rule: Context Invariants can only be used for extensions + Rule: FHIR Specification models only use FHIR defined types + Rule: Default values can only be specified on specializations + Rule: FHIR Specification models never have default values + Rule: No slice name on root Elements defined in Ancestors: [id](resource.html#Resource "The logical id of the resource, as used in the URL for the resource. Once assigned, this value never changes."), [meta](resource.html#Resource "The metadata about the resource. This is content that is maintained by the infrastructure. Changes to the content might not always be associated with version changes to the resource."), [implicitRules](resource.html#Resource "A reference to a set of rules that were followed when the resource was constructed, and which must be understood when processing the content. Often, this is a reference to an implementation guide that defines the special rules along with other profiles etc."), [language](resource.html#Resource "The base language in which the resource is written."), [text](domainresource.html#DomainResource "A human-readable narrative that contains a summary of the resource and can be used to represent the content of the resource to a human. The narrative need not encode all the structured data, but is required to contain sufficient detail to make it \"clinically safe\" for a human to just read the narrative. Resource definitions may define what content should be represented in the narrative to ensure clinical safety."), [contained](domainresource.html#DomainResource "These resources do not have an independent existence apart from the resource that contains them - they cannot be identified independently, and nor can they have their own independent transaction scope."), [extension](domainresource.html#DomainResource "May be used to represent additional information that is not part of the basic definition of the resource. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension."), [modifierExtension](domainresource.html#DomainResource "May be used to represent additional information that is not part of the basic definition of the resource and that modifies the understanding of the element that contains it and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer is allowed to define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.  Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).") |
| ... [url](structuredefinition-definitions.html#StructureDefinition.url "StructureDefinition.url : An absolute URI that is used to identify this structure definition when it is referenced in a specification, model, design or an instance; also called its canonical identifier. This SHOULD be globally unique and SHOULD be a literal address at which at which an authoritative instance of this structure definition is (or will be) published. This URL can be the target of a canonical reference. It SHALL remain the same when the structure definition is stored on different servers.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [uri](datatypes.html#uri) | Canonical identifier for this structure definition, represented as a URI (globally unique) |
| ... [identifier](structuredefinition-definitions.html#StructureDefinition.identifier "StructureDefinition.identifier : A formal identifier that is used to identify this structure definition when it is represented in other formats, or referenced in a specification, model, design or an instance.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [Identifier](datatypes.html#Identifier) | Additional identifier for the structure definition |
| ... [version](structuredefinition-definitions.html#StructureDefinition.version "StructureDefinition.version : The identifier that is used to identify this version of the structure definition when it is referenced in a specification, model, design or instance. This is an arbitrary value managed by the structure definition author and is not expected to be globally unique. For example, it might be a timestamp (e.g. yyyymmdd) if a managed version is not available. There is also no expectation that versions can be placed in a lexicographical sequence.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | Business version of the structure definition |
| ... [name](structuredefinition-definitions.html#StructureDefinition.name "StructureDefinition.name : A natural language name identifying the structure definition. This name should be usable as an identifier for the module by machine processing applications such as code generation.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 1..1 | [string](datatypes.html#string) | Name for this structure definition (computer friendly) |
| ... [title](structuredefinition-definitions.html#StructureDefinition.title "StructureDefinition.title : A short, descriptive, user-friendly title for the structure definition.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | Name for this structure definition (human friendly) |
| ... [status](structuredefinition-definitions.html#StructureDefinition.status "StructureDefinition.status : The status of this structure definition. Enables tracking the life-cycle of the content.") | [?!](conformance-rules.html#isModifier "This element is a modifier element")[Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [code](datatypes.html#code) | draft | active | retired | unknown [PublicationStatus](valueset-publication-status.html "The lifecycle status of an artifact.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ... [experimental](structuredefinition-definitions.html#StructureDefinition.experimental "StructureDefinition.experimental : A Boolean value to indicate that this structure definition is authored for testing purposes (or education/evaluation/marketing) and is not intended to be used for genuine usage.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [boolean](datatypes.html#boolean) | For testing purposes, not real usage |
| ... [date](structuredefinition-definitions.html#StructureDefinition.date "StructureDefinition.date : The date  (and optionally time) when the structure definition was published. The date must change when the business version changes and it must change if the status code changes. In addition, it should change when the substantive content of the structure definition changes.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [dateTime](datatypes.html#dateTime) | Date last changed |
| ... [publisher](structuredefinition-definitions.html#StructureDefinition.publisher "StructureDefinition.publisher : The name of the organization or individual that published the structure definition.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | Name of the publisher (organization or individual) |
| ... [contact](structuredefinition-definitions.html#StructureDefinition.contact "StructureDefinition.contact : Contact details to assist a user in finding and communicating with the publisher.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [ContactDetail](metadatatypes.html#ContactDetail) | Contact details for the publisher |
| ... [description](structuredefinition-definitions.html#StructureDefinition.description "StructureDefinition.description : A free text natural language description of the structure definition from a consumer's perspective.") |  | 0..1 | [markdown](datatypes.html#markdown) | Natural language description of the structure definition |
| ... [useContext](structuredefinition-definitions.html#StructureDefinition.useContext "StructureDefinition.useContext : The content was developed with a focus and intent of supporting the contexts that are listed. These contexts may be general categories (gender, age, ...) or may be references to specific programs (insurance plans, studies, ...) and may be used to assist with indexing and searching for appropriate structure definition instances.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[TU](versions.html#std-process "Standards Status = Trial Use") | 0..\* | [UsageContext](metadatatypes.html#UsageContext) | The context that the content is intended to support |
| ... [jurisdiction](structuredefinition-definitions.html#StructureDefinition.jurisdiction "StructureDefinition.jurisdiction : A legal or geographic region in which the structure definition is intended to be used.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [CodeableConcept](datatypes.html#CodeableConcept) | Intended jurisdiction for structure definition (if applicable) [Jurisdiction](valueset-jurisdiction.html "Countries and regions within which this artifact is targeted for use.") ([Extensible](terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept (based on human review), alternate codings (or, data type allowing, text) may be included instead.")) |
| ... [purpose](structuredefinition-definitions.html#StructureDefinition.purpose "StructureDefinition.purpose : Explanation of why this structure definition is needed and why it has been designed as it has.") |  | 0..1 | [markdown](datatypes.html#markdown) | Why this structure definition is defined |
| ... [copyright](structuredefinition-definitions.html#StructureDefinition.copyright "StructureDefinition.copyright : A copyright statement relating to the structure definition and/or its contents. Copyright statements are generally legal restrictions on the use and publishing of the structure definition.") |  | 0..1 | [markdown](datatypes.html#markdown) | Use and/or publishing restrictions |
| ... [keyword](structuredefinition-definitions.html#StructureDefinition.keyword "StructureDefinition.keyword : A set of key words or terms from external terminologies that may be used to assist with indexing and searching of templates nby describing the use of this structure definition, or the content it describes.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [Coding](datatypes.html#Coding) | Assist with indexing and finding [Structure Definition Use Codes / Keywords](valueset-definition-use.html "Codes for the meaning of the defined structure (SNOMED CT and LOINC codes, as an example).") ([Extensible](terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept (based on human review), alternate codings (or, data type allowing, text) may be included instead.")) |
| ... [fhirVersion](structuredefinition-definitions.html#StructureDefinition.fhirVersion "StructureDefinition.fhirVersion : The version of the FHIR specification on which this StructureDefinition is based - this is the formal version of the specification, without the revision number, e.g. [publication].[major].[minor], which is 4.0.1. for this version.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [code](datatypes.html#code) | FHIR Version this StructureDefinition targets [FHIRVersion](valueset-FHIR-version.html "All published FHIR Versions.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ... [mapping](structuredefinition-definitions.html#StructureDefinition.mapping "StructureDefinition.mapping : An external specification that the content is mapped to.") | [I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..\* | [BackboneElement](backboneelement.html) | External specification that the content is mapped to + Rule: Must have at least a name or a uri (or both) |
| .... [identity](structuredefinition-definitions.html#StructureDefinition.mapping.identity "StructureDefinition.mapping.identity : An Internal id that is used to identify this mapping set when specific mappings are made.") |  | 1..1 | [id](datatypes.html#id) | Internal id when this mapping is used |
| .... [uri](structuredefinition-definitions.html#StructureDefinition.mapping.uri "StructureDefinition.mapping.uri : An absolute URI that identifies the specification that this mapping is expressed to.") | [I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..1 | [uri](datatypes.html#uri) | Identifies what this mapping refers to |
| .... [name](structuredefinition-definitions.html#StructureDefinition.mapping.name "StructureDefinition.mapping.name : A name for the specification that is being mapped to.") | [I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..1 | [string](datatypes.html#string) | Names what this mapping refers to |
| .... [comment](structuredefinition-definitions.html#StructureDefinition.mapping.comment "StructureDefinition.mapping.comment : Comments about this mapping, including version notes, issues, scope limitations, and other important notes for usage.") |  | 0..1 | [string](datatypes.html#string) | Versions, Issues, Scope limitations etc. |
| ... [kind](structuredefinition-definitions.html#StructureDefinition.kind "StructureDefinition.kind : Defines the kind of structure that this definition is describing.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [code](datatypes.html#code) | primitive-type | complex-type | resource | logical [StructureDefinitionKind](valueset-structure-definition-kind.html "Defines the type of structure that a definition is describing.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ... [abstract](structuredefinition-definitions.html#StructureDefinition.abstract "StructureDefinition.abstract : Whether structure this definition describes is abstract or not  - that is, whether the structure is not intended to be instantiated. For Resources and Data types, abstract types will never be exchanged  between systems.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [boolean](datatypes.html#boolean) | Whether the structure is abstract |
| ... [context](structuredefinition-definitions.html#StructureDefinition.context "StructureDefinition.context : Identifies the types of resource or data type elements to which the extension can be applied.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..\* | [BackboneElement](backboneelement.html) | If an extension, where it can be used in instances |
| .... [type](structuredefinition-definitions.html#StructureDefinition.context.type "StructureDefinition.context.type : Defines how to interpret the expression that defines what the context of the extension is.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [code](datatypes.html#code) | fhirpath | element | extension [ExtensionContextType](valueset-extension-context-type.html "How an extension context is interpreted.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| .... [expression](structuredefinition-definitions.html#StructureDefinition.context.expression "StructureDefinition.context.expression : An expression that defines where an extension can be used in resources.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [string](datatypes.html#string) | Where the extension can be used in instances |
| ... [contextInvariant](structuredefinition-definitions.html#StructureDefinition.contextInvariant "StructureDefinition.contextInvariant : A set of rules as FHIRPath Invariants about when the extension can be used (e.g. co-occurrence variants for the extension). All the rules must be true.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..\* | [string](datatypes.html#string) | FHIRPath invariants - when the extension can be used |
| ... [type](structuredefinition-definitions.html#StructureDefinition.type "StructureDefinition.type : The type this structure describes. If the derivation kind is 'specialization' then this is the master definition for a type, and there is always one of these (a data type, an extension, a resource, including abstract ones). Otherwise the structure definition is a constraint on the stated type (and in this case, the type cannot be an abstract type).  References are URLs that are relative to http://hl7.org/fhir/StructureDefinition e.g. \"string\" is a reference to http://hl7.org/fhir/StructureDefinition/string. Absolute URLs are only allowed in logical models.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 1..1 | [uri](datatypes.html#uri) | Type defined or constrained by this structure [FHIRDefinedType](valueset-defined-types.html "Either a resource or a data type, including logical model types.") ([Extensible](terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept (based on human review), alternate codings (or, data type allowing, text) may be included instead.")) |
| ... [baseDefinition](structuredefinition-definitions.html#StructureDefinition.baseDefinition "StructureDefinition.baseDefinition : An absolute URI that is the base structure from which this type is derived, either by specialization or constraint.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..1 | [canonical](datatypes.html#canonical)([StructureDefinition](structuredefinition.html)) | Definition that this type is constrained/specialized from |
| ... [derivation](structuredefinition-definitions.html#StructureDefinition.derivation "StructureDefinition.derivation : How the type relates to the baseDefinition.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [code](datatypes.html#code) | specialization | constraint - How relates to base definition [TypeDerivationRule](valueset-type-derivation-rule.html "How a type relates to its baseDefinition.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ... [snapshot](structuredefinition-definitions.html#StructureDefinition.snapshot "StructureDefinition.snapshot : A snapshot view is expressed in a standalone form that can be used and interpreted without considering the base StructureDefinition.") | [I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..1 | [BackboneElement](backboneelement.html) | Snapshot view of the structure + Rule: Each element definition in a snapshot must have a formal definition and cardinalities + Rule: All snapshot elements must start with the StructureDefinition's specified type for non-logical models, or with the same type name for logical models + Rule: All snapshot elements must have a base definition |
| .... [element](structuredefinition-definitions.html#StructureDefinition.snapshot.element "StructureDefinition.snapshot.element : Captures constraints on each element within the resource.") | [I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 1..\* | [ElementDefinition](elementdefinition.html#ElementDefinition) | Definition of elements in the resource (if no StructureDefinition) + Rule: provide either a binding reference or a description (or both) |
| ... [differential](structuredefinition-definitions.html#StructureDefinition.differential "StructureDefinition.differential : A differential view is expressed relative to the base StructureDefinition - a statement of differences that it applies.") | [I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..1 | [BackboneElement](backboneelement.html) | Differential view of the structure + Rule: No slicing on the root element + Rule: In any differential, all the elements must start with the StructureDefinition's specified type for non-logical models, or with the same type name for logical models |
| .... [element](structuredefinition-definitions.html#StructureDefinition.differential.element "StructureDefinition.differential.element : Captures constraints on each element within the resource.") |  | 1..\* | [ElementDefinition](elementdefinition.html#ElementDefinition) | Definition of elements in the resource (if no StructureDefinition) |
| [doco Documentation for this format](formats.html#table "Legend for this format") | | | | |

**UML Diagram** ([Legend](formats.html#uml))

**XML Template**

```

<StructureDefinition xmlns="http://hl7.org/fhir"> ![doco](help.png)
 <!-- from Resource: id, meta, implicitRules, and language -->
 <!-- from DomainResource: text, contained, extension, and modifierExtension -->
 <url value="[uri]"/><!-- 1..1 Canonical identifier for this structure definition, represented as a URI (globally unique) -->
 <identifier><!-- 0..* Identifier Additional identifier for the structure definition --></identifier>
 <version value="[string]"/><!-- 0..1 Business version of the structure definition -->
 <name value="[string]"/><!-- ![??](lock.png) 1..1 Name for this structure definition (computer friendly) -->
 <title value="[string]"/><!-- 0..1 Name for this structure definition (human friendly) -->
 <status value="[code]"/><!-- 1..1 draft | active | retired | unknown -->
 <experimental value="[boolean]"/><!-- 0..1 For testing purposes, not real usage -->
 <date value="[dateTime]"/><!-- 0..1 Date last changed -->
 <publisher value="[string]"/><!-- 0..1 Name of the publisher (organization or individual) -->
 <contact><!-- 0..* ContactDetail Contact details for the publisher --></contact>
 <description value="[markdown]"/><!-- 0..1 Natural language description of the structure definition -->
 <useContext><!-- 0..* UsageContext The context that the content is intended to support --></useContext>
 <jurisdiction><!-- 0..* CodeableConcept Intended jurisdiction for structure definition (if applicable) --></jurisdiction>
 <purpose value="[markdown]"/><!-- 0..1 Why this structure definition is defined -->
 <copyright value="[markdown]"/><!-- 0..1 Use and/or publishing restrictions -->
 <keyword><!-- 0..* Coding Assist with indexing and finding --></keyword>
 <fhirVersion value="[code]"/><!-- 0..1 FHIR Version this StructureDefinition targets -->
 <mapping>  <!-- 0..* External specification that the content is mapped to -->
  <identity value="[id]"/><!-- 1..1 Internal id when this mapping is used -->
  <uri value="[uri]"/><!-- ![??](lock.png) 0..1 Identifies what this mapping refers to -->
  <name value="[string]"/><!-- ![??](lock.png) 0..1 Names what this mapping refers to -->
  <comment value="[string]"/><!-- 0..1 Versions, Issues, Scope limitations etc. -->
 </mapping>
 <kind value="[code]"/><!-- 1..1 primitive-type | complex-type | resource | logical -->
 <abstract value="[boolean]"/><!-- 1..1 Whether the structure is abstract -->
 <context>  <!-- ![??](lock.png) 0..* If an extension, where it can be used in instances -->
  <type value="[code]"/><!-- 1..1 fhirpath | element | extension -->
  <expression value="[string]"/><!-- 1..1 Where the extension can be used in instances -->
 </context>
 <contextInvariant value="[string]"/><!-- ![??](lock.png) 0..* FHIRPath invariants - when the extension can be used -->
 <type value="[uri]"/><!-- ![??](lock.png) 1..1 Type defined or constrained by this structure -->
 <baseDefinition><!-- ![??](lock.png) 0..1 canonical(StructureDefinition) Definition that this type is constrained/specialized from --></baseDefinition>
 <derivation value="[code]"/><!-- 0..1 specialization | constraint - How relates to base definition -->
 <snapshot>  <!-- ![??](lock.png) 0..1 Snapshot view of the structure -->
  <element><!-- ![??](lock.png) 1..* ElementDefinition Definition of elements in the resource (if no StructureDefinition) --></element>
 </snapshot>
 <differential>  <!-- ![??](lock.png) 0..1 Differential view of the structure -->
  <element><!-- 1..* ElementDefinition Definition of elements in the resource (if no StructureDefinition) --></element>
 </differential>
</StructureDefinition>
```

**JSON Template**

```

{![doco](help.png)
  "resourceType" : "StructureDefinition",
  // from Resource: id, meta, implicitRules, and language
  // from DomainResource: text, contained, extension, and modifierExtension
  "url" : "<uri>", // R!  Canonical identifier for this structure definition, represented as a URI (globally unique)
  "identifier" : [{ Identifier }], // Additional identifier for the structure definition
  "version" : "<string>", // Business version of the structure definition
  "name" : "<string>", // C? R!  Name for this structure definition (computer friendly)
  "title" : "<string>", // Name for this structure definition (human friendly)
  "status" : "<code>", // R!  draft | active | retired | unknown
  "experimental" : <boolean>, // For testing purposes, not real usage
  "date" : "<dateTime>", // Date last changed
  "publisher" : "<string>", // Name of the publisher (organization or individual)
  "contact" : [{ ContactDetail }], // Contact details for the publisher
  "description" : "<markdown>", // Natural language description of the structure definition
  "useContext" : [{ UsageContext }], // The context that the content is intended to support
  "jurisdiction" : [{ CodeableConcept }], // Intended jurisdiction for structure definition (if applicable)
  "purpose" : "<markdown>", // Why this structure definition is defined
  "copyright" : "<markdown>", // Use and/or publishing restrictions
  "keyword" : [{ Coding }], // Assist with indexing and finding
  "fhirVersion" : "<code>", // FHIR Version this StructureDefinition targets
  "mapping" : [{ // External specification that the content is mapped to
    "identity" : "<id>", // R!  Internal id when this mapping is used
    "uri" : "<uri>", // C? Identifies what this mapping refers to
    "name" : "<string>", // C? Names what this mapping refers to
    "comment" : "<string>" // Versions, Issues, Scope limitations etc.
  }],
  "kind" : "<code>", // R!  primitive-type | complex-type | resource | logical
  "abstract" : <boolean>, // R!  Whether the structure is abstract
  "context" : [{ // C? If an extension, where it can be used in instances
    "type" : "<code>", // R!  fhirpath | element | extension
    "expression" : "<string>" // R!  Where the extension can be used in instances
  }],
  "contextInvariant" : ["<string>"], // C? FHIRPath invariants - when the extension can be used
  "type" : "<uri>", // C? R!  Type defined or constrained by this structure
  "baseDefinition" : { canonical(StructureDefinition) }, // C? Definition that this type is constrained/specialized from
  "derivation" : "<code>", // specialization | constraint - How relates to base definition
  "snapshot" : { // C? Snapshot view of the structure
    "element" : [{ ElementDefinition }] // C? R!  Definition of elements in the resource (if no StructureDefinition)
  },
  "differential" : { // C? Differential view of the structure
    "element" : [{ ElementDefinition }] // R!  Definition of elements in the resource (if no StructureDefinition)
  }
}
```

**Turtle Template**

```

@prefix fhir: <http://hl7.org/fhir/> .![doco](help.png)


[ a fhir:StructureDefinition;
  fhir:nodeRole fhir:treeRoot; # if this is the parser root

  # from Resource: .id, .meta, .implicitRules, and .language
  # from DomainResource: .text, .contained, .extension, and .modifierExtension
  fhir:StructureDefinition.url [ uri ]; # 1..1 Canonical identifier for this structure definition, represented as a URI (globally unique)
  fhir:StructureDefinition.identifier [ Identifier ], ... ; # 0..* Additional identifier for the structure definition
  fhir:StructureDefinition.version [ string ]; # 0..1 Business version of the structure definition
  fhir:StructureDefinition.name [ string ]; # 1..1 Name for this structure definition (computer friendly)
  fhir:StructureDefinition.title [ string ]; # 0..1 Name for this structure definition (human friendly)
  fhir:StructureDefinition.status [ code ]; # 1..1 draft | active | retired | unknown
  fhir:StructureDefinition.experimental [ boolean ]; # 0..1 For testing purposes, not real usage
  fhir:StructureDefinition.date [ dateTime ]; # 0..1 Date last changed
  fhir:StructureDefinition.publisher [ string ]; # 0..1 Name of the publisher (organization or individual)
  fhir:StructureDefinition.contact [ ContactDetail ], ... ; # 0..* Contact details for the publisher
  fhir:StructureDefinition.description [ markdown ]; # 0..1 Natural language description of the structure definition
  fhir:StructureDefinition.useContext [ UsageContext ], ... ; # 0..* The context that the content is intended to support
  fhir:StructureDefinition.jurisdiction [ CodeableConcept ], ... ; # 0..* Intended jurisdiction for structure definition (if applicable)
  fhir:StructureDefinition.purpose [ markdown ]; # 0..1 Why this structure definition is defined
  fhir:StructureDefinition.copyright [ markdown ]; # 0..1 Use and/or publishing restrictions
  fhir:StructureDefinition.keyword [ Coding ], ... ; # 0..* Assist with indexing and finding
  fhir:StructureDefinition.fhirVersion [ code ]; # 0..1 FHIR Version this StructureDefinition targets
  fhir:StructureDefinition.mapping [ # 0..* External specification that the content is mapped to
    fhir:StructureDefinition.mapping.identity [ id ]; # 1..1 Internal id when this mapping is used
    fhir:StructureDefinition.mapping.uri [ uri ]; # 0..1 Identifies what this mapping refers to
    fhir:StructureDefinition.mapping.name [ string ]; # 0..1 Names what this mapping refers to
    fhir:StructureDefinition.mapping.comment [ string ]; # 0..1 Versions, Issues, Scope limitations etc.
  ], ...;
  fhir:StructureDefinition.kind [ code ]; # 1..1 primitive-type | complex-type | resource | logical
  fhir:StructureDefinition.abstract [ boolean ]; # 1..1 Whether the structure is abstract
  fhir:StructureDefinition.context [ # 0..* If an extension, where it can be used in instances
    fhir:StructureDefinition.context.type [ code ]; # 1..1 fhirpath | element | extension
    fhir:StructureDefinition.context.expression [ string ]; # 1..1 Where the extension can be used in instances
  ], ...;
  fhir:StructureDefinition.contextInvariant [ string ], ... ; # 0..* FHIRPath invariants - when the extension can be used
  fhir:StructureDefinition.type [ uri ]; # 1..1 Type defined or constrained by this structure
  fhir:StructureDefinition.baseDefinition [ canonical(StructureDefinition) ]; # 0..1 Definition that this type is constrained/specialized from
  fhir:StructureDefinition.derivation [ code ]; # 0..1 specialization | constraint - How relates to base definition
  fhir:StructureDefinition.snapshot [ # 0..1 Snapshot view of the structure
    fhir:StructureDefinition.snapshot.element [ ElementDefinition ], ... ; # 1..* Definition of elements in the resource (if no StructureDefinition)
  ];
  fhir:StructureDefinition.differential [ # 0..1 Differential view of the structure
    fhir:StructureDefinition.differential.element [ ElementDefinition ], ... ; # 1..* Definition of elements in the resource (if no StructureDefinition)
  ];
]
```

**Changes since R3**

|  |  |
| --- | --- |
| [StructureDefinition](structuredefinition.html#StructureDefinition) |  |
| StructureDefinition.status | - Change value set from http://hl7.org/fhir/ValueSet/publication-status to http://hl7.org/fhir/ValueSet/publication-status|4.0.1 |
| StructureDefinition.experimental | - No longer marked as Modifier |
| StructureDefinition.keyword | - Add Binding `http://hl7.org/fhir/ValueSet/definition-use` (extensible) |
| StructureDefinition.fhirVersion | - Type changed from id to code - Add Binding `http://hl7.org/fhir/ValueSet/FHIR-version|4.0.1` (required) |
| StructureDefinition.kind | - Change value set from http://hl7.org/fhir/ValueSet/structure-definition-kind to http://hl7.org/fhir/ValueSet/structure-definition-kind|4.0.1 |
| StructureDefinition.context | - Type changed from string to BackboneElement |
| StructureDefinition.context.type | - **Added Mandatory Element** |
| StructureDefinition.context.expression | - **Added Mandatory Element** |
| StructureDefinition.type | - Type changed from code to uri |
| StructureDefinition.baseDefinition | - Type changed from uri to canonical(StructureDefinition) |
| StructureDefinition.derivation | - Change value set from http://hl7.org/fhir/ValueSet/type-derivation-rule to http://hl7.org/fhir/ValueSet/type-derivation-rule|4.0.1 |
| StructureDefinition.contextType | - deleted |

See the [Full Difference](diff.html) for further information

This analysis is available as [XML](structuredefinition.diff.xml) or [JSON](structuredefinition.diff.json).

See [R3 <--> R4 Conversion Maps](structuredefinition-version-maps.html) (status = 206 tests that all execute ok. 4 fail round-trip testing and 206 r3 resources are invalid (0 errors).)

**Structure**

| [Name](formats.html#table "The logical name of the element") | [Flags](formats.html#table "Information about the use of the element") | [Card.](formats.html#table "Minimum and Maximum # of times the the element can appear in the instance") | [Type](formats.html#table "Reference to the type of the element") | [Description & Constraints](formats.html#table "Additional information about the element")[doco](formats.html#table "Legend for this format") |
| --- | --- | --- | --- | --- |
| .. [StructureDefinition](structuredefinition-definitions.html#StructureDefinition "StructureDefinition : A definition of a FHIR structure. This resource is used to describe the underlying resources, data types defined in FHIR, and also for describing extensions and constraints on resources and data types.") | [I](conformance-rules.html#constraints "This element has or is affected by some invariants")[N](versions.html#std-process "Standards Status = Normative") |  | [DomainResource](domainresource.html) | Structural Definition + Warning: Name should be usable as an identifier for the module by machine processing applications such as code generation + Rule: Element paths must be unique unless the structure is a constraint + Rule: If the first element in a differential has no "." in the path and it's not a logical model, it has no type + Rule: If the structure is not abstract, then there SHALL be a baseDefinition + Rule: If the structure defines an extension then the structure must have context information + Rule: A structure must have either a differential, or a snapshot (or both) + Rule: In any snapshot or differential, no label, code or requirements on an element without a "." in the path (e.g. the first element) + Rule: If there's a type, its content must match the path name in the first element of a snapshot + Rule: All element definitions must have an id + Rule: The first element in a snapshot has no type unless model is a logical model. + Rule: All element definitions must have unique ids (snapshot) + Rule: All element definitions must have unique ids (diff) + Rule: Context Invariants can only be used for extensions + Rule: FHIR Specification models only use FHIR defined types + Rule: Default values can only be specified on specializations + Rule: FHIR Specification models never have default values + Rule: No slice name on root Elements defined in Ancestors: [id](resource.html#Resource "The logical id of the resource, as used in the URL for the resource. Once assigned, this value never changes."), [meta](resource.html#Resource "The metadata about the resource. This is content that is maintained by the infrastructure. Changes to the content might not always be associated with version changes to the resource."), [implicitRules](resource.html#Resource "A reference to a set of rules that were followed when the resource was constructed, and which must be understood when processing the content. Often, this is a reference to an implementation guide that defines the special rules along with other profiles etc."), [language](resource.html#Resource "The base language in which the resource is written."), [text](domainresource.html#DomainResource "A human-readable narrative that contains a summary of the resource and can be used to represent the content of the resource to a human. The narrative need not encode all the structured data, but is required to contain sufficient detail to make it \"clinically safe\" for a human to just read the narrative. Resource definitions may define what content should be represented in the narrative to ensure clinical safety."), [contained](domainresource.html#DomainResource "These resources do not have an independent existence apart from the resource that contains them - they cannot be identified independently, and nor can they have their own independent transaction scope."), [extension](domainresource.html#DomainResource "May be used to represent additional information that is not part of the basic definition of the resource. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension."), [modifierExtension](domainresource.html#DomainResource "May be used to represent additional information that is not part of the basic definition of the resource and that modifies the understanding of the element that contains it and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer is allowed to define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.  Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).") |
| ... [url](structuredefinition-definitions.html#StructureDefinition.url "StructureDefinition.url : An absolute URI that is used to identify this structure definition when it is referenced in a specification, model, design or an instance; also called its canonical identifier. This SHOULD be globally unique and SHOULD be a literal address at which at which an authoritative instance of this structure definition is (or will be) published. This URL can be the target of a canonical reference. It SHALL remain the same when the structure definition is stored on different servers.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [uri](datatypes.html#uri) | Canonical identifier for this structure definition, represented as a URI (globally unique) |
| ... [identifier](structuredefinition-definitions.html#StructureDefinition.identifier "StructureDefinition.identifier : A formal identifier that is used to identify this structure definition when it is represented in other formats, or referenced in a specification, model, design or an instance.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [Identifier](datatypes.html#Identifier) | Additional identifier for the structure definition |
| ... [version](structuredefinition-definitions.html#StructureDefinition.version "StructureDefinition.version : The identifier that is used to identify this version of the structure definition when it is referenced in a specification, model, design or instance. This is an arbitrary value managed by the structure definition author and is not expected to be globally unique. For example, it might be a timestamp (e.g. yyyymmdd) if a managed version is not available. There is also no expectation that versions can be placed in a lexicographical sequence.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | Business version of the structure definition |
| ... [name](structuredefinition-definitions.html#StructureDefinition.name "StructureDefinition.name : A natural language name identifying the structure definition. This name should be usable as an identifier for the module by machine processing applications such as code generation.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 1..1 | [string](datatypes.html#string) | Name for this structure definition (computer friendly) |
| ... [title](structuredefinition-definitions.html#StructureDefinition.title "StructureDefinition.title : A short, descriptive, user-friendly title for the structure definition.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | Name for this structure definition (human friendly) |
| ... [status](structuredefinition-definitions.html#StructureDefinition.status "StructureDefinition.status : The status of this structure definition. Enables tracking the life-cycle of the content.") | [?!](conformance-rules.html#isModifier "This element is a modifier element")[Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [code](datatypes.html#code) | draft | active | retired | unknown [PublicationStatus](valueset-publication-status.html "The lifecycle status of an artifact.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ... [experimental](structuredefinition-definitions.html#StructureDefinition.experimental "StructureDefinition.experimental : A Boolean value to indicate that this structure definition is authored for testing purposes (or education/evaluation/marketing) and is not intended to be used for genuine usage.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [boolean](datatypes.html#boolean) | For testing purposes, not real usage |
| ... [date](structuredefinition-definitions.html#StructureDefinition.date "StructureDefinition.date : The date  (and optionally time) when the structure definition was published. The date must change when the business version changes and it must change if the status code changes. In addition, it should change when the substantive content of the structure definition changes.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [dateTime](datatypes.html#dateTime) | Date last changed |
| ... [publisher](structuredefinition-definitions.html#StructureDefinition.publisher "StructureDefinition.publisher : The name of the organization or individual that published the structure definition.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | Name of the publisher (organization or individual) |
| ... [contact](structuredefinition-definitions.html#StructureDefinition.contact "StructureDefinition.contact : Contact details to assist a user in finding and communicating with the publisher.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [ContactDetail](metadatatypes.html#ContactDetail) | Contact details for the publisher |
| ... [description](structuredefinition-definitions.html#StructureDefinition.description "StructureDefinition.description : A free text natural language description of the structure definition from a consumer's perspective.") |  | 0..1 | [markdown](datatypes.html#markdown) | Natural language description of the structure definition |
| ... [useContext](structuredefinition-definitions.html#StructureDefinition.useContext "StructureDefinition.useContext : The content was developed with a focus and intent of supporting the contexts that are listed. These contexts may be general categories (gender, age, ...) or may be references to specific programs (insurance plans, studies, ...) and may be used to assist with indexing and searching for appropriate structure definition instances.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[TU](versions.html#std-process "Standards Status = Trial Use") | 0..\* | [UsageContext](metadatatypes.html#UsageContext) | The context that the content is intended to support |
| ... [jurisdiction](structuredefinition-definitions.html#StructureDefinition.jurisdiction "StructureDefinition.jurisdiction : A legal or geographic region in which the structure definition is intended to be used.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [CodeableConcept](datatypes.html#CodeableConcept) | Intended jurisdiction for structure definition (if applicable) [Jurisdiction](valueset-jurisdiction.html "Countries and regions within which this artifact is targeted for use.") ([Extensible](terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept (based on human review), alternate codings (or, data type allowing, text) may be included instead.")) |
| ... [purpose](structuredefinition-definitions.html#StructureDefinition.purpose "StructureDefinition.purpose : Explanation of why this structure definition is needed and why it has been designed as it has.") |  | 0..1 | [markdown](datatypes.html#markdown) | Why this structure definition is defined |
| ... [copyright](structuredefinition-definitions.html#StructureDefinition.copyright "StructureDefinition.copyright : A copyright statement relating to the structure definition and/or its contents. Copyright statements are generally legal restrictions on the use and publishing of the structure definition.") |  | 0..1 | [markdown](datatypes.html#markdown) | Use and/or publishing restrictions |
| ... [keyword](structuredefinition-definitions.html#StructureDefinition.keyword "StructureDefinition.keyword : A set of key words or terms from external terminologies that may be used to assist with indexing and searching of templates nby describing the use of this structure definition, or the content it describes.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [Coding](datatypes.html#Coding) | Assist with indexing and finding [Structure Definition Use Codes / Keywords](valueset-definition-use.html "Codes for the meaning of the defined structure (SNOMED CT and LOINC codes, as an example).") ([Extensible](terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept (based on human review), alternate codings (or, data type allowing, text) may be included instead.")) |
| ... [fhirVersion](structuredefinition-definitions.html#StructureDefinition.fhirVersion "StructureDefinition.fhirVersion : The version of the FHIR specification on which this StructureDefinition is based - this is the formal version of the specification, without the revision number, e.g. [publication].[major].[minor], which is 4.0.1. for this version.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [code](datatypes.html#code) | FHIR Version this StructureDefinition targets [FHIRVersion](valueset-FHIR-version.html "All published FHIR Versions.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ... [mapping](structuredefinition-definitions.html#StructureDefinition.mapping "StructureDefinition.mapping : An external specification that the content is mapped to.") | [I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..\* | [BackboneElement](backboneelement.html) | External specification that the content is mapped to + Rule: Must have at least a name or a uri (or both) |
| .... [identity](structuredefinition-definitions.html#StructureDefinition.mapping.identity "StructureDefinition.mapping.identity : An Internal id that is used to identify this mapping set when specific mappings are made.") |  | 1..1 | [id](datatypes.html#id) | Internal id when this mapping is used |
| .... [uri](structuredefinition-definitions.html#StructureDefinition.mapping.uri "StructureDefinition.mapping.uri : An absolute URI that identifies the specification that this mapping is expressed to.") | [I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..1 | [uri](datatypes.html#uri) | Identifies what this mapping refers to |
| .... [name](structuredefinition-definitions.html#StructureDefinition.mapping.name "StructureDefinition.mapping.name : A name for the specification that is being mapped to.") | [I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..1 | [string](datatypes.html#string) | Names what this mapping refers to |
| .... [comment](structuredefinition-definitions.html#StructureDefinition.mapping.comment "StructureDefinition.mapping.comment : Comments about this mapping, including version notes, issues, scope limitations, and other important notes for usage.") |  | 0..1 | [string](datatypes.html#string) | Versions, Issues, Scope limitations etc. |
| ... [kind](structuredefinition-definitions.html#StructureDefinition.kind "StructureDefinition.kind : Defines the kind of structure that this definition is describing.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [code](datatypes.html#code) | primitive-type | complex-type | resource | logical [StructureDefinitionKind](valueset-structure-definition-kind.html "Defines the type of structure that a definition is describing.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ... [abstract](structuredefinition-definitions.html#StructureDefinition.abstract "StructureDefinition.abstract : Whether structure this definition describes is abstract or not  - that is, whether the structure is not intended to be instantiated. For Resources and Data types, abstract types will never be exchanged  between systems.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [boolean](datatypes.html#boolean) | Whether the structure is abstract |
| ... [context](structuredefinition-definitions.html#StructureDefinition.context "StructureDefinition.context : Identifies the types of resource or data type elements to which the extension can be applied.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..\* | [BackboneElement](backboneelement.html) | If an extension, where it can be used in instances |
| .... [type](structuredefinition-definitions.html#StructureDefinition.context.type "StructureDefinition.context.type : Defines how to interpret the expression that defines what the context of the extension is.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [code](datatypes.html#code) | fhirpath | element | extension [ExtensionContextType](valueset-extension-context-type.html "How an extension context is interpreted.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| .... [expression](structuredefinition-definitions.html#StructureDefinition.context.expression "StructureDefinition.context.expression : An expression that defines where an extension can be used in resources.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [string](datatypes.html#string) | Where the extension can be used in instances |
| ... [contextInvariant](structuredefinition-definitions.html#StructureDefinition.contextInvariant "StructureDefinition.contextInvariant : A set of rules as FHIRPath Invariants about when the extension can be used (e.g. co-occurrence variants for the extension). All the rules must be true.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..\* | [string](datatypes.html#string) | FHIRPath invariants - when the extension can be used |
| ... [type](structuredefinition-definitions.html#StructureDefinition.type "StructureDefinition.type : The type this structure describes. If the derivation kind is 'specialization' then this is the master definition for a type, and there is always one of these (a data type, an extension, a resource, including abstract ones). Otherwise the structure definition is a constraint on the stated type (and in this case, the type cannot be an abstract type).  References are URLs that are relative to http://hl7.org/fhir/StructureDefinition e.g. \"string\" is a reference to http://hl7.org/fhir/StructureDefinition/string. Absolute URLs are only allowed in logical models.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 1..1 | [uri](datatypes.html#uri) | Type defined or constrained by this structure [FHIRDefinedType](valueset-defined-types.html "Either a resource or a data type, including logical model types.") ([Extensible](terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept (based on human review), alternate codings (or, data type allowing, text) may be included instead.")) |
| ... [baseDefinition](structuredefinition-definitions.html#StructureDefinition.baseDefinition "StructureDefinition.baseDefinition : An absolute URI that is the base structure from which this type is derived, either by specialization or constraint.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..1 | [canonical](datatypes.html#canonical)([StructureDefinition](structuredefinition.html)) | Definition that this type is constrained/specialized from |
| ... [derivation](structuredefinition-definitions.html#StructureDefinition.derivation "StructureDefinition.derivation : How the type relates to the baseDefinition.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [code](datatypes.html#code) | specialization | constraint - How relates to base definition [TypeDerivationRule](valueset-type-derivation-rule.html "How a type relates to its baseDefinition.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ... [snapshot](structuredefinition-definitions.html#StructureDefinition.snapshot "StructureDefinition.snapshot : A snapshot view is expressed in a standalone form that can be used and interpreted without considering the base StructureDefinition.") | [I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..1 | [BackboneElement](backboneelement.html) | Snapshot view of the structure + Rule: Each element definition in a snapshot must have a formal definition and cardinalities + Rule: All snapshot elements must start with the StructureDefinition's specified type for non-logical models, or with the same type name for logical models + Rule: All snapshot elements must have a base definition |
| .... [element](structuredefinition-definitions.html#StructureDefinition.snapshot.element "StructureDefinition.snapshot.element : Captures constraints on each element within the resource.") | [I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 1..\* | [ElementDefinition](elementdefinition.html#ElementDefinition) | Definition of elements in the resource (if no StructureDefinition) + Rule: provide either a binding reference or a description (or both) |
| ... [differential](structuredefinition-definitions.html#StructureDefinition.differential "StructureDefinition.differential : A differential view is expressed relative to the base StructureDefinition - a statement of differences that it applies.") | [I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..1 | [BackboneElement](backboneelement.html) | Differential view of the structure + Rule: No slicing on the root element + Rule: In any differential, all the elements must start with the StructureDefinition's specified type for non-logical models, or with the same type name for logical models |
| .... [element](structuredefinition-definitions.html#StructureDefinition.differential.element "StructureDefinition.differential.element : Captures constraints on each element within the resource.") |  | 1..\* | [ElementDefinition](elementdefinition.html#ElementDefinition) | Definition of elements in the resource (if no StructureDefinition) |
| [doco Documentation for this format](formats.html#table "Legend for this format") | | | | |

**UML Diagram** ([Legend](formats.html#uml))

**XML Template**

```

<StructureDefinition xmlns="http://hl7.org/fhir"> ![doco](help.png)
 <!-- from Resource: id, meta, implicitRules, and language -->
 <!-- from DomainResource: text, contained, extension, and modifierExtension -->
 <url value="[uri]"/><!-- 1..1 Canonical identifier for this structure definition, represented as a URI (globally unique) -->
 <identifier><!-- 0..* Identifier Additional identifier for the structure definition --></identifier>
 <version value="[string]"/><!-- 0..1 Business version of the structure definition -->
 <name value="[string]"/><!-- ![??](lock.png) 1..1 Name for this structure definition (computer friendly) -->
 <title value="[string]"/><!-- 0..1 Name for this structure definition (human friendly) -->
 <status value="[code]"/><!-- 1..1 draft | active | retired | unknown -->
 <experimental value="[boolean]"/><!-- 0..1 For testing purposes, not real usage -->
 <date value="[dateTime]"/><!-- 0..1 Date last changed -->
 <publisher value="[string]"/><!-- 0..1 Name of the publisher (organization or individual) -->
 <contact><!-- 0..* ContactDetail Contact details for the publisher --></contact>
 <description value="[markdown]"/><!-- 0..1 Natural language description of the structure definition -->
 <useContext><!-- 0..* UsageContext The context that the content is intended to support --></useContext>
 <jurisdiction><!-- 0..* CodeableConcept Intended jurisdiction for structure definition (if applicable) --></jurisdiction>
 <purpose value="[markdown]"/><!-- 0..1 Why this structure definition is defined -->
 <copyright value="[markdown]"/><!-- 0..1 Use and/or publishing restrictions -->
 <keyword><!-- 0..* Coding Assist with indexing and finding --></keyword>
 <fhirVersion value="[code]"/><!-- 0..1 FHIR Version this StructureDefinition targets -->
 <mapping>  <!-- 0..* External specification that the content is mapped to -->
  <identity value="[id]"/><!-- 1..1 Internal id when this mapping is used -->
  <uri value="[uri]"/><!-- ![??](lock.png) 0..1 Identifies what this mapping refers to -->
  <name value="[string]"/><!-- ![??](lock.png) 0..1 Names what this mapping refers to -->
  <comment value="[string]"/><!-- 0..1 Versions, Issues, Scope limitations etc. -->
 </mapping>
 <kind value="[code]"/><!-- 1..1 primitive-type | complex-type | resource | logical -->
 <abstract value="[boolean]"/><!-- 1..1 Whether the structure is abstract -->
 <context>  <!-- ![??](lock.png) 0..* If an extension, where it can be used in instances -->
  <type value="[code]"/><!-- 1..1 fhirpath | element | extension -->
  <expression value="[string]"/><!-- 1..1 Where the extension can be used in instances -->
 </context>
 <contextInvariant value="[string]"/><!-- ![??](lock.png) 0..* FHIRPath invariants - when the extension can be used -->
 <type value="[uri]"/><!-- ![??](lock.png) 1..1 Type defined or constrained by this structure -->
 <baseDefinition><!-- ![??](lock.png) 0..1 canonical(StructureDefinition) Definition that this type is constrained/specialized from --></baseDefinition>
 <derivation value="[code]"/><!-- 0..1 specialization | constraint - How relates to base definition -->
 <snapshot>  <!-- ![??](lock.png) 0..1 Snapshot view of the structure -->
  <element><!-- ![??](lock.png) 1..* ElementDefinition Definition of elements in the resource (if no StructureDefinition) --></element>
 </snapshot>
 <differential>  <!-- ![??](lock.png) 0..1 Differential view of the structure -->
  <element><!-- 1..* ElementDefinition Definition of elements in the resource (if no StructureDefinition) --></element>
 </differential>
</StructureDefinition>
```

**JSON Template**

```

{![doco](help.png)
  "resourceType" : "StructureDefinition",
  // from Resource: id, meta, implicitRules, and language
  // from DomainResource: text, contained, extension, and modifierExtension
  "url" : "<uri>", // R!  Canonical identifier for this structure definition, represented as a URI (globally unique)
  "identifier" : [{ Identifier }], // Additional identifier for the structure definition
  "version" : "<string>", // Business version of the structure definition
  "name" : "<string>", // C? R!  Name for this structure definition (computer friendly)
  "title" : "<string>", // Name for this structure definition (human friendly)
  "status" : "<code>", // R!  draft | active | retired | unknown
  "experimental" : <boolean>, // For testing purposes, not real usage
  "date" : "<dateTime>", // Date last changed
  "publisher" : "<string>", // Name of the publisher (organization or individual)
  "contact" : [{ ContactDetail }], // Contact details for the publisher
  "description" : "<markdown>", // Natural language description of the structure definition
  "useContext" : [{ UsageContext }], // The context that the content is intended to support
  "jurisdiction" : [{ CodeableConcept }], // Intended jurisdiction for structure definition (if applicable)
  "purpose" : "<markdown>", // Why this structure definition is defined
  "copyright" : "<markdown>", // Use and/or publishing restrictions
  "keyword" : [{ Coding }], // Assist with indexing and finding
  "fhirVersion" : "<code>", // FHIR Version this StructureDefinition targets
  "mapping" : [{ // External specification that the content is mapped to
    "identity" : "<id>", // R!  Internal id when this mapping is used
    "uri" : "<uri>", // C? Identifies what this mapping refers to
    "name" : "<string>", // C? Names what this mapping refers to
    "comment" : "<string>" // Versions, Issues, Scope limitations etc.
  }],
  "kind" : "<code>", // R!  primitive-type | complex-type | resource | logical
  "abstract" : <boolean>, // R!  Whether the structure is abstract
  "context" : [{ // C? If an extension, where it can be used in instances
    "type" : "<code>", // R!  fhirpath | element | extension
    "expression" : "<string>" // R!  Where the extension can be used in instances
  }],
  "contextInvariant" : ["<string>"], // C? FHIRPath invariants - when the extension can be used
  "type" : "<uri>", // C? R!  Type defined or constrained by this structure
  "baseDefinition" : { canonical(StructureDefinition) }, // C? Definition that this type is constrained/specialized from
  "derivation" : "<code>", // specialization | constraint - How relates to base definition
  "snapshot" : { // C? Snapshot view of the structure
    "element" : [{ ElementDefinition }] // C? R!  Definition of elements in the resource (if no StructureDefinition)
  },
  "differential" : { // C? Differential view of the structure
    "element" : [{ ElementDefinition }] // R!  Definition of elements in the resource (if no StructureDefinition)
  }
}
```

**Turtle Template**

```

@prefix fhir: <http://hl7.org/fhir/> .![doco](help.png)


[ a fhir:StructureDefinition;
  fhir:nodeRole fhir:treeRoot; # if this is the parser root

  # from Resource: .id, .meta, .implicitRules, and .language
  # from DomainResource: .text, .contained, .extension, and .modifierExtension
  fhir:StructureDefinition.url [ uri ]; # 1..1 Canonical identifier for this structure definition, represented as a URI (globally unique)
  fhir:StructureDefinition.identifier [ Identifier ], ... ; # 0..* Additional identifier for the structure definition
  fhir:StructureDefinition.version [ string ]; # 0..1 Business version of the structure definition
  fhir:StructureDefinition.name [ string ]; # 1..1 Name for this structure definition (computer friendly)
  fhir:StructureDefinition.title [ string ]; # 0..1 Name for this structure definition (human friendly)
  fhir:StructureDefinition.status [ code ]; # 1..1 draft | active | retired | unknown
  fhir:StructureDefinition.experimental [ boolean ]; # 0..1 For testing purposes, not real usage
  fhir:StructureDefinition.date [ dateTime ]; # 0..1 Date last changed
  fhir:StructureDefinition.publisher [ string ]; # 0..1 Name of the publisher (organization or individual)
  fhir:StructureDefinition.contact [ ContactDetail ], ... ; # 0..* Contact details for the publisher
  fhir:StructureDefinition.description [ markdown ]; # 0..1 Natural language description of the structure definition
  fhir:StructureDefinition.useContext [ UsageContext ], ... ; # 0..* The context that the content is intended to support
  fhir:StructureDefinition.jurisdiction [ CodeableConcept ], ... ; # 0..* Intended jurisdiction for structure definition (if applicable)
  fhir:StructureDefinition.purpose [ markdown ]; # 0..1 Why this structure definition is defined
  fhir:StructureDefinition.copyright [ markdown ]; # 0..1 Use and/or publishing restrictions
  fhir:StructureDefinition.keyword [ Coding ], ... ; # 0..* Assist with indexing and finding
  fhir:StructureDefinition.fhirVersion [ code ]; # 0..1 FHIR Version this StructureDefinition targets
  fhir:StructureDefinition.mapping [ # 0..* External specification that the content is mapped to
    fhir:StructureDefinition.mapping.identity [ id ]; # 1..1 Internal id when this mapping is used
    fhir:StructureDefinition.mapping.uri [ uri ]; # 0..1 Identifies what this mapping refers to
    fhir:StructureDefinition.mapping.name [ string ]; # 0..1 Names what this mapping refers to
    fhir:StructureDefinition.mapping.comment [ string ]; # 0..1 Versions, Issues, Scope limitations etc.
  ], ...;
  fhir:StructureDefinition.kind [ code ]; # 1..1 primitive-type | complex-type | resource | logical
  fhir:StructureDefinition.abstract [ boolean ]; # 1..1 Whether the structure is abstract
  fhir:StructureDefinition.context [ # 0..* If an extension, where it can be used in instances
    fhir:StructureDefinition.context.type [ code ]; # 1..1 fhirpath | element | extension
    fhir:StructureDefinition.context.expression [ string ]; # 1..1 Where the extension can be used in instances
  ], ...;
  fhir:StructureDefinition.contextInvariant [ string ], ... ; # 0..* FHIRPath invariants - when the extension can be used
  fhir:StructureDefinition.type [ uri ]; # 1..1 Type defined or constrained by this structure
  fhir:StructureDefinition.baseDefinition [ canonical(StructureDefinition) ]; # 0..1 Definition that this type is constrained/specialized from
  fhir:StructureDefinition.derivation [ code ]; # 0..1 specialization | constraint - How relates to base definition
  fhir:StructureDefinition.snapshot [ # 0..1 Snapshot view of the structure
    fhir:StructureDefinition.snapshot.element [ ElementDefinition ], ... ; # 1..* Definition of elements in the resource (if no StructureDefinition)
  ];
  fhir:StructureDefinition.differential [ # 0..1 Differential view of the structure
    fhir:StructureDefinition.differential.element [ ElementDefinition ], ... ; # 1..* Definition of elements in the resource (if no StructureDefinition)
  ];
]
```

**Changes since Release 3**

|  |  |
| --- | --- |
| [StructureDefinition](structuredefinition.html#StructureDefinition) |  |
| StructureDefinition.status | - Change value set from http://hl7.org/fhir/ValueSet/publication-status to http://hl7.org/fhir/ValueSet/publication-status|4.0.1 |
| StructureDefinition.experimental | - No longer marked as Modifier |
| StructureDefinition.keyword | - Add Binding `http://hl7.org/fhir/ValueSet/definition-use` (extensible) |
| StructureDefinition.fhirVersion | - Type changed from id to code - Add Binding `http://hl7.org/fhir/ValueSet/FHIR-version|4.0.1` (required) |
| StructureDefinition.kind | - Change value set from http://hl7.org/fhir/ValueSet/structure-definition-kind to http://hl7.org/fhir/ValueSet/structure-definition-kind|4.0.1 |
| StructureDefinition.context | - Type changed from string to BackboneElement |
| StructureDefinition.context.type | - **Added Mandatory Element** |
| StructureDefinition.context.expression | - **Added Mandatory Element** |
| StructureDefinition.type | - Type changed from code to uri |
| StructureDefinition.baseDefinition | - Type changed from uri to canonical(StructureDefinition) |
| StructureDefinition.derivation | - Change value set from http://hl7.org/fhir/ValueSet/type-derivation-rule to http://hl7.org/fhir/ValueSet/type-derivation-rule|4.0.1 |
| StructureDefinition.contextType | - deleted |

See the [Full Difference](diff.html) for further information

This analysis is available as [XML](structuredefinition.diff.xml) or [JSON](structuredefinition.diff.json).

See [R3 <--> R4 Conversion Maps](structuredefinition-version-maps.html) (status = 206 tests that all execute ok. 4 fail round-trip testing and 206 r3 resources are invalid (0 errors).)

See the [Profiles & Extensions](structuredefinition-profiles.html) and the alternate definitions:
Master Definition [XML](structuredefinition.profile.xml.html) + [JSON](structuredefinition.profile.json.html),
[XML](xml.html) [Schema](structuredefinition.xsd)/[Schematron](structuredefinition.sch) + [JSON](json.html)
[Schema](structuredefinition.schema.json.html), [ShEx](structuredefinition.shex.html) (for [Turtle](rdf.html)) + [see the extensions](structuredefinition-profiles.html) & the [dependency analysis](structuredefinition-dependencies.html)

### 5.3.4.1 Terminology Bindings

| Path | Definition | Type | Reference |
| --- | --- | --- | --- |
| StructureDefinition.status | The lifecycle status of an artifact. | [Required](terminologies.html#required) | [PublicationStatus](valueset-publication-status.html) |
| StructureDefinition.jurisdiction | Countries and regions within which this artifact is targeted for use. | [Extensible](terminologies.html#extensible) | [Jurisdiction ValueSet](valueset-jurisdiction.html) |
| StructureDefinition.keyword | Codes for the meaning of the defined structure (SNOMED CT and LOINC codes, as an example). | [Extensible](terminologies.html#extensible) | [DefinitionUseCodes](valueset-definition-use.html) |
| StructureDefinition.fhirVersion | All published FHIR Versions. | [Required](terminologies.html#required) | [FHIRVersion](valueset-FHIR-version.html) |
| StructureDefinition.kind | Defines the type of structure that a definition is describing. | [Required](terminologies.html#required) | [StructureDefinitionKind](valueset-structure-definition-kind.html) |
| StructureDefinition.context.type | How an extension context is interpreted. | [Required](terminologies.html#required) | [ExtensionContextType](valueset-extension-context-type.html) |
| StructureDefinition.type | Either a resource or a data type, including logical model types. | [Extensible](terminologies.html#extensible) | [FHIRDefinedType](valueset-defined-types.html) |
| StructureDefinition.derivation | How a type relates to its baseDefinition. | [Required](terminologies.html#required) | [TypeDerivationRule](valueset-type-derivation-rule.html) |

### 5.3.4.2 Constraints

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **id** | **Level** | **Location** | **Description** | **[Expression](fhirpath.html)** |
| **sdf-0** | [Warning](conformance-rules.html#warning) | (base) | Name should be usable as an identifier for the module by machine processing applications such as code generation | name.matches('[A-Z]([A-Za-z0-9\_]){0,254}') |
| **sdf-1** | [Rule](conformance-rules.html#rule) | (base) | Element paths must be unique unless the structure is a constraint | derivation = 'constraint' or snapshot.element.select(path).isDistinct() |
| **sdf-15a** | [Rule](conformance-rules.html#rule) | (base) | If the first element in a differential has no "." in the path and it's not a logical model, it has no type | (kind!='logical' and differential.element.first().path.contains('.').not()) implies differential.element.first().type.empty() |
| **sdf-2** | [Rule](conformance-rules.html#rule) | StructureDefinition.mapping | Must have at least a name or a uri (or both) | name.exists() or uri.exists() |
| **sdf-3** | [Rule](conformance-rules.html#rule) | StructureDefinition.snapshot | Each element definition in a snapshot must have a formal definition and cardinalities | element.all(definition.exists() and min.exists() and max.exists()) |
| **sdf-4** | [Rule](conformance-rules.html#rule) | (base) | If the structure is not abstract, then there SHALL be a baseDefinition | abstract = true or baseDefinition.exists() |
| **sdf-5** | [Rule](conformance-rules.html#rule) | (base) | If the structure defines an extension then the structure must have context information | type != 'Extension' or derivation = 'specialization' or (context.exists()) |
| **sdf-6** | [Rule](conformance-rules.html#rule) | (base) | A structure must have either a differential, or a snapshot (or both) | snapshot.exists() or differential.exists() |
| **sdf-8** | [Rule](conformance-rules.html#rule) | StructureDefinition.snapshot | All snapshot elements must start with the StructureDefinition's specified type for non-logical models, or with the same type name for logical models | (%resource.kind = 'logical' or element.first().path = %resource.type) and element.tail().all(path.startsWith(%resource.snapshot.element.first().path&'.')) |
| **sdf-10** | [Rule](conformance-rules.html#rule) | StructureDefinition.snapshot.element | provide either a binding reference or a description (or both) | binding.empty() or binding.valueSet.exists() or binding.description.exists() |
| **sdf-11** | [Rule](conformance-rules.html#rule) | (base) | If there's a type, its content must match the path name in the first element of a snapshot | kind != 'logical' implies snapshot.empty() or snapshot.element.first().path = type |
| **sdf-14** | [Rule](conformance-rules.html#rule) | (base) | All element definitions must have an id | snapshot.element.all(id.exists()) and differential.element.all(id.exists()) |
| **sdf-15** | [Rule](conformance-rules.html#rule) | (base) | The first element in a snapshot has no type unless model is a logical model. | kind!='logical' implies snapshot.element.first().type.empty() |
| **sdf-16** | [Rule](conformance-rules.html#rule) | (base) | All element definitions must have unique ids (snapshot) | snapshot.element.all(id.exists()) and snapshot.element.id.trace('ids').isDistinct() |
| **sdf-17** | [Rule](conformance-rules.html#rule) | (base) | All element definitions must have unique ids (diff) | differential.element.all(id.exists()) and differential.element.id.trace('ids').isDistinct() |
| **sdf-18** | [Rule](conformance-rules.html#rule) | (base) | Context Invariants can only be used for extensions | contextInvariant.exists() implies type = 'Extension' |
| **sdf-19** | [Rule](conformance-rules.html#rule) | (base) | FHIR Specification models only use FHIR defined types | url.startsWith('http://hl7.org/fhir/StructureDefinition') implies (differential.element.type.code.all(matches('^[a-zA-Z0-9]+$') or matches('^http:\\/\\/hl7\\.org\\/fhirpath\\/System\\.[A-Z][A-Za-z]+$')) and snapshot.element.type.code.all(matches('^[a-zA-Z0-9\\.]+$') or matches('^http:\\/\\/hl7\\.org\\/fhirpath\\/System\\.[A-Z][A-Za-z]+$'))) |
| **sdf-20** | [Rule](conformance-rules.html#rule) | StructureDefinition.differential | No slicing on the root element | element.where(path.contains('.').not()).slicing.empty() |
| **sdf-21** | [Rule](conformance-rules.html#rule) | (base) | Default values can only be specified on specializations | differential.element.defaultValue.exists() implies (derivation = 'specialization') |
| **sdf-22** | [Rule](conformance-rules.html#rule) | (base) | FHIR Specification models never have default values | url.startsWith('http://hl7.org/fhir/StructureDefinition') implies (snapshot.element.defaultValue.empty() and differential.element.defaultValue.empty()) |
| **sdf-23** | [Rule](conformance-rules.html#rule) | (base) | No slice name on root | (snapshot | differential).element.all(path.contains('.').not() implies sliceName.empty()) |
| **sdf-8a** | [Rule](conformance-rules.html#rule) | StructureDefinition.differential | In any differential, all the elements must start with the StructureDefinition's specified type for non-logical models, or with the same type name for logical models | (%resource.kind = 'logical' or element.first().path.startsWith(%resource.type)) and (element.tail().empty() or element.tail().all(path.startsWith(%resource.differential.element.first().path.replaceMatches('\\..\*','')&'.'))) |
| **sdf-8b** | [Rule](conformance-rules.html#rule) | StructureDefinition.snapshot | All snapshot elements must have a base definition | element.all(base.exists()) |
| **sdf-9** | [Rule](conformance-rules.html#rule) | (base) | In any snapshot or differential, no label, code or requirements on an element without a "." in the path (e.g. the first element) | children().element.where(path.contains('.').not()).label.empty() and children().element.where(path.contains('.').not()).code.empty() and children().element.where(path.contains('.').not()).requirements.empty() |

## 5.3.5 Interpretation Notes:

- A structure is represented as a flat list of elements. The `element.path` provides the overall structure.
- Differentials in constraints need only specify elements that they are making rules about. Other elements can be inferred as defined in the base resource
- Elements specified in the differential (and all elements in the snapshot) must be ordered as such:
  - Elements from the baseDefinition appear before new elements in a StructureDefinition with derivation 'specialization'
  - Elements must be in the same order as the baseDefinition, and child elements appear in depth-first order.
  - Unsliced descendants of sliced elements appear before slices
- `element.short`, `element.formal`, `element.comments` and `element.mapping` provide the specific definition for the field in a specific context.
- `element.type` is used to specify which types may be used for this element. If there is more than one type, the element offers a choice of types and must have a name that terminates in "[x]". (Note: when substituting [x] with a specific data type, always capitalize the first letter. Choice types are always camel-case. Ex: "effectiveDateTime" is correct, "effectivedateTime" is NOT correct.)
  When profiling a resource and only one type is specified, the name of the element is changed to include the type instead of '[x]'.
- When using XPath to define constraints about the relationship between the contents of the narrative and the contents of the data elements, the element against which the rule is expressed is the one against which the error or warning will be reported by a validator.
- When expression constraints are placed on elements that offer a choice of types, the expression has to select the type to which it applies using the [FHIRPath `is` operator](fhirpath.html).
- For XPath constraints, the prefix "f" should be used for "http://hl7.org/fhir", and "h" for "http://www.w3.org/1999/xhtml". XPath constraints are written against the XML representation
- The condition element is used to assert that a constraint defined on another element affects the allowed cardinality of this element.

### 5.3.5.1 Different Uses for StructureDefinition

The base structure definition is used in a number of different ways to support
the FHIR specification. The various uses of the StructureDefinition are
controlled by the elements `kind`, `type`, `base`, and `url`,
using this basic pattern:

```

{
  "url": the identity of this structure definition,
  "kind": (primitive-type | complex-type | resource | logical),
  "type": the type being constrained (if it's a constraint)
  "baseDefinition": the structure definition from which this is derived
}
```

This list shows a number of examples, with links to real examples for each:

1. Base definition of a data type (example: [Quantity](datatypes.html#Quantity) - [XML](quantity.profile.xml.html), [JSON](quantity.profile.json.html)):  

   ```
   
   {
     "resourceType": "StructureDefinition",
     "url": "http://hl7.org/fhir/StructureDefinition/Quantity",
     "name": "Quantity",
     "kind": "complex-type",
     "baseDefinition": "http://hl7.org/fhir/StructureDefinition/Element"
   }
   ```
2. A constrained data type (example: [Money](datatypes.html#Money) - [XML](money.profile.xml.html), [JSON](money.profile.json.html)):  

   ```
   
   {
     "resourceType": "StructureDefinition",
     "url": "http://hl7.org/fhir/StructureDefinition/Money",
     "name": "Money",
     "kind": "complex-type",
     "type": "Quantity",
     "baseDefinition": "http://hl7.org/fhir/StructureDefinition/Quantity"
   }
   ```
3. Base definition of a resource (example: [Patient](patient.html) - [XML](patient.profile.xml.html), [JSON](patient.profile.json.html)):   

   ```
   
   {
     "resourceType": "StructureDefinition",
     "url": "http://hl7.org/fhir/StructureDefinition/Patient",
     "name": "Patient",
     "kind": "resource",
     "baseDefinition": "http://hl7.org/fhir/StructureDefinition/DomainResource"
   }
   ```
4. Constraint on a resource (example: [Clinical Document Profile for Composition](clinicaldocument.html) - [XML](clinicaldocument.profile.xml.html), [JSON](clinicaldocument.profile.json.html)):   

   ```
   
   {
     "resourceType": "StructureDefinition",
     "url": "http://hl7.org/fhir/StructureDefinition/clinicaldocument",
     "name": "Clinical Document Profile for Composition",
     "kind": "resource",
     "type": "Composition",
     "baseDefinition": "http://hl7.org/fhir/StructureDefinition/Composition"
   }
   ```
5. Base Extension (a standard data type) (example: [Extension](extensibility.html#Extension) - [XML](extension.profile.xml.html), [JSON](extension.profile.json.html)):   

   ```
   
   {
     "resourceType": "StructureDefinition",
     "url": "http://hl7.org/fhir/StructureDefinition/Extension",
     "name": "Extension",
     "kind": "datatype",
     "baseDefinition": "http://hl7.org/fhir/StructureDefinition/Element"
   }
   ```
6. A defined Extension (example: [Extension Data Absent Reason](extension-data-absent-reason.html) - [XML](extension-data-absent-reason.xml.html), [JSON](extension-data-absent-reason.json.html)):   

   ```
   
   {
     "resourceType": "StructureDefinition",
     "url": "http://hl7.org/fhir/StructureDefinition/data-absent-reason",
     "name": "Data Absent Reason",
     "kind": "complex-type",
     "type": "Extension",
     "baseDefinition": "http://hl7.org/fhir/StructureDefinition/Extension"
   }
   ```
7. A constraint on a defined extension (no examples currently defined):   

   ```
   
   {
     "resourceType": "StructureDefinition",
     "url": "http://example.org/fhir/StructureDefinition/race",
     "name": "Race codes used by institution (a subset of meaningful use codes)",
     "kind": "complex-type",
     "type": "Extension",
     "baseDefinition": "http://hl7.org/fhir/us/core/StructureDefinition/us-core-race"
   }
   ```

On this list, structure definitions of type 1, 3, and 5 can only be defined by the FHIR specification itself. The other kinds of structure definitions
are (or may be) created by the specification but can also be defined by other implementers.

### 5.3.5.2 Rules for Constrained Types

When the structure is a constraint (`derivation` = `constraint`), see [Extending and Restricting Resources](profiling.html#resources) for the rules that apply.

### 5.3.5.3 Common Mapping Targets

Structures are able to map elements to concepts in other definition systems. Generally, these are used to
map the elements to local implementation models, data paths, and concepts. However they are also used to map
to other standards and published terminologies. These are the standard URIs used for common targets of the
mapping:

| Name | Details |
| --- | --- |
| Logical Mapping | Formal URL: http://hl7.org/fhir/logical |
| [ClinicalTrials.gov Mapping](http://clinicaltrials.gov) | Formal URL: http://clinicaltrials.gov |
| [Workflow Pattern](http://hl7.org/fhir/workflow-module.html) | Formal URL: http://hl7.org/fhir/workflow |
| [CDISC Define XML 2.0 metadata standard](http://www.cdisc.org/define-xml) | Formal URL: http://www.cdisc.org/define-xml |
| [Mapping to NCPDP SCRIPT 10.6](http://www.ncpdp.org/NCPDP/media/pdf/NCPDPEprescribing101.pdf) | Formal URL: http://ncpdp.org/SCRIPT10\_6 |
| [FiveWs Pattern Mapping](http://hl7.org/fhir/fivews.html) | Formal URL: http://hl7.org/fhir/fivews |
| [BRIDG 5.1 Mapping](https://bridgmodel.nci.nih.gov/download-model/bridg-releases/release-51/release-package) | Formal URL: https://bridgmodel.nci.nih.gov |
| [FHIR Composition](http://hl7.org/fhir/composition.html) | Formal URL: http://hl7.org/fhir/composition |
| [IHE Structured Data Capture](http://wiki.siframework.org/IHE+SDC+Profile) | Formal URL: http://siframework.org/ihe-sdc-profile |
| [Canadian Dental Association eclaims standard](http://www.cda-adc.ca/en/services/cdanet/) | Formal URL: http://www.cda-adc.ca/en/services/cdanet/ |
| [SNOMED CT Concept Domain Binding](http://snomed.info/conceptdomain) | Formal URL: http://snomed.info/conceptdomain  Concept domain bindings link a resource or an element to a set of SNOMED CT concepts that represent the intended semantics of the instances (whether or not SNOMED CT is used to encode that data element). This set of concepts is represented using a SNOMED CT expression constraint. Note that the 'Concept domain binding' may be a superset of the 'value set binding'. These bindings help to support:   - Quality checking FHIR resources by ensuring that (a) the intended semantics of the instances matches the valid range of the corresponding SNOMED CT attribute, and (b) the intended value set is appropriate for the intended semantics of the instances - Semantic checking of data instances by helping to detect potential inconsistencies caused by overlap between the semantics incorporated in two concept domains |
| [R3-ReferalRequest Mapping](http://hl7.org/fhir/rr) | Formal URL: http://hl7.org/fhir/rr |
| [HL7 v2 Mapping](http://www.hl7.org/implement/standards/product_brief.cfm?product_id=185) | Formal URL: http://hl7.org/v2 |
| [RIM Mapping](http://www.hl7.org/implement/standards/product_brief.cfm?product_id=186) | Formal URL: http://hl7.org/v3 |
| [ISO 11179](http://metadata-standards.org/11179/) | Formal URL: http://metadata-standards.org/11179/  These mappings are included to indicate where properties of the data elements defined by the FHIR specification relate to similar fields in the ISO 11179 specification. |
| [Mapping to Quality Improvement Domain Analysis Model](http://www.hl7.org/implement/standards/product_brief.cfm?product_id=378) | Formal URL: http://hl7.org/qidam |
| [DICOM Tag Mapping](http://nema.org/dicom) | Formal URL: http://nema.org/dicom |
| [MDMI Referent Index Mapping](http://github.com/MDMI/ReferentIndexContent) | Formal URL: http://github.com/MDMI/ReferentIndexContent |
| [V3 Pharmacy Dispense RMIM](http://www.hl7.org/documentcenter/private/standards/v3/edition_web/domains/uvrx/uvrx_MedicationDispenseEvent.html#PORX_RM020070UV) | Formal URL: http://www.hl7.org/v3/PORX\_RM020070UV |
| [XDS metadata equivalent](http://wiki.ihe.net/index.php/Category:DocShare) | Formal URL: http://ihe.net/xds |
| [Equivalent CAP Code](https://www.cap.org/laboratory-improvement/proficiency-testing/cap-ecc) | Formal URL: http://cap.org/ecc |
| [CDA (R2)](http://www.hl7.org/implement/standards/product_brief.cfm?product_id=7) | Formal URL: http://hl7.org/v3/cda |
| [Quality Improvement and Clinical Knowledge (QUICK)](http://wiki.siframework.org/CQF) | Formal URL: http://siframework.org/cqf |
| [FHIR DocumentReference](http://hl7.org/fhir/documentreference.html) | Formal URL: http://hl7.org/fhir/documentreference |
| [Canadian Pharmacy Associaiton eclaims standard](http://www.pharmacists.ca/) | Formal URL: http://www.pharmacists.ca/ |
| [UDI Mapping](http://www.fda.gov/MedicalDevices/DeviceRegulationandGuidance/UniqueDeviceIdentification/default.htm) | Formal URL: http://fda.gov/UDI  UDI is a unique numeric or alphanumeric code that consists of two parts: (1) a device identifier (DI), a mandatory, fixed portion of a UDI that identifies the labeler and the specific version or model of a device, and (2) a production identifier (PI), a conditional, variable portion of a UDI that identifies one or more of the following when included on the label of a device: (2a) the lot or batch number within which a device was manufactured; (2b) the serial number of a specific device; (2c) the expiration date of a specific device; (2d) the date a specific device was manufactured; (2e) the distinct identification code required by §1271.290(c) for a human cell, tissue, or cellular and tissue-based product (HCT/P) regulated as a device. |
| [Quality Data Model](http://www.healthit.gov/quality-data-model) | Formal URL: http://www.healthit.gov/quality-data-model |
| [FHIR AuditEvent Mapping](http://hl7.org/fhir/auditevent.html) | Formal URL: http://hl7.org/fhir/auditevent |
| [IHE Data Element Exchange (DEX)](http://wiki.ihe.net/index.php?title=Data_Element_Exchange) | Formal URL: http://ihe.net/data-element-exchange |
| [SNOMED CT Attribute Binding](http://snomed.org/attributebinding) | Formal URL: http://snomed.org/attributebinding  Attribute bindings link coded data elements in FHIR resources to a corresponding attribute in the SNOMED CT concept model. These bindings help to support:   - clarifying the intended meaning of the data element - Quality checking the alignment between FHIR resource design and any coresponding SNOMED CT concept model - Composition and decomposition of data instances by indicating the SNOMED CT concept model attribute whose value may be used to decompose a precoordinated concept into this data element |
| [W3C PROV](http://www.w3.org/ns/prov) | Formal URL: http://www.w3.org/ns/prov  The provenance resource is based on known practices in the HL7 implementation space, particularly those found in the v2 EVN segment, the v3 ControlAct Wrapper, the CDA header, and IHE ATNA. The conceptual model underlying the design is the [W3C provenance Specification](http://www.w3.org/2011/prov/wiki/Main_Page)  . Though the content and format of the resource is designed to meet specific requirements for FHIR, all the parts of the resource are formally mapped to the PROV-O specification, and FHIR resources can be transformed to their W3C PROV equivalent. |
| [Ontological RIM Mapping](http://hl7.org/orim) | Formal URL: http://hl7.org/orim |
| [LOINC code for the element](http://loinc.org) | Formal URL: http://loinc.org |
| [vCard Mapping](https://tools.ietf.org/html/rfc6350) | Formal URL: http://w3.org/vcard |
| [Open EHR Archetype Mapping](http://openehr.org) | Formal URL: http://openehr.org |
| [ServD](http://www.omg.org/spec/ServD/1.0/) | Formal URL: http://www.omg.org/spec/ServD/1.0/ |
| [FHIR Provenance Mapping](http://hl7.org/fhir/provenance.html) | Formal URL: http://hl7.org/fhir/provenance |
| [iCalendar](http://www.ietf.org/rfc/rfc2445.txt) | Formal URL: http://ietf.org/rfc/2445 |

### 5.3.5.4 Logical Models

StructureDefinitions are used to define the basic structures of FHIR: data types, resources, extensions, and profiles.
The same definition structure can also be used to define any arbitrary structures that are a directed acyclic graph
with typed nodes, where the primitive types are those defined by the FHIR specification.

This technique has many uses:

- Describing any arbitrary content model
- Describing existing HL7 content models (e.g. v2, CDA) using FHIR
- Describing common design patterns used in FHIR
- Defining a content model to support the mapping language

## 5.3.6 Search Parameters

Search parameters for this resource. The [common parameters](search.html#all) also apply. See [Searching](search.html) for more information about searching in REST, messaging, and services.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Name** | **Type** | **Description** | **Expression** | **In Common** |
| abstract [TU](versions.html#std-process "Trial Use Content") | [token](search.html#token) | Whether the structure is abstract | StructureDefinition.abstract |  |
| base [TU](versions.html#std-process "Trial Use Content") | [reference](search.html#reference) | Definition that this type is constrained/specialized from | StructureDefinition.baseDefinition ([StructureDefinition](structuredefinition.html)) |  |
| base-path [TU](versions.html#std-process "Trial Use Content") | [token](search.html#token) | Path that identifies the base element | StructureDefinition.snapshot.element.base.path | StructureDefinition.differential.element.base.path |  |
| context [TU](versions.html#std-process "Trial Use Content") | [token](search.html#token) | A use context assigned to the structure definition | (StructureDefinition.useContext.value as CodeableConcept) |  |
| context-quantity [TU](versions.html#std-process "Trial Use Content") | [quantity](search.html#quantity) | A quantity- or range-valued use context assigned to the structure definition | (StructureDefinition.useContext.value as Quantity) | (StructureDefinition.useContext.value as Range) |  |
| context-type [TU](versions.html#std-process "Trial Use Content") | [token](search.html#token) | A type of use context assigned to the structure definition | StructureDefinition.useContext.code |  |
| context-type-quantity [TU](versions.html#std-process "Trial Use Content") | [composite](search.html#composite) | A use context type and quantity- or range-based value assigned to the structure definition | On StructureDefinition.useContext:   context-type: code   context-quantity: value.as(Quantity) | value.as(Range) |  |
| context-type-value [TU](versions.html#std-process "Trial Use Content") | [composite](search.html#composite) | A use context type and value assigned to the structure definition | On StructureDefinition.useContext:   context-type: code   context: value.as(CodeableConcept) |  |
| date [TU](versions.html#std-process "Trial Use Content") | [date](search.html#date) | The structure definition publication date | StructureDefinition.date |  |
| derivation [TU](versions.html#std-process "Trial Use Content") | [token](search.html#token) | specialization | constraint - How relates to base definition | StructureDefinition.derivation |  |
| description [TU](versions.html#std-process "Trial Use Content") | [string](search.html#string) | The description of the structure definition | StructureDefinition.description |  |
| experimental [TU](versions.html#std-process "Trial Use Content") | [token](search.html#token) | For testing purposes, not real usage | StructureDefinition.experimental |  |
| ext-context [TU](versions.html#std-process "Trial Use Content") | [token](search.html#token) | The system is the URL for the context-type: e.g. http://hl7.org/fhir/extension-context-type#element|CodeableConcept.text | StructureDefinition.context.type |  |
| identifier [TU](versions.html#std-process "Trial Use Content") | [token](search.html#token) | External identifier for the structure definition | StructureDefinition.identifier |  |
| jurisdiction [TU](versions.html#std-process "Trial Use Content") | [token](search.html#token) | Intended jurisdiction for the structure definition | StructureDefinition.jurisdiction |  |
| keyword [TU](versions.html#std-process "Trial Use Content") | [token](search.html#token) | A code for the StructureDefinition | StructureDefinition.keyword |  |
| kind [TU](versions.html#std-process "Trial Use Content") | [token](search.html#token) | primitive-type | complex-type | resource | logical | StructureDefinition.kind |  |
| name [TU](versions.html#std-process "Trial Use Content") | [string](search.html#string) | Computationally friendly name of the structure definition | StructureDefinition.name |  |
| path [TU](versions.html#std-process "Trial Use Content") | [token](search.html#token) | A path that is constrained in the StructureDefinition | StructureDefinition.snapshot.element.path | StructureDefinition.differential.element.path |  |
| publisher [TU](versions.html#std-process "Trial Use Content") | [string](search.html#string) | Name of the publisher of the structure definition | StructureDefinition.publisher |  |
| status [TU](versions.html#std-process "Trial Use Content") | [token](search.html#token) | The current status of the structure definition | StructureDefinition.status |  |
| title [TU](versions.html#std-process "Trial Use Content") | [string](search.html#string) | The human-friendly name of the structure definition | StructureDefinition.title |  |
| type [TU](versions.html#std-process "Trial Use Content") | [uri](search.html#uri) | Type defined or constrained by this structure | StructureDefinition.type |  |
| url [TU](versions.html#std-process "Trial Use Content") | [uri](search.html#uri) | The uri that identifies the structure definition | StructureDefinition.url |  |
| valueset [TU](versions.html#std-process "Trial Use Content") | [reference](search.html#reference) | A vocabulary binding reference | StructureDefinition.snapshot.element.binding.valueSet ([ValueSet](valueset.html)) |  |
| version [TU](versions.html#std-process "Trial Use Content") | [token](search.html#token) | The business version of the structure definition | StructureDefinition.version |  |

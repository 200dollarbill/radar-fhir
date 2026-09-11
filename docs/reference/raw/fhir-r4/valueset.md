---
id: valueset
title: ValueSet
source_url: https://hl7.org/fhir/R4/valueset.html
group: fhir-r4
fhir_version: R4
fetched_at: '2026-09-11T13:23:37Z'
sha256: a77507ed319b9aef7387537b7c5c0b15943953256aeacdb6ea7dfc7c698cef52
---
This page is part of the FHIR Specification (v4.0.1: R4 - Mixed [Normative](https://confluence.hl7.org/display/HL7/HL7+Balloting "Normative Standard") and [STU](https://confluence.hl7.org/display/HL7/HL7+Balloting "Standard for Trial-Use")) in it's permanent home (it will always be available at this URL). The current version which supercedes this version is [5.0.0](http://hl7.org/fhir/index.html). For a full list of available versions, see the [Directory of published versions ![](external.png)](http://hl7.org/fhir/directory.html). Page versions: [R5](http://hl7.org/fhir/R5/valueset.html) [R4B](http://hl7.org/fhir/R4B/valueset.html) **R4** [R3](http://hl7.org/fhir/STU3/valueset.html) [R2](http://hl7.org/fhir/DSTU2/valueset.html)

- [Content](#)
- [Examples](valueset-examples.html)
- [Detailed Descriptions](valueset-definitions.html)
- [Mappings](valueset-mappings.html)
- [Profiles & Extensions](valueset-profiles.html)
- [Operations](valueset-operations.html)
- [R3 Conversions](valueset-version-maps.html)

# 4.9 Resource ValueSet - Content

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [Vocabulary](http://www.hl7.org/Special/committees/Vocab/index.cfm)  Work Group | [Maturity Level](versions.html#maturity): [N](versions.html#std-process) | [Normative](versions.html#std-process "Standard Status") (from v4.0.0) | [Security Category](security.html#SecPrivConsiderations): Anonymous | [Compartments](compartmentdefinition.html): Not linked to any defined compartments |

|  |  |
| --- | --- |
|  | This page has been approved as part of an [ANSI](https://www.ansi.org/)  standard. See the [Conformance](ansi-conformance.html) Package for further details. |

A ValueSet resource instance specifies a set of codes drawn from one or more code systems, intended for use in a particular context. Value sets link between [CodeSystem](codesystem.html) definitions and their use in [coded elements](terminologies.html).

## 4.9.1 Scope and Usage

The FHIR terminology specification is based on two key concepts, originally defined in [HL7 v3 Core Principles ![](external.png)](http://www.hl7.org/documentcenter/public/standards/V3/core_principles/infrastructure/coreprinciples/v3modelcoreprinciples.html):

- `CodeSystem` - declares the existence of and describes a code system or code system supplement and its key properties, and optionally defines a part or all of its content. Also known as Ontology, Terminology, or Enumeration
- `ValueSet` - specifies a set of codes drawn from one or more code systems, intended for use in a particular context. Value sets link between [CodeSystem](codesystem.html) definitions and their use in [coded elements](terminologies.html)

Value sets have 2 aspects:

- `.compose`: A definition of which codes are intended to be in the value set ("intension")
- `.expansion`: The list of codes that are actually in the value set under a given set of conditions ("extension") - see [Value Set Expansion](valueset.html#expansion)

The `ValueSet` resource can carry either the `.compose` or the `.expansion`,
both of them, or neither of them (if only the metadata is being represented). There is an ["$expand" operation](valueset-operation-expand.html) which can be used to ask a server to generate
an expansion given the composition rules, in a particular context, and a ["$validate-code" operation](valueset-operation-validate-code.html) which can be used to ask a server to
check whether a given code or concept is in the value set in a particular context.

## 4.9.2 Boundaries and Relationships

Value Sets are used by many resources:

- Value sets use [CodeSystem](codesystem.html) resources by referring to them via their canonical reference.
- Value sets are used in [StructureDefinition](structuredefinition.html),
  [OperationDefinition](operationdefinition.html#OperationDefinition), [Questionnaire](questionnaire.html), and other resources
  to specify the allowable contents for coded elements, or business rules for data processing
- [ConceptMap resources](conceptmap.html) describe mappings between value sets
- [DataRequirement](metadatatypes.html#DataRequirement) data types to specify data processing conditions

For a full list of uses, see below.

The Characteristics of the `ValueSet` resource are derived from Formal Value Set Definitions:

- The ValueSet resource design is based on the functionality described in the [OMG CTS 2 ![](external.png)](http://www.omg.org/spec/CTS2/1.0/) specification, along
  with metadata in the HL7 Value Set Definition specification. Value set resources can be converted to CTS2
  value set or code system instances.
- The value set resource is aligned with the [Value Set Definition ![](external.png)](https://confluence.hl7.org/display/VOC/Characteristics+of+a+Value+Set+Definition+%28VSD%29+Project) (VSD) project.
  Not all of the elements defined by the VSD are part of the base resource - some are defined as part of the [ValueSet Extensions](valueset-extensions.html).
  In the ValueSet resource, the `compose` element is the VSD "Content Logical definition".

## 4.9.3 Background and Context

When using value sets, proper differentiation between a code system and a value set is important.
This is one very common area where significant clinical safety risks occur in practice. Implementers
should be familiar with the content in [Using Codes in Resources](terminologies.html).

### 4.9.3.1 ValueSet Identification

A value set has 3 identifiers:

- `ValueSet.id`: the [logical id](resource.html#id) on the system that holds the value set - this changes as it moves from server to server (this id, with the server address prepended, is called the 'literal identity' of the resource)
- `ValueSet.url`: the canonical URL that never changes for this value set - it is the same in every copy. The element is named `url` rather than `uri` for legacy reasons and to strongly encourage providing a resolvable URL as the identifier whenever possible. Ideally, it should be a literal URL that is the location of the master version of the value set, though this is not always possible
- `ValueSet.identifier`: A system/value pair that is used to identify the value set in other contexts (such as an OID in an [HL7 v3 ![](external.png)](https://www.hl7.org/implement/standards/product_brief.cfm?product_id=186) specification)

In addition, any expansion for the value set also has `ValueSet.expansion.identifier` which uniquely identifies each expansion.
For further information regarding resource identification, see [Resource Identity](resource.html#id).

This means that each value set has 2 different URLs that can be used to reference it - its canonical URL (the `url` element), and its local location from which it may be retrieved (which includes the `id` element). Because it is common practice to copy (cache) value sets locally, most references to value sets use the canonical URL.

> For example, the value sets published as part of FHIR all have a location ("literal") URI which is the URL where they may be accessed in the FHIR specification itself. Note, though, that while a new version of the FHIR Specification is being prepared, value sets that are published in the drafts will not be found in the current published FHIR specification at their canonical URL.

Alternatively, the `identifier` and `version` elements may be used to reference this value set in a
design, a profile, a [CDA ![](external.png)](http://www.hl7.org/implement/standards/product_brief.cfm?product_id=7) template
or [HL7 v3 ![](external.png)](https://www.hl7.org/implement/standards/product_brief.cfm?product_id=186) message (in the CD data
type valueSet and valueSetVersion properties). These different contexts may make additional restrictions on the
possible values of these elements. The `identifier` is generally not needed when using value sets in
a FHIR context, where the canonical URL is always the focus.

### 4.9.3.2 Intensional vs Extensional

A value set may be described as intensional or extensional. The terms intensional and extensional come from the fields of mathematical logic and set theory.

An intensional value set is typically algorithmically defined. That is, the code group is defined as a rule e.g. all codes with the word diabetes in their
description). The key benefit of intensional code groups is that they can be dynamically updated. Dynamic updating helps healthcare organizations keep
current when new drugs (and their associated codes) become available or codes for diseases and other clinical concepts change. An intensional value set
designed to contain all of the drugs in the beta blocker category can automatically receive a new beta blocker’s code as soon as it hits the market.

Extensional value sets, meanwhile, are enumerated lists of codes where each code is listed individually. This gives the author and user of the value set
more control over the which codes are in the value set, but there is a greater maintenance burden to ensure that the value set is kept up to date.

This resource is referenced by [DataRequirement](metadatatypes.html#DataRequirement), [ElementDefinition](elementdefinition.html#ElementDefinition), [CodeSystem](codesystem.html#CodeSystem), [ConceptMap](conceptmap.html#ConceptMap), [ObservationDefinition](observationdefinition.html#ObservationDefinition), [OperationDefinition](operationdefinition.html#OperationDefinition), [Questionnaire](questionnaire.html#Questionnaire), [ResearchElementDefinition](researchelementdefinition.html#ResearchElementDefinition) and itself

## 4.9.4 Resource Content

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
| .. [ValueSet](valueset-definitions.html#ValueSet "ValueSet : A ValueSet resource instance specifies a set of codes drawn from one or more code systems, intended for use in a particular context. Value sets link between [[[CodeSystem]]] definitions and their use in [coded elements](terminologies.html).") | [I](conformance-rules.html#constraints "This element has or is affected by some invariants")[N](versions.html#std-process "Standards Status = Normative") |  | [DomainResource](domainresource.html) | A set of codes drawn from one or more code systems + Warning: Name should be usable as an identifier for the module by machine processing applications such as code generation Elements defined in Ancestors: [id](resource.html#Resource "The logical id of the resource, as used in the URL for the resource. Once assigned, this value never changes."), [meta](resource.html#Resource "The metadata about the resource. This is content that is maintained by the infrastructure. Changes to the content might not always be associated with version changes to the resource."), [implicitRules](resource.html#Resource "A reference to a set of rules that were followed when the resource was constructed, and which must be understood when processing the content. Often, this is a reference to an implementation guide that defines the special rules along with other profiles etc."), [language](resource.html#Resource "The base language in which the resource is written."), [text](domainresource.html#DomainResource "A human-readable narrative that contains a summary of the resource and can be used to represent the content of the resource to a human. The narrative need not encode all the structured data, but is required to contain sufficient detail to make it \"clinically safe\" for a human to just read the narrative. Resource definitions may define what content should be represented in the narrative to ensure clinical safety."), [contained](domainresource.html#DomainResource "These resources do not have an independent existence apart from the resource that contains them - they cannot be identified independently, and nor can they have their own independent transaction scope."), [extension](domainresource.html#DomainResource "May be used to represent additional information that is not part of the basic definition of the resource. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension."), [modifierExtension](domainresource.html#DomainResource "May be used to represent additional information that is not part of the basic definition of the resource and that modifies the understanding of the element that contains it and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer is allowed to define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.  Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).") |
| ... [url](valueset-definitions.html#ValueSet.url "ValueSet.url : An absolute URI that is used to identify this value set when it is referenced in a specification, model, design or an instance; also called its canonical identifier. This SHOULD be globally unique and SHOULD be a literal address at which at which an authoritative instance of this value set is (or will be) published. This URL can be the target of a canonical reference. It SHALL remain the same when the value set is stored on different servers.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [uri](datatypes.html#uri) | Canonical identifier for this value set, represented as a URI (globally unique) |
| ... [identifier](valueset-definitions.html#ValueSet.identifier "ValueSet.identifier : A formal identifier that is used to identify this value set when it is represented in other formats, or referenced in a specification, model, design or an instance.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [Identifier](datatypes.html#Identifier) | Additional identifier for the value set (business identifier) |
| ... [version](valueset-definitions.html#ValueSet.version "ValueSet.version : The identifier that is used to identify this version of the value set when it is referenced in a specification, model, design or instance. This is an arbitrary value managed by the value set author and is not expected to be globally unique. For example, it might be a timestamp (e.g. yyyymmdd) if a managed version is not available. There is also no expectation that versions can be placed in a lexicographical sequence.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | Business version of the value set |
| ... [name](valueset-definitions.html#ValueSet.name "ValueSet.name : A natural language name identifying the value set. This name should be usable as an identifier for the module by machine processing applications such as code generation.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..1 | [string](datatypes.html#string) | Name for this value set (computer friendly) |
| ... [title](valueset-definitions.html#ValueSet.title "ValueSet.title : A short, descriptive, user-friendly title for the value set.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | Name for this value set (human friendly) |
| ... [status](valueset-definitions.html#ValueSet.status "ValueSet.status : The status of this value set. Enables tracking the life-cycle of the content. The status of the value set applies to the value set definition (ValueSet.compose) and the associated ValueSet metadata. Expansions do not have a state.") | [?!](conformance-rules.html#isModifier "This element is a modifier element")[Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [code](datatypes.html#code) | draft | active | retired | unknown [PublicationStatus](valueset-publication-status.html "The lifecycle status of an artifact.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ... [experimental](valueset-definitions.html#ValueSet.experimental "ValueSet.experimental : A Boolean value to indicate that this value set is authored for testing purposes (or education/evaluation/marketing) and is not intended to be used for genuine usage.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [boolean](datatypes.html#boolean) | For testing purposes, not real usage |
| ... [date](valueset-definitions.html#ValueSet.date "ValueSet.date : The date (and optionally time) when the value set was created or revised (e.g. the 'content logical definition').") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [dateTime](datatypes.html#dateTime) | Date last changed |
| ... [publisher](valueset-definitions.html#ValueSet.publisher "ValueSet.publisher : The name of the organization or individual that published the value set.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | Name of the publisher (organization or individual) |
| ... [contact](valueset-definitions.html#ValueSet.contact "ValueSet.contact : Contact details to assist a user in finding and communicating with the publisher.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [ContactDetail](metadatatypes.html#ContactDetail) | Contact details for the publisher |
| ... [description](valueset-definitions.html#ValueSet.description "ValueSet.description : A free text natural language description of the value set from a consumer's perspective. The textual description specifies the span of meanings for concepts to be included within the Value Set Expansion, and also may specify the intended use and limitations of the Value Set.") |  | 0..1 | [markdown](datatypes.html#markdown) | Natural language description of the value set |
| ... [useContext](valueset-definitions.html#ValueSet.useContext "ValueSet.useContext : The content was developed with a focus and intent of supporting the contexts that are listed. These contexts may be general categories (gender, age, ...) or may be references to specific programs (insurance plans, studies, ...) and may be used to assist with indexing and searching for appropriate value set instances.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[TU](versions.html#std-process "Standards Status = Trial Use") | 0..\* | [UsageContext](metadatatypes.html#UsageContext) | The context that the content is intended to support |
| ... [jurisdiction](valueset-definitions.html#ValueSet.jurisdiction "ValueSet.jurisdiction : A legal or geographic region in which the value set is intended to be used.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [CodeableConcept](datatypes.html#CodeableConcept) | Intended jurisdiction for value set (if applicable) [Jurisdiction](valueset-jurisdiction.html "Countries and regions within which this artifact is targeted for use.") ([Extensible](terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept (based on human review), alternate codings (or, data type allowing, text) may be included instead.")) |
| ... [immutable](valueset-definitions.html#ValueSet.immutable "ValueSet.immutable : If this is set to 'true', then no new versions of the content logical definition can be created.  Note: Other metadata might still change.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [boolean](datatypes.html#boolean) | Indicates whether or not any change to the content logical definition may occur |
| ... [purpose](valueset-definitions.html#ValueSet.purpose "ValueSet.purpose : Explanation of why this value set is needed and why it has been designed as it has.") |  | 0..1 | [markdown](datatypes.html#markdown) | Why this value set is defined |
| ... [copyright](valueset-definitions.html#ValueSet.copyright "ValueSet.copyright : A copyright statement relating to the value set and/or its contents. Copyright statements are generally legal restrictions on the use and publishing of the value set.") |  | 0..1 | [markdown](datatypes.html#markdown) | Use and/or publishing restrictions |
| ... [compose](valueset-definitions.html#ValueSet.compose "ValueSet.compose : A set of criteria that define the contents of the value set by including or excluding codes selected from the specified code system(s) that the value set draws from. This is also known as the Content Logical Definition (CLD).") |  | 0..1 | [BackboneElement](backboneelement.html) | Content logical definition of the value set (CLD) |
| .... [lockedDate](valueset-definitions.html#ValueSet.compose.lockedDate "ValueSet.compose.lockedDate : The Locked Date is  the effective date that is used to determine the version of all referenced Code Systems and Value Set Definitions included in the compose that are not already tied to a specific version.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [date](datatypes.html#date) | Fixed date for references with no specified version (transitive) |
| .... [inactive](valueset-definitions.html#ValueSet.compose.inactive "ValueSet.compose.inactive : Whether inactive codes - codes that are not approved for current use - are in the value set. If inactive = true, inactive codes are to be included in the expansion, if inactive = false, the inactive codes will not be included in the expansion. If absent, the behavior is determined by the implementation, or by the applicable $expand parameters (but generally, inactive codes would be expected to be included).") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [boolean](datatypes.html#boolean) | Whether inactive codes are in the value set |
| .... [include](valueset-definitions.html#ValueSet.compose.include "ValueSet.compose.include : Include one or more codes from a code system or other value set(s).") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 1..\* | [BackboneElement](backboneelement.html) | Include one or more codes from a code system or other value set(s) + Rule: A value set include/exclude SHALL have a value set or a system + Rule: A value set with concepts or filters SHALL include a system + Rule: Cannot have both concept and filter |
| ..... [system](valueset-definitions.html#ValueSet.compose.include.system "ValueSet.compose.include.system : An absolute URI which is the code system from which the selected codes come from.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..1 | [uri](datatypes.html#uri) | The system the codes come from |
| ..... [version](valueset-definitions.html#ValueSet.compose.include.version "ValueSet.compose.include.version : The version of the code system that the codes are selected from, or the special version '*' for all versions.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | Specific version of the code system referred to |
| ..... [concept](valueset-definitions.html#ValueSet.compose.include.concept "ValueSet.compose.include.concept : Specifies a concept to be included or excluded.") | [I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..\* | [BackboneElement](backboneelement.html) | A concept defined in the system |
| ...... [code](valueset-definitions.html#ValueSet.compose.include.concept.code "ValueSet.compose.include.concept.code : Specifies a code for the concept to be included or excluded.") |  | 1..1 | [code](datatypes.html#code) | Code or expression from system |
| ...... [display](valueset-definitions.html#ValueSet.compose.include.concept.display "ValueSet.compose.include.concept.display : The text to display to the user for this concept in the context of this valueset. If no display is provided, then applications using the value set use the display specified for the code by the system.") |  | 0..1 | [string](datatypes.html#string) | Text to display for this code for this value set in this valueset |
| ...... [designation](valueset-definitions.html#ValueSet.compose.include.concept.designation "ValueSet.compose.include.concept.designation : Additional representations for this concept when used in this value set - other languages, aliases, specialized purposes, used for particular purposes, etc.") |  | 0..\* | [BackboneElement](backboneelement.html) | Additional representations for this concept |
| ....... [language](valueset-definitions.html#ValueSet.compose.include.concept.designation.language "ValueSet.compose.include.concept.designation.language : The language this designation is defined for.") |  | 0..1 | [code](datatypes.html#code) | Human language of the designation [Common Languages](valueset-languages.html "A human language.") ([Preferred](terminologies.html#preferred "Instances are encouraged to draw from the specified codes for interoperability purposes but are not required to do so to be considered conformant.") but limited to [AllLanguages](valueset-all-languages.html)) |
| ....... [use](valueset-definitions.html#ValueSet.compose.include.concept.designation.use "ValueSet.compose.include.concept.designation.use : A code that represents types of uses of designations.") |  | 0..1 | [Coding](datatypes.html#Coding) | Types of uses of designations [Designation Use](valueset-designation-use.html "Details of how a designation would be used.") ([Extensible](terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept (based on human review), alternate codings (or, data type allowing, text) may be included instead.")) |
| ....... [value](valueset-definitions.html#ValueSet.compose.include.concept.designation.value "ValueSet.compose.include.concept.designation.value : The text value for this designation.") |  | 1..1 | [string](datatypes.html#string) | The text value for this designation |
| ..... [filter](valueset-definitions.html#ValueSet.compose.include.filter "ValueSet.compose.include.filter : Select concepts by specify a matching criterion based on the properties (including relationships) defined by the system, or on filters defined by the system. If multiple filters are specified, they SHALL all be true.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..\* | [BackboneElement](backboneelement.html) | Select codes/concepts by their properties (including relationships) |
| ...... [property](valueset-definitions.html#ValueSet.compose.include.filter.property "ValueSet.compose.include.filter.property : A code that identifies a property or a filter defined in the code system.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [code](datatypes.html#code) | A property/filter defined by the code system |
| ...... [op](valueset-definitions.html#ValueSet.compose.include.filter.op "ValueSet.compose.include.filter.op : The kind of operation to perform as a part of the filter criteria.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [code](datatypes.html#code) | = | is-a | descendent-of | is-not-a | regex | in | not-in | generalizes | exists [FilterOperator](valueset-filter-operator.html "The kind of operation to perform as a part of a property based filter.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ...... [value](valueset-definitions.html#ValueSet.compose.include.filter.value "ValueSet.compose.include.filter.value : The match value may be either a code defined by the system, or a string value, which is a regex match on the literal string of the property value  (if the filter represents a property defined in CodeSystem) or of the system filter value (if the filter represents a filter defined in CodeSystem) when the operation is 'regex', or one of the values (true and false), when the operation is 'exists'.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [string](datatypes.html#string) | Code from the system, or regex criteria, or boolean value for exists |
| ..... [valueSet](valueset-definitions.html#ValueSet.compose.include.valueSet "ValueSet.compose.include.valueSet : Selects the concepts found in this value set (based on its value set definition). This is an absolute URI that is a reference to ValueSet.url.  If multiple value sets are specified this includes the union of the contents of all of the referenced value sets.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..\* | [canonical](datatypes.html#canonical)([ValueSet](valueset.html)) | Select the contents included in this value set |
| .... [exclude](valueset-definitions.html#ValueSet.compose.exclude "ValueSet.compose.exclude : Exclude one or more codes from the value set based on code system filters and/or other value sets.") | [I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..\* | see [include](#ValueSet.compose.include "ValueSet.compose.include") | Explicitly exclude codes from a code system or other value sets |
| ... [expansion](valueset-definitions.html#ValueSet.expansion "ValueSet.expansion : A value set can also be \"expanded\", where the value set is turned into a simple collection of enumerated codes. This element holds the expansion, if it has been performed.") |  | 0..1 | [BackboneElement](backboneelement.html) | Used when the value set is "expanded" |
| .... [identifier](valueset-definitions.html#ValueSet.expansion.identifier "ValueSet.expansion.identifier : An identifier that uniquely identifies this expansion of the valueset, based on a unique combination of the provided parameters, the system default parameters, and the underlying system code system versions etc. Systems may re-use the same identifier as long as those factors remain the same, and the expansion is the same, but are not required to do so. This is a business identifier.") |  | 0..1 | [uri](datatypes.html#uri) | Identifies the value set expansion (business identifier) |
| .... [timestamp](valueset-definitions.html#ValueSet.expansion.timestamp "ValueSet.expansion.timestamp : The time at which the expansion was produced by the expanding system.") |  | 1..1 | [dateTime](datatypes.html#dateTime) | Time ValueSet expansion happened |
| .... [total](valueset-definitions.html#ValueSet.expansion.total "ValueSet.expansion.total : The total number of concepts in the expansion. If the number of concept nodes in this resource is less than the stated number, then the server can return more using the offset parameter.") |  | 0..1 | [integer](datatypes.html#integer) | Total number of codes in the expansion |
| .... [offset](valueset-definitions.html#ValueSet.expansion.offset "ValueSet.expansion.offset : If paging is being used, the offset at which this resource starts.  I.e. this resource is a partial view into the expansion. If paging is not being used, this element SHALL NOT be present.") |  | 0..1 | [integer](datatypes.html#integer) | Offset at which this resource starts |
| .... [parameter](valueset-definitions.html#ValueSet.expansion.parameter "ValueSet.expansion.parameter : A parameter that controlled the expansion process. These parameters may be used by users of expanded value sets to check whether the expansion is suitable for a particular purpose, or to pick the correct expansion.") |  | 0..\* | [BackboneElement](backboneelement.html) | Parameter that controlled the expansion process |
| ..... [name](valueset-definitions.html#ValueSet.expansion.parameter.name "ValueSet.expansion.parameter.name : Name of the input parameter to the $expand operation; may be a server-assigned name for additional default or other server-supplied parameters used to control the expansion process.") |  | 1..1 | [string](datatypes.html#string) | Name as assigned by the client or server |
| ..... [value[x]](valueset-definitions.html#ValueSet.expansion.parameter.value_x_ "ValueSet.expansion.parameter.value[x] : The value of the parameter.") |  | 0..1 |  | Value of the named parameter |
| ...... valueString |  |  | [string](datatypes.html#string) |  |
| ...... valueBoolean |  |  | [boolean](datatypes.html#boolean) |  |
| ...... valueInteger |  |  | [integer](datatypes.html#integer) |  |
| ...... valueDecimal |  |  | [decimal](datatypes.html#decimal) |  |
| ...... valueUri |  |  | [uri](datatypes.html#uri) |  |
| ...... valueCode |  |  | [code](datatypes.html#code) |  |
| ...... valueDateTime |  |  | [dateTime](datatypes.html#dateTime) |  |
| .... [contains](valueset-definitions.html#ValueSet.expansion.contains "ValueSet.expansion.contains : The codes that are contained in the value set expansion.") | [I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..\* | [BackboneElement](backboneelement.html) | Codes in the value set + Rule: SHALL have a code or a display + Rule: Must have a code if not abstract + Rule: Must have a system if a code is present |
| ..... [system](valueset-definitions.html#ValueSet.expansion.contains.system "ValueSet.expansion.contains.system : An absolute URI which is the code system in which the code for this item in the expansion is defined.") |  | 0..1 | [uri](datatypes.html#uri) | System value for the code |
| ..... [abstract](valueset-definitions.html#ValueSet.expansion.contains.abstract "ValueSet.expansion.contains.abstract : If true, this entry is included in the expansion for navigational purposes, and the user cannot select the code directly as a proper value.") |  | 0..1 | [boolean](datatypes.html#boolean) | If user cannot select this entry |
| ..... [inactive](valueset-definitions.html#ValueSet.expansion.contains.inactive "ValueSet.expansion.contains.inactive : If the concept is inactive in the code system that defines it. Inactive codes are those that are no longer to be used, but are maintained by the code system for understanding legacy data. It might not be known or specified whether an concept is inactive (and it may depend on the context of use).") |  | 0..1 | [boolean](datatypes.html#boolean) | If concept is inactive in the code system |
| ..... [version](valueset-definitions.html#ValueSet.expansion.contains.version "ValueSet.expansion.contains.version : The version of the code system from this code was taken. Note that a well-maintained code system does not need the version reported, because the meaning of codes is consistent across versions. However this cannot consistently be assured, and when the meaning is not guaranteed to be consistent, the version SHOULD be exchanged.") |  | 0..1 | [string](datatypes.html#string) | Version in which this code/display is defined |
| ..... [code](valueset-definitions.html#ValueSet.expansion.contains.code "ValueSet.expansion.contains.code : The code for this item in the expansion hierarchy. If this code is missing the entry in the hierarchy is a place holder (abstract) and does not represent a valid code in the value set.") | [I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..1 | [code](datatypes.html#code) | Code - if blank, this is not a selectable code |
| ..... [display](valueset-definitions.html#ValueSet.expansion.contains.display "ValueSet.expansion.contains.display : The recommended display for this item in the expansion.") | [I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..1 | [string](datatypes.html#string) | User display for the concept |
| ..... [designation](valueset-definitions.html#ValueSet.expansion.contains.designation "ValueSet.expansion.contains.designation : Additional representations for this item - other languages, aliases, specialized purposes, used for particular purposes, etc. These are relevant when the conditions of the expansion do not fix to a single correct representation.") |  | 0..\* | see [designation](#ValueSet.compose.include.concept.designation "ValueSet.compose.include.concept.designation") | Additional representations for this item |
| ..... [contains](valueset-definitions.html#ValueSet.expansion.contains.contains "ValueSet.expansion.contains.contains : Other codes and entries contained under this entry in the hierarchy.") |  | 0..\* | see [contains](#ValueSet.expansion.contains "ValueSet.expansion.contains") | Codes contained under this entry |
| [doco Documentation for this format](formats.html#table "Legend for this format") | | | | |

**UML Diagram** ([Legend](formats.html#uml))

**XML Template**

```

<ValueSet xmlns="http://hl7.org/fhir"> ![doco](help.png)
 <!-- from Resource: id, meta, implicitRules, and language -->
 <!-- from DomainResource: text, contained, extension, and modifierExtension -->
 <url value="[uri]"/><!-- 0..1 Canonical identifier for this value set, represented as a URI (globally unique) -->
 <identifier><!-- 0..* Identifier Additional identifier for the value set (business identifier) --></identifier>
 <version value="[string]"/><!-- 0..1 Business version of the value set -->
 <name value="[string]"/><!-- ![??](lock.png) 0..1 Name for this value set (computer friendly) -->
 <title value="[string]"/><!-- 0..1 Name for this value set (human friendly) -->
 <status value="[code]"/><!-- 1..1 draft | active | retired | unknown -->
 <experimental value="[boolean]"/><!-- 0..1 For testing purposes, not real usage -->
 <date value="[dateTime]"/><!-- 0..1 Date last changed -->
 <publisher value="[string]"/><!-- 0..1 Name of the publisher (organization or individual) -->
 <contact><!-- 0..* ContactDetail Contact details for the publisher --></contact>
 <description value="[markdown]"/><!-- 0..1 Natural language description of the value set -->
 <useContext><!-- 0..* UsageContext The context that the content is intended to support --></useContext>
 <jurisdiction><!-- 0..* CodeableConcept Intended jurisdiction for value set (if applicable) --></jurisdiction>
 <immutable value="[boolean]"/><!-- 0..1 Indicates whether or not any change to the content logical definition may occur -->
 <purpose value="[markdown]"/><!-- 0..1 Why this value set is defined -->
 <copyright value="[markdown]"/><!-- 0..1 Use and/or publishing restrictions -->
 <compose>  <!-- 0..1 Content logical definition of the value set (CLD) -->
  <lockedDate value="[date]"/><!-- 0..1 Fixed date for references with no specified version (transitive) -->
  <inactive value="[boolean]"/><!-- 0..1 Whether inactive codes are in the value set -->
  <include>  <!-- 1..* Include one or more codes from a code system or other value set(s) -->
   <system value="[uri]"/><!-- ![??](lock.png) 0..1 The system the codes come from -->
   <version value="[string]"/><!-- 0..1 Specific version of the code system referred to -->
   <concept>  <!-- ![??](lock.png) 0..* A concept defined in the system -->
    <code value="[code]"/><!-- 1..1 Code or expression from system -->
    <display value="[string]"/><!-- 0..1 Text to display for this code for this value set in this valueset -->
    <designation>  <!-- 0..* Additional representations for this concept -->
     <language value="[code]"/><!-- 0..1 Human language of the designation -->
     <use><!-- 0..1 Coding Types of uses of designations --></use>
     <value value="[string]"/><!-- 1..1 The text value for this designation -->
    </designation>
   </concept>
   <filter>  <!-- ![??](lock.png) 0..* Select codes/concepts by their properties (including relationships) -->
    <property value="[code]"/><!-- 1..1 A property/filter defined by the code system -->
    <op value="[code]"/><!-- 1..1 = | is-a | descendent-of | is-not-a | regex | in | not-in | generalizes | exists -->
    <value value="[string]"/><!-- 1..1 Code from the system, or regex criteria, or boolean value for exists -->
   </filter>
   <valueSet><!-- ![??](lock.png) 0..* canonical(ValueSet) Select the contents included in this value set --></valueSet>
  </include>
  <exclude><!-- ![??](lock.png) 0..* Content as for ValueSet.compose.include Explicitly exclude codes from a code system or other value sets --></exclude>
 </compose>
 <expansion>  <!-- 0..1 Used when the value set is "expanded" -->
  <identifier value="[uri]"/><!-- 0..1 Identifies the value set expansion (business identifier) -->
  <timestamp value="[dateTime]"/><!-- 1..1 Time ValueSet expansion happened -->
  <total value="[integer]"/><!-- 0..1 Total number of codes in the expansion -->
  <offset value="[integer]"/><!-- 0..1 Offset at which this resource starts -->
  <parameter>  <!-- 0..* Parameter that controlled the expansion process -->
   <name value="[string]"/><!-- 1..1 Name as assigned by the client or server -->
   <value[x]><!-- 0..1 string|boolean|integer|decimal|uri|code|dateTime Value of the named parameter --></value[x]>
  </parameter>
  <contains>  <!-- 0..* Codes in the value set -->
   <system value="[uri]"/><!-- 0..1 System value for the code -->
   <abstract value="[boolean]"/><!-- 0..1 If user cannot select this entry -->
   <inactive value="[boolean]"/><!-- 0..1 If concept is inactive in the code system -->
   <version value="[string]"/><!-- 0..1 Version in which this code/display is defined -->
   <code value="[code]"/><!-- ![??](lock.png) 0..1 Code - if blank, this is not a selectable code -->
   <display value="[string]"/><!-- ![??](lock.png) 0..1 User display for the concept -->
   <designation><!-- 0..* Content as for ValueSet.compose.include.concept.designation Additional representations for this item --></designation>
   <contains><!-- 0..* Content as for ValueSet.expansion.contains Codes contained under this entry --></contains>
  </contains>
 </expansion>
</ValueSet>
```

**JSON Template**

```

{![doco](help.png)
  "resourceType" : "ValueSet",
  // from Resource: id, meta, implicitRules, and language
  // from DomainResource: text, contained, extension, and modifierExtension
  "url" : "<uri>", // Canonical identifier for this value set, represented as a URI (globally unique)
  "identifier" : [{ Identifier }], // Additional identifier for the value set (business identifier)
  "version" : "<string>", // Business version of the value set
  "name" : "<string>", // C? Name for this value set (computer friendly)
  "title" : "<string>", // Name for this value set (human friendly)
  "status" : "<code>", // R!  draft | active | retired | unknown
  "experimental" : <boolean>, // For testing purposes, not real usage
  "date" : "<dateTime>", // Date last changed
  "publisher" : "<string>", // Name of the publisher (organization or individual)
  "contact" : [{ ContactDetail }], // Contact details for the publisher
  "description" : "<markdown>", // Natural language description of the value set
  "useContext" : [{ UsageContext }], // The context that the content is intended to support
  "jurisdiction" : [{ CodeableConcept }], // Intended jurisdiction for value set (if applicable)
  "immutable" : <boolean>, // Indicates whether or not any change to the content logical definition may occur
  "purpose" : "<markdown>", // Why this value set is defined
  "copyright" : "<markdown>", // Use and/or publishing restrictions
  "compose" : { // Content logical definition of the value set (CLD)
    "lockedDate" : "<date>", // Fixed date for references with no specified version (transitive)
    "inactive" : <boolean>, // Whether inactive codes are in the value set
    "include" : [{ // R!  Include one or more codes from a code system or other value set(s)
      "system" : "<uri>", // C? The system the codes come from
      "version" : "<string>", // Specific version of the code system referred to
      "concept" : [{ // C? A concept defined in the system
        "code" : "<code>", // R!  Code or expression from system
        "display" : "<string>", // Text to display for this code for this value set in this valueset
        "designation" : [{ // Additional representations for this concept
          "language" : "<code>", // Human language of the designation
          "use" : { Coding }, // Types of uses of designations
          "value" : "<string>" // R!  The text value for this designation
        }]
      }],
      "filter" : [{ // C? Select codes/concepts by their properties (including relationships)
        "property" : "<code>", // R!  A property/filter defined by the code system
        "op" : "<code>", // R!  = | is-a | descendent-of | is-not-a | regex | in | not-in | generalizes | exists
        "value" : "<string>" // R!  Code from the system, or regex criteria, or boolean value for exists
      }],
      "valueSet" : [{ canonical(ValueSet) }] // C? Select the contents included in this value set
    }],
    "exclude" : [{ Content as for ValueSet.compose.include }] // C? Explicitly exclude codes from a code system or other value sets
  },
  "expansion" : { // Used when the value set is "expanded"
    "identifier" : "<uri>", // Identifies the value set expansion (business identifier)
    "timestamp" : "<dateTime>", // R!  Time ValueSet expansion happened
    "total" : <integer>, // Total number of codes in the expansion
    "offset" : <integer>, // Offset at which this resource starts
    "parameter" : [{ // Parameter that controlled the expansion process
      "name" : "<string>", // R!  Name as assigned by the client or server
      // value[x]: Value of the named parameter. One of these 7:
      "valueString" : "<string>"
      "valueBoolean" : <boolean>
      "valueInteger" : <integer>
      "valueDecimal" : <decimal>
      "valueUri" : "<uri>"
      "valueCode" : "<code>"
      "valueDateTime" : "<dateTime>"
    }],
    "contains" : [{ // Codes in the value set
      "system" : "<uri>", // System value for the code
      "abstract" : <boolean>, // If user cannot select this entry
      "inactive" : <boolean>, // If concept is inactive in the code system
      "version" : "<string>", // Version in which this code/display is defined
      "code" : "<code>", // C? Code - if blank, this is not a selectable code
      "display" : "<string>", // C? User display for the concept
      "designation" : [{ Content as for ValueSet.compose.include.concept.designation }], // Additional representations for this item
      "contains" : [{ Content as for ValueSet.expansion.contains }] // Codes contained under this entry
    }]
  }
}
```

**Turtle Template**

```

@prefix fhir: <http://hl7.org/fhir/> .![doco](help.png)


[ a fhir:ValueSet;
  fhir:nodeRole fhir:treeRoot; # if this is the parser root

  # from Resource: .id, .meta, .implicitRules, and .language
  # from DomainResource: .text, .contained, .extension, and .modifierExtension
  fhir:ValueSet.url [ uri ]; # 0..1 Canonical identifier for this value set, represented as a URI (globally unique)
  fhir:ValueSet.identifier [ Identifier ], ... ; # 0..* Additional identifier for the value set (business identifier)
  fhir:ValueSet.version [ string ]; # 0..1 Business version of the value set
  fhir:ValueSet.name [ string ]; # 0..1 Name for this value set (computer friendly)
  fhir:ValueSet.title [ string ]; # 0..1 Name for this value set (human friendly)
  fhir:ValueSet.status [ code ]; # 1..1 draft | active | retired | unknown
  fhir:ValueSet.experimental [ boolean ]; # 0..1 For testing purposes, not real usage
  fhir:ValueSet.date [ dateTime ]; # 0..1 Date last changed
  fhir:ValueSet.publisher [ string ]; # 0..1 Name of the publisher (organization or individual)
  fhir:ValueSet.contact [ ContactDetail ], ... ; # 0..* Contact details for the publisher
  fhir:ValueSet.description [ markdown ]; # 0..1 Natural language description of the value set
  fhir:ValueSet.useContext [ UsageContext ], ... ; # 0..* The context that the content is intended to support
  fhir:ValueSet.jurisdiction [ CodeableConcept ], ... ; # 0..* Intended jurisdiction for value set (if applicable)
  fhir:ValueSet.immutable [ boolean ]; # 0..1 Indicates whether or not any change to the content logical definition may occur
  fhir:ValueSet.purpose [ markdown ]; # 0..1 Why this value set is defined
  fhir:ValueSet.copyright [ markdown ]; # 0..1 Use and/or publishing restrictions
  fhir:ValueSet.compose [ # 0..1 Content logical definition of the value set (CLD)
    fhir:ValueSet.compose.lockedDate [ date ]; # 0..1 Fixed date for references with no specified version (transitive)
    fhir:ValueSet.compose.inactive [ boolean ]; # 0..1 Whether inactive codes are in the value set
    fhir:ValueSet.compose.include [ # 1..* Include one or more codes from a code system or other value set(s)
      fhir:ValueSet.compose.include.system [ uri ]; # 0..1 The system the codes come from
      fhir:ValueSet.compose.include.version [ string ]; # 0..1 Specific version of the code system referred to
      fhir:ValueSet.compose.include.concept [ # 0..* A concept defined in the system
        fhir:ValueSet.compose.include.concept.code [ code ]; # 1..1 Code or expression from system
        fhir:ValueSet.compose.include.concept.display [ string ]; # 0..1 Text to display for this code for this value set in this valueset
        fhir:ValueSet.compose.include.concept.designation [ # 0..* Additional representations for this concept
          fhir:ValueSet.compose.include.concept.designation.language [ code ]; # 0..1 Human language of the designation
          fhir:ValueSet.compose.include.concept.designation.use [ Coding ]; # 0..1 Types of uses of designations
          fhir:ValueSet.compose.include.concept.designation.value [ string ]; # 1..1 The text value for this designation
        ], ...;
      ], ...;
      fhir:ValueSet.compose.include.filter [ # 0..* Select codes/concepts by their properties (including relationships)
        fhir:ValueSet.compose.include.filter.property [ code ]; # 1..1 A property/filter defined by the code system
        fhir:ValueSet.compose.include.filter.op [ code ]; # 1..1 = | is-a | descendent-of | is-not-a | regex | in | not-in | generalizes | exists
        fhir:ValueSet.compose.include.filter.value [ string ]; # 1..1 Code from the system, or regex criteria, or boolean value for exists
      ], ...;
      fhir:ValueSet.compose.include.valueSet [ canonical(ValueSet) ], ... ; # 0..* Select the contents included in this value set
    ], ...;
    fhir:ValueSet.compose.exclude [ See ValueSet.compose.include ], ... ; # 0..* Explicitly exclude codes from a code system or other value sets
  ];
  fhir:ValueSet.expansion [ # 0..1 Used when the value set is "expanded"
    fhir:ValueSet.expansion.identifier [ uri ]; # 0..1 Identifies the value set expansion (business identifier)
    fhir:ValueSet.expansion.timestamp [ dateTime ]; # 1..1 Time ValueSet expansion happened
    fhir:ValueSet.expansion.total [ integer ]; # 0..1 Total number of codes in the expansion
    fhir:ValueSet.expansion.offset [ integer ]; # 0..1 Offset at which this resource starts
    fhir:ValueSet.expansion.parameter [ # 0..* Parameter that controlled the expansion process
      fhir:ValueSet.expansion.parameter.name [ string ]; # 1..1 Name as assigned by the client or server
      # ValueSet.expansion.parameter.value[x] : 0..1 Value of the named parameter. One of these 7
        fhir:ValueSet.expansion.parameter.valueString [ string ]
        fhir:ValueSet.expansion.parameter.valueBoolean [ boolean ]
        fhir:ValueSet.expansion.parameter.valueInteger [ integer ]
        fhir:ValueSet.expansion.parameter.valueDecimal [ decimal ]
        fhir:ValueSet.expansion.parameter.valueUri [ uri ]
        fhir:ValueSet.expansion.parameter.valueCode [ code ]
        fhir:ValueSet.expansion.parameter.valueDateTime [ dateTime ]
    ], ...;
    fhir:ValueSet.expansion.contains [ # 0..* Codes in the value set
      fhir:ValueSet.expansion.contains.system [ uri ]; # 0..1 System value for the code
      fhir:ValueSet.expansion.contains.abstract [ boolean ]; # 0..1 If user cannot select this entry
      fhir:ValueSet.expansion.contains.inactive [ boolean ]; # 0..1 If concept is inactive in the code system
      fhir:ValueSet.expansion.contains.version [ string ]; # 0..1 Version in which this code/display is defined
      fhir:ValueSet.expansion.contains.code [ code ]; # 0..1 Code - if blank, this is not a selectable code
      fhir:ValueSet.expansion.contains.display [ string ]; # 0..1 User display for the concept
      fhir:ValueSet.expansion.contains.designation [ See ValueSet.compose.include.concept.designation ], ... ; # 0..* Additional representations for this item
      fhir:ValueSet.expansion.contains.contains [ See ValueSet.expansion.contains ], ... ; # 0..* Codes contained under this entry
    ], ...;
  ];
]
```

**Changes since R3**

|  |  |
| --- | --- |
| [ValueSet](valueset.html#ValueSet) |  |
| ValueSet.status | - Change value set from http://hl7.org/fhir/ValueSet/publication-status to http://hl7.org/fhir/ValueSet/publication-status|4.0.1 |
| ValueSet.experimental | - No longer marked as Modifier |
| ValueSet.compose.include.concept.designation.language | - Change binding strength from extensible to preferred |
| ValueSet.compose.include.filter | - No longer marked as Modifier |
| ValueSet.compose.include.filter.op | - Change value set from http://hl7.org/fhir/ValueSet/filter-operator to http://hl7.org/fhir/ValueSet/filter-operator|4.0.1 |
| ValueSet.compose.include.filter.value | - Type changed from code to string |
| ValueSet.compose.include.valueSet | - Type changed from uri to canonical(ValueSet) |
| ValueSet.expansion.identifier | - Min Cardinality changed from 1 to 0 |
| ValueSet.expansion.parameter.value[x] | - Add Type dateTime |
| ValueSet.expansion.contains.abstract | - Default Value "false" removed |
| ValueSet.expansion.contains.inactive | - Default Value "false" removed |
| ValueSet.extensible | - deleted |

See the [Full Difference](diff.html) for further information

This analysis is available as [XML](valueset.diff.xml) or [JSON](valueset.diff.json).

See [R3 <--> R4 Conversion Maps](valueset-version-maps.html) (status = 8 tests that all execute ok. All tests pass round-trip testing and 8 r3 resources are invalid (0 errors).)

**Structure**

| [Name](formats.html#table "The logical name of the element") | [Flags](formats.html#table "Information about the use of the element") | [Card.](formats.html#table "Minimum and Maximum # of times the the element can appear in the instance") | [Type](formats.html#table "Reference to the type of the element") | [Description & Constraints](formats.html#table "Additional information about the element")[doco](formats.html#table "Legend for this format") |
| --- | --- | --- | --- | --- |
| .. [ValueSet](valueset-definitions.html#ValueSet "ValueSet : A ValueSet resource instance specifies a set of codes drawn from one or more code systems, intended for use in a particular context. Value sets link between [[[CodeSystem]]] definitions and their use in [coded elements](terminologies.html).") | [I](conformance-rules.html#constraints "This element has or is affected by some invariants")[N](versions.html#std-process "Standards Status = Normative") |  | [DomainResource](domainresource.html) | A set of codes drawn from one or more code systems + Warning: Name should be usable as an identifier for the module by machine processing applications such as code generation Elements defined in Ancestors: [id](resource.html#Resource "The logical id of the resource, as used in the URL for the resource. Once assigned, this value never changes."), [meta](resource.html#Resource "The metadata about the resource. This is content that is maintained by the infrastructure. Changes to the content might not always be associated with version changes to the resource."), [implicitRules](resource.html#Resource "A reference to a set of rules that were followed when the resource was constructed, and which must be understood when processing the content. Often, this is a reference to an implementation guide that defines the special rules along with other profiles etc."), [language](resource.html#Resource "The base language in which the resource is written."), [text](domainresource.html#DomainResource "A human-readable narrative that contains a summary of the resource and can be used to represent the content of the resource to a human. The narrative need not encode all the structured data, but is required to contain sufficient detail to make it \"clinically safe\" for a human to just read the narrative. Resource definitions may define what content should be represented in the narrative to ensure clinical safety."), [contained](domainresource.html#DomainResource "These resources do not have an independent existence apart from the resource that contains them - they cannot be identified independently, and nor can they have their own independent transaction scope."), [extension](domainresource.html#DomainResource "May be used to represent additional information that is not part of the basic definition of the resource. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension."), [modifierExtension](domainresource.html#DomainResource "May be used to represent additional information that is not part of the basic definition of the resource and that modifies the understanding of the element that contains it and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer is allowed to define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.  Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).") |
| ... [url](valueset-definitions.html#ValueSet.url "ValueSet.url : An absolute URI that is used to identify this value set when it is referenced in a specification, model, design or an instance; also called its canonical identifier. This SHOULD be globally unique and SHOULD be a literal address at which at which an authoritative instance of this value set is (or will be) published. This URL can be the target of a canonical reference. It SHALL remain the same when the value set is stored on different servers.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [uri](datatypes.html#uri) | Canonical identifier for this value set, represented as a URI (globally unique) |
| ... [identifier](valueset-definitions.html#ValueSet.identifier "ValueSet.identifier : A formal identifier that is used to identify this value set when it is represented in other formats, or referenced in a specification, model, design or an instance.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [Identifier](datatypes.html#Identifier) | Additional identifier for the value set (business identifier) |
| ... [version](valueset-definitions.html#ValueSet.version "ValueSet.version : The identifier that is used to identify this version of the value set when it is referenced in a specification, model, design or instance. This is an arbitrary value managed by the value set author and is not expected to be globally unique. For example, it might be a timestamp (e.g. yyyymmdd) if a managed version is not available. There is also no expectation that versions can be placed in a lexicographical sequence.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | Business version of the value set |
| ... [name](valueset-definitions.html#ValueSet.name "ValueSet.name : A natural language name identifying the value set. This name should be usable as an identifier for the module by machine processing applications such as code generation.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..1 | [string](datatypes.html#string) | Name for this value set (computer friendly) |
| ... [title](valueset-definitions.html#ValueSet.title "ValueSet.title : A short, descriptive, user-friendly title for the value set.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | Name for this value set (human friendly) |
| ... [status](valueset-definitions.html#ValueSet.status "ValueSet.status : The status of this value set. Enables tracking the life-cycle of the content. The status of the value set applies to the value set definition (ValueSet.compose) and the associated ValueSet metadata. Expansions do not have a state.") | [?!](conformance-rules.html#isModifier "This element is a modifier element")[Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [code](datatypes.html#code) | draft | active | retired | unknown [PublicationStatus](valueset-publication-status.html "The lifecycle status of an artifact.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ... [experimental](valueset-definitions.html#ValueSet.experimental "ValueSet.experimental : A Boolean value to indicate that this value set is authored for testing purposes (or education/evaluation/marketing) and is not intended to be used for genuine usage.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [boolean](datatypes.html#boolean) | For testing purposes, not real usage |
| ... [date](valueset-definitions.html#ValueSet.date "ValueSet.date : The date (and optionally time) when the value set was created or revised (e.g. the 'content logical definition').") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [dateTime](datatypes.html#dateTime) | Date last changed |
| ... [publisher](valueset-definitions.html#ValueSet.publisher "ValueSet.publisher : The name of the organization or individual that published the value set.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | Name of the publisher (organization or individual) |
| ... [contact](valueset-definitions.html#ValueSet.contact "ValueSet.contact : Contact details to assist a user in finding and communicating with the publisher.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [ContactDetail](metadatatypes.html#ContactDetail) | Contact details for the publisher |
| ... [description](valueset-definitions.html#ValueSet.description "ValueSet.description : A free text natural language description of the value set from a consumer's perspective. The textual description specifies the span of meanings for concepts to be included within the Value Set Expansion, and also may specify the intended use and limitations of the Value Set.") |  | 0..1 | [markdown](datatypes.html#markdown) | Natural language description of the value set |
| ... [useContext](valueset-definitions.html#ValueSet.useContext "ValueSet.useContext : The content was developed with a focus and intent of supporting the contexts that are listed. These contexts may be general categories (gender, age, ...) or may be references to specific programs (insurance plans, studies, ...) and may be used to assist with indexing and searching for appropriate value set instances.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[TU](versions.html#std-process "Standards Status = Trial Use") | 0..\* | [UsageContext](metadatatypes.html#UsageContext) | The context that the content is intended to support |
| ... [jurisdiction](valueset-definitions.html#ValueSet.jurisdiction "ValueSet.jurisdiction : A legal or geographic region in which the value set is intended to be used.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [CodeableConcept](datatypes.html#CodeableConcept) | Intended jurisdiction for value set (if applicable) [Jurisdiction](valueset-jurisdiction.html "Countries and regions within which this artifact is targeted for use.") ([Extensible](terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept (based on human review), alternate codings (or, data type allowing, text) may be included instead.")) |
| ... [immutable](valueset-definitions.html#ValueSet.immutable "ValueSet.immutable : If this is set to 'true', then no new versions of the content logical definition can be created.  Note: Other metadata might still change.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [boolean](datatypes.html#boolean) | Indicates whether or not any change to the content logical definition may occur |
| ... [purpose](valueset-definitions.html#ValueSet.purpose "ValueSet.purpose : Explanation of why this value set is needed and why it has been designed as it has.") |  | 0..1 | [markdown](datatypes.html#markdown) | Why this value set is defined |
| ... [copyright](valueset-definitions.html#ValueSet.copyright "ValueSet.copyright : A copyright statement relating to the value set and/or its contents. Copyright statements are generally legal restrictions on the use and publishing of the value set.") |  | 0..1 | [markdown](datatypes.html#markdown) | Use and/or publishing restrictions |
| ... [compose](valueset-definitions.html#ValueSet.compose "ValueSet.compose : A set of criteria that define the contents of the value set by including or excluding codes selected from the specified code system(s) that the value set draws from. This is also known as the Content Logical Definition (CLD).") |  | 0..1 | [BackboneElement](backboneelement.html) | Content logical definition of the value set (CLD) |
| .... [lockedDate](valueset-definitions.html#ValueSet.compose.lockedDate "ValueSet.compose.lockedDate : The Locked Date is  the effective date that is used to determine the version of all referenced Code Systems and Value Set Definitions included in the compose that are not already tied to a specific version.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [date](datatypes.html#date) | Fixed date for references with no specified version (transitive) |
| .... [inactive](valueset-definitions.html#ValueSet.compose.inactive "ValueSet.compose.inactive : Whether inactive codes - codes that are not approved for current use - are in the value set. If inactive = true, inactive codes are to be included in the expansion, if inactive = false, the inactive codes will not be included in the expansion. If absent, the behavior is determined by the implementation, or by the applicable $expand parameters (but generally, inactive codes would be expected to be included).") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [boolean](datatypes.html#boolean) | Whether inactive codes are in the value set |
| .... [include](valueset-definitions.html#ValueSet.compose.include "ValueSet.compose.include : Include one or more codes from a code system or other value set(s).") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 1..\* | [BackboneElement](backboneelement.html) | Include one or more codes from a code system or other value set(s) + Rule: A value set include/exclude SHALL have a value set or a system + Rule: A value set with concepts or filters SHALL include a system + Rule: Cannot have both concept and filter |
| ..... [system](valueset-definitions.html#ValueSet.compose.include.system "ValueSet.compose.include.system : An absolute URI which is the code system from which the selected codes come from.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..1 | [uri](datatypes.html#uri) | The system the codes come from |
| ..... [version](valueset-definitions.html#ValueSet.compose.include.version "ValueSet.compose.include.version : The version of the code system that the codes are selected from, or the special version '*' for all versions.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | Specific version of the code system referred to |
| ..... [concept](valueset-definitions.html#ValueSet.compose.include.concept "ValueSet.compose.include.concept : Specifies a concept to be included or excluded.") | [I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..\* | [BackboneElement](backboneelement.html) | A concept defined in the system |
| ...... [code](valueset-definitions.html#ValueSet.compose.include.concept.code "ValueSet.compose.include.concept.code : Specifies a code for the concept to be included or excluded.") |  | 1..1 | [code](datatypes.html#code) | Code or expression from system |
| ...... [display](valueset-definitions.html#ValueSet.compose.include.concept.display "ValueSet.compose.include.concept.display : The text to display to the user for this concept in the context of this valueset. If no display is provided, then applications using the value set use the display specified for the code by the system.") |  | 0..1 | [string](datatypes.html#string) | Text to display for this code for this value set in this valueset |
| ...... [designation](valueset-definitions.html#ValueSet.compose.include.concept.designation "ValueSet.compose.include.concept.designation : Additional representations for this concept when used in this value set - other languages, aliases, specialized purposes, used for particular purposes, etc.") |  | 0..\* | [BackboneElement](backboneelement.html) | Additional representations for this concept |
| ....... [language](valueset-definitions.html#ValueSet.compose.include.concept.designation.language "ValueSet.compose.include.concept.designation.language : The language this designation is defined for.") |  | 0..1 | [code](datatypes.html#code) | Human language of the designation [Common Languages](valueset-languages.html "A human language.") ([Preferred](terminologies.html#preferred "Instances are encouraged to draw from the specified codes for interoperability purposes but are not required to do so to be considered conformant.") but limited to [AllLanguages](valueset-all-languages.html)) |
| ....... [use](valueset-definitions.html#ValueSet.compose.include.concept.designation.use "ValueSet.compose.include.concept.designation.use : A code that represents types of uses of designations.") |  | 0..1 | [Coding](datatypes.html#Coding) | Types of uses of designations [Designation Use](valueset-designation-use.html "Details of how a designation would be used.") ([Extensible](terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept (based on human review), alternate codings (or, data type allowing, text) may be included instead.")) |
| ....... [value](valueset-definitions.html#ValueSet.compose.include.concept.designation.value "ValueSet.compose.include.concept.designation.value : The text value for this designation.") |  | 1..1 | [string](datatypes.html#string) | The text value for this designation |
| ..... [filter](valueset-definitions.html#ValueSet.compose.include.filter "ValueSet.compose.include.filter : Select concepts by specify a matching criterion based on the properties (including relationships) defined by the system, or on filters defined by the system. If multiple filters are specified, they SHALL all be true.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..\* | [BackboneElement](backboneelement.html) | Select codes/concepts by their properties (including relationships) |
| ...... [property](valueset-definitions.html#ValueSet.compose.include.filter.property "ValueSet.compose.include.filter.property : A code that identifies a property or a filter defined in the code system.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [code](datatypes.html#code) | A property/filter defined by the code system |
| ...... [op](valueset-definitions.html#ValueSet.compose.include.filter.op "ValueSet.compose.include.filter.op : The kind of operation to perform as a part of the filter criteria.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [code](datatypes.html#code) | = | is-a | descendent-of | is-not-a | regex | in | not-in | generalizes | exists [FilterOperator](valueset-filter-operator.html "The kind of operation to perform as a part of a property based filter.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ...... [value](valueset-definitions.html#ValueSet.compose.include.filter.value "ValueSet.compose.include.filter.value : The match value may be either a code defined by the system, or a string value, which is a regex match on the literal string of the property value  (if the filter represents a property defined in CodeSystem) or of the system filter value (if the filter represents a filter defined in CodeSystem) when the operation is 'regex', or one of the values (true and false), when the operation is 'exists'.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [string](datatypes.html#string) | Code from the system, or regex criteria, or boolean value for exists |
| ..... [valueSet](valueset-definitions.html#ValueSet.compose.include.valueSet "ValueSet.compose.include.valueSet : Selects the concepts found in this value set (based on its value set definition). This is an absolute URI that is a reference to ValueSet.url.  If multiple value sets are specified this includes the union of the contents of all of the referenced value sets.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..\* | [canonical](datatypes.html#canonical)([ValueSet](valueset.html)) | Select the contents included in this value set |
| .... [exclude](valueset-definitions.html#ValueSet.compose.exclude "ValueSet.compose.exclude : Exclude one or more codes from the value set based on code system filters and/or other value sets.") | [I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..\* | see [include](#ValueSet.compose.include "ValueSet.compose.include") | Explicitly exclude codes from a code system or other value sets |
| ... [expansion](valueset-definitions.html#ValueSet.expansion "ValueSet.expansion : A value set can also be \"expanded\", where the value set is turned into a simple collection of enumerated codes. This element holds the expansion, if it has been performed.") |  | 0..1 | [BackboneElement](backboneelement.html) | Used when the value set is "expanded" |
| .... [identifier](valueset-definitions.html#ValueSet.expansion.identifier "ValueSet.expansion.identifier : An identifier that uniquely identifies this expansion of the valueset, based on a unique combination of the provided parameters, the system default parameters, and the underlying system code system versions etc. Systems may re-use the same identifier as long as those factors remain the same, and the expansion is the same, but are not required to do so. This is a business identifier.") |  | 0..1 | [uri](datatypes.html#uri) | Identifies the value set expansion (business identifier) |
| .... [timestamp](valueset-definitions.html#ValueSet.expansion.timestamp "ValueSet.expansion.timestamp : The time at which the expansion was produced by the expanding system.") |  | 1..1 | [dateTime](datatypes.html#dateTime) | Time ValueSet expansion happened |
| .... [total](valueset-definitions.html#ValueSet.expansion.total "ValueSet.expansion.total : The total number of concepts in the expansion. If the number of concept nodes in this resource is less than the stated number, then the server can return more using the offset parameter.") |  | 0..1 | [integer](datatypes.html#integer) | Total number of codes in the expansion |
| .... [offset](valueset-definitions.html#ValueSet.expansion.offset "ValueSet.expansion.offset : If paging is being used, the offset at which this resource starts.  I.e. this resource is a partial view into the expansion. If paging is not being used, this element SHALL NOT be present.") |  | 0..1 | [integer](datatypes.html#integer) | Offset at which this resource starts |
| .... [parameter](valueset-definitions.html#ValueSet.expansion.parameter "ValueSet.expansion.parameter : A parameter that controlled the expansion process. These parameters may be used by users of expanded value sets to check whether the expansion is suitable for a particular purpose, or to pick the correct expansion.") |  | 0..\* | [BackboneElement](backboneelement.html) | Parameter that controlled the expansion process |
| ..... [name](valueset-definitions.html#ValueSet.expansion.parameter.name "ValueSet.expansion.parameter.name : Name of the input parameter to the $expand operation; may be a server-assigned name for additional default or other server-supplied parameters used to control the expansion process.") |  | 1..1 | [string](datatypes.html#string) | Name as assigned by the client or server |
| ..... [value[x]](valueset-definitions.html#ValueSet.expansion.parameter.value_x_ "ValueSet.expansion.parameter.value[x] : The value of the parameter.") |  | 0..1 |  | Value of the named parameter |
| ...... valueString |  |  | [string](datatypes.html#string) |  |
| ...... valueBoolean |  |  | [boolean](datatypes.html#boolean) |  |
| ...... valueInteger |  |  | [integer](datatypes.html#integer) |  |
| ...... valueDecimal |  |  | [decimal](datatypes.html#decimal) |  |
| ...... valueUri |  |  | [uri](datatypes.html#uri) |  |
| ...... valueCode |  |  | [code](datatypes.html#code) |  |
| ...... valueDateTime |  |  | [dateTime](datatypes.html#dateTime) |  |
| .... [contains](valueset-definitions.html#ValueSet.expansion.contains "ValueSet.expansion.contains : The codes that are contained in the value set expansion.") | [I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..\* | [BackboneElement](backboneelement.html) | Codes in the value set + Rule: SHALL have a code or a display + Rule: Must have a code if not abstract + Rule: Must have a system if a code is present |
| ..... [system](valueset-definitions.html#ValueSet.expansion.contains.system "ValueSet.expansion.contains.system : An absolute URI which is the code system in which the code for this item in the expansion is defined.") |  | 0..1 | [uri](datatypes.html#uri) | System value for the code |
| ..... [abstract](valueset-definitions.html#ValueSet.expansion.contains.abstract "ValueSet.expansion.contains.abstract : If true, this entry is included in the expansion for navigational purposes, and the user cannot select the code directly as a proper value.") |  | 0..1 | [boolean](datatypes.html#boolean) | If user cannot select this entry |
| ..... [inactive](valueset-definitions.html#ValueSet.expansion.contains.inactive "ValueSet.expansion.contains.inactive : If the concept is inactive in the code system that defines it. Inactive codes are those that are no longer to be used, but are maintained by the code system for understanding legacy data. It might not be known or specified whether an concept is inactive (and it may depend on the context of use).") |  | 0..1 | [boolean](datatypes.html#boolean) | If concept is inactive in the code system |
| ..... [version](valueset-definitions.html#ValueSet.expansion.contains.version "ValueSet.expansion.contains.version : The version of the code system from this code was taken. Note that a well-maintained code system does not need the version reported, because the meaning of codes is consistent across versions. However this cannot consistently be assured, and when the meaning is not guaranteed to be consistent, the version SHOULD be exchanged.") |  | 0..1 | [string](datatypes.html#string) | Version in which this code/display is defined |
| ..... [code](valueset-definitions.html#ValueSet.expansion.contains.code "ValueSet.expansion.contains.code : The code for this item in the expansion hierarchy. If this code is missing the entry in the hierarchy is a place holder (abstract) and does not represent a valid code in the value set.") | [I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..1 | [code](datatypes.html#code) | Code - if blank, this is not a selectable code |
| ..... [display](valueset-definitions.html#ValueSet.expansion.contains.display "ValueSet.expansion.contains.display : The recommended display for this item in the expansion.") | [I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..1 | [string](datatypes.html#string) | User display for the concept |
| ..... [designation](valueset-definitions.html#ValueSet.expansion.contains.designation "ValueSet.expansion.contains.designation : Additional representations for this item - other languages, aliases, specialized purposes, used for particular purposes, etc. These are relevant when the conditions of the expansion do not fix to a single correct representation.") |  | 0..\* | see [designation](#ValueSet.compose.include.concept.designation "ValueSet.compose.include.concept.designation") | Additional representations for this item |
| ..... [contains](valueset-definitions.html#ValueSet.expansion.contains.contains "ValueSet.expansion.contains.contains : Other codes and entries contained under this entry in the hierarchy.") |  | 0..\* | see [contains](#ValueSet.expansion.contains "ValueSet.expansion.contains") | Codes contained under this entry |
| [doco Documentation for this format](formats.html#table "Legend for this format") | | | | |

**UML Diagram** ([Legend](formats.html#uml))

**XML Template**

```

<ValueSet xmlns="http://hl7.org/fhir"> ![doco](help.png)
 <!-- from Resource: id, meta, implicitRules, and language -->
 <!-- from DomainResource: text, contained, extension, and modifierExtension -->
 <url value="[uri]"/><!-- 0..1 Canonical identifier for this value set, represented as a URI (globally unique) -->
 <identifier><!-- 0..* Identifier Additional identifier for the value set (business identifier) --></identifier>
 <version value="[string]"/><!-- 0..1 Business version of the value set -->
 <name value="[string]"/><!-- ![??](lock.png) 0..1 Name for this value set (computer friendly) -->
 <title value="[string]"/><!-- 0..1 Name for this value set (human friendly) -->
 <status value="[code]"/><!-- 1..1 draft | active | retired | unknown -->
 <experimental value="[boolean]"/><!-- 0..1 For testing purposes, not real usage -->
 <date value="[dateTime]"/><!-- 0..1 Date last changed -->
 <publisher value="[string]"/><!-- 0..1 Name of the publisher (organization or individual) -->
 <contact><!-- 0..* ContactDetail Contact details for the publisher --></contact>
 <description value="[markdown]"/><!-- 0..1 Natural language description of the value set -->
 <useContext><!-- 0..* UsageContext The context that the content is intended to support --></useContext>
 <jurisdiction><!-- 0..* CodeableConcept Intended jurisdiction for value set (if applicable) --></jurisdiction>
 <immutable value="[boolean]"/><!-- 0..1 Indicates whether or not any change to the content logical definition may occur -->
 <purpose value="[markdown]"/><!-- 0..1 Why this value set is defined -->
 <copyright value="[markdown]"/><!-- 0..1 Use and/or publishing restrictions -->
 <compose>  <!-- 0..1 Content logical definition of the value set (CLD) -->
  <lockedDate value="[date]"/><!-- 0..1 Fixed date for references with no specified version (transitive) -->
  <inactive value="[boolean]"/><!-- 0..1 Whether inactive codes are in the value set -->
  <include>  <!-- 1..* Include one or more codes from a code system or other value set(s) -->
   <system value="[uri]"/><!-- ![??](lock.png) 0..1 The system the codes come from -->
   <version value="[string]"/><!-- 0..1 Specific version of the code system referred to -->
   <concept>  <!-- ![??](lock.png) 0..* A concept defined in the system -->
    <code value="[code]"/><!-- 1..1 Code or expression from system -->
    <display value="[string]"/><!-- 0..1 Text to display for this code for this value set in this valueset -->
    <designation>  <!-- 0..* Additional representations for this concept -->
     <language value="[code]"/><!-- 0..1 Human language of the designation -->
     <use><!-- 0..1 Coding Types of uses of designations --></use>
     <value value="[string]"/><!-- 1..1 The text value for this designation -->
    </designation>
   </concept>
   <filter>  <!-- ![??](lock.png) 0..* Select codes/concepts by their properties (including relationships) -->
    <property value="[code]"/><!-- 1..1 A property/filter defined by the code system -->
    <op value="[code]"/><!-- 1..1 = | is-a | descendent-of | is-not-a | regex | in | not-in | generalizes | exists -->
    <value value="[string]"/><!-- 1..1 Code from the system, or regex criteria, or boolean value for exists -->
   </filter>
   <valueSet><!-- ![??](lock.png) 0..* canonical(ValueSet) Select the contents included in this value set --></valueSet>
  </include>
  <exclude><!-- ![??](lock.png) 0..* Content as for ValueSet.compose.include Explicitly exclude codes from a code system or other value sets --></exclude>
 </compose>
 <expansion>  <!-- 0..1 Used when the value set is "expanded" -->
  <identifier value="[uri]"/><!-- 0..1 Identifies the value set expansion (business identifier) -->
  <timestamp value="[dateTime]"/><!-- 1..1 Time ValueSet expansion happened -->
  <total value="[integer]"/><!-- 0..1 Total number of codes in the expansion -->
  <offset value="[integer]"/><!-- 0..1 Offset at which this resource starts -->
  <parameter>  <!-- 0..* Parameter that controlled the expansion process -->
   <name value="[string]"/><!-- 1..1 Name as assigned by the client or server -->
   <value[x]><!-- 0..1 string|boolean|integer|decimal|uri|code|dateTime Value of the named parameter --></value[x]>
  </parameter>
  <contains>  <!-- 0..* Codes in the value set -->
   <system value="[uri]"/><!-- 0..1 System value for the code -->
   <abstract value="[boolean]"/><!-- 0..1 If user cannot select this entry -->
   <inactive value="[boolean]"/><!-- 0..1 If concept is inactive in the code system -->
   <version value="[string]"/><!-- 0..1 Version in which this code/display is defined -->
   <code value="[code]"/><!-- ![??](lock.png) 0..1 Code - if blank, this is not a selectable code -->
   <display value="[string]"/><!-- ![??](lock.png) 0..1 User display for the concept -->
   <designation><!-- 0..* Content as for ValueSet.compose.include.concept.designation Additional representations for this item --></designation>
   <contains><!-- 0..* Content as for ValueSet.expansion.contains Codes contained under this entry --></contains>
  </contains>
 </expansion>
</ValueSet>
```

**JSON Template**

```

{![doco](help.png)
  "resourceType" : "ValueSet",
  // from Resource: id, meta, implicitRules, and language
  // from DomainResource: text, contained, extension, and modifierExtension
  "url" : "<uri>", // Canonical identifier for this value set, represented as a URI (globally unique)
  "identifier" : [{ Identifier }], // Additional identifier for the value set (business identifier)
  "version" : "<string>", // Business version of the value set
  "name" : "<string>", // C? Name for this value set (computer friendly)
  "title" : "<string>", // Name for this value set (human friendly)
  "status" : "<code>", // R!  draft | active | retired | unknown
  "experimental" : <boolean>, // For testing purposes, not real usage
  "date" : "<dateTime>", // Date last changed
  "publisher" : "<string>", // Name of the publisher (organization or individual)
  "contact" : [{ ContactDetail }], // Contact details for the publisher
  "description" : "<markdown>", // Natural language description of the value set
  "useContext" : [{ UsageContext }], // The context that the content is intended to support
  "jurisdiction" : [{ CodeableConcept }], // Intended jurisdiction for value set (if applicable)
  "immutable" : <boolean>, // Indicates whether or not any change to the content logical definition may occur
  "purpose" : "<markdown>", // Why this value set is defined
  "copyright" : "<markdown>", // Use and/or publishing restrictions
  "compose" : { // Content logical definition of the value set (CLD)
    "lockedDate" : "<date>", // Fixed date for references with no specified version (transitive)
    "inactive" : <boolean>, // Whether inactive codes are in the value set
    "include" : [{ // R!  Include one or more codes from a code system or other value set(s)
      "system" : "<uri>", // C? The system the codes come from
      "version" : "<string>", // Specific version of the code system referred to
      "concept" : [{ // C? A concept defined in the system
        "code" : "<code>", // R!  Code or expression from system
        "display" : "<string>", // Text to display for this code for this value set in this valueset
        "designation" : [{ // Additional representations for this concept
          "language" : "<code>", // Human language of the designation
          "use" : { Coding }, // Types of uses of designations
          "value" : "<string>" // R!  The text value for this designation
        }]
      }],
      "filter" : [{ // C? Select codes/concepts by their properties (including relationships)
        "property" : "<code>", // R!  A property/filter defined by the code system
        "op" : "<code>", // R!  = | is-a | descendent-of | is-not-a | regex | in | not-in | generalizes | exists
        "value" : "<string>" // R!  Code from the system, or regex criteria, or boolean value for exists
      }],
      "valueSet" : [{ canonical(ValueSet) }] // C? Select the contents included in this value set
    }],
    "exclude" : [{ Content as for ValueSet.compose.include }] // C? Explicitly exclude codes from a code system or other value sets
  },
  "expansion" : { // Used when the value set is "expanded"
    "identifier" : "<uri>", // Identifies the value set expansion (business identifier)
    "timestamp" : "<dateTime>", // R!  Time ValueSet expansion happened
    "total" : <integer>, // Total number of codes in the expansion
    "offset" : <integer>, // Offset at which this resource starts
    "parameter" : [{ // Parameter that controlled the expansion process
      "name" : "<string>", // R!  Name as assigned by the client or server
      // value[x]: Value of the named parameter. One of these 7:
      "valueString" : "<string>"
      "valueBoolean" : <boolean>
      "valueInteger" : <integer>
      "valueDecimal" : <decimal>
      "valueUri" : "<uri>"
      "valueCode" : "<code>"
      "valueDateTime" : "<dateTime>"
    }],
    "contains" : [{ // Codes in the value set
      "system" : "<uri>", // System value for the code
      "abstract" : <boolean>, // If user cannot select this entry
      "inactive" : <boolean>, // If concept is inactive in the code system
      "version" : "<string>", // Version in which this code/display is defined
      "code" : "<code>", // C? Code - if blank, this is not a selectable code
      "display" : "<string>", // C? User display for the concept
      "designation" : [{ Content as for ValueSet.compose.include.concept.designation }], // Additional representations for this item
      "contains" : [{ Content as for ValueSet.expansion.contains }] // Codes contained under this entry
    }]
  }
}
```

**Turtle Template**

```

@prefix fhir: <http://hl7.org/fhir/> .![doco](help.png)


[ a fhir:ValueSet;
  fhir:nodeRole fhir:treeRoot; # if this is the parser root

  # from Resource: .id, .meta, .implicitRules, and .language
  # from DomainResource: .text, .contained, .extension, and .modifierExtension
  fhir:ValueSet.url [ uri ]; # 0..1 Canonical identifier for this value set, represented as a URI (globally unique)
  fhir:ValueSet.identifier [ Identifier ], ... ; # 0..* Additional identifier for the value set (business identifier)
  fhir:ValueSet.version [ string ]; # 0..1 Business version of the value set
  fhir:ValueSet.name [ string ]; # 0..1 Name for this value set (computer friendly)
  fhir:ValueSet.title [ string ]; # 0..1 Name for this value set (human friendly)
  fhir:ValueSet.status [ code ]; # 1..1 draft | active | retired | unknown
  fhir:ValueSet.experimental [ boolean ]; # 0..1 For testing purposes, not real usage
  fhir:ValueSet.date [ dateTime ]; # 0..1 Date last changed
  fhir:ValueSet.publisher [ string ]; # 0..1 Name of the publisher (organization or individual)
  fhir:ValueSet.contact [ ContactDetail ], ... ; # 0..* Contact details for the publisher
  fhir:ValueSet.description [ markdown ]; # 0..1 Natural language description of the value set
  fhir:ValueSet.useContext [ UsageContext ], ... ; # 0..* The context that the content is intended to support
  fhir:ValueSet.jurisdiction [ CodeableConcept ], ... ; # 0..* Intended jurisdiction for value set (if applicable)
  fhir:ValueSet.immutable [ boolean ]; # 0..1 Indicates whether or not any change to the content logical definition may occur
  fhir:ValueSet.purpose [ markdown ]; # 0..1 Why this value set is defined
  fhir:ValueSet.copyright [ markdown ]; # 0..1 Use and/or publishing restrictions
  fhir:ValueSet.compose [ # 0..1 Content logical definition of the value set (CLD)
    fhir:ValueSet.compose.lockedDate [ date ]; # 0..1 Fixed date for references with no specified version (transitive)
    fhir:ValueSet.compose.inactive [ boolean ]; # 0..1 Whether inactive codes are in the value set
    fhir:ValueSet.compose.include [ # 1..* Include one or more codes from a code system or other value set(s)
      fhir:ValueSet.compose.include.system [ uri ]; # 0..1 The system the codes come from
      fhir:ValueSet.compose.include.version [ string ]; # 0..1 Specific version of the code system referred to
      fhir:ValueSet.compose.include.concept [ # 0..* A concept defined in the system
        fhir:ValueSet.compose.include.concept.code [ code ]; # 1..1 Code or expression from system
        fhir:ValueSet.compose.include.concept.display [ string ]; # 0..1 Text to display for this code for this value set in this valueset
        fhir:ValueSet.compose.include.concept.designation [ # 0..* Additional representations for this concept
          fhir:ValueSet.compose.include.concept.designation.language [ code ]; # 0..1 Human language of the designation
          fhir:ValueSet.compose.include.concept.designation.use [ Coding ]; # 0..1 Types of uses of designations
          fhir:ValueSet.compose.include.concept.designation.value [ string ]; # 1..1 The text value for this designation
        ], ...;
      ], ...;
      fhir:ValueSet.compose.include.filter [ # 0..* Select codes/concepts by their properties (including relationships)
        fhir:ValueSet.compose.include.filter.property [ code ]; # 1..1 A property/filter defined by the code system
        fhir:ValueSet.compose.include.filter.op [ code ]; # 1..1 = | is-a | descendent-of | is-not-a | regex | in | not-in | generalizes | exists
        fhir:ValueSet.compose.include.filter.value [ string ]; # 1..1 Code from the system, or regex criteria, or boolean value for exists
      ], ...;
      fhir:ValueSet.compose.include.valueSet [ canonical(ValueSet) ], ... ; # 0..* Select the contents included in this value set
    ], ...;
    fhir:ValueSet.compose.exclude [ See ValueSet.compose.include ], ... ; # 0..* Explicitly exclude codes from a code system or other value sets
  ];
  fhir:ValueSet.expansion [ # 0..1 Used when the value set is "expanded"
    fhir:ValueSet.expansion.identifier [ uri ]; # 0..1 Identifies the value set expansion (business identifier)
    fhir:ValueSet.expansion.timestamp [ dateTime ]; # 1..1 Time ValueSet expansion happened
    fhir:ValueSet.expansion.total [ integer ]; # 0..1 Total number of codes in the expansion
    fhir:ValueSet.expansion.offset [ integer ]; # 0..1 Offset at which this resource starts
    fhir:ValueSet.expansion.parameter [ # 0..* Parameter that controlled the expansion process
      fhir:ValueSet.expansion.parameter.name [ string ]; # 1..1 Name as assigned by the client or server
      # ValueSet.expansion.parameter.value[x] : 0..1 Value of the named parameter. One of these 7
        fhir:ValueSet.expansion.parameter.valueString [ string ]
        fhir:ValueSet.expansion.parameter.valueBoolean [ boolean ]
        fhir:ValueSet.expansion.parameter.valueInteger [ integer ]
        fhir:ValueSet.expansion.parameter.valueDecimal [ decimal ]
        fhir:ValueSet.expansion.parameter.valueUri [ uri ]
        fhir:ValueSet.expansion.parameter.valueCode [ code ]
        fhir:ValueSet.expansion.parameter.valueDateTime [ dateTime ]
    ], ...;
    fhir:ValueSet.expansion.contains [ # 0..* Codes in the value set
      fhir:ValueSet.expansion.contains.system [ uri ]; # 0..1 System value for the code
      fhir:ValueSet.expansion.contains.abstract [ boolean ]; # 0..1 If user cannot select this entry
      fhir:ValueSet.expansion.contains.inactive [ boolean ]; # 0..1 If concept is inactive in the code system
      fhir:ValueSet.expansion.contains.version [ string ]; # 0..1 Version in which this code/display is defined
      fhir:ValueSet.expansion.contains.code [ code ]; # 0..1 Code - if blank, this is not a selectable code
      fhir:ValueSet.expansion.contains.display [ string ]; # 0..1 User display for the concept
      fhir:ValueSet.expansion.contains.designation [ See ValueSet.compose.include.concept.designation ], ... ; # 0..* Additional representations for this item
      fhir:ValueSet.expansion.contains.contains [ See ValueSet.expansion.contains ], ... ; # 0..* Codes contained under this entry
    ], ...;
  ];
]
```

**Changes since Release 3**

|  |  |
| --- | --- |
| [ValueSet](valueset.html#ValueSet) |  |
| ValueSet.status | - Change value set from http://hl7.org/fhir/ValueSet/publication-status to http://hl7.org/fhir/ValueSet/publication-status|4.0.1 |
| ValueSet.experimental | - No longer marked as Modifier |
| ValueSet.compose.include.concept.designation.language | - Change binding strength from extensible to preferred |
| ValueSet.compose.include.filter | - No longer marked as Modifier |
| ValueSet.compose.include.filter.op | - Change value set from http://hl7.org/fhir/ValueSet/filter-operator to http://hl7.org/fhir/ValueSet/filter-operator|4.0.1 |
| ValueSet.compose.include.filter.value | - Type changed from code to string |
| ValueSet.compose.include.valueSet | - Type changed from uri to canonical(ValueSet) |
| ValueSet.expansion.identifier | - Min Cardinality changed from 1 to 0 |
| ValueSet.expansion.parameter.value[x] | - Add Type dateTime |
| ValueSet.expansion.contains.abstract | - Default Value "false" removed |
| ValueSet.expansion.contains.inactive | - Default Value "false" removed |
| ValueSet.extensible | - deleted |

See the [Full Difference](diff.html) for further information

This analysis is available as [XML](valueset.diff.xml) or [JSON](valueset.diff.json).

See [R3 <--> R4 Conversion Maps](valueset-version-maps.html) (status = 8 tests that all execute ok. All tests pass round-trip testing and 8 r3 resources are invalid (0 errors).)

See the [Profiles & Extensions](valueset-profiles.html) and the alternate definitions:
Master Definition [XML](valueset.profile.xml.html) + [JSON](valueset.profile.json.html),
[XML](xml.html) [Schema](valueset.xsd)/[Schematron](valueset.sch) + [JSON](json.html)
[Schema](valueset.schema.json.html), [ShEx](valueset.shex.html) (for [Turtle](rdf.html)) + [see the extensions](valueset-profiles.html) & the [dependency analysis](valueset-dependencies.html)

### 4.9.4.1 Terminology Bindings

| Path | Definition | Type | Reference |
| --- | --- | --- | --- |
| ValueSet.status | The lifecycle status of an artifact. | [Required](terminologies.html#required) | [PublicationStatus](valueset-publication-status.html) |
| ValueSet.jurisdiction | Countries and regions within which this artifact is targeted for use. | [Extensible](terminologies.html#extensible) | [Jurisdiction ValueSet](valueset-jurisdiction.html) |
| ValueSet.compose.include.concept.designation.language | A human language. | [Preferred](terminologies.html#preferred), but limited to [AllLanguages](valueset-all-languages.html) | [CommonLanguages](valueset-languages.html) |
| ValueSet.compose.include.concept.designation.use | Details of how a designation would be used. | [Extensible](terminologies.html#extensible) | [DesignationUse](valueset-designation-use.html) |
| ValueSet.compose.include.filter.op | The kind of operation to perform as a part of a property based filter. | [Required](terminologies.html#required) | [FilterOperator](valueset-filter-operator.html) |

### 4.9.4.2 Constraints

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **id** | **Level** | **Location** | **Description** | **[Expression](fhirpath.html)** |
| **vsd-0** | [Warning](conformance-rules.html#warning) | (base) | Name should be usable as an identifier for the module by machine processing applications such as code generation | name.matches('[A-Z]([A-Za-z0-9\_]){0,254}') |
| **vsd-1** | [Rule](conformance-rules.html#rule) | ValueSet.compose.include | A value set include/exclude SHALL have a value set or a system | valueSet.exists() or system.exists() |
| **vsd-2** | [Rule](conformance-rules.html#rule) | ValueSet.compose.include | A value set with concepts or filters SHALL include a system | (concept.exists() or filter.exists()) implies system.exists() |
| **vsd-3** | [Rule](conformance-rules.html#rule) | ValueSet.compose.include | Cannot have both concept and filter | concept.empty() or filter.empty() |
| **vsd-6** | [Rule](conformance-rules.html#rule) | ValueSet.expansion.contains | SHALL have a code or a display | code.exists() or display.exists() |
| **vsd-9** | [Rule](conformance-rules.html#rule) | ValueSet.expansion.contains | Must have a code if not abstract | code.exists() or abstract = true |
| **vsd-10** | [Rule](conformance-rules.html#rule) | ValueSet.expansion.contains | Must have a system if a code is present | code.empty() or system.exists() |

## 4.9.5 Composition Rules

A value set can be a simple list of included codes, or it can be some kind of general selection criteria
using the facilities provided by the [code system](codesystem.html). For these value sets:

- Multiple `include` statements are cumulative - e.g. the value set contains the union of all the includes
- Within an `include`, all the criterion apply -e.g. the value set contains the intersection of the criterion
- Within an `include`, a single system with selection criteria may be listed, and/or one or more value sets may be listed
- **`valueSet`(s) only**: Codes are 'selected' for inclusion if they are in all the referenced value sets
- If a **`System` only** is specified, the following rules apply:
  - **no `concept` or `filter`**: All codes in the system are included
  - **`concept`**: Only the enumerated codes are selected
  - **`filter`**: Any codes meeting the filter criteria are selected
- **`valueSet` and `System`**: Codes are 'selected' for inclusion if they are selected by the code system selection
  (after checking for `concept` and `filter`) and if they are in all the referenced value sets
- If the system reference is not version specific and filters are present, then the contents of the value set are open and change
  over time as the underlying code systems are updated
- The version reference may be the special value '`*`', which indicates that the value set includes codes from all versions of the code system.
  how to handle provision of the required versions and generation of expansions is at server discretion, including for poorly behaved code systems where
  a code changes in meaning).
  > **Implementation Note:**
  > Use of this capability is subject to future clarification and conformance requirements based on implementation experience.
- Using the property filters is only possible where the code system in use defines
  the relevant properties. Note that in some cases the underlying code system defines the
  logical concepts but not the syntax for exercising them. In such cases, the literal
  definitions may be provided by a third party
- In addition to include rules, codes may be excluded. Rules for interpretation of exclude statements match those for includes, but codes in the exclude statements are never in the value set
- Value sets may include abstract codes - that is, codes designated by the underlying code system as
  not for use as a selectable concept in a particular context. These abstract codes are typically used as a grouping/searching mechanism,
  and can be included either by enumerating them, or by using a filter.
- Any compose.exclude SHALL be processed such that excluded codes are not found in the expansion

## 4.9.6 Display and Designations

Concepts used in ValueSets can have a `display`, which is a short text that represents the meaning
of the concept to human users in the context of the value set (which often has narrower meaning and therefore
is amenable to shorter displays. If a display is not provided, the value set uses the
[display from the code system](codesystem.html#designations) (which is the preferred approach,
because overriding the display can lead to very unsafe outcomes).

When a value set enumerates codes, it is sometimes useful to define an alternative display for
the code that is to be used wherever the value set is expanded and used in a UI. This
facility is provided to cover the following circumstances:

- The system that defines the code or expression doesn't provide a display for this code (or any codes).
- The system that defines the code or expression defines multiple choices for display.
- The system provides a very long display name that is unnecessary or inappropriate in the context of this value set (e.g. a display name of "Glucose [Mass/volume] in Serum or Plasma --10 PM specimen" for LOINC code 48991-4, when the value set only includes Glucose mass/vol in serum/plasma codes). As the display names get longer, this becomes more important.

Note that care must be taken in order to avoid "changing the meaning" of the concept by
implying that it means something other than the explicit definition of the concept in the
underlying code system (e.g., in the case above, using a display of "Glucose Concentration at 10pm").
For this reason, some contexts of use do not allow a display to be associated with a specific code
in a value set.

Any display name for a concept provided in the value set is for display to a human user.
The display in the [Coding](datatypes.html#Coding) that results from a user
selecting a concept from the expansion must be taken from the underlying code system
definition, even if a value set is referenced explicitly in the Coding (e.g. by an
[extension](extension-valueset-reference.html)). The correct display for a
code can be determined by a [$lookup operation](codesystem-operation-lookup.html).
Any alternative display specified in the value set would go in
[CodeableConcept](datatypes.html#CodeableConcept).text, perhaps appended to
the UI label for the matching data element.

As an example, the [LOINC code](loinc.html) [`55423-8` ![](external.png)](https://s.details.loinc.org/LOINC/55423-8.html?sections=Comprehensive)
has a display value of "Number of steps in unspecified time Pedometer". A value set for a pick list
in a patient generated data form might choose a simpler name:

```

{
  "resourceType" : "ValueSet",
  "compose" : {
    "include" : [{
      "system" : "http://loinc.org",
      "concept" : [{
        "code" : "55423-8",
        "display" : "Step Count"
      }]
    }]
  }
}
```

The expansion generated by a terminology server will have this:

```

{
  "resourceType" : "ValueSet",
  "expansion" : {
    "contains" : [{
      "system" : "http://loinc.org",
      "code" : "55423-8",
      "display" : "Step Count"
    }]
  }
}
```

The expansion display is taken from the value set, and this is what is displayed in the pick list.
Once the user picks the code, it will appear in the [Observation.code](observation-definitions.html#Observation.code) like this:

```

{
  "resourceType" : "Observation",
  "code" : {
    "coding" : [{
      "system" : "http://loinc.org",
      "code" : "55423-8",
      "display" : "Number of steps in unspecified time Pedometer"
    }],
    "text" : "Step Count"
  }
}
```

Note that the correct value for the display is not in the expansion above.
The client can either omit the display, look it up using [$lookup](codesystem-operation-lookup.html), or the
server might pre-populate it in the expansion:

```

{
  "resourceType" : "ValueSet",
  "expansion" : {
    "contains" : [{
      "system" : "http://loinc.org",
      "code" : "55423-8",
      "display" : "Step Count",
      "designation" : [{
        "use" : {
          "system" : "http://snomed.info/sct",
          "code" : "900000000000003001"
        },
        "value" : "Number of steps in unspecified time Pedometer"
      }]
    }]
  }
}
```

Irrespective of this, the display in the expansion always goes in [CodeableConcept.text](datatypes-definitions.html#CodeableConcept.text).

In addition to the display, a concept can have one or more `designation` elements.
The display is equivalent to a special designation with an implied `designation.use` of "primary code"
and a language equal to the [Resource Language](resource.html#language). The designations can provide
additional displays for other languages, as well as designations for other purposes.
When using concepts, applications use the `display` unless the language or usage in context provides a reason
to use one of the designations.

## 4.9.7 Value Sets with multiple code systems

Value sets may select codes from multiple code systems - either
by including codes from different systems, or importing other
value sets that include them. A typical use for crossing code systems is
when including a set of codes, and adding a few additional codes to cover
cases not catered to by the included codes (e.g. Data missing or workflow error codes).

Best Practice Note: Mixing definitional systems offers the potential for
confusing, overlapping, and inconsistent definitions. Creating value sets that cross
code systems should be done with care to avoid creating definitional confusion.

Value sets should only include well differentiated concepts, but many value sets and code systems
do not have well differentiated concepts because of various real world constraints.

### 4.9.7.1 Code systems Note

Each [Code System](codesystem.html) defines which filters can be
used in `ValueSet.compose.include.filter`. All code systems have
[base filters](codesystem.html#filter) and any additional
filters defined in ([CodeSystem.filter)](codesystem-definitions.html#CodeSystem.filter).

This specification also defines filters for various published code systems:

- [LOINC Filters](loinc.html#filters)
- [Using CT Filters](snomedct.html#filters)
- [RxNorm Filters](rxnorm.html#filters)
- [UCUM Filters](ucum.html#filters)
- [Using Metathesaurus Filters](ncimeta.html#filters)
- [CPT Filters](cpt.html#filters)
- [NDF-RT Filters](ndfrt.html#filters)

## 4.9.8 Value Set Expansion

A value set can be "expanded", where the definition of the value set is
used to create a simple collection of codes suitable for use for data
entry or validation. There is a [defined operation $expand](valueset-operation-expand.html) to ask a server to perform this expansion.
Expansions are most useful when a value set includes
all the codes in a code system, or a set of codes by filter.

A resource that represents a value set expansion includes the same
identification details as the definition of the value set, and MAY
include the definition of the value set (`.compose`). In
addition, it has an `.expansion` element which contains
the list of codes that constitute the value set expansion. Each
contained code can include nested contained codes - see [below
for further discussion](#hierarchy).

When a request for an expansion is received (e.g., for the [$expand](valueset-operations.html#expand) operation),
the following process should be followed:

- If the value set already has an expansion (e.g., a stored expansion):
  - Check that the parameters associated with the [$expand](valueset-operation-expand.html) operation are consistent with the parameters recorded in the expansion
  - If the parameters are inconsistent, then either generate a new expansion, or, if there is no definition (`.compose`), return an error
  - Additional parameters may be applied to an existing expansion if the server has validated that the result will be the same as if the expansion
    was generated directly from the value set definition (e.g. text filter, designations included).
- Otherwise: For each *compose.include*:
  1. If there is a system, identify the correct version of the [code system](codesystem.html), and then:
     - If there are no codes or filters, add every code in the code system to the result set.
     - If codes are listed, check that they are valid, and check their active status, and if ok, add them to the result set (the parameters to the [$expand](valueset-operation-expand.html) operation may be used to control whether active codes are included).
     - If any filters are present, process them in order (as explained above), and add the intersection of their results to the result set.
  2. For each `valueSet`, find the referenced value set by ValueSet.url, expand that (e.g., using the [$expand](valueset-operations.html#expand) operation: GET [base]/ValueSet/$expand$url=[compose.include.valueSet]), and add it to the result set. This means that expansion across imports is a recursive process.
  3. Add the intersection of the result set from the system and the result sets from the value sets to the expansion
- For each *compose.exclude*, follow the same process as for *compose.include*, but remove any codes from the result set, instead of adding them.

The final "result set" is then represented in *expansion*.
Note that the expansion structure is inherently ordered; this specification does not fix the
meaning of use of the order. The conceptual approach described should not be understood to prohibit any implementation approach in
these regards. In addition, note that the method described above is a conceptual approach; individual servers may choose to follow
alternative approaches that are more efficient, as long as the outcome is the same.

![](assets/images/dragon.png "Here Be Dragons!")

The impact of [Code System supplements](codesystem.html#supplements) on [value set expansion](valueset-operation-expand.html) - and
therefore [value set validation](valueset-operation-validate-code.html) - is
subject to ongoing experimentation and implementation testing, and further clarification and additional
rules might be proposed in future versions of this specification.

### 4.9.8.1 Hierarchical Expansions

The expansion MAY be hierarchical - that is, it may have contains element that contain their own sub-elements, to any
level of depth. This specification does not fix the meaning of the hierarchy: there is
no implication about the logical relationship between the nested `contain` elements, and the
structure cannot be used for logical inferencing. The structure
exists to provide navigational assistance for helping human users to
locate codes in the expansion. There is an [example of use of a hierarchical expansion](valueset-example-hierarchical.html).

Note that the
`CodeSystem` resource and `ValueSet.compose` offer no direct support for defining hierarchies and groups;
applications may want to take advantage of the [expand-rules](extension-valueset-expand-rules.html) and
[expand-group](extension-valueset-expand-group.html) extensions as an implementation feature.
An expansion may include entries in the expansion that only serve an arbitrary grouping purpose, to make it easier
for a human to use the list. These entries have no system or code, and must be marked as abstract.

### 4.9.8.2 Uniqueness of Concepts in Expansions

Value set definitions may lead to more than one instruction to include a given concept in the value set across the includes and imports.
No matter how many times the definitions include a concept, it is only present in the value set once, and will only appear once
in a flat expansion of the value set. Note, however, that a concept may appear more than once in a nested hierarchy when the
expansion is prepared for UI use (irrespective of how many times it is included in the definitions). Note that uniqueness is
based on system/version/code; it is possible to include the same concept from different versions of a code system in the
same expansion, though this is generally confusing for users and should be avoided.

The codes in the expansion should be treated as case sensitive - implementers should use the correct
case. Implementers can consult the definition of the underlying code systems to determine whether the code system
that defines the code is case sensitive or not.

### 4.9.8.3 Expansion Identifiers

It is important that expansions be identified properly. Any value set definition may produce an infinite
number of expansions, depending on the operation parameters. Any expansions
produced must be clearly identified so that there is no confusion. The following rules apply:

- The canonical URL for the expansion is the same as the value set it was expanded from
- Each expansion SHALL have a unique identifier in `ValueSet.expansion.identifier`
- The result of an [$expand](valueset-operation-expand.html) operation may use the same identifier in ValueSet.expansion.identifier as a
  previous expansion, but if it does, the canonical representation of the value set expansion SHALL be identical (e.g. a cached response)

### 4.9.8.4 Expansion Parameters

The expansion contains a set of parameters in `ValueSet.expansion.parameter` that record what controlled the expansion process.
These parameters may be used by users of expanded value sets to check whether the expansion
is suitable for a particular purpose, or to pick the correct expansion. The server decides which
parameters to include here, but at a minimum, the list SHOULD include all of the parameters that
affect the [$expand](valueset-operation-expand.html) operation. If the expansion will be persisted all of these parameters SHALL
be included. If the codeSystem on the server has a specified
version then this version SHALL be provided as a parameter in the expansion (note that not all
code systems have a version).

The following parameters are predefined by the [$expand](valueset-operation-expand.html) operation, and are suitable for use in the
expansion parameters:

|  |  |
| --- | --- |
| `filter` | A text filter that is applied to restrict the codes that are returned (this is useful in a UI context). The interpretation of this is delegated to the server in order to allow to determine the most optimal search approach for the context. The server can document the way this parameter works in [TerminologyCapabilities](terminologycapabilities.html)..expansion.textFilter. Typical usage of this parameter includes functionality like:   - using left matching e.g. "acut ast" - allowing for wild cards such as %, &, ? - searching on definition as well as display(s) - allowing for search conditions (and / or / exclusions)   Text Search engines such as Lucene or Solr, long with their considerable functionality, might also be used. The optional text search might also be code system specific, and servers might have different implementations for different code systems |
| `date` | The date for which the expansion should be generated. if a date is provided, it means that the server should use the value set / code system definitions as they were on the given date, or return an error if this is not possible. Normally, the date is the current conditions (which is the default value) but under some circumstances, systems need to generate an expansion as it would have been in the past. A typical example of this would be where code selection is constrained to the set of codes that were available when the patient was treated, not when the record is being edited. Note that which date is appropriate is a matter for implementation policy. |
| `offset` | Paging support - where to start if a subset is desired (default = 0). Offset is number of records (not number of pages) |
| `count` | Paging support - how many codes should be provided in a partial page view. Paging only applies to flat expansions - servers ignore paging if the expansion is not flat. If count = 0, the client is asking how large the expansion is. Servers SHOULD honor this request for hierarchical expansions as well, and simply return the overall count |
| `includeDesignations` | Controls whether concept designations are to be included or excluded in value set expansions |
| `designation` | A [token](search.html#token) that specifies a system+code that is either a use or a language. Designations that match by language or use are included in the expansion. If no designation is specified, it is at the server discretion which designations to return |
| `includeDefinition` | Controls whether the value set definition is included or excluded in value set expansions |
| `activeOnly` | Controls whether inactive concepts are included or excluded in value set expansions. Note that if the value set explicitly specifies that inactive codes are included, this parameter can still remove them from a specific expansion, but this parameter cannot include them if the value set excludes them |
| `excludeNested` | Controls whether or not the value set expansion nests codes or not (i.e. ValueSet.expansion.contains.contains) |
| `excludeNotForUI` | Controls whether or not the value set expansion is assembled for a user interface use or not. Value sets intended for User Interface might include ['abstract' codes](codesystem.html#status) or have nested contains with items with no code or abstract = true, with the sole purpose of helping a user navigate through the list efficiently, where as a value set not generated for UI use might be flat, and only contain the selectable codes in the value set. The exact implications of 'for UI' depend on the code system, and what properties it exposes for a terminology server to use. In the FHIR Specification itself, the value set expansions are generated with excludeNotForUI = false, and the expansions used when generated schema / code etc, or performing validation, are all excludeNotForUI = true. |
| `excludePostCoordinated` | Controls whether or not the value set expansion includes post coordinated codes |
| `displayLanguage` | Specifies the language to be used for description in the expansions i.e. the language to be used for ValueSet.expansion.contains.display |
| `exclude-system` | Code system, or a particular version of a code system to be excluded from the value set expansion. The format is the same as a canonical URL: [system]|[version] - e.g. http://loinc.org|2.56 |
| `system-version` | Specifies a version to use for a system, if the value set does not specify which one to use. The format is the same as a canonical URL: [system]|[version] - e.g. http://loinc.org|2.56 |
| `check-system-version` | Edge Case: Specifies a version to use for a system. If a value set specifies a different version, an error is returned instead of the expansion. The format is the same as a canonical URL: [system]|[version] - e.g. http://loinc.org|2.56 |
| `force-system-version` | Edge Case: Specifies a version to use for a system. This parameter overrides any specified version in the value set (and any it depends on). The format is the same as a canonical URL: [system]|[version] - e.g. http://loinc.org|2.56. Note that this has obvious safety issues, in that it may result in a value set expansion giving a different list of codes that is both wrong and unsafe, and implementers should only use this capability reluctantly. It primarily exists to deal with situations where specifications have fallen into decay as time passes. If the value is override, the version used SHALL explicitly be represented in the expansion parameters |

The count and offset parameters are important. If the expansion is a page out of
the whole expansion, the offset and count parameters SHALL be populated. Clients
can reliably use the count/offset parameters to determine whether the whole
expansion is returned.

Other parameters that servers may be required to use:

|  |  |
| --- | --- |
| `[canonical]#CodeSystem.content` | [content] : The content value for the [code system](codesystem.html) for the canonical URL. Applications generating expansions SHALL use this parameter if the CodeSystem.content value is "fragment" or " |
| `[canonical1]#supplement` | [canonical2] : Indicates that the specified supplement (canonical2) contributed to the content of the expansion for the code system canonical1 (by influencing selection, or providing designations). Applications generating expansions SHALL use this parameter to record that a supplement was used during the expansion process |

Beyond this, servers MAY define their own parameters, though Terminology server
authors are requested to bring additional parameters to HL7 (via 'Propose a change'
link below) in the interests of interoperability.

Servers can also create and store [Provenance](provenance.html) statements about the expansion, or [AuditEvent](auditevent.html) records
of the expansion process if further transparency is required. These resources can contain considerable
detail about the various inputs to the process, and any significant decisions by the expansion
engine. Further details around this (and profiles on the relevant resources) may be provided
in future versions of this specification or related implementation guides.

> **Request for Feedback:**
> The existing set of parameters are intended to cover the vast majority of
> use cases, but there are some cases where the parameters do not provide
> enough control to a client, particularly with regard to combinations of
> parameters, and the interplay between code system versions and other parameters.
> Implementers may need to define their own value sets to meet these requirements.
>
> Ongoing feedback is welcome at [link to be provided]

### 4.9.8.5 Storing Expansions

Whether to store expanded value sets, or simply to store their definitions and expand on the fly is
a matter for system deployment. Some servers, including public value sets servers, only store expansions.
However, any system that stores an expansion must be concerned with how to determine whether the expansion
is still current, and this requires deep knowledge of how the expansion was created.
A system with a dedicated terminology server that returns expansions on demand avoids this problem, but
leaves open the question of how to audit the specific expansion that was used for a particular case.
One solution to this is to use a dedicated terminology server, and have the clients ask for
expansions on demand based on the value set definitions, and for the server to store (and reuse as
appropriate) the returned expansion (when it reuses the expansion, ValueSet.expansion.identifier will
be the same). If expansions are shared, users need to be aware of how expansion identifiers (which may be
server specific) work.

### 4.9.8.6 Searching for codes in value sets

The search parameters defined on ValueSet include the `code` parameter. This is intended
to allow a consumer to find all the value sets that include a particular code. However, fully
evaluating this search parameter is extremely onerous for a server. Further, whether a code is
in a value set depends on the context in which expansions are performed (see the [$expand](valueset-operation-expand.html) operation).
For this reason, the degree to which the search parameter is supported can be declared in the [Terminology Capability](terminologycapabilities-definitions.html#TerminologyCapabilities.codeSearch)
statement.

## 4.9.9 Combinations of .compose and .expansion

Use cases for the different combinations:

- `.compose` only:
  Provides the value set definition (CLD). This is the expected format from the value set publisher.
- `.expansion` only:
  Provides the value set expansion, which might or might not be persisted (see [4.8.7 Value Set Expansion](valueset.html#expansion) above).
  The "expansion only" format may be returned in the [$expand](valueset-operation-expand.html) operation output (at the terminology server's discretion).
- Both `.compose` and `.expansion`:
  The terminology server often may include the definition as well as the expansion in the [$expand](valueset-operation-expand.html) operation output.
  The resource instance including the expansion might or might not be persisted.
- Neither `.compose` nor `.expansion`:
  This is a valid format for ValueSet resource instances. A primary use case is the return from a summary search (i.e. \_summary=true).
  This may be especially useful to reduce the performance overhead when returning a summary of extensionally defined value sets
  (which may include a large number of concepts in the value set definition).

## 4.9.10 Search Parameters

Search parameters for this resource. The [common parameters](search.html#all) also apply. See [Searching](search.html) for more information about searching in REST, messaging, and services.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Name** | **Type** | **Description** | **Expression** | **In Common** |
| code [TU](versions.html#std-process "Trial Use Content") | [token](search.html#token) | This special parameter searches for codes in the value set. See additional notes on the ValueSet resource | ValueSet.expansion.contains.code | ValueSet.compose.include.concept.code |  |
| context [TU](versions.html#std-process "Trial Use Content") | [token](search.html#token) | A use context assigned to the value set | (ValueSet.useContext.value as CodeableConcept) |  |
| context-quantity [TU](versions.html#std-process "Trial Use Content") | [quantity](search.html#quantity) | A quantity- or range-valued use context assigned to the value set | (ValueSet.useContext.value as Quantity) | (ValueSet.useContext.value as Range) |  |
| context-type [TU](versions.html#std-process "Trial Use Content") | [token](search.html#token) | A type of use context assigned to the value set | ValueSet.useContext.code |  |
| context-type-quantity [TU](versions.html#std-process "Trial Use Content") | [composite](search.html#composite) | A use context type and quantity- or range-based value assigned to the value set | On ValueSet.useContext:   context-type: code   context-quantity: value.as(Quantity) | value.as(Range) |  |
| context-type-value [TU](versions.html#std-process "Trial Use Content") | [composite](search.html#composite) | A use context type and value assigned to the value set | On ValueSet.useContext:   context-type: code   context: value.as(CodeableConcept) |  |
| date [TU](versions.html#std-process "Trial Use Content") | [date](search.html#date) | The value set publication date | ValueSet.date |  |
| description [TU](versions.html#std-process "Trial Use Content") | [string](search.html#string) | The description of the value set | ValueSet.description |  |
| expansion [TU](versions.html#std-process "Trial Use Content") | [uri](search.html#uri) | Identifies the value set expansion (business identifier) | ValueSet.expansion.identifier |  |
| identifier [TU](versions.html#std-process "Trial Use Content") | [token](search.html#token) | External identifier for the value set | ValueSet.identifier |  |
| jurisdiction [TU](versions.html#std-process "Trial Use Content") | [token](search.html#token) | Intended jurisdiction for the value set | ValueSet.jurisdiction |  |
| name [TU](versions.html#std-process "Trial Use Content") | [string](search.html#string) | Computationally friendly name of the value set | ValueSet.name |  |
| publisher [TU](versions.html#std-process "Trial Use Content") | [string](search.html#string) | Name of the publisher of the value set | ValueSet.publisher |  |
| reference [TU](versions.html#std-process "Trial Use Content") | [uri](search.html#uri) | A code system included or excluded in the value set or an imported value set | ValueSet.compose.include.system |  |
| status [TU](versions.html#std-process "Trial Use Content") | [token](search.html#token) | The current status of the value set | ValueSet.status |  |
| title [TU](versions.html#std-process "Trial Use Content") | [string](search.html#string) | The human-friendly name of the value set | ValueSet.title |  |
| url [TU](versions.html#std-process "Trial Use Content") | [uri](search.html#uri) | The uri that identifies the value set | ValueSet.url |  |
| version [TU](versions.html#std-process "Trial Use Content") | [token](search.html#token) | The business version of the value set | ValueSet.version |  |

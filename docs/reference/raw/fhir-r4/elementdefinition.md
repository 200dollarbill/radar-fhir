---
id: elementdefinition
title: ElementDefinition
source_url: https://hl7.org/fhir/R4/elementdefinition.html
group: fhir-r4
fhir_version: R4
fetched_at: '2026-09-11T13:23:22Z'
sha256: b41f6522283fed744057b0b792325f11cc131e746e142911c78d73d75edfa085
---
This page is part of the FHIR Specification (v4.0.1: R4 - Mixed [Normative](https://confluence.hl7.org/display/HL7/HL7+Balloting "Normative Standard") and [STU](https://confluence.hl7.org/display/HL7/HL7+Balloting "Standard for Trial-Use")) in it's permanent home (it will always be available at this URL). The current version which supercedes this version is [5.0.0](http://hl7.org/fhir/index.html). For a full list of available versions, see the [Directory of published versions ![](external.png)](http://hl7.org/fhir/directory.html). Page versions: [R5](http://hl7.org/fhir/R5/elementdefinition.html) [R4B](http://hl7.org/fhir/R4B/elementdefinition.html) **R4** [R3](http://hl7.org/fhir/STU3/elementdefinition.html) [R2](http://hl7.org/fhir/DSTU2/elementdefinition.html)

- [Element Definition](#)
- [Examples](elementdefinition-examples.html)
- [Detailed Descriptions](elementdefinition-definitions.html)
- [Mappings](elementdefinition-mappings.html)
- [Extensions](elementdefinition-extras.html)

# 2.30.0 Element Definition

|  |  |  |
| --- | --- | --- |
| [FHIR Infrastructure](http://www.hl7.org/Special/committees/fiwg/index.cfm)  Work Group | [Maturity Level](versions.html#maturity): Normative | [Standards Status](versions.html#std-process): [Normative](versions.html#std-process) |

|  |  |
| --- | --- |
|  | This page has been approved as part of an [ANSI](https://www.ansi.org/)  standard. See the [Infrastructure](ansi-infrastructure.html) Package for further details. |

The definition of an element in a resource or an extension. The definition includes:

- Path (name), Cardinality, and data type
- Definitions, usage notes, and requirements
- Default or fixed values
- Constraints, Length limits, and other usage rules
- Terminology Binding
- Mappings to other specifications
- Structural Usage Information such as [Slicing](profiling.html#slicing)

The ElementDefinition type is the core of the FHIR metadata layer, and is closely (conceptually) aligned to [ISO 11179](elementdefinition-mappings.html#iso11179). All the data elements defined in this specification are published
as a collection of data elements ([XML](dataelements.xml) or [JSON](dataelements.json)).

ElementDefinition is used in [StructureDefinition](structuredefinition.html#structuredefinition)

## 2.30.0.1 Content

- [Structure](#tabs-ElementDefinition-struc)
- [UML](#tabs-ElementDefinition-uml)
- [XML](#tabs-ElementDefinition-xml)
- [JSON](#tabs-ElementDefinition-json)
- [Turtle](#tabs-ElementDefinition-ttl)
- [R3 Diff](#tabs-ElementDefinition-diff)
- [All](#tabs-ElementDefinition-all)

**Structure**

| [Name](formats.html#table "The logical name of the element") | [Flags](formats.html#table "Information about the use of the element") | [Card.](formats.html#table "Minimum and Maximum # of times the the element can appear in the instance") | [Type](formats.html#table "Reference to the type of the element") | [Description & Constraints](formats.html#table "Additional information about the element")[doco](formats.html#table "Legend for this format") |
| --- | --- | --- | --- | --- |
| .. [ElementDefinition](elementdefinition-definitions.html#ElementDefinition "ElementDefinition : Captures constraints on each element within the resource, profile, or extension.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants")[N](versions.html#std-process "Standards Status = Normative") |  | [BackBoneElement](backboneelement.html) | Definition of an element in a resource or extension + Rule: Min <= Max + Rule: if the element definition has a contentReference, it cannot have type, defaultValue, fixed, pattern, example, minValue, maxValue, maxLength, or binding + Rule: Fixed value may only be specified if there is one type + Rule: Pattern may only be specified if there is one type + Rule: Pattern and fixed are mutually exclusive + Rule: Binding can only be present for coded elements, string, and uri + Rule: Types must be unique by code + Rule: Constraints must be unique by key + Rule: default value and meaningWhenMissing are mutually exclusive + Rule: sliceName must be composed of proper tokens separated by "/" + Rule: Must have a modifier reason if isModifier = true + Rule: Element names cannot include some special characters + Warning: Element names should be simple alphanumerics with a max of 64 characters, or code generation tools may be broken + Rule: sliceIsConstraining can only appear if slicename is present Elements defined in Ancestors: [id](element.html#Element "Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces."), [extension](element.html#Element "May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension."), [modifierExtension](backboneelement.html#BackboneElement "May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.  Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).") |
| ... [path](elementdefinition-definitions.html#ElementDefinition.path "ElementDefinition.path : The path identifies the element and is expressed as a \".\"-separated list of ancestor elements, beginning with the name of the resource or extension.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [string](datatypes.html#string) | Path of the element in the hierarchy of elements |
| ... [representation](elementdefinition-definitions.html#ElementDefinition.representation "ElementDefinition.representation : Codes that define how this element is represented in instances, when the deviation varies from the normal case.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [code](datatypes.html#code) | xmlAttr | xmlText | typeAttr | cdaText | xhtml [PropertyRepresentation](valueset-property-representation.html "How a property is represented when serialized.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ... [sliceName](elementdefinition-definitions.html#ElementDefinition.sliceName "ElementDefinition.sliceName : The name of this element definition slice, when slicing is working. The name must be a token with no dots or spaces. This is a unique name referring to a specific set of constraints applied to this element, used to provide a name to different slices of the same element.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | Name for this particular element (in a set of slices) |
| ... [sliceIsConstraining](elementdefinition-definitions.html#ElementDefinition.sliceIsConstraining "ElementDefinition.sliceIsConstraining : If true, indicates that this slice definition is constraining a slice definition with the same name in an inherited profile. If false, the slice is not overriding any slice in an inherited profile. If missing, the slice might or might not be overriding a slice in an inherited profile, depending on the sliceName.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[TU](versions.html#std-process "Standards Status = Trial Use") | 0..1 | [boolean](datatypes.html#boolean) | If this slice definition constrains an inherited slice definition (or not) |
| ... [label](elementdefinition-definitions.html#ElementDefinition.label "ElementDefinition.label : A single preferred label which is the text to display beside the element indicating its meaning or to use to prompt for the element in a user display or form.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | Name for element to display with or prompt for element |
| ... [code](elementdefinition-definitions.html#ElementDefinition.code "ElementDefinition.code : A code that has the same meaning as the element in a particular terminology.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [Coding](datatypes.html#Coding) | Corresponding codes in terminologies [LOINC Codes](valueset-observation-codes.html "Codes that indicate the meaning of a data element.") ([Example](terminologies.html#example "Instances are not expected or even encouraged to draw from the specified value set.  The value set merely provides examples of the types of concepts intended to be included.")) |
| ... [slicing](elementdefinition-definitions.html#ElementDefinition.slicing "ElementDefinition.slicing : Indicates that the element is sliced into a set of alternative definitions (i.e. in a structure definition, there are multiple different constraints on a single element in the base resource). Slicing can be used in any resource that has cardinality ..* on the base resource, or any resource with a choice of types. The set of slices is any elements that come after this in the element sequence that have the same path, until a shorter path occurs (the shorter path terminates the set).") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..1 | [Element](element.html) | This element is sliced - slices follow + Rule: If there are no discriminators, there must be a definition |
| .... [discriminator](elementdefinition-definitions.html#ElementDefinition.slicing.discriminator "ElementDefinition.slicing.discriminator : Designates which child elements are used to discriminate between the slices when processing an instance. If one or more discriminators are provided, the value of the child elements in the instance data SHALL completely distinguish which slice the element in the resource matches based on the allowed values for those elements in each of the slices.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [Element](element.html) | Element values that are used to distinguish the slices |
| ..... [type](elementdefinition-definitions.html#ElementDefinition.slicing.discriminator.type "ElementDefinition.slicing.discriminator.type : How the element value is interpreted when discrimination is evaluated.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [code](datatypes.html#code) | value | exists | pattern | type | profile [DiscriminatorType](valueset-discriminator-type.html "How an element value is interpreted when discrimination is evaluated.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ..... [path](elementdefinition-definitions.html#ElementDefinition.slicing.discriminator.path "ElementDefinition.slicing.discriminator.path : A FHIRPath expression, using [the simple subset of FHIRPath](fhirpath.html#simple), that is used to identify the element on which discrimination is based.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [string](datatypes.html#string) | Path to element value |
| .... [description](elementdefinition-definitions.html#ElementDefinition.slicing.description "ElementDefinition.slicing.description : A human-readable text description of how the slicing works. If there is no discriminator, this is required to be present to provide whatever information is possible about how the slices can be differentiated.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..1 | [string](datatypes.html#string) | Text description of how slicing works (or not) |
| .... [ordered](elementdefinition-definitions.html#ElementDefinition.slicing.ordered "ElementDefinition.slicing.ordered : If the matching elements have to occur in the same order as defined in the profile.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [boolean](datatypes.html#boolean) | If elements must be in same order as slices |
| .... [rules](elementdefinition-definitions.html#ElementDefinition.slicing.rules "ElementDefinition.slicing.rules : Whether additional slices are allowed or not. When the slices are ordered, profile authors can also say that additional slices are only allowed at the end.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [code](datatypes.html#code) | closed | open | openAtEnd [SlicingRules](valueset-resource-slicing-rules.html "How slices are interpreted when evaluating an instance.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ... [short](elementdefinition-definitions.html#ElementDefinition.short "ElementDefinition.short : A concise description of what this element means (e.g. for use in autogenerated summaries).") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | Concise definition for space-constrained presentation |
| ... [definition](elementdefinition-definitions.html#ElementDefinition.definition "ElementDefinition.definition : Provides a complete explanation of the meaning of the data element for human readability.  For the case of elements derived from existing elements (e.g. constraints), the definition SHALL be consistent with the base definition, but convey the meaning of the element in the particular context of use of the resource. (Note: The text you are reading is specified in ElementDefinition.definition).") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [markdown](datatypes.html#markdown) | Full formal definition as narrative text |
| ... [comment](elementdefinition-definitions.html#ElementDefinition.comment "ElementDefinition.comment : Explanatory notes and implementation guidance about the data element, including notes about how to use the data properly, exceptions to proper use, etc. (Note: The text you are reading is specified in ElementDefinition.comment).") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [markdown](datatypes.html#markdown) | Comments about the use of this element |
| ... [requirements](elementdefinition-definitions.html#ElementDefinition.requirements "ElementDefinition.requirements : This element is for traceability of why the element was created and why the constraints exist as they do. This may be used to point to source materials or specifications that drove the structure of this element.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [markdown](datatypes.html#markdown) | Why this resource has been created |
| ... [alias](elementdefinition-definitions.html#ElementDefinition.alias "ElementDefinition.alias : Identifies additional names by which this element might also be known.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [string](datatypes.html#string) | Other names |
| ... [min](elementdefinition-definitions.html#ElementDefinition.min "ElementDefinition.min : The minimum number of times this element SHALL appear in the instance.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..1 | [unsignedInt](datatypes.html#unsignedInt) | Minimum Cardinality |
| ... [max](elementdefinition-definitions.html#ElementDefinition.max "ElementDefinition.max : The maximum number of times this element is permitted to appear in the instance.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..1 | [string](datatypes.html#string) | Maximum Cardinality (a number or \*) + Rule: Max SHALL be a number or "\*" |
| ... [base](elementdefinition-definitions.html#ElementDefinition.base "ElementDefinition.base : Information about the base definition of the element, provided to make it unnecessary for tools to trace the deviation of the element through the derived and related profiles. When the element definition is not the original definition of an element - i.g. either in a constraint on another type, or for elements from a super type in a snap shot - then the information in provided in the element definition may be different to the base definition. On the original definition of the element, it will be same.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [Element](element.html) | Base definition information for tools |
| .... [path](elementdefinition-definitions.html#ElementDefinition.base.path "ElementDefinition.base.path : The Path that identifies the base element - this matches the ElementDefinition.path for that element. Across FHIR, there is only one base definition of any element - that is, an element definition on a [[[StructureDefinition]]] without a StructureDefinition.base.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [string](datatypes.html#string) | Path that identifies the base element |
| .... [min](elementdefinition-definitions.html#ElementDefinition.base.min "ElementDefinition.base.min : Minimum cardinality of the base element identified by the path.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [unsignedInt](datatypes.html#unsignedInt) | Min cardinality of the base element |
| .... [max](elementdefinition-definitions.html#ElementDefinition.base.max "ElementDefinition.base.max : Maximum cardinality of the base element identified by the path.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [string](datatypes.html#string) | Max cardinality of the base element |
| ... [contentReference](elementdefinition-definitions.html#ElementDefinition.contentReference "ElementDefinition.contentReference : Identifies an element defined elsewhere in the definition whose content rules should be applied to the current element. ContentReferences bring across all the rules that are in the ElementDefinition for the element, including definitions, cardinality constraints, bindings, invariants etc.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..1 | [uri](datatypes.html#uri) | Reference to definition of content for the element |
| ... [type](elementdefinition-definitions.html#ElementDefinition.type "ElementDefinition.type : The data type or resource that the value of this element is permitted to be.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..\* | [Element](element.html) | Data type and Profile for this element + Rule: Aggregation may only be specified if one of the allowed types for the element is a reference + Rule: targetProfile is only allowed if the type is Reference or canonical |
| .... [code](elementdefinition-definitions.html#ElementDefinition.type.code "ElementDefinition.type.code : URL of Data type or Resource that is a(or the) type used for this element. References are URLs that are relative to http://hl7.org/fhir/StructureDefinition e.g. \"string\" is a reference to http://hl7.org/fhir/StructureDefinition/string. Absolute URLs are only allowed in logical models.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [uri](datatypes.html#uri) | Data type or Resource (reference to definition) [FHIRDefinedType](valueset-defined-types.html "Either a resource or a data type, including logical model types.") ([Extensible](terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept (based on human review), alternate codings (or, data type allowing, text) may be included instead.")) |
| .... [profile](elementdefinition-definitions.html#ElementDefinition.type.profile "ElementDefinition.type.profile : Identifies a profile structure or implementation Guide that applies to the datatype this element refers to. If any profiles are specified, then the content must conform to at least one of them. The URL can be a local reference - to a contained StructureDefinition, or a reference to another StructureDefinition or Implementation Guide by a canonical URL. When an implementation guide is specified, the type SHALL conform to at least one profile defined in the implementation guide.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [canonical](datatypes.html#canonical)([StructureDefinition](structuredefinition.html) | [ImplementationGuide](implementationguide.html)) | Profiles (StructureDefinition or IG) - one must apply |
| .... [targetProfile](elementdefinition-definitions.html#ElementDefinition.type.targetProfile "ElementDefinition.type.targetProfile : Used when the type is \"Reference\" or \"canonical\", and identifies a profile structure or implementation Guide that applies to the target of the reference this element refers to. If any profiles are specified, then the content must conform to at least one of them. The URL can be a local reference - to a contained StructureDefinition, or a reference to another StructureDefinition or Implementation Guide by a canonical URL. When an implementation guide is specified, the target resource SHALL conform to at least one profile defined in the implementation guide.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [canonical](datatypes.html#canonical)([StructureDefinition](structuredefinition.html) | [ImplementationGuide](implementationguide.html)) | Profile (StructureDefinition or IG) on the Reference/canonical target - one must apply |
| .... [aggregation](elementdefinition-definitions.html#ElementDefinition.type.aggregation "ElementDefinition.type.aggregation : If the type is a reference to another resource, how the resource is or can be aggregated - is it a contained resource, or a reference, and if the context is a bundle, is it included in the bundle.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..\* | [code](datatypes.html#code) | contained | referenced | bundled - how aggregated [AggregationMode](valueset-resource-aggregation-mode.html "How resource references can be aggregated.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| .... [versioning](elementdefinition-definitions.html#ElementDefinition.type.versioning "ElementDefinition.type.versioning : Whether this reference needs to be version specific or version independent, or whether either can be used.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [code](datatypes.html#code) | either | independent | specific [ReferenceVersionRules](valueset-reference-version-rules.html "Whether a reference needs to be version specific or version independent, or whether either can be used.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ... [defaultValue[x]](elementdefinition-definitions.html#ElementDefinition.defaultValue_x_ "ElementDefinition.defaultValue[x] : The value that should be used if there is no value stated in the instance (e.g. 'if not otherwise specified, the abstract is false').") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..1 | [\*](datatypes.html#open) | Specified value if missing from instance |
| ... [meaningWhenMissing](elementdefinition-definitions.html#ElementDefinition.meaningWhenMissing "ElementDefinition.meaningWhenMissing : The Implicit meaning that is to be understood when this element is missing (e.g. 'when this element is missing, the period is ongoing').") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..1 | [markdown](datatypes.html#markdown) | Implicit meaning when this element is missing |
| ... [orderMeaning](elementdefinition-definitions.html#ElementDefinition.orderMeaning "ElementDefinition.orderMeaning : If present, indicates that the order of the repeating element has meaning and describes what that meaning is.  If absent, it means that the order of the element has no meaning.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | What the order of the elements means |
| ... [fixed[x]](elementdefinition-definitions.html#ElementDefinition.fixed_x_ "ElementDefinition.fixed[x] : Specifies a value that SHALL be exactly the value  for this element in the instance. For purposes of comparison, non-significant whitespace is ignored, and all values must be an exact match (case and accent sensitive). Missing elements/attributes must also be missing.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..1 | [\*](datatypes.html#open) | Value must be exactly this |
| ... [pattern[x]](elementdefinition-definitions.html#ElementDefinition.pattern_x_ "ElementDefinition.pattern[x] : Specifies a value that the value in the instance SHALL follow - that is, any value in the pattern must be found in the instance. Other additional values may be found too. This is effectively constraint by example.    When pattern[x] is used to constrain a primitive, it means that the value provided in the pattern[x] must match the instance value exactly.  When pattern[x] is used to constrain an array, it means that each element provided in the pattern[x] array must (recursively) match at least one element from the instance array.  When pattern[x] is used to constrain a complex object, it means that each property in the pattern must be present in the complex object, and its value must recursively match -- i.e.,  1. If primitive: it must match exactly the pattern value 2. If a complex object: it must match (recursively) the pattern value 3. If an array: it must match (recursively) the pattern value.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..1 | [\*](datatypes.html#open) | Value must have at least these property values |
| ... [example](elementdefinition-definitions.html#ElementDefinition.example "ElementDefinition.example : A sample value for this element demonstrating the type of information that would typically be found in the element.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [Element](element.html) | Example value (as defined for type) |
| .... [label](elementdefinition-definitions.html#ElementDefinition.example.label "ElementDefinition.example.label : Describes the purpose of this example amoung the set of examples.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [string](datatypes.html#string) | Describes the purpose of this example |
| .... [value[x]](elementdefinition-definitions.html#ElementDefinition.example.value_x_ "ElementDefinition.example.value[x] : The actual value for the element, which must be one of the types allowed for this element.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [\*](datatypes.html#open) | Value of Example (one of allowed types) |
| ... [minValue[x]](elementdefinition-definitions.html#ElementDefinition.minValue_x_ "ElementDefinition.minValue[x] : The minimum allowed value for the element. The value is inclusive. This is allowed for the types date, dateTime, instant, time, decimal, integer, and Quantity.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 |  | Minimum Allowed Value (for some types) |
| .... minValueDate |  |  | [date](datatypes.html#date) |  |
| .... minValueDateTime |  |  | [dateTime](datatypes.html#dateTime) |  |
| .... minValueInstant |  |  | [instant](datatypes.html#instant) |  |
| .... minValueTime |  |  | [time](datatypes.html#time) |  |
| .... minValueDecimal |  |  | [decimal](datatypes.html#decimal) |  |
| .... minValueInteger |  |  | [integer](datatypes.html#integer) |  |
| .... minValuePositiveInt |  |  | [positiveInt](datatypes.html#positiveInt) |  |
| .... minValueUnsignedInt |  |  | [unsignedInt](datatypes.html#unsignedInt) |  |
| .... minValueQuantity |  |  | [Quantity](datatypes.html#Quantity) |  |
| ... [maxValue[x]](elementdefinition-definitions.html#ElementDefinition.maxValue_x_ "ElementDefinition.maxValue[x] : The maximum allowed value for the element. The value is inclusive. This is allowed for the types date, dateTime, instant, time, decimal, integer, and Quantity.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 |  | Maximum Allowed Value (for some types) |
| .... maxValueDate |  |  | [date](datatypes.html#date) |  |
| .... maxValueDateTime |  |  | [dateTime](datatypes.html#dateTime) |  |
| .... maxValueInstant |  |  | [instant](datatypes.html#instant) |  |
| .... maxValueTime |  |  | [time](datatypes.html#time) |  |
| .... maxValueDecimal |  |  | [decimal](datatypes.html#decimal) |  |
| .... maxValueInteger |  |  | [integer](datatypes.html#integer) |  |
| .... maxValuePositiveInt |  |  | [positiveInt](datatypes.html#positiveInt) |  |
| .... maxValueUnsignedInt |  |  | [unsignedInt](datatypes.html#unsignedInt) |  |
| .... maxValueQuantity |  |  | [Quantity](datatypes.html#Quantity) |  |
| ... [maxLength](elementdefinition-definitions.html#ElementDefinition.maxLength "ElementDefinition.maxLength : Indicates the maximum length in characters that is permitted to be present in conformant instances and which is expected to be supported by conformant consumers that support the element.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [integer](datatypes.html#integer) | Max length for strings |
| ... [condition](elementdefinition-definitions.html#ElementDefinition.condition "ElementDefinition.condition : A reference to an invariant that may make additional statements about the cardinality or value in the instance.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [id](datatypes.html#id) | Reference to invariant about presence |
| ... [constraint](elementdefinition-definitions.html#ElementDefinition.constraint "ElementDefinition.constraint : Formal constraints such as co-occurrence and other constraints that can be computationally evaluated within the context of the instance.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..\* | [Element](element.html) | Condition that must evaluate to true + Warning: Constraints should have an expression or else validators will not be able to enforce them |
| .... [key](elementdefinition-definitions.html#ElementDefinition.constraint.key "ElementDefinition.constraint.key : Allows identification of which elements have their cardinalities impacted by the constraint.  Will not be referenced for constraints that do not affect cardinality.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 1..1 | [id](datatypes.html#id) | Target of 'condition' reference above |
| .... [requirements](elementdefinition-definitions.html#ElementDefinition.constraint.requirements "ElementDefinition.constraint.requirements : Description of why this constraint is necessary or appropriate.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | Why this constraint is necessary or appropriate |
| .... [severity](elementdefinition-definitions.html#ElementDefinition.constraint.severity "ElementDefinition.constraint.severity : Identifies the impact constraint violation has on the conformance of the instance.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [code](datatypes.html#code) | error | warning [ConstraintSeverity](valueset-constraint-severity.html "SHALL applications comply with this constraint?") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| .... [human](elementdefinition-definitions.html#ElementDefinition.constraint.human "ElementDefinition.constraint.human : Text that can be used to describe the constraint in messages identifying that the constraint has been violated.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [string](datatypes.html#string) | Human description of constraint |
| .... [expression](elementdefinition-definitions.html#ElementDefinition.constraint.expression "ElementDefinition.constraint.expression : A [FHIRPath](fhirpath.html) expression of constraint that can be executed to see if this constraint is met.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | FHIRPath expression of constraint |
| .... [xpath](elementdefinition-definitions.html#ElementDefinition.constraint.xpath "ElementDefinition.constraint.xpath : An XPath expression of constraint that can be executed to see if this constraint is met.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[TU](versions.html#std-process "Standards Status = Trial Use") | 0..1 | [string](datatypes.html#string) | XPath expression of constraint |
| .... [source](elementdefinition-definitions.html#ElementDefinition.constraint.source "ElementDefinition.constraint.source : A reference to the original source of the constraint, for traceability purposes.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [canonical](datatypes.html#canonical)([StructureDefinition](structuredefinition.html)) | Reference to original source of constraint |
| ... [mustSupport](elementdefinition-definitions.html#ElementDefinition.mustSupport "ElementDefinition.mustSupport : If true, implementations that produce or consume resources SHALL provide \"support\" for the element in some meaningful way.  If false, the element may be ignored and not supported. If false, whether to populate or use the data element in any way is at the discretion of the implementation.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [boolean](datatypes.html#boolean) | If the element must be supported |
| ... [isModifier](elementdefinition-definitions.html#ElementDefinition.isModifier "ElementDefinition.isModifier : If true, the value of this element affects the interpretation of the element or resource that contains it, and the value of the element cannot be ignored. Typically, this is used for status, negation and qualification codes. The effect of this is that the element cannot be ignored by systems: they SHALL either recognize the element and process it, and/or a pre-determination has been made that it is not relevant to their particular system.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [boolean](datatypes.html#boolean) | If this modifies the meaning of other elements |
| ... [isModifierReason](elementdefinition-definitions.html#ElementDefinition.isModifierReason "ElementDefinition.isModifierReason : Explains how that element affects the interpretation of the resource or element that contains it.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | Reason that this element is marked as a modifier |
| ... [isSummary](elementdefinition-definitions.html#ElementDefinition.isSummary "ElementDefinition.isSummary : Whether the element should be included if a client requests a search with the parameter _summary=true.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [boolean](datatypes.html#boolean) | Include when \_summary = true? |
| ... [binding](elementdefinition-definitions.html#ElementDefinition.binding "ElementDefinition.binding : Binds to a value set if this element is coded (code, Coding, CodeableConcept, Quantity), or the data types (string, uri).") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..1 | [Element](element.html) | ValueSet details if this is coded + Rule: ValueSet SHALL start with http:// or https:// or urn: |
| .... [strength](elementdefinition-definitions.html#ElementDefinition.binding.strength "ElementDefinition.binding.strength : Indicates the degree of conformance expectations associated with this binding - that is, the degree to which the provided value set must be adhered to in the instances.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [code](datatypes.html#code) | required | extensible | preferred | example [BindingStrength](valueset-binding-strength.html "Indication of the degree of conformance expectations associated with a binding.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| .... [description](elementdefinition-definitions.html#ElementDefinition.binding.description "ElementDefinition.binding.description : Describes the intended use of this particular set of codes.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | Human explanation of the value set |
| .... [valueSet](elementdefinition-definitions.html#ElementDefinition.binding.valueSet "ElementDefinition.binding.valueSet : Refers to the value set that identifies the set of codes the binding refers to.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..1 | [canonical](datatypes.html#canonical)([ValueSet](valueset.html)) | Source of value set |
| ... [mapping](elementdefinition-definitions.html#ElementDefinition.mapping "ElementDefinition.mapping : Identifies a concept from an external specification that roughly corresponds to this element.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [Element](element.html) | Map element to another set of definitions |
| .... [identity](elementdefinition-definitions.html#ElementDefinition.mapping.identity "ElementDefinition.mapping.identity : An internal reference to the definition of a mapping.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [id](datatypes.html#id) | Reference to mapping declaration |
| .... [language](elementdefinition-definitions.html#ElementDefinition.mapping.language "ElementDefinition.mapping.language : Identifies the computable language in which mapping.map is expressed.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [code](datatypes.html#code) | Computable language of mapping [MimeType](valueset-mimetypes.html "The mime type of an attachment. Any valid mime type is allowed.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| .... [map](elementdefinition-definitions.html#ElementDefinition.mapping.map "ElementDefinition.mapping.map : Expresses what part of the target specification corresponds to this element.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [string](datatypes.html#string) | Details of the mapping |
| .... [comment](elementdefinition-definitions.html#ElementDefinition.mapping.comment "ElementDefinition.mapping.comment : Comments that provide information about the mapping or its use.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | Comments about the mapping or its use |
| [doco Documentation for this format](formats.html#table "Legend for this format") | | | | |

**UML Diagram** ([Legend](formats.html#uml))

**XML Template**

```

<ElementDefinition xmlns="http://hl7.org/fhir">
 <!-- from BackboneElement: extension, modifierExtension -->
 <path value="[string]"/><!-- 1..1 Path of the element in the hierarchy of elements -->
 <representation value="[code]"/><!-- 0..* xmlAttr | xmlText | typeAttr | cdaText | xhtml -->
 <sliceName value="[string]"/><!-- 0..1 Name for this particular element (in a set of slices) -->
 <sliceIsConstraining value="[boolean]"/><!-- 0..1 If this slice definition constrains an inherited slice definition (or not) -->
 <label value="[string]"/><!-- 0..1 Name for element to display with or prompt for element -->
 <code><!-- 0..* Coding Corresponding codes in terminologies --></code>
 <slicing>  <!-- 0..1 This element is sliced - slices follow -->
  <discriminator>  <!-- 0..* Element values that are used to distinguish the slices -->
   <type value="[code]"/><!-- 1..1 value | exists | pattern | type | profile -->
   <path value="[string]"/><!-- 1..1 Path to element value -->
  </discriminator>
  <description value="[string]"/><!-- ![??](lock.png) 0..1 Text description of how slicing works (or not) -->
  <ordered value="[boolean]"/><!-- 0..1 If elements must be in same order as slices -->
  <rules value="[code]"/><!-- 1..1 closed | open | openAtEnd -->
 </slicing>
 <short value="[string]"/><!-- 0..1 Concise definition for space-constrained presentation -->
 <definition value="[markdown]"/><!-- 0..1 Full formal definition as narrative text -->
 <comment value="[markdown]"/><!-- 0..1 Comments about the use of this element -->
 <requirements value="[markdown]"/><!-- 0..1 Why this resource has been created -->
 <alias value="[string]"/><!-- 0..* Other names -->
 <min value="[unsignedInt]"/><!-- ![??](lock.png) 0..1 Minimum Cardinality -->
 <max value="[string]"/><!-- ![??](lock.png) 0..1 Maximum Cardinality (a number or *) -->
 <base>  <!-- 0..1 Base definition information for tools -->
  <path value="[string]"/><!-- 1..1 Path that identifies the base element -->
  <min value="[unsignedInt]"/><!-- 1..1 Min cardinality of the base element -->
  <max value="[string]"/><!-- 1..1 Max cardinality of the base element -->
 </base>
 <contentReference value="[uri]"/><!-- ![??](lock.png) 0..1 Reference to definition of content for the element -->
 <type>  <!-- ![??](lock.png) 0..* Data type and Profile for this element -->
  <code value="[uri]"/><!-- 1..1 Data type or Resource (reference to definition) -->
  <profile><!-- 0..* canonical(StructureDefinition|ImplementationGuide) Profiles (StructureDefinition or IG) - one must apply --></profile>
  <targetProfile><!-- 0..* canonical(StructureDefinition|ImplementationGuide) Profile (StructureDefinition or IG) on the Reference/canonical target - one must apply --></targetProfile>
  <aggregation value="[code]"/><!-- ![??](lock.png) 0..* contained | referenced | bundled - how aggregated -->
  <versioning value="[code]"/><!-- 0..1 either | independent | specific -->
 </type>
 <defaultValue[x]><!-- ![??](lock.png) 0..1 * Specified value if missing from instance --></defaultValue[x]>
 <meaningWhenMissing value="[markdown]"/><!-- ![??](lock.png) 0..1 Implicit meaning when this element is missing -->
 <orderMeaning value="[string]"/><!-- 0..1 What the order of the elements means -->
 <fixed[x]><!-- ![??](lock.png) 0..1 * Value must be exactly this --></fixed[x]>
 <pattern[x]><!-- ![??](lock.png) 0..1 * Value must have at least these property values --></pattern[x]>
 <example>  <!-- 0..* Example value (as defined for type) -->
  <label value="[string]"/><!-- 1..1 Describes the purpose of this example -->
  <value[x]><!-- 1..1 * Value of Example (one of allowed types) --></value[x]>
 </example>
 <minValue[x]><!-- 0..1 date|dateTime|instant|time|decimal|integer|positiveInt|
   unsignedInt|Quantity Minimum Allowed Value (for some types) --></minValue[x]>
 <maxValue[x]><!-- 0..1 date|dateTime|instant|time|decimal|integer|positiveInt|
   unsignedInt|Quantity Maximum Allowed Value (for some types) --></maxValue[x]>
 <maxLength value="[integer]"/><!-- 0..1 Max length for strings -->
 <condition value="[id]"/><!-- 0..* Reference to invariant about presence -->
 <constraint>  <!-- 0..* Condition that must evaluate to true -->
  <key value="[id]"/><!-- ![??](lock.png) 1..1 Target of 'condition' reference above -->
  <requirements value="[string]"/><!-- 0..1 Why this constraint is necessary or appropriate -->
  <severity value="[code]"/><!-- 1..1 error | warning -->
  <human value="[string]"/><!-- 1..1 Human description of constraint -->
  <expression value="[string]"/><!-- 0..1 FHIRPath expression of constraint -->
  <xpath value="[string]"/><!-- 0..1 XPath expression of constraint -->
  <source><!-- 0..1 canonical(StructureDefinition) Reference to original source of constraint --></source>
 </constraint>
 <mustSupport value="[boolean]"/><!-- 0..1 If the element must be supported -->
 <isModifier value="[boolean]"/><!-- 0..1 If this modifies the meaning of other elements -->
 <isModifierReason value="[string]"/><!-- 0..1 Reason that this element is marked as a modifier -->
 <isSummary value="[boolean]"/><!-- 0..1 Include when _summary = true? -->
 <binding>  <!-- ![??](lock.png) 0..1 ValueSet details if this is coded -->
  <strength value="[code]"/><!-- 1..1 required | extensible | preferred | example -->
  <description value="[string]"/><!-- 0..1 Human explanation of the value set -->
  <valueSet><!-- ![??](lock.png) 0..1 canonical(ValueSet) Source of value set --></valueSet>
 </binding>
 <mapping>  <!-- 0..* Map element to another set of definitions -->
  <identity value="[id]"/><!-- 1..1 Reference to mapping declaration -->
  <language value="[code]"/><!-- 0..1 Computable language of mapping -->
  <map value="[string]"/><!-- 1..1 Details of the mapping -->
  <comment value="[string]"/><!-- 0..1 Comments about the mapping or its use -->
 </mapping>
</ElementDefinition>
```

**JSON Template**

```

{![doco](help.png)
  // from BackboneElement: extension, modifierExtension
  "path" : "<string>", // R!  Path of the element in the hierarchy of elements
  "representation" : ["<code>"], // xmlAttr | xmlText | typeAttr | cdaText | xhtml
  "sliceName" : "<string>", // Name for this particular element (in a set of slices)
  "sliceIsConstraining" : <boolean>, // If this slice definition constrains an inherited slice definition (or not)
  "label" : "<string>", // Name for element to display with or prompt for element
  "code" : [{ Coding }], // Corresponding codes in terminologies
  "slicing" : { // This element is sliced - slices follow
    "discriminator" : [{ // Element values that are used to distinguish the slices
      "type" : "<code>", // R!  value | exists | pattern | type | profile
      "path" : "<string>" // R!  Path to element value
    }],
    "description" : "<string>", // C? Text description of how slicing works (or not)
    "ordered" : <boolean>, // If elements must be in same order as slices
    "rules" : "<code>" // R!  closed | open | openAtEnd
  },
  "short" : "<string>", // Concise definition for space-constrained presentation
  "definition" : "<markdown>", // Full formal definition as narrative text
  "comment" : "<markdown>", // Comments about the use of this element
  "requirements" : "<markdown>", // Why this resource has been created
  "alias" : ["<string>"], // Other names
  "min" : "<unsignedInt>", // C? Minimum Cardinality
  "max" : "<string>", // C? Maximum Cardinality (a number or *)
  "base" : { // Base definition information for tools
    "path" : "<string>", // R!  Path that identifies the base element
    "min" : "<unsignedInt>", // R!  Min cardinality of the base element
    "max" : "<string>" // R!  Max cardinality of the base element
  },
  "contentReference" : "<uri>", // C? Reference to definition of content for the element
  "type" : [{ // C? Data type and Profile for this element
    "code" : "<uri>", // R!  Data type or Resource (reference to definition)
    "profile" : [{ canonical(StructureDefinition|ImplementationGuide) }], // Profiles (StructureDefinition or IG) - one must apply
    "targetProfile" : [{ canonical(StructureDefinition|ImplementationGuide) }], // Profile (StructureDefinition or IG) on the Reference/canonical target - one must apply
    "aggregation" : ["<code>"], // C? contained | referenced | bundled - how aggregated
    "versioning" : "<code>" // either | independent | specific
  }],
  // defaultValue[x]: Specified value if missing from instance. One of these 50:
  "defaultValueBase64Binary" : "<base64Binary>",
  "defaultValueBoolean" : <boolean>,
  "defaultValueCanonical" : "<canonical>",
  "defaultValueCode" : "<code>",
  "defaultValueDate" : "<date>",
  "defaultValueDateTime" : "<dateTime>",
  "defaultValueDecimal" : <decimal>,
  "defaultValueId" : "<id>",
  "defaultValueInstant" : "<instant>",
  "defaultValueInteger" : <integer>,
  "defaultValueMarkdown" : "<markdown>",
  "defaultValueOid" : "<oid>",
  "defaultValuePositiveInt" : "<positiveInt>",
  "defaultValueString" : "<string>",
  "defaultValueTime" : "<time>",
  "defaultValueUnsignedInt" : "<unsignedInt>",
  "defaultValueUri" : "<uri>",
  "defaultValueUrl" : "<url>",
  "defaultValueUuid" : "<uuid>",
  "defaultValueAddress" : { Address },
  "defaultValueAge" : { Age },
  "defaultValueAnnotation" : { Annotation },
  "defaultValueAttachment" : { Attachment },
  "defaultValueCodeableConcept" : { CodeableConcept },
  "defaultValueCoding" : { Coding },
  "defaultValueContactPoint" : { ContactPoint },
  "defaultValueCount" : { Count },
  "defaultValueDistance" : { Distance },
  "defaultValueDuration" : { Duration },
  "defaultValueHumanName" : { HumanName },
  "defaultValueIdentifier" : { Identifier },
  "defaultValueMoney" : { Money },
  "defaultValuePeriod" : { Period },
  "defaultValueQuantity" : { Quantity },
  "defaultValueRange" : { Range },
  "defaultValueRatio" : { Ratio },
  "defaultValueReference" : { Reference },
  "defaultValueSampledData" : { SampledData },
  "defaultValueSignature" : { Signature },
  "defaultValueTiming" : { Timing },
  "defaultValueContactDetail" : { ContactDetail },
  "defaultValueContributor" : { Contributor },
  "defaultValueDataRequirement" : { DataRequirement },
  "defaultValueExpression" : { Expression },
  "defaultValueParameterDefinition" : { ParameterDefinition },
  "defaultValueRelatedArtifact" : { RelatedArtifact },
  "defaultValueTriggerDefinition" : { TriggerDefinition },
  "defaultValueUsageContext" : { UsageContext },
  "defaultValueDosage" : { Dosage },
  "defaultValueMeta" : { Meta },
  "meaningWhenMissing" : "<markdown>", // C? Implicit meaning when this element is missing
  "orderMeaning" : "<string>", // What the order of the elements means
  // fixed[x]: Value must be exactly this. One of these 50:
  "fixedBase64Binary" : "<base64Binary>",
  "fixedBoolean" : <boolean>,
  "fixedCanonical" : "<canonical>",
  "fixedCode" : "<code>",
  "fixedDate" : "<date>",
  "fixedDateTime" : "<dateTime>",
  "fixedDecimal" : <decimal>,
  "fixedId" : "<id>",
  "fixedInstant" : "<instant>",
  "fixedInteger" : <integer>,
  "fixedMarkdown" : "<markdown>",
  "fixedOid" : "<oid>",
  "fixedPositiveInt" : "<positiveInt>",
  "fixedString" : "<string>",
  "fixedTime" : "<time>",
  "fixedUnsignedInt" : "<unsignedInt>",
  "fixedUri" : "<uri>",
  "fixedUrl" : "<url>",
  "fixedUuid" : "<uuid>",
  "fixedAddress" : { Address },
  "fixedAge" : { Age },
  "fixedAnnotation" : { Annotation },
  "fixedAttachment" : { Attachment },
  "fixedCodeableConcept" : { CodeableConcept },
  "fixedCoding" : { Coding },
  "fixedContactPoint" : { ContactPoint },
  "fixedCount" : { Count },
  "fixedDistance" : { Distance },
  "fixedDuration" : { Duration },
  "fixedHumanName" : { HumanName },
  "fixedIdentifier" : { Identifier },
  "fixedMoney" : { Money },
  "fixedPeriod" : { Period },
  "fixedQuantity" : { Quantity },
  "fixedRange" : { Range },
  "fixedRatio" : { Ratio },
  "fixedReference" : { Reference },
  "fixedSampledData" : { SampledData },
  "fixedSignature" : { Signature },
  "fixedTiming" : { Timing },
  "fixedContactDetail" : { ContactDetail },
  "fixedContributor" : { Contributor },
  "fixedDataRequirement" : { DataRequirement },
  "fixedExpression" : { Expression },
  "fixedParameterDefinition" : { ParameterDefinition },
  "fixedRelatedArtifact" : { RelatedArtifact },
  "fixedTriggerDefinition" : { TriggerDefinition },
  "fixedUsageContext" : { UsageContext },
  "fixedDosage" : { Dosage },
  "fixedMeta" : { Meta },
  // pattern[x]: Value must have at least these property values. One of these 50:
  "patternBase64Binary" : "<base64Binary>",
  "patternBoolean" : <boolean>,
  "patternCanonical" : "<canonical>",
  "patternCode" : "<code>",
  "patternDate" : "<date>",
  "patternDateTime" : "<dateTime>",
  "patternDecimal" : <decimal>,
  "patternId" : "<id>",
  "patternInstant" : "<instant>",
  "patternInteger" : <integer>,
  "patternMarkdown" : "<markdown>",
  "patternOid" : "<oid>",
  "patternPositiveInt" : "<positiveInt>",
  "patternString" : "<string>",
  "patternTime" : "<time>",
  "patternUnsignedInt" : "<unsignedInt>",
  "patternUri" : "<uri>",
  "patternUrl" : "<url>",
  "patternUuid" : "<uuid>",
  "patternAddress" : { Address },
  "patternAge" : { Age },
  "patternAnnotation" : { Annotation },
  "patternAttachment" : { Attachment },
  "patternCodeableConcept" : { CodeableConcept },
  "patternCoding" : { Coding },
  "patternContactPoint" : { ContactPoint },
  "patternCount" : { Count },
  "patternDistance" : { Distance },
  "patternDuration" : { Duration },
  "patternHumanName" : { HumanName },
  "patternIdentifier" : { Identifier },
  "patternMoney" : { Money },
  "patternPeriod" : { Period },
  "patternQuantity" : { Quantity },
  "patternRange" : { Range },
  "patternRatio" : { Ratio },
  "patternReference" : { Reference },
  "patternSampledData" : { SampledData },
  "patternSignature" : { Signature },
  "patternTiming" : { Timing },
  "patternContactDetail" : { ContactDetail },
  "patternContributor" : { Contributor },
  "patternDataRequirement" : { DataRequirement },
  "patternExpression" : { Expression },
  "patternParameterDefinition" : { ParameterDefinition },
  "patternRelatedArtifact" : { RelatedArtifact },
  "patternTriggerDefinition" : { TriggerDefinition },
  "patternUsageContext" : { UsageContext },
  "patternDosage" : { Dosage },
  "patternMeta" : { Meta },
  "example" : [{ // Example value (as defined for type)
    "label" : "<string>", // R!  Describes the purpose of this example
    // value[x]: Value of Example (one of allowed types). One of these 50:
    "valueBase64Binary" : "<base64Binary>"
    "valueBoolean" : <boolean>
    "valueCanonical" : "<canonical>"
    "valueCode" : "<code>"
    "valueDate" : "<date>"
    "valueDateTime" : "<dateTime>"
    "valueDecimal" : <decimal>
    "valueId" : "<id>"
    "valueInstant" : "<instant>"
    "valueInteger" : <integer>
    "valueMarkdown" : "<markdown>"
    "valueOid" : "<oid>"
    "valuePositiveInt" : "<positiveInt>"
    "valueString" : "<string>"
    "valueTime" : "<time>"
    "valueUnsignedInt" : "<unsignedInt>"
    "valueUri" : "<uri>"
    "valueUrl" : "<url>"
    "valueUuid" : "<uuid>"
    "valueAddress" : { Address }
    "valueAge" : { Age }
    "valueAnnotation" : { Annotation }
    "valueAttachment" : { Attachment }
    "valueCodeableConcept" : { CodeableConcept }
    "valueCoding" : { Coding }
    "valueContactPoint" : { ContactPoint }
    "valueCount" : { Count }
    "valueDistance" : { Distance }
    "valueDuration" : { Duration }
    "valueHumanName" : { HumanName }
    "valueIdentifier" : { Identifier }
    "valueMoney" : { Money }
    "valuePeriod" : { Period }
    "valueQuantity" : { Quantity }
    "valueRange" : { Range }
    "valueRatio" : { Ratio }
    "valueReference" : { Reference }
    "valueSampledData" : { SampledData }
    "valueSignature" : { Signature }
    "valueTiming" : { Timing }
    "valueContactDetail" : { ContactDetail }
    "valueContributor" : { Contributor }
    "valueDataRequirement" : { DataRequirement }
    "valueExpression" : { Expression }
    "valueParameterDefinition" : { ParameterDefinition }
    "valueRelatedArtifact" : { RelatedArtifact }
    "valueTriggerDefinition" : { TriggerDefinition }
    "valueUsageContext" : { UsageContext }
    "valueDosage" : { Dosage }
    "valueMeta" : { Meta }
  }],
  // minValue[x]: Minimum Allowed Value (for some types). One of these 9:
  "minValueDate" : "<date>",
  "minValueDateTime" : "<dateTime>",
  "minValueInstant" : "<instant>",
  "minValueTime" : "<time>",
  "minValueDecimal" : <decimal>,
  "minValueInteger" : <integer>,
  "minValuePositiveInt" : "<positiveInt>",
  "minValueUnsignedInt" : "<unsignedInt>",
  "minValueQuantity" : { Quantity },
  // maxValue[x]: Maximum Allowed Value (for some types). One of these 9:
  "maxValueDate" : "<date>",
  "maxValueDateTime" : "<dateTime>",
  "maxValueInstant" : "<instant>",
  "maxValueTime" : "<time>",
  "maxValueDecimal" : <decimal>,
  "maxValueInteger" : <integer>,
  "maxValuePositiveInt" : "<positiveInt>",
  "maxValueUnsignedInt" : "<unsignedInt>",
  "maxValueQuantity" : { Quantity },
  "maxLength" : <integer>, // Max length for strings
  "condition" : ["<id>"], // Reference to invariant about presence
  "constraint" : [{ // Condition that must evaluate to true
    "key" : "<id>", // C? R!  Target of 'condition' reference above
    "requirements" : "<string>", // Why this constraint is necessary or appropriate
    "severity" : "<code>", // R!  error | warning
    "human" : "<string>", // R!  Human description of constraint
    "expression" : "<string>", // FHIRPath expression of constraint
    "xpath" : "<string>", // XPath expression of constraint
    "source" : { canonical(StructureDefinition) } // Reference to original source of constraint
  }],
  "mustSupport" : <boolean>, // If the element must be supported
  "isModifier" : <boolean>, // If this modifies the meaning of other elements
  "isModifierReason" : "<string>", // Reason that this element is marked as a modifier
  "isSummary" : <boolean>, // Include when _summary = true?
  "binding" : { // C? ValueSet details if this is coded
    "strength" : "<code>", // R!  required | extensible | preferred | example
    "description" : "<string>", // Human explanation of the value set
    "valueSet" : { canonical(ValueSet) } // C? Source of value set
  },
  "mapping" : [{ // Map element to another set of definitions
    "identity" : "<id>", // R!  Reference to mapping declaration
    "language" : "<code>", // Computable language of mapping
    "map" : "<string>", // R!  Details of the mapping
    "comment" : "<string>" // Comments about the mapping or its use
  }]
}
```

**Turtle Template**

```

@prefix fhir: <http://hl7.org/fhir/> .

[
 # from BackboneElement: Element.extension, BackboneElement.modifierextension
  fhir:ElementDefinition.path [ string ]; # 1..1 Path of the element in the hierarchy of elements
  fhir:ElementDefinition.representation [ code ], ... ; # 0..* xmlAttr | xmlText | typeAttr | cdaText | xhtml
  fhir:ElementDefinition.sliceName [ string ]; # 0..1 Name for this particular element (in a set of slices)
  fhir:ElementDefinition.sliceIsConstraining [ boolean ]; # 0..1 If this slice definition constrains an inherited slice definition (or not)
  fhir:ElementDefinition.label [ string ]; # 0..1 Name for element to display with or prompt for element
  fhir:ElementDefinition.code [ Coding ], ... ; # 0..* Corresponding codes in terminologies
  fhir:ElementDefinition.slicing [ # 0..1 This element is sliced - slices follow
    fhir:ElementDefinition.slicing.discriminator [ # 0..* Element values that are used to distinguish the slices
      fhir:ElementDefinition.slicing.discriminator.type [ code ]; # 1..1 value | exists | pattern | type | profile
      fhir:ElementDefinition.slicing.discriminator.path [ string ]; # 1..1 Path to element value
    ], ...;
    fhir:ElementDefinition.slicing.description [ string ]; # 0..1 Text description of how slicing works (or not)
    fhir:ElementDefinition.slicing.ordered [ boolean ]; # 0..1 If elements must be in same order as slices
    fhir:ElementDefinition.slicing.rules [ code ]; # 1..1 closed | open | openAtEnd
  ];
  fhir:ElementDefinition.short [ string ]; # 0..1 Concise definition for space-constrained presentation
  fhir:ElementDefinition.definition [ markdown ]; # 0..1 Full formal definition as narrative text
  fhir:ElementDefinition.comment [ markdown ]; # 0..1 Comments about the use of this element
  fhir:ElementDefinition.requirements [ markdown ]; # 0..1 Why this resource has been created
  fhir:ElementDefinition.alias [ string ], ... ; # 0..* Other names
  fhir:ElementDefinition.min [ unsignedInt ]; # 0..1 Minimum Cardinality
  fhir:ElementDefinition.max [ string ]; # 0..1 Maximum Cardinality (a number or *)
  fhir:ElementDefinition.base [ # 0..1 Base definition information for tools
    fhir:ElementDefinition.base.path [ string ]; # 1..1 Path that identifies the base element
    fhir:ElementDefinition.base.min [ unsignedInt ]; # 1..1 Min cardinality of the base element
    fhir:ElementDefinition.base.max [ string ]; # 1..1 Max cardinality of the base element
  ];
  fhir:ElementDefinition.contentReference [ uri ]; # 0..1 Reference to definition of content for the element
  fhir:ElementDefinition.type [ # 0..* Data type and Profile for this element
    fhir:ElementDefinition.type.code [ uri ]; # 1..1 Data type or Resource (reference to definition)
    fhir:ElementDefinition.type.profile [ canonical(StructureDefinition|ImplementationGuide) ], ... ; # 0..* Profiles (StructureDefinition or IG) - one must apply
    fhir:ElementDefinition.type.targetProfile [ canonical(StructureDefinition|ImplementationGuide) ], ... ; # 0..* Profile (StructureDefinition or IG) on the Reference/canonical target - one must apply
    fhir:ElementDefinition.type.aggregation [ code ], ... ; # 0..* contained | referenced | bundled - how aggregated
    fhir:ElementDefinition.type.versioning [ code ]; # 0..1 either | independent | specific
  ], ...;
  # ElementDefinition.defaultValue[x] : 0..1 Specified value if missing from instance. One of these 50
    fhir:ElementDefinition.defaultValueBase64Binary [ base64Binary ]
    fhir:ElementDefinition.defaultValueBoolean [ boolean ]
    fhir:ElementDefinition.defaultValueCanonical [ canonical ]
    fhir:ElementDefinition.defaultValueCode [ code ]
    fhir:ElementDefinition.defaultValueDate [ date ]
    fhir:ElementDefinition.defaultValueDateTime [ dateTime ]
    fhir:ElementDefinition.defaultValueDecimal [ decimal ]
    fhir:ElementDefinition.defaultValueId [ id ]
    fhir:ElementDefinition.defaultValueInstant [ instant ]
    fhir:ElementDefinition.defaultValueInteger [ integer ]
    fhir:ElementDefinition.defaultValueMarkdown [ markdown ]
    fhir:ElementDefinition.defaultValueOid [ oid ]
    fhir:ElementDefinition.defaultValuePositiveInt [ positiveInt ]
    fhir:ElementDefinition.defaultValueString [ string ]
    fhir:ElementDefinition.defaultValueTime [ time ]
    fhir:ElementDefinition.defaultValueUnsignedInt [ unsignedInt ]
    fhir:ElementDefinition.defaultValueUri [ uri ]
    fhir:ElementDefinition.defaultValueUrl [ url ]
    fhir:ElementDefinition.defaultValueUuid [ uuid ]
    fhir:ElementDefinition.defaultValueAddress [ Address ]
    fhir:ElementDefinition.defaultValueAge [ Age ]
    fhir:ElementDefinition.defaultValueAnnotation [ Annotation ]
    fhir:ElementDefinition.defaultValueAttachment [ Attachment ]
    fhir:ElementDefinition.defaultValueCodeableConcept [ CodeableConcept ]
    fhir:ElementDefinition.defaultValueCoding [ Coding ]
    fhir:ElementDefinition.defaultValueContactPoint [ ContactPoint ]
    fhir:ElementDefinition.defaultValueCount [ Count ]
    fhir:ElementDefinition.defaultValueDistance [ Distance ]
    fhir:ElementDefinition.defaultValueDuration [ Duration ]
    fhir:ElementDefinition.defaultValueHumanName [ HumanName ]
    fhir:ElementDefinition.defaultValueIdentifier [ Identifier ]
    fhir:ElementDefinition.defaultValueMoney [ Money ]
    fhir:ElementDefinition.defaultValuePeriod [ Period ]
    fhir:ElementDefinition.defaultValueQuantity [ Quantity ]
    fhir:ElementDefinition.defaultValueRange [ Range ]
    fhir:ElementDefinition.defaultValueRatio [ Ratio ]
    fhir:ElementDefinition.defaultValueReference [ Reference ]
    fhir:ElementDefinition.defaultValueSampledData [ SampledData ]
    fhir:ElementDefinition.defaultValueSignature [ Signature ]
    fhir:ElementDefinition.defaultValueTiming [ Timing ]
    fhir:ElementDefinition.defaultValueContactDetail [ ContactDetail ]
    fhir:ElementDefinition.defaultValueContributor [ Contributor ]
    fhir:ElementDefinition.defaultValueDataRequirement [ DataRequirement ]
    fhir:ElementDefinition.defaultValueExpression [ Expression ]
    fhir:ElementDefinition.defaultValueParameterDefinition [ ParameterDefinition ]
    fhir:ElementDefinition.defaultValueRelatedArtifact [ RelatedArtifact ]
    fhir:ElementDefinition.defaultValueTriggerDefinition [ TriggerDefinition ]
    fhir:ElementDefinition.defaultValueUsageContext [ UsageContext ]
    fhir:ElementDefinition.defaultValueDosage [ Dosage ]
    fhir:ElementDefinition.defaultValueMeta [ Meta ]
  fhir:ElementDefinition.meaningWhenMissing [ markdown ]; # 0..1 Implicit meaning when this element is missing
  fhir:ElementDefinition.orderMeaning [ string ]; # 0..1 What the order of the elements means
  # ElementDefinition.fixed[x] : 0..1 Value must be exactly this. One of these 50
    fhir:ElementDefinition.fixedBase64Binary [ base64Binary ]
    fhir:ElementDefinition.fixedBoolean [ boolean ]
    fhir:ElementDefinition.fixedCanonical [ canonical ]
    fhir:ElementDefinition.fixedCode [ code ]
    fhir:ElementDefinition.fixedDate [ date ]
    fhir:ElementDefinition.fixedDateTime [ dateTime ]
    fhir:ElementDefinition.fixedDecimal [ decimal ]
    fhir:ElementDefinition.fixedId [ id ]
    fhir:ElementDefinition.fixedInstant [ instant ]
    fhir:ElementDefinition.fixedInteger [ integer ]
    fhir:ElementDefinition.fixedMarkdown [ markdown ]
    fhir:ElementDefinition.fixedOid [ oid ]
    fhir:ElementDefinition.fixedPositiveInt [ positiveInt ]
    fhir:ElementDefinition.fixedString [ string ]
    fhir:ElementDefinition.fixedTime [ time ]
    fhir:ElementDefinition.fixedUnsignedInt [ unsignedInt ]
    fhir:ElementDefinition.fixedUri [ uri ]
    fhir:ElementDefinition.fixedUrl [ url ]
    fhir:ElementDefinition.fixedUuid [ uuid ]
    fhir:ElementDefinition.fixedAddress [ Address ]
    fhir:ElementDefinition.fixedAge [ Age ]
    fhir:ElementDefinition.fixedAnnotation [ Annotation ]
    fhir:ElementDefinition.fixedAttachment [ Attachment ]
    fhir:ElementDefinition.fixedCodeableConcept [ CodeableConcept ]
    fhir:ElementDefinition.fixedCoding [ Coding ]
    fhir:ElementDefinition.fixedContactPoint [ ContactPoint ]
    fhir:ElementDefinition.fixedCount [ Count ]
    fhir:ElementDefinition.fixedDistance [ Distance ]
    fhir:ElementDefinition.fixedDuration [ Duration ]
    fhir:ElementDefinition.fixedHumanName [ HumanName ]
    fhir:ElementDefinition.fixedIdentifier [ Identifier ]
    fhir:ElementDefinition.fixedMoney [ Money ]
    fhir:ElementDefinition.fixedPeriod [ Period ]
    fhir:ElementDefinition.fixedQuantity [ Quantity ]
    fhir:ElementDefinition.fixedRange [ Range ]
    fhir:ElementDefinition.fixedRatio [ Ratio ]
    fhir:ElementDefinition.fixedReference [ Reference ]
    fhir:ElementDefinition.fixedSampledData [ SampledData ]
    fhir:ElementDefinition.fixedSignature [ Signature ]
    fhir:ElementDefinition.fixedTiming [ Timing ]
    fhir:ElementDefinition.fixedContactDetail [ ContactDetail ]
    fhir:ElementDefinition.fixedContributor [ Contributor ]
    fhir:ElementDefinition.fixedDataRequirement [ DataRequirement ]
    fhir:ElementDefinition.fixedExpression [ Expression ]
    fhir:ElementDefinition.fixedParameterDefinition [ ParameterDefinition ]
    fhir:ElementDefinition.fixedRelatedArtifact [ RelatedArtifact ]
    fhir:ElementDefinition.fixedTriggerDefinition [ TriggerDefinition ]
    fhir:ElementDefinition.fixedUsageContext [ UsageContext ]
    fhir:ElementDefinition.fixedDosage [ Dosage ]
    fhir:ElementDefinition.fixedMeta [ Meta ]
  # ElementDefinition.pattern[x] : 0..1 Value must have at least these property values. One of these 50
    fhir:ElementDefinition.patternBase64Binary [ base64Binary ]
    fhir:ElementDefinition.patternBoolean [ boolean ]
    fhir:ElementDefinition.patternCanonical [ canonical ]
    fhir:ElementDefinition.patternCode [ code ]
    fhir:ElementDefinition.patternDate [ date ]
    fhir:ElementDefinition.patternDateTime [ dateTime ]
    fhir:ElementDefinition.patternDecimal [ decimal ]
    fhir:ElementDefinition.patternId [ id ]
    fhir:ElementDefinition.patternInstant [ instant ]
    fhir:ElementDefinition.patternInteger [ integer ]
    fhir:ElementDefinition.patternMarkdown [ markdown ]
    fhir:ElementDefinition.patternOid [ oid ]
    fhir:ElementDefinition.patternPositiveInt [ positiveInt ]
    fhir:ElementDefinition.patternString [ string ]
    fhir:ElementDefinition.patternTime [ time ]
    fhir:ElementDefinition.patternUnsignedInt [ unsignedInt ]
    fhir:ElementDefinition.patternUri [ uri ]
    fhir:ElementDefinition.patternUrl [ url ]
    fhir:ElementDefinition.patternUuid [ uuid ]
    fhir:ElementDefinition.patternAddress [ Address ]
    fhir:ElementDefinition.patternAge [ Age ]
    fhir:ElementDefinition.patternAnnotation [ Annotation ]
    fhir:ElementDefinition.patternAttachment [ Attachment ]
    fhir:ElementDefinition.patternCodeableConcept [ CodeableConcept ]
    fhir:ElementDefinition.patternCoding [ Coding ]
    fhir:ElementDefinition.patternContactPoint [ ContactPoint ]
    fhir:ElementDefinition.patternCount [ Count ]
    fhir:ElementDefinition.patternDistance [ Distance ]
    fhir:ElementDefinition.patternDuration [ Duration ]
    fhir:ElementDefinition.patternHumanName [ HumanName ]
    fhir:ElementDefinition.patternIdentifier [ Identifier ]
    fhir:ElementDefinition.patternMoney [ Money ]
    fhir:ElementDefinition.patternPeriod [ Period ]
    fhir:ElementDefinition.patternQuantity [ Quantity ]
    fhir:ElementDefinition.patternRange [ Range ]
    fhir:ElementDefinition.patternRatio [ Ratio ]
    fhir:ElementDefinition.patternReference [ Reference ]
    fhir:ElementDefinition.patternSampledData [ SampledData ]
    fhir:ElementDefinition.patternSignature [ Signature ]
    fhir:ElementDefinition.patternTiming [ Timing ]
    fhir:ElementDefinition.patternContactDetail [ ContactDetail ]
    fhir:ElementDefinition.patternContributor [ Contributor ]
    fhir:ElementDefinition.patternDataRequirement [ DataRequirement ]
    fhir:ElementDefinition.patternExpression [ Expression ]
    fhir:ElementDefinition.patternParameterDefinition [ ParameterDefinition ]
    fhir:ElementDefinition.patternRelatedArtifact [ RelatedArtifact ]
    fhir:ElementDefinition.patternTriggerDefinition [ TriggerDefinition ]
    fhir:ElementDefinition.patternUsageContext [ UsageContext ]
    fhir:ElementDefinition.patternDosage [ Dosage ]
    fhir:ElementDefinition.patternMeta [ Meta ]
  fhir:ElementDefinition.example [ # 0..* Example value (as defined for type)
    fhir:ElementDefinition.example.label [ string ]; # 1..1 Describes the purpose of this example
    # ElementDefinition.example.value[x] : 1..1 Value of Example (one of allowed types). One of these 50
      fhir:ElementDefinition.example.valueBase64Binary [ base64Binary ]
      fhir:ElementDefinition.example.valueBoolean [ boolean ]
      fhir:ElementDefinition.example.valueCanonical [ canonical ]
      fhir:ElementDefinition.example.valueCode [ code ]
      fhir:ElementDefinition.example.valueDate [ date ]
      fhir:ElementDefinition.example.valueDateTime [ dateTime ]
      fhir:ElementDefinition.example.valueDecimal [ decimal ]
      fhir:ElementDefinition.example.valueId [ id ]
      fhir:ElementDefinition.example.valueInstant [ instant ]
      fhir:ElementDefinition.example.valueInteger [ integer ]
      fhir:ElementDefinition.example.valueMarkdown [ markdown ]
      fhir:ElementDefinition.example.valueOid [ oid ]
      fhir:ElementDefinition.example.valuePositiveInt [ positiveInt ]
      fhir:ElementDefinition.example.valueString [ string ]
      fhir:ElementDefinition.example.valueTime [ time ]
      fhir:ElementDefinition.example.valueUnsignedInt [ unsignedInt ]
      fhir:ElementDefinition.example.valueUri [ uri ]
      fhir:ElementDefinition.example.valueUrl [ url ]
      fhir:ElementDefinition.example.valueUuid [ uuid ]
      fhir:ElementDefinition.example.valueAddress [ Address ]
      fhir:ElementDefinition.example.valueAge [ Age ]
      fhir:ElementDefinition.example.valueAnnotation [ Annotation ]
      fhir:ElementDefinition.example.valueAttachment [ Attachment ]
      fhir:ElementDefinition.example.valueCodeableConcept [ CodeableConcept ]
      fhir:ElementDefinition.example.valueCoding [ Coding ]
      fhir:ElementDefinition.example.valueContactPoint [ ContactPoint ]
      fhir:ElementDefinition.example.valueCount [ Count ]
      fhir:ElementDefinition.example.valueDistance [ Distance ]
      fhir:ElementDefinition.example.valueDuration [ Duration ]
      fhir:ElementDefinition.example.valueHumanName [ HumanName ]
      fhir:ElementDefinition.example.valueIdentifier [ Identifier ]
      fhir:ElementDefinition.example.valueMoney [ Money ]
      fhir:ElementDefinition.example.valuePeriod [ Period ]
      fhir:ElementDefinition.example.valueQuantity [ Quantity ]
      fhir:ElementDefinition.example.valueRange [ Range ]
      fhir:ElementDefinition.example.valueRatio [ Ratio ]
      fhir:ElementDefinition.example.valueReference [ Reference ]
      fhir:ElementDefinition.example.valueSampledData [ SampledData ]
      fhir:ElementDefinition.example.valueSignature [ Signature ]
      fhir:ElementDefinition.example.valueTiming [ Timing ]
      fhir:ElementDefinition.example.valueContactDetail [ ContactDetail ]
      fhir:ElementDefinition.example.valueContributor [ Contributor ]
      fhir:ElementDefinition.example.valueDataRequirement [ DataRequirement ]
      fhir:ElementDefinition.example.valueExpression [ Expression ]
      fhir:ElementDefinition.example.valueParameterDefinition [ ParameterDefinition ]
      fhir:ElementDefinition.example.valueRelatedArtifact [ RelatedArtifact ]
      fhir:ElementDefinition.example.valueTriggerDefinition [ TriggerDefinition ]
      fhir:ElementDefinition.example.valueUsageContext [ UsageContext ]
      fhir:ElementDefinition.example.valueDosage [ Dosage ]
      fhir:ElementDefinition.example.valueMeta [ Meta ]
  ], ...;
  # ElementDefinition.minValue[x] : 0..1 Minimum Allowed Value (for some types). One of these 9
    fhir:ElementDefinition.minValueDate [ date ]
    fhir:ElementDefinition.minValueDateTime [ dateTime ]
    fhir:ElementDefinition.minValueInstant [ instant ]
    fhir:ElementDefinition.minValueTime [ time ]
    fhir:ElementDefinition.minValueDecimal [ decimal ]
    fhir:ElementDefinition.minValueInteger [ integer ]
    fhir:ElementDefinition.minValuePositiveInt [ positiveInt ]
    fhir:ElementDefinition.minValueUnsignedInt [ unsignedInt ]
    fhir:ElementDefinition.minValueQuantity [ Quantity ]
  # ElementDefinition.maxValue[x] : 0..1 Maximum Allowed Value (for some types). One of these 9
    fhir:ElementDefinition.maxValueDate [ date ]
    fhir:ElementDefinition.maxValueDateTime [ dateTime ]
    fhir:ElementDefinition.maxValueInstant [ instant ]
    fhir:ElementDefinition.maxValueTime [ time ]
    fhir:ElementDefinition.maxValueDecimal [ decimal ]
    fhir:ElementDefinition.maxValueInteger [ integer ]
    fhir:ElementDefinition.maxValuePositiveInt [ positiveInt ]
    fhir:ElementDefinition.maxValueUnsignedInt [ unsignedInt ]
    fhir:ElementDefinition.maxValueQuantity [ Quantity ]
  fhir:ElementDefinition.maxLength [ integer ]; # 0..1 Max length for strings
  fhir:ElementDefinition.condition [ id ], ... ; # 0..* Reference to invariant about presence
  fhir:ElementDefinition.constraint [ # 0..* Condition that must evaluate to true
    fhir:ElementDefinition.constraint.key [ id ]; # 1..1 Target of 'condition' reference above
    fhir:ElementDefinition.constraint.requirements [ string ]; # 0..1 Why this constraint is necessary or appropriate
    fhir:ElementDefinition.constraint.severity [ code ]; # 1..1 error | warning
    fhir:ElementDefinition.constraint.human [ string ]; # 1..1 Human description of constraint
    fhir:ElementDefinition.constraint.expression [ string ]; # 0..1 FHIRPath expression of constraint
    fhir:ElementDefinition.constraint.xpath [ string ]; # 0..1 XPath expression of constraint
    fhir:ElementDefinition.constraint.source [ canonical(StructureDefinition) ]; # 0..1 Reference to original source of constraint
  ], ...;
  fhir:ElementDefinition.mustSupport [ boolean ]; # 0..1 If the element must be supported
  fhir:ElementDefinition.isModifier [ boolean ]; # 0..1 If this modifies the meaning of other elements
  fhir:ElementDefinition.isModifierReason [ string ]; # 0..1 Reason that this element is marked as a modifier
  fhir:ElementDefinition.isSummary [ boolean ]; # 0..1 Include when _summary = true?
  fhir:ElementDefinition.binding [ # 0..1 ValueSet details if this is coded
    fhir:ElementDefinition.binding.strength [ code ]; # 1..1 required | extensible | preferred | example
    fhir:ElementDefinition.binding.description [ string ]; # 0..1 Human explanation of the value set
    fhir:ElementDefinition.binding.valueSet [ canonical(ValueSet) ]; # 0..1 Source of value set
  ];
  fhir:ElementDefinition.mapping [ # 0..* Map element to another set of definitions
    fhir:ElementDefinition.mapping.identity [ id ]; # 1..1 Reference to mapping declaration
    fhir:ElementDefinition.mapping.language [ code ]; # 0..1 Computable language of mapping
    fhir:ElementDefinition.mapping.map [ string ]; # 1..1 Details of the mapping
    fhir:ElementDefinition.mapping.comment [ string ]; # 0..1 Comments about the mapping or its use
  ], ...;
]
```

**Changes since Release 3**

|  |  |
| --- | --- |
| [ElementDefinition](elementdefinition.html#ElementDefinition) |  |
| ElementDefinition.representation | - Change value set from http://hl7.org/fhir/ValueSet/property-representation to http://hl7.org/fhir/ValueSet/property-representation|4.0.1 |
| ElementDefinition.sliceIsConstraining | - Added Element |
| ElementDefinition.slicing.discriminator.type | - Change value set from http://hl7.org/fhir/ValueSet/discriminator-type to http://hl7.org/fhir/ValueSet/discriminator-type|4.0.1 |
| ElementDefinition.slicing.ordered | - Default Value "false" removed |
| ElementDefinition.slicing.rules | - Change value set from http://hl7.org/fhir/ValueSet/resource-slicing-rules to http://hl7.org/fhir/ValueSet/resource-slicing-rules|4.0.1 |
| ElementDefinition.type.profile | - Max Cardinality changed from 1 to \* - Type changed from uri to canonical(StructureDefinition | ImplementationGuide) |
| ElementDefinition.type.targetProfile | - Max Cardinality changed from 1 to \* - Type changed from uri to canonical(StructureDefinition | ImplementationGuide) |
| ElementDefinition.type.aggregation | - Change value set from http://hl7.org/fhir/ValueSet/resource-aggregation-mode to http://hl7.org/fhir/ValueSet/resource-aggregation-mode|4.0.1 |
| ElementDefinition.type.versioning | - Change value set from http://hl7.org/fhir/ValueSet/reference-version-rules to http://hl7.org/fhir/ValueSet/reference-version-rules|4.0.1 - Default Value "either" removed |
| ElementDefinition.defaultValue[x] | - Add Types canonical, url, uuid, ContactDetail, Contributor, DataRequirement, Expression, ParameterDefinition, RelatedArtifact, TriggerDefinition, UsageContext, Dosage |
| ElementDefinition.fixed[x] | - Add Types canonical, url, uuid, ContactDetail, Contributor, DataRequirement, Expression, ParameterDefinition, RelatedArtifact, TriggerDefinition, UsageContext, Dosage |
| ElementDefinition.pattern[x] | - Add Types canonical, url, uuid, ContactDetail, Contributor, DataRequirement, Expression, ParameterDefinition, RelatedArtifact, TriggerDefinition, UsageContext, Dosage |
| ElementDefinition.example.value[x] | - Add Types canonical, url, uuid, ContactDetail, Contributor, DataRequirement, Expression, ParameterDefinition, RelatedArtifact, TriggerDefinition, UsageContext, Dosage |
| ElementDefinition.constraint.severity | - Change value set from http://hl7.org/fhir/ValueSet/constraint-severity to http://hl7.org/fhir/ValueSet/constraint-severity|4.0.1 |
| ElementDefinition.constraint.expression | - Min Cardinality changed from 1 to 0 |
| ElementDefinition.constraint.source | - Type changed from uri to canonical(StructureDefinition) |
| ElementDefinition.mustSupport | - Default Value "false" removed |
| ElementDefinition.isModifier | - Default Value "false" removed |
| ElementDefinition.isModifierReason | - Added Element |
| ElementDefinition.isSummary | - Default Value "false" removed |
| ElementDefinition.binding.strength | - Change value set from http://hl7.org/fhir/ValueSet/binding-strength to http://hl7.org/fhir/ValueSet/binding-strength|4.0.1 |
| ElementDefinition.binding.valueSet | - Renamed from valueSet[x] to valueSet - Add Type canonical(ValueSet) - Remove Types uri, Reference(ValueSet) |
| ElementDefinition.mapping.language | - Change value set from http://hl7.org/fhir/ValueSet/mimetypes to http://hl7.org/fhir/ValueSet/mimetypes|4.0.1 |

See the [Full Difference](diff.html) for further information

**Structure**

| [Name](formats.html#table "The logical name of the element") | [Flags](formats.html#table "Information about the use of the element") | [Card.](formats.html#table "Minimum and Maximum # of times the the element can appear in the instance") | [Type](formats.html#table "Reference to the type of the element") | [Description & Constraints](formats.html#table "Additional information about the element")[doco](formats.html#table "Legend for this format") |
| --- | --- | --- | --- | --- |
| .. [ElementDefinition](elementdefinition-definitions.html#ElementDefinition "ElementDefinition : Captures constraints on each element within the resource, profile, or extension.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants")[N](versions.html#std-process "Standards Status = Normative") |  | [BackBoneElement](backboneelement.html) | Definition of an element in a resource or extension + Rule: Min <= Max + Rule: if the element definition has a contentReference, it cannot have type, defaultValue, fixed, pattern, example, minValue, maxValue, maxLength, or binding + Rule: Fixed value may only be specified if there is one type + Rule: Pattern may only be specified if there is one type + Rule: Pattern and fixed are mutually exclusive + Rule: Binding can only be present for coded elements, string, and uri + Rule: Types must be unique by code + Rule: Constraints must be unique by key + Rule: default value and meaningWhenMissing are mutually exclusive + Rule: sliceName must be composed of proper tokens separated by "/" + Rule: Must have a modifier reason if isModifier = true + Rule: Element names cannot include some special characters + Warning: Element names should be simple alphanumerics with a max of 64 characters, or code generation tools may be broken + Rule: sliceIsConstraining can only appear if slicename is present Elements defined in Ancestors: [id](element.html#Element "Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces."), [extension](element.html#Element "May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension."), [modifierExtension](backboneelement.html#BackboneElement "May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.  Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself).") |
| ... [path](elementdefinition-definitions.html#ElementDefinition.path "ElementDefinition.path : The path identifies the element and is expressed as a \".\"-separated list of ancestor elements, beginning with the name of the resource or extension.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [string](datatypes.html#string) | Path of the element in the hierarchy of elements |
| ... [representation](elementdefinition-definitions.html#ElementDefinition.representation "ElementDefinition.representation : Codes that define how this element is represented in instances, when the deviation varies from the normal case.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [code](datatypes.html#code) | xmlAttr | xmlText | typeAttr | cdaText | xhtml [PropertyRepresentation](valueset-property-representation.html "How a property is represented when serialized.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ... [sliceName](elementdefinition-definitions.html#ElementDefinition.sliceName "ElementDefinition.sliceName : The name of this element definition slice, when slicing is working. The name must be a token with no dots or spaces. This is a unique name referring to a specific set of constraints applied to this element, used to provide a name to different slices of the same element.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | Name for this particular element (in a set of slices) |
| ... [sliceIsConstraining](elementdefinition-definitions.html#ElementDefinition.sliceIsConstraining "ElementDefinition.sliceIsConstraining : If true, indicates that this slice definition is constraining a slice definition with the same name in an inherited profile. If false, the slice is not overriding any slice in an inherited profile. If missing, the slice might or might not be overriding a slice in an inherited profile, depending on the sliceName.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[TU](versions.html#std-process "Standards Status = Trial Use") | 0..1 | [boolean](datatypes.html#boolean) | If this slice definition constrains an inherited slice definition (or not) |
| ... [label](elementdefinition-definitions.html#ElementDefinition.label "ElementDefinition.label : A single preferred label which is the text to display beside the element indicating its meaning or to use to prompt for the element in a user display or form.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | Name for element to display with or prompt for element |
| ... [code](elementdefinition-definitions.html#ElementDefinition.code "ElementDefinition.code : A code that has the same meaning as the element in a particular terminology.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [Coding](datatypes.html#Coding) | Corresponding codes in terminologies [LOINC Codes](valueset-observation-codes.html "Codes that indicate the meaning of a data element.") ([Example](terminologies.html#example "Instances are not expected or even encouraged to draw from the specified value set.  The value set merely provides examples of the types of concepts intended to be included.")) |
| ... [slicing](elementdefinition-definitions.html#ElementDefinition.slicing "ElementDefinition.slicing : Indicates that the element is sliced into a set of alternative definitions (i.e. in a structure definition, there are multiple different constraints on a single element in the base resource). Slicing can be used in any resource that has cardinality ..* on the base resource, or any resource with a choice of types. The set of slices is any elements that come after this in the element sequence that have the same path, until a shorter path occurs (the shorter path terminates the set).") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..1 | [Element](element.html) | This element is sliced - slices follow + Rule: If there are no discriminators, there must be a definition |
| .... [discriminator](elementdefinition-definitions.html#ElementDefinition.slicing.discriminator "ElementDefinition.slicing.discriminator : Designates which child elements are used to discriminate between the slices when processing an instance. If one or more discriminators are provided, the value of the child elements in the instance data SHALL completely distinguish which slice the element in the resource matches based on the allowed values for those elements in each of the slices.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [Element](element.html) | Element values that are used to distinguish the slices |
| ..... [type](elementdefinition-definitions.html#ElementDefinition.slicing.discriminator.type "ElementDefinition.slicing.discriminator.type : How the element value is interpreted when discrimination is evaluated.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [code](datatypes.html#code) | value | exists | pattern | type | profile [DiscriminatorType](valueset-discriminator-type.html "How an element value is interpreted when discrimination is evaluated.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ..... [path](elementdefinition-definitions.html#ElementDefinition.slicing.discriminator.path "ElementDefinition.slicing.discriminator.path : A FHIRPath expression, using [the simple subset of FHIRPath](fhirpath.html#simple), that is used to identify the element on which discrimination is based.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [string](datatypes.html#string) | Path to element value |
| .... [description](elementdefinition-definitions.html#ElementDefinition.slicing.description "ElementDefinition.slicing.description : A human-readable text description of how the slicing works. If there is no discriminator, this is required to be present to provide whatever information is possible about how the slices can be differentiated.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..1 | [string](datatypes.html#string) | Text description of how slicing works (or not) |
| .... [ordered](elementdefinition-definitions.html#ElementDefinition.slicing.ordered "ElementDefinition.slicing.ordered : If the matching elements have to occur in the same order as defined in the profile.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [boolean](datatypes.html#boolean) | If elements must be in same order as slices |
| .... [rules](elementdefinition-definitions.html#ElementDefinition.slicing.rules "ElementDefinition.slicing.rules : Whether additional slices are allowed or not. When the slices are ordered, profile authors can also say that additional slices are only allowed at the end.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [code](datatypes.html#code) | closed | open | openAtEnd [SlicingRules](valueset-resource-slicing-rules.html "How slices are interpreted when evaluating an instance.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ... [short](elementdefinition-definitions.html#ElementDefinition.short "ElementDefinition.short : A concise description of what this element means (e.g. for use in autogenerated summaries).") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | Concise definition for space-constrained presentation |
| ... [definition](elementdefinition-definitions.html#ElementDefinition.definition "ElementDefinition.definition : Provides a complete explanation of the meaning of the data element for human readability.  For the case of elements derived from existing elements (e.g. constraints), the definition SHALL be consistent with the base definition, but convey the meaning of the element in the particular context of use of the resource. (Note: The text you are reading is specified in ElementDefinition.definition).") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [markdown](datatypes.html#markdown) | Full formal definition as narrative text |
| ... [comment](elementdefinition-definitions.html#ElementDefinition.comment "ElementDefinition.comment : Explanatory notes and implementation guidance about the data element, including notes about how to use the data properly, exceptions to proper use, etc. (Note: The text you are reading is specified in ElementDefinition.comment).") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [markdown](datatypes.html#markdown) | Comments about the use of this element |
| ... [requirements](elementdefinition-definitions.html#ElementDefinition.requirements "ElementDefinition.requirements : This element is for traceability of why the element was created and why the constraints exist as they do. This may be used to point to source materials or specifications that drove the structure of this element.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [markdown](datatypes.html#markdown) | Why this resource has been created |
| ... [alias](elementdefinition-definitions.html#ElementDefinition.alias "ElementDefinition.alias : Identifies additional names by which this element might also be known.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [string](datatypes.html#string) | Other names |
| ... [min](elementdefinition-definitions.html#ElementDefinition.min "ElementDefinition.min : The minimum number of times this element SHALL appear in the instance.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..1 | [unsignedInt](datatypes.html#unsignedInt) | Minimum Cardinality |
| ... [max](elementdefinition-definitions.html#ElementDefinition.max "ElementDefinition.max : The maximum number of times this element is permitted to appear in the instance.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..1 | [string](datatypes.html#string) | Maximum Cardinality (a number or \*) + Rule: Max SHALL be a number or "\*" |
| ... [base](elementdefinition-definitions.html#ElementDefinition.base "ElementDefinition.base : Information about the base definition of the element, provided to make it unnecessary for tools to trace the deviation of the element through the derived and related profiles. When the element definition is not the original definition of an element - i.g. either in a constraint on another type, or for elements from a super type in a snap shot - then the information in provided in the element definition may be different to the base definition. On the original definition of the element, it will be same.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [Element](element.html) | Base definition information for tools |
| .... [path](elementdefinition-definitions.html#ElementDefinition.base.path "ElementDefinition.base.path : The Path that identifies the base element - this matches the ElementDefinition.path for that element. Across FHIR, there is only one base definition of any element - that is, an element definition on a [[[StructureDefinition]]] without a StructureDefinition.base.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [string](datatypes.html#string) | Path that identifies the base element |
| .... [min](elementdefinition-definitions.html#ElementDefinition.base.min "ElementDefinition.base.min : Minimum cardinality of the base element identified by the path.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [unsignedInt](datatypes.html#unsignedInt) | Min cardinality of the base element |
| .... [max](elementdefinition-definitions.html#ElementDefinition.base.max "ElementDefinition.base.max : Maximum cardinality of the base element identified by the path.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [string](datatypes.html#string) | Max cardinality of the base element |
| ... [contentReference](elementdefinition-definitions.html#ElementDefinition.contentReference "ElementDefinition.contentReference : Identifies an element defined elsewhere in the definition whose content rules should be applied to the current element. ContentReferences bring across all the rules that are in the ElementDefinition for the element, including definitions, cardinality constraints, bindings, invariants etc.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..1 | [uri](datatypes.html#uri) | Reference to definition of content for the element |
| ... [type](elementdefinition-definitions.html#ElementDefinition.type "ElementDefinition.type : The data type or resource that the value of this element is permitted to be.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..\* | [Element](element.html) | Data type and Profile for this element + Rule: Aggregation may only be specified if one of the allowed types for the element is a reference + Rule: targetProfile is only allowed if the type is Reference or canonical |
| .... [code](elementdefinition-definitions.html#ElementDefinition.type.code "ElementDefinition.type.code : URL of Data type or Resource that is a(or the) type used for this element. References are URLs that are relative to http://hl7.org/fhir/StructureDefinition e.g. \"string\" is a reference to http://hl7.org/fhir/StructureDefinition/string. Absolute URLs are only allowed in logical models.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [uri](datatypes.html#uri) | Data type or Resource (reference to definition) [FHIRDefinedType](valueset-defined-types.html "Either a resource or a data type, including logical model types.") ([Extensible](terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept (based on human review), alternate codings (or, data type allowing, text) may be included instead.")) |
| .... [profile](elementdefinition-definitions.html#ElementDefinition.type.profile "ElementDefinition.type.profile : Identifies a profile structure or implementation Guide that applies to the datatype this element refers to. If any profiles are specified, then the content must conform to at least one of them. The URL can be a local reference - to a contained StructureDefinition, or a reference to another StructureDefinition or Implementation Guide by a canonical URL. When an implementation guide is specified, the type SHALL conform to at least one profile defined in the implementation guide.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [canonical](datatypes.html#canonical)([StructureDefinition](structuredefinition.html) | [ImplementationGuide](implementationguide.html)) | Profiles (StructureDefinition or IG) - one must apply |
| .... [targetProfile](elementdefinition-definitions.html#ElementDefinition.type.targetProfile "ElementDefinition.type.targetProfile : Used when the type is \"Reference\" or \"canonical\", and identifies a profile structure or implementation Guide that applies to the target of the reference this element refers to. If any profiles are specified, then the content must conform to at least one of them. The URL can be a local reference - to a contained StructureDefinition, or a reference to another StructureDefinition or Implementation Guide by a canonical URL. When an implementation guide is specified, the target resource SHALL conform to at least one profile defined in the implementation guide.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [canonical](datatypes.html#canonical)([StructureDefinition](structuredefinition.html) | [ImplementationGuide](implementationguide.html)) | Profile (StructureDefinition or IG) on the Reference/canonical target - one must apply |
| .... [aggregation](elementdefinition-definitions.html#ElementDefinition.type.aggregation "ElementDefinition.type.aggregation : If the type is a reference to another resource, how the resource is or can be aggregated - is it a contained resource, or a reference, and if the context is a bundle, is it included in the bundle.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..\* | [code](datatypes.html#code) | contained | referenced | bundled - how aggregated [AggregationMode](valueset-resource-aggregation-mode.html "How resource references can be aggregated.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| .... [versioning](elementdefinition-definitions.html#ElementDefinition.type.versioning "ElementDefinition.type.versioning : Whether this reference needs to be version specific or version independent, or whether either can be used.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [code](datatypes.html#code) | either | independent | specific [ReferenceVersionRules](valueset-reference-version-rules.html "Whether a reference needs to be version specific or version independent, or whether either can be used.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| ... [defaultValue[x]](elementdefinition-definitions.html#ElementDefinition.defaultValue_x_ "ElementDefinition.defaultValue[x] : The value that should be used if there is no value stated in the instance (e.g. 'if not otherwise specified, the abstract is false').") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..1 | [\*](datatypes.html#open) | Specified value if missing from instance |
| ... [meaningWhenMissing](elementdefinition-definitions.html#ElementDefinition.meaningWhenMissing "ElementDefinition.meaningWhenMissing : The Implicit meaning that is to be understood when this element is missing (e.g. 'when this element is missing, the period is ongoing').") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..1 | [markdown](datatypes.html#markdown) | Implicit meaning when this element is missing |
| ... [orderMeaning](elementdefinition-definitions.html#ElementDefinition.orderMeaning "ElementDefinition.orderMeaning : If present, indicates that the order of the repeating element has meaning and describes what that meaning is.  If absent, it means that the order of the element has no meaning.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | What the order of the elements means |
| ... [fixed[x]](elementdefinition-definitions.html#ElementDefinition.fixed_x_ "ElementDefinition.fixed[x] : Specifies a value that SHALL be exactly the value  for this element in the instance. For purposes of comparison, non-significant whitespace is ignored, and all values must be an exact match (case and accent sensitive). Missing elements/attributes must also be missing.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..1 | [\*](datatypes.html#open) | Value must be exactly this |
| ... [pattern[x]](elementdefinition-definitions.html#ElementDefinition.pattern_x_ "ElementDefinition.pattern[x] : Specifies a value that the value in the instance SHALL follow - that is, any value in the pattern must be found in the instance. Other additional values may be found too. This is effectively constraint by example.    When pattern[x] is used to constrain a primitive, it means that the value provided in the pattern[x] must match the instance value exactly.  When pattern[x] is used to constrain an array, it means that each element provided in the pattern[x] array must (recursively) match at least one element from the instance array.  When pattern[x] is used to constrain a complex object, it means that each property in the pattern must be present in the complex object, and its value must recursively match -- i.e.,  1. If primitive: it must match exactly the pattern value 2. If a complex object: it must match (recursively) the pattern value 3. If an array: it must match (recursively) the pattern value.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..1 | [\*](datatypes.html#open) | Value must have at least these property values |
| ... [example](elementdefinition-definitions.html#ElementDefinition.example "ElementDefinition.example : A sample value for this element demonstrating the type of information that would typically be found in the element.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [Element](element.html) | Example value (as defined for type) |
| .... [label](elementdefinition-definitions.html#ElementDefinition.example.label "ElementDefinition.example.label : Describes the purpose of this example amoung the set of examples.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [string](datatypes.html#string) | Describes the purpose of this example |
| .... [value[x]](elementdefinition-definitions.html#ElementDefinition.example.value_x_ "ElementDefinition.example.value[x] : The actual value for the element, which must be one of the types allowed for this element.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [\*](datatypes.html#open) | Value of Example (one of allowed types) |
| ... [minValue[x]](elementdefinition-definitions.html#ElementDefinition.minValue_x_ "ElementDefinition.minValue[x] : The minimum allowed value for the element. The value is inclusive. This is allowed for the types date, dateTime, instant, time, decimal, integer, and Quantity.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 |  | Minimum Allowed Value (for some types) |
| .... minValueDate |  |  | [date](datatypes.html#date) |  |
| .... minValueDateTime |  |  | [dateTime](datatypes.html#dateTime) |  |
| .... minValueInstant |  |  | [instant](datatypes.html#instant) |  |
| .... minValueTime |  |  | [time](datatypes.html#time) |  |
| .... minValueDecimal |  |  | [decimal](datatypes.html#decimal) |  |
| .... minValueInteger |  |  | [integer](datatypes.html#integer) |  |
| .... minValuePositiveInt |  |  | [positiveInt](datatypes.html#positiveInt) |  |
| .... minValueUnsignedInt |  |  | [unsignedInt](datatypes.html#unsignedInt) |  |
| .... minValueQuantity |  |  | [Quantity](datatypes.html#Quantity) |  |
| ... [maxValue[x]](elementdefinition-definitions.html#ElementDefinition.maxValue_x_ "ElementDefinition.maxValue[x] : The maximum allowed value for the element. The value is inclusive. This is allowed for the types date, dateTime, instant, time, decimal, integer, and Quantity.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 |  | Maximum Allowed Value (for some types) |
| .... maxValueDate |  |  | [date](datatypes.html#date) |  |
| .... maxValueDateTime |  |  | [dateTime](datatypes.html#dateTime) |  |
| .... maxValueInstant |  |  | [instant](datatypes.html#instant) |  |
| .... maxValueTime |  |  | [time](datatypes.html#time) |  |
| .... maxValueDecimal |  |  | [decimal](datatypes.html#decimal) |  |
| .... maxValueInteger |  |  | [integer](datatypes.html#integer) |  |
| .... maxValuePositiveInt |  |  | [positiveInt](datatypes.html#positiveInt) |  |
| .... maxValueUnsignedInt |  |  | [unsignedInt](datatypes.html#unsignedInt) |  |
| .... maxValueQuantity |  |  | [Quantity](datatypes.html#Quantity) |  |
| ... [maxLength](elementdefinition-definitions.html#ElementDefinition.maxLength "ElementDefinition.maxLength : Indicates the maximum length in characters that is permitted to be present in conformant instances and which is expected to be supported by conformant consumers that support the element.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [integer](datatypes.html#integer) | Max length for strings |
| ... [condition](elementdefinition-definitions.html#ElementDefinition.condition "ElementDefinition.condition : A reference to an invariant that may make additional statements about the cardinality or value in the instance.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [id](datatypes.html#id) | Reference to invariant about presence |
| ... [constraint](elementdefinition-definitions.html#ElementDefinition.constraint "ElementDefinition.constraint : Formal constraints such as co-occurrence and other constraints that can be computationally evaluated within the context of the instance.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..\* | [Element](element.html) | Condition that must evaluate to true + Warning: Constraints should have an expression or else validators will not be able to enforce them |
| .... [key](elementdefinition-definitions.html#ElementDefinition.constraint.key "ElementDefinition.constraint.key : Allows identification of which elements have their cardinalities impacted by the constraint.  Will not be referenced for constraints that do not affect cardinality.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 1..1 | [id](datatypes.html#id) | Target of 'condition' reference above |
| .... [requirements](elementdefinition-definitions.html#ElementDefinition.constraint.requirements "ElementDefinition.constraint.requirements : Description of why this constraint is necessary or appropriate.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | Why this constraint is necessary or appropriate |
| .... [severity](elementdefinition-definitions.html#ElementDefinition.constraint.severity "ElementDefinition.constraint.severity : Identifies the impact constraint violation has on the conformance of the instance.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [code](datatypes.html#code) | error | warning [ConstraintSeverity](valueset-constraint-severity.html "SHALL applications comply with this constraint?") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| .... [human](elementdefinition-definitions.html#ElementDefinition.constraint.human "ElementDefinition.constraint.human : Text that can be used to describe the constraint in messages identifying that the constraint has been violated.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [string](datatypes.html#string) | Human description of constraint |
| .... [expression](elementdefinition-definitions.html#ElementDefinition.constraint.expression "ElementDefinition.constraint.expression : A [FHIRPath](fhirpath.html) expression of constraint that can be executed to see if this constraint is met.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | FHIRPath expression of constraint |
| .... [xpath](elementdefinition-definitions.html#ElementDefinition.constraint.xpath "ElementDefinition.constraint.xpath : An XPath expression of constraint that can be executed to see if this constraint is met.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[TU](versions.html#std-process "Standards Status = Trial Use") | 0..1 | [string](datatypes.html#string) | XPath expression of constraint |
| .... [source](elementdefinition-definitions.html#ElementDefinition.constraint.source "ElementDefinition.constraint.source : A reference to the original source of the constraint, for traceability purposes.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [canonical](datatypes.html#canonical)([StructureDefinition](structuredefinition.html)) | Reference to original source of constraint |
| ... [mustSupport](elementdefinition-definitions.html#ElementDefinition.mustSupport "ElementDefinition.mustSupport : If true, implementations that produce or consume resources SHALL provide \"support\" for the element in some meaningful way.  If false, the element may be ignored and not supported. If false, whether to populate or use the data element in any way is at the discretion of the implementation.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [boolean](datatypes.html#boolean) | If the element must be supported |
| ... [isModifier](elementdefinition-definitions.html#ElementDefinition.isModifier "ElementDefinition.isModifier : If true, the value of this element affects the interpretation of the element or resource that contains it, and the value of the element cannot be ignored. Typically, this is used for status, negation and qualification codes. The effect of this is that the element cannot be ignored by systems: they SHALL either recognize the element and process it, and/or a pre-determination has been made that it is not relevant to their particular system.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [boolean](datatypes.html#boolean) | If this modifies the meaning of other elements |
| ... [isModifierReason](elementdefinition-definitions.html#ElementDefinition.isModifierReason "ElementDefinition.isModifierReason : Explains how that element affects the interpretation of the resource or element that contains it.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | Reason that this element is marked as a modifier |
| ... [isSummary](elementdefinition-definitions.html#ElementDefinition.isSummary "ElementDefinition.isSummary : Whether the element should be included if a client requests a search with the parameter _summary=true.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [boolean](datatypes.html#boolean) | Include when \_summary = true? |
| ... [binding](elementdefinition-definitions.html#ElementDefinition.binding "ElementDefinition.binding : Binds to a value set if this element is coded (code, Coding, CodeableConcept, Quantity), or the data types (string, uri).") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..1 | [Element](element.html) | ValueSet details if this is coded + Rule: ValueSet SHALL start with http:// or https:// or urn: |
| .... [strength](elementdefinition-definitions.html#ElementDefinition.binding.strength "ElementDefinition.binding.strength : Indicates the degree of conformance expectations associated with this binding - that is, the degree to which the provided value set must be adhered to in the instances.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [code](datatypes.html#code) | required | extensible | preferred | example [BindingStrength](valueset-binding-strength.html "Indication of the degree of conformance expectations associated with a binding.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| .... [description](elementdefinition-definitions.html#ElementDefinition.binding.description "ElementDefinition.binding.description : Describes the intended use of this particular set of codes.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | Human explanation of the value set |
| .... [valueSet](elementdefinition-definitions.html#ElementDefinition.binding.valueSet "ElementDefinition.binding.valueSet : Refers to the value set that identifies the set of codes the binding refers to.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..1 | [canonical](datatypes.html#canonical)([ValueSet](valueset.html)) | Source of value set |
| ... [mapping](elementdefinition-definitions.html#ElementDefinition.mapping "ElementDefinition.mapping : Identifies a concept from an external specification that roughly corresponds to this element.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..\* | [Element](element.html) | Map element to another set of definitions |
| .... [identity](elementdefinition-definitions.html#ElementDefinition.mapping.identity "ElementDefinition.mapping.identity : An internal reference to the definition of a mapping.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [id](datatypes.html#id) | Reference to mapping declaration |
| .... [language](elementdefinition-definitions.html#ElementDefinition.mapping.language "ElementDefinition.mapping.language : Identifies the computable language in which mapping.map is expressed.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [code](datatypes.html#code) | Computable language of mapping [MimeType](valueset-mimetypes.html "The mime type of an attachment. Any valid mime type is allowed.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set.")) |
| .... [map](elementdefinition-definitions.html#ElementDefinition.mapping.map "ElementDefinition.mapping.map : Expresses what part of the target specification corresponds to this element.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [string](datatypes.html#string) | Details of the mapping |
| .... [comment](elementdefinition-definitions.html#ElementDefinition.mapping.comment "ElementDefinition.mapping.comment : Comments that provide information about the mapping or its use.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | Comments about the mapping or its use |
| [doco Documentation for this format](formats.html#table "Legend for this format") | | | | |

**UML Diagram** ([Legend](formats.html#uml))

**XML Template**

```

<ElementDefinition xmlns="http://hl7.org/fhir">
 <!-- from BackboneElement: extension, modifierExtension -->
 <path value="[string]"/><!-- 1..1 Path of the element in the hierarchy of elements -->
 <representation value="[code]"/><!-- 0..* xmlAttr | xmlText | typeAttr | cdaText | xhtml -->
 <sliceName value="[string]"/><!-- 0..1 Name for this particular element (in a set of slices) -->
 <sliceIsConstraining value="[boolean]"/><!-- 0..1 If this slice definition constrains an inherited slice definition (or not) -->
 <label value="[string]"/><!-- 0..1 Name for element to display with or prompt for element -->
 <code><!-- 0..* Coding Corresponding codes in terminologies --></code>
 <slicing>  <!-- 0..1 This element is sliced - slices follow -->
  <discriminator>  <!-- 0..* Element values that are used to distinguish the slices -->
   <type value="[code]"/><!-- 1..1 value | exists | pattern | type | profile -->
   <path value="[string]"/><!-- 1..1 Path to element value -->
  </discriminator>
  <description value="[string]"/><!-- ![??](lock.png) 0..1 Text description of how slicing works (or not) -->
  <ordered value="[boolean]"/><!-- 0..1 If elements must be in same order as slices -->
  <rules value="[code]"/><!-- 1..1 closed | open | openAtEnd -->
 </slicing>
 <short value="[string]"/><!-- 0..1 Concise definition for space-constrained presentation -->
 <definition value="[markdown]"/><!-- 0..1 Full formal definition as narrative text -->
 <comment value="[markdown]"/><!-- 0..1 Comments about the use of this element -->
 <requirements value="[markdown]"/><!-- 0..1 Why this resource has been created -->
 <alias value="[string]"/><!-- 0..* Other names -->
 <min value="[unsignedInt]"/><!-- ![??](lock.png) 0..1 Minimum Cardinality -->
 <max value="[string]"/><!-- ![??](lock.png) 0..1 Maximum Cardinality (a number or *) -->
 <base>  <!-- 0..1 Base definition information for tools -->
  <path value="[string]"/><!-- 1..1 Path that identifies the base element -->
  <min value="[unsignedInt]"/><!-- 1..1 Min cardinality of the base element -->
  <max value="[string]"/><!-- 1..1 Max cardinality of the base element -->
 </base>
 <contentReference value="[uri]"/><!-- ![??](lock.png) 0..1 Reference to definition of content for the element -->
 <type>  <!-- ![??](lock.png) 0..* Data type and Profile for this element -->
  <code value="[uri]"/><!-- 1..1 Data type or Resource (reference to definition) -->
  <profile><!-- 0..* canonical(StructureDefinition|ImplementationGuide) Profiles (StructureDefinition or IG) - one must apply --></profile>
  <targetProfile><!-- 0..* canonical(StructureDefinition|ImplementationGuide) Profile (StructureDefinition or IG) on the Reference/canonical target - one must apply --></targetProfile>
  <aggregation value="[code]"/><!-- ![??](lock.png) 0..* contained | referenced | bundled - how aggregated -->
  <versioning value="[code]"/><!-- 0..1 either | independent | specific -->
 </type>
 <defaultValue[x]><!-- ![??](lock.png) 0..1 * Specified value if missing from instance --></defaultValue[x]>
 <meaningWhenMissing value="[markdown]"/><!-- ![??](lock.png) 0..1 Implicit meaning when this element is missing -->
 <orderMeaning value="[string]"/><!-- 0..1 What the order of the elements means -->
 <fixed[x]><!-- ![??](lock.png) 0..1 * Value must be exactly this --></fixed[x]>
 <pattern[x]><!-- ![??](lock.png) 0..1 * Value must have at least these property values --></pattern[x]>
 <example>  <!-- 0..* Example value (as defined for type) -->
  <label value="[string]"/><!-- 1..1 Describes the purpose of this example -->
  <value[x]><!-- 1..1 * Value of Example (one of allowed types) --></value[x]>
 </example>
 <minValue[x]><!-- 0..1 date|dateTime|instant|time|decimal|integer|positiveInt|
   unsignedInt|Quantity Minimum Allowed Value (for some types) --></minValue[x]>
 <maxValue[x]><!-- 0..1 date|dateTime|instant|time|decimal|integer|positiveInt|
   unsignedInt|Quantity Maximum Allowed Value (for some types) --></maxValue[x]>
 <maxLength value="[integer]"/><!-- 0..1 Max length for strings -->
 <condition value="[id]"/><!-- 0..* Reference to invariant about presence -->
 <constraint>  <!-- 0..* Condition that must evaluate to true -->
  <key value="[id]"/><!-- ![??](lock.png) 1..1 Target of 'condition' reference above -->
  <requirements value="[string]"/><!-- 0..1 Why this constraint is necessary or appropriate -->
  <severity value="[code]"/><!-- 1..1 error | warning -->
  <human value="[string]"/><!-- 1..1 Human description of constraint -->
  <expression value="[string]"/><!-- 0..1 FHIRPath expression of constraint -->
  <xpath value="[string]"/><!-- 0..1 XPath expression of constraint -->
  <source><!-- 0..1 canonical(StructureDefinition) Reference to original source of constraint --></source>
 </constraint>
 <mustSupport value="[boolean]"/><!-- 0..1 If the element must be supported -->
 <isModifier value="[boolean]"/><!-- 0..1 If this modifies the meaning of other elements -->
 <isModifierReason value="[string]"/><!-- 0..1 Reason that this element is marked as a modifier -->
 <isSummary value="[boolean]"/><!-- 0..1 Include when _summary = true? -->
 <binding>  <!-- ![??](lock.png) 0..1 ValueSet details if this is coded -->
  <strength value="[code]"/><!-- 1..1 required | extensible | preferred | example -->
  <description value="[string]"/><!-- 0..1 Human explanation of the value set -->
  <valueSet><!-- ![??](lock.png) 0..1 canonical(ValueSet) Source of value set --></valueSet>
 </binding>
 <mapping>  <!-- 0..* Map element to another set of definitions -->
  <identity value="[id]"/><!-- 1..1 Reference to mapping declaration -->
  <language value="[code]"/><!-- 0..1 Computable language of mapping -->
  <map value="[string]"/><!-- 1..1 Details of the mapping -->
  <comment value="[string]"/><!-- 0..1 Comments about the mapping or its use -->
 </mapping>
</ElementDefinition>
```

**JSON Template**

```

{![doco](help.png)
  // from BackboneElement: extension, modifierExtension
  "path" : "<string>", // R!  Path of the element in the hierarchy of elements
  "representation" : ["<code>"], // xmlAttr | xmlText | typeAttr | cdaText | xhtml
  "sliceName" : "<string>", // Name for this particular element (in a set of slices)
  "sliceIsConstraining" : <boolean>, // If this slice definition constrains an inherited slice definition (or not)
  "label" : "<string>", // Name for element to display with or prompt for element
  "code" : [{ Coding }], // Corresponding codes in terminologies
  "slicing" : { // This element is sliced - slices follow
    "discriminator" : [{ // Element values that are used to distinguish the slices
      "type" : "<code>", // R!  value | exists | pattern | type | profile
      "path" : "<string>" // R!  Path to element value
    }],
    "description" : "<string>", // C? Text description of how slicing works (or not)
    "ordered" : <boolean>, // If elements must be in same order as slices
    "rules" : "<code>" // R!  closed | open | openAtEnd
  },
  "short" : "<string>", // Concise definition for space-constrained presentation
  "definition" : "<markdown>", // Full formal definition as narrative text
  "comment" : "<markdown>", // Comments about the use of this element
  "requirements" : "<markdown>", // Why this resource has been created
  "alias" : ["<string>"], // Other names
  "min" : "<unsignedInt>", // C? Minimum Cardinality
  "max" : "<string>", // C? Maximum Cardinality (a number or *)
  "base" : { // Base definition information for tools
    "path" : "<string>", // R!  Path that identifies the base element
    "min" : "<unsignedInt>", // R!  Min cardinality of the base element
    "max" : "<string>" // R!  Max cardinality of the base element
  },
  "contentReference" : "<uri>", // C? Reference to definition of content for the element
  "type" : [{ // C? Data type and Profile for this element
    "code" : "<uri>", // R!  Data type or Resource (reference to definition)
    "profile" : [{ canonical(StructureDefinition|ImplementationGuide) }], // Profiles (StructureDefinition or IG) - one must apply
    "targetProfile" : [{ canonical(StructureDefinition|ImplementationGuide) }], // Profile (StructureDefinition or IG) on the Reference/canonical target - one must apply
    "aggregation" : ["<code>"], // C? contained | referenced | bundled - how aggregated
    "versioning" : "<code>" // either | independent | specific
  }],
  // defaultValue[x]: Specified value if missing from instance. One of these 50:
  "defaultValueBase64Binary" : "<base64Binary>",
  "defaultValueBoolean" : <boolean>,
  "defaultValueCanonical" : "<canonical>",
  "defaultValueCode" : "<code>",
  "defaultValueDate" : "<date>",
  "defaultValueDateTime" : "<dateTime>",
  "defaultValueDecimal" : <decimal>,
  "defaultValueId" : "<id>",
  "defaultValueInstant" : "<instant>",
  "defaultValueInteger" : <integer>,
  "defaultValueMarkdown" : "<markdown>",
  "defaultValueOid" : "<oid>",
  "defaultValuePositiveInt" : "<positiveInt>",
  "defaultValueString" : "<string>",
  "defaultValueTime" : "<time>",
  "defaultValueUnsignedInt" : "<unsignedInt>",
  "defaultValueUri" : "<uri>",
  "defaultValueUrl" : "<url>",
  "defaultValueUuid" : "<uuid>",
  "defaultValueAddress" : { Address },
  "defaultValueAge" : { Age },
  "defaultValueAnnotation" : { Annotation },
  "defaultValueAttachment" : { Attachment },
  "defaultValueCodeableConcept" : { CodeableConcept },
  "defaultValueCoding" : { Coding },
  "defaultValueContactPoint" : { ContactPoint },
  "defaultValueCount" : { Count },
  "defaultValueDistance" : { Distance },
  "defaultValueDuration" : { Duration },
  "defaultValueHumanName" : { HumanName },
  "defaultValueIdentifier" : { Identifier },
  "defaultValueMoney" : { Money },
  "defaultValuePeriod" : { Period },
  "defaultValueQuantity" : { Quantity },
  "defaultValueRange" : { Range },
  "defaultValueRatio" : { Ratio },
  "defaultValueReference" : { Reference },
  "defaultValueSampledData" : { SampledData },
  "defaultValueSignature" : { Signature },
  "defaultValueTiming" : { Timing },
  "defaultValueContactDetail" : { ContactDetail },
  "defaultValueContributor" : { Contributor },
  "defaultValueDataRequirement" : { DataRequirement },
  "defaultValueExpression" : { Expression },
  "defaultValueParameterDefinition" : { ParameterDefinition },
  "defaultValueRelatedArtifact" : { RelatedArtifact },
  "defaultValueTriggerDefinition" : { TriggerDefinition },
  "defaultValueUsageContext" : { UsageContext },
  "defaultValueDosage" : { Dosage },
  "defaultValueMeta" : { Meta },
  "meaningWhenMissing" : "<markdown>", // C? Implicit meaning when this element is missing
  "orderMeaning" : "<string>", // What the order of the elements means
  // fixed[x]: Value must be exactly this. One of these 50:
  "fixedBase64Binary" : "<base64Binary>",
  "fixedBoolean" : <boolean>,
  "fixedCanonical" : "<canonical>",
  "fixedCode" : "<code>",
  "fixedDate" : "<date>",
  "fixedDateTime" : "<dateTime>",
  "fixedDecimal" : <decimal>,
  "fixedId" : "<id>",
  "fixedInstant" : "<instant>",
  "fixedInteger" : <integer>,
  "fixedMarkdown" : "<markdown>",
  "fixedOid" : "<oid>",
  "fixedPositiveInt" : "<positiveInt>",
  "fixedString" : "<string>",
  "fixedTime" : "<time>",
  "fixedUnsignedInt" : "<unsignedInt>",
  "fixedUri" : "<uri>",
  "fixedUrl" : "<url>",
  "fixedUuid" : "<uuid>",
  "fixedAddress" : { Address },
  "fixedAge" : { Age },
  "fixedAnnotation" : { Annotation },
  "fixedAttachment" : { Attachment },
  "fixedCodeableConcept" : { CodeableConcept },
  "fixedCoding" : { Coding },
  "fixedContactPoint" : { ContactPoint },
  "fixedCount" : { Count },
  "fixedDistance" : { Distance },
  "fixedDuration" : { Duration },
  "fixedHumanName" : { HumanName },
  "fixedIdentifier" : { Identifier },
  "fixedMoney" : { Money },
  "fixedPeriod" : { Period },
  "fixedQuantity" : { Quantity },
  "fixedRange" : { Range },
  "fixedRatio" : { Ratio },
  "fixedReference" : { Reference },
  "fixedSampledData" : { SampledData },
  "fixedSignature" : { Signature },
  "fixedTiming" : { Timing },
  "fixedContactDetail" : { ContactDetail },
  "fixedContributor" : { Contributor },
  "fixedDataRequirement" : { DataRequirement },
  "fixedExpression" : { Expression },
  "fixedParameterDefinition" : { ParameterDefinition },
  "fixedRelatedArtifact" : { RelatedArtifact },
  "fixedTriggerDefinition" : { TriggerDefinition },
  "fixedUsageContext" : { UsageContext },
  "fixedDosage" : { Dosage },
  "fixedMeta" : { Meta },
  // pattern[x]: Value must have at least these property values. One of these 50:
  "patternBase64Binary" : "<base64Binary>",
  "patternBoolean" : <boolean>,
  "patternCanonical" : "<canonical>",
  "patternCode" : "<code>",
  "patternDate" : "<date>",
  "patternDateTime" : "<dateTime>",
  "patternDecimal" : <decimal>,
  "patternId" : "<id>",
  "patternInstant" : "<instant>",
  "patternInteger" : <integer>,
  "patternMarkdown" : "<markdown>",
  "patternOid" : "<oid>",
  "patternPositiveInt" : "<positiveInt>",
  "patternString" : "<string>",
  "patternTime" : "<time>",
  "patternUnsignedInt" : "<unsignedInt>",
  "patternUri" : "<uri>",
  "patternUrl" : "<url>",
  "patternUuid" : "<uuid>",
  "patternAddress" : { Address },
  "patternAge" : { Age },
  "patternAnnotation" : { Annotation },
  "patternAttachment" : { Attachment },
  "patternCodeableConcept" : { CodeableConcept },
  "patternCoding" : { Coding },
  "patternContactPoint" : { ContactPoint },
  "patternCount" : { Count },
  "patternDistance" : { Distance },
  "patternDuration" : { Duration },
  "patternHumanName" : { HumanName },
  "patternIdentifier" : { Identifier },
  "patternMoney" : { Money },
  "patternPeriod" : { Period },
  "patternQuantity" : { Quantity },
  "patternRange" : { Range },
  "patternRatio" : { Ratio },
  "patternReference" : { Reference },
  "patternSampledData" : { SampledData },
  "patternSignature" : { Signature },
  "patternTiming" : { Timing },
  "patternContactDetail" : { ContactDetail },
  "patternContributor" : { Contributor },
  "patternDataRequirement" : { DataRequirement },
  "patternExpression" : { Expression },
  "patternParameterDefinition" : { ParameterDefinition },
  "patternRelatedArtifact" : { RelatedArtifact },
  "patternTriggerDefinition" : { TriggerDefinition },
  "patternUsageContext" : { UsageContext },
  "patternDosage" : { Dosage },
  "patternMeta" : { Meta },
  "example" : [{ // Example value (as defined for type)
    "label" : "<string>", // R!  Describes the purpose of this example
    // value[x]: Value of Example (one of allowed types). One of these 50:
    "valueBase64Binary" : "<base64Binary>"
    "valueBoolean" : <boolean>
    "valueCanonical" : "<canonical>"
    "valueCode" : "<code>"
    "valueDate" : "<date>"
    "valueDateTime" : "<dateTime>"
    "valueDecimal" : <decimal>
    "valueId" : "<id>"
    "valueInstant" : "<instant>"
    "valueInteger" : <integer>
    "valueMarkdown" : "<markdown>"
    "valueOid" : "<oid>"
    "valuePositiveInt" : "<positiveInt>"
    "valueString" : "<string>"
    "valueTime" : "<time>"
    "valueUnsignedInt" : "<unsignedInt>"
    "valueUri" : "<uri>"
    "valueUrl" : "<url>"
    "valueUuid" : "<uuid>"
    "valueAddress" : { Address }
    "valueAge" : { Age }
    "valueAnnotation" : { Annotation }
    "valueAttachment" : { Attachment }
    "valueCodeableConcept" : { CodeableConcept }
    "valueCoding" : { Coding }
    "valueContactPoint" : { ContactPoint }
    "valueCount" : { Count }
    "valueDistance" : { Distance }
    "valueDuration" : { Duration }
    "valueHumanName" : { HumanName }
    "valueIdentifier" : { Identifier }
    "valueMoney" : { Money }
    "valuePeriod" : { Period }
    "valueQuantity" : { Quantity }
    "valueRange" : { Range }
    "valueRatio" : { Ratio }
    "valueReference" : { Reference }
    "valueSampledData" : { SampledData }
    "valueSignature" : { Signature }
    "valueTiming" : { Timing }
    "valueContactDetail" : { ContactDetail }
    "valueContributor" : { Contributor }
    "valueDataRequirement" : { DataRequirement }
    "valueExpression" : { Expression }
    "valueParameterDefinition" : { ParameterDefinition }
    "valueRelatedArtifact" : { RelatedArtifact }
    "valueTriggerDefinition" : { TriggerDefinition }
    "valueUsageContext" : { UsageContext }
    "valueDosage" : { Dosage }
    "valueMeta" : { Meta }
  }],
  // minValue[x]: Minimum Allowed Value (for some types). One of these 9:
  "minValueDate" : "<date>",
  "minValueDateTime" : "<dateTime>",
  "minValueInstant" : "<instant>",
  "minValueTime" : "<time>",
  "minValueDecimal" : <decimal>,
  "minValueInteger" : <integer>,
  "minValuePositiveInt" : "<positiveInt>",
  "minValueUnsignedInt" : "<unsignedInt>",
  "minValueQuantity" : { Quantity },
  // maxValue[x]: Maximum Allowed Value (for some types). One of these 9:
  "maxValueDate" : "<date>",
  "maxValueDateTime" : "<dateTime>",
  "maxValueInstant" : "<instant>",
  "maxValueTime" : "<time>",
  "maxValueDecimal" : <decimal>,
  "maxValueInteger" : <integer>,
  "maxValuePositiveInt" : "<positiveInt>",
  "maxValueUnsignedInt" : "<unsignedInt>",
  "maxValueQuantity" : { Quantity },
  "maxLength" : <integer>, // Max length for strings
  "condition" : ["<id>"], // Reference to invariant about presence
  "constraint" : [{ // Condition that must evaluate to true
    "key" : "<id>", // C? R!  Target of 'condition' reference above
    "requirements" : "<string>", // Why this constraint is necessary or appropriate
    "severity" : "<code>", // R!  error | warning
    "human" : "<string>", // R!  Human description of constraint
    "expression" : "<string>", // FHIRPath expression of constraint
    "xpath" : "<string>", // XPath expression of constraint
    "source" : { canonical(StructureDefinition) } // Reference to original source of constraint
  }],
  "mustSupport" : <boolean>, // If the element must be supported
  "isModifier" : <boolean>, // If this modifies the meaning of other elements
  "isModifierReason" : "<string>", // Reason that this element is marked as a modifier
  "isSummary" : <boolean>, // Include when _summary = true?
  "binding" : { // C? ValueSet details if this is coded
    "strength" : "<code>", // R!  required | extensible | preferred | example
    "description" : "<string>", // Human explanation of the value set
    "valueSet" : { canonical(ValueSet) } // C? Source of value set
  },
  "mapping" : [{ // Map element to another set of definitions
    "identity" : "<id>", // R!  Reference to mapping declaration
    "language" : "<code>", // Computable language of mapping
    "map" : "<string>", // R!  Details of the mapping
    "comment" : "<string>" // Comments about the mapping or its use
  }]
}
```

**Turtle Template**

```

@prefix fhir: <http://hl7.org/fhir/> .

[
 # from BackboneElement: Element.extension, BackboneElement.modifierextension
  fhir:ElementDefinition.path [ string ]; # 1..1 Path of the element in the hierarchy of elements
  fhir:ElementDefinition.representation [ code ], ... ; # 0..* xmlAttr | xmlText | typeAttr | cdaText | xhtml
  fhir:ElementDefinition.sliceName [ string ]; # 0..1 Name for this particular element (in a set of slices)
  fhir:ElementDefinition.sliceIsConstraining [ boolean ]; # 0..1 If this slice definition constrains an inherited slice definition (or not)
  fhir:ElementDefinition.label [ string ]; # 0..1 Name for element to display with or prompt for element
  fhir:ElementDefinition.code [ Coding ], ... ; # 0..* Corresponding codes in terminologies
  fhir:ElementDefinition.slicing [ # 0..1 This element is sliced - slices follow
    fhir:ElementDefinition.slicing.discriminator [ # 0..* Element values that are used to distinguish the slices
      fhir:ElementDefinition.slicing.discriminator.type [ code ]; # 1..1 value | exists | pattern | type | profile
      fhir:ElementDefinition.slicing.discriminator.path [ string ]; # 1..1 Path to element value
    ], ...;
    fhir:ElementDefinition.slicing.description [ string ]; # 0..1 Text description of how slicing works (or not)
    fhir:ElementDefinition.slicing.ordered [ boolean ]; # 0..1 If elements must be in same order as slices
    fhir:ElementDefinition.slicing.rules [ code ]; # 1..1 closed | open | openAtEnd
  ];
  fhir:ElementDefinition.short [ string ]; # 0..1 Concise definition for space-constrained presentation
  fhir:ElementDefinition.definition [ markdown ]; # 0..1 Full formal definition as narrative text
  fhir:ElementDefinition.comment [ markdown ]; # 0..1 Comments about the use of this element
  fhir:ElementDefinition.requirements [ markdown ]; # 0..1 Why this resource has been created
  fhir:ElementDefinition.alias [ string ], ... ; # 0..* Other names
  fhir:ElementDefinition.min [ unsignedInt ]; # 0..1 Minimum Cardinality
  fhir:ElementDefinition.max [ string ]; # 0..1 Maximum Cardinality (a number or *)
  fhir:ElementDefinition.base [ # 0..1 Base definition information for tools
    fhir:ElementDefinition.base.path [ string ]; # 1..1 Path that identifies the base element
    fhir:ElementDefinition.base.min [ unsignedInt ]; # 1..1 Min cardinality of the base element
    fhir:ElementDefinition.base.max [ string ]; # 1..1 Max cardinality of the base element
  ];
  fhir:ElementDefinition.contentReference [ uri ]; # 0..1 Reference to definition of content for the element
  fhir:ElementDefinition.type [ # 0..* Data type and Profile for this element
    fhir:ElementDefinition.type.code [ uri ]; # 1..1 Data type or Resource (reference to definition)
    fhir:ElementDefinition.type.profile [ canonical(StructureDefinition|ImplementationGuide) ], ... ; # 0..* Profiles (StructureDefinition or IG) - one must apply
    fhir:ElementDefinition.type.targetProfile [ canonical(StructureDefinition|ImplementationGuide) ], ... ; # 0..* Profile (StructureDefinition or IG) on the Reference/canonical target - one must apply
    fhir:ElementDefinition.type.aggregation [ code ], ... ; # 0..* contained | referenced | bundled - how aggregated
    fhir:ElementDefinition.type.versioning [ code ]; # 0..1 either | independent | specific
  ], ...;
  # ElementDefinition.defaultValue[x] : 0..1 Specified value if missing from instance. One of these 50
    fhir:ElementDefinition.defaultValueBase64Binary [ base64Binary ]
    fhir:ElementDefinition.defaultValueBoolean [ boolean ]
    fhir:ElementDefinition.defaultValueCanonical [ canonical ]
    fhir:ElementDefinition.defaultValueCode [ code ]
    fhir:ElementDefinition.defaultValueDate [ date ]
    fhir:ElementDefinition.defaultValueDateTime [ dateTime ]
    fhir:ElementDefinition.defaultValueDecimal [ decimal ]
    fhir:ElementDefinition.defaultValueId [ id ]
    fhir:ElementDefinition.defaultValueInstant [ instant ]
    fhir:ElementDefinition.defaultValueInteger [ integer ]
    fhir:ElementDefinition.defaultValueMarkdown [ markdown ]
    fhir:ElementDefinition.defaultValueOid [ oid ]
    fhir:ElementDefinition.defaultValuePositiveInt [ positiveInt ]
    fhir:ElementDefinition.defaultValueString [ string ]
    fhir:ElementDefinition.defaultValueTime [ time ]
    fhir:ElementDefinition.defaultValueUnsignedInt [ unsignedInt ]
    fhir:ElementDefinition.defaultValueUri [ uri ]
    fhir:ElementDefinition.defaultValueUrl [ url ]
    fhir:ElementDefinition.defaultValueUuid [ uuid ]
    fhir:ElementDefinition.defaultValueAddress [ Address ]
    fhir:ElementDefinition.defaultValueAge [ Age ]
    fhir:ElementDefinition.defaultValueAnnotation [ Annotation ]
    fhir:ElementDefinition.defaultValueAttachment [ Attachment ]
    fhir:ElementDefinition.defaultValueCodeableConcept [ CodeableConcept ]
    fhir:ElementDefinition.defaultValueCoding [ Coding ]
    fhir:ElementDefinition.defaultValueContactPoint [ ContactPoint ]
    fhir:ElementDefinition.defaultValueCount [ Count ]
    fhir:ElementDefinition.defaultValueDistance [ Distance ]
    fhir:ElementDefinition.defaultValueDuration [ Duration ]
    fhir:ElementDefinition.defaultValueHumanName [ HumanName ]
    fhir:ElementDefinition.defaultValueIdentifier [ Identifier ]
    fhir:ElementDefinition.defaultValueMoney [ Money ]
    fhir:ElementDefinition.defaultValuePeriod [ Period ]
    fhir:ElementDefinition.defaultValueQuantity [ Quantity ]
    fhir:ElementDefinition.defaultValueRange [ Range ]
    fhir:ElementDefinition.defaultValueRatio [ Ratio ]
    fhir:ElementDefinition.defaultValueReference [ Reference ]
    fhir:ElementDefinition.defaultValueSampledData [ SampledData ]
    fhir:ElementDefinition.defaultValueSignature [ Signature ]
    fhir:ElementDefinition.defaultValueTiming [ Timing ]
    fhir:ElementDefinition.defaultValueContactDetail [ ContactDetail ]
    fhir:ElementDefinition.defaultValueContributor [ Contributor ]
    fhir:ElementDefinition.defaultValueDataRequirement [ DataRequirement ]
    fhir:ElementDefinition.defaultValueExpression [ Expression ]
    fhir:ElementDefinition.defaultValueParameterDefinition [ ParameterDefinition ]
    fhir:ElementDefinition.defaultValueRelatedArtifact [ RelatedArtifact ]
    fhir:ElementDefinition.defaultValueTriggerDefinition [ TriggerDefinition ]
    fhir:ElementDefinition.defaultValueUsageContext [ UsageContext ]
    fhir:ElementDefinition.defaultValueDosage [ Dosage ]
    fhir:ElementDefinition.defaultValueMeta [ Meta ]
  fhir:ElementDefinition.meaningWhenMissing [ markdown ]; # 0..1 Implicit meaning when this element is missing
  fhir:ElementDefinition.orderMeaning [ string ]; # 0..1 What the order of the elements means
  # ElementDefinition.fixed[x] : 0..1 Value must be exactly this. One of these 50
    fhir:ElementDefinition.fixedBase64Binary [ base64Binary ]
    fhir:ElementDefinition.fixedBoolean [ boolean ]
    fhir:ElementDefinition.fixedCanonical [ canonical ]
    fhir:ElementDefinition.fixedCode [ code ]
    fhir:ElementDefinition.fixedDate [ date ]
    fhir:ElementDefinition.fixedDateTime [ dateTime ]
    fhir:ElementDefinition.fixedDecimal [ decimal ]
    fhir:ElementDefinition.fixedId [ id ]
    fhir:ElementDefinition.fixedInstant [ instant ]
    fhir:ElementDefinition.fixedInteger [ integer ]
    fhir:ElementDefinition.fixedMarkdown [ markdown ]
    fhir:ElementDefinition.fixedOid [ oid ]
    fhir:ElementDefinition.fixedPositiveInt [ positiveInt ]
    fhir:ElementDefinition.fixedString [ string ]
    fhir:ElementDefinition.fixedTime [ time ]
    fhir:ElementDefinition.fixedUnsignedInt [ unsignedInt ]
    fhir:ElementDefinition.fixedUri [ uri ]
    fhir:ElementDefinition.fixedUrl [ url ]
    fhir:ElementDefinition.fixedUuid [ uuid ]
    fhir:ElementDefinition.fixedAddress [ Address ]
    fhir:ElementDefinition.fixedAge [ Age ]
    fhir:ElementDefinition.fixedAnnotation [ Annotation ]
    fhir:ElementDefinition.fixedAttachment [ Attachment ]
    fhir:ElementDefinition.fixedCodeableConcept [ CodeableConcept ]
    fhir:ElementDefinition.fixedCoding [ Coding ]
    fhir:ElementDefinition.fixedContactPoint [ ContactPoint ]
    fhir:ElementDefinition.fixedCount [ Count ]
    fhir:ElementDefinition.fixedDistance [ Distance ]
    fhir:ElementDefinition.fixedDuration [ Duration ]
    fhir:ElementDefinition.fixedHumanName [ HumanName ]
    fhir:ElementDefinition.fixedIdentifier [ Identifier ]
    fhir:ElementDefinition.fixedMoney [ Money ]
    fhir:ElementDefinition.fixedPeriod [ Period ]
    fhir:ElementDefinition.fixedQuantity [ Quantity ]
    fhir:ElementDefinition.fixedRange [ Range ]
    fhir:ElementDefinition.fixedRatio [ Ratio ]
    fhir:ElementDefinition.fixedReference [ Reference ]
    fhir:ElementDefinition.fixedSampledData [ SampledData ]
    fhir:ElementDefinition.fixedSignature [ Signature ]
    fhir:ElementDefinition.fixedTiming [ Timing ]
    fhir:ElementDefinition.fixedContactDetail [ ContactDetail ]
    fhir:ElementDefinition.fixedContributor [ Contributor ]
    fhir:ElementDefinition.fixedDataRequirement [ DataRequirement ]
    fhir:ElementDefinition.fixedExpression [ Expression ]
    fhir:ElementDefinition.fixedParameterDefinition [ ParameterDefinition ]
    fhir:ElementDefinition.fixedRelatedArtifact [ RelatedArtifact ]
    fhir:ElementDefinition.fixedTriggerDefinition [ TriggerDefinition ]
    fhir:ElementDefinition.fixedUsageContext [ UsageContext ]
    fhir:ElementDefinition.fixedDosage [ Dosage ]
    fhir:ElementDefinition.fixedMeta [ Meta ]
  # ElementDefinition.pattern[x] : 0..1 Value must have at least these property values. One of these 50
    fhir:ElementDefinition.patternBase64Binary [ base64Binary ]
    fhir:ElementDefinition.patternBoolean [ boolean ]
    fhir:ElementDefinition.patternCanonical [ canonical ]
    fhir:ElementDefinition.patternCode [ code ]
    fhir:ElementDefinition.patternDate [ date ]
    fhir:ElementDefinition.patternDateTime [ dateTime ]
    fhir:ElementDefinition.patternDecimal [ decimal ]
    fhir:ElementDefinition.patternId [ id ]
    fhir:ElementDefinition.patternInstant [ instant ]
    fhir:ElementDefinition.patternInteger [ integer ]
    fhir:ElementDefinition.patternMarkdown [ markdown ]
    fhir:ElementDefinition.patternOid [ oid ]
    fhir:ElementDefinition.patternPositiveInt [ positiveInt ]
    fhir:ElementDefinition.patternString [ string ]
    fhir:ElementDefinition.patternTime [ time ]
    fhir:ElementDefinition.patternUnsignedInt [ unsignedInt ]
    fhir:ElementDefinition.patternUri [ uri ]
    fhir:ElementDefinition.patternUrl [ url ]
    fhir:ElementDefinition.patternUuid [ uuid ]
    fhir:ElementDefinition.patternAddress [ Address ]
    fhir:ElementDefinition.patternAge [ Age ]
    fhir:ElementDefinition.patternAnnotation [ Annotation ]
    fhir:ElementDefinition.patternAttachment [ Attachment ]
    fhir:ElementDefinition.patternCodeableConcept [ CodeableConcept ]
    fhir:ElementDefinition.patternCoding [ Coding ]
    fhir:ElementDefinition.patternContactPoint [ ContactPoint ]
    fhir:ElementDefinition.patternCount [ Count ]
    fhir:ElementDefinition.patternDistance [ Distance ]
    fhir:ElementDefinition.patternDuration [ Duration ]
    fhir:ElementDefinition.patternHumanName [ HumanName ]
    fhir:ElementDefinition.patternIdentifier [ Identifier ]
    fhir:ElementDefinition.patternMoney [ Money ]
    fhir:ElementDefinition.patternPeriod [ Period ]
    fhir:ElementDefinition.patternQuantity [ Quantity ]
    fhir:ElementDefinition.patternRange [ Range ]
    fhir:ElementDefinition.patternRatio [ Ratio ]
    fhir:ElementDefinition.patternReference [ Reference ]
    fhir:ElementDefinition.patternSampledData [ SampledData ]
    fhir:ElementDefinition.patternSignature [ Signature ]
    fhir:ElementDefinition.patternTiming [ Timing ]
    fhir:ElementDefinition.patternContactDetail [ ContactDetail ]
    fhir:ElementDefinition.patternContributor [ Contributor ]
    fhir:ElementDefinition.patternDataRequirement [ DataRequirement ]
    fhir:ElementDefinition.patternExpression [ Expression ]
    fhir:ElementDefinition.patternParameterDefinition [ ParameterDefinition ]
    fhir:ElementDefinition.patternRelatedArtifact [ RelatedArtifact ]
    fhir:ElementDefinition.patternTriggerDefinition [ TriggerDefinition ]
    fhir:ElementDefinition.patternUsageContext [ UsageContext ]
    fhir:ElementDefinition.patternDosage [ Dosage ]
    fhir:ElementDefinition.patternMeta [ Meta ]
  fhir:ElementDefinition.example [ # 0..* Example value (as defined for type)
    fhir:ElementDefinition.example.label [ string ]; # 1..1 Describes the purpose of this example
    # ElementDefinition.example.value[x] : 1..1 Value of Example (one of allowed types). One of these 50
      fhir:ElementDefinition.example.valueBase64Binary [ base64Binary ]
      fhir:ElementDefinition.example.valueBoolean [ boolean ]
      fhir:ElementDefinition.example.valueCanonical [ canonical ]
      fhir:ElementDefinition.example.valueCode [ code ]
      fhir:ElementDefinition.example.valueDate [ date ]
      fhir:ElementDefinition.example.valueDateTime [ dateTime ]
      fhir:ElementDefinition.example.valueDecimal [ decimal ]
      fhir:ElementDefinition.example.valueId [ id ]
      fhir:ElementDefinition.example.valueInstant [ instant ]
      fhir:ElementDefinition.example.valueInteger [ integer ]
      fhir:ElementDefinition.example.valueMarkdown [ markdown ]
      fhir:ElementDefinition.example.valueOid [ oid ]
      fhir:ElementDefinition.example.valuePositiveInt [ positiveInt ]
      fhir:ElementDefinition.example.valueString [ string ]
      fhir:ElementDefinition.example.valueTime [ time ]
      fhir:ElementDefinition.example.valueUnsignedInt [ unsignedInt ]
      fhir:ElementDefinition.example.valueUri [ uri ]
      fhir:ElementDefinition.example.valueUrl [ url ]
      fhir:ElementDefinition.example.valueUuid [ uuid ]
      fhir:ElementDefinition.example.valueAddress [ Address ]
      fhir:ElementDefinition.example.valueAge [ Age ]
      fhir:ElementDefinition.example.valueAnnotation [ Annotation ]
      fhir:ElementDefinition.example.valueAttachment [ Attachment ]
      fhir:ElementDefinition.example.valueCodeableConcept [ CodeableConcept ]
      fhir:ElementDefinition.example.valueCoding [ Coding ]
      fhir:ElementDefinition.example.valueContactPoint [ ContactPoint ]
      fhir:ElementDefinition.example.valueCount [ Count ]
      fhir:ElementDefinition.example.valueDistance [ Distance ]
      fhir:ElementDefinition.example.valueDuration [ Duration ]
      fhir:ElementDefinition.example.valueHumanName [ HumanName ]
      fhir:ElementDefinition.example.valueIdentifier [ Identifier ]
      fhir:ElementDefinition.example.valueMoney [ Money ]
      fhir:ElementDefinition.example.valuePeriod [ Period ]
      fhir:ElementDefinition.example.valueQuantity [ Quantity ]
      fhir:ElementDefinition.example.valueRange [ Range ]
      fhir:ElementDefinition.example.valueRatio [ Ratio ]
      fhir:ElementDefinition.example.valueReference [ Reference ]
      fhir:ElementDefinition.example.valueSampledData [ SampledData ]
      fhir:ElementDefinition.example.valueSignature [ Signature ]
      fhir:ElementDefinition.example.valueTiming [ Timing ]
      fhir:ElementDefinition.example.valueContactDetail [ ContactDetail ]
      fhir:ElementDefinition.example.valueContributor [ Contributor ]
      fhir:ElementDefinition.example.valueDataRequirement [ DataRequirement ]
      fhir:ElementDefinition.example.valueExpression [ Expression ]
      fhir:ElementDefinition.example.valueParameterDefinition [ ParameterDefinition ]
      fhir:ElementDefinition.example.valueRelatedArtifact [ RelatedArtifact ]
      fhir:ElementDefinition.example.valueTriggerDefinition [ TriggerDefinition ]
      fhir:ElementDefinition.example.valueUsageContext [ UsageContext ]
      fhir:ElementDefinition.example.valueDosage [ Dosage ]
      fhir:ElementDefinition.example.valueMeta [ Meta ]
  ], ...;
  # ElementDefinition.minValue[x] : 0..1 Minimum Allowed Value (for some types). One of these 9
    fhir:ElementDefinition.minValueDate [ date ]
    fhir:ElementDefinition.minValueDateTime [ dateTime ]
    fhir:ElementDefinition.minValueInstant [ instant ]
    fhir:ElementDefinition.minValueTime [ time ]
    fhir:ElementDefinition.minValueDecimal [ decimal ]
    fhir:ElementDefinition.minValueInteger [ integer ]
    fhir:ElementDefinition.minValuePositiveInt [ positiveInt ]
    fhir:ElementDefinition.minValueUnsignedInt [ unsignedInt ]
    fhir:ElementDefinition.minValueQuantity [ Quantity ]
  # ElementDefinition.maxValue[x] : 0..1 Maximum Allowed Value (for some types). One of these 9
    fhir:ElementDefinition.maxValueDate [ date ]
    fhir:ElementDefinition.maxValueDateTime [ dateTime ]
    fhir:ElementDefinition.maxValueInstant [ instant ]
    fhir:ElementDefinition.maxValueTime [ time ]
    fhir:ElementDefinition.maxValueDecimal [ decimal ]
    fhir:ElementDefinition.maxValueInteger [ integer ]
    fhir:ElementDefinition.maxValuePositiveInt [ positiveInt ]
    fhir:ElementDefinition.maxValueUnsignedInt [ unsignedInt ]
    fhir:ElementDefinition.maxValueQuantity [ Quantity ]
  fhir:ElementDefinition.maxLength [ integer ]; # 0..1 Max length for strings
  fhir:ElementDefinition.condition [ id ], ... ; # 0..* Reference to invariant about presence
  fhir:ElementDefinition.constraint [ # 0..* Condition that must evaluate to true
    fhir:ElementDefinition.constraint.key [ id ]; # 1..1 Target of 'condition' reference above
    fhir:ElementDefinition.constraint.requirements [ string ]; # 0..1 Why this constraint is necessary or appropriate
    fhir:ElementDefinition.constraint.severity [ code ]; # 1..1 error | warning
    fhir:ElementDefinition.constraint.human [ string ]; # 1..1 Human description of constraint
    fhir:ElementDefinition.constraint.expression [ string ]; # 0..1 FHIRPath expression of constraint
    fhir:ElementDefinition.constraint.xpath [ string ]; # 0..1 XPath expression of constraint
    fhir:ElementDefinition.constraint.source [ canonical(StructureDefinition) ]; # 0..1 Reference to original source of constraint
  ], ...;
  fhir:ElementDefinition.mustSupport [ boolean ]; # 0..1 If the element must be supported
  fhir:ElementDefinition.isModifier [ boolean ]; # 0..1 If this modifies the meaning of other elements
  fhir:ElementDefinition.isModifierReason [ string ]; # 0..1 Reason that this element is marked as a modifier
  fhir:ElementDefinition.isSummary [ boolean ]; # 0..1 Include when _summary = true?
  fhir:ElementDefinition.binding [ # 0..1 ValueSet details if this is coded
    fhir:ElementDefinition.binding.strength [ code ]; # 1..1 required | extensible | preferred | example
    fhir:ElementDefinition.binding.description [ string ]; # 0..1 Human explanation of the value set
    fhir:ElementDefinition.binding.valueSet [ canonical(ValueSet) ]; # 0..1 Source of value set
  ];
  fhir:ElementDefinition.mapping [ # 0..* Map element to another set of definitions
    fhir:ElementDefinition.mapping.identity [ id ]; # 1..1 Reference to mapping declaration
    fhir:ElementDefinition.mapping.language [ code ]; # 0..1 Computable language of mapping
    fhir:ElementDefinition.mapping.map [ string ]; # 1..1 Details of the mapping
    fhir:ElementDefinition.mapping.comment [ string ]; # 0..1 Comments about the mapping or its use
  ], ...;
]
```

**Changes since Release 3**

|  |  |
| --- | --- |
| [ElementDefinition](elementdefinition.html#ElementDefinition) |  |
| ElementDefinition.representation | - Change value set from http://hl7.org/fhir/ValueSet/property-representation to http://hl7.org/fhir/ValueSet/property-representation|4.0.1 |
| ElementDefinition.sliceIsConstraining | - Added Element |
| ElementDefinition.slicing.discriminator.type | - Change value set from http://hl7.org/fhir/ValueSet/discriminator-type to http://hl7.org/fhir/ValueSet/discriminator-type|4.0.1 |
| ElementDefinition.slicing.ordered | - Default Value "false" removed |
| ElementDefinition.slicing.rules | - Change value set from http://hl7.org/fhir/ValueSet/resource-slicing-rules to http://hl7.org/fhir/ValueSet/resource-slicing-rules|4.0.1 |
| ElementDefinition.type.profile | - Max Cardinality changed from 1 to \* - Type changed from uri to canonical(StructureDefinition | ImplementationGuide) |
| ElementDefinition.type.targetProfile | - Max Cardinality changed from 1 to \* - Type changed from uri to canonical(StructureDefinition | ImplementationGuide) |
| ElementDefinition.type.aggregation | - Change value set from http://hl7.org/fhir/ValueSet/resource-aggregation-mode to http://hl7.org/fhir/ValueSet/resource-aggregation-mode|4.0.1 |
| ElementDefinition.type.versioning | - Change value set from http://hl7.org/fhir/ValueSet/reference-version-rules to http://hl7.org/fhir/ValueSet/reference-version-rules|4.0.1 - Default Value "either" removed |
| ElementDefinition.defaultValue[x] | - Add Types canonical, url, uuid, ContactDetail, Contributor, DataRequirement, Expression, ParameterDefinition, RelatedArtifact, TriggerDefinition, UsageContext, Dosage |
| ElementDefinition.fixed[x] | - Add Types canonical, url, uuid, ContactDetail, Contributor, DataRequirement, Expression, ParameterDefinition, RelatedArtifact, TriggerDefinition, UsageContext, Dosage |
| ElementDefinition.pattern[x] | - Add Types canonical, url, uuid, ContactDetail, Contributor, DataRequirement, Expression, ParameterDefinition, RelatedArtifact, TriggerDefinition, UsageContext, Dosage |
| ElementDefinition.example.value[x] | - Add Types canonical, url, uuid, ContactDetail, Contributor, DataRequirement, Expression, ParameterDefinition, RelatedArtifact, TriggerDefinition, UsageContext, Dosage |
| ElementDefinition.constraint.severity | - Change value set from http://hl7.org/fhir/ValueSet/constraint-severity to http://hl7.org/fhir/ValueSet/constraint-severity|4.0.1 |
| ElementDefinition.constraint.expression | - Min Cardinality changed from 1 to 0 |
| ElementDefinition.constraint.source | - Type changed from uri to canonical(StructureDefinition) |
| ElementDefinition.mustSupport | - Default Value "false" removed |
| ElementDefinition.isModifier | - Default Value "false" removed |
| ElementDefinition.isModifierReason | - Added Element |
| ElementDefinition.isSummary | - Default Value "false" removed |
| ElementDefinition.binding.strength | - Change value set from http://hl7.org/fhir/ValueSet/binding-strength to http://hl7.org/fhir/ValueSet/binding-strength|4.0.1 |
| ElementDefinition.binding.valueSet | - Renamed from valueSet[x] to valueSet - Add Type canonical(ValueSet) - Remove Types uri, Reference(ValueSet) |
| ElementDefinition.mapping.language | - Change value set from http://hl7.org/fhir/ValueSet/mimetypes to http://hl7.org/fhir/ValueSet/mimetypes|4.0.1 |

See the [Full Difference](diff.html) for further information

**Constraints**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **id** | **Level** | **Location** | **Description** | **[Expression](fhirpath.html)** |
| **eld-1** | [Rule](conformance-rules.html#rule) | ElementDefinition.slicing | If there are no discriminators, there must be a definition | discriminator.exists() or description.exists() |
| **eld-2** | [Rule](conformance-rules.html#rule) | (base) | Min <= Max | min.empty() or max.empty() or (max = '\*') or iif(max != '\*', min <= max.toInteger()) |
| **eld-3** | [Rule](conformance-rules.html#rule) | ElementDefinition.max | Max SHALL be a number or "\*" | empty() or ($this = '\*') or (toInteger() >= 0) |
| **eld-4** | [Rule](conformance-rules.html#rule) | ElementDefinition.type | Aggregation may only be specified if one of the allowed types for the element is a reference | aggregation.empty() or (code = 'Reference') or (code = 'canonical') |
| **eld-5** | [Rule](conformance-rules.html#rule) | (base) | if the element definition has a contentReference, it cannot have type, defaultValue, fixed, pattern, example, minValue, maxValue, maxLength, or binding | contentReference.empty() or (type.empty() and defaultValue.empty() and fixed.empty() and pattern.empty() and example.empty() and minValue.empty() and maxValue.empty() and maxLength.empty() and binding.empty()) |
| **eld-6** | [Rule](conformance-rules.html#rule) | (base) | Fixed value may only be specified if there is one type | fixed.empty() or (type.count() <= 1) |
| **eld-7** | [Rule](conformance-rules.html#rule) | (base) | Pattern may only be specified if there is one type | pattern.empty() or (type.count() <= 1) |
| **eld-8** | [Rule](conformance-rules.html#rule) | (base) | Pattern and fixed are mutually exclusive | pattern.empty() or fixed.empty() |
| **eld-11** | [Rule](conformance-rules.html#rule) | (base) | Binding can only be present for coded elements, string, and uri | binding.empty() or type.code.empty() or type.select((code = 'code') or (code = 'Coding') or (code='CodeableConcept') or (code = 'Quantity') or (code = 'string') or (code = 'uri')).exists() |
| **eld-12** | [Rule](conformance-rules.html#rule) | ElementDefinition.binding | ValueSet SHALL start with http:// or https:// or urn: | valueSet.exists() implies (valueSet.startsWith('http:') or valueSet.startsWith('https') or valueSet.startsWith('urn:')) |
| **eld-13** | [Rule](conformance-rules.html#rule) | (base) | Types must be unique by code | type.select(code).isDistinct() |
| **eld-14** | [Rule](conformance-rules.html#rule) | (base) | Constraints must be unique by key | constraint.select(key).isDistinct() |
| **eld-15** | [Rule](conformance-rules.html#rule) | (base) | default value and meaningWhenMissing are mutually exclusive | defaultValue.empty() or meaningWhenMissing.empty() |
| **eld-16** | [Rule](conformance-rules.html#rule) | (base) | sliceName must be composed of proper tokens separated by "/" | sliceName.empty() or sliceName.matches('^[a-zA-Z0-9\\/\\-\_\\[\\]\\@]+$') |
| **eld-17** | [Rule](conformance-rules.html#rule) | ElementDefinition.type | targetProfile is only allowed if the type is Reference or canonical | (code='Reference' or code = 'canonical') or targetProfile.empty() |
| **eld-18** | [Rule](conformance-rules.html#rule) | (base) | Must have a modifier reason if isModifier = true | (isModifier.exists() and isModifier) implies isModifierReason.exists() |
| **eld-19** | [Rule](conformance-rules.html#rule) | (base) | Element names cannot include some special characters | path.matches('[^\\s\\.,:;\\\'"\\/|?!@#$%&\*()\\[\\]{}]{1,64}(\\.[^\\s\\.,:;\\\'"\\/|?!@#$%&\*()\\[\\]{}]{1,64}(\\[x\\])?(\\:[^\\s\\.]+)?)\*') |
| **eld-20** | [Warning](conformance-rules.html#warning) | (base) | Element names should be simple alphanumerics with a max of 64 characters, or code generation tools may be broken | path.matches('[A-Za-z][A-Za-z0-9]\*(\\.[a-z][A-Za-z0-9]\*(\\[x])?)\*') |
| **eld-21** | [Warning](conformance-rules.html#warning) | ElementDefinition.constraint | Constraints should have an expression or else validators will not be able to enforce them | expression.exists() |
| **eld-22** | [Rule](conformance-rules.html#rule) | (base) | sliceIsConstraining can only appear if slicename is present | sliceIsConstraining.exists() implies sliceName.exists() |

## 2.30.0.2 Use of ElementDefinition.path

The `path` element is the most important property of the element definition.
It both names the element, and locates the element within a hierarchy defined within a
particular context. Within the FHIR specification, there is only one original definition
for each path. This is the master definition to which all the other definitions with the
same path must conform.

All elements defined within the FHIR specification itself are defined within a [StructureDefinition](structuredefinition.html) that defines a resource, or a datatype. This defines the identity of the element and provides the
context in which the meaning of the element is understood. When Elements are defined, the following rules apply:

- Element names (the parts of a path delineated by the '.' character) SHALL NOT contain whitespace (i.e. Unicode characters marked as whitespace)
- Element names SHALL NOT contain the characters ,:;'"/|?!@#$%^&\*()[]{}
- Element names SHOULD not contain non-ASCII characters
- Element names SHALL NOT exceed 64 characters in length
- Element paths cannot imply elements that are not explicitly defined i.e. a.b.c.d cannot be defined unless a.b.c is explicitly defined
- By convention, each path starts with an uppercase letter (type) but all the element names that follow this are lowercase (not type names). All resources and data types (except for Primitive data types) follow this convention, but logical
  models are not required to do so

Elements may be defined in:

- StructureDefinitions of [kind](structuredefinition-definitions.html#StructureDefinition.kind) = `resource`, `complex-type` or `primitive-type`, where [derivation](structuredefinition-definitions.html#StructureDefinition.derivation) = `specialization`. These are either Resources or Data Types defined in the specification
- StructureDefinitions of [kind](structuredefinition-definitions.html#StructureDefinition.kind) = `logical`
- Data Elements

StructureDefinitions with [derivation](structuredefinition-definitions.html#StructureDefinition.derivation) = `constraint` (i.e. Resource and Data Type profiles) are not allowed to define or include ElementDefinitions
with a path not defined within the base type definition from which they derive (e.g. in the FHIR specification).

## 2.30.0.3 ElementDefinition.id

In addition to the path, every ElementDefinition SHALL have a populated [id](element.html#table), and the `id` SHALL have a unique value populated by following this algorithm:

- The id will be constructed as a dot separated string, each part corresponding to a token in the path
- For each token in the path, use the syntax `pathpart:slicename/reslicename`
- For type choice elements, the id reflects the type slice. e.g. For path = Patient.deceasedBoolean, the id is Patient.deceased[x]:deceasedBoolean

Note that in a profile with no slices, this id will match the path exactly and entirely.
`id` values constructed in this fashion are unique, and persistent, and may be used as the target of external references into the definition, where necessary.

## 2.30.0.4 Interpretation of ElementDefinition in different contexts

The data type `ElementDefinition` is used in [StructureDefinition](structuredefinition.html). The way its elements are to be used and interpreted depends on the context:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **ElementDefinition field** | **Type definition, first element** | **Type definition, following elements** | **Constraint Definition, first element** | **Constraint Definition, following elements** |
| sliceName | prohibited | prohibited | prohibited | required for slices, else prohibited |
| label | optional | optional | recommended | recommended |
| code | optional | optional | optional | optional |
| slicing | prohibited | prohibited | prohibited | optional |
| short/definition | required | required | required‡ | required‡ |
| requirements/ comments/alias | prohibited | optional | prohibited‡ | optional‡ |
| base | snapshot: required differential: optional | snapshot: required differential: optional | required | required |
| type | required | required | optional | optional |
| nameReference | prohibited | optional | prohibited | optional |
| min/max | optional (irrelevant) | required | optional | optional† |
| defaultValue[x] | prohibited | optional | prohibited | optional† |
| meaningWhenMissing | prohibited | optional | prohibited | optional† |
| fixed[x] | prohibited | prohibited | prohibited | optional |
| pattern[x] | prohibited | prohibited | prohibited | optional |
| example[x] | prohibited | optional | prohibited | optional |
| minValue[x] | prohibited | prohibited | prohibited | optional |
| maxValue[x] | prohibited | prohibited | prohibited | optional |
| maxLength | prohibited | prohibited | prohibited | optional |
| mustSupport | prohibited | prohibited | optional | optional |
| isModifier | prohibited | optional | prohibited | optional† |
| isSummary | prohibited | optional | prohibited | optional† |
| binding | prohibited | optional | prohibited | optional |
| constraint | optional | optional | optional∆ | optional∆ |
| condition | prohibited | optional | prohibited | optional∆ |
| mapping | optional | optional | optional∆ | optional∆ |

Notes:

- Type definition: A StructureDefinition without a `baseDefinition` element, or where the derivation type is 'specialization'
- Constraint definition: A StructureDefinition with a `baseDefinition` element and a derivation of 'constraint' - e.g. a definition of a structure that constrains another base structure, referring to the differential portion
- †: The element's presence, and value, must match the definition in the base definition
- ‡: The element content must be consistent with that matching element in the base definition
- ∆: Additional constraints and mappings can be defined, but they do not replace the ones in the base definition

The use of Path and type depends more deeply on the context where the ElementDefinition is used:

|  |  |  |  |
| --- | --- | --- | --- |
| **Context** | **path (1st element)** | **path (following elements)** | **type (1st element)** |
| Base definition of a data type  (example: [Quantity](datatypes.html#Quantity) - [XML](quantity.profile.xml.html), [JSON](quantity.profile.json.html)) | Name of the type | Path inside the datatype | `Element` |
| A constrained data type  (example: [Money](datatypes.html#Money) - [XML](money.profile.xml.html), [JSON](money.profile.json.html)) | Name of the base type | Path inside the datatype | Name of the base type |
| Base definition of a resource  (example: [Patient](patient.html) - [XML](patient.profile.xml.html), [JSON](patient.profile.json.html)) | The name of the resource | Path inside the resource | `DomainResource` or sometimes `Resource` |
| Constraint on a resource  (example: [DAF Patient](vitalsigns.html) - [XML](vitalsigns.profile.xml.html), [JSON](vitalsigns.profile.json.html)) | The name of the resource | Path inside the resource  (including into the data types) | The name of the resource |
| Base Extension (which is a standard data type)  (example: [Extension](extensibility.html#Extension) - [XML](extension.profile.xml.html), [JSON](extension.profile.json.html)) | `Extension` | `Extension.value[x]` or `Extension.extension` | `Extension` |
| A defined Extension  (example: [Extension](extension-geolocation.html) - [XML](extension-geolocation.xml.html), [JSON](extension-geolocation.json.html)) | `Extension` | `Extension.value[x]` or `Extension.extension` (for complex extensions) | `Extension` |

There are additional notes about the use of `ElementDefinition` when defining Extensions on the [Defining Extensions](defining-extensions.html#ed) page.

### 2.30.0.4.1 Rules about Slicing

For a description of slicing, see [Slicing](profiling.html#slicing)

- Slicing is only allowed when constraining an existing structure
- `slicing` can only be used on the first repetition of an element. This first element that declares `slicing` is considered to be the slicing entry
- All elements following the first repeat that containing a slicing SHALL have a `sliceName`
- The special slice name `@default` applies to all entries that are not in any other slice
- The first entry (the one having the `slicing` information) is understood to be the set of constraints that apply to all slices and entries, whether they have a defined slice or not
  It's use follows the "normal case", except:
  - `slicing` must be present
  - `min` governs the number of total occurrences of the sliced element including the number of occurrences in the open portion of the slice (individual slices may have a different `min` value).

### 2.30.0.4.2 Constraining elements with a choice of Type

Elements that allow a choice of multiple types can be constrained. In principle, there are two different types of constraints to apply:

- A constraint that applies to the element as a whole - e.g. as restricting the cardinality, or limiting the choice of types
- A constraint that applies to the use of a particular type - e.g. value set binding

When constraining elements with multiple types, the following rules apply:

- Constraints limiting the acceptable list of types must be applied to the original "[x]" element as this is where the list of acceptable types is defined
- The inclusion of a type specific path (such as "Patient.deceasedBoolean") SHALL NOT be interpreted as constraining allowed types, but instead, it constrains the use of a particular type
- the original element SHALL always be represented in a snapshot; the type specific variants are only represented when needed

### 2.30.0.4.3 Rules about min and max

- **If there is no `StructureDefinition.baseDefinition`**: min and max are always required
- Otherwise, in `StructureDefinition.differential`: min and max are always optional; if they are not present, they default to the min and max from the base definition
- In `StructureDefinition.snapshot`: min and max are always required

### 2.30.0.4.4 Rules about Aggregation

- If an aggregationMode is present in the definition, the 'reference' element SHALL be present and have a value
  and the target of the reference SHALL be aggregated as defined
- If type.versioning is present in the definition, the 'reference' element SHALL be present and have a value
  and the reference SHALL be populated as the versioning constraint dictates.

### 2.30.0.4.5 Missing Elements

Most elements have a minimum cardinality of 0, which means that they may be missing from a resource when it is exchanged between systems.
Generally, when an element is missing, all that an application processing the resource can say about the element
is that the value is unknown - it may have a correct value, but it has not been provided for security or workflow reasons.
On the other hand, it might not have a value at all. All the application can say is that the value is unknown.

This also applies when the element is present, but has no value or child elements, and only has extensions instead.

However, for some elements, this specification makes specific rules about what it means if the element is missing.
Constraints on other structures cannot change the missing meaning of an element.
Here is a list of all elements with a default value or a missing meaning:

- [DataRequirement.subject[x]](metadatatypes-definitions.html#DataRequirement.subject[x]): Patient
- [Period.end](datatypes-definitions.html#Period.end): If the end of the period is missing, it means that the period is ongoing
- [Quantity.comparator](datatypes-definitions.html#Quantity.comparator): If there is no comparator, then there is no modification of the value
- [SampledData.factor](datatypes-definitions.html#SampledData.factor): If no factor is assigned, the data is not adjusted before adding to the origin
- [Timing.repeat.frequency](datatypes-definitions.html#Timing.repeat.frequency): If no frequency is stated, the assumption is that the event occurs once per period, but systems SHOULD always be specific about this
- [ElementDefinition.slicing.ordered](elementdefinition-definitions.html#ElementDefinition.slicing.ordered): Order is not required unless specified
- [ElementDefinition.mustSupport](elementdefinition-definitions.html#ElementDefinition.mustSupport): In a base type, where the element is being defined for the first time, the element is assumed to be mustSupport = false. In a profile (a constraint on an existing type), if mustSupport is not specific in either the differentil or the snapshot, the mustSupport value is not changed fro the base definition. Not, though, that the snapshot SHOULD always populate the mustSuppot value
- [ElementDefinition.isModifier](elementdefinition-definitions.html#ElementDefinition.isModifier): An element is not a modifier element unless it is explicitly specified to be one
- [ElementDefinition.isSummary](elementdefinition-definitions.html#ElementDefinition.isSummary): An element is not included in the summary unless it is explicitly specified to be so
- [ActivityDefinition.subject[x]](activitydefinition-definitions.html#ActivityDefinition.subject[x]): Patient
- [BodyStructure.active](bodystructure-definitions.html#BodyStructure.active): This resource is generally assumed to be active if no value is provided for the active element
- [CarePlan.activity.detail.doNotPerform](careplan-definitions.html#CarePlan.activity.detail.doNotPerform): If missing indicates that the described activity is one that should be engaged in when following the plan.
- [Communication.priority](communication-definitions.html#Communication.priority): If missing, this communication should be treated with normal priority
- [CommunicationRequest.priority](communicationrequest-definitions.html#CommunicationRequest.priority): If missing, this task should be performed with normal priority
- [CommunicationRequest.doNotPerform](communicationrequest-definitions.html#CommunicationRequest.doNotPerform): If do not perform is not specified, the request is a positive request e.g. "do perform"
- [ConceptMap.group.element.target.dependsOn.system](conceptmap-definitions.html#ConceptMap.group.element.target.dependsOn.system): The code is in the source (dependsOn) or target (product) system
- [Consent.provision.actor](consent-definitions.html#Consent.provision.actor): There is no specific actor associated with the exception
- [Consent.provision.action](consent-definitions.html#Consent.provision.action): all actions
- [Consent.provision.data](consent-definitions.html#Consent.provision.data): all data
- [DeviceRequest.priority](devicerequest-definitions.html#DeviceRequest.priority): If missing, normal priority
- [EventDefinition.subject[x]](eventdefinition-definitions.html#EventDefinition.subject[x]): Patient
- [EvidenceVariable.characteristic.exclude](evidencevariable-definitions.html#EvidenceVariable.characteristic.exclude): False
- [FamilyMemberHistory.estimatedAge](familymemberhistory-definitions.html#FamilyMemberHistory.estimatedAge): It is unknown whether the age is an estimate or not
- [Group.active](group-definitions.html#Group.active): This resource is generally assumed to be active if no value is provided for the active element
- [Group.member.period](group-definitions.html#Group.member.period): The member is in the group at this time
- [Group.member.inactive](group-definitions.html#Group.member.inactive): Members are considered active unless explicitly specified otherwise
- [HealthcareService.active](healthcareservice-definitions.html#HealthcareService.active): This resource is generally assumed to be active if no value is provided for the active element
- [Immunization.isSubpotent](immunization-definitions.html#Immunization.isSubpotent): By default, a dose should be considered to be potent.
- [InsurancePlan.status](insuranceplan-definitions.html#InsurancePlan.status): Default interpretation is active.
- [Library.subject[x]](library-definitions.html#Library.subject[x]): Patient
- [Linkage.active](linkage-definitions.html#Linkage.active): This resource is generally assumed to be active if no value is provided for the active element
- [List.entry.deleted](list-definitions.html#List.entry.deleted): List items are generally only treated as deleted when this element explicitly carries a value of true. Systems SHOULD always populate this value when mode is 'changes'
- [Measure.subject[x]](measure-definitions.html#Measure.subject[x]): Patient
- [NamingSystem.uniqueId.preferred](namingsystem-definitions.html#NamingSystem.uniqueId.preferred): If there are multiple ids, and one is labeled "preferred", then the assumption is that the others are not preferred. In the absence of any id marked as preferred, no inference can be drawn
- [Organization.active](organization-definitions.html#Organization.active): This resource is generally assumed to be active if no value is provided for the active element
- [OrganizationAffiliation.active](organizationaffiliation-definitions.html#OrganizationAffiliation.active): This resource is generally assumed to be active if no value is provided for the active element
- [Patient.active](patient-definitions.html#Patient.active): This resource is generally assumed to be active if no value is provided for the active element
- [PlanDefinition.subject[x]](plandefinition-definitions.html#PlanDefinition.subject[x]): Patient
- [PlanDefinition.action.subject[x]](plandefinition-definitions.html#PlanDefinition.action.subject[x]): Patient
- [Practitioner.active](practitioner-definitions.html#Practitioner.active): This resource is generally assumed to be active if no value is provided for the active element
- [PractitionerRole.active](practitionerrole-definitions.html#PractitionerRole.active): This resource is generally assumed to be active if no value is provided for the active element
- [Questionnaire.item.required](questionnaire-definitions.html#Questionnaire.item.required): Items are generally assumed not to be required unless explicitly specified. Systems SHOULD always populate this value
- [Questionnaire.item.repeats](questionnaire-definitions.html#Questionnaire.item.repeats): Items are generally assumed not to repeat unless explicitly specified. Systems SHOULD always populate this value
- [Questionnaire.item.answerOption.initialSelected](questionnaire-definitions.html#Questionnaire.item.answerOption.initialSelected): Only selected items explicitly marked to be selected
- [RelatedPerson.active](relatedperson-definitions.html#RelatedPerson.active): This resource is generally assumed to be active if no value is provided for the active element
- [RequestGroup.priority](requestgroup-definitions.html#RequestGroup.priority): If missing, this request should be performed with normal priority
- [ResearchDefinition.subject[x]](researchdefinition-definitions.html#ResearchDefinition.subject[x]): Patient
- [ResearchElementDefinition.subject[x]](researchelementdefinition-definitions.html#ResearchElementDefinition.subject[x]): Patient
- [ResearchElementDefinition.characteristic.exclude](researchelementdefinition-definitions.html#ResearchElementDefinition.characteristic.exclude): False
- [Schedule.active](schedule-definitions.html#Schedule.active): This resource is generally assumed to be active if no value is provided for the active element
- [ServiceRequest.priority](servicerequest-definitions.html#ServiceRequest.priority): If missing, this task should be performed with normal priority
- [ServiceRequest.doNotPerform](servicerequest-definitions.html#ServiceRequest.doNotPerform): If missing, the request is a positive request e.g. "do perform"
- [Slot.overbooked](slot-definitions.html#Slot.overbooked): If overbooked is missing, systems may assume that there are still appointments available
- [Substance.instance](substance-definitions.html#Substance.instance): If this element is not present, then the substance resource describes a kind of substance
- [SupplyRequest.priority](supplyrequest-definitions.html#SupplyRequest.priority): If missing, this task should be performed with normal priority
- [Task.priority](task-definitions.html#Task.priority): If missing, this task should be performed with normal priority
- [TestScript.origin.profile](testscript-definitions.html#TestScript.origin.profile): FHIR-Client
- [TestScript.destination.profile](testscript-definitions.html#TestScript.destination.profile): FHIR-Server
- [ValueSet.expansion.offset](valueset-definitions.html#ValueSet.expansion.offset): Paging is not being used
- [ValueSet.expansion.contains.abstract](valueset-definitions.html#ValueSet.expansion.contains.abstract): If this is not populated, systems can assume that the concept it not abstract. This SHALL always be populated for abstract concepts

This specification does not define any default values for resources or data types because:

- The value must be known by all implementations
- When an element has a default value, it can never be unknown - e.g. it is implicitly mandatory
- The default value can never be changed
- The presence of a default value interacts with minimum cardinality and the [:missing search token](search.html#modifiers) in ways that create confusion for implementations

Note that default values can be defined in [Logical Models](structuredefinition.html#logical).

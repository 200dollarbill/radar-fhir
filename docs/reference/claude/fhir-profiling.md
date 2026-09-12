# FHIR R4 — Profiling, StructureDefinition, ElementDefinition, Extensibility, Conformance, ImplementationGuide

Summary: FHIR is a "platform specification" that "usually requires further adaptation to particular contexts of use". Adaptations are expressed as *conformance resources*: StructureDefinition (profiles and extensions), ValueSet, CapabilityStatement, OperationDefinition, SearchParameter, NamingSystem, ConceptMap, CompartmentDefinition, packaged by an ImplementationGuide. `profiling`, `structuredefinition`, `elementdefinition`, `extensibility` and `conformance-rules` are Normative (ANSI-approved); `implementationguide` is Trial Use (maturity 1); `conformance-module` is Informative. Flags used below: `Σ` summary, `?!` modifier, `I` has invariants, `TU` trial use.

## Profile vs base (`profiling` §5.1.0.1, 5.1.0.5–5.1.0.8; `conformance-rules`)
| Term | Definition as printed |
|---|---|
| Implementation Guide (IG) | "A coherent and bounded set of adaptations that are published as a single unit. Validation occurs within the context of the Implementation Guide" |
| Package | "A group of related adaptations that are published as a group within an Implementation Guide" |
| Conformance Resource | "A single resource in a package that makes rules about how an implementation works" |
| Profile | "A set of constraints on a resource represented as a structure definition with kind = `constraint`" (sic — the resource table actually uses `derivation = constraint`; `kind` is primitive-type/complex-type/resource/logical) |
| profiling a resource | "Extending and restricting resources (collectively known as 'profiling a resource') is done with a 'StructureDefinition' resource, which is a statement of rules about how the elements in a resource are used, and where extensions are used in a resource" |
| constraint StructureDefinition | "specifies a set of restrictions on the content of a FHIR resource or data type, or an additional set of constraints on an existing profile"; identified by its canonical URL, "which SHOULD be the URL at which it is published" |

What a profile may state about an element (§5.1.0.8): restrict cardinality (e.g. base 0..\* → 1..2); rule out an element (max = 0); fix a single value; add constraints on nested content; restrict the types of a choice element; require a typed element or reference target to conform to another profile; bind to a different value set; refine definitions/comments/examples; add mappings; declare elements must be 'supported'. "Any changed definitions SHALL be restrictions that are consistent with the rules defined in the resource … from which the profile is derived." Structure definitions "cannot 'remove' mappings and constraints that are defined in the base structure".

Limitations of use (§5.1.0.7): profiles cannot break base rules; cannot specify default values or meanings; cannot give more specific names to elements or add new elements; "It must be safe to process a resource without knowing the profile" → extended behaviour that cannot be ignored must be a modifier extension ("knowledge must be explicit in the instance, not implicit in the profile").

Two uses of profiles (§5.1.0.3): `CapabilityStatement.rest.resource.profile` = general features per resource type; `rest.resource.supportedProfile` = per use case. For any profile declared in `supportedProfile` a producer "SHALL" (1) mark resources with `meta.profile` assertions and (2) if a server, support search by `_profile`; it "SHOULD" publish every instance expected to conform in that form (Trial-Use Note attached).

### Allowed cardinality changes (§5.1.0.6) — derived (across) vs base (down)
| base \ derived | 0..0 | 0..1 | 0..n | 1..1 | 1..n |
|---|---|---|---|---|---|
| 0..1 | yes | yes | no | yes | no |
| 0..\* | yes | yes | yes | yes | yes |
| 1..1 | no | no | no | yes | no |
| 1..\* | no | no | no | yes | yes |

"the constraining profile can only allow what the base profile allows". Narrowing x..\* to x..1 does not change the JSON representation — the element stays an array.

## StructureDefinition — key elements (`structuredefinition` §5.3.4)
Root `StructureDefinition` (IN) is a DomainResource; Normative (from v4.0.0), security category Anonymous. Full table has 35 element rows; the 17 metadata rows not in the table below: `identifier` 0..\* Identifier, `title` 0..1, `experimental` 0..1 boolean, `date` 0..1 dateTime, `publisher` 0..1, `contact` 0..\* ContactDetail, `description` 0..1 markdown, `useContext` 0..\* UsageContext (TU), `jurisdiction` 0..\* CodeableConcept (Extensible), `purpose` 0..1 markdown, `copyright` 0..1 markdown, `keyword` 0..\* Coding (Extensible), `mapping` 0..\* (`identity` 1..1 id, `uri` 0..1, `name` 0..1, `comment` 0..1; sdf-2 name or uri).

| Element | Flags | Card. | Type | Notes |
|---|---|---|---|---|
| `url` | Σ | 1..1 | uri | Canonical identifier (globally unique); "SHALL remain the same when the structure definition is stored on different servers" |
| `version` | Σ | 0..1 | string | Business version |
| `name` | ΣI | 1..1 | string | Computer-friendly; sdf-0 warning `[A-Z]([A-Za-z0-9_]){0,254}` (regex mangled in raw as `'A-Z{0,254}'`) |
| `status` | ?!Σ | 1..1 | code | draft \| active \| retired \| unknown; PublicationStatus (Required) |
| `fhirVersion` | Σ | 0..1 | code | FHIRVersion (Required) |
| `kind` | Σ | 1..1 | code | primitive-type \| complex-type \| resource \| logical; StructureDefinitionKind (Required) |
| `abstract` | Σ | 1..1 | boolean | Whether the structure is abstract |
| `context` | ΣI | 0..\* | BackboneElement | "If an extension, where it can be used in instances" |
| `context.type` | Σ | 1..1 | code | fhirpath \| element \| extension; ExtensionContextType (Required) |
| `context.expression` | Σ | 1..1 | string | Where the extension can be used in instances |
| `contextInvariant` | ΣI | 0..\* | string | FHIRPath invariants — when the extension can be used (sdf-18: extensions only) |
| `type` | ΣI | 1..1 | uri | Type defined or constrained; FHIRDefinedType (Extensible). Tooltip: if derivation is 'specialization' this is the master definition for a type; "Otherwise the structure definition is a constraint on the stated type (and in this case, the type cannot be an abstract type)"; relative to `http://hl7.org/fhir/StructureDefinition` |
| `baseDefinition` | ΣI | 0..1 | canonical(StructureDefinition) | Definition this is constrained/specialized from (sdf-4: required unless abstract) |
| `derivation` | Σ | 0..1 | code | specialization \| constraint; TypeDerivationRule (Required) |
| `snapshot` | I | 0..1 | BackboneElement | Snapshot view; sdf-3, sdf-8, sdf-8b |
| `snapshot.element` | I | 1..\* | ElementDefinition | sdf-10: binding reference or description |
| `differential` | I | 0..1 | BackboneElement | Differential view; sdf-20 no slicing on root, sdf-8a |
| `differential.element` |  | 1..\* | ElementDefinition | |

Bindings (§5.3.4.1, 8 rows): status Required PublicationStatus; jurisdiction Extensible Jurisdiction ValueSet; keyword Extensible DefinitionUseCodes; fhirVersion Required FHIRVersion; kind Required StructureDefinitionKind; context.type Required ExtensionContextType; type Extensible FHIRDefinedType; derivation Required TypeDerivationRule.

### The `kind` / `type` / `baseDefinition` pattern (§5.3.5.1)
| Use | `kind` | `type` | `baseDefinition` | Who may define |
|---|---|---|---|---|
| 1. Base data type (Quantity) | complex-type | — | …/Element | FHIR spec only |
| 2. Constrained data type (Money) | complex-type | Quantity | …/Quantity | anyone |
| 3. Base resource (Patient) | resource | — | …/DomainResource | FHIR spec only |
| 4. Constraint on a resource (clinicaldocument) | resource | Composition | …/Composition | anyone |
| 5. Base Extension | "datatype" (as printed) | — | …/Element | FHIR spec only |
| 6. A defined Extension (data-absent-reason) | complex-type | Extension | …/Extension | anyone |
| 7. Constraint on a defined extension | complex-type | Extension | the extension's canonical (e.g. us-core-race) | anyone |

### StructureDefinition invariants relevant to authoring (§5.3.4.2, 25 rows in raw)
| id | Level | Rule (as printed) |
|---|---|---|
| sdf-1 | Rule | Element paths must be unique unless the structure is a constraint |
| sdf-3 | Rule | Each element definition in a snapshot must have a formal definition and cardinalities |
| sdf-4 | Rule | If the structure is not abstract, then there SHALL be a baseDefinition |
| sdf-5 | Rule | If the structure defines an extension then the structure must have context information (`type != 'Extension' or derivation = 'specialization' or context.exists()`) |
| sdf-6 | Rule | A structure must have either a differential, or a snapshot (or both) |
| sdf-8 / sdf-8a | Rule | All snapshot / differential elements must start with the StructureDefinition's specified type |
| sdf-8b | Rule | All snapshot elements must have a base definition |
| sdf-9 | Rule | No label, code or requirements on the root element |
| sdf-10 | Rule | snapshot.element: provide either a binding reference or a description (or both) |
| sdf-11 | Rule | If there's a type, its content must match the path name in the first element of a snapshot |
| sdf-14 / 16 / 17 | Rule | All element definitions must have an id; ids unique in snapshot; unique in differential |
| sdf-15 / 15a | Rule | First element of snapshot / differential has no type (unless logical model) |
| sdf-18 | Rule | Context Invariants can only be used for extensions |
| sdf-20 | Rule | differential: No slicing on the root element |
| sdf-21 | Rule | Default values can only be specified on specializations |
| sdf-23 | Rule | No slice name on root |
Not repeated: sdf-0 (warning, name), sdf-2 (mapping), sdf-19 and sdf-22 (FHIR-spec-only models).

### Differential vs snapshot (`profiling` §5.1.0.9; `structuredefinition` §5.3.5)
| View | Rule |
|---|---|
| differential | "describe only the differences … relative to the structure definition they constrain"; may be sparse; the root element is not needed; elements listed only when rules are made about them; order must follow the base (depth-first; unsliced descendants before slices) |
| snapshot | "a fully calculated form of the structure that is not dependent on any other structure"; "StructureDefinition resources used in operational systems should always have the snapshot view populated"; min/max always required (eld rules §2.30.0.4.3) |
| both | "the most useful form - the differential form serves the authoring process, while the snapshot serves the implementation tooling" |

Path/structure rules (§5.3.5, `elementdefinition` §2.30.0.2–3): flat list, nesting derived from `path`; choice elements end in `[x]` and when only one type is left in a profile "the name of the element is changed to include the type instead of '[x]'" (capitalise the type: `effectiveDateTime`); constraint profiles "are not allowed to define or include ElementDefinitions with a path not defined within the base type"; every ElementDefinition SHALL have an `id` built as `pathpart:slicename/reslicename` per token (e.g. `Patient.deceased[x]:deceasedBoolean`).

## ElementDefinition — constraints usable in a profile (`elementdefinition` §2.30.0.1, 2.30.0.4)
ElementDefinition (ΣIN, BackboneElement) is Normative. The full table has 82 element rows (18 of them `minValue*`/`maxValue*` type rows); below are the elements a constraint profile may set. Column "Constraint def." is from the printed context table (first element / following elements): † "presence, and value, must match the … base definition"; ‡ "must be consistent with" the base; ∆ additional ones allowed, they "do not replace the ones in the base definition".

| Element | Card. | Type | Constraint def. (1st / following) | Notes and invariants |
|---|---|---|---|---|
| `path` | 1..1 | string | required | eld-19 no special characters; eld-20 warning ≤64 alphanumerics |
| `sliceName` | 0..1 | string | prohibited / "required for slices, else prohibited" | eld-16 tokens separated by "/" |
| `sliceIsConstraining` (TU) | 0..1 | boolean | — | eld-22 only with sliceName |
| `label` | 0..1 | string | recommended / recommended | display name |
| `code` | 0..\* | Coding | optional / optional | LOINC Codes (Example) |
| `slicing` | 0..1 | Element | prohibited / optional | eld-1: no discriminators → description required; `slicing.discriminator` 0..\* |
| `slicing.discriminator.type` | 1..1 | code | | value \| exists \| pattern \| type \| profile; DiscriminatorType (Required) |
| `slicing.discriminator.path` | 1..1 | string | | restricted FHIRPath to the element |
| `slicing.description` | 0..1 | string | | |
| `slicing.ordered` | 0..1 | boolean | | missing = "Order is not required unless specified" |
| `slicing.rules` | 1..1 | code | | closed \| open \| openAtEnd; SlicingRules (Required) |
| `short` / `definition` | 0..1 | string / markdown | required‡ | definition "SHALL be consistent with the base definition, but convey the meaning of the element in the particular context of use" |
| `comment` / `requirements` / `alias` | 0..1 / 0..1 / 0..\* | markdown / markdown / string | prohibited‡ / optional‡ | |
| `min` | 0..1 | unsignedInt | optional / optional† | eld-2 Min <= Max; in a differential "if they are not present, they default to the min and max from the base" |
| `max` | 0..1 | string | optional / optional† | eld-3 "Max SHALL be a number or '\*'" |
| `base` (path/min/max) | 0..1 | Element | required / required | base cardinality for tools |
| `contentReference` | 0..1 | uri | prohibited / optional ("nameReference" in the printed table) | eld-5: excludes type, fixed, pattern, binding, … |
| `type` | 0..\* | Element | optional / optional | eld-13 unique by code; limiting the type list must be applied to the `[x]` element; a type-specific path "SHALL NOT be interpreted as constraining allowed types" |
| `type.code` | 1..1 | uri | | FHIRDefinedType (Extensible); relative to `http://hl7.org/fhir/StructureDefinition` |
| `type.profile` | 0..\* | canonical(StructureDefinition \| ImplementationGuide) | | "Profiles (StructureDefinition or IG) - one must apply" |
| `type.targetProfile` | 0..\* | canonical(StructureDefinition \| ImplementationGuide) | | on the Reference/canonical target; eld-17 only for Reference or canonical |
| `type.aggregation` | 0..\* | code | | contained \| referenced \| bundled; eld-4 only for reference types |
| `type.versioning` | 0..1 | code | | either \| independent \| specific |
| `defaultValue[x]` / `meaningWhenMissing` | 0..1 | \* / markdown | prohibited / optional† | eld-15 mutually exclusive; sdf-21: defaults only on specializations |
| `fixed[x]` | 0..1 | \* | prohibited / optional | "a value that SHALL be exactly the value for this element in the instance … non-significant whitespace is ignored … exact match (case and accent sensitive). Missing elements/attributes must also be missing"; eld-6 one type only; eld-8 not with pattern |
| `pattern[x]` | 0..1 | \* | prohibited / optional | "a value that the value in the instance SHALL follow - that is, any value in the pattern must be found in the instance. Other additional values may be found too"; primitive → exact match; array → each pattern element matches at least one instance element; complex → each property present and recursively matching; eld-7 one type only |
| `example` (label 1..1, value[x] 1..1) | 0..\* | Element | prohibited / optional | |
| `minValue[x]` / `maxValue[x]` | 0..1 | date, dateTime, instant, time, decimal, integer, positiveInt, unsignedInt, Quantity | prohibited / optional | inclusive |
| `maxLength` | 0..1 | integer | prohibited / optional | for strings |
| `condition` | 0..\* | id | prohibited / optional∆ | reference to invariant about presence |
| `constraint` | 0..\* | Element | optional∆ / optional∆ | `key` 1..1 id, `requirements` 0..1, `severity` 1..1 error \| warning, `human` 1..1, `expression` 0..1 FHIRPath, `xpath` 0..1 (TU), `source` 0..1 canonical; eld-14 unique keys; eld-21 warning without expression |
| `mustSupport` | 0..1 | boolean | optional / optional | in a profile, if absent "the mustSupport value is not changed fro[m] the base definition"; snapshot SHOULD populate it |
| `isModifier` / `isModifierReason` | 0..1 | boolean / string | prohibited / optional† | eld-18 reason required when true; cannot be changed by profiles (`conformance-rules`) |
| `isSummary` | 0..1 | boolean | prohibited / optional† | |
| `binding` | 0..1 | Element | prohibited / optional | eld-11 only for code, Coding, CodeableConcept, Quantity, string, uri |
| `binding.strength` | 1..1 | code | | required \| extensible \| preferred \| example; BindingStrength (Required) |
| `binding.description` | 0..1 | string | | |
| `binding.valueSet` | 0..1 | canonical(ValueSet) | | eld-12 SHALL start with http:// https:// or urn: |
| `mapping` (identity 1..1, language 0..1, map 1..1, comment 0..1) | 0..\* | Element | optional∆ / optional∆ | |
Not listed: `representation` 0..\* code (xmlAttr \| xmlText \| typeAttr \| cdaText \| xhtml), `orderMeaning` 0..1 string.

## Slicing (`profiling` §5.1.0.10–5.1.0.14; `elementdefinition` §2.30.0.4.1)
Slicing splits a repeating element (or a choice of types) into named sub-lists ("slices"); slice names "are never exchanged". Discriminator = pair (type, restricted FHIRPath: element selections, `extension(url)`, `resolve()`, `ofType()`).

| Discriminator type | Definition as printed | Typical use note |
|---|---|---|
| value | "The slices have different values in the nominated element." | most common; mostly primitives `code`, `uri` (e.g. `Patient.telecom.system`) |
| exists | "The slices are differentiated by the presence or absence of the nominated element." | adjunct only — "not much discrimination power" |
| pattern | "The slices have different values in the nominated element, as determined by testing them against the applicable ElementDefinition.pattern[x]." | mostly `CodeableConcept` (e.g. `Observation.code` LOINC codes) |
| type | "The slices are differentiated by type of the nominated element." | polymorphic elements or reference targets (`List.item.resolve()`) |
| profile | "The slices are differentiated by conformance of the nominated element to a specified profile." | hardest, ">1000-fold" processing; "only where absolutely required" |

Rules:
- Discriminated values "SHALL" be "different and non-overlapping"; the *composite* of discriminator values is unique. For `value`/`pattern` the slice's element must use `fixed[x]`, `pattern[x]`, or a required binding to an extensional value set. Omitting discriminators is allowed but "discouraged".
- Slice group: initiated by a "slicing entry" (first element with `slicing`, also the unconstrained definition); mutually exclusive ("SHALL describe a distinct set of values"); serialized adjacently. "Slicing is only allowed when constraining an existing structure"; `slicing` only on the first repetition; "All elements following the first repeat … SHALL have a `sliceName`"; the entry's `min` "governs the number of total occurrences of the sliced element".
- Slice cardinality (m..n sliced): no slice may exceed the max; sum of maxima may exceed n; sum of minima ≤ n; a slice may have min 0 but the instance total must still be ≥ m.
- Default slice `@default`: reserved name; only when `slicing.rules = closed`; must not fix discriminator values; may be re-sliced.
- Re-profiling: `rules` may go `open` → `closed`; `ordered` `false` → `true`; child profiles "SHALL include all the same discriminators" and "MAY add additional discriminators"; re-slicing names use `/` (`example/example1`). "extensions are always sliced by the `url` element".
- Discriminator examples printed (7 rows): `List.entry` value `item.resolve().name`; type `item.resolve()`; profile `item.resolve()`; value `item.extension('…').value`; `List.entry.extension` value `url`; type+value `item.resolve(), item.resolve().value`; `Observation.value[x]` type `$this`.

## Extensions (`extensibility`; `structuredefinition` §5.3.5.1; `profiling` §5.1.0.15)
Extension element (Normative): `url` 1..1 uri "identifies the meaning of the extension"; `value[x]` 0..1 of 50 listed types (primitives, general-purpose types, Reference, metadata types, Dosage, Meta); nested `extension`. Rule: "Must have either extensions or value[x], not both".

| Rule (as printed) |
|---|
| "The `url` SHALL be a URL, not a URN … and it SHALL be the canonical URL of a StructureDefinition that defines the extension. Except for child extensions defined within complex extensions, the URL SHALL be an absolute URL" |
| Definitions "SHOULD be available to consumers" — resolvable canonical URL and/or a registry |
| "An extension SHALL have either a value (i.e. a value[x] element) or sub-extensions, but not both. If present, the value[x] element SHALL have content" |
| `valueCode` only "if the extension definition provides a fixed binding to a suitable set of codes" |
| "If it is not safe for an application processing the content of the resource to ignore the extension it SHALL be represented using a Modifier Extension" |
| Complex extensions: child identity is local/relative (`url = "code"`, `"period"`); a foreign extension inside uses its own absolute URL |

Where extensions can appear: "Every element in a resource or data type includes an optional 'extension' child element that may be present any number of times"; a few resources not specialising DomainResource have no root extensions. Modifier extensions: allowed "at the base of a resource or in any elements that do not have a data type … and on a few specially selected data types"; "Other data types and elements inside data types SHALL NOT have modifier extensions, and extensions SHALL NOT have modifier extensions internally"; "Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource".

Defining an extension: a StructureDefinition with `kind = complex-type`, `type = Extension`, `baseDefinition = http://hl7.org/fhir/StructureDefinition/Extension` (§5.3.5.1 example 6) plus `context` (sdf-5; `context.type` fhirpath \| element \| extension, `context.expression`); elements have path `Extension`, then `Extension.value[x]` or `Extension.extension` for complex extensions (`elementdefinition` context table). The definition "defines the URL … and the context where the extension can be used (usually a particular path or a data type)"; one definition can be reused on several resources. Using it in a profile = slice the `extension` list; "the minimum cardinality of an extension SHALL be a valid restriction on the minimum cardinality in the definition of the extension" — recommended definition min is 0.

Modifier-extension conformance (§2.5.0.2.1): SHALL only modify the containing element and/or its children; SHALL be represented in the narrative; applications SHALL ensure unrecognised modifier extensions are not present when processing; if present and not understood, SHALL refuse to process or SHALL warn users. Processing options when one is found: recognise it; reject (e.g. "HTTP 422 status code with an OperationOutcome"); treat as rendering-only; ask a human; carry a warning. Servers "that simply move whole resources around unchanged are not 'processing the data'". Exchange rules (§2.5.0.3): SHOULD retain unknown extensions; a modifying system SHOULD remove extensions it does not understand from the modified element; "A system SHALL NOT modify a resource or element that contains 'modifier' extensions it doesn't understand"; SHOULD ignore unknown non-modifier extensions. Missing mandatory data: `http://hl7.org/fhir/StructureDefinition/data-absent-reason` on a primitive with no value (not a modifier); inventing a value is "not valid".

## Binding strengths (`elementdefinition`, `structuredefinition` tooltips; `profiling` §5.1.0.16–18)
| Strength | Definition as printed |
|---|---|
| required | "To be conformant, the concept in this element SHALL be from the specified value set." |
| extensible | "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated. If the value set does not cover the concept (based on human review), alternate codings (or, data type allowing, text) may be included instead." |
| preferred | "Instances are encouraged to draw from the specified codes for interoperability purposes but are not required to do so to be considered conformant." (tooltip printed in `valueset` / `codesystem` tables, not in the profiling pages) |
| example | "Instances are not expected or even encouraged to draw from the specified value set. The value set merely provides examples of the types of concepts intended to be included." |

Value-set customisation in profiles (§5.1.0.17): base required → "can only contain codes contained in the value set specified by the FHIR specification"; base extensible → may add codes that "SHOULD NOT have the same meaning as existing codes"; base preferred or example → "whatever is appropriate for local use". A profile "cannot make codes valid that are invalid in the base profile".

Allowed strength changes (§5.1.0.18, derived across / base down): required → required only; extensible → required, extensible; preferred → required, extensible, preferred; example → any of the four.

## Must Support (`profiling` §5.1.0.19; `conformance-rules` §2.1.0.5)
"If true, it means that systems claiming to conform to a given profile must 'support' the element. This is distinct from cardinality." The base spec never sets it; a profile that sets it "SHALL also make clear exactly what kind of 'support' is required" in `ElementDefinition.definition`, `StructureDefinition.description` or IG documentation (examples: store and retrieve; display/capture; appear in a report; used in decision support). Derived profiles may change false → true, never true → false. IsModifier does not imply mustSupport.

## Conformance verbs and properties (`conformance-rules` §2.1.0.1–2.1.0.6)
| Verb | Definition as printed |
|---|---|
| SHALL | "an absolute requirement for all implementations" |
| SHALL NOT | "an absolute prohibition against inclusion for all implementations" |
| SHOULD/SHOULD NOT | "A best practice or recommendation to be considered by implementers within the context of their particular implementation; there may be valid reasons to ignore an item, but the full implications must be understood and carefully weighed before choosing a different course" |
| MAY | "This is truly optional language for an implementation; can be included or omitted as the implementer decides with no implications" |

Frameworks a system claims conformance to: "RESTful FHIR", "FHIR messaging", "FHIR documents". "Systems can only claim FHIR Conformance for functionality described in the applicable CapabilityStatement." FHIR is a "*closed* specification" — extensions beyond it "cannot be considered or described as 'FHIR conformant'".

| Property | Rules as printed |
|---|---|
| Cardinality | base uses only 0..1, 0..\*, 1..1, 1..\*; profiles may use other values within base limits; present elements "SHALL have a value attribute, child elements, or extensions" (min 1 does not guarantee data — FHIRPath constraints do); order of repeats has no meaning unless `orderMeaning` says so (cannot be defined in a profile) |
| Is-Modifier | "an element is a modifier if and only if it cannot be safely ignored because its value, or its meaning if missing, may cause the interpretation of the containing element or one of its descendants to no longer conform"; "cannot be changed when element usage is described in a constraining Structure Definition" (either direction); processors "SHALL understand the impact"; if narrative `status = generated`, modifier elements SHALL be in the narrative |
| MustSupport | see above |
| Constraints | key, requirements, severity, human, expression (FHIRPath), xpath; severities: **Error (rule)** — "A rule that all resources must conform to"; **Warning** — valid but "there may be a problem"; **Guideline** — warning with `elementdefinition-bestpractice` extension, error when best practice is enforced. Profiles "may define additional constraints … but they cannot alter or remove constraints that are already applied"; systems "SHOULD always ensure that all resources are valid against all applicable constraints" |

Conformance Module (`conformance-module`): conformance resources = CapabilityStatement, StructureDefinition, OperationDefinition, SearchParameter, CompartmentDefinition, ImplementationGuide, ElementDefinition (datatype) plus MessageDefinition; normative = StructureDefinition, ValueSet; CapabilityStatement partly TU; ImplementationGuide and CompartmentDefinition "still under development". Security notes: invariants are executable expressions (sandbox them); uploaded SearchParameters/compartments may be expensive or expose data; a conformance repository "should tightly control modifications".

## ImplementationGuide — how it packages profiles (`implementationguide` §5.8)
"A set of rules of how a particular interoperability or standards problem is solved … used to gather all the parts of an implementation guide into a logical whole and to publish a computable definition of all the parts." Contains two reference kinds: **Contents** ("almost always conformance resources") and **Examples**. Validators use it "to validate content against the implementation guide as a whole". Distributed "through the FHIR Package distribution system".

| Element | Flags | Card. | Type | Notes |
|---|---|---|---|---|
| `url` | Σ | 1..1 | uri | canonical, globally unique |
| `version` | Σ | 0..1 | string | |
| `name` | ΣI | 1..1 | string | ig-0 warning name regex |
| `title` | Σ | 0..1 | string | |
| `status` | ?!Σ | 1..1 | code | draft \| active \| retired \| unknown (Required) |
| `experimental`, `date`, `publisher`, `contact`, `description`, `useContext`, `jurisdiction`, `copyright` | Σ (mostly) | 0..1 / 0..\* | as StructureDefinition | metadata |
| `packageId` | Σ | 1..1 | id | "NPM Package name for IG" |
| `license` | Σ | 0..1 | code | SPDXLicense (Required, new SPDX ids allowed) |
| `fhirVersion` | Σ | 1..\* | code | FHIRVersion (Required); e.g. `["3.0", "4.0"]` — patch omitted |
| `dependsOn` (`uri` 1..1 canonical(IG), `packageId` 0..1, `version` 0..1) | Σ | 0..\* | BackboneElement | other IGs |
| `global` (`type` 1..1 code ResourceType, `profile` 1..1 canonical(StructureDefinition)) | Σ | 0..\* | BackboneElement | default profiles: "apply to any resource that does not otherwise have an explicit profile assigned"; must also be in `resource` |
| `definition` | I | 0..1 | BackboneElement | ig-1 groupingId must exist |
| `definition.grouping` (`name` 1..1, `description` 0..1) |  | 0..\* | BackboneElement | |
| `definition.resource` |  | 1..\* | BackboneElement | `reference` 1..1 Reference(Any); `fhirVersion` 0..\* code (ig-2); `name` 0..1; `description` 0..1; `exampleBoolean` / `exampleCanonical(StructureDefinition)` 0..1; `groupingId` 0..1 |
| `definition.page` (`nameUrl`/`nameReference(Binary)` 1..1, `title` 1..1, `generation` 1..1 html \| markdown \| xml \| generated, nested `page`) |  | 0..1 | BackboneElement | |
| `definition.parameter` (`code` 1..1 apply \| path-resource \| path-pages \| path-tx-cache \| expansion-parameter \| rule-broken-links \| generate-xml \| generate-json \| generate-turtle \| html-template, `value` 1..1) |  | 0..\* | BackboneElement | build parameters |
| `definition.template` (`code`, `source` 1..1, `scope` 0..1) |  | 0..\* | BackboneElement | |
| `manifest` |  | 0..1 | BackboneElement | assembled IG: `rendering` 0..1 url; `resource` 1..\* (`reference` 1..1, `example[x]`, `relativePath`); `page` 0..\* (`name` 1..1, `title`, `anchor`); `image`, `other` 0..\* string |

## Steps to define a new Device profile (checklist derived only from the pages above)
1. Create a StructureDefinition with `url` (canonical, 1..1 — the URL it is published at, `profiling` §5.1.0.8), `name` 1..1, `status` 1..1, `kind = resource`, `abstract = false`, `type = Device`, `baseDefinition = http://hl7.org/fhir/StructureDefinition/Device`, `derivation = constraint` (`structuredefinition` §5.3.5.1 example 4, sdf-4); optionally `fhirVersion` (FHIRVersion code), `version`, `publisher`, `description` (§5.3.3.1).
2. Author a `differential` listing only the elements you constrain; root element not needed; keep base order; `differential.element` 1..\* (`profiling` §5.1.0.9; `structuredefinition` §5.3.5). Every element needs `path` and an `id` built as `path:slicename` (`elementdefinition` §2.30.0.3, sdf-14).
3. Only use paths that exist in base Device — no new elements, no renaming (`profiling` §5.1.0.7; `elementdefinition` §2.30.0.2).
4. Tighten cardinality only within the base table (`profiling` §5.1.0.6): 0..1 → 1..1 or 0..0; 0..\* → 0..1, 1..1, 1..\*, 0..0. `max` is a string, a number or `*` (eld-3).
5. Fix or pattern values with one type only (eld-6/7), never both (eld-8): `fixed[x]` for exact match, `pattern[x]` for "at least these property values" (`elementdefinition` table).
6. Bindings: allowed only on code/Coding/CodeableConcept/Quantity/string/uri (eld-11); `binding.valueSet` canonical starting `http://`, `https://` or `urn:` (eld-12); strength may only tighten per the §5.1.0.18 table, and a required base value set may only be narrowed (§5.1.0.17).
7. Restrict reference targets with `type.targetProfile` on Reference elements (eld-17) or add `type.profile` for a typed element (`elementdefinition` table).
8. For repeating elements (e.g. `identifier`, `deviceName`, `property`) slice: first entry carries `slicing.discriminator` (type + path), `slicing.rules`, optional `ordered`/`description`; each following entry has `sliceName`; `value`/`pattern` discriminators need `fixed[x]`, `pattern[x]`, or an extensional required binding; keep slice mins summing ≤ base max (`profiling` §5.1.0.11–12; `elementdefinition` §2.30.0.4.1; eld-1).
9. Extra data not in Device: define a separate StructureDefinition with `kind = complex-type`, `type = Extension`, `baseDefinition = …/Extension`, `context` (sdf-5), absolute canonical `url`, `Extension.value[x]` of one listed type or sub-extensions (`extensibility` §2.5.0.1); then slice `Device.extension` on `url` in the profile with min ≥ the extension's own min (`profiling` §5.1.0.15). If ignoring it is unsafe, it must be a modifier extension (`extensibility` §2.5.0.2).
10. Mark `mustSupport = true` where needed and state in `definition`/`description` what "support" means (`profiling` §5.1.0.19; `conformance-rules` §2.1.0.5). Do not change `isModifier` (`conformance-rules` §2.1.0.4).
11. Add extra invariants as `constraint` (`key`, `severity`, `human`, `expression`); base constraints cannot be removed (`conformance-rules` §2.1.0.6; eld-14, eld-21).
12. Generate the `snapshot` (every element with definition, min, max, base; sdf-3, sdf-8b) — operational systems "should always have the snapshot view populated" (`profiling` §5.1.0.9).
13. Package: add the profile (and extension) to `ImplementationGuide.definition.resource`, set `packageId`, `fhirVersion`, `dependsOn`, optionally `global` (`implementationguide` §5.8.3); declare it in `CapabilityStatement.rest.resource.supportedProfile`, stamp instances with `meta.profile`, and support `_profile` search (`profiling` §5.1.0.3.2).

## Notes for our server
- Store profiles as StructureDefinition resources with both differential and snapshot; validate incoming Device / Observation instances against `meta.profile` canonicals, walking the snapshot (min/max, fixed/pattern, binding strength, slicing by discriminator, `constraint.expression`).
- Reject unknown modifier extensions with `422` + OperationOutcome (`extensibility` §2.5.0.2 option 2); keep unknown non-modifier extensions on store, and remove not-understood extensions only from elements we modify.
- The SATUSEHAT profiles (see satusehat-*.md) are constraint StructureDefinitions on R4 resources; our device profile derives from base Device, and a later SATUSEHAT-conformant Observation profile may derive from the vital-signs profile — check the §5.1.0.6 / §5.1.0.18 tables before every tightening.
- Publish `GET [base]/metadata` with `rest.resource.supportedProfile` for each profile, and index `_profile`.
- `elementdefinition` scrape mangled several link tooltips into the Name column (e.g. `slicing.`, `definition,`, `short.")`); element names were recovered from the XML template — no cardinalities were affected. sdf-0/ig-0 regex printed as `'A-Z{0,254}'` (brackets lost).

## Sources
- raw/fhir-r4/profiling.md
- raw/fhir-r4/structuredefinition.md
- raw/fhir-r4/elementdefinition.md
- raw/fhir-r4/extensibility.md
- raw/fhir-r4/conformance-rules.md
- raw/fhir-r4/conformance-module.md
- raw/fhir-r4/implementationguide.md
- raw/fhir-r4/valueset.md

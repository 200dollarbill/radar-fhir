# FHIR R4 — ValueSet, CodeSystem

Purpose: `CodeSystem` "declares the existence of and describes a code system or code system supplement and its key properties, and optionally defines a part or all of its content" (also known as Ontology, Terminology, or Enumeration). `ValueSet` "specifies a set of codes drawn from one or more code systems, intended for use in a particular context. Value sets link between CodeSystem definitions and their use in coded elements." Both are Normative (from v4.0.0), Vocabulary Work Group, security category Anonymous, no compartments. "proper differentiation between a code system and a value set is important. This is one very common area where significant clinical safety risks occur in practice." Flags: `Σ` summary, `?!` modifier, `I` invariants, `TU` trial use.

## Identification (both pages)
| Identifier | Rule |
|---|---|
| `.id` | logical id on the holding server; changes as the resource moves; with the server address = the 'literal identity' |
| `.url` | "the canonical URL that never changes … it is the same in every copy"; named `url` "to strongly encourage providing a resolvable URL"; "most references … use the canonical URL"; for CodeSystem this is the value used in `Coding.system` |
| `.identifier` | system/value pair for other contexts (e.g. an OID in HL7 v3); "generally not needed … in a FHIR context" |
| `ValueSet.expansion.identifier` | uniquely identifies each expansion |

Intensional value set = algorithmically defined (a rule, dynamically updated); extensional = enumerated list of codes (more control, more maintenance).

## ValueSet — elements (`valueset` §4.9.4; 59 element rows in raw, all listed (7 `value[x]` type rows collapsed))
Root `ValueSet` (IN) is a DomainResource; vsd-0 warning on `name`.

| Element | Flags | Card. | Type | Notes |
|---|---|---|---|---|
| `url` | Σ | 0..1 | uri | Canonical identifier; "SHALL remain the same when the value set is stored on different servers" |
| `identifier` | Σ | 0..\* | Identifier | business identifier |
| `version` | Σ | 0..1 | string | Business version |
| `name` | ΣI | 0..1 | string | computer friendly |
| `title` | Σ | 0..1 | string | human friendly |
| `status` | ?!Σ | 1..1 | code | draft \| active \| retired \| unknown; PublicationStatus (Required); "Expansions do not have a state" |
| `experimental` | Σ | 0..1 | boolean | |
| `date` | Σ | 0..1 | dateTime | Date last changed |
| `publisher` | Σ | 0..1 | string | |
| `contact` | Σ | 0..\* | ContactDetail | |
| `description` |  | 0..1 | markdown | |
| `useContext` | ΣTU | 0..\* | UsageContext | |
| `jurisdiction` | Σ | 0..\* | CodeableConcept | Jurisdiction (Extensible) |
| `immutable` | Σ | 0..1 | boolean | "whether or not any change to the content logical definition may occur" |
| `purpose` |  | 0..1 | markdown | |
| `copyright` |  | 0..1 | markdown | |
| `compose` |  | 0..1 | BackboneElement | Content logical definition (CLD) |
| `compose.lockedDate` | Σ | 0..1 | date | Fixed date for references with no specified version (transitive) |
| `compose.inactive` | Σ | 0..1 | boolean | Whether inactive codes are in the value set |
| `compose.include` | ΣI | 1..\* | BackboneElement | vsd-1, vsd-2, vsd-3 |
| `compose.include.system` | ΣI | 0..1 | uri | The system the codes come from |
| `compose.include.version` | Σ | 0..1 | string | Specific code-system version |
| `compose.include.concept` | I | 0..\* | BackboneElement | A concept defined in the system |
| `compose.include.concept.code` |  | 1..1 | code | Code or expression from system |
| `compose.include.concept.display` |  | 0..1 | string | display for this code "in this valueset" |
| `compose.include.concept.designation` |  | 0..\* | BackboneElement | |
| `….designation.language` |  | 0..1 | code | Common Languages (Preferred but limited to AllLanguages) |
| `….designation.use` |  | 0..1 | Coding | Designation Use (Extensible) |
| `….designation.value` |  | 1..1 | string | |
| `compose.include.filter` | ΣI | 0..\* | BackboneElement | "If multiple filters are specified, they SHALL all be true" |
| `compose.include.filter.property` | Σ | 1..1 | code | A property/filter defined by the code system |
| `compose.include.filter.op` | Σ | 1..1 | code | = \| is-a \| descendent-of \| is-not-a \| regex \| in \| not-in \| generalizes \| exists; FilterOperator (Required) |
| `compose.include.filter.value` | Σ | 1..1 | string | code, regex, or boolean for exists |
| `compose.include.valueSet` | ΣI | 0..\* | canonical(ValueSet) | absolute URI = `ValueSet.url`; multiple → union of their contents |
| `compose.exclude` | I | 0..\* | see include | codes in exclude statements "are never in the value set" |
| `expansion` |  | 0..1 | BackboneElement | Used when the value set is "expanded" |
| `expansion.identifier` |  | 0..1 | uri | business identifier of the expansion |
| `expansion.timestamp` |  | 1..1 | dateTime | Time expansion happened |
| `expansion.total` |  | 0..1 | integer | Total number of codes in the expansion |
| `expansion.offset` |  | 0..1 | integer | missing = "Paging is not being used" |
| `expansion.parameter` |  | 0..\* | BackboneElement | Parameter that controlled the expansion |
| `expansion.parameter.name` |  | 1..1 | string | |
| `expansion.parameter.value[x]` |  | 0..1 | string \| boolean \| integer \| decimal \| uri \| code \| dateTime | (7 type rows) |
| `expansion.contains` | I | 0..\* | BackboneElement | vsd-6, vsd-9, vsd-10 |
| `expansion.contains.system` |  | 0..1 | uri | |
| `expansion.contains.abstract` |  | 0..1 | boolean | "If user cannot select this entry"; SHALL be populated for abstract concepts |
| `expansion.contains.inactive` |  | 0..1 | boolean | |
| `expansion.contains.version` |  | 0..1 | string | |
| `expansion.contains.code` | I | 0..1 | code | "if blank, this is not a selectable code" |
| `expansion.contains.display` | I | 0..1 | string | |
| `expansion.contains.designation` |  | 0..\* | see designation | |
| `expansion.contains.contains` |  | 0..\* | see contains | nested codes |

Bindings (5): status Required PublicationStatus; jurisdiction Extensible; designation.language "Preferred, but limited to AllLanguages" CommonLanguages; designation.use Extensible DesignationUse; filter.op Required FilterOperator.

### ValueSet invariants (7 rows)
| id | Level | Location | Rule | Expression |
|---|---|---|---|---|
| vsd-0 | Warning | (base) | Name should be usable as an identifier … code generation | `name.matches('A-Z{0,254}')` (brackets lost in scrape) |
| vsd-1 | Rule | compose.include | A value set include/exclude SHALL have a value set or a system | `valueSet.exists() or system.exists()` |
| vsd-2 | Rule | compose.include | A value set with concepts or filters SHALL include a system | `(concept.exists() or filter.exists()) implies system.exists()` |
| vsd-3 | Rule | compose.include | Cannot have both concept and filter | `concept.empty() or filter.empty()` |
| vsd-6 | Rule | expansion.contains | SHALL have a code or a display | `code.exists() or display.exists()` |
| vsd-9 | Rule | expansion.contains | Must have a code if not abstract | `code.exists() or abstract = true` |
| vsd-10 | Rule | expansion.contains | Must have a system if a code is present | `code.empty() or system.exists()` |

### Composition rules (§4.9.5)
| Case | Result |
|---|---|
| multiple `include` | cumulative — union |
| within one `include` | all criteria apply — intersection; one system with criteria and/or one or more value sets |
| `valueSet`(s) only | codes selected if "in all the referenced value sets" |
| `system` only, no `concept`/`filter` | all codes in the system |
| `system` + `concept` | only the enumerated codes |
| `system` + `filter` | codes meeting the filter criteria (only where the code system defines the properties) |
| `valueSet` + `system` | selected by the system selection *and* in all referenced value sets |
| non-version-specific system + filters | contents "are open and change over time" |
| `version = '*'` | codes from all versions (Implementation Note: subject to future clarification) |
| `exclude` | same interpretation as include; "Any compose.exclude SHALL be processed such that excluded codes are not found in the expansion" |
| abstract codes | may be included (enumerated or by filter) — grouping/searching only |

Display rules (§4.9.6): if no `display` in the value set, the code system display is used ("the preferred approach, because overriding the display can lead to very unsafe outcomes"); a value-set display goes to the expansion for pick lists, but "The display in the Coding that results from a user selecting a concept from the expansion must be taken from the underlying code system definition" — the alternative display belongs in `CodeableConcept.text`; the correct display "can be determined by a $lookup operation". `display` = designation with implied use "primary code" and the resource language.

### Expansion (§4.9.8)
Process: if a stored expansion exists, check parameters are consistent (else regenerate, or error if no `.compose`); otherwise for each `compose.include`: (1) system → pick the version; no codes/filters → every code; listed codes → check validity and active status; filters → process in order, add the intersection; (2) each `valueSet` → expand recursively (`GET [base]/ValueSet/$expand?url=[compose.include.valueSet]` — printed as `$expand$url=`); (3) add the intersection of system and value-set result sets; then apply `compose.exclude` the same way, removing codes. Rules: expansion MAY be hierarchical (navigational only — "cannot be used for logical inferencing"; grouping entries have no system/code and "must be marked as abstract"); a concept appears once in a flat expansion (uniqueness by system/version/code); codes "should be treated as case sensitive"; canonical URL of an expansion = the value set's; "Each expansion SHALL have a unique identifier in `ValueSet.expansion.identifier`" (a reused identifier means an identical canonical representation); `expansion.parameter` SHOULD list all parameters affecting `$expand`, SHALL if persisted, SHALL include the code-system version when the server's code system has one; when paging, `offset` and `count` SHALL be populated; `[canonical]#CodeSystem.content` and `[canonical1]#supplement` parameters SHALL be recorded when a fragment/supplement was used.

Predefined `$expand` parameters (16): `filter`, `date`, `offset`, `count` (0 = ask for size), `includeDesignations`, `designation`, `includeDefinition`, `activeOnly`, `excludeNested`, `excludeNotForUI`, `excludePostCoordinated`, `displayLanguage`, `exclude-system`, `system-version`, `check-system-version`, `force-system-version` (`[system]|[version]` format for the last four). `.compose`/`.expansion` combinations (§4.9.9): compose only = the publisher's definition; expansion only = `$expand` output at server discretion; both = common `$expand` output; neither = valid, e.g. `_summary=true` result.

### ValueSet search parameters (18, all TU)
| Name | Type | Expression |
|---|---|---|
| code | token | `ValueSet.expansion.contains.code \| ValueSet.compose.include.concept.code` ("extremely onerous for a server"; support level declared in TerminologyCapabilities) |
| context | token | `(ValueSet.useContext.value as CodeableConcept)` |
| context-quantity | quantity | `(ValueSet.useContext.value as Quantity) \| (ValueSet.useContext.value as Range)` |
| context-type | token | `ValueSet.useContext.code` |
| context-type-quantity | composite | on `ValueSet.useContext`: context-type + context-quantity |
| context-type-value | composite | on `ValueSet.useContext`: context-type + context |
| date | date | `ValueSet.date` |
| description | string | `ValueSet.description` |
| expansion | uri | `ValueSet.expansion.identifier` |
| identifier | token | `ValueSet.identifier` |
| jurisdiction | token | `ValueSet.jurisdiction` |
| name | string | `ValueSet.name` |
| publisher | string | `ValueSet.publisher` |
| reference | uri | `ValueSet.compose.include.system` |
| status | token | `ValueSet.status` |
| title | string | `ValueSet.title` |
| url | uri | `ValueSet.url` |
| version | token | `ValueSet.version` |

## CodeSystem — elements (`codesystem` §4.8.4; 52 element rows in raw, all listed (7 `value[x]` type rows collapsed))
Root `CodeSystem` (IN) is a DomainResource; csd-0 warning on `name`; csd-1 "Within a code system definition, all the codes SHALL be unique" (`concept.code.combine($this.descendants().concept.code).isDistinct()`). CodeSystem "is not intended to support the process of maintaining code systems" and "is generally not an efficient way to distribute" large systems (SNOMED CT, LOINC, RxNorm, ICD family).

| Element | Flags | Card. | Type | Notes |
|---|---|---|---|---|
| `url` | Σ | 0..1 | uri | Canonical identifier "(Coding.system)"; "SHALL remain the same when the code system is stored on different servers" |
| `identifier` | Σ | 0..\* | Identifier | |
| `version` | Σ | 0..1 | string | Business version "(Coding.version)" |
| `name` | ΣI | 0..1 | string | |
| `title` | Σ | 0..1 | string | |
| `status` | ?!Σ | 1..1 | code | draft \| active \| retired \| unknown; PublicationStatus (Required) |
| `experimental` | Σ | 0..1 | boolean | |
| `date` | Σ | 0..1 | dateTime | |
| `publisher` | Σ | 0..1 | string | |
| `contact` | Σ | 0..\* | ContactDetail | |
| `description` |  | 0..1 | markdown | |
| `useContext` | ΣTU | 0..\* | UsageContext | |
| `jurisdiction` | Σ | 0..\* | CodeableConcept | Jurisdiction (Extensible) |
| `purpose` |  | 0..1 | markdown | |
| `copyright` |  | 0..1 | markdown | |
| `caseSensitive` | Σ | 0..1 | boolean | If code comparison is case sensitive |
| `valueSet` | Σ | 0..1 | canonical(ValueSet) | value set with the entire code system |
| `hierarchyMeaning` | Σ | 0..1 | code | grouped-by \| is-a \| part-of \| classified-with; CodeSystemHierarchyMeaning (Required) |
| `compositional` | Σ | 0..1 | boolean | defines a compositional grammar |
| `versionNeeded` | Σ | 0..1 | boolean | "If definitions are not stable"; when true "the version identifier SHALL be used in Coding instances" |
| `content` | Σ | 1..1 | code | not-present \| example \| fragment \| complete \| supplement; CodeSystemContentMode (Required) |
| `supplements` | Σ | 0..1 | canonical(CodeSystem) | code system this adds designations and properties to |
| `count` | Σ | 0..1 | unsignedInt | Total concepts in the code system |
| `filter` | Σ | 0..\* | BackboneElement | Filter usable in a value set |
| `filter.code` | Σ | 1..1 | code | |
| `filter.description` | Σ | 0..1 | string | |
| `filter.operator` | Σ | 1..\* | code | = \| is-a \| descendent-of \| is-not-a \| regex \| in \| not-in \| generalizes \| exists; FilterOperator (Required) |
| `filter.value` | Σ | 1..1 | string | What to use for the value |
| `property` | Σ | 0..\* | BackboneElement | Additional information supplied about each concept |
| `property.code` | Σ | 1..1 | code | identifies the property "when referred to in operations" and in filters |
| `property.uri` | Σ | 0..1 | uri | Formal identifier (e.g. Concept Properties code system) |
| `property.description` | Σ | 0..1 | string | |
| `property.type` | Σ | 1..1 | code | code \| Coding \| string \| integer \| boolean \| dateTime \| decimal; PropertyType (Required); "code" = a code defined by the code system |
| `concept` |  | 0..\* | BackboneElement | Concepts in the code system |
| `concept.code` |  | 1..1 | code | |
| `concept.display` |  | 0..1 | string | Text to display; all concepts SHOULD have display and definition |
| `concept.definition` |  | 0..1 | string | Formal definition |
| `concept.designation` |  | 0..\* | BackboneElement | |
| `concept.designation.language` |  | 0..1 | code | Common Languages (Preferred but limited to AllLanguages) |
| `concept.designation.use` |  | 0..1 | Coding | Designation Use (Extensible) |
| `concept.designation.value` |  | 1..1 | string | |
| `concept.property` |  | 0..\* | BackboneElement | Property value for the concept |
| `concept.property.code` |  | 1..1 | code | Reference to `CodeSystem.property.code` |
| `concept.property.value[x]` |  | 1..1 | code \| Coding \| string \| integer \| boolean \| dateTime \| decimal | (7 type rows) |
| `concept.concept` |  | 0..\* | see concept | Child Concepts (is-a/contains/categorizes) — "see hierarchyMeaning" |

Bindings (8): status Required PublicationStatus; jurisdiction Extensible; hierarchyMeaning Required CodeSystemHierarchyMeaning; content Required CodeSystemContentMode; filter.operator Required FilterOperator; property.type Required PropertyType; concept.designation.language Preferred (limited to AllLanguages) CommonLanguages; concept.designation.use Extensible DesignationUse.

### Content mode (`CodeSystem.content`) and multi-part code systems (§4.8.6–4.8.8)
| Value | What the page says |
|---|---|
| not-present, example, complete | listed values only — no per-value definition is printed on the page (n/s; the CodeSystemContentMode value set is not in the raw set) |
| fragment | "the resource describes part of a code system"; all fragments SHALL have the same `CodeSystem.url`; published only by the code-system authority (or its process); cannot contain codes/concepts/properties absent from a complete representation |
| supplement | "the resource describes a code system supplement"; `supplements` SHALL have a value (URL of the supplemented system); the supplement's `url` "SHALL never appear in a Coding.system"; must be under the supplement author's control; "cannot define any new CodeSystem.concept.code" — new property-value concepts need a paired (possibly contained) CodeSystem and `Coding` values |

Versioning (§4.8.5): changing the meaning of an existing code "SHOULD be avoided"; a version identifier MAY be provided and SHOULD be when meaning changes across releases; no format required, HL7 recommends a date-based value (FHIR date format of the official publication date).

### Properties, status, hierarchy, subsumption (§4.8.10–4.8.13)
- Property definition elements (4): `code` (used in `concept.property.code`, `ValueSet.compose.include.filter.property`, ConceptMap dependsOn/product, `$lookup`, `$translate`, `$find-matches` parameter names), `uri` (optional), `description` (optional), `type` (code \| Coding \| string \| integer \| boolean \| dateTime).
- Standard property URIs (6): `http://hl7.org/fhir/concept-properties#status` (code; SHALL use at least active / experimental / deprecated / retired where appropriate; HL7 treats active as default), `#retirementDate` (date), `#deprecationDate` (date), `#parent` (code), `#child` (code), `#notSelectable` (boolean = 'Abstract').
- Hierarchy: nested `concept` = single tree with meaning in `hierarchyMeaning`; multi-parent systems "SHOULD NOT" use nesting — use properties; if nesting is used, additional parents SHALL be given as a property; operations "SHALL have the same result" whether relationships are explicit properties or implicit nesting.
- Subsumption: A is subsumed by B if under B in the hierarchy or parent/child declared in properties with `hierarchyMeaning = "is-a"`; without a declared meaning none of the subsumption features can be used. Arises in: CodeSystem `$subsumes`, CodeSystem `$lookup`, ConceptMap `$closure`, search by subsumption, ValueSet `$expand`, ValueSet `$validate-code`.
- Base filters for all code systems (2 rows): `[property] = [string]`; `[property] in [string,string...]` (values cannot contain ",").
- Implicit code systems (§4.8.15, informative): StructureDefinition (`url` = system, each `snapshot.element.id` = code); Questionnaire (`url`, `item.linkId`); Medication (`[base]/Medication`, logical id = code).

### CodeSystem search parameters (20, all TU)
| Name | Type | Expression |
|---|---|---|
| code | token | `CodeSystem.concept.code` |
| content-mode | token | `CodeSystem.content` (not-present \| example \| fragment \| complete \| supplement) |
| context | token | `(CodeSystem.useContext.value as CodeableConcept)` |
| context-quantity | quantity | `(CodeSystem.useContext.value as Quantity) \| (CodeSystem.useContext.value as Range)` |
| context-type | token | `CodeSystem.useContext.code` |
| context-type-quantity | composite | on `CodeSystem.useContext`: context-type + context-quantity |
| context-type-value | composite | on `CodeSystem.useContext`: context-type + context |
| date | date | `CodeSystem.date` |
| description | string | `CodeSystem.description` |
| identifier | token | `CodeSystem.identifier` |
| jurisdiction | token | `CodeSystem.jurisdiction` |
| language | token | `CodeSystem.concept.designation.language` |
| name | string | `CodeSystem.name` |
| publisher | string | `CodeSystem.publisher` |
| status | token | `CodeSystem.status` |
| supplements | reference | `CodeSystem.supplements` (CodeSystem) |
| system | uri | `CodeSystem.url` ("same as 'url'") |
| title | string | `CodeSystem.title` |
| url | uri | `CodeSystem.url` |
| version | token | `CodeSystem.version` |

## Operations as mentioned on these pages
The content pages only *name* the operations; their parameter tables live on the (unscraped) operations pages — marked n/s.

| Operation | What the pages state |
|---|---|
| ValueSet `$expand` | "ask a server to generate an expansion given the composition rules, in a particular context"; predefined parameters listed above; `GET [base]/ValueSet/$expand?url=…` for imported value sets; output may be expansion-only or compose + expansion |
| ValueSet `$validate-code` | "ask a server to check whether a given code or concept is in the value set in a particular context"; uses subsumption |
| CodeSystem `$lookup` | returns information about a code, property codes in `Parameters.parameter.name`; the correct display for a code "can be determined by a $lookup operation"; uses parent/child properties and subsumption |
| CodeSystem `$subsumes`, ConceptMap `$closure`, `$translate`, `$find-matches` | named only (subsumption list; property-code usage) — n/s |

## Relationships
- ValueSet references: CodeSystem (`compose.include.system`, canonical), ValueSet (`compose.include.valueSet`). Referenced by: DataRequirement, ElementDefinition (`binding.valueSet`), CodeSystem (`valueSet`), ConceptMap, ObservationDefinition, OperationDefinition, Questionnaire, ResearchElementDefinition, itself.
- CodeSystem references: ValueSet (`valueSet`), CodeSystem (`supplements`). Referenced by: Coding (`system` = canonical URL), itself, ConceptMap, TerminologyCapabilities, ValueSet. `CodeSystem` is managed by the code-system publisher; `NamingSystem` is often defined by third parties and may have several per system; ConceptMaps assert context-specific relationships while supplements define inherent properties.

## Notes for our server
- Seed a terminology store with CodeSystem resources for the SATUSEHAT-mandated systems (see satusehat-terminology.md): `content = not-present` for LOINC / SNOMED CT / ICD-10 / ICD-9 CM / UCUM (we only declare `url`, `caseSensitive`, `version`), `content = complete` for small local systems (e.g. our device-type or measurement-method codes) with `concept.code/display/definition`.
- Represent each profile binding as a ValueSet with `compose.include` (LOINC vital-sign codes by `concept`, or a whole local system by `system` only) and precompute a stored `expansion` with `timestamp`, unique `expansion.identifier`, and `parameter` rows recording the code-system versions; use it for `required`/`extensible` binding checks in the validator and for UI pick lists.
- Implement `$expand` (with `filter`, `count`/`offset`, `activeOnly`) and `$validate-code` over the stored expansions; treat codes as case sensitive; never copy a ValueSet `display` into `Coding.display` — take it from the CodeSystem (`$lookup`), put the pick-list label in `CodeableConcept.text`.
- Enforce vsd-1..3 and csd-1 on write; reject supplements whose `url` appears in any `Coding.system`.
- Search support: `ValueSet?url=`, `ValueSet?reference=`, `CodeSystem?url=`/`system=`, `CodeSystem?content-mode=`; the `ValueSet?code=` parameter may be left unsupported (declared in TerminologyCapabilities).

## Sources
- raw/fhir-r4/valueset.md
- raw/fhir-r4/codesystem.md

# FHIR R4 — Data-model basics: primitive and complex types, references, narrative, validation

Summary: `datatypes.md` (Normative / partially normative) defines the primitive types and the general-purpose complex types; `references.md` (Normative) defines `Reference`, canonical references and contained resources; `narrative.md` (Normative) defines `Narrative` (`text.status` + XHTML `div`) and its security limits; `validation.md` (Informative) lists what validation checks and the tooling options. `Meta` (`resource.html`) and `Extension` (`extensibility.html`) are documented elsewhere — only what these four pages say about them is recorded here (see fhir-profiling.md for extensions).

## Primitive types (`datatypes` §2.24.0.1)
JSON: value is the property itself; `id`/extensions go in a sibling `_name` object (`"count": 2, "_count": {...}`). A missing value with no extensions means the element is absent — `""` and `null` are not valid (one JSON-array `null` exception exists on the JSON page). Primitives other than `string` SHALL NOT have leading/trailing whitespace. The regexes are informative, **not normative**, need anchoring, and over-accept (e.g. leap years) — "additional validation is always needed".

| Type | Value domain / format | Regex (as printed) | JSON |
|---|---|---|---|
| boolean | `true` / `false`; `0`/`1` not valid | `true\|false` | JSON boolean |
| integer | signed 32-bit −2,147,483,648..2,147,483,647; no leading zeros | `[0]\|[-+]?[1-9][0-9]*` | JSON number, no decimal point |
| string | Unicode; SHALL NOT exceed 1 MB; SHOULD not contain code points < 32 except tab/CR/LF (page prints u0009, u0010, u0013); SHOULD contain non-whitespace | `[ \r\n\t\S]+` | JSON string |
| decimal | rationals with decimal representation; **precision is significant** (0.010 ≠ 0.01) and SHALL be preserved; no `INF`/`NaN` | `-?(0\|[1-9][0-9]*)(\.[0-9]+)?([eE][+-]?[0-9]+)?` | JSON number |
| uri | RFC 3986; case sensitive; `urn:uuid:` lowercase; absolute or relative, optional fragment | `\S*` (permissive) | JSON string |
| url | RFC 1738 locator (`http{s}:`, `ftp:`, `mailto:`, `mllp:`…) | — | JSON string |
| canonical | URI referring to a resource by its canonical `url`, may carry `\|version` and `#fragment` | — | JSON string |
| base64Binary | RFC 4648; no size limit in spec — implementation limit must be documented | `(\s*([0-9a-zA-Z\+\=]){4}\s*)+` | JSON string |
| instant | `YYYY-MM-DDThh:mm:ss.sss+zz:zz`; SHALL be at least to the second and SHALL include a time zone; for system times | see raw (anchored full dateTime with mandatory time and zone) | JSON string |
| date | `YYYY`, `YYYY-MM`, `YYYY-MM-DD`; **SHALL be no time zone**; SHALL be valid dates | `([0-9]([0-9]([0-9][1-9]\|[1-9]0)\|[1-9]00)\|[1-9]000)(-(0[1-9]\|1[0-2])(-(0[1-9]\|[1-2][0-9]\|3[0-1]))?)?` | JSON string |
| dateTime | `YYYY`, `YYYY-MM`, `YYYY-MM-DD`, or `YYYY-MM-DDThh:mm:ss+zz:zz`; if hours and minutes are given a time zone SHALL be populated; seconds required (may be zero-filled); `24:00` not allowed; leap seconds allowed | date regex extended with `(T([01][0-9]\|2[0-3]):[0-5][0-9]:([0-5][0-9]\|60)(\.[0-9]+)?(Z\|(\+\|-)((0[0-9]\|1[0-3]):[0-5][0-9]\|14:00)))?` | JSON string |
| time | `hh:mm:ss`, no date; `24:00` SHALL NOT be used; time zone SHALL NOT be present | `([01][0-9]\|2[0-3]):[0-5][0-9]:([0-5][0-9]\|60)(\.[0-9]+)?` | JSON string |
| code | ≥1 char, no leading/trailing whitespace, only single spaces inside | `[^\s]+(\s[^\s]+)*` | JSON string |
| oid | `urn:oid:…` | `urn:oid:[0-2](\.(0\|[1-9][0-9]*))+` | JSON string |
| id | ASCII letters, digits, `-`, `.`; 1–64 chars; case sensitive | `[A-Za-z0-9\-\.]{1,64}` | JSON string |
| markdown | a `string` with GFM CommonMark (raw HTML prohibited by GFM); same rules as string | `\s*(\S\|\s)*` | JSON string |
| unsignedInt | 0..2,147,483,647 | `[0]\|([1-9][0-9]*)` | JSON number |
| positiveInt | 1..2,147,483,647 | `+?[1-9][0-9]*` | JSON number |
| uuid | `urn:uuid:…` (RFC 4122), lowercase | — | JSON string |

Notes from the page: `uri`/`url`/`canonical` are never substituted for each other and compare case-sensitively; a full UUID is a `uri`, not an `id`; `[type]/[id]` path tail (e.g. `1234` in `Patient/1234`) is an `id`; applications reading times SHOULD accept leap seconds; all types may have extensions, but only `Timing`, `Dosage`, `ElementDefinition` may have modifier extensions.

## General-purpose complex types (`datatypes` §2.24.0.3–18)
Elements common to all: `id` (string, no spaces) and `extension`. `?!` = modifier element, `Σ` = in summary.

| Type | Element | Card. | Type | Notes / binding |
|---|---|---|---|---|
| **Identifier** | `use` | 0..1 ?! | code | `usual` \| `official` \| `temp` \| `secondary` \| `old` (required) |
| | `type` | 0..1 | CodeableConcept | IdentifierType (extensible); general category only, SHOULD not duplicate `system` 1:1 |
| | `system` | 0..1 | uri | namespace; always case sensitive; SHOULD resolve if URL; `urn:ietf:rfc:3986` when the value is itself a globally unique URI |
| | `value` | 0..1 | string | SHALL be unique within `system`; case sensitive unless system says otherwise |
| | `period` | 0..1 | Period | validity |
| | `assigner` | 0..1 | Reference(Organization) | may be `display` text only |
| **HumanName** | `use` | 0..1 ?! | code | `usual` \| `official` \| `temp` \| `nickname` \| `anonymous` \| `old` \| `maiden` |
| | `text` | 0..1 | string | full name as displayed; SHOULD be populated; when text and parts both present, text SHALL contain nothing not in a part |
| | `family` | 0..1 | string | surname (extensions for compound family names: own-name, own-prefix, partner-name, partner-prefix, fathers-family, mothers-family) |
| | `given` / `prefix` / `suffix` | 0..* | string | order within a part type is significant and SHALL be observed |
| | `period` | 0..1 | Period | |
| **Address** | `use` | 0..1 ?! | code | `home` \| `work` \| `temp` \| `old` \| `billing` |
| | `type` | 0..1 | code | `postal` \| `physical` \| `both` |
| | `text` | 0..1 | string | same text-vs-parts rule as HumanName |
| | `line` | 0..* | string | ordered |
| | `city`, `district`, `state`, `postalCode`, `country` | 0..1 | string | country e.g. ISO 3166 2/3-letter |
| | `period` | 0..1 | Period | |
| **ContactPoint** | `system` | 0..1 | code | `phone` \| `fax` \| `email` \| `pager` \| `url` \| `sms` \| `other`; **cpt-2**: a system is required if a value is provided |
| | `value` | 0..1 | string | phone SHOULD follow ITU-T E.123; for `other` the value SHOULD be a URL |
| | `use` | 0..1 ?! | code | `home` \| `work` \| `temp` \| `old` \| `mobile` |
| | `rank` | 0..1 | positiveInt | 1 = most preferred |
| | `period` | 0..1 | Period | |
| **Coding** | `system` | 0..1 | uri | code-system URI (`CodeSystem.url`); SHALL NOT be a value-set URL |
| | `version` | 0..1 | string | SHOULD be exchanged when definitions vary by version (national SNOMED CT, ICD) |
| | `code` | 0..1 | code | SHALL be syntactically correct for the system; case sensitive unless system says otherwise |
| | `display` | 0..1 | string | SHALL be one of the system's display strings for the code; preferred one SHOULD be used |
| | `userSelected` | 0..1 | boolean | chosen directly by the user; preferred for translation |
| **CodeableConcept** | `coding` | 0..* | Coding | translations; order has no meaning; usually only one `userSelected=true` |
| | `text` | 0..1 | string | as entered/chosen by user; text-only allowed when no code fits |
| **Quantity** | `value` | 0..1 | decimal | implicit precision |
| | `comparator` | 0..1 ?! | code | `<` \| `<=` \| `>=` \| `>`; "can never be ignored"; absent = point value |
| | `unit` | 0..1 | string | displayable unit |
| | `system` | 0..1 | uri | **qty-3**: if `code` present, `system` SHALL be present |
| | `code` | 0..1 | code | if codable in UCUM, SHOULD be a UCUM code (enables canonical comparison) |
| | variants | — | — | `SimpleQuantity` (**sqty-1** comparator SHALL be empty); `Age`/`Duration` (**age-1**/**drt-1**: SHALL have a code if value present, expression of time, system SHALL be UCUM); `Count` (**cnt-3** code `1`, whole number); `Distance` (**dis-1**); `Money` (`value` decimal, `currency` ISO 4217 code) |
| **Range** | `low`, `high` | 0..1 | SimpleQuantity | **rng-2**: low SHALL be lower than high |
| **Ratio** | `numerator`, `denominator` | 0..1 | Quantity | **rat-1**: both present or both absent (then an extension SHALL exist) |
| **Period** | `start` | 0..1 | dateTime | inclusive; missing = unknown |
| | `end` | 0..1 | dateTime | inclusive (a date `end` covers the whole day); missing = ongoing/planned; rule: if present, start SHALL have a lower value than end (id not printed) |
| **Annotation** | `author[x]` | 0..1 | Reference(Practitioner \| Patient \| RelatedPerson \| Organization) or string | |
| | `time` | 0..1 | dateTime | |
| | `text` | 1..1 | markdown | SHOULD NOT carry "modifying" computable information |
| **Attachment** | `contentType` | 0..1 | code | MimeType (required); **att-1**: SHALL be present when `data` is present |
| | `language` | 0..1 | code | BCP-47 |
| | `data` | 0..1 | base64Binary | inline |
| | `url` | 0..1 | url | SHALL resolve to the same content as `data` if both given; version-specific |
| | `size`, `hash` | 0..1 | unsignedInt, base64Binary | of the raw bytes (SHA-1); hash not for signatures |
| | `title`, `creation` | 0..1 | string, dateTime | |
| **SampledData** (TU) | `origin` 1..1 SimpleQuantity, `period` 1..1 decimal (ms), `factor`, `lowerLimit`, `upperLimit` 0..1 decimal, `dimensions` 1..1 positiveInt, `data` 0..1 string | | | "A series of measurements taken by a device"; data = space-separated decimals or `E`/`L`/`U` |
| **Timing** | `event` 0..* dateTime; `repeat` (bounds[x] Duration\|Range\|Period, count/countMax, duration/durationMax + `durationUnit` `s|min|h|d|wk|mo|a`, frequency/frequencyMax, period/periodMax + `periodUnit`, `dayOfWeek` `mon…sun`, `timeOfDay` time, `when` EventTiming, `offset`); `code` CodeableConcept (e.g. BID) | | | tim-1/2 units required with duration/period; tim-4/5 non-negative; tim-6/7/8 max requires base; tim-9 offset needs `when`; tim-10 timeOfDay xor when; only complex type allowed modifier extensions |
| **Signature** (TU) | `type` 1..* Coding, `when` 1..1 instant, `who` 1..1 Reference, `onBehalfOf` 0..1, `targetFormat`/`sigFormat` 0..1 code, `data` 0..1 base64Binary | | | |
| **Meta** | listed by `datatypes` only as a Special Type defined on `resource.html` (not in corpus); elements named across these pages: `versionId`, `lastUpdated` (server-managed; `http.md`), `profile`, `tag`, `security` (searchable via `_profile`/`_tag`/`_security`; `search.md`) | | | contained resources SHALL NOT carry `meta.versionId`, `meta.lastUpdated`, `meta.security`; MAY carry `meta.tag` (`references.md`) |
| **Extension** | "used to convey additional data in a resource" — defined on `extensibility.html` (see fhir-profiling.md); JSON form for primitives shown above (`_name.extension[]` with `url` + `value[x]`) | | | |

Open-type elements (`[x]`) may take any primitive, any of the general-purpose types above, the metadata types, `Dosage` or `Meta`; the element name ends with the Title-cased type (`valueQuantity`).

## Reference (`references`)
| Element | Card. | Type | Notes |
|---|---|---|---|
| `reference` | 0..1 | string | literal reference: absolute URL, relative URL (to service base, or to `Bundle.entry.fullUrl` base), or `#id` internal fragment |
| `type` | 0..1 | uri | expected target type, relative to `http://hl7.org/fhir/StructureDefinition/` (so just `Patient`); SHALL agree with the resolved type |
| `identifier` | 0..1 | Identifier | logical reference when no literal is known |
| `display` | 0..1 | string | short text alternative; not the target's narrative |
- At least one of `reference`, `identifier`, `display` SHALL be present (unless an extension is provided). **ref-1**: a `#local` reference SHALL point to a contained resource id.
- Literal references SHALL point to an actual FHIR resource and SHALL be resolvable; URLs are case-sensitive; may be version-specific `Observation/123/_history/234234`; the RESTful-URL regex `((http|https)://([A-Za-z0-9\-\\\.\:\%\$]*/)+)?(<ResourceType>)/[A-Za-z0-9\-\.]{1,64}(/_history/[A-Za-z0-9\-\.]{1,64})?` identifies API-shaped references (see raw for the type list).
- Logical references: identifier only; chaining/includes not possible; servers may accept untouched, resolve, or reject (`CapabilityStatement.rest.resource.referencePolicy`); when both are given the literal reference is preferred. The identifier SHALL denote a business concept of a type allowed by the reference.
- Relationships are one-directional and not transitive; context (e.g. subject) is not inherited across references, except for contained resources. Cross-FHIR-version references are undefined.
- Canonical references (`canonical` type): preferred for terminology/conformance/knowledge resources (StructureDefinition, ValueSet, CodeSystem, CapabilityStatement, SearchParameter, OperationDefinition… list in raw); `url|version` refers to the business `version`, not `meta.versionId`; without a version pick the latest; servers SHOULD detect `|[version]` in searches; resolve first via registry, then fall back to the URL.
- Contained resources: for content with no independent identity; SHOULD NOT be used when the content can be identified; same FHIR version as container; `contained` element SHALL NOT have extensions; SHALL NOT nest; SHALL NOT have `meta.versionId`/`lastUpdated`/`security`; SHALL only be included if something references it (or it references the container with `#`); references to contained resources never resolve outside the container; contained narrative is ignored, so key information SHALL appear in the container's narrative; no context inheritance.
- Circular/hierarchical references with `:above`/`:below` search support: `Encounter.partOf`, `Location.partOf`, `Organization.partOf`, `CarePlan.basedOn/replaces/partOf`, `StructureDefinition.baseDefinition`; `Patient.link.other` may point back; `Device.parent`, `Observation.hasMember`, `Observation.derivedFrom`, `Procedure.partOf`, `Person.link.target` are circular without specified hierarchy behavior.

## Narrative (`narrative`)
| Element | Card. | Type | Rule |
|---|---|---|---|
| `status` | 1..1 | code | `generated` \| `extensions` \| `additional` \| `empty` (required) |
| `div` | 1..1 | xhtml | SHALL contain only basic HTML formatting elements (HTML 4.0 ch. 7–11 except 9.4, and 15), `<a>` (name or href), images, internal `style` attributes; SHALL have some non-whitespace content |
- Any DomainResource (all except Bundle, Parameters, Binary) may have narrative; instances SHOULD always contain it as a human fallback; a resource MAY be text-only as long as minOccurs=1 elements are satisfied.
- If status ≠ `empty` the narrative SHALL reflect all content needed for a human to understand the essential clinical/business information and SHALL be safe to render alone; SHOULD summarise referenced resources; with `status=extensions` SHALL reflect modifier extensions; content derived from other resources still counts as `generated`.
- Forbidden: `head`, `body`, external stylesheet references, deprecated elements, scripts, forms, base/link/xlink, frames, iframes, objects, event attributes (`onClick`). No HTML entities (`&nbsp;`) — use Unicode (`&#160;`).
- JSON: `div` string SHALL be encoded so the text between the first `>` and last `<` is the div content: `"<div xmlns=\"http://www.w3.org/1999/xhtml\">text</div>"` is legal; `"<?xml ...><div>text</div>"` is not.
- `lang` attribute on the root `div` SHOULD mirror the resource language; multi-language content via `div` children with `lang`.
- Images essential to the narrative SHOULD be embedded as `data:` URLs, attachments or contained resources; `id` attributes SHALL be unique within the resource (contained resources share the scope).
- Styling: renderer supplies stylesheets; classes every renderer SHALL support: `bold italics underline strikethrough left right center justify border-left border-right border-top border-bottom arabic little-roman big-roman little-alpha big-alpha disc circle square unlist`; inline `style` for bold/italic/underline/strikethrough, font colour/family/size, background, alignment, whitespace, list numbering — renderers SHOULD respect them. Styles SHOULD NOT be the sole carrier of meaning; avoid complex nested layouts.
- Extensions `narrativeLink` and `originalText` link data and text.

## Validation (`validation`)
Aspects a validator checks: **Structure** (nothing extra), **Cardinality**, **Value domains** (type rules, enumerated codes), **Coding/CodeableConcept bindings**, **Invariants**, **Profiles** (from `meta.profile`, CapabilityStatement, ImplementationGuide or context), **Questionnaires**, **Business rules** (duplicates, reference resolution, authorization — outside the spec).

| Method | Notes stated |
|---|---|
| XML Schema (`fhir-all.xsd` / `fhir-single.xsd`) | least capable; not connected to a terminology server |
| XML Schema + Schematron (`fhir-invariants.sch`, XSLT2) | profile-generated schematron tests cardinality and invariants, not bindings; slicing poorly supported |
| JSON Schema | profile-generated schema tests cardinality; slicing partially supported |
| ShEx (RDF) | enforces some bindings for well-understood terminologies |
| FHIR Validator (Java jar) | used to validate all published examples; needs a terminology server (default `http://fhir3.healthintersections.com.au`); only as good as the definitions |
| `$validate` operation | `POST [base]/Observation/$validate?profile=<canonical>` with the resource as body → `OperationOutcome`; not all servers support it; usually only registered profiles; server decides how much to validate (most derive from the Java validator) |
(The per-method coverage matrix is icon-based in the source and did not survive scraping — only the footnotes above are recoverable.)

- All methods are incomplete: narrative rules ("all clinically important content SHALL be in the narrative") cannot be machine-checked; final arbiter is human inspection.
- Production validation trade-offs: full terminology validation is computationally demanding; over-strict validation can lose critical data or fail historical data; but validation may be required for security (narrative active content / external references) and as a control point. Postel's law recommended: conservative in sending, liberal in receiving.

## Notes for our server
- Parser/serializer: JSON only; reject `""`/`null` primitives, enforce the regexes above *plus* real date validity, no leading zeros in integers, 32-bit integer ranges, 64-char ids, lowercase `urn:uuid:`; keep decimals as arbitrary-precision (BigDecimal-style) to preserve `0.010` vs `0.01`; store `dateTime` with its zone (required whenever hours are present) and `instant` for `meta.lastUpdated`.
- Element validators: Identifier (`system` URI + `value`, both case-sensitive — matches SATUSEHAT RuleNumber 10117 for invalid identifier systems), Coding/CodeableConcept (`system` SHALL be a code-system URI, `code` and `display` checked against our terminology table — RuleNumbers 10001/10002), Quantity (qty-3 code⇒system; UCUM for vital signs; reject `comparator` in SimpleQuantity contexts), Period (start ≤ end), ContactPoint (cpt-2), Attachment (att-1), Range (rng-2), Ratio (rat-1).
- References: accept relative `Type/id` and absolute URLs under our base; resolve and 422 when the target does not exist (business rule); require `Reference.type` consistency; support `#contained` per ref-1 and the contained-resource constraints; treat identifier-only references per our declared `referencePolicy` (suggest `resolves` + `local`); device Observations reference `Device/[id]`, `Patient/[id]`, `Encounter/[id]` literally.
- Generate `text` (`status=generated`, XHTML with `xmlns`, `lang="id"`) for resources we create, and sanitize incoming `div` against the forbidden-element list; encode JSON `div` exactly as the page requires.
- Validation pipeline order: structure → cardinality → value domains → bindings (our terminology table) → invariants → profile (SATUSEHAT-derived) → business rules (duplicates, reference resolution, authorization); expose `POST [base]/[type]/$validate` returning `OperationOutcome` for client testing; keep full validation on write (SATUSEHAT-style processor-then-server) but consider leniency for historical imports.

## Sources
- raw/fhir-r4/datatypes.md
- raw/fhir-r4/references.md
- raw/fhir-r4/narrative.md
- raw/fhir-r4/validation.md

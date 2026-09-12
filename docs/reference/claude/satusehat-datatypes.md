# SATUSEHAT — Data Types (Tipe Data)

Ringkasan (summary): The playbook's four data-type pages (Primitif, Umum, Metadata, Khusus) restate the FHIR R4 data types in Indonesian with a JSON structure per complex type. They add no SATUSEHAT-specific constraints beyond what FHIR R4 already says; their value for us is the exact format strings for dates/times/ids and the `*` (WAJIB, mandatory) / `?` (conditionally mandatory) markers the pages put on some sub-elements. Nothing here is a profile — cardinalities are only implied by the `*`/`?` markers.

Marker convention (stated on the Umum page): `*variabel` = **WAJIB** (mandatory, always present); `?variabel` = **WAJIB ada bila memenuhi kondisi tertentu** (mandatory under a condition, e.g. one of a choice).

## Primitive types (`datatype-primitive`)
| Type | Rule / format as stated | Example given |
|---|---|---|
| `boolean` | `true` or `false` | — |
| `integer` | −2.147.483.648 … 2.147.483.647 (32-bit); use `decimal` for larger | — |
| `string` | Unicode; ≤ 1.048.576 characters; code points ≥ 32 except tab, CR, LF; no leading/trailing whitespace; must not be empty | — |
| `decimal` | Rational decimal; also accepts an `integer` when the value exceeds integer capacity | — |
| `uri` | RFC 3986; case sensitive; absolute or relative, may carry `#` fragment; UUID values must be all lowercase | `urn:uuid:53fefa32-fcbb-4ff8-8a92-55ee120877b7` |
| `url` | RFC 1738; schemes `http{s}:`, `ftp:`, `mailto:`, `mllp:` | — |
| `canonical` | URI referencing a resource by its canonical URL; version separated by a separator | — |
| `base64binary` | Base64 stream of bytes (RFC 4648) | — |
| `instant` | `YYYY-MM-DDThh:mm:ss.sss+zz:zz`; system time only; at least seconds and a time zone required | `2015-02-07T13:28:17.239+02:00` |
| `date` | `YYYY`, `YYYY-MM`, `YYYY-MM-DD` | `2022`, `1993-02`, `2023-02-01` |
| `dateTime` | `YYYY`, `YYYY-MM`, `YYYY-MM-DD`, `YYYY-MM-DDThh:mm:ss+zz:zz`; `24:00` not allowed | `2015-02-07T13:28:17-05:00`, `2017-01-01T00:00:00.000Z` |
| `time` | `hh:mm:ss` | `11:07:20` |
| `code` | String whose value is defined elsewhere (a code system) | — |
| `oid` | OID as URI (RFC 3001) | `urn:oid:1.2.3.4.5` |
| `id` | `A..Z`, `a..z`, `0..9`, `.`, `-`; max 64 characters | — |
| `markdown` | FHIR string containing markdown | — |
| `unsignedInt` | range `0..2,147,483,647` (page literally says "bilangan negatif", a typo for non-negative) | — |
| `positiveInt` | range `1..2,147,483,647` | — |
| `uuid` | UUID (GUID) represented as URI (RFC 4122) | — |

## General (Umum) types (`datatype-general`)
Structures exactly as printed (`*`/`?` markers preserved; unmarked = optional). Types with no structure on the page are listed with their reference only.

| Type | JSON structure (element: type) | Notes from the page |
|---|---|---|
| `Address` | `*use: code`, `*type: code`, `text`, `line: [string]`, `city`, `district`, `state`, `postalCode`, `country`, `period: Period` | `use` from AddressUse (page mislabels it "IdentifierUse"), `type` from AddressType; `city` = kota/kabupaten, `district` = kecamatan, `state` = kelurahan (page's own mapping); `country` ISO 3166-2 / 3166-3 |
| `Age`, `Distance`, `Duration` | Quantity-based | UCUM value sets: CommonUCUMCodesForAge / Distance / Duration |
| `Annotation` | `?authorReference: Reference`, `?authorString: string`, `time: dateTime`, `*text: markdown` | authorReference targets `Practitioner, Patient, RelatedPerson, Organization` |
| `Attachment` | `contentType: code`, `language: code`, `data: base64Binary`, `url: url`, `size: unsignedInt`, `hash: base64Binary`, `title`, `creation: dateTime` | MimeType; BCP-47 language; hash = sha-1 base64 |
| `CodeableConcept` | `coding: [Coding]`, `text: string` | — |
| `CodeableReference` | `concept: CodeableConcept`, `reference: Reference` | Listed on both Umum and Khusus pages |
| `Coding` | `system: uri`, `version: string`, `code: code`, `display: string`, `userSelected: boolean` | — |
| `ContactPoint` | `system: code`, `value: string`, `use: code`, `rank: positiveInt`, `period: Period` | system: phone, fax, email, pager, url, sms; use: home, work, temp, old, mobile; rank 1 = highest |
| `Count`, `MoneyQuantity`, `SimpleQuantity` | "mereferensi ke resource `Quantity`" | — |
| `HumanName` | `use: code`, `text`, `family`, `given: [string]`, `prefix: [string]`, `suffix: [string]`, `period: Period` | use: usual, official, temp, nickname, anonymous, old, maiden; prefix e.g. "Prof. dr., Mr., Ny."; suffix e.g. "ST, MBA" |
| `Identifier` | `use: code`, `type: CodeableConcept`, `system: uri`, `value: string`, `period: Period`, `assigner: Reference` | use: usual, official, temp, secondary, old; `system` = namespace, `value` = unique value |
| `Money` | `value: decimal`, `currency: code` | ISO 4217 |
| `Period` | `start: dateTime`, `end: dateTime` | — |
| `Quantity` | `value: decimal`, `comparator: code`, `unit: string`, `system: uri`, `code: code` | `comparator` **WAJIB ada bila** the value is approximate (`>`, `≥`, `<`, `≤`), from QuantityComparator; `system` **WAJIB ada bila** `unit` is filled |
| `Range` | `low: SimpleQuantity`, `high: SimpleQuantity` | — |
| `Ratio` | `numerator: Quantity`, `denominator: Quantity` | — |
| `RatioRange` | `lowNumerator`, `highNumerator`, `denominator` (all SimpleQuantity) | — |
| `Reference` | `reference: string`, `type: uri`, `identifier: Identifier`, `display: string` | One of `reference`, `identifier`, `display` must be present; direction is always source → target |
| `SampledData` | `origin: [SimpleQuantity]`, `period: [decimal]`, `factor`, `lowerLimit`, `upperLimit`, `dimensions: [positiveInt]`, `data: string` | period = milliseconds between samples; data = decimals separated by spaces or `E`, `U`, `L` (page brackets origin/period/dimensions as arrays, unlike FHIR R4) |
| `Signature` | `type: [Coding]`, `when: [instant]`, `who: [Reference]`, `onBehalfOf: Reference`, `targetFormat: code`, `sigFormat: code`, `data: base64Binary` | Page brackets `when`/`who` as arrays, unlike FHIR R4 |
| `Timing` | `event: [dateTime]`, `repeat { ?boundsDuration \| ?boundsRange \| ?boundsPeriod, count, countMax, duration, durationMax, durationUnit, frequency, frequencyMax, period, periodMax, periodUnit, dayOfWeek: [code], timeOfDay: [time], when: [code], offset: unsignedInt }`, `code: CodeableConcept` | durationUnit: detik, menit, jam, hari, minggu, bulan |

## Metadata types (`datatype-metadata`)
| Type | JSON structure | Notes |
|---|---|---|
| `ContactDetail` | `name: string`, `telecom: [ContactPoint]` | — |
| `Contributor` | `*type: code`, `*name: string`, `contact: [ContactDetail]` | type: author, editor, reviewer, endorser |
| `DataRequirement` | `*type: code`, `profile: [canonical]`, `?subjectCodeableConcept`, `?subjectReference`, `mustSupport: [string]`, `codeFilter[] { path, searchParam, valueSet: canonical, code: [Coding] }`, `dateFilter[] { path, searchParam, ?valueDateTime \| ?valuePeriod \| ?valueDuration }`, `limit: positiveInt`, `sort[] { *path, *direction: code }` | Page prints the nested elements flat |
| `Expression` | `description`, `name: id`, `*language: code`, `expression: string`, `reference: uri` | language: text/cql, text/fhirpath, application/x-fhir-query, text/cql-identifier, text/cql-expression |
| `ParameterDefinition` | `name: code`, `*use: code`, `min: integer`, `max: string`, `documentation`, `*type: code`, `profile: canonical` | use from OperationParameterUse |
| `RelatedArtifact` | `*type: code`, `label`, `display`, `citation: markdown`, `url: url`, `document: Attachment`, `resource: canonical` | type: documentation, justification, citation, predecessor, successor, derived-from, depends-on, composed-of |
| `TriggerDefinition` | `*type: code`, `name`, `?timingTiming \| ?timingReference \| ?timingDate \| ?timingDateTime`, `data: [DataRequirement]`, `condition: Expression` | type: named-event, periodic, data-changed, data-added, data-modified, data-removed, data-accessed, data-access-ended |
| `UsageContext` | `*code: Coding`, `*?valueCodeableConcept \| *?valueQuantity \| *?valueRange \| *?valueReference` | one value[x] is mandatory |

## Special (Khusus) types (`datatype-special`)
| Type | JSON structure | Notes |
|---|---|---|
| `CodeableReference` | `concept: CodeableConcept`, `reference: Reference` | duplicate of the Umum entry |
| `Dosage` | `sequence: integer`, `text`, `additionalInstruction: [CodeableConcept]`, `patientInstruction`, `timing: Timing`, `?asNeededBoolean \| ?asNeededCodeableConcept`, `site`, `route`, `method` (CodeableConcept), `doseAndRate[] { type, ?doseRange \| ?doseQuantity, ?rateRatio \| ?rateRange \| ?rateQuantity }`, `maxDosePerPeriod: Ratio`, `maxDosePerAdministration`, `maxDosePerLifetime` (SimpleQuantity) | — |
| `Extension` | `*url: uri`, `?value: *` | value type is open (`*`) |
| `Meta` | `versionId: id`, `lastUpdated: instant`, `source: uri`, `profile: [canonical]`, `security: [Coding]`, `tag: [Coding]` | `profile` = profiles the resource must conform to |
| `Narrative` | `*status: code`, `*div: xhtml` | — |
| `Reference` | `reference: string`, `type: uri`, `identifier: identifier`, `display: string` | same rule: one of reference/identifier/display required |
| `xhtml` | HTML 4.0 subset; no head, body, external stylesheet, scripts, forms, base/link/xlink, frames, iframes, objects | — |

## Inconsistencies noted (verbatim, not resolved)
- `datatype-general` `Address`: `use` and `type` are both marked `*` (mandatory) — FHIR R4 has them 0..1. The page also says `use` values come from "IdentifierUse" while linking the AddressUse value set.
- `datatype-general` `SampledData` and `Signature` print several scalar FHIR elements as arrays (`origin`, `period`, `dimensions`; `when`, `who`).
- `datatype-primitive` `unsignedInt` is described as "bilangan negatif" with range `0..2,147,483,647`.
- `datatype-general` `Annotation.text` and `Extension.url`, `Narrative.status/div`, `Contributor.type/name` are marked `*`, matching FHIR R4 1..1 cardinality; no other complex-type element is marked.

## Notes for our server
- Validate primitives to the formats above: `date` (3 precisions), `dateTime` (4 precisions, zone required when time present, reject `24:00`), `instant` (seconds + zone mandatory), `time` `hh:mm:ss`, `id` ≤ 64 chars `[A-Za-z0-9.-]`, `string` non-empty and trimmed.
- Enforce the two conditional rules on `Quantity`: `system` required when `unit` is set (our vital signs always carry UCUM `http://unitsofmeasure.org`), `comparator` only when the value is approximate.
- `Reference` must have at least one of `reference` / `identifier` / `display`; our resources use literal `reference` strings like `Patient/{ihs-number}`.
- Treat the `*` on `Address.use`/`Address.type` as a playbook quirk: patient addresses in the MPI pages use `use: home` but never mention `type`; do not reject an address lacking `type`.
- `Meta.profile` should carry the SATUSEHAT profile canonical (e.g. `https://fhir.kemkes.go.id/r4/StructureDefinition/Patient`) when we echo resources back.
- `SampledData` is the type intended for device waveform series; single device vital signs use `valueQuantity` instead.

## Sources
- raw/satusehat/datatype-primitive.md
- raw/satusehat/datatype-general.md
- raw/satusehat/datatype-metadata.md
- raw/satusehat/datatype-special.md

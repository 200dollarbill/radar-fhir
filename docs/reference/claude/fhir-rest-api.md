# FHIR R4 — RESTful API, Search, Operations, Bundle, CapabilityStatement

Summary: FHIR R4 defines a Level-2 REST API where each resource type has the same set of "interactions" managed at `[base]/[type]`. Servers SHALL provide a CapabilityStatement (`GET [base]/metadata`) saying which resources and interactions they support; the API itself "does not directly address authentication, authorization, and audit" (see fhir-security.md). `http.md` and `search.md` are Normative (ANSI-approved); conditional create/update/patch/delete are marked *trial use* on the same page. Bundle is Normative; CapabilityStatement core is Normative with many flags `trial-use`.

## Conventions (`http`)
| Item | Rule |
|---|---|
| URL pattern style | `VERB [base]/[type]/[id] {?_format=[mime-type]}`; `[]` = mandatory literal, `{}` = optional |
| Service base URL | `http{s}://server{/path}`, no trailing slash; resource manager at `/[type]`; all URLs and ids are **case sensitive**; clients SHOULD encode URLs as UTF-8 |
| Reserved prefixes | `_` for system-wide search/history and all-resource parameters; `$` for operation names |
| Identity | query part ignored; `http:` vs `https:` SHALL NOT refer to different objects; different explicit port = different object |
| Metadata ↔ HTTP | `id` in URL; `meta.versionId` in `ETag` (weak: `ETag: W/"3141"`); `meta.lastUpdated` in `Last-Modified` |
| MIME types | `application/fhir+json`, `application/fhir+xml`, `application/fhir+turtle`; SHALL be used by clients and servers; UTF-8 SHALL be used; servers SHALL support server-driven content negotiation; generic `application/json` in Accept → server SHOULD answer with the FHIR JSON format; `406` when Accept unsupported, `415` when posted format unsupported |
| Version parameter | `Accept: application/fhir+json; fhirVersion=4.0` (R4 = `4.0`); on Content-Type and/or Accept; two different versions in one interaction is an error |
| General parameters | `_format` (servers SHOULD support; `json`/`application/json`/`application/fhir+json` SHALL mean JSON), `_pretty` (MAY), `_summary`, `_elements` |
| Prefer header | `Prefer: return=minimal` / `return=representation` / `return=OperationOutcome`; servers SHOULD honor; on failure servers SHOULD always return a body with an `OperationOutcome`; also `Prefer: handling=strict|lenient` for unknown search params (`search`) |
| Versioning levels | CapabilityStatement `rest.resource.versioning`: `no-version` / `versioned` / `versioned-update`; servers SHOULD provide full version support; servers without versioning SHALL omit `meta.versionId` and SHALL still update `meta.lastUpdated` |
| Security | HTTPS optional but production exchange SHOULD use SSL; servers SHOULD implement CORS |
| Status codes | FHIR only mandates codes "where the correct status code is not obvious"; `OperationOutcome` MAY accompany any 4xx/5xx |
| Conditional read | Client may send `If-Modified-Since` / `If-None-Match` on read and SHALL accept `304 Not Modified` or full content |
| HEAD | Allowed wherever GET is; servers not supporting it MUST respond per HTTP (e.g. `405` or `501`) |
| Custom headers | `X-Request-Id` (client or server assigned), `X-Correlation-Id` (server SHOULD return when it changed the request id), `X-Forwarded-For`, `X-Forwarded-Host`, `X-Intermediary` (SHALL be stamped by content-altering intermediaries; endpoints SHALL NOT use it) |
| `Date` header | If the server has a default timezone it SHOULD return it in the `Date` response header |

## Interaction table (`http` §3.1.0.2–3.1.0.12 and Summary §3.1.0.17)
"Required headers" = what the page marks R or SHALL on request/response. All requests MAY carry `Accept`.

| Interaction | Verb + URL | Request body / headers | Success status | Required response headers | Other codes listed |
|---|---|---|---|---|---|
| read | `GET [base]/[type]/[id]` | none; optional `If-Modified-Since`, `If-None-Match` | `200` | resource with `id` = `[id]`; SHOULD `ETag` (if versioned) + `Last-Modified` (summary table marks R) | `404` unknown, `410` deleted, `304` conditional |
| vread | `GET [base]/[type]/[id]/_history/[vid]` | none | `200` | `id` = `[id]`, `meta.versionId` = `[vid]`; `ETag` + `Last-Modified` | `404` (history not supported), `410` (deleted version) |
| update | `PUT [base]/[type]/[id]` | Resource whose `id` SHALL equal URL id; `Content-Type` R; optional `If-Match`, `Prefer` | `200` updated, `201` created (SHOULD add `Location`) | `ETag` with new versionId, `Last-Modified` | `400` id mismatch/parse, `401`, `404`, `405` client-defined id not allowed, `409`/`412` version conflict, `422` business rules |
| conditional update | `PUT [base]/[type]?[search params]` | Resource, `id` optional (SHALL be ignored) | as update | as update | `400` one match but id differs, `412` multiple matches; unsupported → SHOULD `400` |
| patch | `PATCH [base]/[type]/[id]` | body SHALL be JSON Patch (`application/json-patch+json`), XML Patch (`application/xml-patch+xml`) or FHIRPath Patch `Parameters`; optional `If-Match`, `Prefer` | `200`, `201` | `ETag`, `Last-Modified` | `400`, `404`, `405`, `409`, `412`, `422`; servers SHALL support conditional (version-aware) PATCH; conditional-by-search PATCH: `404` no match, `412` multiple |
| delete | `DELETE [base]/[type]/[id]` | body SHALL be empty | `200` (with payload), `204` (no payload), `202` (non-committal) | none (optional `OperationOutcome`, MAY `ETag`) | `404`, `405` type-level refusal, `409` referential integrity, `412` |
| conditional delete | `DELETE [base]/[type]/?[search params]` | none | as delete | — | multiple matches: delete all or `412` (declared in `rest.resource.conditionalDelete`) |
| create | `POST [base]/[type]` | Resource (`id` SHALL be ignored; `meta.versionId`/`lastUpdated` SHALL be ignored); `Content-Type` R; optional `If-None-Exist`, `Prefer` | `201` | `Location: [base]/[type]/[id]/_history/[vid]` SHALL; SHOULD `ETag` + `Last-Modified` | `400` parse/basic validation, `404`, `405`, `422` profile/business rules |
| conditional create | `POST [base]/[type]` + `If-None-Exist: [search params]` | as create | `201` none matched; `200` one match (post ignored) | — | `412` multiple matches |
| search | `GET [base]/[type]{?params}` and `POST [base]/[type]/_search` (`Content-Type: application/x-www-form-urlencoded`; servers SHALL support the POST form) | none / form data | `200` + Bundle `type=searchset` | — | `400` cannot process, `401`, `403` refused, `404`; failure SHALL be 4xx/5xx with `OperationOutcome`; empty result is not a failure |
| search (compartment) | `GET [base]/[Compartment]/[id]/[type]{?params}` or `.../[id]/*` | none | `200` searchset | — | — |
| search-all | `GET [base]?_type=A,B&params` or `GET [base]?params` | none | `200` searchset | — | SHOULD `400` when a param is not common to all listed types |
| capabilities | `GET [base]/metadata{?mode=full|normative|terminology}` | none | `200` + CapabilityStatement (or TerminologyCapabilities for `mode=terminology`; servers MAY ignore `mode`) | SHOULD `ETag`, SHALL change when content changes | `404` = FHIR not supported at this URL |
| transaction | `POST [base]` with Bundle `type=transaction` | `Content-Type` R; each entry SHALL carry `request`; PUT/POST entries SHALL contain a resource | `200` + Bundle `transaction-response` | — | reject all with `400` or `500`-type and a single `OperationOutcome`; `404`, `405`, `409`, `412`, `422` |
| batch | `POST [base]` with Bundle `type=batch` | as transaction | `200` + Bundle `batch-response` regardless of per-entry success | — | per-entry status inside `entry.response.status` |
| history (instance / type / system) | `GET [base]/[type]/[id]/_history`, `GET [base]/[type]/_history`, `GET [base]/_history` | none; params `_count`, `_since` (instant), `_at`, `_list` (each SHALL NOT repeat) | `200` + Bundle `type=history`, oldest versions last, includes deletes | — | `404` + OperationOutcome when history not kept |
| operation | `POST [base]/$[name]`, `[base]/[type]/$[name]`, `[base]/[type]/[id]/$[name]` (`GET` allowed when all params primitive and `affectsState=false`; servers SHALL support that GET form) | `Parameters` resource (or the single Resource input as body) | `200` (2xx; `303` possible) + `Parameters`, or the resource itself when the only out parameter is `return` | — | 4xx/5xx SHOULD carry `OperationOutcome` |

### Update / create details worth keeping
- Update-as-create (`PUT` to a non-existent id) is a server choice, declared in `rest.resource.updateCreate`; otherwise `405`.
- Servers MAY reject updates for business rules ("usually a `422`"); `400` ≈ fails CapabilityStatement-documented constraints, `422` ≈ other business rules — the page says servers need not tightly adhere.
- Concurrency: servers SHOULD always return `ETag`; client sends `If-Match: W/"23"`; mismatch → `412 Precondition Failed`; server MAY require `If-Match` by answering `400` when absent; `409 Conflict` when the update cannot be done (e.g. pessimistic locking).
- Deleted then re-`PUT` = "brought back to life" (`201`).
- Transactional integrity: servers SHOULD change the resource as little as possible but MAY alter it; both sides SHOULD document handling in the CapabilityStatement.
- Servers not supporting conditional interactions or batch/transaction SHOULD return `400` and MAY include an `OperationOutcome`.

### Transaction processing rules (`http` §3.1.0.11.2)
1. Process `DELETE`s, 2. `POST`s, 3. `PUT`/`PATCH`, 4. `GET`/`HEAD`, 5. resolve conditional references.
- Outcome SHALL NOT depend on entry order; a resource may appear only once (by identity); overlapping identities in steps 1–3 → transaction SHALL fail.
- Server SHALL rewrite references to POSTed resources whose id it assigned — in references, `uri`/`url`/`oid`/`uuid` elements and narrative `<a href>`/`<img src>`; `canonical` is not replaced.
- Conditional references (`"reference": "Patient?identifier=12345"`, transaction only): servers SHALL search; no match or multiple → transaction fails; single match → replace.
- Batch: SHALL have no interdependencies between entries; references between entries created in the batch are non-conformant.
- Servers SHOULD accept a `history` Bundle POSTed to `[base]` (treat as transaction/batch).

### Paging (`http` §3.1.0.14)
- Servers SHOULD support paging for search/history and, if so, SHALL use `Bundle.link` with `relation` `self` (SHALL be returned; carries the parameters actually used), `first`, `previous`, `next`, `last` (optional but recommended). Links are opaque to the client. `Bundle.total` MAY report the total. Follow-up pages are GET; servers SHOULD allow POST too.

## Search (`search`)
Contexts: `[base]/[type]?…`, compartment `[base]/Patient/[id]/[type]?…`, all types `[base]?…` (params must be common to all types, or to the `_type` list). Search parameter names are case sensitive. Servers are not required to implement any standard parameter except `_id`, and MAY define their own (SHOULD start with `-`). Servers SHOULD ignore unknown/unsupported parameters (client may force `Prefer: handling=strict`). Servers SHALL reject a modifier they do not support for a parameter with `400` + OperationOutcome. Servers SHALL return the parameters actually used (self link); clients SHALL check them.

### Search parameter types
| Type | Definition (as written) | Value syntax / modifiers |
|---|---|---|
| number | "SHALL be a number (a whole number, or a decimal)"; implicit precision range (100 → [99.5, 100.5)) | prefixes `eq ne gt lt ge le sa eb ap` (`eq` default; `sa`/`eb` not for integers) |
| date | date/time or period; format `yyyy-mm-ddThh:mm:ss[Z|(+|-)hh:mm]`; populated from the left; minutes SHALL be present if hour is; SHOULD give time zone if time is present; servers SHALL handle escaped `:` | same prefixes; partial dates are intervals; matches `date`, `dateTime`, `instant`, `Period`, `Timing` |
| string | case- and accent-insensitive; default = starts-with after normalisation | `:exact` (entire value incl. case), `:contains`, `:text`; HumanName/Address search covers their string parts only |
| token | close-to-exact match "on a coded element or identifier"; matches literal, case sensitive unless the code system says otherwise (servers SHOULD lean case-insensitive when in doubt) | `[code]`, `[system]|[code]`, `|[code]` (no system), `[system]|` (any code); `:text`, `:not`, `:above`, `:below`, `:in`, `:not-in`, `:of-type` (`system|code|value`); for ContactPoint/uri/boolean the pipe SHALL NOT be used |
| reference | "A reference to another resource (Reference or canonical)" | `[id]`, `[type]/[id]`, `[url]`; relative and absolute forms match each other; `:[type]`, `:identifier` (then token semantics, no chaining), `:above`/`:below` for hierarchies; servers SHOULD reject a bare id matching several types |
| composite | joins two values with `$` (`code-value-quantity=http://loinc.org|8480-6$lt60`) | no modifiers |
| quantity | `[prefix][number]|[system]|[code]`; system/code optional (`5.4||mg` matches code or unit text) | prefixes as number; server MAY normalise via UCUM canonical units |
| uri | exact match on `uri`/`url` elements (case, accent, escape sensitive) | `:above`, `:below` (left-match); not for URNs/OIDs |
| special | logic defined per parameter | `_filter`, Location `near` |

- Universal modifier `:missing=true|false` (all types except composite).
- AND = repeat the parameter (`language=FR&language=NL`); OR = comma list (`language=FR,NL`); escaping: `\` before `$`, `,`, `|`, `\` — applied after URL %-decoding.
- Chaining: `subject.name=peter`, `subject:Patient.name=peter` (chains evaluated independently). Reverse chaining: `_has:Observation:patient:code=1234-5` (chainable).
- Parameters for all resources: `_id` (token, exact, case sensitive), `_lastUpdated` (date), `_tag` (token), `_profile` (uri in the summary table; "reference" in the prose — recorded as written), `_security` (token), `_text` (string, narrative), `_content` (string, whole resource), `_list`, `_query` (only one; unknown → SHALL refuse), `_filter`, `_source`, `_type`, `_has`.

### Search result (control) parameters
| Param | Type | Behaviour stated |
|---|---|---|
| `_sort` | string | comma list of search-parameter names, `-` prefix = descending; servers SHOULD honor; string sorts SHOULD be case-insensitive; `_score` for relevance |
| `_count` | number | max results per page for `entry.search.mode=match` only; servers SHALL NOT return more than requested (may return fewer); SHOULD repeat `_count` in page links; `_count=0` ≡ `_summary=count` |
| `_include` | string | `SourceType:searchParam(:targetType)`; repeat the parameter for multiple; `*` wildcard; `:iterate` for recursive; included entries get `search.mode=include`; missing/unresolvable targets are silently omitted; each page SHOULD carry its own includes |
| `_revinclude` | string | same syntax; resources that refer *to* the matches (`Provenance:target`) |
| `_summary` | string | `true` (elements flagged summary, SHOULD only those), `text` (text+id+meta+top-level mandatory), `data` (drop text), `count` (search only, no entries), `false`; not mixable with `_include`/`_revinclude` when `text`; servers SHOULD tag subset resources `SUBSETTED` |
| `_total` | string (trial-use) | `none` / `estimate` / `accurate` — hint only; `Bundle.total` stays optional |
| `_elements` | string | comma list of top-level elements; servers SHOULD always return mandatory elements and tag `SUBSETTED` |
| `_contained` / `_containedType` | string | `false` (default)/`true`/`both`; `container` (default)/`contained` |

Cross-map (search type → data types, from the summary table): number ← decimal, integer; date ← date, dateTime, instant, Period, Timing; reference ← Reference, canonical, uri; quantity ← Quantity, Age, Duration, Money, Range; uri ← uri, canonical; string ← string, HumanName, Address; token ← boolean, code, id, string, CodeableConcept, Coding, ContactPoint, Identifier.

## Operations (`operations`)
- Named with `$`; endpoints: system `[base]/$[name]`, type `[base]/[type]/$[name]`, instance `[base]/[type]/[id]/$[name]`.
- Invoked by `POST` with a `Parameters` resource ("in" params; search-typed params may carry modifiers like `code:in`); `GET` with URL params only when all inputs are primitive and `affectsState = false` — servers SHALL support that GET form. Exactly one Resource input → may POST that resource directly. No-parameter state-changing operation → `POST` with `Content-Length: 0`.
- Response: `Parameters` with "out" params; if the single out param is named `return` and is a Resource, the response MAY be that resource alone. Bundle responses use `type=collection` unless they have search semantics. Success is 2xx (or `303`); 4xx/5xx SHOULD return `OperationOutcome`. Binary results behave like a `read` of Binary.
- Operations are "subject to the same security constraints and requirements as the RESTful API"; implementation-defined operations are allowed (name clashes resolved via the CapabilityStatement); spec never defines parameter names starting with `x-`.

## Bundle (`bundle`)
| Element | Card. | Type | Notes |
|---|---|---|---|
| `identifier` | 0..1 | Identifier | persistent id; document bundles SHALL have system+value (bdl-9) |
| `type` | 1..1 | code (required binding) | `document` \| `message` \| `transaction` \| `transaction-response` \| `batch` \| `batch-response` \| `history` \| `searchset` \| `collection` |
| `timestamp` | 0..1 | instant | when assembled; required for `document` (bdl-10) |
| `total` | 0..1 | unsignedInt | only for `searchset`/`history` (bdl-1); counts `match` entries across all pages, not includes/outcomes |
| `link` | 0..* | BackboneElement | `relation` 1..1 string (IANA), `url` 1..1 uri |
| `entry` | 0..* | BackboneElement | order meaningful per type; `document`/`message` first entry SHALL be Composition/MessageHeader (bdl-11/12) |
| `entry.fullUrl` | 0..1 | uri | SHALL NOT disagree with resource `id`; version-independent (bdl-8: no `/_history/`); unique per bundle unless versionId differs (bdl-7, except history); may be `urn:uuid:` |
| `entry.resource` | 0..1 | Resource | bdl-5: resource, request or response must exist |
| `entry.search` | 0..1 | — | `searchset` only (bdl-2); `mode` 0..1 `match` \| `include` \| `outcome`; `score` 0..1 decimal 0–1 |
| `entry.request` | 0..1 | — | mandatory for batch/transaction/history, otherwise prohibited (bdl-3); `method` 1..1 `GET|HEAD|POST|PUT|DELETE|PATCH`, `url` 1..1 (relative to base), `ifNoneMatch`, `ifModifiedSince`, `ifMatch`, `ifNoneExist` (query part only) |
| `entry.response` | 0..1 | — | mandatory for batch-response/transaction-response/history, otherwise prohibited (bdl-4); `status` 1..1 string starting with the 3-digit code, `location`, `etag`, `lastModified`, `outcome` (OperationOutcome) |
| `signature` | 0..1 | Signature (TU) | XML-DSig or JWT |

Bundle types and their rules:
| Type | Rule stated |
|---|---|
| `document` | first entry is a Composition; every entry SHALL contain a resource |
| `message` | first entry is a MessageHeader; every entry SHALL contain a resource |
| `searchset` | 0..* entries, each SHALL contain a resource; `total` = matches reachable via `next` |
| `history` | each entry SHALL contain `request`; a resource when method is POST/PUT; `response` SHALL also be present (location) |
| `transaction` / `batch` | each entry SHALL contain `request`; PUT/POST entries SHALL contain a resource |
| `transaction-response` / `batch-response` | one entry per request entry, same order; each SHALL contain `response` |
| `collection` | 0..* entries, each SHALL contain a resource; no defined use |

- Except transactions/batches, each entry must have a `fullUrl`; unidentified resources use `urn:uuid:`. A given version of a resource SHALL only appear once per Bundle.
- Reference resolution inside a bundle: relative `[type]/[id]` + RESTful `fullUrl` root → absolute, then match `fullUrl`; else try the URL externally; versioned references matched after stripping `/_history/` and checking `meta.versionId`.
- POSTing to `/Bundle` stores the bundle as a static resource (not processed as transaction/batch/message). Bundle search params: `composition`, `identifier`, `message`, `timestamp`, `type`.

## CapabilityStatement (`capabilitystatement`)
Three kinds: `instance` (`implementation` must be present, `software` may be; what `/metadata` returns), `capability` (`software` present, `implementation` absent), `requirements` (both absent) — enforced by cpb-14/15/16. Servers SHALL specify supported resource types and operations, SHOULD specify profiles per resource; "Resource Types or operations that are not listed are not supported". Servers that require authentication SHOULD still return a CapabilityStatement before authentication. One statement per supported FHIR version.

Elements marked `R!` in the JSON template (mandatory) and the ones our server must fill:
| Element | Card. / binding | Values |
|---|---|---|
| `status` | R!, required binding | `draft` \| `active` \| `retired` \| `unknown` |
| `date` | R! | last changed |
| `kind` | R!, required binding | `instance` \| `capability` \| `requirements` |
| `fhirVersion` | R!, required binding (FHIRVersion) | e.g. `4.0.1` |
| `format` | R! 1..*, required binding (mime types) | `xml` \| `json` \| `ttl` \| mime type |
| `patchFormat` | 0..* | patch mime types supported |
| `implementationGuide` | 0..* canonical | IGs supported |
| `software.name` | R! within `software` | plus `version`, `releaseDate` |
| `implementation.description` | R! within `implementation` | plus `url` (base URL), `custodian` |
| `rest.mode` | R!, required binding | `client` \| `server` |
| `rest.security` | 0..1 | `cors` boolean, `service` (extensible: `OAuth` \| `SMART-on-FHIR` \| `NTLM` \| `Basic` \| `Kerberos` \| `Certificates`), `description` |
| `rest.resource.type` | R! (one entry per type, cpb-9) | resource type |
| `rest.resource.profile` / `supportedProfile` | canonical(StructureDefinition) | base profile / use-case profiles |
| `rest.resource.interaction.code` | R! per interaction, required binding | `read` \| `vread` \| `update` \| `patch` \| `delete` \| `history-instance` \| `history-type` \| `create` \| `search-type` |
| `rest.resource.versioning` | required binding | `no-version` \| `versioned` \| `versioned-update` |
| `rest.resource.readHistory`, `updateCreate`, `conditionalCreate`, `conditionalUpdate` | boolean | feature flags |
| `rest.resource.conditionalRead` | code | `not-supported` \| `modified-since` \| `not-match` \| `full-support` |
| `rest.resource.conditionalDelete` | code | `not-supported` \| `single` \| `multiple` |
| `rest.resource.referencePolicy` | 0..* code | `literal` \| `logical` \| `resolves` \| `enforced` \| `local` |
| `rest.resource.searchInclude` / `searchRevInclude` | 0..* string | supported `_include` / `_revinclude` values |
| `rest.resource.searchParam` | 0..* | `name` R!, `definition` canonical(SearchParameter), `type` R! (`number|date|string|token|reference|composite|quantity|uri|special`), `documentation`; names unique per resource (cpb-12) |
| `rest.resource.operation` | 0..* | `name` R!, `definition` R! canonical(OperationDefinition) |
| `rest.interaction.code` | required binding | `transaction` \| `batch` \| `search-system` \| `history-system` |
| `rest.searchParam`, `rest.operation`, `rest.compartment` | 0..* | system-level params/ops; canonical(CompartmentDefinition) served |
| `messaging`, `document` | 0..* | not needed for a pure REST server |

Invariants: cpb-1 SHALL have at least one of `rest`, `messaging`, `document`; cpb-2 SHALL have at least one of `description`, `software`, `implementation`; cpb-3 messaging endpoint only when `kind = instance`; cpb-0 (warning) `name` matches `[A-Z]([A-Za-z0-9_]){0,254}`.

## Notes for our server
- Serve `GET [base]/metadata` returning a `CapabilityStatement` with `kind=instance`, `status=active`, `date`, `fhirVersion=4.0.1`, `format=["json"]` (add `application/fhir+json`), `implementation.description` + `implementation.url`, `software.name/version`, `rest[0].mode=server`, `rest.security.service=OAuth` (or `SMART-on-FHIR`) + `cors=true`, and one `rest.resource` per supported type listing every `interaction.code`, `searchParam` (name+type), `versioning`, `updateCreate`, `conditionalCreate/Update/Delete`, `supportedProfile` (our SATUSEHAT-derived profiles). Anything not listed is by definition unsupported; return it before auth.
- Implement at minimum read, vread, create, update (with `If-Match`/`412`), delete (`204`), search (`GET` and `POST …/_search`), history-instance, transaction and batch; emit `ETag: W/"<versionId>"`, `Last-Modified`, `Location: [base]/[type]/[id]/_history/[vid]` on `201`, and honor `Prefer: return=*`.
- Content negotiation: accept `application/fhir+json` and `application/json`, `_format=json`; answer `406`/`415` on unsupported formats; decode URLs as UTF-8; treat `[type]`/`[id]` case-sensitively.
- Search engine: index by parameter type (token for `identifier`/`code`/`status`, reference for `subject`/`patient`/`encounter`, date for `date`/`_lastUpdated`, quantity for `value-quantity`); support `:missing`, `:exact`, `:not`, `:identifier`, prefixes on date/number/quantity, AND/OR and `\` escaping; SHALL reject unsupported modifiers with `400`; always return the `self` link with the parameters actually applied plus `next`/`previous` links; `_count` hard cap; `_include`/`_revinclude` for `Observation:patient`, `Observation:device`, `Encounter:*` as declared in `searchInclude`.
- SATUSEHAT usage (see satusehat-*.md) only needs create/`PUT`/`PATCH`/search; the device-sourced vital-sign feed maps to `POST Observation` (optionally `If-None-Exist: identifier=…` to dedupe device readings) or a `transaction` Bundle with `urn:uuid:` fullUrls and conditional references `Patient?identifier=…`.
- Transactions: process in DELETE→POST→PUT/PATCH→GET order, fail atomically with a single `OperationOutcome`, rewrite `urn:uuid:` references, and refuse cross-entry references in `batch`.
- Log search URLs as PHI (the spec says logs are "as sensitive as the resources themselves").

## Sources
- raw/fhir-r4/http.md
- raw/fhir-r4/search.md
- raw/fhir-r4/operations.md
- raw/fhir-r4/bundle.md
- raw/fhir-r4/capabilitystatement.md

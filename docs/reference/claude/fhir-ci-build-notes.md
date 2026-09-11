# FHIR CI build (R6 draft) — documentation index and developer overview

> **WARNING — NOT NORMATIVE FOR SATUSEHAT.** Both raw pages come from `https://build.fhir.org/` (frontmatter `fhir_version: R6-ci`), which the pages themselves label "the Continuous Integration Build of FHIR (will be incorrect/inconsistent at times)". SATUSEHAT is FHIR **R4** (see satusehat-overview.md). Use this file only for orientation on how the spec is organised and for statements that are the same in R4; for any rule, verb, status code, element or cardinality use the `fhir-r4/*` views (fhir-rest-api.md, fhir-datamodel-basics.md, …). Anything below that is not confirmed by an R4 page is marked *(CI only)*.

## Documentation index structure (`fhir-ci/documentation`)
The index page is Informative and lists "the key commonly used background documentation pages" plus a link to "the list of 119 resources" *(CI only — R4 has a different count)*. `[I]` = only informative content (no SHALL/SHOULD rules).

| Column | Group | Pages listed (page names as printed) |
|---|---|---|
| 1 | Framework | Conformance Rules; References between Resources; Compartments; Narrative; Extensibility; FHIR NPM Packages; FHIRPath, Patch & X-FHIR-Query; Terminologies (Code Systems [I], Value Sets [I], Terminology Service); Mappings to other standards [I]; Resource Life Cycles [I] |
| 1 | Version Management | Change Management & Versioning; Managing Multiple FHIR Versions [I]; Version History [I]; Differences to Release 4 [I]; Transforms between Release 4 and Release 5 [I] |
| 1 | Background [I] | Overviews: General, Developers, Clinical, Architects; 1 page Summary (Glossy); Glossary (Multi-Language); License and Legal Terms; Community & Credits; Appendix: Coming Challenges for Healthcare |
| 1 | ANSI Documentation [I] | HL7, ANSI and the FHIR Standard |
| 2 | Exchanging Resources (how to choose [I]) | **RESTful API (HTTP)**; Search (Search Param Registry [I]); Operations; Using GraphQL; Operations for Large Resources [I]; Asynchronous Use [I]; Documents; Messaging; Subscriptions Framework; Services [I]; Persistence/Data bases [I] |
| 2 | Resource Definitions | Resource Formats; UML Definition; XML Format; JSON Format; ND-JSON Format; RDF Definition |
| 2 | Datatypes | Metadata Types; ElementDefinition; Dosage; MarketingStatus; ProductShelfLife |
| 2 | Type Framework | Resource; DomainResource; CanonicalResource; MetadataResource |
| 3 | Adopting & Using FHIR | Profiling FHIR; Implementation Obligations; Mapping Language (tutorial [I]); FHIR Workflow [I]; Downloads – Schemas, Code, Tools [I]; Managing Multiple FHIR Versions [I]; Validating Resources [I]; Logical models [I]; Best Practices for Implementers [I]; Testing Implementations [I] |
| 3 | Safety & Security | Security, Security Labels & Signatures; Clinical Safety [I] |
| 3 | Implementation Advice [I] | Managing Resource Identity; Guide to Resources; Multi-language support; Variations between Submitted data and Retrieved data; Push vs Pull; Integrated Examples; Common Use Cases |
| 3 | Relationship to Other Standards [I] | v2 Messaging; v3 Messaging; CDA (see also CDA on FHIR); Other Specifications |

Where our R4 corpus maps onto this index: Framework → `conformance-rules`, `references`, `narrative`, `extensibility`; Exchanging → `http`, `search`, `operations`; Datatypes → `datatypes`, `elementdefinition`; Adopting → `profiling`, `workflow`, `validation`; Safety & Security → `security`, `secpriv-module`. Pages such as `CanonicalResource`, `MetadataResource`, `Implementation Obligations`, `Subscriptions Framework`, `ND-JSON`, `Operations for Large Resources` are R5/R6 additions *(CI only)* and have no R4 counterpart in the corpus.

## Developer overview — version-independent points (`fhir-ci/overview-dev`)
Statements below also hold in R4 (cross-checked against `http.md`, `datatypes.md`, `bundle.md`, `references.md`); anything R6-specific is marked.

| Topic | What the overview says | R4 confirmation |
|---|---|---|
| Resource features | every resource has an identifier (typically a URL where it is found), common metadata, a human-readable XHTML summary, a defined set of data elements per type, an extensibility framework | fhir-datamodel-basics.md (narrative, Meta), fhir-profiling.md |
| Formats | instances are XML, JSON or RDF (Turtle); "currently 119 different resource types" *(CI only)* | `http.md` MIME types (R4 count differs) |
| Instance anatomy | `resourceType` required; `id` always present except during create; `meta` usually present (infrastructure-managed); `text` recommended; `extension` optional; data elements per type; JSON property order not significant | fhir-rest-api.md create rules |
| URL identity | REST URL is `[base]/[resourceType]/[id]`, not stored inside the resource; publication-cycle resources carry an explicit canonical `url` that stays constant across copies | `http.md` service base URL; `references.md` canonical URLs |
| Interactions | Create `POST {base}/{type}`; Read `GET {base}/{type}/{id}`; Update `PUT …/{id}`; Patch `PATCH …/{id}`; Delete `DELETE …/{id}`; Search `GET {base}/{type}?…`; History `GET …/{id}/_history`; Transaction `POST {base}/`; Operation `GET …/{id}/${opname}` | fhir-rest-api.md interaction table (R4 says operations are generally POST; GET only for stateless primitive-parameter operations) |
| Variability | no central authority; extension framework + "profiles" on base resources for richer content (blood-pressure example: simple observation vs. rich vital-sign profile) | fhir-profiling.md, fhir-observation.md |
| Three meanings of "version" | FHIR version (fixed by context/CapabilityStatement); record version (`meta.versionId`, three server support levels: none / versionId without history / versionId with history; version-aware updates optional); business version (`version` element on published content) | `http.md` §Support for Versions (`no-version`/`versioned`/`versioned-update`), `references.md` canonical `\|version` |
| Create example | `POST /base/Patient` with `Authorization: Bearer …`, `Accept`/`Content-Type: application/fhir+json`, UTF-8 always; client id is overwritten by the server; no `meta` yet; response `201 Created` + `ETag: W/"1"` + `Location: …/Patient/f001`; OperationOutcome body optional and has no `id`/`meta`; HTTP/1.1 "strongly recommended but not required" | fhir-rest-api.md create row |
| Error example | `422 Unprocessable Entity` + `OperationOutcome` (business rule: MRN already assigned); content errors use an appropriate HTTP status with OperationOutcome | `http.md` 400 vs 422 guidance |
| Read example | `GET /base/Patient/f001?_format=xml`; response `200` with `Last-Modified`, `ETag: W/"1"`; `id` must match the request; `versionId` best practice equals the ETag but clients must never assume it; `lastUpdated` must match the header; cache control is outside FHIR | `http.md` read/metadata mapping |
| Search example | `GET {base}/MedicationRequest?patient=347` → Bundle `type=searchset` with server-assigned unique `id`, `timestamp` (same or newer than newest resource), `total` (all matches, not this page), `link` names `first`, `prev`, `next`, `last`, `self`; entries may include related resources | fhir-rest-api.md search/paging (R4 link names `first`, `previous`, `next`, `last`, `self` — note `prev` vs `previous` wording differs *(CI only)*) |
| Update example | `PUT /base/Patient/f001` with `If-Match`; URL type and id must match the body; `If-Match` must match `meta.versionId` and the server must check it or return `412` if it does not support versions; `meta.lastUpdated` in the body is ignored; server may create at a new id ("update as create"); response `200`, `ETag: W/"2"`, `Location: …/_history/2` | fhir-rest-api.md update row (R4: `412` on mismatch; `If-Match` shown as `W/"23"`) |
| Base resource content | `meta.versionId` changes on any content change except `profile`, `security`, `tag`; `meta.lastUpdated` changes with versionId; `meta.profile` = conformance assertion; `meta.security` = security labels linked to the security policy, updatable by the security subsystem; `meta.tag` = workflow tags applications need not interpret; `implicitRules` (discouraged); `language` = base language | `http.md` metadata table; `search.md` `_profile`/`_security`/`_tag`; `references.md` contained-resource meta rules |

## Notes for our server
- Treat this file as a map, not a rulebook: when the CI wording and an R4 page differ (e.g. operation invocation verb, `prev` vs `previous` link name, resource count), the R4 page wins for SATUSEHAT compatibility.
- The developer walkthrough is a good acceptance-test script shape for our implementation: create (`201` + `Location` + `ETag`), read (`200` + `Last-Modified` + `ETag`, ids match), search (`searchset` with `self`/`next` links and `total`), update with `If-Match` (`200`/`412`), business-rule rejection (`422` + OperationOutcome) — all of which are also mandated by `http.md`.
- Persist `meta` exactly as described: bump `versionId` and `lastUpdated` on content changes, allow `profile`/`security`/`tag` to be edited by the security/validation subsystem without a content version bump only if we document it (R4 `http.md` says servers SHALL update `lastUpdated` correctly).
- Do not cite R6-only pages (CanonicalResource, Subscriptions Framework, Implementation Obligations, ND-JSON) in the design; they have no R4 equivalent in the corpus.

## Sources
- raw/fhir-ci/documentation.md
- raw/fhir-ci/overview-dev.md

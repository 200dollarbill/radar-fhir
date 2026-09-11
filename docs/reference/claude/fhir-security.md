# FHIR R4 — Security and Privacy

Summary: "FHIR is not a security protocol, nor does it define any security related functionality." It assumes an external security sub-system (authentication, access-control decision engine, audit log) deployed in front of or behind the FHIR API, and supplies building blocks: security labels on `meta.security`, `AuditEvent`, `Provenance`, `Consent`, `Signature`, and a non-active-content narrative. `security.md` is Trial Use (maturity 4); `secpriv-module.md` is Informative. Neither page defines user, role or permission resources — "FHIR does not provide user, profile, or other such administration resources".

## The eleven security topics (`security` summary list, as written)
| # | Topic | Statement |
|---|---|---|
| 1 | Time keeping | all clocks should be synchronized using NTP/SNTP; design robust against a wrong system clock |
| 2 | Communications security | all exchange of production data should be secured using TLS (e.g. https) |
| 3 | Authentication | users/clients must be authenticated; for web-centric, OAuth is recommended (a profile of OAuth will be needed; consider SMART-on-FHIR) |
| 4 | Authorization / access control | FHIR defines a Security Label infrastructure; "may also define a set of resources to administer access control management, but does not define any at present" |
| 5 | Audit | `Provenance` and `AuditEvent` resources track origins, authorship, history, status and access |
| 6 | Digital signatures | reserved locations for signatures (Bundle.signature, Provenance.signature) |
| 7 | Attachments | binary resources/attachments "have their own concerns" (may contain executable code) |
| 8 | Labels | security-related tags that affect how resources are handled |
| 9 | Data management policies | not every FHIR capability is legal in every jurisdiction (HIPAA, GDPR cited); implementer's responsibility |
| 10 | Narrative | care must be taken when displaying narrative |
| 11 | Input validation | validate all input; test with fuzzing, invalid input and injection attacks |

## Sensitivity classes for READ/QUERY guidance (`security` §6.1.0.2)
"Most Resources will need some form of Access Control to Create, Update, or Delete." For reads:
| Class | Description | Suggested protection |
|---|---|---|
| Anonymous READ | no individual or business data (e.g. conformance resources) | server-authenticated https for integrity |
| Business sensitive | organisation/location/service data, not individuals | client authentication: mutual-TLS, APIKey, app-signed JWT, OAuth client-id JWT |
| Individual sensitive | Practitioner, PractitionerRole, CareTeam, other users | role-specific access via RBAC or ABAC |
| Patient sensitive | "the bulk of FHIR" — clinical data | security labels for confidentiality levels; often a declared Purpose Of Use; often governed by `Consent` |
| Not classified | Bundle, Composition, Group, List… (variable) | special handling; metadata drives decisions |

## Communications (`security` §6.1.0.3)
- Normal HTTP security rules (RFC 7231 §9). The service base URL specifies whether TLS is required; client certificates may be required.
- Follow BCP 195: TLS 1.2 or higher for production, forbid SSL, strong cipher suites (e.g. AES). Consider DNSSEC.
- Responses to non-authorized clients: HTTP headers and error messages must not disclose details of the underlying web server.
- Servers SHOULD consider enabling CORS for browser-based clients (`http.md` says servers SHOULD implement CORS).
- Audit logging of GET parameters into an unprotected log is called out as an endpoint risk.

## Authentication (`security` §6.1.0.4)
- "Other than testing systems, FHIR servers should authenticate the clients" — either the client system (and trust it) or the individual user.
- Recommended: OpenID Connect to identify end users; OAuth to authenticate/authorize client and user; SMART-on-FHIR profile of OAuth; HEART and IHE IUA cited as OAuth profiles for healthcare.
- "All systems are shall protect authenticator mechanisms" (sic — page text), choosing credential strength by risk.
- CapabilityStatement can advertise `rest.security.service` = `OAuth` | `SMART-on-FHIR` | `NTLM` | `Basic` | `Kerberos` | `Certificates` and `rest.security.cors` (see fhir-rest-api.md).

## Authorization / access control (`security` §6.1.0.5, `secpriv-module` §6.0.5.1–2)
- Principle: data is not communicated unless the other party is authorized — for PUT/POST as much as GET.
- Two models named: **RBAC** (permissions = CRUDE operations — Create, Read, Update, Delete, Execute — on resource types, grouped into roles assigned to users; "FHIR readily enables RBAC") and **ABAC** (policies over attributes: security tags, environment, user and object characteristics).
- Decision inputs listed: client (identity, role, location, level of assurance), resource (confidentiality, sensitivity, type, date range, author), patient (identity, relationship to user, consent), context (system identity, time-of-day, purpose of use, workflow state, transport security).
- Access control MAY redact or restrict data returned by read/search.
- Roles should be conveyed with codes from the Security Role Vocabulary; purpose of use with the PurposeOfUse vocabulary; with OAuth these travel in the token (JWT) managed by the authorization service.
- **Access-control considerations checklist** (all access paths must be evaluated): basic CRUD; chained search (both the searched and the chained resource); `_include`/`_revinclude` (access to included resources); security labels; container resources (Bundle, Composition, Group, List — does access to the container grant access to contents?); operations that disclose patient data (page names them: Fetch Encounter Record, Evaluate Measure, Observation Statistics, Find Patient Matches using MPI-based Logic, Fetch Patient Record); batch/transaction (authorize each action); Break-the-Glass protocol.
- Query-parameter policy (`secpriv-module`): when a restricted user queries beyond their rights, local policy decides between error, zero data, or results after dropping the unauthorized parameters (e.g. silently dropping `_include`).

### Access-denied responses (`security` §6.1.0.5.2)
| Response | What it leaks / when to use |
|---|---|
| `200` + empty Bundle | indistinguishable from "no data"; hides which patients exist; only when a Bundle is a valid result |
| `404 Not Found` | indistinguishable from non-existent resource; leaks that authentication succeeded |
| `403 Forbidden` | says it is an authorization failure; only when the user may know that |
| `401 Unauthorized` | authentication attempted and failed |
Caveat: if the server allows update-as-create (`PUT` to a new id), `404` is not feasible and clients can probe existence.

## Audit (`security` §6.1.0.6, `secpriv-module` §6.0.5.3–4)
- `AuditEvent` records security/privacy-relevant events "as much detail as reasonable at the time"; aligned with IHE ATNA; usable for reporting, alerting, filtering, forwarding; clients can search or subscribe to them.
- Use case quoted: "A FHIR server should keep a complete, tamper-proof log of all API access and other security- and privacy-relevant events". "All uses of FHIR Resources would be security/privacy relevant and thus should be recorded in an AuditEvent."
- HTTP logs (even URL-only) should be regarded as being as sensitive as the resources themselves.
- Accounting of Disclosures / access report for the patient: derived from AuditEvent (Who, What, Where, When, Why); must de-duplicate and protect the accessor's privacy; disclosures may be recorded as an explicit disclosure AuditEvent.
- Read operations are recorded with `AuditEvent`; create/update/delete provenance with `Provenance` (`?_revinclude=Provenance:target` returns provenance with query results).

## Security labels (`security` §6.1.0.8, `secpriv-module`)
- Resources carry labels in `meta.security`; the security system uses them (plus resource content) to decide authorization; searchable via `_security` (token).
- Named label vocabularies on these pages: confidentiality/sensitivity levels for patient-sensitive data; integrity labels after de-identification `ANONYED`, `MASKED`, `PSEUDED`, `REDACTED`; PurposeOfUse `HTEST` for test data; `SUBSETTED` on partial resources (from `search.md`). Break-the-glass is defined on the security-labels page (not in corpus).

## Consent, Provenance, Signature, De-identification, Test data (`secpriv-module`)
| Building block | Statement |
|---|---|
| `Consent` | records current privacy-consent state; meaning of presence/absence is local policy; may point to external policy (XACML id) or scanned signature; simple base+exception rules |
| `Provenance` | who/what/where/when/why for Create, Update, Delete or any activity; carries `signature` |
| Signatures | prove authenticity, integrity, non-repudiation via `Provenance.signature`; server-managed changes on create/update (id, lastUpdated) break prior signatures — sign after the REST create completes |
| De-identification | pseudonymization + anonymization; direct identifiers on Observation: `.identifier .subject .performer .encounter .focus .note .specimen .basedOn`; indirect: `.category .code .issued .effective[x] .method .bodySite .interpretation .value[x] .component`; label results |
| Test data | isolate on a test server, or tag with PurposeOfUse `HTEST`, or use an obviously-test Patient |

## Narrative / XSS (`security` §6.1.0.9)
- Narrative is XHTML that "can't contain active content" (see fhir-datamodel-basics.md). Still: validate the narrative; external image/anchor references may leak headers or let a host track display; do not run external links in a privileged context; separate API sessions from browser sessions (cookie theft via `text/html` content is the cited attack); document CSS may reference external content — check before following.

## Mapping admin / doctor / patient roles to the mechanisms these pages describe
The pages do not define a role model. What they do provide, mapped to our three roles:
| Role | Mechanism the spec names | How it applies |
|---|---|---|
| all | OAuth / SMART-on-FHIR / OpenID Connect; role + purpose-of-use codes in the JWT (Security Role Vocabulary, PurposeOfUse) | one bearer-token flow; token carries role claim and purpose of use |
| admin | "Business sensitive" and "Individual sensitive" classes → client authentication + RBAC on Organization, Location, Practitioner, PractitionerRole, Device | CRUDE permissions on administrative resource types; sees AuditEvent for reporting |
| doctor | RBAC on patient-sensitive types; ABAC inputs "patient relationship to the user", encounter/workflow state; Break-the-Glass noted | CRUD on clinical resources (Observation, Encounter, Condition, Procedure…) scoped by relationship; every access → AuditEvent |
| patient | Compartment-scoped URLs (`http.md`: a base path or OAuth login can bind the API to one patient, "see Compartments"); `Patient/[id]/[type]` searches; Accounting-of-Disclosures report from AuditEvent; `Consent` | read-only view of own compartment; access report derived from AuditEvent |
| device / integration client | "authenticate the client system and trust it" (mutual-TLS, APIKey, app-signed JWT, OAuth client-id JWT) | POST Observation only, under a system identity |

## Notes for our server
- TLS 1.2+ only, no SSL; a single OAuth2/OIDC issuer; every request authenticated (client-credentials for device feeders and SATUSEHAT-style integration clients, user tokens for admin/doctor/patient); JWT claims: role (Security Role Vocabulary code), purpose of use, and for patients the bound `Patient/[id]`.
- Authorization layer evaluates the spec's checklist: CRUD per type per role, chained search targets, `_include`/`_revinclude` targets, compartment membership for patient tokens, each entry in a transaction/batch, and `$everything`-style operations. Policy for over-reaching queries: drop unauthorized `_include`s (documented) or return `403` for doctors/admins; return `404` or empty `searchset` to patient tokens to avoid existence leaks; never expose server details in error bodies.
- Choose one access-denied strategy per role and record it in `CapabilityStatement.rest.security.description`; do not enable update-as-create for patient-scope tokens (it defeats `404`).
- Write an `AuditEvent` for every interaction (reads included) and a `Provenance` for every create/update/delete; treat HTTP access logs as PHI; expose `AuditEvent` search to admins and a filtered "accounting of disclosures" view to patients.
- Tag resources with `meta.security`: confidentiality level on clinical data, `HTEST` on seed/test data, `SUBSETTED` on `_summary`/`_elements` responses, `ANONYED`/`PSEUDED` on any de-identified exports.
- Sanitize `text.div` on write (reject scripts/event handlers/object; strip or reject external `src`/`href`) and serve API responses only as `application/fhir+json`, never `text/html`, with API sessions separate from any web UI cookies.
- Sync clocks (NTP) — `meta.lastUpdated`, token expiry and the SATUSEHAT future-date rule all depend on it.

## Sources
- raw/fhir-r4/security.md
- raw/fhir-r4/secpriv-module.md

# Validity review — claim tables, part 2

Continuation of [VALIDITY-REVIEW.md](VALIDITY-REVIEW.md) (systemic issues S1–S29, the Observation / Patient / Encounter / Device-related claims, summary and consequences live there). Same columns, continuous numbering; `S#` references point to the systemic table in the entry file.

## Claim-by-claim — Practitioner and PractitionerRole (satusehat-practitioner.md ↔ fhir-practitioner-practitionerrole.md)
| # | SATUSEHAT claim (file) | FHIR R4 source | Verdict | Note |
|---|---|---|---|---|
| 123 | `identifier[i]` Identifier; NIK system `https://fhir.kemkes.go.id/id/nik` (satusehat-practitioner.md) | fhir-practitioner-practitionerrole.md: Practitioner.identifier 0..* | satusehat-specific constraint | Same NIK URI as Patient. |
| 124 | `active` boolean | Practitioner.active 0..1 boolean | confirmed | — |
| 125 | `name[i]` HumanName | Practitioner.name 0..* HumanName | confirmed | — |
| 126 | `telecom[i]` ContactPoint (phone, email) | Practitioner.telecom 0..* ContactPoint | confirmed | — |
| 127 | `address[i]` Address with use/type/text/line/city/district/state/postalCode/country/period | Practitioner.address 0..* Address; fhir-datamodel-basics.md Address children | confirmed | No value sets named; R4 binds `use`/`type` (required). |
| 128 | `gender` code; search API accepts `male`/`female` only | Practitioner.gender 0..1, Required AdministrativeGender | satusehat-specific constraint | Subset. |
| 129 | `birthDate` date | Practitioner.birthDate 0..1 date | confirmed | — |
| 130 | `photo[i]` Attachment | Practitioner.photo 0..* Attachment | confirmed | — |
| 131 | `qualification[i]`: identifier[i], period, issuer Reference(Organization) | Practitioner.qualification 0..*; qualification.identifier 0..*, period 0..1, issuer 0..1 Reference(Organization) | confirmed | — |
| 132 | `*qualification.code` wajib within qualification; `*qualification.code.coding` wajib | qualification.code 1..1 CodeableConcept, Example v2.0360; CodeableConcept.coding 0..* | satusehat-specific constraint | `code` 1..1 confirmed; `coding` ≥1 is tighter; no system named. |
| 133 | `communication[i]` CodeableConcept with coding | Practitioner.communication 0..* CodeableConcept, Preferred CommonLanguages | confirmed | — |
| 134 | Practitioner is read-only for faskes: only `GET ?identifier=nik\|<nik>`, `GET ?name&birthdate&gender` (all three wajib), `GET /:id` | Practitioner search params `identifier`, `name`, `gender`; **no `birthdate` search parameter is defined for Practitioner in R4**; fhir-rest-api.md: servers MAY define their own parameters | satusehat-specific constraint | `birthdate` is a custom parameter on Practitioner; read-only surface is policy. |
| 135 | Practitioner IHS number (`N10000001` / `10009880728`) is `Practitioner.id`; no system URI stated | fhir-datamodel-basics.md: id `[A-Za-z0-9.-]{1,64}` | unverifiable | Looked for a Practitioner identifier system on res-/api-practitioner; none printed (S26). |
| 136 | PractitionerRole: search `?practitioner`, `?practitioner&organization` (both wajib), read, POST, PUT, PATCH replace | PractitionerRole search params `practitioner` (reference), `organization` (reference); fhir-rest-api.md interactions | satusehat-specific constraint | Standard params; no profile page so no element rules (S23 for the copy-paste). |

## Claim-by-claim — Organization and Location (satusehat-organization-location.md ↔ fhir-organization-location.md)
| # | SATUSEHAT claim (file) | FHIR R4 source | Verdict | Note |
|---|---|---|---|---|
| 137 | Organization `identifier[i]` internal code, `use` official; system `http://sys-ids.kemkes.go.id/organization/{organization-ihs-number}` (satusehat-organization-location.md) | Organization.identifier 0..* Identifier | satusehat-specific constraint | — |
| 138 | Organization `active` boolean | Organization.active 0..1 (?!) | confirmed | — |
| 139 | Organization `type[i]` from `organization-type`, e.g. `dept` | Organization.type 0..*, Example OrganizationType | confirmed | — |
| 140 | Organization `name` string; `alias[i]` string | Organization.name 0..1 string; alias 0..* | confirmed | org-1 (identifier or name) not restated. |
| 141 | Organization `telecom[i]` ContactPoint (`contact-point-system`, `contact-point-use`), may repeat | Organization.telecom 0..*; org-3: use never `home` | confirmed | Examples use `work`, satisfying org-3. |
| 142 | Organization `address[i]` Address with `address-use`, `address-type`, `administrativeCode` extension (province/city/district/village) | Organization.address 0..*; org-2: use never `home` | satusehat-specific constraint | Extension is local; examples use `work`. |
| 143 | Organization `partOf` Reference(Organization) — **wajib when the organisation is a suborganisation**; Tahap 1 IHS number, Tahap 2 server UUID | Organization.partOf 0..1 Reference(Organization) | satusehat-specific constraint | Conditional min 1 (profile invariant). |
| 144 | Organization `contact[i]` purpose/name/telecom/address; `*contact.purpose.coding` wajib within; system `contactentity-type` \| `BILL`; `name.use` from `name-use` | Organization.contact 0..*; contact.purpose 0..1, Extensible ContactEntityType (raw organization.md names `contactentity-type`) | satusehat-specific constraint | `purpose.coding` ≥1 while `purpose` itself is 0..1 in base. |
| 145 | Organization `endpoint[i]` Reference to Endpoint, profile `https://fhir.kemkes.go.id/r4/StructureDefinition/Endpoint` | Organization.endpoint 0..* Reference(Endpoint) | satusehat-specific constraint | Profile canonical not in corpus. |
| 146 | Location `identifier[i]` internal code; system `http://sys-ids.kemkes.go.id/location/{organization-ihs-number}`; search token `.../location/<id-lokasi-induk>\|<nomor>` | Location.identifier 0..*; search `identifier` token | satusehat-specific constraint | S23 for the wilayah wording. |
| 147 | Location `status` code `location-status`, e.g. `active` | Location.status 0..1 (?!), Required LocationStatus; raw names `location-status` | confirmed | — |
| 148 | Location `operationalStatus` Coding from `v2-0116`, e.g. `O` | Location.operationalStatus 0..1 Coding, Preferred v2.0116 | confirmed | — |
| 149 | Location `name`, `alias[i]`, `description` strings | Location.name 0..1, alias 0..*, description 0..1 | confirmed | — |
| 150 | Location `mode` code `location-mode`: `instance` vs `kind` | Location.mode 0..1, Required LocationMode; raw names `location-mode` | confirmed | — |
| 151 | Location `type[i]` from `v3-RoleCode`, e.g. `ICU` | Location.type 0..*, Extensible v3.ServiceDeliveryLocationRoleType | confirmed | R4 value set is the ServiceDeliveryLocationRoleType subset of v3 RoleCode. |
| 152 | Location `telecom[i]` ContactPoint | Location.telecom 0..* | confirmed | — |
| 153 | Location `address` Address with `administrativeCode` extension (province…rw) | Location.address 0..1 Address | satusehat-specific constraint | Extension local. |
| 154 | Location `physicalType.coding` from `location-physical-type`, e.g. `ro` | Location.physicalType 0..1 CodeableConcept, Example LocationType | confirmed | — |
| 155 | Location `position` with `*longitude`, `*latitude` decimal (wajib within), `altitude` optional | Location.position 0..1; position.longitude 1..1, latitude 1..1, altitude 0..1 decimal | confirmed | Example values look swapped (S15). |
| 156 | Location `managingOrganization` Reference(Organization) (IHS number, then UUID) | Location.managingOrganization 0..1 Reference(Organization) | confirmed | — |
| 157 | Location `partOf` Reference `Location/{uuid}` | Location.partOf 0..1 Reference(Location) | confirmed | — |
| 158 | Location `hoursOfOperation[i]` daysOfWeek (`days-of-week`), allDay, openingTime/closingTime `time` | hoursOfOperation 0..*; daysOfWeek 0..* Required DaysOfWeek; allDay boolean; openingTime/closingTime time | confirmed | — |
| 159 | Location `availabilityExceptions` string | Location.availabilityExceptions 0..1 string | confirmed | — |
| 160 | Location `endpoint[i]` Reference(Endpoint) | Location.endpoint 0..* Reference(Endpoint) | confirmed | — |
| 161 | `*Location.extension.serviceClass` wajib: ward class Kelas 1/2/3/VIP/VVIP (LocationServiceClass) | fhir-profiling.md: extension = `url` 1..1 + value; profiles may require an extension (min 1) | satusehat-specific constraint | URL not printed (S18). |
| 162 | Organization search `?name`, `?partof`; Location search `?identifier`, `?name`, `?organization`; read; POST/PUT/PATCH-replace on both | Organization search `name`, `partof`; Location search `identifier`, `name`, `organization` | confirmed | All standard R4 parameters. |
| 163 | RuleNumber 10171: PATCH `Location` must use path `/operationalStatus`, not `/operationalStatus/system` | fhir-rest-api.md: JSON Patch per RFC 6902 (any valid path) | satusehat-specific constraint | Path restriction is SATUSEHAT policy. |
| 164 | Facility master (MSI): `kode_satusehat` 10 digits as the organisation IHS number; `jenis_sarana` 101–104 (satusehat-identifiers-and-master-data.md) | no R4 counterpart | unverifiable | National registry API, not FHIR. |

## Claim-by-claim — Condition (satusehat-condition.md ↔ fhir-condition.md)
| # | SATUSEHAT claim (file) | FHIR R4 source | Verdict | Note |
|---|---|---|---|---|
| 165 | `identifier[i]` local diagnosis number, `use` official; system `http://sys-ids.kemkes.go.id/condition/{organization-ihs-number}` (satusehat-condition.md) | Condition.identifier 0..* | satusehat-specific constraint | Doubled braces on the page (S6). |
| 166 | `clinicalStatus` from `http://terminology.hl7.org/CodeSystem/condition-clinical`, e.g. `active` | Condition.clinicalStatus 0..1 (?!), Required; con-4 prints that CodeSystem URI | confirmed | con-3 (guideline) / con-4 / con-5 not restated. |
| 167 | `verificationStatus` named system `http://terminology.hl7.org/CodeSystem/condition-ver-status`, e.g. `provisional` | Condition.verificationStatus 0..1 (?!), Required; con-3/con-5 print that URI | confirmed | — |
| 168 | `verificationStatus` example system `https://www.hl7.org/fhir/Codesystem-condition-ver-status` | same: R4 defines the system as `http://terminology.hl7.org/CodeSystem/condition-ver-status` | conflict | Code-system URI defined differently by R4 (S14). |
| 169 | `category[i]` from `condition-category`, e.g. `encounter-diagnosis`; use-case adds kemkes `http://terminology.kemkes.go.id` \| `chief-complaint` / `previous-condition` | Condition.category 0..*, Extensible ConditionCategoryCodes | satusehat-specific constraint | Extensible binding admits the kemkes categories. |
| 170 | `severity` SNOMED, e.g. `24484000` | Condition.severity 0..1, Preferred Condition/DiagnosisSeverity | confirmed | — |
| 171 | `*code` wajib; ICD-10 `http://hl7.org/fhir/sid/icd-10` (or kemkes `clinical-term` at discharge); **one ICD-10 code per Condition** | Condition.code 0..1, Example; CodeableConcept.coding 0..* | satusehat-specific constraint | min 1, single coding, fixed systems — all tighter. ICD-10 URI not on captured R4 pages (see terminology rows). |
| 172 | `bodySite[i]` SNOMED, e.g. `111002` | Condition.bodySite 0..*, Example SNOMEDCTBodyStructures | confirmed | — |
| 173 | `*subject` Reference `Patient/{patient-ihs-number}` (types Patient \| Group) | Condition.subject 1..1 Reference(Patient \| Group) | satusehat-specific constraint | Cardinality confirmed; Group excluded in practice. |
| 174 | `*encounter` Reference(Encounter) wajib | Condition.encounter 0..1 Reference(Encounter) | satusehat-specific constraint | min raised to 1. |
| 175 | `onset[x]` dateTime / Age / Period (`YYYY-MM-DD`) / Range / string | Condition.onset[x] 0..1 same five types | confirmed | Period sub-headings mislabeled (S16). |
| 176 | `abatement[x]` same five types | Condition.abatement[x] 0..1 same | confirmed | con-4 applies. |
| 177 | `recordedDate` dateTime | Condition.recordedDate 0..1 dateTime | confirmed | — |
| 178 | `recorder` Reference(Practitioner \| PractitionerRole \| Patient \| RelatedPerson), format `Practitioner/{ihs}` | Condition.recorder 0..1 same targets | confirmed | — |
| 179 | `asserter` same targets | Condition.asserter 0..1 same targets | confirmed | — |
| 180 | `stage[i]` summary (SNOMED), assessment[i] Reference(ClinicalImpression \| DiagnosticReport \| Observation), type (SNOMED) | Condition.stage 0..*; summary 0..1, assessment 0..*, type 0..1 | confirmed | con-1 (summary or assessment) not restated. |
| 181 | `evidence[i]` code[i] (SNOMED), detail[i] Reference(Any) | Condition.evidence 0..*; code 0..*, detail 0..* Reference(Any) | confirmed | con-2 not restated. |
| 182 | `note[i]` Annotation | Condition.note 0..* Annotation | confirmed | — |
| 183 | Search `?subject` (string) and/or `?encounter` (uuid); read; POST; PUT; PATCH replace | fhir-condition.md search `subject`, `encounter` (both reference type) | confirmed | Types printed as string/uuid are API-doc shorthand; values are R4 reference ids. |
| 184 | Chief complaint = separate Condition (kemkes category `chief-complaint`, SNOMED ECL `< 404684003`) referenced from `Encounter.diagnosis` with `use` `CC` (use-case step 3) | Condition.code Example binding; Encounter.diagnosis.use Preferred DiagnosisRole | satusehat-specific constraint | Valid under Example/Preferred bindings. |

## Claim-by-claim — Procedure (satusehat-procedure.md ↔ fhir-procedure.md)
`focalDevice`, `usedReference` and `usedCode` are reviewed in the Device-related table of VALIDITY-REVIEW.md; RuleNumbers 10124 and `duplicate` in its Encounter table; the vital-sign LOINC table in its Observation table.
| # | SATUSEHAT claim (file) | FHIR R4 source | Verdict | Note |
|---|---|---|---|---|
| 185 | `identifier[i]` local id, `use` official; system `http://sys-ids.kemkes.go.id/procedure/{organization-ihs-number}` (satusehat-procedure.md) | Procedure.identifier 0..* | satusehat-specific constraint | Trailing-slash variant (S6). |
| 186 | `instantiatesCanonical[i]` canonical, `instantiatesUri[i]` uri | Procedure.instantiatesCanonical 0..*, instantiatesUri 0..* | confirmed | — |
| 187 | `basedOn[i]` Reference(CarePlan \| ServiceRequest) | Procedure.basedOn 0..* same | confirmed | — |
| 188 | `partOf[i]` Reference(Procedure \| Observation \| MedicationAdministration) | Procedure.partOf 0..* same | confirmed | — |
| 189 | `*status` code `http://hl7.org/fhir/event-status`, e.g. `completed` | Procedure.status 1..1 (?!), Required EventStatus; raw procedure.md names `event-status` | confirmed | — |
| 190 | `statusReason` SNOMED, value set `procedure-not-performed-reason` | Procedure.statusReason 0..1, Example ProcedureNotPerformedReason(SNOMED-CT) | confirmed | — |
| 191 | `category` SNOMED, e.g. `103693007`; use-case ECL `< 71388002` | Procedure.category 0..1, Example ProcedureCategoryCodes(SNOMEDCT) | confirmed | — |
| 192 | `*code` wajib with `*code.coding`; ICD-9-CM `http://hl7.org/fhir/sid/icd-9-cm`, e.g. `87.44` (use-case adds SNOMED ECL and KPTL) | Procedure.code 0..1, Example ProcedureCodes(SNOMEDCT); coding 0..* | satusehat-specific constraint | min 1 and coding ≥1 tighter; ICD-9-CM URI not on captured R4 pages. |
| 193 | `*subject` Reference `Patient/{ihs}` (types Patient \| Group) | Procedure.subject 1..1 Reference(Patient \| Group) | satusehat-specific constraint | Cardinality confirmed; Group excluded. |
| 194 | `*encounter` Reference(Encounter) wajib | Procedure.encounter 0..1 | satusehat-specific constraint | min raised to 1. |
| 195 | `performed[x]` dateTime / Period / string / Age / Range | Procedure.performed[x] 0..1 same five types | confirmed | `+01:00` examples are valid dateTimes. |
| 196 | `recorder` / `asserter` Reference(Patient \| RelatedPerson \| Practitioner \| PractitionerRole) | Procedure.recorder, asserter 0..1 same targets | confirmed | — |
| 197 | `performer[i]` BackboneElement; `performer.function` SNOMED (ProcedurePerformerRoleCodes) | Procedure.performer 0..*; function 0..1, Example ProcedurePerformerRoleCodes | confirmed | — |
| 198 | `*performer.actor` wajib within performer; Reference(Practitioner \| PractitionerRole \| Organization \| Patient \| RelatedPerson \| Device) | performer.actor 1..1 same targets | confirmed | — |
| 199 | `performer.onBehalfOf` Reference(Organization) | performer.onBehalfOf 0..1 Reference(Organization) | confirmed | — |
| 200 | `location` Reference(Location) | Procedure.location 0..1 Reference(Location) | confirmed | — |
| 201 | `reasonCode[i]` ICD-10 `http://hl7.org/fhir/sid/icd-10`, e.g. `A15.0` | Procedure.reasonCode 0..*, Example ProcedureReasonCodes | satusehat-specific constraint | Example binding admits ICD-10. |
| 202 | `reasonReference[i]` Reference(Condition \| Observation \| Procedure \| DiagnosticReport \| DocumentReference) | Procedure.reasonReference 0..* same | confirmed | — |
| 203 | `bodySite[i]` SNOMED, e.g. `302551006` | Procedure.bodySite 0..*, Example SNOMEDCTBodyStructures | confirmed | — |
| 204 | `outcome` SNOMED, e.g. `385669000` | Procedure.outcome 0..1, Example ProcedureOutcomeCodes(SNOMEDCT) | confirmed | Description copy-pasted (S23). |
| 205 | `report[i]` Reference(DiagnosticReport \| DocumentReference \| Composition) | Procedure.report 0..* same | confirmed | — |
| 206 | `complication[i]` ICD-10, e.g. `A41.9`; `complicationDetail[i]` Reference(Condition) | Procedure.complication 0..*, Example Condition/Problem/DiagnosisCodes; complicationDetail 0..* Reference(Condition) | satusehat-specific constraint | ICD-10 under an Example binding. |
| 207 | `followUp[i]` SNOMED, value set `procedure-followup` | Procedure.followUp 0..*, Example ProcedureFollowUpCodes(SNOMED CT) | confirmed | — |
| 208 | `note[i]` Annotation with authorReference `Practitioner/{ihs}`, time, text | Procedure.note 0..* Annotation; fhir-datamodel-basics.md Annotation (author[x] Reference(Practitioner…), time, text 1..1) | confirmed | Sub-headings `note[i].note.time` (S16). |
| 209 | Search `?subject` and/or `?encounter`; read; POST; PUT; PATCH replace | fhir-procedure.md search `subject`, `encounter` | confirmed | — |
| 210 | Education recorded as a Procedure with category SNOMED `409073007` and two `code` codings (KPTL `10913` + SNOMED) (use-case step 21) | Procedure.code CodeableConcept.coding 0..* (translations) | satusehat-specific constraint | Two codings in one CodeableConcept is valid R4. |

## Claim-by-claim — RelatedPerson (satusehat-related-person.md ↔ fhir-patient-person-relatedperson.md)
| # | SATUSEHAT claim (file) | FHIR R4 source | Verdict | Note |
|---|---|---|---|---|
| 211 | `identifier[i]` Identifier, `use` official, `value` NIK; system `https://fhir.kemkes.go.id/id/nik` (satusehat-related-person.md) | RelatedPerson.identifier 0..* | satusehat-specific constraint | — |
| 212 | `active` boolean | RelatedPerson.active 0..1 (?!) | confirmed | — |
| 213 | `*patient` Reference(Patient) wajib | RelatedPerson.patient 1..1 Reference(Patient) | confirmed | — |
| 214 | `relationship[i]` from `v3-RoleCode`, e.g. `NMTH`; MPI newborn flow uses `MTH` | RelatedPerson.relationship 0..*, Preferred PatientRelationshipType | confirmed | R4 value set draws on v3 RoleCode; URI not printed on captured page. |
| 215 | `name[i]` HumanName | RelatedPerson.name 0..* | confirmed | — |
| 216 | `telecom[i]` ContactPoint (`contact-point-system`, `contact-point-use`) | RelatedPerson.telecom 0..* | confirmed | — |
| 217 | `gender` code, e.g. `female`; no value set named | RelatedPerson.gender 0..1, Required AdministrativeGender | confirmed | Server must enforce the Required binding SATUSEHAT omits. |
| 218 | `birthDate` date | RelatedPerson.birthDate 0..1 date | confirmed | — |
| 219 | `address[i]` Address (use, line, city, postalCode, country) | RelatedPerson.address 0..* Address | confirmed | — |
| 220 | `photo[i]` Attachment; `period` Period | RelatedPerson.photo 0..*; period 0..1 | confirmed | — |
| 221 | `communication[i]`; `*communication.language` wajib within; `*language.coding` wajib; `urn:ietf:bcp:47` (`en`, `en-US`, `id-ID`) | RelatedPerson.communication 0..*; communication.language 1..1, Preferred CommonLanguages; coding 0..* | satusehat-specific constraint | `language` 1..1 confirmed; `coding` ≥1 tighter. |
| 222 | `communication.preferred` boolean | communication.preferred 0..1 boolean | confirmed | — |
| 223 | No REST endpoints documented; `Patient.link.other` → `RelatedPerson/{uuid}` with `type` `refer` | fhir-patient-person-relatedperson.md: link.other Reference(Patient \| RelatedPerson); mother/newborn example uses `see-also` | confirmed | `refer` is a valid LinkType; R4's own example uses `seealso`. |
| 224 | Newborn RelatedPerson minimum data (MPI): UUID id, identifier IHS, patient IHS, relationship, name, gender, birthDate, address, phone — all wajib | RelatedPerson table: only `patient` 1..1 | satusehat-specific constraint | min 1 set on several elements. |

## Claim-by-claim — Data types (satusehat-datatypes.md ↔ fhir-datamodel-basics.md)
| # | SATUSEHAT claim (file) | FHIR R4 source | Verdict | Note |
|---|---|---|---|---|
| 225 | `boolean` true/false; `integer` 32-bit; `decimal` rational (satusehat-datatypes.md) | fhir-datamodel-basics.md primitive table | confirmed | — |
| 226 | `string` ≤ 1,048,576 characters, code points ≥ 32 except tab/CR/LF, non-empty | string: SHALL NOT exceed 1 MB; SHOULD not contain code points < 32 except tab/CR/LF; SHOULD contain non-whitespace | confirmed | R4 phrases the limit in bytes and the others as SHOULD. |
| 227 | `uri` RFC 3986, case sensitive, UUID lowercase; `url` RFC 1738; `canonical`; `base64binary` RFC 4648; `oid`; `uuid` RFC 4122 | primitive table rows uri/url/canonical/base64Binary/oid/uuid | confirmed | — |
| 228 | `instant` `YYYY-MM-DDThh:mm:ss.sss+zz:zz`, at least seconds and a zone | instant: SHALL be at least to the second and SHALL include a time zone | confirmed | — |
| 229 | `date` `YYYY` / `YYYY-MM` / `YYYY-MM-DD` | date: same three precisions, no time zone | confirmed | — |
| 230 | `dateTime` four precisions, zone with time, `24:00` not allowed | dateTime: same; zone SHALL be populated when hours/minutes given; `24:00` not allowed | confirmed | — |
| 231 | `time` `hh:mm:ss` | time: `hh:mm:ss`, no zone, no `24:00` | confirmed | — |
| 232 | `code` defined elsewhere; `id` `[A-Za-z0-9.-]` ≤ 64; `markdown` | code, id `[A-Za-z0-9\-\.]{1,64}`, markdown rows | confirmed | — |
| 233 | `unsignedInt` `0..2,147,483,647` ("bilangan negatif" typo); `positiveInt` `1..2,147,483,647` | unsignedInt 0..2,147,483,647; positiveInt 1..2,147,483,647 | confirmed | Typo (S25). |
| 234 | `Address`: `*use`, `*type` mandatory; use from "IdentifierUse" (link AddressUse); `district`=kecamatan, `state`=kelurahan mapping | Address.use 0..1 (?!) `home\|work\|temp\|old\|billing`; type 0..1 `postal\|physical\|both`; city/district/state 0..1 string (no semantics printed) | satusehat-specific constraint | Tightening to 1..1 is a valid restriction but contradicts the MPI pages (S25); the state=kelurahan mapping is unverifiable against captured R4 text. |
| 235 | `Annotation`: `?authorReference`/`?authorString`, `time`, `*text` markdown | Annotation.author[x] 0..1, time 0..1, text 1..1 markdown | confirmed | — |
| 236 | `Attachment`: contentType, language, data, url, size, hash (SHA-1), title, creation | Attachment same elements; att-1 (contentType when data present) | confirmed | att-1 not restated. |
| 237 | `CodeableConcept` coding[] + text; `Coding` system/version/code/display/userSelected | CodeableConcept, Coding tables | confirmed | — |
| 238 | `CodeableReference` (concept + reference) listed as an R4 data type (Umum and Khusus pages) | raw/fhir-r4/datatypes.md: no `CodeableReference` entry (grep 0 hits); fhir-datamodel-basics.md lists none | conflict | Type does not exist in R4 (introduced in R5). |
| 239 | `RatioRange` (lowNumerator/highNumerator/denominator) listed as an R4 data type | raw/fhir-r4/datatypes.md: no `RatioRange` entry (grep 0 hits) | conflict | Type does not exist in R4 (R5). |
| 240 | `ContactPoint` system phone/fax/email/pager/url/sms; use home/work/temp/old/mobile; rank | ContactPoint.system also includes `other`; use same; rank positiveInt; cpt-2 | confirmed | `other` omitted; cpt-2 (system required when value present) not restated. |
| 241 | `HumanName` use usual/official/temp/nickname/anonymous/old/maiden; text/family/given[]/prefix[]/suffix[]/period | HumanName table | confirmed | — |
| 242 | `Identifier` use usual/official/temp/secondary/old; type, system, value, period, assigner | Identifier table | confirmed | — |
| 243 | `Money` value + ISO 4217 currency; `Period` start/end dateTime; `Range` low/high SimpleQuantity; `Ratio` numerator/denominator | Money, Period, Range (rng-2), Ratio (rat-1) rows | confirmed | Invariants not restated. |
| 244 | `Quantity`: `comparator` WAJIB when the value is approximate; `system` WAJIB when `unit` is filled | Quantity.comparator 0..1 (absent = point value); qty-3: `system` SHALL be present if `code` is present | satusehat-specific constraint | R4 ties `system` to `code`, not `unit`; SATUSEHAT's rule is stricter and does not restate qty-3. |
| 245 | `Reference`: reference/type/identifier/display; one of reference, identifier, display must be present | fhir-datamodel-basics.md Reference: at least one of the three SHALL be present (unless an extension) | confirmed | — |
| 246 | `SampledData`: `origin: [SimpleQuantity]`, `period: [decimal]`, `dimensions: [positiveInt]` (arrays) | SampledData origin 1..1 SimpleQuantity, period 1..1 decimal, dimensions 1..1 positiveInt | conflict | Type/cardinality mismatch: scalars printed as arrays; a JSON array on a 1..1 element is invalid. |
| 247 | `Signature`: `when: [instant]`, `who: [Reference]` (arrays) | Signature.when 1..1 instant, who 1..1 Reference | conflict | Same array-for-scalar mismatch. |
| 248 | `Timing`: event[], repeat {bounds[x], count…, durationUnit, frequency, period, periodUnit, dayOfWeek, timeOfDay, when, offset}, code | Timing row (event, repeat children, code); tim-1…tim-10 | confirmed | Invariants not restated. |
| 249 | `Age`, `Distance`, `Duration`, `Count`, `MoneyQuantity`, `SimpleQuantity` are Quantity variants | Quantity variants row (age-1, drt-1, cnt-3, dis-1, sqty-1) | confirmed | — |
| 250 | Metadata types (`ContactDetail`, `Contributor`, `DataRequirement`, `Expression`, `ParameterDefinition`, `RelatedArtifact`, `TriggerDefinition`, `UsageContext`) with `*` markers | not captured (R4 `metadatatypes.html` not in corpus) | unverifiable | Looked in fhir-datamodel-basics.md and raw/fhir-r4/datatypes.md; only names appear. Not needed by our resources. |
| 251 | `Dosage` structure | not captured (`dosage.html`) | unverifiable | Pharmacy out of scope. |
| 252 | `Extension`: `*url`, `?value` (open type) | fhir-profiling.md: Extension.url 1..1 uri, value[x] 0..1; value or sub-extensions, not both | confirmed | — |
| 253 | `Meta`: versionId, lastUpdated, source, profile[], security[], tag[] | fhir-datamodel-basics.md Meta row: versionId, lastUpdated, profile, tag, security (from http/search pages) | confirmed | `source` not mentioned on captured pages (resource.html not in corpus). |
| 254 | `Narrative`: `*status`, `*div` xhtml; xhtml forbids head/body/scripts/forms/frames/objects | Narrative.status 1..1, div 1..1; forbidden list | confirmed | — |
| 255 | Marker convention `*` = WAJIB, `?` = wajib under a condition (choice) | fhir-profiling.md: profiles state min/max; choice `[x]` elements | confirmed | Presentation only. |

## Claim-by-claim — REST API basics and validation (satusehat-rest-api-and-validation.md ↔ fhir-rest-api.md, fhir-security.md, fhir-datamodel-basics.md)
| # | SATUSEHAT claim (file) | FHIR R4 source | Verdict | Note |
|---|---|---|---|---|
| 256 | One FHIR base per environment: `https://api-satusehat-stg.dto.kemkes.go.id/fhir-r4/v1` (sandbox), `https://api-satusehat.kemkes.go.id/fhir-r4/v1` (production) (satusehat-rest-api-and-validation.md) | fhir-rest-api.md: URL pattern `[base]/[type]/[id]`; `[base]` is server-defined | confirmed | — |
| 257 | Every request WAJIB authenticated: `Authorization: Bearer <access_token>` | fhir-security.md: every request authenticated; OAuth recommended; bearer-token flow | confirmed | R4 REST "does not directly address authentication". |
| 258 | Write calls (POST/PUT) send `Content-Type: application/json` | fhir-rest-api.md: MIME `application/fhir+json` SHALL be used by clients and servers; raw http.md ~279–283: the generic `application/json` tolerance applies to the Accept header only | conflict | Same fact pattern as row 32: SATUSEHAT mandates a media type R4 says clients SHALL NOT use for FHIR request bodies. |
| 259 | Onboarding resources (Patient, Practitioner, Organization, Location) must exist before any data transaction | fhir-datamodel-basics.md: literal references SHALL be resolvable; fhir-rest-api.md transaction can create referenced resources atomically | satusehat-specific constraint | Ordering is policy; R4 also allows a transaction Bundle. |
| 260 | Validation pipeline: FHIR Processor validates before the FHIR Server stores; any error → nothing written | fhir-rest-api.md create: `400` parse/basic validation, `422` profile/business rules; fhir-datamodel-basics.md validation aspects | confirmed | — |
| 261 | 4xx body is `OperationOutcome` `{resourceType, issue[{severity, code, details.text, expression}]}` | fhir-rest-api.md: OperationOutcome MAY accompany any 4xx/5xx; search failures SHALL carry one; OperationOutcome element table not captured | unverifiable | Looked for the OperationOutcome/IssueType pages; not in corpus, so `issue.code` `format` could not be checked against IssueType. |
| 262 | `issue.severity` only `error`; `issue.code` ∈ {`duplicate`, `format`, `value`} | not captured (IssueSeverity/IssueType value sets) | unverifiable | As above. |
| 263 | `issue.expression` = element path, e.g. `Encounter.serviceProvider` | not captured | unverifiable | As above. |
| 264 | `5xx` responses are `text/plain` (e.g. `Gateway Timeout`) | fhir-rest-api.md: on failure servers SHOULD return an OperationOutcome body | satusehat-specific constraint | Deviates from a SHOULD; not forbidden. |
| 265 | RuleNumber 10001 `Code not found` / 10002 `Invalid coding system`: codes must come from the listed systems (ICD-10, ICD-9 CM, LOINC, SNOMED CT, HL7) | fhir-observation.md etc.: bindings are mostly Example/Preferred/Extensible; only Required bindings SHALL be enforced in base R4 | satusehat-specific constraint | Enforcing a closed system list on Example-bound elements is a profile constraint. |
| 266 | RuleNumber 10117 `Invalid identifier system`: `Identifier.system` must be a SATUSEHAT system | fhir-datamodel-basics.md: Identifier.system 0..1 uri, any namespace | satusehat-specific constraint | — |
| 267 | RuleNumber 10132 (`format`): date-times must be `YYYY-MM-DDThh:mm:ss+00:00` (example rejects `2022-06-14` on `Composition.date`) | fhir-datamodel-basics.md: dateTime allows `YYYY-MM-DD` and any offset | satusehat-specific constraint | Tighter precision and fixed offset. |
| 268 | RuleNumber 10132 (`value`): no future dates; no past dates older than 31 August 2022 | no lower/upper bound in R4 | satusehat-specific constraint | Contradicts 03 June 2014 (S4). |
| 269 | UTC+00 rule: WIB −7 h, WITA −8 h, WIT −9 h; exceptions for genuinely future periods (appointments, expiry) | fhir-datamodel-basics.md: zone SHALL be present when time is given; value semantics unchanged by offset | satusehat-specific constraint | Any offset is equivalent in R4. |
| 270 | RuleNumber 10134: empty strings rejected | fhir-datamodel-basics.md: `""` is not valid; string SHOULD contain non-whitespace | confirmed | — |
| 271 | RuleNumber 10254: integers must not be quoted strings | fhir-datamodel-basics.md: integer is a JSON number | confirmed | — |
| 272 | RuleNumber 10263 `Element not found`: a `*` element is missing | fhir-profiling.md: profile `min` 1 → validator cardinality check | satusehat-specific constraint | — |
| 273 | PATCH: JSON Patch array, only `op: replace`, path like `/language` | fhir-rest-api.md: JSON Patch (RFC 6902, all ops) | satusehat-specific constraint | Content-type conflict counted in the Observation rows. |
| 274 | POST returns the resource with server-assigned `id` (UUID) that must be stored | fhir-rest-api.md create: `id` in body SHALL be ignored, server assigns; `201` + `Location` | confirmed | R4 also requires `Location: [base]/[type]/[id]/_history/[vid]`, not mentioned by SATUSEHAT. |
| 275 | PUT returns the payload sent | fhir-rest-api.md update: `200`; body per `Prefer` (representation) | confirmed | — |
| 276 | `*Content-Type: application/json` on GET detail | fhir-rest-api.md read: no request body, no Content-Type requirement | satusehat-specific constraint | Harmless template artefact (S19). |
| 277 | HTTP status codes listed on the preface: 200/201 (+Location)/202/204/206; 400/401/403/404/405/409/413/415/422/429; 500/501/503/504 (satusehat-overview.md) | fhir-rest-api.md interaction table lists 200/201/202/204/304/400/401/403/404/405/406/409/410/412/415/422 | confirmed | 206/413/429/5xx are generic HTTP; 304/406/410/412 missing from the preface. |
| 278 | RFC 2119 keywords: WAJIB=MUST, TIDAK BOLEH=MUST NOT, SEBAIKNYA=SHOULD, BOLEH=MAY | fhir-profiling.md SHALL/SHOULD/MAY conformance language | confirmed | — |
| 279 | `uuid` symbol = 36 characters; ISO 8601 forms incl. `Z` / `+0000` | fhir-datamodel-basics.md: uuid is `urn:uuid:` uri; dateTime zone form is `Z` or `±hh:mm` | satusehat-specific constraint | `+0000` (no colon) is not a valid R4 dateTime zone; only the preface prints it. |
| 280 | Bundle framework: `total` wajib for search; `entry.request/response` shapes (satusehat-overview.md) | fhir-rest-api.md Bundle: `total` 0..1 only for searchset/history (bdl-1); request/response per bdl-3/bdl-4 | satusehat-specific constraint | `total` is optional in base; SATUSEHAT always returns it. |
| 281 | Element JSON: primitives with `_name` sibling for id/extension; repeated primitives as parallel arrays with `null` | fhir-datamodel-basics.md: same JSON rules | confirmed | — |

## Claim-by-claim — Terminology (satusehat-terminology.md ↔ fhir-terminology-resources.md, fhir-observation.md, fhir-datamodel-basics.md)
| # | SATUSEHAT claim (file) | FHIR R4 source | Verdict | Note |
|---|---|---|---|---|
| 282 | ICD-10 (2010) is the diagnosis standard; system `http://hl7.org/fhir/sid/icd-10` (satusehat-terminology.md) | fhir-condition.md: Condition.code Example binding; URI not on any captured R4 page (grep `sid/icd-10` 0 hits) | unverifiable | Looked in raw/fhir-r4/*; the R4 terminologies-systems page is not in corpus. |
| 283 | ICD-9 CM (2010) for procedures; `http://hl7.org/fhir/sid/icd-9-cm` | fhir-procedure.md: Procedure.code Example binding; URI not captured | unverifiable | As above. |
| 284 | LOINC for lab tests, vital signs, sections; `http://loinc.org` | raw/fhir-r4/observation.md examples `http://loinc.org`; fhir-observation.md Example LOINCCodes | confirmed | — |
| 285 | SNOMED CT for clinical terms; `http://snomed.info/sct`; ECL constraints per use case | raw/fhir-r4/observation.md, datatypes.md use `http://snomed.info/sct` | confirmed | ECL is a SNOMED mechanism, not R4. |
| 286 | UCUM in every Quantity; `http://unitsofmeasure.org` | fhir-datamodel-basics.md: Quantity.code SHOULD be UCUM; raw observation.md `http://unitsofmeasure.org` | confirmed | R4 says SHOULD; SATUSEHAT mandates. |
| 287 | KPTL `http://terminology.kemkes.go.id/CodeSystem/kptl`; KFA `http://sys-ids.kemkes.go.id/kfa`; kemkes `clinical-term`, `discharge-disposition`, `locationServiceClass-Outpatient`, `locationUpgradeClass`, `medication-form`, bare `http://terminology.kemkes.go.id` | fhir-datamodel-basics.md: Coding.system = CodeSystem canonical, SHALL NOT be a value-set URL; fhir-terminology-resources.md CodeSystem.url | satusehat-specific constraint | Local code systems; a bare domain as `system` is unusual but not forbidden. |
| 288 | HL7 terminology systems `http://terminology.hl7.org/CodeSystem/...` for status/category value sets | fhir-condition.md con-4/con-5 print that host for condition-clinical and condition-ver-status; fhir-observation.md prints it only for data-absent-reason | confirmed | Other members of the list not printed on captured pages. |
| 289 | `urn:ietf:bcp:47` for languages (`id-ID`) | fhir-datamodel-basics.md: Attachment.language BCP-47; Patient/RelatedPerson `communication.language` CommonLanguages | unverifiable | Looked for the URI string in raw/fhir-r4/*; 0 hits. |
| 290 | WHO ATC `http://www.whocc.no/atc` (route); DICOM `http://dicom.nema.org/resources/ontology/DCM` | not captured | unverifiable | Out of scope. |
| 291 | ICD-O, ICD-MM, ICD-PM, national `X` lab codes — no URIs printed | — | unverifiable | Nothing to check. |
| 292 | Processor validates ICD-10, ICD-9 CM, LOINC, SNOMED CT and HL7 code systems on write | fhir-datamodel-basics.md validation aspects: bindings, terminology; fhir-terminology-resources.md `$validate-code` | satusehat-specific constraint | Closed-list enforcement (see REST rows). |
| 293 | Kemkes `clinical-term` → SNOMED migrations (prognosis, discharge condition, consciousness, follow-up, education) | fhir-terminology-resources.md: ConceptMap / supplements for mappings (not captured in detail) | satusehat-specific constraint | Keep as a local ConceptMap. |
| 294 | LOINC code shape: numeric with check digit `xxxxx-x`; Long Common Name recommended display | fhir-datamodel-basics.md: Coding.display SHALL be one of the system's displays | satusehat-specific constraint | LOINC rules; not R4 content. |
| 295 | Prescribing: `Medication.code` KFA `92`/`93` on MedicationRequest (`91` invalid), `93` on MedicationDispense | not captured (pharmacy resources) | unverifiable | Out of scope. |

## Claim-by-claim — Rawat Jalan use case and overview (satusehat-usecase-rawat-jalan.md, satusehat-overview.md ↔ fhir-workflow.md, resource files)
| # | SATUSEHAT claim (file) | FHIR R4 source | Verdict | Note |
|---|---|---|---|---|
| 296 | Posting order: Patient GET (1) → Encounter POST (2) → Condition/Observation/Procedure referencing `Encounter/{id}` (3–26) → Encounter PUT (27) → Composition (28) (satusehat-usecase-rawat-jalan.md) | fhir-workflow.md: Observation/Condition/Procedure are events with `encounter` 0..1 Reference(Encounter); fhir-datamodel-basics.md references SHALL be resolvable | satusehat-specific constraint | Order follows from referential integrity; R4 does not prescribe it. |
| 297 | Prerequisites: token → Organization → Location → Practitioner IHS (→ Patient IHS) | same | satusehat-specific constraint | "4 langkah / 5 steps" (S23). |
| 298 | Step 2 Encounter wajib set: identifier, status, statusHistory, class, classHistory, subject, participant.type/individual, period, diagnosis.condition, hospitalization.dischargeDisposition, location, serviceProvider | fhir-encounter.md: only status, class 1..1 | satusehat-specific constraint | Use-case set is larger than the profile page's (adds participant, classHistory, dischargeDisposition). |
| 299 | Step 4/5 Observation wajib: status, code, subject, encounter, **performer** | fhir-observation.md: performer 0..* | satusehat-specific constraint | S8. |
| 300 | Step 13 Condition: one diagnosis per payload; category `encounter-diagnosis`; ICD-10 plus SNOMED ECL | fhir-condition.md: code 0..1 CodeableConcept with 0..* codings | satusehat-specific constraint | Two codings (ICD-10 + SNOMED) in one `code` is valid R4. |
| 301 | Step 15 Procedure wajib: status, code, subject, encounter, performer.actor, focalDevice.manipulated | fhir-procedure.md: status, subject, performer.actor, focalDevice.manipulated 1..1 | satusehat-specific constraint | code/encounter tightened. |
| 302 | Step 27 Encounter PUT must carry `Encounter.id` from step 2 and adds diagnosis (primary/secondary), `period.end`, length, discharge condition, follow-up | fhir-rest-api.md update: body `id` SHALL equal URL `[id]`; `Encounter.diagnosis.rank` for primary/secondary | confirmed | — |
| 303 | Encounter `location.extension.serviceClass` codes `reguler`/`eksekutif`; upgradeClassIndicator `kelas-tetap`/`naik-kelas`/`turun-kelas`/`titip-rawat` | fhir-profiling.md extension rules | satusehat-specific constraint | — |
| 304 | Follow-up `ServiceRequest.locationCode` `v3-RoleCode` \| `OF`/`HOSP`/`PC`/`AMB` | not captured (ServiceRequest) | unverifiable | S23 for the double mapping. |
| 305 | Composition type LOINC `88645-7`, section codes (LOINC + kemkes `TK0000xx`) | not captured (Composition) | unverifiable | Out of scope for sub-project 2. |
| 306 | Lab/radiology/pharmacy flows (steps 10, 11, 16–19) | not captured (ServiceRequest, Specimen, DiagnosticReport, ImagingStudy, Medication*) | unverifiable | Out of scope. |
| 307 | SATUSEHAT uses HL7 FHIR over HTTPS REST; R4 evidenced only by URLs (satusehat-overview.md) | fhir-rest-api.md: `fhirVersion=4.0` MIME parameter; R4 = 4.0.1 | satusehat-specific constraint | S21. |
| 308 | 46 supported resources incl. `BillingStatus`, `ChargeItemResponse` | fhir-workflow.md request/event resource lists: no R4 page in the corpus defines them and neither name matches any R4 resource type | conflict | Resource names that do not exist in R4 (S20). |
| 309 | `Resource` = resourceType, id, meta, implicitRules, language; `DomainResource` adds text, contained, extension, modifierExtension | fhir-observation.md root: DomainResource inherits id, meta, implicitRules, language, text, contained, extension, modifierExtension | confirmed | — |
| 310 | Glossary: IHS issues `{patient-ihs-number}` / `{practitioner-ihs-number}`; MPI/MNI/MSI master indexes | no R4 counterpart | unverifiable | National infrastructure. |

## Sources
- raw/satusehat/res-practitioner.md
- raw/satusehat/api-practitioner.md
- raw/satusehat/api-practitioner-role.md
- raw/satusehat/res-organization.md
- raw/satusehat/res-location.md
- raw/satusehat/api-organization.md
- raw/satusehat/api-location.md
- raw/satusehat/res-condition.md
- raw/satusehat/api-condition.md
- raw/satusehat/res-procedure.md
- raw/satusehat/api-procedure.md
- raw/satusehat/res-related-person.md
- raw/satusehat/api-patient.md
- raw/satusehat/mpi-pasien-bayi.md
- raw/satusehat/datatype-primitive.md
- raw/satusehat/datatype-general.md
- raw/satusehat/datatype-metadata.md
- raw/satusehat/datatype-special.md
- raw/satusehat/api-onboardings.md
- raw/satusehat/api-integrations.md
- raw/satusehat/api-validasi.md
- raw/satusehat/api-kamus-validasi.md
- raw/satusehat/api-list-response.md
- raw/satusehat/mpi-rest-api.md
- raw/satusehat/msi-rest-api.md
- raw/satusehat/term-index.md
- raw/satusehat/term-standar.md
- raw/satusehat/term-loinc.md
- raw/satusehat/term-loinc-laboratory.md
- raw/satusehat/term-snomed-ct.md
- raw/satusehat/term-icd-10.md
- raw/satusehat/term-icd-9-cm.md
- raw/satusehat/term-lampiran-rawat-jalan.md
- raw/satusehat/interop-index.md
- raw/satusehat/interop-rme-rawat-jalan.md
- raw/satusehat/playbook-preface.md
- raw/satusehat/fhir-framework.md
- raw/satusehat/fhir-resources-index.md
- raw/satusehat/fhir-prerequisites.md
- raw/fhir-r4/practitioner.md
- raw/fhir-r4/practitionerrole.md
- raw/fhir-r4/organization.md
- raw/fhir-r4/location.md
- raw/fhir-r4/condition.md
- raw/fhir-r4/procedure.md
- raw/fhir-r4/relatedperson.md
- raw/fhir-r4/patient.md
- raw/fhir-r4/datatypes.md
- raw/fhir-r4/references.md
- raw/fhir-r4/narrative.md
- raw/fhir-r4/validation.md
- raw/fhir-r4/http.md
- raw/fhir-r4/search.md
- raw/fhir-r4/bundle.md
- raw/fhir-r4/security.md
- raw/fhir-r4/profiling.md
- raw/fhir-r4/extensibility.md
- raw/fhir-r4/observation.md
- raw/fhir-r4/workflow.md

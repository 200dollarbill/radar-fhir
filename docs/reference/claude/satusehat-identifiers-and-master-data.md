# SATUSEHAT — Identifiers and Master Data (MPI, MSI, Master Wilayah)

Ringkasan (summary): SATUSEHAT keeps national master indexes — Master Patient Index (MPI) for patients, Master Sarana Index (MSI) for facilities (fasyankes), Master Wilayah for administrative regions, and KFA for drugs/devices. Every record in the IHS (Indonesia Health Service) gets an **IHS Number**; for patients it is `{patient-ihs-number}` and is the value used in `Patient/{patient-ihs-number}` references. This file consolidates the identifier system URIs, the MPI minimum-data rules for the three patient kinds, the MSI facility lookup API, and the wilayah (region) code formats as the raw pages state them.

## Master data products (master-index)
| Product | What the page says | Source of truth named |
|---|---|---|
| Master Patient Index (MPI) | Standard patient data, validated by Dukcapil (civil registry) for demographics | Dukcapil |
| Master Sarana Index (MSI) | Standard facility data, "35 jenis Fasilitas Pelayanan Kesehatan" (35 facility types); compiled from SISDMK, SIRS, SIMADA, etc. | SISDMK, SIRS, SIMADA |
| Master Wilayah | Provinsi, Kota/Kabupaten, Kecamatan, Kelurahan/Desa codes | Kemendagri RI (Ministry of Home Affairs) |
| Kamus Farmasi dan Alat Kesehatan (KFA) | Drug and medical-device dictionary | BPOM, LKPP |

`msi-preliminary` and `wilayah-preliminary` are pure prefaces (background + purpose + table of contents); they contain no rules, codes or endpoints. The Master Wilayah REST API page itself (`rest-api-wilayah`) is **not** in the raw corpus.

## Identifier system URIs
All URIs below appear verbatim in the raw text; "seen in" lists the raw files.

| Purpose | system URI | Seen in |
|---|---|---|
| NIK (Nomor Induk Kependudukan, national ID number) of the patient | `https://fhir.kemkes.go.id/id/nik` | mpi-rest-api, res-patient, api-patient, api-practitioner, res-related-person |
| NIK Ibu (mother's NIK) — newborn without own NIK | `https://fhir.kemkes.go.id/id/nik-ibu` | mpi-rest-api, api-patient |
| IHS Number of the patient (returned by the server; also the resource `id`) | `https://fhir.kemkes.go.id/id/ihs-number` | mpi-rest-api, api-patient |
| Search-parameter form for the patient IHS number (stated once, on the Patient profile page) | `https://fhir.kemkes.go.id/id/patient-ihs-number` | res-patient |
| Paspor (passport) | `https://fhir.kemkes.go.id/id/paspor` | res-patient, api-patient |
| KK (Kartu Keluarga, family card number) | `https://fhir.kemkes.go.id/id/kk` | res-patient, api-patient |
| Patient profile (`meta.profile`) | `https://fhir.kemkes.go.id/r4/StructureDefinition/Patient` | mpi-rest-api |
| Faskes-local identifiers of other resources | `http://sys-ids.kemkes.go.id/<resource>/{organization-ihs-number}` (e.g. `encounter`, `condition`, `procedure`, `location`, `organization`; the exact suffix varies per page — see each resource file) | res-*/api-* pages, not the MPI/MSI pages |

Contradiction to record, not resolve: `res-patient.md` gives `https://fhir.kemkes.go.id/id/patient-ihs-number` as the search identifier system, while `mpi-rest-api.md` (search response example) shows the stored identifier as `https://fhir.kemkes.go.id/id/ihs-number`. Both are quoted verbatim.

Search-parameter formats stated in `mpi-rest-api`:
- by NIK: `identifier=https://fhir.kemkes.go.id/id/nik|<nilai-nik>`
- newborn by mother's NIK: `identifier=https://fhir.kemkes.go.id/id/nik-ibu|<nik-ibu>`

## IHS Number
| Fact | Raw statement (paraphrased; source `mpi-preliminary` unless noted) |
|---|---|
| What | "nomor urut yang akan dihasilkan oleh IHS (Indonesia Health Service) untuk setiap record" — patients, tenaga kesehatan (health workers), fasilitas kesehatan, alat kesehatan, etc. |
| Why | Dukcapil API is now limited to NIK validity checks, no autofill; and people without NIK (newborns, WNI abroad, WNA/foreigners, unregistered) need a unique identifier |
| Use in FHIR | Every resource that references the patient needs `{patient-ihs-number}`; it is obtained from MPI and may be stored by the fasyankes/partner internally |
| Format seen in examples | `P02478375538` (letter `P` + 11 digits) for patients (`mpi-rest-api` search example and dummy table); other pages use `N10000001` for practitioners and 10-digit `kode_satusehat` (e.g. `1000201991`) for facilities — no format rule is stated anywhere |
| Distinguishing records | MPI text says a change of identifier logic is being formulated so patients, nakes, faskes can be told apart in one system (no rule given) |
| MPI cases | Pasien dengan NIK; Pasien bayi baru lahir (newborn); Pasien tanpa NIK (e.g. WNA); Pasien tanpa identitas atau dalam gangguan jiwa (no identity / mental disorder — no dedicated page in corpus) |

## MPI minimum data per patient kind
`*` = WAJIB (mandatory). "Setiap data harus unik / TIDAK BOLEH terdapat duplikasi" (no duplicates) is stated for all three kinds.

| Data point | Pasien dengan NIK (`mpi-pasien-nik`) | Bayi baru lahir (`mpi-pasien-bayi`) | Tanpa NIK (`mpi-pasien-no-nik`, search only) |
|---|---|---|---|
| identifier | `*` — only NIK (`nik`) allowed | `*` — NIK (`nik`) or NIK Ibu (`nik-ibu`) | — |
| name | `*` full name per KTP | `*` family-given name or generic `Bayi Ny. [Nama ibu]` | `*` partial or full name, e.g. `Budi` |
| birthDate | `*` `YYYY-MM-DD` | `*` `YYYY-MM-DD` | `*` `YYYY`, `YYYY-MM` or `YYYY-MM-DD` |
| birthPlace | optional, per NIK/KTP standard | optional | — |
| gender | `*` `male` / `female` | `*` `male` / `female` | `*` `male` / `female` |
| Nomor Kartu Keluarga | optional, issued by Dukcapil | optional | — |
| multipleBirthInteger | — | `*` birth order `1`, `2`, …; `0` if not a multiple birth | (returned in response: `0` if not twin) |
| address | `*` components `use`=`home`, `line`, `city`, `postalCode`, `country`=`ID`, `extension` | `*` same; may use the parents' address | — |
| address-extension | `*` `province`, `city`, `district`, `village`, `rt`, `rw` — codes per Kemendagri | `*` same | — |
| telecom | optional | optional | — |
| maritalStatus | optional: `S` Never Married, `M` Married, `W` Widowed, `D` Divorced | must be `S` (Never Married) | (response: `Married` / `unmarried`) |
| citizenshipStatus | optional `WNI` / `WNA`; WNA only if they hold NIK + e-KTP | optional `WNI` / `WNA` | — |
| communication-language | optional, BCP 47: `en`, `id-ID`, `zh-CN` | — | — |

Processes available: NIK and newborn: Create, Get, Update/Patch. Tanpa NIK: Get only.

Newborn related person (Ibu/Ayah) minimum data (all `*`): ID Related Person (UUID generated by FHIR), Related person's Identifier (Nomor IHS), Patient's Identifier (Nomor IHS), Relationship type, Name, Gender, Birth Date, Address, Phone Number. The create flow uses `Relation Type: MTH` and links the `RelatedPerson` back to the mother's record with a PUT.

### Create flow (NIK and newborn)
| Step | Rule |
|---|---|
| 1. GET by Nomor IHS or search by NIK | If found, use the IHS number; if not, POST |
| 2. POST Patient (NIK) | Sent to Dukcapil for verification: NIK, Nama Lengkap, Tanggal Lahir, Jenis Kelamin, Kode Provinsi, Kode Kab/Kota, Kode Kecamatan, Kode Desa/Kelurahan. All match → new Nomor IHS returned; any mismatch → error naming the unverified element; fix and resend. Defaults listed: status kematian False, kewarganegaraan WNI, bahasa Indonesian |
| 2.a POST newborn (NIK Ibu) | Duplicate check on Nama, Tanggal Lahir, Jenis Kelamin, Urutan Kelahiran; no duplicate → new IHS number, duplicate → existing IHS number returned. Then 2.b POST `RelatedPerson` |
| NIK Ibu verification | Checked against MPI first; if not found, NIK Ibu + Nama Ibu are sent to Dukcapil; mismatch → NIK Ibu cannot be used |
| Other identifiers | No verification; "proses penggabungan" (merge) links matching profiles |

### Get options
| Option | Parameters |
|---|---|
| By ID | Nomor IHS Pasien |
| Search NIK | NIK |
| Search Name + Birthdate + NIK | NIK, Nama, Tanggal Lahir |
| Search Name + Birthdate + Gender | Nama (≥ 3 characters, similar-case match), Tanggal Lahir (`YYYY-MM-DD`, exact), Jenis Kelamin (exact) — the only option for pasien tanpa NIK |
| Newborn by NIK Ibu | `identifier` system nik-ibu → returns Nomor IHS, Nama, Urutan Kelahiran for every child of that mother |
| Newborn via mother's RelatedPerson list | mother's Nomor IHS, or NIK Ibu + Nama + Tanggal Lahir → patients with relation type "MTH" |

Tanpa-NIK search response fields: `identifier` (IHS Number only), `name`, `gender`, `birthdate`, `multipleBirthInteger`, `address` (masked), `maritalStatus`.

### Update/Patch rules
- Allowed when Dukcapil has newer data than MPI (NIK) or when the newborn has no NIK yet and is not Dukcapil-validated.
- Updatable: Nama lengkap, Tanggal lahir, Tempat lahir, Jenis kelamin, Alamat, Status pernikahan, Kewarganegaraan (newborn additionally: NIK).
- PATCH must carry the Nomor IHS plus existing Nama, Tanggal lahir, Jenis kelamin for validation; if NIK is present, NIK + nama + tanggal lahir are re-validated at Dukcapil.

## MPI REST API (`mpi-rest-api`)
Auth: OAuth 2 `client_credentials`; `POST {oauth-base}/accesstoken` with `Content-Type: application/x-www-form-urlencoded`, query `grant_type=client_credentials`, body `client_id`, `client_secret`. Response `token_type` is `BearerToken`, `expires_in` `3599`. One Client ID may be used by only one Organization ID; a mismatch yields `"text": "resource cannot be accessed due to business rule"`.

| Environment | Auth base | FHIR base |
|---|---|---|
| Sandbox | `https://api-satusehat-stg.dto.kemkes.go.id/oauth2/v1` | `https://api-satusehat-stg.dto.kemkes.go.id/fhir-r4/v1` |
| Production | `https://api-satusehat.kemkes.go.id/oauth2/v1` | `https://api-satusehat.kemkes.go.id/fhir-r4/v1` |

| Method | Path (as printed) | Parameters / body | Response |
|---|---|---|---|
| GET | `/Patient` | `?identifier=https://fhir.kemkes.go.id/id/nik\|<nik>`; or `?name&birthdate&nik`; or `?identifier=https://fhir.kemkes.go.id/id/nik-ibu\|<nik-ibu>`; or `?name&birthdate&gender` | `Bundle` type `searchset` with `total`, `entry[].resource` (Patient with `ihs-number` + `nik` identifiers, `link[].other` → `RelatedPerson/...`, `meta.profile`) |
| GET | `/Patient:id` (raw prints it without slash; `:id` typed `uuid`) | header `Authorization`, `Content-Type: application/json` | `Patient` |
| POST | `/Patient:` (raw prints a trailing colon) | Patient JSON with identifier `nik` or `nik-ibu` | `Patient` with `id`; "PERLU disimpan nilai UUID … dari properti id" |
| PATCH | `/Patient/:id` | JSON Patch array; only `op: "replace"`; path like `/language` | echo of the payload |

`4xx` bodies are `OperationOutcome` (`application/json`); `5xx` is `text/plain` (`Gateway Timeout`). Note the POST response example shows `"id": "100000000001"` (numeric) although the text calls it a UUID — recorded verbatim.

Sandbox dummy patients (only usable in Sandbox): 10 rows, e.g. NIK `9271060312000001` Ardianto Putra male 1992-01-09 IHS `P02478375538`; NIK `9204014804000002` Claudia Sintia female 1989-11-03 IHS `P03647103112`.

## MSI REST API (`msi-rest-api`)
Same OAuth flow and auth bases as MPI. MSI base: Sandbox `https://api-satusehat-stg.dto.kemkes.go.id/masterdata`, Production `https://api-satusehat.kemkes.go.id/masterdata`. Sections 4.1–4.5 (Multi Sarana, Rumah Sakit, Klinik, PUSKESMAS, Praktik Mandiri) all describe the **same** endpoint with the same parameters and identical response structure; they differ only in the `jenis_sarana` value passed.

| Method | Path | Query (`*` wajib) |
|---|---|---|
| GET | `/v1/mastersaranaindex/mastersarana` | `*limit` (error if > 2000), `*page`, `*jenis_sarana` (repeat the key for multiple values), `kode_satusehat` (10 digits), `kode_sarana`, `nama`, `kode_provinsi` (2 digits), `kode_kabkota` (4 digits), `kode_kecamatan` (6 digits), `status_aktif` (`true`/`false`), `status_sarana` (`draft`, `verified`, `valid`, `reverified`), `sumber_identifier` + `identifier_kode_sarana` (must be used together), `lower_bound_updated_at`, `upper_bound_updated_at` (`YYYY-MM-DD`) |

| `jenis_sarana` code | Facility type |
|---|---|
| `104` | Rumah sakit (hospital) |
| `103` | Klinik |
| `102` | PUSKESMAS |
| `101` | Praktek mandiri (independent practice) |

`sumber_identifier` values: `satset`, `dto_msfi`, `yankes_praktik_mandiri`, `yankes_klinik`, `yankes_rs`, `puskesmas_pusdatin_baru`, `puskesmas_pusdatin_lama`, `sisdmk_sarana`, `yankes_praktik_mandiri_kmk`, `yankes_klinik_kmk`, `yankes_utd`, `yankes_utd_kmk`, `yankes_labkes`, `yankes_labkes_kmk`.

Response shape (all fields `*`): `{ status_code, message, page, total_page, data: [ { kode_satusehat (10-digit SATUSEHAT code), kode_sarana, nama, telp, email, website, longitude, latitude, operasional (bool), wilayah_perairan_darat, wilayah_karakteristik, sarana_administrasi { kode, nama, kode_sarana, status_aktif, status_sarana }, alamat, provinsi { kode, nama, kode_bps, kode_lama }, kabkota { kode, nama, kode_bps, kode_lama }, jenis_sarana { kode, nama, nama_alt }, subjenis { kode, nama, nama_alt }, kelas_sarana { kode, nama }, status_sarana, status_aktif } ] }`. Example item: `kode_satusehat` `1000156689`, `jenis_sarana.kode` `104` "Rumah Sakit", `subjenis.kode` `10401` "Rumah Sakit Umum", `kelas_sarana.kode` `other`. Error example: `{ "status_code": 400, "message": "limit cannot be more than 2000", "data": null }`.

Internal inconsistencies recorded verbatim: `status_sarana` query doc lists `draft, verified, valid, reverified` but the response doc lists `draft, review, verified, valid`; `provinsi.kode`/`kabkota.kode` are typed `number` in the structure block but described as `string` in the notes and returned as strings (`"96"`, `"9605"`); the auth text says `client_server` where it means `client_secret`.

## Wilayah (region) codes
No dedicated Master Wilayah API page exists in the corpus; the code format is inferred only from what the MPI and MSI pages state:

| Level | Format stated | Where |
|---|---|---|
| Provinsi | Kemendagri code, 2 digits (e.g. `35`, `96`) | msi-rest-api `kode_provinsi` |
| Kabupaten/Kota | 4 digits (e.g. `3603`, `9605`) | msi-rest-api `kode_kabkota` |
| Kecamatan | 6 digits (e.g. `350105`) | msi-rest-api `kode_kecamatan` |
| Desa/Kelurahan, RT, RW | required in Patient `address-extension` (`village`, `rt`, `rw`); no digit count stated | mpi-pasien-nik, mpi-pasien-bayi |
| Reference list | "Kode Wilayah KEMENDAGRI" Google-Sheets link; `kode_bps` and `kode_lama` (pre-pemekaran) also returned by MSI | mpi-pasien-nik, msi-rest-api |

## Notes for our server
- Model patient identifiers as a list with these systems: `nik`, `nik-ibu`, `ihs-number`, `paspor`, `kk`; accept `patient-ihs-number` as a search alias since the corpus uses both spellings.
- Newborns: allow `nik-ibu` as sole identifier; require `multipleBirthInteger` (0 for singleton) and force `maritalStatus` `S`; duplicate check on name + birthDate + gender + birth order; auto-create a `RelatedPerson` with relationship `MTH` and a `Patient.link` (`type: refer`) to it.
- Search modes to implement on `/Patient`: identifier token (`system|value`), `name+birthdate+nik`, `name+birthdate+gender` (name ≥ 3 chars, birthdate/gender exact).
- We have no Dukcapil; treat NIK as syntactically validated only, and record that the "verified" state is unreachable locally.
- Facility (Organization) master: store `kode_satusehat` (10 digits) as the organization IHS number and `jenis_sarana` 101–104 as the type code; region codes as 2/4/6-digit Kemendagri strings.
- Reuse the MPI PATCH contract: JSON Patch, `replace` only.

## Sources
- raw/satusehat/master-index.md
- raw/satusehat/mpi-preliminary.md
- raw/satusehat/mpi-pasien-nik.md
- raw/satusehat/mpi-pasien-no-nik.md
- raw/satusehat/mpi-pasien-bayi.md
- raw/satusehat/mpi-rest-api.md
- raw/satusehat/msi-preliminary.md
- raw/satusehat/msi-rest-api.md
- raw/satusehat/wilayah-preliminary.md
- raw/satusehat/res-patient.md
- raw/satusehat/api-patient.md
- raw/satusehat/api-practitioner.md
- raw/satusehat/res-related-person.md

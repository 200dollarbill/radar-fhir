# Catatan Bab III (2026-11-26)

Notes for the student on the Bab III rewrite (spec
`docs/design/specs/2026-11-26-proposal-merge-and-bab3-design.md`). English is allowed here;
the proposal text is Indonesian.

## Tabel klaim

Every number in Bab III, with its source. Citation numbers ([16], [20], [21], [23]) and
section or figure numbers are not listed.

| Klaim di Bab III | Angka | Sumber |
|---|---|---|
| Rantai argumen literatur | L1 sampai L8 (8) | `docs/papers/search/`, `CLAUDE.md` |
| Konsultasi dengan dokter mitra | 15 Oktober 2026, sekitar 100 subjek, lebih dari satu bulan | `docs/notul/konsultasi_15okt.txt` line 14 |
| Radar CW | 24 GHz | `firmware/radar_json/README.md`, proposal etik |
| Papan | ESP32 (AtomS3R) | `firmware/radar_json/README.md` |
| ADC | 12 bit, 3,3 V | `firmware/radar_json/README.md` |
| Laju sampel | 100 per detik; selang 10 ms | `firmware/radar_json/sampling.h`; `website/src/observation.js` (`period = 1000 / fs`) |
| Potongan | paling lama 10 detik (1000 sampel per kanal) | `website/src/chunker.js`, `docs/HOW-IT-WORKS.md` §2 |
| Jumlah kanal per Observation | delapan (I, Q, 3 akselerometer, 3 giroskop) | `website/src/observation.js` (`COMPONENTS`) |
| Token login | berlaku satu jam | `docs/HOW-IT-WORKS.md` §3 (`FHIR_JWT_TTL` 3600 s) |
| Peran | empat | `fhir_server/authz.py`, `docs/HOW-IT-WORKS.md` §3 |
| Metode tampilan | enam metode, hybrid, median 0,92 | `docs/eval/2026-11-18-radar-display-processing.md` |
| Uji otomatis 26 November 2026 | 236 server, 179 web, 23 hosting (semua lolos) | fresh `make test` on 2026-11-26 (also 34 scraper tests, linter 0 problems) |
| Papan diam | sekitar 1,53 V, sebaran sekitar 1 mV | `CLAUDE.md` Status, 2026-11-18 handover §5 |
| Saat ada gerakan | sebaran 90 sampai 170 mV | `CLAUDE.md` Status, recordings 2026-11-18 |
| Uji gangguan | terunggah 16 sampai 17 detik setelah server kembali, tanpa duplikasi | end of `docs/design/specs/2026-11-19-tidy-up-and-cloudflare-hosting-design.md` |
| Worker | tidak lebih dari 3 ms per permintaan | same hosting spec, live checks |
| Kriteria kelengkapan sampel | 100%, duplikat nol | design target from 1.4 (*seluruh sampel yang dikirim tersimpan utuh tanpa duplikasi*) |
| Kepmenkes | HK.01.07/Menkes/1423/2022 | reference [21] |
| Listing 3.1 | `2026-11-18T07:30:10+00:00`, `1.531 1.532 1.530`, period 10 | illustrative values in the shape of `website/src/observation.js`; the date and voltages are examples near the idle reading, not a stored recording |

## Placeholder

| Placeholder | Where | What fills it |
|---|---|---|
| `[insert data: jumlah subjek dan kriteria dari protokol etik]` | 3.2 | the group's approved ethics protocol |
| `[insert data: sumber RME sintetis]` | 3.2 | choice of synthetic RME source (open question O4) |
| `[insert data: jenis rekaman EKG cabang A]` | 3.5 | confirm with branch A whether its ECG is 12 lead |
| `[insert data: target kelengkapan pemetaan]` | 3.9 Tabel 3.2 | target to agree with the supervisor (also in 1.4) |
| `[insert data: toleransi penyelarasan waktu]` | 3.9 Tabel 3.2 | tolerance to agree before testing (also in 1.4) |
| `[cite: HL7 FHIR Validator]` | 3.9 | suggested entry: HL7 International, "FHIR Validator." [Online]. Available: https://confluence.hl7.org/display/FHIR/Using+the+FHIR+Validator |
| `[insert data: prosedur persetujuan subjek dan penilaian risiko dari proposal etik]` | 3.10 | ethics proposal, once its methods section is written |
| `[cite: Undang Undang Nomor 27 Tahun 2022 tentang Pelindungan Data Pribadi]` | 3.10 | suggested entry: Republik Indonesia, "Undang Undang Nomor 27 Tahun 2022 tentang Pelindungan Data Pribadi," 2022. |
| `[insert data: jadwal]` (6) | 3.12 Tabel 3.4 | dates for each step (open question O5) |

## Komentar Word pemilik

The 15 comments in `proposal_revised/proposal_prata_revised.docx` (not carried into the v2
file). "Selesai" means the current `proposal.md` already resolves it.

| # | Komentar | Pada teks | Status |
|---|---|---|---|
| 0 | tambahin author | 1.1 "dengan **studi** kohort ... 10,9% ... 27%" [3] | Masih terbuka: now "Pada satu kohort", author not named |
| 1 | DOI: 10.4103/JCPC.JCPC_4_20 | 1.1 two object method "[8][new]" | Masih terbuka: see *Usulan referensi* R1 |
| 2 | https://doi.org/10.1016/j.cjco.2025.12.001 | 1.1 "sensitivitas rendah (43.3%), dan spesifitas rendah (67.7%) [new]" | Masih terbuka: now `[cite: sumber angka two object method]`; see R2 |
| 3 | tambahi author | 1.1 "beberapa **studi** menggunakan RADAR CW ataupun FMCW" | Masih terbuka |
| 4 | tambahin data ntar | 1.1 "akurasi tinggi **saat** divalidasikan" | Masih terbuka: no number given yet |
| 5 | diganti ntar | 1.1 "[9]. **[10].**" | Selesai: now "[9], [10]" |
| 6 | author | 1.1 "Terdapat beberapa **studi** ... JVP di permukaan leher" | Masih terbuka: now "Beberapa studi juga memakai RADAR ... [6], [10]" |
| 7 | author | 1.1 "Suatu **studi** meta analisis" [12] | Masih terbuka: now "Satu analisis dengan pencocokan skor kecenderungan" |
| 8 | author | 1.1 "**Studi** lain melaporkan bahwa JVP tinggi" [13] | Masih terbuka |
| 9 | author | 1.1 "**Fudim, et. al (2025)**" [14] | Selesai: now named by trial, "Pada uji SCALE HF 1" |
| 10 | author | 1.1 "**Pada uji acak lain**" [15] | Masih terbuka |
| 11 | author, 18 | 1.1 "Survey oleh **cite**" | Selesai: "Survei Aisyah dkk. ... [18]" |
| 12 | author, 19 | 1.1 "PGHD terbuktikan oleh **cite**" | Masih terbuka: now "telaah sistematis ... [19]" |
| 13 | author | 1.1 "Studi **oleh** di RSUD" [24] | Masih terbuka: now "Studi campuran di 12 RSUD tipe C dan D" |
| 14 | author 18 | 2.3 "Survei lintas Puskesmas **oleh**" | Selesai: "oleh Aisyah dkk. [18]" |

## Usulan referensi

Not yet in the reference list. They enter as [42] and [43] only after the student confirms
them; the full IEEE entries need author, title and journal from the papers (no metadata was
looked up, to avoid an outside call without permission).

| # | DOI | Proposed use |
|---|---|---|
| R1 | 10.4103/JCPC.JCPC_4_20 | 1.1, description of the two object method, next to [8] |
| R2 | 10.1016/j.cjco.2025.12.001 | 1.1, reliability 82,9%, sensitivity 43,3%, specificity 67,7%, replacing `[cite: sumber angka two object method]` |

## Perubahan struktur Bab III

| Lama (2026-11-24) | Baru (2026-11-26) |
|---|---|
| BAB III METODOLOGI | BAB III METODOLOGI DAN PERANCANGAN SISTEM, with an opening paragraph |
| 3.1 Alur Penelitian | 3.1 Pendekatan dan Alur Penelitian (approach paragraph added) |
| 3.2, 3.3 | unchanged |
| 3.4 Arsitektur Sistem | 3.4.1 Gambaran Umum, 3.4.2 Use Case Diagram (Gambar 3.3), 3.4.3 Kebutuhan Sistem, 3.4.4 Alur Kerja Sistem (Gambar 3.4, 3.5) |
| 3.5 Protokol Akuisisi dan Penerimaan Data | 3.5 Perancangan Akuisisi dan Penerimaan Data (Gambar 3.6) |
| 3.6 Pemodelan Data FHIR | 3.6 Perancangan Pemodelan Data FHIR (Tabel 3.1, Listing 3.1) |
| 3.8 Rancangan Tampilan Terpadu | 3.7 Perancangan Antarmuka (pages per role plus the planned view) |
| 3.7 Sesi, Peran, dan Keamanan | 3.8 Perancangan Keamanan (in layers) |
| 3.9 Metode Pengujian dan Analisis | 3.9 Perancangan Pengujian (Gambar 3.7, Tabel 3.2, Persamaan 3.1 sampai 3.4) |
| 3.10, 3.11, 3.12 | 3.10 unchanged; 3.11 date and Tabel 3.3; 3.12 Tabel 3.4 |

The senior thesis (`docs/reference/seniors/`) was used only as a pattern for how the
chapter is laid out; it is not cited.

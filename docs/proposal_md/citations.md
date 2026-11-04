# Panduan Sitasi Silang dan Matriks Rekonsiliasi Literatur (*Cross-Citations Guide*)

Dokumen ini merupakan panduan rujukan silang induk (*master cross-citation guide*) yang menghubungkan seluruh berkas literatur pada repositori tugas akhir. Dokumen ini memetakan hubungan timbal balik antara:
1. **Draf Naskah Proposal**: [proposal.md](file:///mnt/Data/yep/Kuliah/Tugas/Semester%207%20ntr%20lagi%20lulus/PRATA/docs/proposal_md/proposal.md) (Sitasi bernomor IEEE [1] sampai [41]).
2. **Katalog Sumber dan Klaim**: [daftar_sumber_dan_klaim.md](file:///mnt/Data/yep/Kuliah/Tugas/Semester%207%20ntr%20lagi%20lulus/PRATA/docs/proposal_md/daftar_sumber_dan_klaim.md).
3. **Kompilasi Pengayaan Latar Belakang & Sidang**: [klaim_penting_latar_belakang.md](file:///mnt/Data/yep/Kuliah/Tugas/Semester%207%20ntr%20lagi%20lulus/PRATA/docs/proposal_md/klaim_penting_latar_belakang.md).
4. **Koleksi 41 Berkas Literatur Asli**: Seluruh berkas markdown di dalam folder `papers/` (P1 sampai P38 dan dokumen regulasi nasional).

---

## DAFTAR ISI

1. [Matriks Sitasi Silang Induk (Master Cross-Citation Matrix [1]–[41])](#1-matriks-sitasi-silang-induk-master-cross-citation-matrix-141)
2. [Rekonsiliasi Ketidaksesuaian Sitasi (Discrepancy Audit & Resolution)](#2-rekonsiliasi-ketidaksesuaian-sitasi-discrepancy-audit--resolution)
   * 2.1 Duplikasi Entri Lama [16] dan [29] → **TERSELESAIKAN**
   * 2.2 Rujukan Tergantung Lama [34] (Morgan et al. 2022) → **TERSELESAIKAN**
   * 2.3 Pemetaan Sitasi Sekunder ([1], [5], [8], [12], [13]) ke Makalah Primer `papers/`
   * 2.4 Makalah Primer di `papers/` yang Semula Belum Terdaftar → Status Terkini
   * 2.5 Isu Terbuka pada Proposal Baru (Open Issues)
3. [Jejaring Sitasi Antarmakalah (Internal Paper-to-Paper Citation Network)](#3-jejaring-sitasi-antarmakalah-internal-paper-to-paper-citation-network)
   * 3.1 Klaster Kardiovaskular, Gagal Jantung, & Hemodinamik
   * 3.2 Klaster Penderiaan RADAR Nirkontak
   * 3.3 Klaster Informatika Medis, Standar FHIR, & CDSS
   * 3.4 Klaster Regulasi & Ekosistem Kesehatan Indonesia
4. [Indeks Lengkap 41 Berkas Literatur di Folder `papers/`](#4-indeks-lengkap-41-berkas-literatur-di-folder-papers)

---

## 1. MATRIKS SITASI SILANG INDUK (MASTER CROSS-CITATION MATRIX [1]–[41])

Tabel berikut menyajikan pemetaan lengkap setiap nomor sitasi yang ada pada Daftar Pustaka [proposal.md](file:///mnt/Data/yep/Kuliah/Tugas/Semester%207%20ntr%20lagi%20lulus/PRATA/docs/proposal_md/proposal.md) terhadap berkas sumber di `papers/`, letak kemunculannya dalam bab proposal, serta keberadaannya dalam dokumen pendukung:

| No. Sitasi | Penulis Utama & Tahun | Berkas Sumber Terkait di `papers/` | Kemunculan di Bab `proposal.md` | Status di `daftar_sumber_dan_klaim.md` | Status di `klaim_penting_latar_belakang.md` | Catatan Integritas & Status Silang |
|:---:|---|---|---|:---:|:---:|---|
| **[1]** | WHO (2022 data) | *Sitasi Web Eksternal* (Dikutip dalam `P36 GBD`, hal. 194) | Bab 1.1 (P1), Bab 2.1 (P1) | Ada (Entri [1]) | Ada (Tema 1.1) | **Sitasi Sekunder**: Fakta kematian global CVD 17,9 juta jiwa; dirujuk langsung pada pendahuluan P36 GBD. |
| **[2]** | Muharram et al. (2024) | `papers/SupportingData/md/P36 GBD in data for Cardiovascular problems in INdonesia.md` | Bab 1.1 (P1), Bab 2.1 (P1) | Ada (Entri [2]) | Ada (Tema 1.1) | **Makalah Primer**: Kematian kardiovaskular Indonesia melonjak 2× lipat (292 ribu ke 659 ribu jiwa, 1990–2019). |
| **[3]** | Tung et al. (2016) | `papers/SupportingData/md/P23 Readmissions and HF.md` | Bab 1.1 (P1), Bab 2.1 (P1) | Ada (Entri [3]) | Ada (Tema 2.1) | **Makalah Primer**: Data readmisi 30 hari (10,9%) dan 6 bulan (27%) pasien gagal jantung pascarawat. |
| **[4]** | Metra et al. (2023) | `papers/PatientHFManagement/md/P26 Pre and Post discharge of HF patietns.md` | Bab 1.1 (P1), Bab 2.1 (P1, P2) | Ada (Entri [4]) | Ada (Tema 2.1) | **Makalah Primer (ESC-HFA)**: Kongesti sisa pascarawat (*residual congestion* 30,9%) dan lonjakan mortalitas 6×. |
| **[5]** | Mullens et al. (2009) | *Sitasi Klinis Landmark* (Dikutip dalam `P25 Biomarkers` dan `P6 Kenny`) | Bab 1.1 (P1), Bab 2.1 (P2) | Ada (Entri [5]) | Ada (Tema 2.5) | **Sitasi Sekunder**: Landasan hubungan tekanan vena sentral dengan perburukan fungsi ginjal (*cardiorenal syndrome*). |
| **[6]** | Das et al. (2024) | `papers/RADAR/md/P4 RADAR JVP.md` | Bab 1.1 (P1, P2), Bab 2.1, Bab 2.2 | Ada (Entri [6]) | Ada (Tema 4.1) | **Makalah Primer**: Penderiaan JVP nirkontak radar FMCW dan titik anatomis leher SI16/SI17. |
| **[7]** | Kenny et al. (2025) | `papers/RADAR/md/P6 JVP Doppler Ultrasound.md` | Bab 1.1 (P1, P3), Bab 2.2, Bab 2.5 | Ada (Entri [7]) | Ada (Tema 2.5) | **Makalah Primer**: Tinjauan fisiologi JVP sebagai jendela hemodinamik jantung kanan dan sindrom kardiorenal. |
| **[8]** | Storrow et al. (2007) | *Sitasi Klinis Sekunder* (Dikutip dalam latar belakang `P4 Das`) | Bab 1.1 (P1), Bab 2.2 (P1) | Ada (Entri [8]) | Ada (Tema 4.1) | **Sitasi Sekunder – ⚠ MASIH TIDAK LENGKAP**: Rendahnya keandalan observasi visual JVP (*bedside*). Penulis dan judul kosong; DOI tersedia: `10.1016/j.amjcard.2007.01.037`. |
| **[9]** | Schellenberger et al. (2020) | `papers/RADAR/md/P16 RADAR Dataset.md` | Bab 1.1 (P2), Bab 2.2, Bab 2.5 | Ada (Entri [9]) | Ada (Tema 4.3) | **Makalah Primer (Nature Sci Data)**: Basis data 24 jam radar 24 GHz menembus pakaian dan tersinkronisasi ECG. |
| **[10]** | Suzuki et al. (2021) | `papers/RADAR/md/P5 mmWave JVP RADAR.md` | Bab 1.1 (P2), Bab 2.2 (P1, P2) | Ada (Entri [10]) | Ada (Tema 4.1) | **Makalah Primer**: Radar gelombang mikro nirkontak untuk deteksi bentuk gelombang denyut vena jugularis. |
| **[11]** | Yen et al. (2022) | `papers/RADAR/md/P13 RADAR Summary.md` | Bab 1.1 (P2), Bab 2.2, Bab 2.5 | Ada (Entri [11]) | Ada (Tema 4.4) | **Makalah Primer**: Evaluasi mutu sinyal radar 24 GHz berbasis SVM pada pasien geriatri (akurasi 93–100%). |
| **[12]** | Drazner et al. (2009) | *Sitasi Klinis Sekunder* (Dikutip pada `P24 ESC Guidelines`) | Bab 1.1 (P3), Bab 2.2 (P1) | Ada (Entri [12]) | Ada (Tema 2.6) | **Sitasi Sekunder – ⚠ MASIH TIDAK LENGKAP**: Signifikansi prognostik peningkatan JVP pada readmisi gagal jantung. Penulis dan judul kosong; DOI tersedia: `10.1016/j.amjcard.2008.11.045`. |
| **[13]** | Kasai et al. (2023) | *Sitasi Klinis Sekunder* (Dikutip dalam literatur `P26 Metra`) | Bab 1.1 (P3), Bab 2.1 (P2) | Ada (Entri [13]) | Ada (Tema 2.1) | **Sitasi Sekunder**: Peningkatan JVP saat pemulangan pasien sebagai prediktor kuat kekambuhan dekompensasi. |
| **[14]** | Fudim et al. (2025) | `papers/CDSSandMonitoring/md/P20 Noninvasive monitoring for HF .md` | Bab 1.1 (P3), Bab 2.1 (P2) | Ada (Entri [14]) | Ada (Tema 2.4) | **Makalah Primer (SCALE-HF 1)**: Indeks multiparameter mendeteksi 70% perburukan vs aturan berat badan (35%). |
| **[15]** | Weiner et al. (2022) | `papers/FHIRSystem/md/P38 Effect of EHR for CDSS in at home care.md` | Bab 1.1 (P3), Bab 2.5 | Ada (Entri [15]) | Ada (Tema 3.5) | **Makalah Primer (RCT JAMA Netw Open)**: CDSS terkontekstualisasi RME meningkatkan adaptasi rencana dokter 2,67× dan luaran klinis 2,13×. **Baru ditambahkan** ke Daftar Pustaka proposal (sebelumnya hanya di `papers/`). |
| **[16]** | Permenkes 24/2022 | `papers/Regulations/md/UU PERMENKES 24 2024 TENTANG RME.md` | Bab 1.1 (P4), Bab 1.3, Bab 2.3 | Ada (Entri [16]) | Ada (Tema 5.7) | **Regulasi Nasional**: Kewajiban RME seluruh faskes Indonesia dan integrasi platform nasional SATUSEHAT. **Diselesaikan**: tidak lagi duplikat dengan Purnama et al. (kini [17]). |
| **[17]** | Purnama et al. (2026) | `papers/FHIRSystem/md/P10 INDO RME Management FHIR.md` | Bab 1.1 (P4, P5), Bab 2.3 | Ada (Entri [17]) | Ada (Tema 5.7) | **Makalah Primer**: Pengendalian akses rekam medis berbasis IOTA terdesentralisasi untuk pembagian antarfaskes. **Diselesaikan**: nomor dipisah dari entri regulasi (kini [16]=Permenkes, [17]=Purnama). |
| **[18]** | Aisyah et al. (2025) | `papers/FHIRSystem/md/P29 Health information system utilization in Indonesia.md` | Bab 1.1 (P4), Bab 2.3 | Ada (Entri [18]) | Ada (Tema 1.2) | **Makalah Primer**: 10.260 Puskesmas di Indonesia mengoperasikan rata-rata 30 sistem informasi kesehatan yang terfragmentasi. **Diselesaikan**: sebelumnya tertukar sebagai duplikat [29] Purnama; kini entri mandiri [18]. |
| **[19]** | Tapuria et al. (2021) | `papers/FHIRSystem/md/P11 Impact of MIM.md` | Bab 1.1 (P4, P5), Bab 1.4, Bab 2.3 | Ada (Entri [19]) | Ada (Tema 5.7) | **Makalah Primer**: Tinjauan dampak akses pasien terhadap RME pada kepatuhan terapi dan kendali mandiri. |
| **[20]** | Chaidir & Hareva (2025) | `papers/FHIRSystem/md/P14 SSP Implementation Guide.md` | Bab 1.1 (P3, P4, P5), Bab 2.3, Bab 2.4 | Ada (Entri [20]) | Ada (Tema 5.2) | **Makalah Primer**: IG pemetaan ECG 12-sadapan ke FHIR R4 SATUSEHAT menggunakan 17 atribut kunci. |
| **[21]** | Kepmenkes 1423/2022 | `papers/Regulations/md/2022kepmenkes1423.md` | Bab 1.1 (P4), Bab 2.3 | Ada (Entri [21]) | Ada (Tema 5.7) | **Regulasi Nasional**: Pedoman variabel klinis dan metadata wajib pada penyelenggaraan RME nasional. |
| **[22]** | UU No. 17 Tahun 2023 | `papers/Regulations/md/UU Nomor 17 Tahun 2023.md` | Bab 1.1 (P4), Bab 2.3 | Ada (Entri [22]) | Ada (Tema 5.7) | **Undang-Undang Nasional**: Pasal 296 (kewajiban RME) dan Pasal 297 ayat 2 (hak pasien mengakses rekam medis). |
| **[23]** | Riech et al. (2021) | `papers/FHIRSystem/md/P18 ISO to FHIR.md` | Bab 1.1 (P4, P5), Bab 2.4 | Ada (Entri [23]) | Ada (Tema 5.3) | **Makalah Primer**: Pemetaan data perangkat medis ISO/IEEE 11073-10207 ke *resource* HL7 FHIR. |
| **[24]** | Savandha et al. (2026) | `papers/FHIRSystem/md/P22 FHIR Implementation barriers Indonesia.md` | Bab 1.1 (P4), Bab 2.3 | Ada (Entri [24]) | Ada (Tema 1.3) | **Makalah Primer**: Hambatan interoperabilitas RME di RSUD daerah Indonesia (*vendor lock-in* dan data silo). |
| **[25]** | Vorisek et al. (2022) | `papers/FHIRSystem/md/P2 FHIR Review.md` | Bab 1.1 (P4, P5), Bab 2.4 (×2) | Ada (Entri [25]) | Ada (Tema 5.1) | **Makalah Primer**: Tinjauan interoperabilitas HL7 FHIR dalam pertukaran data klinis dan penelitian. |
| **[26]** | Adochiei et al. (2024) | `papers/FHIRSystem/md/P9 IoT FHIR Implementation.md` | Bab 1.1 (P5), Bab 2.4 | Ada (Entri [26]) | Ada (Tema 5.4) | **Makalah Primer**: Framework akuisisi sinyal biomedis IoT ke FHIR Observations secara *real-time* latensi <1 detik. ⚠ DOI masih placeholder `[cite: lengkapi DOI]`. **Baru ditambahkan** ke Daftar Pustaka. |
| **[27]** | Abedian et al. (2025) | `papers/FHIRSystem/md/P3 Garmin to FHIR.md` | Bab 2.3 | Ada (Entri [27]) | Ada (Tema 5.5) | **Makalah Primer**: Integrasi data perangkat *wearable* ke RME melalui pipeline terstandarisasi FHIR. **Baru ditambahkan** ke Daftar Pustaka. |
| **[28]** | Wesley et al. (2021) | `papers/FHIRSystem/md/P8 FHIR Integration.md` | Bab 2.4 | Ada (Entri [28]) | Ada (Tema 5.6) | **Makalah Primer**: SMART on FHIR untuk mengalirkan data luaran mandiri pasien (PGHD) ke 3 vendor EHR di 18 klinik rawat jalan. **Baru ditambahkan** ke Daftar Pustaka. |
| **[29]** | Strasberg et al. (2021) | `papers/CDSSandMonitoring/md/P30 CDSS with FHIR.md` | Bab 1.1 (P5), Bab 2.4, Bab 2.5 | Ada (Entri [29]) | Ada (Tema 5.1) | **Makalah Primer (JAMIA)**: Standar CDS kontemporer berbasis FHIR, CQL, dan CDS Hooks memecah masalah *curly braces*. |
| **[30]** | Kamil et al. (2020) | `papers/FHIRSystem/md/P28 Indonesia Doctor opinions on electronic systems.md` | Bab 2.5 | Ada (Entri [30]) | Ada (Tema 6.2) | **Makalah Primer**: Dokumentasi terfragmentasi di RS Indonesia menciptakan sekat komunikasi antarprofesi medis. **Baru ditambahkan** ke Daftar Pustaka. |
| **[31]** | Núñez et al. (2022) | `papers/SupportingData/md/P25 Biomarkers and HF.md` | Bab 1.1 (P3), Bab 2.1 (P1, P2) | Ada (Entri [31]) | Ada (Tema 2.2) | **Makalah Primer (ESC-HFA)**: Taksonomi 4 fenotipe kongesti; JVP mewakili kongesti *systemic intravascular*. **Baru ditambahkan** ke Daftar Pustaka. |
| **[32]** | Stevenson et al. (2023) | `papers/PatientHFManagement/md/P37 Remote Monitoring for HF management at home.md` | Bab 1.1 (P3), Bab 2.1 | Ada (Entri [32]) | Ada (Tema 2.3) | **Makalah Primer (JACC Scientific Statement)**: Kegagalan telemonitoring berat badan harian; JVP mendahului sesak napas berminggu-minggu. **Baru ditambahkan** ke Daftar Pustaka. |
| **[33]** | Køber et al. (2026) | `papers/PatientHFManagement/md/P24 Guidance for HF Management.md` | Bab 1.1 (P3), Bab 2.1 (P2) | Ada (Entri [33]) | Ada (Tema 2.6) | **Makalah Primer (ESC Guidelines 2026)**: Peningkatan JVP sebagai tanda fisik paling spesifik kongesti jantung kanan. **Baru ditambahkan** ke Daftar Pustaka (sebelumnya bernomor [28]). |
| **[34]** | Shi et al. (2018) | `papers/RADAR/md/P7 mmWave Carotid Pulse.md` | Bab 2.2 | Ada (Entri [34]) | Ada (Tema 4.2) | **Makalah Primer**: Bukti matematis korelasi linear gelombang perpindahan dinding pembuluh RADAR vs kecepatan aliran Doppler USG. **Baru ditambahkan** ke Daftar Pustaka. |
| **[35]** | Garza et al. (2021) | `papers/FHIRSystem/md/P21 eSource for FHIR and RME.md` | Bab 2.3 | Ada (Entri [35]) | Ada (Tema 5.1) | **Makalah Primer**: Evaluasi cakupan standar HL7 FHIR untuk pertukaran data *eSource* penelitian multi-situs. **Baru ditambahkan** ke Daftar Pustaka. |
| **[36]** | Papadopoulos et al. (2022) | `papers/SupportingData/md/P35 Rule based CDSS review.md` | Bab 2.5 (P1, P3) | Ada (Entri [36]) | Ada (Tema 3.3) | **Makalah Primer**: Tinjauan sistematis 1.731 makalah CDSS; hanya 2 yang terintegrasi dengan RME berbasis standar. |
| **[37]** | Hak et al. (2022) | `papers/CDSSandMonitoring/md/P34 Systematic review for CDS.md` | Bab 2.5 (P1) | Ada (Entri [37]) | Ada (Tema 3.3) | **Makalah Primer (PLOS ONE)**: Evaluasi CDSS; 51,9% bersifat sistem terisolasi (*standalone*) dan gagal di integrasi alur kerja. |
| **[38]** | Susanto et al. (2023) | `papers/CDSSandMonitoring/md/P32 ML for CDSS review.md` | Bab 2.5 | Ada (Entri [38]) | Ada (Tema 3.2) | **Makalah Primer (JAMIA)**: CDSS kardiovaskular harus bersifat *assistive* dan tertanam langsung pada alur kerja RME. **Baru ditambahkan** ke Daftar Pustaka. |
| **[39]** | Semenov et al. (2019) | `papers/FHIRSystem/md/P27 FHIR and CDSS making.md` | Bab 1.1 (P5), Bab 2.5 | Ada (Entri [39]) | Ada (Tema 3.1) | **Makalah Primer**: Arsitektur platform manajemen data FHIR terpadu untuk penyediaan layanan inferensi CDSS. |
| **[40]** | Isabelle et al. (2025) | `papers/FHIRSystem/md/P33 EHR, Interoperability and factors for CDSS.md` | Bab 2.5 (P3) | Ada (Entri [40]) | Ada (Tema 3.4) | **Makalah Primer (JAMIA Open)**: Evaluasi alat CDS berbasis CQL, CDS Hooks, dan FHIR mencapai akurasi 96–100% dan 0% alarm palsu. |
| **[41]** | Morgan et al. (2022) | `papers/CDSSandMonitoring/md/P31 CDSS with FHIR and SMART.md` | Bab 2.5 (P3) | Ada (Entri [41]) | Ada (Tema 5.6) | **Makalah Primer (JAMIA)**: Uji klinis acak klaster CDS Hooks meningkatkan adopsi aplikasi SMART 130%. **TERSELESAIKAN**: Sebelumnya rujukan tergantung [34] lama; kini [41] tersitasi eksplisit pada Bab 2.5 P3 bersama [40]. |

---

## 2. REKONSILIASI KETIDAKSESUAIAN SITASI (DISCREPANCY AUDIT & RESOLUTION)

Bagian ini menguraikan audit mendalam mengenai akar penyebab ketidaksesuaian sitasi antardokumen serta status rekonsiliasinya pada proposal revisi:

### 2.1 Duplikasi Entri Lama [16] dan [29] → ✅ TERSELESAIKAN

* **Kondisi Faktual (Proposal Lama)**:
  * Di DAFTAR PUSTAKA proposal lama, entri `[16]` dan entri `[29]` memuat teks rujukan yang **sama**: makalah H. Purnama et al. (*Sensors*, Feb. 2026) tentang kontrol akses rekam medis berbasis IOTA — ini adalah duplikasi langsung.
  * Di teks narasi Bab 2.3 Paragraf 3 proposal lama, sitasi `[29]` disematkan pada kalimat yang sesungguhnya merujuk pada temuan Aisyah et al. (P29), yaitu riset empiris DTO Kementerian Kesehatan RI dan UCL yang mengungkap fragmentasi 30 SIK per Puskesmas. Terjadi **kesalahan penjodohan antara nomor sitasi dan konten referensi**.

* **Resolusi pada Proposal Baru**:
  * Nomor [16] lama (Permenkes 24/2022) **dipertahankan** dan sekarang bernomor **[16] baru** (tetap merujuk Permenkes 24/2022).
  * Nomor [16] lama yang juga tertulis sebagai Purnama kini **dipisah** menjadi **[17] baru** = Purnama et al. (2026), berkas `P10 INDO RME Management FHIR.md`.
  * Nomor [29] lama yang seharusnya merujuk Aisyah et al. kini menjadi **[18] baru** = Aisyah et al. (2025), berkas `P29 Health information system utilization in Indonesia.md`.
  * Kedua entri kini **benar-benar terpisah dan berdiri sendiri** — tidak ada lagi tumpang tindih konten referensi.

### 2.2 Rujukan Tergantung Lama [34] (Morgan et al. 2022) → ✅ TERSELESAIKAN

* **Kondisi Faktual (Proposal Lama)**:
  * Entri `[34]` lama (K. L. Morgan et al., *JAMIA*, 2022) telah tertulis rapi di Daftar Pustaka dan diulas mendalam pada [daftar_sumber_dan_klaim.md](file:///mnt/Data/yep/Kuliah/Tugas/Semester%207%20ntr%20lagi%20lulus/PRATA/docs/proposal_md/daftar_sumber_dan_klaim.md) sebagai Bab 2.5 P3.
  * Namun di dalam teks narasi [proposal.md](file:///mnt/Data/yep/Kuliah/Tugas/Semester%207%20ntr%20lagi%20lulus/PRATA/docs/proposal_md/proposal.md) versi lama, nomor `[34]` **tidak tercantum di paragraf mana pun** — menjadikannya rujukan tergantung (*dangling reference*).

* **Resolusi pada Proposal Baru**:
  * Morgan et al. kini bernomor **[41]** dalam penomoran baru (1–41).
  * Sitasi `[41]` sekarang **tersitasi eksplisit** pada teks narasi **Bab 2.5 Paragraf 3**, berdampingan dengan sitasi `[40]` (Isabelle et al.):
    > *"…mesin inferensi aturan klinis … menghasilkan ringkasan status hemodinamik dan peringatan kontekstual **[40], [41]**."*
  * Morgan et al. kini terikat penuh ke dalam narasi dan tidak lagi berupa rujukan tergantung.

### 2.3 Pemetaan Sitasi Sekunder ([1], [5], [8], [12], [13]) ke Makalah Primer `papers/`

Sebanyak 5 rujukan yang tercantum di Daftar Pustaka tidak memiliki berkas `.md` mandiri di `papers/`, melainkan berasal dari literatur sekunder yang dikutip di dalam makalah-makalah primer. Nomor-nomor sitasi ini telah diperbarui sesuai penomoran baru [1]–[41]:

1. **[1] WHO Fact Sheet (data 2022)**:
   * *Status*: Halaman web resmi World Health Organization mengenai angka 17,9 juta kematian CVD global.
   * *Makalah Primer di `papers/`*: Berasal dari kutipan pada halaman 194 berkas `papers/SupportingData/md/P36 GBD in data for Cardiovascular problems in INdonesia.md`.
2. **[5] W. Mullens et al. (2009, JACC)**:
   * *Status*: Makalah kardiologi klasik mengenai pentingnya kongesti vena terhadap sindrom kardiorenal (*worsening renal function*).
   * *Makalah Primer di `papers/`*: Dikutip secara ekstensif pada tinjauan patofisiologi di `papers/SupportingData/md/P25 Biomarkers and HF.md` dan `papers/RADAR/md/P6 JVP Doppler Ultrasound.md`.
3. **[8] Storrow et al. (2007, Am J Cardiol)** — ⚠ **Masih Tidak Lengkap**:
   * *Status*: Studi observasional mengenai kelemahan dokter IGD dalam memperkirakan JVP secara visual di sisi tempat tidur (*bedside*). Penulis lengkap dan judul **masih kosong** di Daftar Pustaka; hanya ada `[cite: lengkapi...]`.
   * *Makalah Primer di `papers/`*: Dirujuk pada latar belakang berkas `papers/RADAR/md/P4 RADAR JVP.md`.
   * *DOI tersedia*: `10.1016/j.amjcard.2007.01.037` — dapat digunakan untuk melengkapi entri.
4. **[12] Drazner et al. (2009, Am J Cardiol)** — ⚠ **Masih Tidak Lengkap**:
   * *Status*: Bukti klinis bahwa peningkatan JVP dan bunyi jantung ketiga berhubungan dengan prognosis buruk rawat inap ulang. Penulis lengkap dan judul **masih kosong** di Daftar Pustaka; hanya ada `[cite: lengkapi...]`.
   * *Makalah Primer di `papers/`*: Dikutip pada bagian rekomendasi tanda fisik di `papers/PatientHFManagement/md/P24 Guidance for HF Management.md`.
   * *DOI tersedia*: `10.1016/j.amjcard.2008.11.045` — dapat digunakan untuk melengkapi entri.
5. **[13] T. Kasai et al. (2023, Int Heart J)**:
   * *Status*: Makalah klinis yang membuktikan peningkatan JVP saat pasien dipulangkan dari RS memprediksi kejadian readmisi gagal jantung.
   * *Makalah Primer di `papers/`*: Dikutip dalam pembahasan kongesti sisa di `papers/PatientHFManagement/md/P26 Pre and Post discharge of HF patietns.md`.

### 2.4 Makalah Primer di `papers/` yang Semula Belum Terdaftar → Status Terkini

Pada proposal lama, 8 makalah primer di `papers/` belum masuk Daftar Pustaka karena batasan 34 nomor. Pada proposal baru [1]–[41], **sebagian besar sudah diinkorporasi**. Berikut status terkini:

| Berkas `papers/` | Penulis | Nomor Sitasi Baru | Status |
|---|---|:---:|---|
| `P37 Remote Monitoring for HF management at home.md` | Stevenson et al. (2023) | **[32]** | ✅ **Sudah masuk** — Bab 1.1 P3 & Bab 2.1 |
| `P38 Effect of EHR for CDSS in at home care.md` | Weiner et al. (2022) | **[15]** | ✅ **Sudah masuk** — Bab 1.1 P3 & Bab 2.5 |
| `P32 ML for CDSS review.md` | Susanto et al. (2023) | **[38]** | ✅ **Sudah masuk** — Bab 2.5 |
| `P28 Indonesia Doctor opinions on electronic systems.md` | Kamil et al. (2020) | **[30]** | ✅ **Sudah masuk** — Bab 2.5 |
| `P7 mmWave Carotid Pulse.md` | Shi et al. (2018) | **[34]** | ✅ **Sudah masuk** — Bab 2.2 |
| `P8 FHIR Integration.md` | Wesley et al. (2021) | **[28]** | ✅ **Sudah masuk** — Bab 2.4 |
| `P9 IoT FHIR Implementation.md` | Adochiei et al. (2024) | **[26]** | ✅ **Sudah masuk** — Bab 1.1 P5 & Bab 2.4 (⚠ DOI masih placeholder) |
| `P19 ISAC and RADAR.md` | Kim et al. (2026) | *Belum ada* | ❌ **Belum masuk** — masih sebagai bahan pengayaan sidang saja |

> [!NOTE]
> Berkas `P19 ISAC and RADAR.md` (Kim et al., Bi-LSTM koreksi frekuensi radar, akurasi >97%) masih belum dimasukkan ke Daftar Pustaka proposal. Klaim utamanya tersedia di `klaim_penting_latar_belakang.md` sebagai amunisi jawaban sidang.

### 2.5 Isu Terbuka pada Proposal Baru (Open Issues)

Meskipun banyak ketidaksesuaian lama telah terselesaikan, terdapat 4 isu aktif yang **masih memerlukan tindak lanjut** sebelum naskah finalisasi:

1. **[8] Storrow et al. (2007)** — `[cite: lengkapi...]`:
   * Penulis penuh dan judul artikel **kosong** di Daftar Pustaka.
   * DOI tersedia: `10.1016/j.amjcard.2007.01.037`. Gunakan DOI ini untuk mengambil data bibliografis lengkap dari CrossRef atau PubMed.

2. **[12] Drazner et al. (2009)** — `[cite: lengkapi...]`:
   * Penulis penuh dan judul artikel **kosong** di Daftar Pustaka.
   * DOI tersedia: `10.1016/j.amjcard.2008.11.045`. Gunakan DOI ini untuk mengambil data bibliografis lengkap dari CrossRef atau PubMed.

3. **[26] Adochiei et al. (2024)** — `[cite: lengkapi DOI]`:
   * Data penulis dan judul **ada** tetapi kolom DOI di Daftar Pustaka masih berupa placeholder `[cite: lengkapi DOI]`.
   * Jurnal: *Sensors* (MDPI), 2024. Lakukan pencarian DOI melalui MDPI atau CrossRef dengan kata kunci penulis + tahun.

4. **[new] ×2 — Paper Metode JVP Dua Objek (Placeholder Terbuka)**:
   * Terdapat dua sitasi bertanda `[new]` pada Bab 1.1 P1 yang merujuk sebuah studi metodologi observasi JVP menggunakan dua objek referensi, melibatkan empat dokter residen dan 40 pasien, dengan hasil reliabilitas 82,9%, sensitivitas 43,3%, dan spesifisitas 67,7%.
   * **Paper ini belum teridentifikasi** — tidak ada berkas di `papers/` maupun data bibliografis di Daftar Pustaka.
   * **Status**: Placeholder terbuka — paper belum teridentifikasi. Perlu penelusuran manual di PubMed/Google Scholar dengan kata kunci: *"JVP assessment reliability sensitivity two-object bedside"* atau *"jugular venous pressure bedside estimation inter-rater reliability"*.

---

## 3. JEJARING SITASI ANTARMAKALAH (INTERNAL PAPER-TO-PAPER CITATION NETWORK)

Makalah-makalah di dalam repositori saling menyitir dan membentuk jejaring pengetahuan kohesif yang memperkuat validitas tugas akhir. Berikut adalah peta sitasi silang internal antarmakalah yang diperbarui:

```
[P24: Pedoman ESC 2026 — Køber [33]] ──────► [P26: Konsensus Pascamulang ESC-HFA 2023 — Metra [4]]
       │                                                │
       ▼                                                ▼
[P25: Fenotipe Kongesti — Núñez [31]] ◄─── [P37: Pernyataan Ilmiah JACC — Stevenson [32]]
       │                                                │
       ▼                                                ▼
[P20: Uji Klinis SCALE-HF 1 — Fudim [14]]     [P23: Readmisi HF — Tung [3]]
       ▲                                                ▲
       │                                                │
[P6: Doppler JVP — Kenny [7]] ──────────────► [P4: Radar JVP — Das [6]]
       │
       ▼
[P7: Karotis mmWave — Shi [34]] ◄── [P5: JVP mmWave — Suzuki [10]]
                                           │
                                           ▼
                                   [P16: Dataset RADAR — Schellenberger [9]]
                                           │
                                           ▼
                                   [P13: Evaluasi Sinyal — Yen [11]]

─────────────────────────────────────────────────────────────────────────────

[P35: Tinjauan CDSS Rule-Based — Papadopoulos [36]] ──────► [P34: Tinjauan Sistematis CDSS — Hak [37]]
       │                                                              │
       ▼                                                              ▼
[P27: Platform FHIR+CDSS — Semenov [39]] ◄─── [P32: ML CDSS Review — Susanto [38]]
       │                                                              │
       ▼                                                              ▼
[P30: Standar CDS FHIR — Strasberg [29]] ──────────────► [P33: CDSS Tanpa Alert Fatigue — Isabelle [40]]
       │                                                              │
       ▼                                                              ▼
[P31: CDS Hooks RCT — Morgan [41]] ◄────────── [P38: CDSS+RME Konteks — Weiner [15]]
       │
       ▼
[P28: Opini Dokter Indonesia — Kamil [30]]

─────────────────────────────────────────────────────────────────────────────

[Permenkes 24/2022 [16]] ──► [Kepmenkes 1423/2022 [21]] ──► [UU No.17/2023 [22]]
       │                                  │
       ▼                                  ▼
[P10: RME IOTA — Purnama [17]]    [P29: Fragmentasi SIK — Aisyah [18]]
       │                                  │
       ▼                                  ▼
[P22: Hambatan FHIR RI — Savandha [24]] ◄── [P28: Opini Dokter RI — Kamil [30]]
```

### 3.1 Klaster Kardiovaskular, Gagal Jantung, & Hemodinamik
* **P24 (ESC Guidelines 2026 — Køber [33])** menyitir **P26 (Metra et al. 2023 [4])** dan **P25 (Núñez et al. 2022 [31])** dalam menetapkan distensi vena jugularis sebagai kriteria spesifik dekompensasi dan kongesti residual.
* **P26 (Metra et al. 2023 [4])** menyitir **P25 (Núñez et al. 2022 [31])** mengenai biomarker kongesti sisa, serta menyitir **P37 (Stevenson et al. 2023 [32])** mengenai pemantauan fase rentan pascarawat di rumah.
* **P37 (Stevenson et al. 2023 [32])** membuktikan secara ilmiah bahwa telemonitoring berat badan harian gagal mendeteksi perburukan dini — JVP meningkat berminggu-minggu sebelum gejala sesak napas muncul. Ini memperkuat justifikasi penderiaan JVP nirkontak pada **P4 (Das [6])** dan **P5 (Suzuki [10])**.
* **P25 (Núñez et al. 2022 [31])** menyitir **P20 (Fudim et al., SCALE-HF 1 [14])** terkait parameter multiparameter noninvasif dalam mendeteksi kelebihan cairan intravaskular; Mullens et al. **[5]** menjadi landasan patofisiologi kardiorenal di kedua makalah.
* **P6 (Kenny et al. 2025 [7])** menghubungkan dinamika gelombang $a, c, v$ dan lembah $x, y$ vena jugularis dengan patofisiologi atrium kanan, yang menjadi dasar fisiologis penderiaan radar pada **P4 (Das et al. 2024 [6])** dan **P5 (Suzuki et al. 2021 [10])**.
* **P36 (Muharram et al. 2024 [2])** melengkapi data klinis global di atas dengan data epidemiologi nasional beban kardiovaskular Indonesia; **P23 (Tung et al. 2016 [3])** menyediakan konteks readmisi klinis.

### 3.2 Klaster Penderiaan RADAR Nirkontak
* **P16 (Schellenberger et al., Nature Sci Data 2020 [9])** menyitir landasan teori gelombang perpindahan vaskular dari **P7 (Shi et al. 2018 [34])** dan metode evaluasi kualitas sinyal nirkontak pada **P13 (Yen et al. 2022 [11])**.
* **P7 (Shi et al. 2018 [34])** memberikan bukti matematis dan fisis korelasi linear antara gelombang perpindahan dinding pembuluh yang ditangkap radar dan kecepatan aliran Doppler USG, menjadi fondasi validitas fisika seluruh klaster ini.
* **P13 (Yen et al. 2022 [11])** dan **P5 (Suzuki et al. 2021 [10])** sama-sama memanfaatkan frekuensi gelombang mikro 24 GHz untuk menangkap pergerakan mikrometer dinding vaskular tanpa distorsi mekanis.
* **P4 (Das et al. 2024 [6])** mengembangkan konsep dari **P5 (Suzuki et al. [10])** menggunakan radar FMCW pada titik anatomis leher (SI16/SI17) untuk merekonstruksi kurva JVP nirkontak, dengan sitasi sekunder Storrow **[8]** sebagai justifikasi keterbatasan metode visual konvensional.

### 3.3 Klaster Informatika Medis, Standar FHIR, & CDSS
* **P33 (Isabelle et al., JAMIA Open 2025 [40])** menyitir arsitektur dasar CDS berbasis standar dari **P30 (Strasberg et al., JAMIA 2021 [29])** dan metodologi CDS Hooks dari **P31 (Morgan et al., JAMIA 2022 [41])**, membuktikan bahwa integrasi berbasis standar meniadakan alarm palsu (0,0%).
* **P35 (Papadopoulos et al. 2022 [36])** dan **P34 (Hak et al. 2022 [37])** secara konsisten mengkritik bahwa sistem CDSS terdahulu gagal karena monolitik (*standalone*), yang dijawab oleh **P27 (Semenov et al. 2019 [39])** dan **P30 (Strasberg et al. [29])** melalui pemanfaatan model data kanonikal FHIR.
* **P32 (Susanto et al. 2023 [38])** dan **P38 (Weiner et al. 2022 [15])** sama-sama menekankan bahwa CDSS harus tertanam dalam alur kerja klinis nyata; Weiner membuktikan secara RCT bahwa integrasi konteks pasien dari RME meningkatkan luaran klinis 2,13×.
* **P14 (Chaidir & Hareva 2025 [20])** mengimplementasikan spesifikasi data deret waktu fisiologis ke dalam FHIR R4 SATUSEHAT, selaras dengan prinsip pemetaan perangkat medis ISO/IEEE 11073 pada **P18 (Riech et al. 2021 [23])**, serta integrasi IoT real-time pada **P9 (Adochiei et al. 2024 [26])** dan **P8 (Wesley et al. 2021 [28])**.

### 3.4 Klaster Regulasi & Ekosistem Kesehatan Indonesia
* **P29 (Aisyah et al., DTO Kemenkes & UCL 2025 [18])** membuktikan fragmentasi 30 aplikasi SIK per Puskesmas, memberikan justifikasi sosioteknis terhadap mandat integrasi SATUSEHAT pada **Permenkes 24/2022 [16]** dan **UU No. 17 Tahun 2023 [22]**.
* **P22 (Savandha et al. 2026 [24])** dan **P28 (Kamil et al. 2020 [30])** menyoroti kendala *vendor lock-in* dan catatan manual di rumah sakit daerah, yang pemecahannya membutuhkan kepatuhan terhadap standarisasi variabel rekam medis pada **Kepmenkes 1423/2022 [21]** dan sistem kontrol akses pasien pada **P10 (Purnama et al. 2026 [17])**.
* **P11 (Tapuria et al. 2021 [19])** memberikan perspektif dampak pasien dari akses RME, melengkapi kerangka regulasi dengan bukti empiris manfaat klinis pemberdayaan pasien.

---

## 4. INDEKS LENGKAP 41 BERKAS LITERATUR DI FOLDER `PAPERS/`

Tabel katalog referensi lengkap seluruh 41 berkas di folder `papers/`. Nomor sitasi IEEE [1]–[41] pada proposal baru ditampilkan di kolom terakhir untuk memudahkan pelacakan silang:

| No. Berkas | Nama Berkas di Repositori | Penulis Utama & Tahun | Topik Utama Makalah | Kategori Domain | Sitasi Baru |
|:---:|---|---|---|---|:---:|
| **P1** | `papers/FHIRSystem/md/P1 FHIR Intro.md` | Bender & Sartipi (2013) | Pengenalan HL7 FHIR sebagai standar generasi baru | Standar Interoperabilitas | — |
| **P2** | `papers/FHIRSystem/md/P2 FHIR Review.md` | Vorisek et al. (2022) | Tinjauan FHIR dalam pertukaran data kesehatan & penelitian | Standar Interoperabilitas | **[25]** |
| **P3** | `papers/FHIRSystem/md/P3 Garmin to FHIR.md` | Abedian et al. (2025) | Integrasi data perangkat *wearable* ke FHIR | IoT & Patient Data | **[27]** |
| **P4** | `papers/RADAR/md/P4 RADAR JVP.md` | Das et al. (2024) | Penderiaan denyut vena jugularis nirkontak via radar FMCW | Penderiaan RADAR | **[6]** |
| **P5** | `papers/RADAR/md/P5 mmWave JVP RADAR.md` | Suzuki et al. (2021) | Pengukuran JVP menggunakan sensor radar gelombang mikro | Penderiaan RADAR | **[10]** |
| **P6** | `papers/RADAR/md/P6 JVP Doppler Ultrasound.md` | Kenny et al. (2025) | Tinjauan fisiologi Doppler JVP hemodinamik jantung kanan | Fisiologi Kardiovaskular | **[7]** |
| **P7** | `papers/RADAR/md/P7 mmWave Carotid Pulse.md` | Shi et al. (2018) | Hubungan linear pengukuran denyut karotis radar vs USG | Biofisika RADAR | **[34]** |
| **P8** | `papers/FHIRSystem/md/P8 FHIR Integration.md` | Wesley et al. (2021) | SMART on FHIR untuk integrasi data luaran mandiri pasien (PGHD) | Interoperabilitas RME | **[28]** |
| **P9** | `papers/FHIRSystem/md/P9 IoT FHIR Implementation.md` | Adochiei et al. (2024) | Framework akuisisi sinyal biomedis IoT ke FHIR secara real-time | IoT Biomedis & FHIR | **[26]** |
| **P10** | `papers/FHIRSystem/md/P10 INDO RME Management FHIR.md` | Purnama et al. (2026) | Kontrol akses desentralisasi IOTA pada pengelolaan RME Indonesia | Keamanan RME Nasional | **[17]** |
| **P11** | `papers/FHIRSystem/md/P11 Impact of MIM.md` | Tapuria et al. (2021) | Dampak akses pasien terhadap rekam medis elektronik | Hak Pasien & PHR | **[19]** |
| **P12** | `papers/FHIRSystem/md/P12 Wearable devices summary.md` | Lu et al. (2020) | Tinjauan sistematik aplikasi perangkat kesehatan pakai (*wearable*) | Perangkat Kesehatan | — |
| **P13** | `papers/RADAR/md/P13 RADAR Summary.md` | Yen et al. (2022) | Radar medis nirkontak & evaluasi kualitas sinyal geriatri | Penderiaan RADAR | **[11]** |
| **P14** | `papers/FHIRSystem/md/P14 SSP Implementation Guide.md` | Chaidir & Hareva (2025) | Implementation Guide ECG 12-sadapan patuh FHIR SATUSEHAT | Standar ECG & SATUSEHAT | **[20]** |
| **P15** | `papers/FHIRSystem/md/P15 IoT.md` | Baker et al. (2017) | Tinjauan Internet of Things dalam pelayanan kesehatan | Arsitektur IoT | — |
| **P16** | `papers/RADAR/md/P16 RADAR Dataset.md` | Schellenberger et al. (2020) | Dataset klinis tanda vital radar 24 GHz tersinkronisasi ECG | Dataset & Validasi | **[9]** |
| **P17** | `papers/FHIRSystem/md/P17 Telemedicine Resources.md` | Kruse et al. (2017) | Telemedisin dan faktor pendukung adopsi layanan jarak jauh | Layanan Kesehatan Digital | — |
| **P18** | `papers/FHIRSystem/md/P18 ISO to FHIR.md` | Riech et al. (2021) | Pemetaan data perangkat medis ISO/IEEE 11073 ke HL7 FHIR | Interoperabilitas Alat Medis | **[23]** |
| **P19** | `papers/RADAR/md/P19 ISAC and RADAR.md` | Kim et al. (2026) | Radar CW dengan koreksi frekuensi Bi-LSTM cerdas | Sinyal RADAR Cerdas | — |
| **P20** | `papers/CDSSandMonitoring/md/P20 Noninvasive monitoring for HF .md` | Fudim et al. (2025) | Uji klinis SCALE-HF 1: pemantauan indeks multiparameter | Manajemen Gagal Jantung | **[14]** |
| **P21** | `papers/FHIRSystem/md/P21 eSource for FHIR and RME.md` | Garza et al. (2021) | Cakupan FHIR untuk pertukaran data *eSource* penelitian klinis | Model Data FHIR | **[35]** |
| **P22** | `papers/FHIRSystem/md/P22 FHIR Implementation barriers Indonesia.md` | Savandha et al. (2026) | Hambatan implementasi interoperabilitas RME di RSUD daerah | Konteks Faskes Daerah | **[24]** |
| **P23** | `papers/SupportingData/md/P23 Readmissions and HF.md` | Tung et al. (2016) | Prognosis buruk dan tingkat readmisi 30 hari pasien gagal jantung | Epidemiologi Klinis | **[3]** |
| **P24** | `papers/PatientHFManagement/md/P24 Guidance for HF Management.md` | Køber et al. (2026) | Pedoman ESC 2026 tatalaksana dan pemantauan gagal jantung | Pedoman Praktik Klinis | **[33]** |
| **P25** | `papers/SupportingData/md/P25 Biomarkers and HF.md` | Núñez et al. (2022) | Taksonomi 4 fenotipe kongesti gagal jantung dan biomarker sirkulasi | Patofisiologi Hemodinamik | **[31]** |
| **P26** | `papers/PatientHFManagement/md/P26 Pre and Post discharge of HF patietns.md` | Metra et al. (2023) | Konsensus ESC-HFA manajemen prapemulangan dan pascarawat | Fase Rentan Pascarawat | **[4]** |
| **P27** | `papers/FHIRSystem/md/P27 FHIR and CDSS making.md` | Semenov et al. (2019) | Pengembangan platform data FHIR untuk penyediaan layanan CDSS | Arsitektur CDSS | **[39]** |
| **P28** | `papers/FHIRSystem/md/P28 Indonesia Doctor opinions on electronic systems.md` | Kamil et al. (2020) | Persepsi dokter Indonesia terhadap sistem dokumentasi elektronik | Persepsi Klinisi Faskes RI | **[30]** |
| **P29** | `papers/FHIRSystem/md/P29 Health information system utilization in Indonesia.md` | Aisyah et al. (2025) | Evaluasi sistem informasi kesehatan di 10.260 Puskesmas Indonesia | Fragmentasi Faskes Nasional | **[18]** |
| **P30** | `papers/CDSSandMonitoring/md/P30 CDSS with FHIR.md` | Strasberg et al. (2021) | Standar CDS modern menggunakan FHIR, CQL, dan CDS Hooks | Standar Logika Klinis | **[29]** |
| **P31** | `papers/CDSSandMonitoring/md/P31 CDSS with FHIR and SMART.md` | Morgan et al. (2022) | Uji klinis CDS Hooks meningkatkan utilisasi aplikasi SMART 130% | Evaluasi Alur Kerja CDSS | **[41]** |
| **P32** | `papers/CDSSandMonitoring/md/P32 ML for CDSS review.md` | Susanto et al. (2023) | Pengaruh CDSS kardiovaskular tingkat bantuan (*assistive*) | Evaluasi CDSS Klinis | **[38]** |
| **P33** | `papers/FHIRSystem/md/P33 EHR, Interoperability and factors for CDSS.md` | Isabelle et al. (2025) | Evaluasi CDSS terstandarisasi bebas *alert fatigue* di RME | Kualitas Keputusan Klinis | **[40]** |
| **P34** | `papers/CDSSandMonitoring/md/P34 Systematic review for CDS.md` | Hak et al. (2022) | Tinjauan sistematik CDSS: isolasi sistem dan maturitas level 2 | Kesenjangan Riset CDSS | **[37]** |
| **P35** | `papers/SupportingData/md/P35 Rule based CDSS review.md` | Papadopoulos et al. (2022) | Tinjauan teknologi dan standar dalam pengembangan rule-based CDSS | Mesin Aturan & RME | **[36]** |
| **P36** | `papers/SupportingData/md/P36 GBD in data for Cardiovascular problems in INdonesia.md` | Muharram et al. (2024) | Analisis Global Burden of Disease beban kardiovaskular Indonesia | Beban Penyakit Nasional | **[2]** |
| **P37** | `papers/PatientHFManagement/md/P37 Remote Monitoring for HF management at home.md` | Stevenson et al. (2023) | Pernyataan ilmiah JACC: pemantauan jarak jauh gagal jantung di rumah | Kinetika Hemodinamik | **[32]** |
| **P38** | `papers/FHIRSystem/md/P38 Effect of EHR for CDSS in at home care.md` | Weiner et al. (2022) | RCT JAMA: CDSS terkontekstualisasi RME melipatgandakan luaran | Kontekstualisasi Perawatan | **[15]** |
| **Reg 1** | `papers/Regulations/md/UU Nomor 17 Tahun 2023.md` | UU No. 17 Tahun 2023 | Undang-Undang Kesehatan Republik Indonesia | Regulasi Primer RI | **[22]** |
| **Reg 2** | `papers/Regulations/md/UU PERMENKES 24 2024 TENTANG RME.md` | Permenkes No. 24 Th 2022 | Peraturan Menteri Kesehatan tentang Rekam Medis Elektronik | Regulasi Teknis RME | **[16]** |
| **Reg 3** | `papers/Regulations/md/2022kepmenkes1423.md` | Kepmenkes HK.01.07/1423 | Pedoman Variabel dan Meta Data Penyelenggaraan RME | Standar Data Klinis RI | **[21]** |

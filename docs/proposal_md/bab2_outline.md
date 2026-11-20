# Panduan Penulisan & Kerangka Pengembangan BAB II (Tinjauan Pustaka)
## Master Outline & Drafting Blueprint untuk Agen Penulis Bab II

Dokumen ini adalah spesifikasi teknis dan panduan penulisan operasional mandiri bagi agen yang bertugas merevisi dan menyusun naskah lengkap **Bab II (Tinjauan Pustaka)** pada proposal tugas akhir. Dokumen ini memetakan seluruh benang merah konseptual, perubahan alur berpikir, pembagian paragraf, klaim literatur bernomor IEEE [1]–[41], serta draf naskah rekomendasi untuk subbab yang memerlukan penulisan ulang total.

---

## 0. KONTEKS PROYEK & PERGESERAN ALUR PENGEMBANGAN (BACKGROUND & FLOW EVOLUTION)

### 0.1 Identitas dan Batasan Inti
* **Judul Tugas Akhir**: *Pengembangan Sistem Pendukung Keputusan Klinis Berbasis Interoperabilitas Data Rekam Medis Elektronik dan Pengukuran Kardiovaskular RADAR*
* **Repositori & Berkas Acuan**:
  * Draf Proposal Saat Ini: `proposal_md/proposal.md`
  * Katalog Sumber & Klaim: `proposal_md/daftar_sumber_dan_klaim.md`
  * Matriks Sitasi Silang: `proposal_md/citations.md`
  * Panduan Proposal: `proposal_guide/panduan_proposal.md`
* **Prinsip Kontribusi Utama**: Kontribusi penelitian terletak pada **rekayasa sistem perangkat lunak, interoperabilitas data kesehatan (HL7 FHIR & SATUSEHAT), dan integrasi alur data klinis**, BUKAN pada pembuatan perangkat keras sensor RADAR dan BUKAN pada perancangan algoritma diagnosis/prediksi baru.

### 0.2 Pergeseran Alur Berpikir (Slight Changes in Background & Flow)
Dibandingkan versi awal proposal, terjadi beberapa penyesuaian alur berpikir yang wajib tercermin pada Bab II:
1. **Pergeseran dari "Pemantauan" ke "Pengukuran"**:
   * Dosen pembimbing menegaskan bahwa perangkat RADAR kelompok riset berfungsi sebagai instrumen **pengukuran (*measurement*)**, bukan pemantauan rawat jalan kontinu (*monitoring*).
   * Kata "pemantauan" hanya digunakan untuk konsep klinis umum (misalnya pemantauan status euvolemia pasien oleh dokter), tetapi instrumen RADAR selalu disebut sebagai alat **"pengukuran"**.
2. **Urgensi Klinis Fase Pascamulang (*Vulnerable Post-Discharge Phase*)**:
   * Alur klinis kini berakar kuat pada tingginya angka rawat inap ulang (readmisi) dan mortalitas 30 hari hingga 6 bulan pascarawat gagal jantung (Tung et al. [3], Metra et al. [4]).
   * Pemicu utamanya adalah **kongesti sisa (*residual congestion*) subklinis** yang luput saat pasien dipulangkan (30,9% pasien).
3. **Diferensiasi 4 Kompartemen Kongesti & Kegagalan Telemonitoring Berat Badan**:
   * Kongesti bukan fenomena seragam. Berdasarkan Núñez et al. [31], kongesti terbagi menjadi: intravaskular paru, jaringan paru, intravaskular sistemik, dan jaringan sistemik.
   * Kenaikan tekanan vena sentral (CVP/JVP) mendahului akumulasi cairan di jaringan.
   * Stevenson et al. [32] membuktikan bahwa telemonitoring berbasis berat badan harian dan gejala sesak napas sering kali memberi hasil netral karena gejala fisik baru muncul 24–48 jam sebelum kejadian akut, sedangkan tekanan hemodinamik vena telah meningkat berminggu-minggu sebelumnya.
4. **Multidimensi vs. Pengukuran Tunggal (Jawaban Kritik "Termometer")**:
   * JVP adalah gelombang kaya fitur hemodinamik, namun nilai prognostiknya tidak independen jika berdiri sendiri (Drazner et al. [12]).
   * Fudim et al. [14] (SCALE-HF 1) membuktikan indeks multiparameter mendeteksi 70% perburukan vs 35% aturan berat badan tunggal.
   * Weiner et al. [15] membuktikan integrasi konteks RME pada CDSS meningkatkan adaptasi rencana dokter 2,67× dan luaran klinis 2,13×. Oleh karena itu, JVP harus diintegrasikan dengan konteks data klinis RME.
5. **Realitas Fragmentasi Faskes Indonesia & Peran FHIR**:
   * RME wajib menurut Permenkes 24/2022 [16], UU 17/2023 [22], dan Kepmenkes 1423/2022 [21].
   * Namun data di lapangan terfragmentasi parah: survei DTO Kemenkes membuktikan Puskesmas menjalankan rata-rata 30 aplikasi dengan 49% entri ganda (Aisyah et al. [18]), dan RSUD daerah terkendala *vendor lock-in* (Savandha et al. [24]).
   * Standar HL7 FHIR bertindak sebagai **model data kanonikal** untuk menjembatani heterogenitas format RME, sinyal RADAR, dan ECG 12 sadapan.

---

## 1. ATURAN PENULISAN WAJIB (STYLE RULES)

Seluruh teks narasi Bab II yang disusun agen wajib mematuhi aturan ketat berikut:
1. **Bahasa Indonesia Baku & Mengalir**: Gaya penulisan ilmiah yang lugas, tidak bertele-tele, tidak menggunakan pembuka klise (*"Di era digital saat ini"*, *"Seiring berjalannya waktu"*).
2. **Dilarang Menggunakan Tanda Hubung / Dash**:
   * Teks narasi **TIDAK BOLEH** memuat tanda hubung (*hyphen* `-`), *en-dash* (`–`), atau *em-dash* (`—`).
   * Kata ulang ditulis dengan variasi (*"berbagai data"*, bukan *"data-data"*).
   * Kata berimbuhan serapan ditulis serangkai (*"noninvasif"*, *"nirkontak"*, *"antarsistem"*, *"multiparameter"*, *"interoperabilitas"*).
   * Rentang angka ditulis dengan kata (*"25% sampai 30%"*, bukan *"25-30%"*).
   * *Pengecualian*: Tanda pisah hanya diperbolehkan pada metadata bibliografis di DAFTAR PUSTAKA (rentang halaman IEEE, nomor DOI).
3. **Format Paragraf Utuh (Tanpa Bullet Points)**: Seluruh narasi subbab disajikan dalam bentuk paragraf mengalir yang saling menyambung logikanya. Jangan gunakan daftar butir (*bullet points*) pada tinjauan pustaka.
4. **Sitasi IEEE Berurutan Sesuai Kemunculan Pertama**:
   * Format sitasi bernomor kurung siku sebelum titik akhir kalimat: `... status hemodinamik pasien [4].`
   * Rentang sitasi: `[4], [5]` atau `[4] sampai [6]`.
   * **DILARANG MERUBAH NOMOR SITASI**: Urutan sitasi terkunci pada [1] sampai [41] sesuai Daftar Pustaka naskah proposal.
5. **Integritas Istilah Teknis**:
   * Jangan gunakan *"citra RADAR"* → gunakan *"data hasil pengukuran RADAR"*.
   * Jangan gunakan *"pemantauan"* untuk alat RADAR → gunakan *"pengukuran"*.
   * Jangan klaim CDSS membuat *"diagnosis"* atau *"prediksi"* mandiri → posisikan sebagai *"pendukung pertimbangan keputusan klinis bagi tenaga medis"*.

---

## 2. PETA STRUKTUR SUBBAB BAB II

| Subbab | Judul Subbab | Status Evaluasi | Rekomendasi Tindakan bagi Agen Penulis |
|:---:|---|:---:|---|
| **2.1** | Penyakit Kardiovaskular, Gagal Jantung, dan Kongesti Vena | Diterima (OK) | Pertahankan draf yang ada; perhalus kohesi antarkalimat; pastikan angka-angka klinis tepat. |
| **2.2** | Deteksi Jugular Vein Pulse melalui Modalitas RADAR | Diterima (OK) | Pertahankan struktur; pastikan validasi korelasi linear Shi et al. [34] dan modul SVM Yen et al. [11] tersaji runtut. |
| **2.3** | Rekam Medis Elektronik dan Data Pasien | Diterima (OK) | Pertahankan; pastikan pemisahan antara regulasi nasional ([16], [21], [22]), fragmentasi ([18], [24]), dan PGHD/eSource ([17], [19], [27], [28], [35]) tetap tegas. |
| **2.4** | Interoperabilitas melalui Platform FHIR | **BURUK (DOGSHIT) — TULIS ULANG TOTAL** | **Lakukan restrukturisasi total menjadi 5 sub-paragraf tematik logis**. Terapkan draf rekomendasi pada Bagian 4 dokumen ini. |
| **2.5** | Sistem Pendukung Keputusan Klinis dan Manajemen Data | Diterima (OK) | Pertahankan alur: definisi CDSS & assistive framing ([36]–[38]), arsitektur 5 tahap & microservices ([39], [11], [9], [7]), dan CDS Hooks ([29], [40], [41]). |
| **2.6** | Penelitian Terkait dan Kesenjangan Penelitian | Khusus Mahasiswa | **Tinggalkan kosong**; tuliskan hanya judul heading dan placeholder `[diisi mahasiswa]`. |
| **2.7** | Rasional | Diterima (OK) | Pertahankan 2 paragraf sintesis; pastikan batasan klaim penutup tetap tegas. |

---

## 3. PANDUAN RINCI SUBBAB YANG SUDAH DITERIMA (2.1, 2.2, 2.3, 2.5, 2.7)

### 3.1 Subbab 2.1 — Penyakit Kardiovaskular, Gagal Jantung, dan Kongesti Vena
* **Tujuan**: Membangun urgensi klinis dari tingkat epidemiologi makro hingga patofisiologi hemodinamik mikro.
* **Pembagian Paragraf**:
  * **Paragraf 1 (Beban Penyakit & Kerentanan Pascarawat)**:
    * Kematian CVD global 19,8 juta jiwa (32% total kematian, 85% serangan jantung & stroke, >75% di LMIC) menurut WHO [1].
    * Beban Indonesia naik 2× lipat dalam 30 tahun (292 ribu ke 659 ribu), DALYs peringkat 2 terburuk di ASEAN [2].
    * Gagal jantung sebagai muara akhir: readmisi 30 hari 10,9% dengan mortalitas 6 bulan 27,66% vs 10,36% [3].
    * Fase rentan pascamulang (*vulnerable phase*): mortalitas melonjak >6× pada bulan pertama, sepertiga hingga separuh pasien dirawat ulang dalam 6 bulan [4].
  * **Paragraf 2 (Patofisiologi Kongesti & Kinetika Hemodinamik)**:
    * Taksonomi 4 kompartemen kongesti: intravaskular paru, jaringan paru, intravaskular sistemik, jaringan sistemik [31].
    * Kenaikan tekanan intravaskular sistemik (CVP/JVP) mendahului akumulasi cairan di jaringan [31].
    * Keterbatasan parameter konvensional: berat badan dan dispnea baru muncul 24 sampai 48 jam sebelum dekompensasi akut, sedangkan tekanan hemodinamik naik berminggu-minggu sebelumnya; telemonitoring berat badan terbukti netral [32].
    * Keunggulan multiparameter: uji SCALE-HF 1 membuktikan indeks multiparameter mendeteksi 70% kejadian vs aturan berat badan 35% [14].
    * Pedoman ESC 2026: pemantauan euvolemia berkelanjutan dan tanda kongesti residual [33]. Persistensi elevasi JVP saat pulang memprediksi perburukan kardiovaskular 1 tahun berikutnya [13].
  * **Paragraf 3 (CVP, Kateterisasi Invasif, dan Batasan Bedside JVP)**:
    * CVP sebagai penanda kongesti vena; hubungannya dengan penurunan gradien perfusi ginjal dan sindrom kardiorenal [5].
    * Kateterisasi vena sentral sebagai baku emas bersifat invasif dan tidak praktis untuk evaluasi rutin [6].
    * JVP interna sebagai cerminan tekanan atrium kanan karena tidak memiliki katup [7].
    * Penilaian visual di sisi tempat tidur (*bedside*) sangat subjektif dan tidak akurat, terutama pada residen pelatihan atau pasien leher tebal [6], [8].

### 3.2 Subbab 2.2 — Deteksi Jugular Vein Pulse melalui Modalitas RADAR
* **Tujuan**: Menjelaskan biofisika gelombang JVP dan kelayakan teknologi penderiaan RADAR nirkontak.
* **Pembagian Paragraf**:
  * **Paragraf 1 (Fisiologi Gelombang JVP & Kebutuhan Sinkronisasi ECG)**:
    * Fitur gelombang JVP: puncak a (kontraksi atrium), c (penonjolan katup trikuspid), v (pengisian atrium) serta lembah x (relaksasi atrium) dan y (pengosongan atrium) [7].
    * Dua gelombang pengosongan vena sinkron dengan lembah x pada sistol dan lembah y pada diastol [7].
    * Informasi morfologi gelombang jauh lebih kaya daripada angka tekanan tunggal, dan hanya terbaca jika diselaraskan dengan acuan siklus jantung (ECG) [7].
  * **Paragraf 2 (Prinsip Biofisika RADAR & Evaluasi Mutu Sinyal)**:
    * Prinsip Doppler dan *backscattering*: membaca pergeseran fase dari gerakan mikro permukaan kulit akibat pulsasi pembuluh [9].
    * Dataset Six-Port 24 GHz continuous wave (CW) tersinkronisasi ECG: rekaman ~24 jam dari 30 subjek sehat dalam 5 skenario provokasi hemodinamik (Valsalva, apnea, tilt table), menembus busana tipis tanpa sentuhan [9].
    * Korelasi linear antara pergeseran fase radar CW dengan perpindahan dinding vaskular yang diukur menggunakan ultrasonografi [34].
    * Kerentanan artefak gerak di lingkungan klinis: modul evaluasi mutu sinyal berbasis Support Vector Machine (SVM) mengklasifikasikan kualitas sinyal dengan akurasi 93,2% sampai 100%, deviasi detak jantung hanya 0 sampai 4 denyut per menit [11].
  * **Paragraf 3 (Aplikasi Penderiaan JVP Nirkontak)**:
    * Sensor gelombang mikro 24 GHz daya rendah (7 mW): responsif terhadap perubahan kemiringan tubuh 0 sampai 75 derajat, merekam pulsasi halus tanpa menekan vena [10].
    * RADAR FMCW 60 GHz dengan *eigen beamforming*: memisahkan sinyal vena jugularis dari arteri karotis pada sudut leher, divalidasi terhadap PPG dan kateter vena sentral [6]. Catatan jujur: berstatus studi kelayakan awal dengan ukuran sampel terbatas.

### 3.3 Subbab 2.3 — Rekam Medis Elektronik dan Data Pasien
* **Tujuan**: Menjelaskan ekosistem data RME nasional, realitas fragmentasi faskes, serta peran data luaran mandiri pasien (PGHD).
* **Pembagian Paragraf**:
  * **Paragraf 1 (Landasan Regulasi RME Nasional)**:
    * Kewajiban RME seluruh faskes di Indonesia dengan standar keamanan, keutuhan, kerahasiaan, dan pembukaan interoperabilitas (Permenkes 24/2022 [16]).
    * Standar variabel minimum dan metadata rekam medis rawat jalan, rawat inap, dan gawat darurat (Kepmenkes 1423/2022 [21]).
    * Mandat kepatuhan sistem informasi dan teknologi kesehatan terhadap standar interoperabilitas nasional serta hak akses pasien terhadap rekam medisnya (UU 17/2023 [22]).
    * Muara platform terintegrasi nasional: SATUSEHAT [cite: dokumentasi resmi SATUSEHAT].
  * **Paragraf 2 (Tantangan Fragmentasi Data di Fasyankes Indonesia)**:
    * Realitas lapangan: survei nasional 10.260 Puskesmas menunjukkan rata-rata 30 aplikasi per faskes, tenaga kesehatan memasukkan data ke hingga 6 sistem berbeda, 49% sistem menuntut entri ganda, dan 29% tanpa analisis otomatis (Aisyah et al. [18]).
    * Kendala di RSUD daerah: studi di 12 RSUD tipe C dan D mengungkap hambatan keterikatan vendor (*vendor lock-in*), keragaman format data instrumen medis, dan perlunya lapisan perantara (*middleware*) yang ringan (Savandha et al. [24]).
    * Persepsi dokter: dokumentasi terfragmentasi menimbulkan sekat komunikasi antarprofesi medis dan keterlambatan verifikasi tindakan (Kamil et al. [30]).
  * **Paragraf 3 (Kedaulatan Akses Pasien, PGHD, dan eSource)**:
    * Manfaat pembukaan akses rekam medis dan pemanfaatan Patient Generated Health Data (PGHD): meningkatkan kesadaran, perawatan mandiri, kualitas hidup, kepatuhan terapi, dan menurunkan kecemasan klinis (Tapuria et al. [19]).
    * Mekanisme kontrol akses desentralisasi: framework DecMed memadukan buku besar IOTA dan kendali kapabilitas (CapBAC), memungkinkan pasien memberi, mencabut, dan membatasi masa berlaku akses rekam medisnya (Purnama et al. [17]).
    * Implementasi teknis integrasi PGHD ke FHIR: data sensor perangkat kesehatan Garmin dialirkan ke server FHIR melalui API terpusat dengan kepatuhan regulasi privasi (Abedian et al. [27]); arsitektur SMART on FHIR mengalirkan data luaran mandiri pasien ke 3 vendor EHR di 18 klinik (Wesley et al. [28]).
    * Konsep eSource: ekstraksi data langsung dari RME lewat resource FHIR standar mengeliminasi transkripsi manual dan menjaga keutuhan data (Garza et al. [35]).

### 3.4 Subbab 2.5 — Sistem Pendukung Keputusan Klinis dan Manajemen Data
* **Tujuan**: Memetakan prinsip arsitektur CDSS, perancangan aliran data, serta mekanisme integrasi alur kerja klinis.
* **Pembagian Paragraf**:
  * **Paragraf 1 (Konseptualisasi CDSS, Dominasi Aturan, dan Bantuan Klinis)**:
    * Definisi CDSS: sistem berbasis pengetahuan aktif yang memadukan data spesifik pasien untuk menghasilkan saran yang disesuaikan [36].
    * Jurang pemisah integrasi: dari 1.731 makalah CDSS berbasis aturan, hanya 15 yang dievaluasi klinis ketat, hanya 2 yang terintegrasi langsung dengan EHR, dan hanya 3 yang menggunakan standar teknologi kesehatan resmi HL7 [36].
    * Dominasi modul berbasis aturan sebagai pendekatan paling transparan dan terjelaskan, namun 51,92% CDSS dibangun sebagai aplikasi yang berdiri sendiri (*standalone*) sehingga gagal di alur kerja [37].
    * Prinsip *assistive*: CDSS kardiovaskular yang sukses diadopsi dokter harus bersifat bantuan, menyajikan sintesis data tanpa mengambil alih keputusan dokter, dan menyatu dalam alur kerja yang ada [38].
  * **Paragraf 2 (Arsitektur Aliran Data Lima Tahap & Peran Sinyal Acuan)**:
    * Arsitektur aliran data terbagi menjadi 5 modul berurutan: penyerapan data (*ingest*), pemeriksaan mutu (*quality check*), penggabungan konteks (*context join*), evaluasi aturan (*rules*), dan penyajian visual (*display*).
    * Landasan arsitektur mikroservis: platform manajemen data medis berbasis FHIR memisahkan modul komunikasi dari mesin inferensi, terbukti memproses ~50.000 transaksi per hari dengan >400 model aturan keputusan [39].
    * Tahap pemeriksaan mutu mutlak diperlukan untuk menyaring artefak gerak sinyal RADAR sebelum diproses secara klinis [11].
    * Rekaman ECG 12 sadapan berperan sebagai acuan waktu mekanis dan sinyal pembanding bagi data RADAR [9], khususnya untuk membedakan fase pengosongan sistol dan diastol gelombang vena [7].
    * Kebutuhan manajemen basis data dalam menyimpan dan menggabungkan data deret waktu fisiologis bersama data relasional RME FHIR [cite: rujukan manajemen basis data untuk data deret waktu dan FHIR].
  * **Paragraf 3 (Integrasi Alur Kerja Aktif via CDS Hooks)**:
    * Pemicu berbasis peristiwa (*event-driven*): standar CDS Hooks memicu layanan CDSS eksternal secara otomatis saat dokter membuka berkas rekam medis atau mencatat hasil pemeriksaan baru tanpa interupsi manual [29].
    * Pembuktian keandalan berbasis standar: evaluasi 3 instrumen CDS berbasis CQL, CDS Hooks, dan FHIR pada RME akademik menghasilkan akurasi 96% sampai 100% dan laju peringatan positif palsu yang sangat rendah (0,0% sampai 11,1%) [40].
    * Utilisasi dokter: uji acak klaster pada 70 dokter selama 7 bulan membuktikan bahwa integrasi CDS Hooks meningkatkan pemanfaatan aplikasi rujukan SMART on FHIR sebesar 130% [41].
    * Prinsip akhir: rekomendasi pendukung keputusan harus hadir tepat waktu di dalam alur kerja tanpa membebani kognisi dokter.

### 3.5 Subbab 2.7 — Rasional
* **Tujuan**: Merangkum sintesis literatur menjadi justifikasi logis arah pengembangan sistem tugas akhir.
* **Isi & Batasan**: Pertahankan 2 paragraf padat dari naskah draf proposal. Paragraf 1 menyimpulkan bahwa data pengukuran RADAR bernilai tinggi namun membutuhkan konteks RME agar bermakna secara klinis, dan FHIR diperlukan untuk mengatasi jurang format keduanya. Paragraf 2 menegaskan lingkup rekayasa perangkat lunak sistem terintegrasi, pemanfaatan ECG 12 sadapan sebagai acuan waktu, fitur kedaulatan data pasien, serta penegasan mutlak bahwa sistem menghasilkan pendukung keputusan dan bukan penentu diagnosis otomatis.

---

## 4. PANDUAN RESTRUKTURISASI TOTAL SUBBAB 2.4 (INTEROPERABILITAS MELALUI PLATFORM FHIR)

> **MENGAPA SUBBAB 2.4 SEBELUMNYA DIANGGAP BURUK**:
> Naskah lama mencampuradukkan definisi terminologi, resource FHIR, tantangan perangkat keras, pipeline streaming, dan Implementation Guide nasional ke dalam paragraf yang tumpang tindih tanpa hierarki logis. Paragraf melompat dari akronim tanpa penjelasan ke tantangan ISO/IEEE secara mendadak.

### 4.1 Hierarki Logis Lima Sub-Paragraf (Wajib Dipatuhi)
Subbab 2.4 harus dibangun dengan struktur berlapis yang mengalir dari landasan semantik hingga sintesis model kanonikal:
1. **Sub-paragraf A (Lapisan Semantik Terminologi)**: ICD untuk penyakit, SNOMED CT untuk konsep klinis, LOINC untuk observasi/lab. Menjelaskan bahwa terminologi menjawab *"apa arti kode ini"*, tetapi bukan format pertukaran data. Implementasi FHIR global memadukannya: LOINC 37%, SNOMED CT 29%, ICD 18% (Vorisek et al. [25]).
2. **Sub-paragraf B (Kerangka Pertukaran Modular FHIR)**: HL7 FHIR menyusun data sebagai resource modular (Observation, Patient, Encounter, Device, DiagnosticReport), dibatasi profil, dan dipertukarkan lewat REST API. Menghadirkan interoperabilitas sintaktik sekaligus semantik (Vorisek et al. [25]).
3. **Sub-paragraf C (Jembatan Perangkat Medis ke FHIR)**: Data instrumen perangkat medis ISO/IEEE 11073 memiliki abstraksi berbeda dari RME, namun dapat dipetakan ke FHIR Observation dan Device. 25 tantangan teknis (status perangkat, stempel waktu, konteks metrik); profil yang valid secara sintaksis belum menjamin kebenaran semantik sehingga verifikasi makna eksplisit diperlukan (Riech et al. [23]).
4. **Sub-paragraf D (Pipeline Aliran Data Fisiologis Real-Time)**: Pembuktian kelayakan transmisi data deret waktu dari sensor nirkabel ke FHIR Observation secara real-time dengan latensi <1 detik dan 0% packet loss (Adochiei et al. [26]). Memvalidasi jalur: keluaran pengukuran RADAR → FHIR Observation → basis data → visualisasi.
5. **Sub-paragraf E (Ekosistem Indonesia: Implementation Guide SATUSEHAT & CDS)**: Implementation Guide ECG 12 sadapan yang patuh SATUSEHAT FHIR R4 (Chaidir & Hareva [20]) memetakan aECG ke Observation/Device dengan 17 atribut inti dan provisional ValueSets untuk menutup keterbatasan SNOMED CT. Menjadi cetak biru metodologis bagi pemetaan data fisiologis kardiovaskular RADAR. Dipadukan dengan Clinical Quality Language (CQL) dan CDS Hooks untuk memisahkan logika klinis dari RME lokal (Strasberg et al. [29]).
6. **Kalimat Penutup Subbab 2.4**: Penetapan FHIR sebagai model data kanonikal tunggal yang mempersatukan data pengukuran RADAR, ECG 12 sadapan, dan data riwayat RME dalam satu format terstandar.

---

### 4.2 Draf Naskah Rekomendasi Subbab 2.4 (Siap Diadopsi oleh Agen Penulis)

Berikut adalah naskah lengkap Bahasa Indonesia untuk Subbab 2.4 yang telah mematuhi seluruh kaidah gaya (tanpa tanda hubung, kalimat mengalir, sitasi presisi, dan alur bertingkat):

```markdown
Interoperabilitas melalui platform FHIR

Standardisasi data medis melibatkan pemisahan tegas antara terminologi semantik dan kerangka pertukaran data. Terminologi klinis memiliki ranah tugas yang saling melengkapi: International Classification of Diseases bertugas mengklasifikasikan diagnosis penyakit dan penyebab kematian, Systematized Nomenclature of Medicine Clinical Terms menyediakan perbendaharaan konsep klinis komprehensif untuk prosedur serta temuan fisik, dan Logical Observation Identifiers Names and Codes menetapkan kodefikasi baku bagi hasil observasi serta pemeriksaan laboratorium [cite: dokumentasi resmi ICD, SNOMED CT, dan LOINC]. Meskipun menjadi acuan penamaan makna medis secara global, standar terminologi tersebut tidak mengatur mekanisme transmisi maupun struktur pembungkus data antarperangkat lunak. Tinjauan sistematis terhadap empat puluh sembilan studi penerapan Fast Healthcare Interoperability Resources di bidang riset kesehatan mengungkap bahwa implementasi pertukaran data klinis paling banyak memadukan standar LOINC sebesar tiga puluh tujuh persen, SNOMED CT sebesar dua puluh sembilan persen, dan ICD sepuluh sebesar delapan belas persen guna menjamin integritas semantik informasi yang dipertukarkan [25].

Organisasi Health Level Seven International mengembangkan FHIR sebagai standar generasi baru yang menyusun informasi klinis ke dalam entitas modular yang disebut resource, seperti Patient, Encounter, Observation, DiagnosticReport, dan Device. Setiap resource mendefinisikan batas data yang terstruktur rapi, dapat diperluas atau dibatasi melalui penyusunan profil khusus sesuai kebutuhan klinis tertentu, serta dipertukarkan melalui protokol Representational State Transfer Application Programming Interface. Pola interaksi berbasis layanan web ini memungkinkan pertukaran data medis berlangsung secara konsisten antarsistem yang heterogen, sehingga menghadirkan interoperabilitas sintaktik sekaligus semantik dalam satu kerangka kerja terpadu [25]. Kajian literatur mencatat pemanfaatan FHIR terdistribusi secara luas untuk standardisasi data sebesar empat puluh satu persen, penangkapan data sebesar dua puluh sembilan persen, dan kebutuhan analisis klinis sebesar dua belas persen, dengan tingkat keterpakaian ulang yang tinggi pada berbagai skenario kesehatan digital [25].

Tantangan interoperabilitas meningkat ketika data berasal dari instrumen perangkat keras biomedis. Perangkat medis pada umumnya mengadopsi model domain ISO atau IEEE sepuluh ribu dua ratus tujuh yang memiliki struktur abstraksi data yang berbeda dari model rekam medis rumah sakit. Melalui panduan implementasi yang terdefinisi cermat, data instrumen tersebut dapat dipetakan secara konsisten ke dalam resource FHIR Observation dan Device tanpa mengorbankan konteks pengukuran asalnya [23]. Walaupun demikian, pemetaan data perangkat medis ke FHIR terbukti menghadapi dua puluh lima tantangan teknis spesifik, antara lain penanganan stempel waktu beresolusi tinggi, representasi status operasional perangkat, dan kalibrasi konteks metrik [23]. Pembuatan profil resource yang valid secara sintaksis tidak otomatis menjamin kebenaran makna klinis, sehingga proses transformasi data dari instrumen penderiaan memerlukan validasi semantik yang eksplisit agar nilai pengukuran tidak mengalami misinterpretasi saat diterima oleh sistem rekam medis [23].

Di samping pemetaan struktur statis, transmisi data deret waktu fisiologis menuntut jalur pipa aliran data yang andal dan berkecepatan tinggi. Pemanfaatan kerangka kerja sumber terbuka berbasis FHIR untuk akuisisi sinyal biomedis dari simpul sensor nirkabel membuktikan bahwa data gelombang fisiologis deret waktu dapat ditransmisikan dan dipetakan secara langsung ke dalam resource Observation secara waktu nyata [26]. Implementasi arsitektur komunikasi tersebut mencatatkan kinerja transmisi yang stabil dengan latensi rata rata di bawah satu detik serta tingkat kehilangan paket data sebesar nol persen [26]. Ketercapaian efisiensi transmisi ini memberikan landasan empiris bahwa aliran data hasil pengukuran instrumen biomedis nirkontak dapat diserap secara waktu nyata ke dalam ekosistem FHIR tanpa menimbulkan beban penundaan komputasi yang berarti.

Di Indonesia, implementasi platform nasional SATUSEHAT menetapkan standar FHIR Release 4 sebagai fondasi pertukaran data kesehatan antarfasilitas pelayanan. Sebagai rujukan penanganan data kardiovaskular, panduan implementasi rekaman elektrokardiogram dua belas sadapan yang sepenuhnya patuh terhadap spesifikasi SATUSEHAT telah berhasil memetakan standar industri HL7 aECG ke dalam resource Observation, DiagnosticReport, dan Device [20]. Panduan tersebut mereduksi tiga ratus dua belas atribut kompleks pada rekaman elektrokardiogram menjadi tujuh belas atribut pertukaran data inti yang esensial, sekaligus menyelesaikan keterbatasan kosakata SNOMED CT yang semula hanya mencakup tiga belas dari tiga puluh dua jenis sadapan menggunakan kumpulan nilai sementara atau provisional ValueSets [20]. Pendekatan metodologis ini menjadi cetak biru teknis yang sangat relevan dalam memetakan data gelombang hasil pengukuran RADAR dan sinyal elektrokardiogram pendukung ke dalam skema profil SATUSEHAT. Standar klinis modern kemudian memadukan model data FHIR dengan Clinical Quality Language dan CDS Hooks, sehingga modul logika pendukung keputusan dapat dipisahkan secara independen dari basis kode rekam medis lokal dan dijalankan lintas institusi pelayanan kesehatan [29]. Melalui arsitektur ini, standar FHIR memegang peranan krusial sebagai model data kanonikal terpadu yang menyatukan data hasil pengukuran RADAR, sinyal elektrokardiogram referensi, dan data riwayat pasien rekam medis elektronik ke dalam satu format bersama yang siap diolah oleh sistem pendukung keputusan klinis.
```

---

## 5. REKONSILIASI SITASI KHUSUS & PLACEHOLDER YANG HARUS DIPERHATIKAN

Agen penulis wajib memperhatikan bahwa naskah proposal memuat beberapa entri yang sengaja dipertahankan sebagai placeholder terbuka:

| No. Sitasi / Tanda | Makalah / Topik | Status di Proposal Saat Ini | Tindakan yang Harus Diambil Agen Penulis |
|:---:|---|---|---|
| **[8]** | Storrow et al. (2007, *Am. J. Cardiol.*) | Penulis dan judul kosong di Daftar Pustaka; DOI: `10.1016/j.amjcard.2007.01.037` | Gunakan nomor sitasi [8] pada teks narasi Bab 2.1 P3; jangan ubah nomor; jangan mengarang judul di daftar pustaka. |
| **[12]** | Drazner et al. (2009, *Am. J. Cardiol.*) | Penulis dan judul kosong di Daftar Pustaka; DOI: `10.1016/j.amjcard.2008.11.045` | Gunakan nomor sitasi [12] pada teks narasi Bab 2.7 P1; jangan ubah nomor. |
| **[26]** | Adochiei et al. (2024, *Sensors*) | DOI tertulis `[cite: lengkapi DOI]` | Gunakan sitasi [26] pada Subbab 2.4 P4; biarkan placeholder DOI tetap ada di daftar rujukan. |
| **`[new]` × 2** | Studi JVP *two-object method* | Disebut di Bab 1.1 P1 (reliabilitas 82,9%, sensitivitas 43,3%, spesifisitas 67,7%) | Tanda ini berada di Bab 1. Jika agen menyusun Bab 2, gunakan sitasi resmi yang ada ([6], [7], [8]); jangan gunakan tag `[new]` di Bab 2. |
| **`[cite]`** | Dokumentasi Resmi SATUSEHAT | Disebut di Bab 2.3 P1 | Gunakan placeholder `[cite: dokumentasi SATUSEHAT]` jika belum ada URL rujukan pasti. |
| **`[cite]`** | Definisi Resmi ICD, SNOMED CT, LOINC | Disebut di Bab 2.4 P1 | Gunakan placeholder `[cite: dokumentasi resmi ICD, SNOMED CT, dan LOINC]`. |
| **`[cite]`** | Manajemen Basis Data Deret Waktu & FHIR | Disebut di Bab 2.5 P2 | Gunakan placeholder `[cite: rujukan manajemen basis data untuk data deret waktu dan FHIR]`. |
| **2.6** | Penelitian Terkait dan Kesenjangan Penelitian | Bagian yang wajib diisi mandiri oleh mahasiswa | Tuliskan heading `### 2.6 Penelitian Terkait dan Kesenjangan Penelitian` diikuti tepat satu baris `[diisi mahasiswa]`. |

---

## 6. MAKALAH DI FOLDER `papers/` YANG TIDAK BOLEH DISITASI PADA BAB II

Terdapat sejumlah makalah yang tersimpan di repositori namun sengaja **TIDAK DIMASUKKAN** ke dalam Daftar Pustaka naskah proposal oleh mahasiswa. Agen penulis **DILARANG** menambahkan makalah berikut ke dalam Bab II untuk menjaga konsistensi penomoran IEEE:
* **P1 (Bender & Sartipi 2013)**: Makalah pengantar FHIR lama; substansi interoperabilitas FHIR telah diwakili oleh tinjauan sistematis Vorisek et al. [25].
* **P12 (Lu et al. 2020)**: Tinjauan umum perangkat *wearable*.
* **P15 (Baker et al. 2017)**: Tinjauan IoT kesehatan generik.
* **P17 (Kruse et al. 2017)**: Tinjauan adopsi telemedisin.
* **P19 (Kim et al. 2026)**: Radar ISAC dengan koreksi Bi-LSTM (dicatat mahasiswa memiliki ketidaksesuaian DOI).

---

## 7. CHECKLIST AKHIR SEBELUM PENYERAHAN NASKAH BAB II

Sebelum menyerahkan draf Bab II kepada pengguna, agen penulis wajib memvalidasi daftar periksa berikut:
- [ ] **Bebas Tanda Hubung Narasi**: Tidak ada karakter `-`, `–`, atau `—` pada seluruh tubuh paragraf narasi bahasa Indonesia.
- [ ] **Struktur Mengalir**: Tidak ada poin butir (*bulleted list*) pada Subbab 2.1 sampai 2.5 serta 2.7.
- [ ] **Penyelarasan Subbab 2.4**: Subbab 2.4 telah mengadopsi struktur lima sub-paragraf berurutan: Terminologi → Kerangka FHIR → Pemetaan Perangkat → Pipeline Real-time → Implementation Guide SATUSEHAT & CDS Hooks → Model Data Kanonikal.
- [ ] **Integritas Penomoran Sitasi**: Seluruh nomor sitasi berada di rentang [1] sampai [41] dan bersesuaian persis dengan entri di DAFTAR PUSTAKA.
- [ ] **Batasan Klaim Sistem**: Seluruh kalimat keluaran sistem dirumuskan sebagai pendukung pertimbangan keputusan klinis, bukan penentu diagnosis otomatis.
- [ ] **Placeholder Mahasiswa**: Subbab 2.6 hanya berisi satu baris `[diisi mahasiswa]`.
- [ ] **Catatan Penutup**: Menyertakan bagian catatan di akhir dokumen yang merangkum placeholder terbuka bagi mahasiswa.

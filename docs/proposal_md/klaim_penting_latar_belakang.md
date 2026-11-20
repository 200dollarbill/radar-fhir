# Klaim Penting dan Temuan Literatur Komprehensif untuk Pengayaan Latar Belakang & Sidang Proposal

Dokumen ini menghimpun kompilasi menyeluruh atas klaim-klaim kunci, data statistik mutakhir, landasan patofisiologi klinis, bukti teknis penderiaan RADAR, kaidah informatika medis FHIR, serta regulasi nasional yang diekstraksi secara mendalam dari seluruh makalah di folder `papers/`. Dokumen ini dirancang khusus sebagai **buku pegangan referensi (reference handbook)** bagi mahasiswa untuk:
1. Memperkaya dan mempertajam argumentasi pada setiap paragraf **Latar Belakang (Bab 1.1: P1 sampai P6)**.
2. Membekali mahasiswa dengan **data kuantitatif konkret dan rujukan ilmiah otoritatif** saat menjawab pertanyaan dosen pembimbing dan menguji argumen dalam sidang proposal.

---

## DAFTAR ISI TEMATIK

1. [Tema 1: Epidemiologi Kardiovaskular di Indonesia & Krisis Fragmentasi Faskes](#tema-1-epidemiologi-kardiovaskular-di-indonesia--krisis-fragmentasi-faskes)
   * 1.1 Beban 30 Tahun Penyakit Kardiovaskular di Indonesia (Analisis GBD 2024)
   * 1.2 Data Resmi Fragmentasi Sistem Informasi Puskesmas RI (Kemenkes DTO & UCL 2025)
   * 1.3 Hambatan Interoperabilitas dan *Vendor Lock-In* di RSUD Daerah (Savandha et al. 2026)
   * 1.4 Dampak Dokumentasi Manual pada Keselamatan Pasien dan Sekat Komunikasi (Kamil et al. 2020)
2. [Tema 2: Patofisiologi Kongesti Hemodinamik & Dilema Pemantauan Pascarawat Gagal Jantung](#tema-2-patofisiologi-kongesti-hemodinamik--dilema-pemantauan-pascarawat-gagal-jantung)
   * 2.1 Fase Rentan (*Vulnerable Phase*) & Bahaya Kongesti Sisa Pascarawat (ESC-HFA Metra et al. 2023)
   * 2.2 Taksonomi 4 Fenotipe Kongesti: Mengapa JVP Mendahului Kenaikan Berat Badan? (Núñez et al. 2022)
   * 2.3 Kegagalan Telemonitoring Berat Badan vs. Kinetika Hemodinamik (JACC Stevenson et al. 2023)
   * 2.4 Bukti Kuantitatif: Indeks Kongesti Multiparameter vs. Aturan Berat Badan (SCALE-HF 1 Trial 2025)
   * 2.5 Hubungan Hemodinamik JVP dengan Tekanan Atrium Kanan dan Sindrom Kardiorenal (Kenny et al. 2025)
   * 2.6 Rekomendasi Pedoman ESC 2026 Mengenai Kongesti Vena Jugularis (Køber et al. 2026)
3. [Tema 3: Mengapa Pengukuran JVP Memerlukan Konteks RME? (Menjawab Kritik "Termometer")](#tema-3-mengapa-pengukuran-jvp-memerlukan-konteks-rme-menjawab-kritik-termometer)
   * 3.1 Bukti Uji Klinis Acak JAMA: Efek Kontekstualisasi RME terhadap Luaran Klinis (Weiner et al. 2022)
   * 3.2 Sistem Pendukung Keputusan Bersifat Bantuan (*Assistive CDS*) dan Alur Kerja Dokter (Susanto et al. 2023)
   * 3.3 Bahaya Sistem Monolitik Standalone & Kesenjangan Evaluasi Klinis CDSS (Hak et al. 2022; Papadopoulos et al. 2022)
   * 3.4 Eliminasi *Alert Fatigue* melalui Integrasi Berbasis Standar (Isabelle et al. 2025)
4. [Tema 4: Landasan Fisika & Keunggulan Penderiaan RADAR Nirkontak](#tema-4-landasan-fisika--keunggulan-penderiaan-radar-nirkontak)
   * 4.1 Fisiologi Tekanan Rendah Vena Jugularis & Distorsi Mekanis Sensor Kontak (Suzuki et al. 2021; Das et al. 2024)
   * 4.2 Hubungan Fisik Linear Antara Perpindahan Dinding Pembuluh RADAR dan Kecepatan Aliran USG (Shi et al. 2018)
   * 4.3 Penetrasi Tembus Pakaian & Validasi Hemodinamik Six-Port CW Radar 24 GHz (Schellenberger et al. 2020)
   * 4.4 Evaluasi Kualitas Sinyal Berbasis AI untuk Pengukuran Pasien Geriatri (Yen et al. 2022)
   * 4.5 Koreksi Frekuensi Cerdas Bi-LSTM pada Radar Nirkontak Kompak (Kim et al. IEEE CCNC 2026)
5. [Tema 5: Arsitektur Interoperabilitas Standar FHIR, PGHD, & Ekosistem Digital Nasional](#tema-5-arsitektur-interoperabilitas-standar-fhir-pghd--ekosistem-digital-nasional)
   * 5.1 Penyelesaian Masalah Historis "Curly Braces" Melalui FHIR R4 (Strasberg et al. 2021)
   * 5.2 Pemetaan Sinyal Fisiologis ECG 12-Sadapan ke FHIR R4 SATUSEHAT (Chaidir & Hareva 2025)
   * 5.3 Standarisasi Perangkat Medis Point-of-Care ISO/IEEE 11073 ke FHIR (Riech et al. 2021)
   * 5.4 Transmisi Real-Time Data Sensor Biomedis ke FHIR Tanpa Paket Hilang (Adochiei et al. 2024)
   * 5.5 Integrasi Data Pasien Mandiri (PGHD) Lintas 18 Klinik via SMART on FHIR (Wesley et al. 2021)
   * 5.6 Peningkatan Utilisasi Aplikasi Klinis sebesar 130% melalui CDS Hooks (Morgan et al. 2022)
   * 5.7 Landasan Regulasi Nasional: UU 17/2023, Permenkes 24/2022, & Kepmenkes 1423/2022
6. [Matriks Integrasi: Panduan Penyisipan Klaim ke Paragraf Latar Belakang (P1–P6)](#matriks-integrasi-panduan-penyisipan-klaim-ke-paragraf-latar-belakang-p1p6)

---

## TEMA 1: EPIDEMIOLOGI KARDIOVASKULAR DI INDONESIA & KRISIS FRAGMENTASI FASKES

### 1.1 Beban 30 Tahun Penyakit Kardiovaskular di Indonesia (Analisis GBD 2024)
* **Sumber Makalah**: `papers/SupportingData/md/P36 GBD in data for Cardiovascular problems in INdonesia.md`
* **Sitasi Ilmiah**: F. R. Muharram, C. E. C. Z. Multazam, A. Mustofa, W. Socha, Andrianto, S. Martini, L. Aminde, and C. Y. Li, "The 30 Years of Shifting in The Indonesian Cardiovascular Burden—Analysis of The Global Burden of Disease Study," *Journal of Epidemiology and Global Health*, vol. 14, pp. 193–212, 2024, doi: 10.1007/s44197-024-00187-8.
* **Klaim Kunci & Angka Terverifikasi**:
  1. **Kematian Akibat CVD Meningkat Lebih dari Dua Kali Lipat**: Kematian semua kelompok umur akibat penyakit kardiovaskular di Indonesia melonjak lebih dari dua kali lipat, dari 292.000 jiwa (95% UI: 246.000–339.000) pada tahun 1990 menjadi **659.000 jiwa (95% UI: 542.000–747.000) pada tahun 2019**.
  2. **Peringkat Global dan Regional Terburuk**: Indonesia tercatat sebagai **negara ke-6 di dunia dengan jumlah kematian penyakit kardiovaskular absolut tertinggi** (375.479 kematian kardiovaskular langsung dalam studi GBD 2019). Di kawasan Asia Tenggara (ASEAN), Indonesia memiliki **angka DALYs (*Disability-Adjusted Life Years*) terburuk kedua setelah Laos**.
  3. **Disparitas Beban Subnasional Antarprovinsi**: Laju DALYs penyakit kardiovaskular tertinggi terkonsentrasi di Provinsi Kepulauan Bangka Belitung, Kalimantan Selatan, dan D.I. Yogyakarta, dengan lonjakan beban tertinggi di Nusa Tenggara Barat (+24%), Kalimantan Selatan (+18%), dan Jawa Tengah (+11%).
* **Relevansi untuk Latar Belakang (Bab 1.1 P1)**:
  * Memberikan justifikasi statistik epidemiologis resmi dan terkini berskala nasional khusus untuk konteks Indonesia.
  * Menegaskan bahwa di balik beban kematian masif tersebut, dekompensasi gagal jantung pascarawat merupakan komponen biaya terbesar bagi BPJS Kesehatan.

---

### 1.2 Data Resmi Fragmentasi Sistem Informasi Puskesmas RI (Kemenkes DTO & UCL 2025)
* **Sumber Makalah**: `papers/FHIRSystem/md/P29 Health information system utilization in Indonesia.md`
* **Sitasi Ilmiah**: D. N. Aisyah, A. H. Setiawan, C. A. Mayadewi, A. F. Lokopessy, Z. Kozlakidis, and L. Manikam (Digital Transformation Office, Kementerian Kesehatan RI & University College London), "Understanding Health Information Systems Utilization Across Public Health Centers in Indonesia: Cross-Sectional Study," *JMIR Medical Informatics*, vol. 13, p. e68613, 2025, doi: 10.2196/68613.
* **Klaim Kunci & Angka Empiris**:
  1. **Jumlah Puskesmas Terverifikasi**: Terdapat **10.260 Pusat Kesehatan Masyarakat (Puskesmas)** di 34 provinsi yang beroperasi sebagai fasilitas pelayanan kesehatan primer utama di Indonesia.
  2. **Fragmentasi Ekstrem (Rata-rata 30 Aplikasi per Puskesmas)**: Satu Puskesmas di Indonesia rata-rata mengoperasikan **30 aplikasi Sistem Informasi Kesehatan (SIK/HIS) secara terpisah** (bahkan fasilitas perkotaan tertentu mengoperasikan lebih dari 30 sistem).
  3. **Beban Penginputan Ganda Tenaga Kesehatan**: Setiap tenaga medis rata-rata wajib menginput data ke **hingga 6 sistem informasi berbeda**. Sebanyak **49% sistem membutuhkan penginputan data berulang (*excessive redundant data entry*)**, dan **29% sistem sama sekali tidak memiliki fitur analisis data otomatis**.
  4. **Keterbatasan Infrastruktur Jaringan**: Hanya 28,9% Puskesmas yang memiliki koneksi internet stabil dan berkecepatan tinggi, sementara 9,45% belum terjangkau koneksi internet sama sekali, serta 33% sistem sering mengalami waktu henti (*downtime*).
* **Relevansi untuk Latar Belakang (Bab 1.1 P4 & P6)**:
  * Memberikan bukti empiris tak terbantahkan mengapa inovasi kesehatan baru tidak boleh menjadi aplikasi silo baru.
  * Menjustifikasi arsitektur berbasis standar FHIR yang langsung terhubung ke SATUSEHAT agar tidak membebani nakes dengan antarmuka yang terfragmentasi.

---

### 1.3 Hambatan Interoperabilitas dan *Vendor Lock-In* di RSUD Daerah (Savandha et al. 2026)
* **Sumber Makalah**: `papers/FHIRSystem/md/P22 FHIR Implementation barriers Indonesia.md`
* **Sitasi Ilmiah**: S. D. Savandha, E. Fitriyanti, and A. Azzahra, "Implementation Barriers of Electronic Health Record Interoperability in Indonesian District Hospitals: A Mixed-Methods Study," *Indonesian Health Journal*, vol. 5, no. 1, pp. 154–165, Jan. 2026.
* **Klaim Kunci**:
  1. Rumah sakit umum daerah (RSUD tipe C dan D) menghadapi kendala parah berupa keterikatan vendor (*vendor lock-in*), di mana basis data SIMRS bersifat tertutup (*proprietary*) dan tidak mematuhi standar pertukaran data terbuka.
  2. Ketiadaan lapisan perantara (*middleware*) interoperabel menyebabkan faskes daerah kesulitan menghubungkan data dari instrumen medis baru ke platform nasional SATUSEHAT.
* **Relevansi untuk Latar Belakang (Bab 1.1 P4 & P5)**:
  * Menunjukkan bahwa jurang terbesar digitalisasi faskes daerah adalah ketiadaan antarmuka standar antara perangkat medis diagnostik dan sistem RME rumah sakit.

---

### 1.4 Dampak Dokumentasi Manual pada Keselamatan Pasien dan Sekat Komunikasi (Kamil et al. 2020)
* **Sumber Makalah**: `papers/FHIRSystem/md/P28 Indonesia Doctor opinions on electronic systems.md`
* **Sitasi Ilmiah**: H. Kamil, Rachmah, Irvanizam, and E. Wardani, "Exploring Health Professionals’ Perceptions on Health-ID, an Electronic Integrated Patient Progress Documentation System: A Qualitative Study in Indonesia," *Journal of Multidisciplinary Healthcare*, vol. 13, pp. 1321–1331, 2020, doi: 10.2147/JMDH.S270740.
* **Klaim Kunci**:
  1. Dokumentasi berbasis kertas dan sistem elektronik yang tidak terintegrasi di rumah sakit Indonesia menciptakan sekat komunikasi antarprofesi (*interprofessional communication boundaries*), berkas pasien yang tidak lengkap (*incomplete patient charts*), serta keterlambatan verifikasi tindakan dokter.
  2. Implementasi sistem catatan perkembangan pasien terintegrasi digital mampu meniadakan isolasi informasi dan mempercepat konsensus terapeutik tim medis.
* **Relevansi untuk Latar Belakang (Bab 1.1 P6)**:
  * Memperkuat kebutuhan dokter akan dasbor terpadu yang memadukan riwayat medis pasien dengan hasil pembacaan perangkat secara instan.

---

## TEMA 2: PATOFISIOLOGI KONGESTI HEMODINAMIK & DILEMA PEMANTAUAN PASCARAWAT GAGAL JANTUNG

### 2.1 Fase Rentan (*Vulnerable Phase*) & Bahaya Kongesti Sisa Pascarawat (ESC-HFA Metra et al. 2023)
* **Sumber Makalah**: `papers/PatientHFManagement/md/P26 Pre and Post discharge of HF patietns.md`
* **Sitasi Ilmiah**: M. Metra, M. Adamo, D. Tomasoni, et al., "Pre-discharge and early post-discharge management of patients hospitalized for acute heart failure: A scientific statement by the Heart Failure Association of the ESC," *European Journal of Heart Failure*, vol. 25, no. 7, pp. 1115–1131, 2023, doi: 10.1002/ejhf.2888.
* **Klaim Kunci & Angka Klinis**:
  1. **Mortalitas Fase Rentan Melonjak 6 Kali Lipat**: Pasien gagal jantung akut yang dipulangkan dari rumah sakit mengalami lonjakan risiko kematian lebih dari **6 kali lipat dalam satu bulan pertama pascapemulangan** (*early post-discharge vulnerable phase*).
  2. **Tingginya Readmisi dan Mortalitas 1 Tahun**: Meskipun mortalitas selama perawatan di rumah sakit berkisar 4% hingga 10%, mortalitas 1 tahun pascarawat melonjak hingga **25%–30%**, dan lebih dari sepertiga (33%–50%) pasien kembali dirawat dalam 6 bulan pertama.
  3. **Tingginya Angka Kongesti Sisa (*Residual Congestion*)**: Registri ESC-EORP-HFA menunjukkan bahwa **30,9% pasien yang dipulangkan dari rumah sakit sebenarnya masih menyisakan tanda kongesti residual**.
  4. **Prediktor Readmisi**: Kongesti sisa ringan (*Congestion Score* 1–2) maupun berat (*CS* > 2) saat pemulangan berkaitan langsung dengan kenaikan risiko rawat inap ulang dan mortalitas. Faktor elektrokardiogram seperti **durasi QRS > 130 ms** terbukti menjadi faktor risiko independen kongesti residual.
* **Relevansi untuk Latar Belakang (Bab 1.1 P1 & P3)**:
  * Menjelaskan mengapa fase pascarawat merupakan jendela paling genting yang membutuhkan kewaspadaan tinggi.
  * Menghubungkan secara patofisiologis mengapa data hasil pengukuran JVP dan data ECG (seperti durasi QRS) wajib dikombinasikan dalam menilai kongesti.

---

### 2.2 Taksonomi 4 Fenotipe Kongesti: Mengapa JVP Mendahului Kenaikan Berat Badan? (Núñez et al. 2022)
* **Sumber Makalah**: `papers/SupportingData/md/P25 Biomarkers and HF.md`
* **Sitasi Ilmiah**: J. Núñez, R. de la Espriella, P. Rossignol, et al. (Biomarkers Working Group of the Heart Failure Association of the ESC), "Congestion in heart failure: a circulating biomarker-based perspective," *European Journal of Heart Failure*, vol. 24, no. 10, pp. 1751–1766, 2022, doi: 10.1002/ejhf.2664.
* **Klaim Kunci**:
  1. **Klasifikasi 4 Kompartemen Kongesti**: Kongesti pada gagal jantung tidak homogen, melainkan terbagi menjadi 4 fenotipe berdasarkan kompartemen anatominya:
     * *Pulmonary intravascular*: Peningkatan tekanan pengisian ventrikel kiri (PCWP).
     * *Pulmonary tissular / extravascular*: Edema interstisial paru (*B-lines* pada USG paru).
     * *Systemic intravascular*: Peningkatan tekanan vena sentral (CVP) dan tekanan vena jugularis (JVP).
     * *Systemic tissular / extravascular*: Edema perifer/ekstremitas, asites, dan kenaikan berat badan.
  2. **Hierarki Transmisi Cairan**: Kenaikan tekanan intravascular sistemik (JVP/CVP) adalah **peristiwa primer** yang mendahului perpindahan cairan transkapiler ke ruang interstisial (*tissular*). Kenaikan berat badan dan edema perifer baru timbul setelah terjadi akumulasi cairan interstisial dalam jumlah masif.
* **Relevansi untuk Latar Belakang (Bab 1.1 P1 & P2)**:
  * Memberikan landasan patofisiologi mutakhir: mengukur gelombang vena jugularis (JVP) adalah pengukuran langsung pada kompartemen *systemic intravascular*, sehingga mendeteksi bahaya sebelum cairan tumpah menjadi edema jaringan atau kenaikan berat badan.

---

### 2.3 Kegagalan Telemonitoring Berat Badan vs. Kinetika Hemodinamik (JACC Stevenson et al. 2023)
* **Sumber Makalah**: `papers/PatientHFManagement/md/P37 Remote Monitoring for HF management at home.md`
* **Sitasi Ilmiah**: L. W. Stevenson, H. J. Ross, L. D. Rathman, and J. P. Boehmer, "Remote Monitoring for Heart Failure Management at Home: JACC Scientific Statement," *Journal of the American College of Cardiology*, vol. 81, no. 23, pp. 2272–2291, 2023, doi: 10.1016/j.jacc.2023.04.010.
* **Klaim Kunci**:
  1. **Kegagalan Pemantauan Konvensional**: Berbagai uji klinis besar membuktikan bahwa telemonitoring berbasis pemantauan berat badan harian dan keluhan sesak napas mandiri pasien memberikan hasil *netral* (tidak mampu menurunkan angka rawat inap ulang).
  2. **Kinetika Hemodinamik ("Congestion Cascade")**: Kenaikan berat badan dan timbulnya sesak napas (*dyspnea*) merupakan **manifestasi klinis tahap akhir (*late-stage events*)** yang baru bermanifestasi secara tiba-tiba 24 sampai 48 jam sebelum pasien mengalami dekompensasi akut fatal.
  3. **Jendela Intervensi Dini Tekanan Pengisian**: Tekanan pengisian jantung (*cardiac filling pressures* / CVP / JVP) meningkat secara bertahap dan senyap **beberapa minggu sebelum timbul kenaikan berat badan atau gejala sesak**.
* **Relevansi untuk Latar Belakang (Bab 1.1 P1)**:
  * Menjadi pondasi konseptual pembuka paragraf P1: menjelaskan secara ilmiah mengapa mengukur denyut vena jugularis nirkontak jauh lebih unggul dan bermakna klinis daripada pemantauan timbangan berat badan konvensional.

---

### 2.4 Bukti Kuantitatif: Indeks Kongesti Multiparameter vs. Aturan Berat Badan (SCALE-HF 1 Trial 2025)
* **Sumber Makalah**: `papers/CDSSandMonitoring/md/P20 Noninvasive monitoring for HF .md`
* **Sitasi Ilmiah**: M. Fudim et al., "Surveillance and Alert-based Multiparameter Monitoring to Reduce Worsening Heart Failure Events: Results From SCALE-HF 1," *Journal of Cardiac Failure*, vol. 31, no. 4, pp. 661–675, Apr. 2025, doi: 10.1016/j.cardfail.2024.08.050.
* **Klaim Kunci & Angka Uji Klinis**:
  1. **Kegagalan Sensitivitas Aturan Berat Badan**: Aturan baku berat badan (*standard weight rule*: kenaikan >3 lb dalam 1 hari atau >5 lb dalam 7 hari) **hanya berhasil mendeteksi 35% (24 dari 69) kejadian perburukan gagal jantung**, dengan laju alarm palsu tinggi sebesar 4,18 peringatan per pasien-tahun.
  2. **Keunggulan Pendekatan Multiparameter**: Pemantauan indeks kongesti berbasis multiparameter noninvasif berhasil **mendeteksi 70% (48 dari 69) kejadian perburukan (p < 0,01)** serta menekan laju alarm palsu menjadi 2,58 peringatan per pasien-tahun.
* **Relevansi untuk Latar Belakang (Bab 1.1 P3)**:
  * Memberikan angka statistik pembanding yang tajam untuk membuktikan bahwa parameter tunggal selalu memiliki sensitivitas rendah (35%), dan penggabungan multiparameter (JVP + ECG + riwayat RME) secara signifikan melipatgandakan sensitivitas deteksi (70%).

---

### 2.5 Hubungan Hemodinamik JVP dengan Tekanan Atrium Kanan dan Sindrom Kardiorenal (Kenny et al. 2025)
* **Sumber Makalah**: `papers/RADAR/md/P6 JVP Doppler Ultrasound.md`
* **Sitasi Ilmiah**: J.-E. S. Kenny, P. Rola, R. Prager, and K. Haycock, "Jugular Venous Doppler Ultrasound as a Non-Invasive Window to Right Heart Hemodynamics: A Narrative Review and Future Perspective," *Therapeutic Advances in Pulmonary and Critical Care Medicine*, vol. 20, pp. 1–14, 2025, doi: 10.1177/29768675251359700.
* **Klaim Kunci**:
  1. Bentuk gelombang pulsasi vena jugularis interna (*jugular venous pulse*) berasal langsung dari gelombang tekanan atrium kanan ($P_{RA}$), yang identik dengan kurva tekanan vena sentral (CVP).
  2. Peningkatan CVP yang ditransmisikan ke vena jugularis merupakan **determinan hemodinamik utama yang paling berkaitan erat dengan perburukan fungsi ginjal (*worsening renal function*) dan sindrom kardiorenal** akibat hipertensi vena retrograd pada organ viseral.
  3. Lembah $x$ dan $y$ (*x and y descents*) serta puncak gelombang $a, c, v$ pada profil vena jugularis mencerminkan kepatuhan pengisian ventrikel kanan dan kompetensi katup trikuspid.
* **Relevansi untuk Latar Belakang (Bab 1.1 P1 & P2)**:
  * Menegaskan kembali rasionalitas fisiologis mengapa vena jugularis disebut sebagai "jendela noninvasif menuju hemodinamik jantung kanan".

---

### 2.6 Rekomendasi Pedoman ESC 2026 Mengenai Kongesti Vena Jugularis (Køber et al. 2026)
* **Sumber Makalah**: `papers/PatientHFManagement/md/P24 Guidance for HF Management.md`
* **Sitasi Ilmiah**: L. Køber, M. Adamo, et al., "2026 ESC Guidelines for the management of heart failure," *European Heart Journal*, vol. 47, no. 38, pp. 5346–5457, 2026, doi: 10.1093/eurheartj/ehag100.
* **Klaim Kunci**:
  1. Distensi vena jugularis (*elevated jugular venous pressure*) dan refluks hepatojugular diklasifikasikan sebagai tanda klinis fisik paling spesifik dalam mengevaluasi kongesti jantung kanan dan kelebihan volume intravascular.
  2. Pedoman ESC memberikan rekomendasi Kelas IIa bagi pemantauan hemodinamik terkelola untuk mengurangi risiko rawat inap ulang pasien gagal jantung.
* **Relevansi untuk Latar Belakang (Bab 1.1 P1)**:
  * Memperkuat legitimasi klinis topik tugas akhir dengan berpedoman pada konsensus kardiologi dunia terbaru (ESC Guidelines 2026).

---

## TEMA 3: MENGAPA PENGUKURAN JVP MEMERLUKAN KONTEKS RME? (MENJAWAB KRITIK "TERMOMETER")

### 3.1 Bukti Uji Klinis Acak JAMA: Efek Kontekstualisasi RME terhadap Luaran Klinis (Weiner et al. 2022)
* **Sumber Makalah**: `papers/FHIRSystem/md/P38 Effect of EHR for CDSS in at home care.md`
* **Sitasi Ilmiah**: S. J. Weiner, A. Schwartz, F. Weaver, et al., "Effect of Electronic Health Record Clinical Decision Support on Contextualization of Care: A Randomized Clinical Trial," *JAMA Network Open*, vol. 5, no. 10, p. e2238231, 2022, doi: 10.1001/jamanetworkopen.2022.38231.
* **Klaim Kunci & Angka Uji Klinis**:
  1. **Peningkatan Adaptasi Rencana Perawatan Pasien Sebesar 2,67 Kali Lipat**: Uji klinis acak membuktikan bahwa sistem pendukung keputusan klinis (CDSS) yang mengintegrasikan faktor kontekstual pasien di dalam RME meningkatkan penyesuaian rencana perawatan dokter hingga **2,67 kali lipat (adjusted OR 2,67; 95% CI 1,32–5,41)**.
  2. **Peningkatan Keberhasilan Luaran Masalah Klinis Sebesar 2,13 Kali Lipat**: Rencana terapi yang terkontekstualisasi (*contextualized care plans*) menghasilkan peluang keberhasilan resolusi masalah klinis pasien **2,13 kali lipat lebih tinggi (aOR 2,13; 95% CI 1,38–3,28)** dibandingkan keputusan tanpa konteks.
* **Relevansi untuk Latar Belakang (Bab 1.1 P3)**:
  * **Senjata utama menjawab kritik "termometer"**: Menunjukkan bukti ilmiah dari jurnal terkemuka (*JAMA*) bahwa instrumen pengukur medis baru (seperti RADAR) hanya akan memberi dampak klinis nyata apabila dihubungkan dengan data kontekstual riwayat penyakit dan terapi di RME!

---

### 3.2 Sistem Pendukung Keputusan Bersifat Bantuan (*Assistive CDS*) dan Alur Kerja Dokter (Susanto et al. 2023)
* **Sumber Makalah**: `papers/CDSSandMonitoring/md/P32 ML for CDSS review.md`
* **Sitasi Ilmiah**: A. P. Susanto (Pusat Jantung Nasional Harapan Kita & Fakultas Kedokteran UI), D. Lyell, B. Widyantoro, S. Berkovsky, and F. Magrabi, "Effects of machine learning-based clinical decision support systems on decision-making, care delivery, and patient outcomes: a scoping review," *Journal of the American Medical Informatics Association*, vol. 30, no. 12, pp. 2050–2063, 2023, doi: 10.1093/jamia/ocad180.
* **Klaim Kunci**:
  1. Mayoritas CDSS kardiovaskular yang sukses diadopsi dalam praktik klinis adalah sistem tingkat bantuan (*assistive CDSS*), di mana kecerdasan buatan menyajikan sintesis data dan indikasi risiko, namun kendali dan verifikasi keputusan diagnosis tetap berada penuh di tangan dokter.
  2. Faktor penentu kegagalan implementasi CDSS adalah keharusan dokter berpindah sistem atau membuka portal baru; CDSS harus menyatu secara tak kasatmata ke dalam infrastruktur TI dan alur kerja klinis faskes yang sudah berjalan.
* **Relevansi untuk Latar Belakang (Bab 1.1 P3 & Bab 1.3 Batasan Masalah)**:
  * Mengukuhkan batasan sistem: bahwa platform ini bukan sistem diagnosis otomatis, melainkan *assistive clinical decision support* yang menghormati otonomi klinisi.

---

### 3.3 Bahaya Sistem Monolitik Standalone & Kesenjangan Evaluasi Klinis CDSS (Hak et al. 2022; Papadopoulos et al. 2022)
* **Sumber Makalah**: `papers/CDSSandMonitoring/md/P34 Systematic review for CDS.md` & `papers/SupportingData/md/P35 Rule based CDSS review.md`
* **Sitasi Ilmiah**:
  * F. Hak, T. Guimarães, and M. Santos, "Towards effective clinical decision support systems: A systematic review," *PLOS ONE*, vol. 17, no. 8, p. e0272846, 2022.
  * P. Papadopoulos, M. Soflano, Y. Chaudy, W. Adejo, and T. M. Connolly, "A systematic review of technologies and standards used in the development of rule-based clinical decision support systems," *Health and Technology*, vol. 12, pp. 713–727, 2022.
* **Klaim Kunci**:
  1. **Dominasi Sistem Terisolasi (Standalone)**: Tinjauan sistematis menemukan bahwa **51,92% CDSS dibangun sebagai aplikasi yang berdiri sendiri (*standalone*)**, dan mayoritas gagal melampaui tingkat maturitas level 2 karena tidak mampu diintegrasikan ke alur kerja faskes.
  2. **Ketiadaan Standar dan Evaluasi Klinis**: Dari 1.731 makalah pengembangan CDSS berbasis aturan yang ditelaah, **hanya 15 makalah yang menyertakan evaluasi luaran klinis riil**. Dari 15 makalah tersebut, hanya 2 yang terintegrasi dengan RME dan hanya 3 yang menggunakan standar teknologi kesehatan resmi (seluruhnya HL7).
* **Relevansi untuk Latar Belakang (Bab 1.1 P3 & P6)**:
  * Menjadi justifikasi akademis yang sangat berbobot (*gap analysis*): penelitian ini mengisi kesenjangan besar di literatur dunia dengan merancang CDSS yang patuh standar terbuka (FHIR) dan terintegrasi langsung dengan ekosistem rekam medis.

---

### 3.4 Eliminasi *Alert Fatigue* melalui Integrasi Berbasis Standar (Isabelle et al. 2025)
* **Sumber Makalah**: `papers/FHIRSystem/md/P33 EHR, Interoperability and factors for CDSS.md`
* **Sitasi Ilmiah**: M. Isabelle, I. K. Ip, M. Bakhtin, L. Schneider, A. S. Raja, S. Dutta, A. Landman, and R. Lacson (Harvard Medical School & Brigham and Women's Hospital), "Assessment of 3 standards-based clinical decision support (CDS) tools in an academic electronic health record using Clinical Quality Language, CDS Hooks, and Fast Healthcare Interoperability Resources: a retrospective evaluation," *JAMIA Open*, vol. 8, no. 4, p. ooaf085, 2025.
* **Klaim Kunci**:
  1. Implementasi CDSS berbasis standar modern (kombinasi CQL, CDS Hooks, dan FHIR) berhasil mencapai **akurasi 96% hingga 100% dan tingkat alarm palsu (*false-positive alerts*) serendah 0,0%**.
  2. CDSS yang tidak terkontekstualisasi dengan parameter spesifik pasien memicu banjir notifikasi tidak bernilai klinis yang menyebabkan kelelahan peringatan (*alert fatigue*) dan kejenuhan tenaga medis (*physician burnout*).
* **Relevansi untuk Latar Belakang (Bab 1.1 P3 & P5)**:
  * Membuktikan bahwa penggabungan data terstandarisasi adalah solusi rekayasa untuk mencegah *alert fatigue* pada dokter.

---

## TEMA 4: LANDASAN FISIKA & KEUNGGULAN PENDERIAAN RADAR NIRKONTAK

### 4.1 Fisiologi Tekanan Rendah Vena Jugularis & Distorsi Mekanis Sensor Kontak (Suzuki et al. 2021; Das et al. 2024)
* **Sumber Makalah**: `papers/RADAR/md/P5 mmWave JVP RADAR.md` & `papers/RADAR/md/P4 RADAR JVP.md`
* **Sitasi Ilmiah**:
  * S. Suzuki et al., "Evaluation of Jugular Venous Pulse Waveforms Using Millimeter-Wave Radar," *Journal of Biomedical Science and Engineering*, vol. 14, pp. 109–120, 2021.
  * S. Das et al., "Characterization of internal jugular venous pulse waveforms using non-contact radar," *medRxiv preprint*, 2024.
* **Klaim Kunci**:
  1. **Sifat Fisik Sistem Tekanan Rendah**: Vena jugularis interna adalah pembuluh darah berdinding tipis dengan tekanan hidrostatik yang sangat rendah dalam kondisi normal (berkisar 5 hingga 8 cmH2O).
  2. **Distorsi Akibat Penekanan Probe Kontak**: Perekaman denyut leher menggunakan transduser mekanis kontak (*pulse-transducer*) atau probe ultrasonografi konvensional memberikan tekanan kontak langsung pada kulit leher. Penekanan fisik ini secara fisiologis menekan dinding pembuluh (*suppresses venous wall excursion*) dan merusak bentuk gelombang alami JVP yang halus.
  3. **Keunggulan Nirkontak Gelombang Mikro**: Sensor radar gelombang milimeter (24 GHz dan 60 GHz) merupakan instrumen murni nirkontak yang menangkap perpindahan mikrometer dinding pembuluh darah tanpa membebani kulit leher pasien, sehingga mempertahankan morfologi gelombang fisiologis asli.
* **Relevansi untuk Latar Belakang (Bab 1.1 P2)**:
  * Memberikan landasan biofisika yang sangat presisi mengapa metode nirkontak RADAR dipilih secara spesifik untuk mengukur denyut vena jugularis.

---

### 4.2 Hubungan Fisik Linear Antara Perpindahan Dinding Pembuluh RADAR dan Kecepatan Aliran USG (Shi et al. 2018)
* **Sumber Makalah**: `papers/RADAR/md/P7 mmWave Carotid Pulse.md`
* **Sitasi Ilmiah**: K. Shi, S. Schellenberger, T. Steigleder, F. Michler, F. Lurz, R. Weigel, and A. Koelpin, "Contactless Carotid Pulse Measurement Using Continuous Wave Radar," in *Proc. 2018 Asia-Pacific Microwave Conference (APMC)*, 2018, pp. 569–571.
* **Klaim Kunci**:
  1. **Tiga Jenis Gelombang Kardiovaskular**: Terdapat tiga jenis gelombang yang merambat dalam sistem vaskular: gelombang kecepatan aliran darah (*velocity waves*), gelombang tekanan (*pressure waves*), dan gelombang perpindahan dinding pembuluh (*wall displacement waves*).
  2. **Korelasi Linear Terbukti**: Sementara Doppler USG mengukur kecepatan aliran darah, radar mengukur perubahan diameter dan perpindahan dinding pembuluh. Penurunan teoritis dan eksperimen membuktikan adanya **hubungan linear langsung antara besaran perpindahan yang diukur radar dan profil ultrasonografi konvensional**.
  3. **Kemudahan Operasional**: Radar nirkontak portabel dapat dioperasikan secara andal tanpa memerlukan pelatihan khusus sonografer medis berkeahlian tinggi seperti halnya USG.
* **Relevansi untuk Latar Belakang (Bab 1.1 P2)**:
  * Membuktikan secara matematis dan fisis bahwa data hasil pengukuran perpindahan mikrometer RADAR valid secara fisiologis dan setara dengan instrumen referensi rumah sakit.

---

### 4.3 Penetrasi Tembus Pakaian & Validasi Hemodinamik Six-Port CW Radar 24 GHz (Schellenberger et al. 2020)
* **Sumber Makalah**: `papers/RADAR/md/P16 RADAR Dataset.md`
* **Sitasi Ilmiah**: S. Schellenberger, K. Shi, et al., "A dataset of clinically recorded radar vital signs with synchronised reference sensor signals," *Nature Scientific Data*, vol. 7, p. 291, 2020, doi: 10.1038/s41597-020-00629-5.
* **Klaim Kunci**:
  1. **Penetrasi Material Kain**: Frekuensi gelombang mikro 24 GHz memiliki sifat fisis yang mampu menembus pakaian tebal maupun kasur tanpa mengurangi resolusi deteksi gerakan kardiovaskular.
  2. **Validasi Hemodinamik 30 Subjek**: Basis data klinis 86.459 detik pada 30 subjek uji membuktikan stabilitas radar Continuous Wave berbasis teknologi Six-Port dalam merekam perubahan hemodinamik selama uji provokasi meja miring (*tilt table test*) yang disinkronkan langsung dengan ECG dan pemantau tekanan darah kontinu.
* **Relevansi untuk Latar Belakang (Bab 1.1 P2)**:
  * Memperkuat kenyamanan pasien: pengukuran dapat dilakukan tanpa melepas pakaian atau memasang gel perekat yang mengiritasi kulit lansia.

---

### 4.4 Evaluasi Kualitas Sinyal Berbasis AI untuk Pengukuran Pasien Geriatri (Yen et al. 2022)
* **Sumber Makalah**: `papers/RADAR/md/P13 RADAR Summary.md`
* **Sitasi Ilmiah**: H. T. Yen, M. Kurosawa, T. Kirimoto, Y. Hakozaki, T. Matsui, and G. Sun, "A medical radar system for non-contact vital sign monitoring and clinical performance evaluation in hospitalized older patients," *Biomedical Signal Processing and Control*, vol. 75, p. 103597, 2022, doi: 10.1016/j.bspc.2022.103597.
* **Klaim Kunci**:
  1. **Akurasi Pengukuran Geriatri**: Penerapan modul evaluasi kualitas sinyal otomatis berbasis Support Vector Machine (SVM) pada radar 24 GHz mencapai akurasi **93,2% hingga 100%**.
  2. **Deviasi Sangat Rendah terhadap Baku Emas**: Ekstraksi frekuensi detak jantung dari radar pada pasien rawat inap geriatri hanya menunjukkan deviasi **0 hingga 4 detak per menit (bpm)** dibandingkan alat perekam ECG kontak.
* **Relevansi untuk Latar Belakang (Bab 1.1 P2)**:
  * Menunjukkan bahwa teknologi radar medis telah diuji pada populasi pasien rentan dan memiliki deviasi yang sangat dapat diterima untuk mendukung keputusan klinis.

---

### 4.5 Koreksi Frekuensi Cerdas Bi-LSTM pada Radar Nirkontak Kompak (Kim et al. IEEE CCNC 2026)
* **Sumber Makalah**: `papers/RADAR/md/P19 ISAC and RADAR.md`
* **Sitasi Ilmiah**: W.-J. Kim, E. Jang, J.-W. Park, M. Cho, S.-J. Park, and J.-W. Kim, "AI-Enhanced CW Radar for Vital Sign Monitoring in ISAC Applications," in *Proc. 2026 IEEE 23rd Consumer Communications & Networking Conference (CCNC)*, 2026, doi: 10.1109/CCNC59702.2026.10636631.
* **Klaim Kunci**:
  1. Instabilitas frekuensi yang jamak dialami perangkat radar gelombang kontinu kompak berbiaya terjangkau dapat diatasi secara cerdas menggunakan algoritma koreksi berbasis jaringan saraf tiruan Bi-LSTM.
  2. Pendekatan AI ini menghasilkan **tingkat akurasi deteksi sinyal kardiorespirasi di atas 97%**, membuktikan kelayakan komersial perangkat keras radar berbiaya rendah untuk penggunaan klinis dan komunitas.
* **Relevansi untuk Latar Belakang (Bab 1.1 P2)**:
  * Mendukung argumen bahwa teknologi penderiaan radar telah matang untuk diimplementasikan secara terjangkau di fasilitas layanan kesehatan Indonesia.

---

## TEMA 5: ARSITEKTUR INTEROPERABILITAS STANDAR FHIR, PGHD, & EKOSISTEM DIGITAL NASIONAL

### 5.1 Penyelesaian Masalah Historis "Curly Braces" Melalui FHIR R4 (Strasberg et al. 2021)
* **Sumber Makalah**: `papers/CDSSandMonitoring/md/P30 CDSS with FHIR.md`
* **Sitasi Ilmiah**: H. R. Strasberg, B. Rhodes, G. Del Fiol, R. A. Jenders, P. J. Haug, and K. Kawamoto, "Contemporary clinical decision support standards using Health Level Seven International Fast Healthcare Interoperability Resources," *Journal of the American Medical Informatics Association*, vol. 28, no. 8, pp. 1796–1806, 2021, doi: 10.1093/jamia/ocab070.
* **Klaim Kunci**:
  1. **Masalah Warisan "Curly Braces"**: Selama tiga dekade, penerapan CDSS terhambat oleh masalah *curly braces*, di mana pemanggilan basis data lokal rumah sakit ditulis dalam format tertutup (seperti `{patient.lab_result}` pada Arden Syntax), sehingga modul keputusan klinis tidak dapat dipindahkan (*non-portable*) ke rumah sakit lain.
  2. **FHIR R4 sebagai Pemecah Kebuntuan**: Standar HL7 FHIR Release 4 menyediakan model data klinis kanonikal yang universal. Dikombinasikan dengan *Clinical Quality Language* (CQL), aturan pendukung keputusan dapat dipisahkan secara tegas dari perangkat lunak EHR, memungkinkan logika klinis dieksekusi lintas institusi tanpa penulisan ulang kode basis data.
* **Relevansi untuk Latar Belakang (Bab 1.1 P5)**:
  * Memberikan kedalaman pemahaman informatika medis: adopsi FHIR bukan sekadar tren teknologi, melainkan keharusan untuk memecahkan kebuntuan portabilitas sistem CDSS antar-rumah sakit.

---

### 5.2 Pemetaan Sinyal Fisiologis ECG 12-Sadapan ke FHIR R4 SATUSEHAT (Chaidir & Hareva 2025)
* **Sumber Makalah**: `papers/FHIRSystem/md/P14 SSP Implementation Guide.md`
* **Sitasi Ilmiah**: T. A. N. Chaidir and D. H. Hareva, "A SatuSehat Compliant FHIR R4 ECG Implementation Guide: Bridging Clinical and Informatics Domains in Indonesia," *International Journal of Informatics, Information System and Computer Engineering*, vol. 6, no. 2, pp. 315–330, 2025.
* **Klaim Kunci**:
  1. **Krisis Sumber Daya Informatika Medis di Indonesia**: Kurang dari 1% perguruan tinggi di Indonesia yang memiliki kurikulum informatika medis terakreditasi, menghasilkan jurang pemahaman yang besar antara praktisi klinis dan pengembang perangkat lunak kesehatan.
  2. **Spesifikasi Pertukaran Data ECG**: Pemetaan standar HL7 aECG ke FHIR R4 membuktikan bahwa **17 atribut kunci** mampu merepresentasikan seluruh sinyal elektrokardiogram 12-sadapan secara utuh ke dalam *resource* `Observation` (menggunakan elemen `valueSampledData`) dan `DiagnosticReport`.
  3. **Penanganan Ketiadaan Terminologi**: Keterbatasan terminologi SNOMED CT lokal di Indonesia (yang awalnya hanya mencakup 13 dari 32 jenis sadapan) diselesaikan melalui pembuatan *provisional ValueSets* yang patuh arsitektur SATUSEHAT.
* **Relevansi untuk Latar Belakang (Bab 1.1 P3 & P5)**:
  * Menjadi pedoman teknis mutakhir yang membuktikan bahwa enkapsulasi deret waktu kardiovaskular ke dalam FHIR telah siap diterapkan secara spesifik pada ekosistem SATUSEHAT Indonesia.

---

### 5.3 Standarisasi Perangkat Medis Point-of-Care ISO/IEEE 11073 ke FHIR (Riech et al. 2021)
* **Sumber Makalah**: `papers/FHIRSystem/md/P18 ISO to FHIR.md`
* **Sitasi Ilmiah**: K. P. Riech, H. Ulrich, J. Ingenerf, and B. Andersen, "Mapping of medical device data from ISO/IEEE 11073-10207 to HL7 FHIR," *GMS Medizinische Informatik, Biometrie und Epidemiologie*, vol. 17, no. 2, p. Doc08, 2021, doi: 10.3205/mibe000220.
* **Klaim Kunci**:
  1. Menjembatani jurang komunikasi struktural antara perangkat keras medis (*point-of-care medical devices*) yang berbasis standar ISO/IEEE 11073 SDC dan sistem perangkat lunak rumah sakit berbasis HL7 FHIR.
  2. Mempertahankan konteks metrik pengukuran instrumen medis secara utuh menggunakan pemetaan ke profil resource FHIR `DeviceMetric` dan `Observation`.
* **Relevansi untuk Latar Belakang (Bab 1.1 P5)**:
  * Memberikan landasan arsitektural bagaimana data dari mikrokontroler sensor diubah menjadi objek interoperabel tanpa kehilangan metadata instrumen.

---

### 5.4 Transmisi Real-Time Data Sensor Biomedis ke FHIR Tanpa Paket Hilang (Adochiei et al. 2024)
* **Sumber Makalah**: `papers/FHIRSystem/md/P9 IoT FHIR Implementation.md`
* **Sitasi Ilmiah**: F.-C. Adochiei et al., "HL7 FHIR-Based Open-Source Framework for Real-Time Biomedical Signal Acquisition and IoMT Interoperability," *Sensors*, vol. 24, no. 4, p. 1211, 2024.
* **Klaim Kunci**:
  1. Arsitektur ujung-ke-ujung (*end-to-end*) yang memetakan sinyal fisiologis mentah dari node sensor IoMT nirkabel ke *FHIR Observations* berhasil mencapai **latensi transmisi sub-detik (<1 detik)**.
  2. Framework membuktikan keandalan transmisi dengan **tingkat kehilangan data nol (*0% packet loss*)** dan pelestarian semantik data secara menyeluruh sepanjang alur komunikasi.
* **Relevansi untuk Latar Belakang (Bab 1.1 P5)**:
  * Membuktikan secara empiris bahwa protokol FHIR sangat bertenaga dan siap melayani aliran data biomedis seketika (*real-time*).

---

### 5.5 Integrasi Data Pasien Mandiri (PGHD) Lintas 18 Klinik via SMART on FHIR (Wesley et al. 2021)
* **Sumber Makalah**: `papers/FHIRSystem/md/P8 FHIR Integration.md`
* **Sitasi Ilmiah**: D. B. Wesley et al., "A novel application of SMART on FHIR architecture for interoperable and scalable integration of patient-reported outcome data with electronic health records," *JAMIA*, vol. 28, no. 10, pp. 2220–2225, 2021, doi: 10.1093/jamia/ocab110.
* **Klaim Kunci**:
  1. Arsitektur SMART on FHIR terbukti berhasil mengintegrasikan data kesehatan mandiri yang dihimpun pasien (*patient-generated health data / PGHD*) ke dalam **3 platform vendor EHR yang berbeda di 18 fasilitas layanan kesehatan rawat jalan**.
  2. Pendekatan berbasis standar terbuka memungkinkan klinisi meninjau riwayat data pasien langsung di jendela RME mereka saat sesi konsultasi tanpa perlu berganti perangkat lunak.
* **Relevansi untuk Latar Belakang (Bab 1.1 P4 & P5)**:
  * Menjadi model percontohan bahwa integrasi data mandiri pasien ke RME rumah sakit telah tervalidasi secara luas dalam skala faskes nyata.

---

### 5.6 Peningkatan Utilisasi Aplikasi Klinis sebesar 130% melalui CDS Hooks (Morgan et al. 2022)
* **Sumber Makalah**: `papers/CDSSandMonitoring/md/P31 CDSS with FHIR and SMART.md`
* **Sitasi Ilmiah**: K. L. Morgan et al., "Using CDS Hooks to increase SMART on FHIR app utilization: a cluster-randomized trial," *JAMIA*, vol. 29, no. 9, pp. 1461–1470, 2022.
* **Klaim Kunci**:
  1. Uji klinis acak klaster pada 70 dokter membuktikan bahwa penyampaian peringatan dan kartu rekomendasi menggunakan standar *CDS Hooks* memicu peningkatan pemanfaatan aplikasi rujukan klinis hingga **130% (OR 2,45; p = 0,02)**.
  2. Integrasi yang terpaut langsung pada titik temu alur kerja (*trigger events*, seperti saat membuka rekam medis pasien) menghilangkan hambatan friksi operasional yang selama ini membuat CDSS diabaikan oleh dokter.
* **Relevansi untuk Latar Belakang (Bab 1.1 P5 & P6)**:
  * Menjawab bagaimana sistem pendukung keputusan yang dibangun akan berinteraksi dengan klinisi di rumah sakit secara praktis.

---

### 5.7 Landasan Regulasi Nasional: UU 17/2023, Permenkes 24/2022, & Kepmenkes 1423/2022
* **Sumber Makalah / Peraturan**:
  * `papers/Regulations/md/UU Nomor 17 Tahun 2023.md`
  * `papers/Regulations/md/UU PERMENKES 24 2024 TENTANG RME.md` (Permenkes 24/2022)
  * `papers/Regulations/md/2022kepmenkes1423.md` (Kepmenkes HK.01.07/MENKES/1423/2022)
* **Klaim Kunci & Pasal Krusial**:
  1. **UU Nomor 17 Tahun 2023 tentang Kesehatan**:
     * **Pasal 296**: Setiap tenaga medis dan tenaga kesehatan wajib menyelenggarakan rekam medis secara lengkap dan bertanggung jawab atas integritas datanya.
     * **Pasal 297 Ayat (2)**: Menegaskan hak hukum pasien: *"Setiap Pasien berhak untuk mengakses informasi yang terdapat dalam dokumen rekam medis"*. Ketentuan ini melegalkan hak pasien untuk memiliki, melihat, dan membagikan data kesehatannya secara digital.
     * **Ketentuan Sistem Informasi**: Seluruh SIMRS diwajibkan terhubung ke Sistem Informasi Kesehatan Nasional.
  2. **Permenkes Nomor 24 Tahun 2022 tentang Rekam Medis**:
     * Mewajibkan seluruh fasilitas pelayanan kesehatan di Indonesia menyelenggarakan Rekam Medis Elektronik (RME) dan berinteroperabilitas dengan platform nasional SATUSEHAT Kemenkes RI yang mengadopsi standar HL7 FHIR.
     * **Pasal 26**: Mengatur pembagian dan akses data rekam medis elektronik oleh pasien demi kesinambungan pelayanan antarfaskes.
  3. **Kepmenkes Nomor HK.01.07/MENKES/1423/2022 tentang Pedoman Variabel dan Meta Data pada Penyelenggaraan RME**:
     * Menetapkan variabel klinis standar, meta data, dan format pengodean terminologi yang wajib dipenuhi sistem elektronik faskes agar kompatibel dan interoperabel secara nasional.
* **Relevansi untuk Latar Belakang (Bab 1.1 P4)**:
  * Memberikan kekuatan hukum dan justifikasi mandat negara yang sangat kokoh bahwa pengembangan sistem RME berbasis FHIR dan portal data pasien bukan sekadar pilihan teknis, melainkan kewajiban hukum positif di Republik Indonesia.

---

## MATRIKS INTEGRASI: PANDUAN PENYISIPAN KLAIM KE PARAGRAF LATAR BELAKANG (P1–P6)

Tabel berikut memetakan seluruh klaim literatur di atas secara sistematis ke dalam alur narasi 6 paragraf Latar Belakang (Bab 1.1):

| Paragraf Bab 1.1 | Fokus Tematik Paragraf | Klaim & Data Kunci yang Dapat Disisipkan | Sumber Sitasi Utama |
|---|---|---|---|
| **Paragraf 1 (P1)** | Urgensi penyakit kardiovaskular, risiko readmisi gagal jantung pascarawat, dan batasan pengukuran invasif CVP | * **Beban Nasional Indonesia**: Kematian CVD melonjak dari 292.000 (1990) menjadi 659.000 jiwa (2019); DALYs Indonesia terburuk kedua di ASEAN; peringkat 6 kematian CVD dunia.<br>* **Fase Rentan Pascarawat**: Mortalitas melonjak >6 kali lipat pada 30 hari pascapemulangan; 30,9% pasien pulang dengan kongesti sisa.<br>* **Kegagalan Pemantauan Berat Badan**: Berat badan dan sesak napas muncul terlambat (24–48 jam sebelum opname), sedangkan tekanan pengisian jantung (JVP/CVP) naik berminggu-minggu sebelumnya.<br>* **Empat Fenotipe Kongesti**: JVP mendeteksi kongesti *systemic intravascular* sebelum cairan tumpah menjadi edema jaringan (*tissular*). | * Muharram et al. (*J. Epidemiol. Glob. Health* 2024)<br>* Metra et al. (*EJHF* 2023)<br>* Stevenson et al. (*JACC* 2023)<br>* Núñez et al. (*EJHF* 2022)<br>* Kenny et al. (*TAPCCM* 2025)<br>* Køber et al. (ESC Guidelines 2026) |
| **Paragraf 2 (P2)** | Penderiaan RADAR sebagai modalitas nirkontak pengukur denyut vena jugularis | * **Fisiologi Sistem Tekanan Rendah**: Vena jugularis memiliki tekanan sangat rendah (5–8 cmH2O); sensor mekanis kontak menekan leher dan merusak gelombang.<br>* **Korelasi Linear Terbukti**: Pengukuran perpindahan dinding pembuluh oleh RADAR berkorelasi linear dengan kecepatan aliran USG Doppler.<br>* **Penetrasi Pakaian & Evaluasi AI**: Gelombang mikro 24 GHz menembus pakaian tebal; modul SVM mencapai akurasi kualitas 93,2%–100% pada geriatri dengan deviasi hanya 0–4 bpm dari baku emas ECG kontak.<br>* **Koreksi AI Bi-LSTM**: Radar kompak CW mencapai akurasi sinyal >97%. | * Suzuki et al. (2021)<br>* Das et al. (2024)<br>* Shi et al. (*IEEE APMC* 2018)<br>* Schellenberger et al. (*Nat. Sci. Data* 2020)<br>* Yen et al. (*BSPC* 2022)<br>* Kim et al. (*IEEE CCNC* 2026) |
| **Paragraf 3 (P3)** | Pengambilan keputusan klinis memerlukan konteks riwayat pasien RME (Menjawab kritik "termometer") | * **Bukti Uji Klinis JAMA**: Menghubungkan faktor kontekstual RME meningkatkan adaptasi perawatan dokter hingga 2,67 kali lipat dan meningkatkan perbaikan klinis 2,13 kali lipat.<br>* **Sensitivitas Multiparameter**: Pemantauan gabungan multiparameter mendeteksi 70% perburukan HF (jauh melampaui aturan berat badan yang hanya 35%).<br>* **Filosofi Assistive CDS**: Sistem dirancang untuk membantu (*assistive*) dan menyatu dalam alur kerja dokter tanpa mengurangi otonomi klinisi.<br>* **Integrasi Sinyal ECG 12-Sadapan**: Durasi QRS > 130 ms berkaitan erat dengan kongesti sisa; 17 atribut ECG berhasil dipetakan ke FHIR SATUSEHAT. | * Weiner et al. (*JAMA Netw Open* 2022)<br>* Fudim et al. (*JCF* 2025)<br>* Susanto et al. (*JAMIA* 2023)<br>* Metra et al. (2023)<br>* Chaidir & Hareva (*INJIISCOM* 2025)<br>* Isabelle et al. (*JAMIA Open* 2025) |
| **Paragraf 4 (P4)** | Ekosistem RME, data pasien mandiri (PGHD), dan mandat regulasi Indonesia | * **Potret Riil Faskes Indonesia**: Indonesia memiliki 10.260 Puskesmas yang rata-rata mengoperasikan 30 sistem informasi kesehatan berbeda secara terfragmentasi.<br>* **Beban Penginputan Ganda**: 49% sistem membutuhkan penginputan data berulang; 1 tenaga medis mengelola hingga 6 sistem; hambatan *vendor lock-in* di RSUD daerah.<br>* **Landasan Regulasi Kuat**: UU Kesehatan 17/2023 (Pasal 296–297 menegaskan hak akses data pasien); Permenkes 24/2022 (mandat interoperabilitas SATUSEHAT); Kepmenkes 1423/2022 (standar variabel dan meta data RME).<br>* **Skalabilitas SMART on FHIR**: Sukses mengalirkan data mandiri pasien ke 3 vendor RME di 18 klinik. | * Aisyah et al. (*JMIR Med Inform* 2025, Kemenkes DTO)<br>* Savandha et al. (*IHJ* 2026)<br>* UU 17/2023<br>* Permenkes 24/2022<br>* Kepmenkes 1423/2022<br>* Wesley et al. (*JAMIA* 2021) |
| **Paragraf 5 (P5)** | Standar FHIR sebagai solusi interoperabilitas data perangkat dan RME | * **Pemecahan Masalah "Curly Braces"**: FHIR R4 dan CQL memisahkan logika keputusan dari sistem vendor, memungkinkan portabilitas CDSS antar-rumah sakit.<br>* **Standarisasi Perangkat Medis (ISO/IEEE 11073)**: Pemetaan data instrumen biomedis ke FHIR DeviceMetric dan Observation.<br>* **Keandalan Real-Time**: Aliran data sensor ke FHIR membuktikan latensi <1 detik dengan 0% data hilang (*zero packet loss*).<br>* **Pemicu Alur Kerja CDS Hooks**: Peringatan kontekstual dalam alur kerja RME meningkatkan utilisasi aplikasi medis hingga 130%. | * Strasberg et al. (*JAMIA* 2021)<br>* Riech et al. (*MIBE* 2021)<br>* Adochiei et al. (*Sensors* 2024)<br>* Morgan et al. (*JAMIA* 2022)<br>* Isabelle et al. (*JAMIA Open* 2025) |
| **Paragraf 6 (P6)** | Kesenjangan solusi (*gap analysis*) dan urgensi platform terintegrasi | * **Sekat Dokumentasi di RS Indonesia**: Sistem pencatatan silo menyebabkan keterlambatan verifikasi, data hilang, dan isolasi antarprofesi kesehatan.<br>* **Dominasi Prototipe Standalone**: 51,9% CDSS di literatur bersifat mandiri tanpa integrasi RME, dan dari 1.731 makalah hanya 2 yang terhubung ke RME berbasis standar terbuka.<br>* **Sintesis Kesenjangan Solusi**: Ketiadaan platform yang menjembatani data hasil pengukuran instrumen RADAR JVP ke RME dokter sekaligus memberikan akses kendali data kepada pasien pascarawat. | * Kamil et al. (*JMDH* 2020)<br>* Hak et al. (*PLOS ONE* 2022)<br>* Papadopoulos et al. (*Health Technol* 2022)<br>* Tapuria et al. (*IHSC* 2021)<br>* Purnama et al. (*Sensors* 2026) |

---

## CONTOH PANDUAN MENJAWAB PERTANYAAN KRITIS SIDANG PROPOSAL

Berikut adalah contoh skenario argumentasi berbasis bukti literatur yang dapat digunakan mahasiswa saat menghadapi pertanyaan penguji:

### Skenario 1: Pertanyaan Penguji tentang Pemilihan RADAR vs. Alat Lain
> **Pertanyaan Dosen**: *"Mengapa Anda repot-repot menggunakan RADAR nirkontak untuk mengukur JVP? Mengapa tidak menggunakan sensor denyut piezoelektrik kontak atau probe USG biasa yang murah dan sudah ada?"*
>
> **Jawaban Mahasiswa Berdasarkan Literatur**:
> *"Secara fisiologis, vena jugularis interna adalah pembuluh darah berdinding tipis dengan tekanan hidrostatik yang sangat rendah, normalnya hanya 5 sampai 8 cmH2O (Suzuki et al., 2021; Das et al., 2024). Apabila kita menggunakan sensor kontak seperti piezoelektrik atau probe USG, tekanan fisik alat pada permukaan leher akan menekan dan mendistorsi dinamika denyut vena yang halus tersebut. Sebaliknya, RADAR 24 GHz bekerja secara murni nirkontak tanpa beban mekanis sama sekali, dan penurunan teoritis serta eksperimen membuktikan perpindahan dinding pembuluh yang direkam RADAR berkorelasi linear dengan profil USG Doppler (Shi et al., 2018; Schellenberger et al., 2020), sehingga keaslian bentuk gelombang vena terjaga."*

---

### Skenario 2: Pertanyaan Penguji Mengapa Tidak Memantau Berat Badan Pasien Saja
> **Pertanyaan Dosen**: *"Bukannya pemantauan pasien gagal jantung di rumah cukup dengan menimbang berat badan setiap pagi dan memantau keluhan sesak napas?"*
>
> **Jawaban Mahasiswa Berdasarkan Literatur**:
> *"Berdasarkan pernyataan ilmiah JACC (Stevenson et al., 2023) dan hasil uji klinis SCALE-HF 1 (Fudim et al., 2025), aturan baku kenaikan berat badan konvensional terbukti gagal karena hanya memiliki sensitivitas 35% dalam mendeteksi kejadian dekompensasi akut, disertai laju alarm palsu yang tinggi. Secara patofisiologi (Núñez et al., 2022), kenaikan berat badan dan sesak napas merupakan kejadian tahap akhir (late-stage events) yang baru bermanifestasi 24 sampai 48 jam sebelum pasien masuk IGD. Sebaliknya, tekanan pengisian vena (JVP) sudah meningkat secara senyap beberapa minggu sebelumnya. Dengan mengukur gelombang JVP, dokter mendapatkan jendela waktu intervensi dini yang jauh lebih panjang untuk menyesuaikan terapi sebelum pasien mengalami dekompensasi fatal."*

---

### Skenario 3: Pertanyaan "Kritik Termometer" (Mengapa Butuh RME & CDSS)
> **Pertanyaan Dosen**: *"Kalau alat RADAR Anda sudah bisa mengukur JVP, mengapa harus repot menghubungkannya ke RME rumah sakit dan membuat CDSS? Bukankah cukup ditampilkan saja angkanya di layar alat seperti termometer digital?"*
>
> **Jawaban Mahasiswa Berdasarkan Literatur**:
> *"Angka JVP yang berdiri sendiri tidak memiliki nilai klinis yang optimal tanpa konteks riwayat medis pasien. Berdasarkan uji klinis acak berskala besar yang dipublikasikan di JAMA (Weiner et al., 2022), penyertaan data kontekstual pasien dalam sistem pendukung keputusan terbukti meningkatkan penyesuaian rencana terapi dokter sebesar 2,67 kali lipat dan meningkatkan resolusi masalah klinis pasien sebesar 2,13 kali lipat. Selain itu, tinjauan sistematis terhadap 1.731 makalah CDSS (Papadopoulos et al., 2022) menemukan bahwa mayoritas kegagalan CDSS di dunia disebabkan karena sistem dibangun secara terisolasi (standalone) tanpa integrasi RME. Dengan menghubungkan data pengukuran ke RME berbasis FHIR, dokter memperoleh sintesis riwayat terapi diuretik, fungsi ginjal, dan durasi QRS ECG secara simultan dalam alur kerjanya."*

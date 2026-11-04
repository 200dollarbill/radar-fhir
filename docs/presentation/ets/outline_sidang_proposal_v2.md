# Outline Presentasi Sidang Proposal, Versi 2 (mengikuti struktur proposal)

Judul kerja (belum final): Pengembangan Sistem Pendukung Keputusan Klinis Berbasis Interoperabilitas Data Rekam Medis Elektronik dan Pengukuran Kardiovaskular RADAR

Prinsip versi ini: urutan slide mengikuti urutan proposal (Bab I, Bab II, lalu awal Bab III), supaya penguji yang membuka proposal bisa mengikuti. Posisi presentasi: Bab I dan II sudah ada, Bab III baru mulai. Semua isi tentang sistem adalah RENCANA, belum ada hasil.

Kode status klaim:
* [P] ada di proposal.md, aman dipakai
* [C] hanya ada di catatan pendukung, belum masuk proposal. Pakai sebagai tambahan lisan dan sebut sumbernya
* [!] belum terverifikasi. Hindari atau ucapkan dengan hati hati

Semua angka berasal dari catatan ringkasan, belum dicocokkan dengan makalah asli.

---

## Peta slide ke proposal

* Slide 1: Bab 1.1 paragraf 1, Bab 2.1
* Slide 2: Bab 1.1 paragraf 2, Bab 2.2
* Slide 3: Bab 1.1 paragraf 3, Bab 2.1 dan 2.7 (jawaban untuk kritik termometer)
* Slide 4: Bab 1.1 paragraf 4 dan 5, Bab 2.3 dan 2.4
* Slide 5: Bab 1.2 sampai 1.5 (rumusan, batasan, tujuan dan manfaat, kontribusi)
* Slide 6: Bab 2.5 (CDSS dan manajemen data, arsitektur aliran data)
* Slide 7: Bab 2.6 (kesenjangan) dan 2.7 (rasional)
* Slide 8: Bab III (rencana implementasi) dan penutup

## Alokasi waktu (total 5:00)

* Slide 1: 0:30
* Slide 2: 0:35
* Slide 3: 0:35
* Slide 4: 0:40
* Slide 5: 0:45
* Slide 6: 0:40
* Slide 7: 0:30
* Slide 8: 1:05

Bila waktu mepet: ringkas slide 1 dan 2 menjadi satu kalimat pembuka tiap slide, dan sisihkan waktu untuk slide 5 dan 8 karena itu inti proposal dan rencana kerja.

---

## Slide 1. Latar belakang: gagal jantung kembali ke rumah sakit karena kongesti yang terlambat terlihat
(Bab 1.1 paragraf 1, Bab 2.1)

Isi slide:
* 19,8 juta kematian penyakit kardiovaskular pada 2022, sekitar 32% kematian global [1] [P]
* Indonesia: sekitar 292 ribu (1990) menjadi sekitar 659 ribu (2019) [2] [P]
* Gagal jantung: rawat ulang 10,9% dalam 30 hari dan 27% dalam 6 bulan [3] [P]
* Pemicu: kongesti sisa, sekitar 30,9% pasien pulang masih menunjukkan kongesti [4] [P]
* Kongesti vena dilihat dari CVP, yang butuh kateter [5][6] [P]
* JVP sebagai alternatif noninvasif yang mewakili tekanan atrium kanan [7] [P]

Poin bicara:
* Beban penyakit besar, gagal jantung adalah tempat beban itu berulang.
* Kongesti sisa saat pulang adalah pemicu yang bisa dicegah, tapi CVP invasif dan JVP di sisi tempat tidur bergantung pemeriksa.

---

## Slide 2. Latar belakang: JVP dan pengukuran RADAR nirkontak
(Bab 1.1 paragraf 2, Bab 2.2)

Isi slide:
* Gelombang JVP berasal dari tekanan atrium kanan: puncak a, c, v dan lembah x, y [7] [P]
* Prinsip RADAR: efek Doppler dan backscatter, membaca perbedaan fase pantulan dari gerakan mikro pembuluh [9] [P]
* Bukti dasar: radar 24 GHz direkam serempak dengan ECG, sekitar 24 jam dari 30 subjek sehat [9] [P]
* Bukti JVP: 24 GHz pada 8 sukarelawan [10], FMCW 60 GHz dengan eigen beamforming [6] [P]
* Tantangan klinis: radar rentan artefak gerakan, mutu sinyal perlu dinilai [11] [P]
* Status: studi kelayakan awal, sampel kecil [P]

Poin bicara:
* RADAR tidak mengukur CVP. RADAR menangkap denyut vena jugularis sebagai indikator tekanan atrium kanan.
* Katakan jujur: bukti masih awal. Itu alasan data harus dibaca bersama konteks.

---

## Slide 3. Latar belakang: satu pengukuran JVP tidak cukup (jawaban kritik termometer)
(Bab 1.1 paragraf 3, Bab 2.1 dan 2.7)

Isi slide:
* JVP bukan satu angka tekanan, melainkan gelombang yang hanya terbaca bila waktunya dirujuk ke siklus jantung [7] [P]
* Variasi antarpasien datang dari obat, berat badan, hasil laboratorium, kunjungan sebelumnya, riwayat penyakit [P]
* Bukti klinis JVP saling bertentangan, jadi JVP tidak layak jadi indikator tunggal [P]
* Data tunggal lemah: aturan berat badan 35% berbanding indeks multiparameter 70% (SCALE HF 1, 329 pasien, 8 pusat) [14] [P]
* Konteks mengubah penanganan: CDSS dengan informasi tambahan pasien, adjusted OR 2,67 untuk penyesuaian rencana [15] [P]

Poin bicara:
* Termometer memberi satu angka dengan makna universal. JVP tidak begitu.
* Karena itu tampilan yang dibutuhkan dokter memadukan gelombang, ECG, dan konteks RME.

---

## Slide 4. Latar belakang: konteks ada di RME, tetapi terfragmentasi, dan FHIR sebagai jembatan
(Bab 1.1 paragraf 4 dan 5, Bab 2.3 dan 2.4)

Isi slide, kolom kiri (RME dan regulasi):
* Permenkes 24/2022 mewajibkan RME [16]; Kepmenkes 1423/2022 mengatur variabel RME [21]; UU 17/2023 mengharuskan teknologi dan sistem informasi kesehatan mengikuti standar interoperabilitas [22] [P]
* 10.260 Puskesmas, sekitar 30 aplikasi per Puskesmas, 49% sistem butuh entri berulang [18] [P]
* RSUD: keterikatan vendor dan ragam format data perangkat [24] [P]
* PGHD sebagai bagian RME; akses pasien meningkatkan kesadaran dan pengelolaan mandiri [19] [P]

Isi slide, kolom kanan (standar dan FHIR):
* ICD, SNOMED CT, LOINC menjawab pertanyaan yang berbeda dari format pertukaran [P]
* FHIR: resource modular lewat REST API; SATUSEHAT berbasis FHIR R4 [20][25] [P]
* Perangkat ke FHIR: data perangkat ke Observation dan Device [23]; ECG 12 lead punya panduan SATUSEHAT, 17 dari 312 atribut inti [20] [P]
* Latensi di bawah 1 detik tanpa paket hilang pada sensor ke FHIR [26] [P]

Poin bicara:
* Konteks yang dibutuhkan sudah ada di RME, tapi tersebar. Format perangkat RADAR juga berbeda dari model RME.
* FHIR dipakai sebagai format kanonik, jembatan antar format, bukan klaim utama penelitian.

---

## Slide 5. Rumusan masalah, batasan, tujuan, dan kontribusi
(Bab 1.2, 1.3, 1.4, 1.5)

Isi slide, empat blok:
* Rumusan: data RADAR tidak bisa langsung menjadi satu rekaman klinis pasien. Dibutuhkan sistem pendukung keputusan yang mengintegrasikan data RME, RADAR, dan ECG 12 lead secara interoperabel, dalam satu tampilan.
* Batasan: sistem informasi untuk perangkat RADAR yang mengukur JVP; ECG 12 lead sebagai titik acuan; data RME sintetis atau data uji; keluaran pendukung keputusan, bukan diagnosis; belum divalidasi klinis.
* Tujuan: membangun sistem; merancang alur data dari penerimaan sampai tampilan dokter; memetakan data RADAR, ECG, RME ke FHIR. Luaran: rancangan, metode, prototipe.
* Kontribusi: pola mengintegrasikan data pengukuran perangkat baru dengan RME berbasis standar, dan pengelolaan data lintas sumber. Kontribusi klinis dan algoritma interpretasi tidak diklaim.

Di luar lingkup (kotak kecil): perangkat RADAR (akuisisi, I/Q, deteksi pulsa), algoritma interpretasi, validasi klinis, diagnosis, data pasien nyata.

Poin bicara:
* Ini slide inti. Tekankan bahwa penelitian membangun sistem di atas keluaran RADAR.
* Arah sempat bergeser dari profil FHIR untuk RADAR menjadi sistem terintegrasi, karena RADAR adalah alat pengukuran. Ceritakan bila ditanya.
* Fitur simpan dan kirim data ke dokter atau poli lain: tulis sebagai manfaat potensial, belum dipastikan sebagai inti.

---

## Slide 6. Tinjauan pustaka: CDSS dan manajemen data
(Bab 2.5)

Isi slide:
* CDSS: sistem berbasis pengetahuan yang memadukan data spesifik pasien untuk saran yang disesuaikan [36] [P]
* Kondisi literatur: dari 1.731 makalah, hanya 15 evaluasi luaran klinis, 2 terintegrasi EHR, 3 memakai standar HL7 [36]; 51,92% berdiri sendiri [37] [P]
* Yang berhasil diadopsi bersifat bantuan: dokter tetap memutuskan, menyatu dengan alur kerja [38] [P]
* Arsitektur aliran data (diagram lima kotak): penerimaan data, pemeriksaan mutu, penggabungan konteks, aturan, tampilan [P]
* Dasar tiap tahap: mutu sinyal radar [11]; ECG sebagai acuan waktu [9][7]; mesin aturan terpisah dari modul komunikasi, sekitar 50.000 transaksi per hari [39] [P]
* Interaksi dengan dokter: CDS Hooks, akurasi 96 sampai 100% pada tiga perangkat berbasis standar [29][40]; pemakaian aplikasi naik 130% [41] [P]

Poin bicara:
* Literatur menunjukkan CDSS yang terintegrasi dan berbasis standar masih langka.
* Rekomendasi harus hadir tepat waktu di alur kerja tanpa menambah beban kognitif dokter.

---

## Slide 7. Kesenjangan dan rasional penelitian
(Bab 2.6 dan 2.7)

Isi slide:
* Kesenjangan: data RADAR dan RME belum terhubung; standar sudah ada (FHIR, SATUSEHAT, panduan ECG) tetapi belum dipakai untuk menyatukan data pengukuran JVP dengan RME [P, dari 1.2 dan 2.7]
* Rantai rasional (enam langkah, satu baris tiap langkah): beban CVD, kongesti sisa, JVP noninvasif, RADAR nirkontak, JVP butuh konteks, RME terfragmentasi, maka butuh sistem
* Arah penelitian: rekayasa sistem pendukung keputusan dan manajemen data terpadu
* Posisi keluaran: instrumen pendukung pertimbangan, bukan diagnosis otomatis atau prediksi risiko mandiri [P]

Catatan penting: subbab 2.6 di proposal masih kosong ("diisi mahasiswa"). Slide ini bersandar pada 1.2 dan 2.7. Isi 2.6 sebelum sidang bila bisa, karena penguji akan menanyakan penelitian terdekat.

---

## Slide 8. Bab III: rencana implementasi dan status, plus penutup
(Bab III baru dimulai)

Isi slide, kiri (status):
* Selesai: Bab I, Bab II (kecuali 2.6), 41 referensi
* Belum ada hasil sistem. Ini proposal.

Isi slide, tengah (rencana kerja):
* 1. Tetapkan keluaran RADAR per sesi dan peran ECG 12 lead
* 2. Rancang alur data lima tahap
* 3. Petakan RADAR, ECG, RME ke FHIR, mengacu panduan ECG SATUSEHAT [20] dan pemetaan perangkat [23]
* 4. Siapkan data RME sintetis atau data uji
* 5. Bangun prototipe: tampilan terpadu dan berbagi rekam
* 6. Ukur: kelengkapan pemetaan, jumlah format sumber, keberhasilan berbagi rekam, akurasi ujung ke ujung (target angka masih placeholder)

Isi slide, kanan (terbuka):
* Keluaran RADAR per sesi, peran dan asal ECG, sumber data sintetis, status fitur simpan dan kirim, judul final

Penutup (satu kalimat di bawah):
* Data hasil pengukuran RADAR bermakna bila dibaca bersama ECG dan konteks RME. Penelitian ini membangun sistem yang menyatukannya, sebagai pendukung keputusan dan bukan diagnosis. Mohon masukan untuk lingkup prototipe dan indikator pengukuran.

---

# Bank punchline per slide (sumber tambahan)

Pilih sedikit, jangan semua.

## Slide 1 (Bab 1.1 P1, 2.1)

* [P] "Penyakit kardiovaskular menyebabkan 19,8 juta kematian pada 2022, sekitar sepertiga dari seluruh kematian di dunia." [1]
* [P] "85% kematian kardiovaskular disebabkan serangan jantung dan stroke, dan lebih dari tiga perempat terjadi di negara berpenghasilan rendah dan menengah." [1]
* [P] "Kematian kardiovaskular di Indonesia lebih dari dua kali lipat dalam 30 tahun." [2]
* [P] "DALYs Indonesia terburuk kedua di ASEAN setelah Laos, dan tidak turun bermakna selama tiga dekade." [2]
* [P] "Gagal jantung adalah tempat beban itu berulang kali kembali ke rumah sakit." (2.1)
* [P] "Kelompok yang dirawat ulang dalam 30 hari punya mortalitas enam bulan 27,66%, dibanding 10,36%." [3] (lihat peringatan Tung)
* [P] "Sebagian besar biaya perawatan gagal jantung dikaitkan dengan rawat inap ulang yang tidak terencana." [3]
* [P] "Risiko kematian melonjak lebih dari enam kali lipat pada bulan pertama setelah pulang." [4]
* [P] "Mortalitas satu tahun 25 sampai 30%, dan sepertiga sampai separuh pasien dirawat ulang dalam enam bulan." [4]
* [P] "Sekitar 30,9% pasien pulang dengan kongesti sisa." [4]
* [P] "Kenaikan CVP dikaitkan dengan memburuknya fungsi ginjal pada gagal jantung dekompensasi akut." [5]
* [P] "Kateterisasi vena sentral jadi baku emas, tetapi invasif sehingga tidak praktis untuk rutin." [6]
* [P] "Vena jugularis interna tidak punya katup menuju atrium kanan, jadi gelombangnya mencerminkan tekanan atrium kanan." [7]
* [P] "Penilaian visual JVP sulit pada leher tebal atau posisi pasien kurang tepat." [6]
* [C] "Indonesia peringkat enam dunia dalam jumlah absolut kematian kardiovaskular." (GBD, catatan pendukung) [2]
* [C] "Pasien yang dirawat ulang punya rawat inap indeks lebih lama (11,5 hari berbanding 8,6 hari)." (Tung, catatan pendukung) [3]

## Slide 2 (Bab 1.1 P2, 2.2)

* [P] "RADAR membaca gerakan mikro permukaan tubuh lewat perubahan fase sinyal pantulan. Tidak ada yang menempel di leher." [9]
* [P] "Gelombang radar dapat menembus pakaian tipis atau kasur, pasien tidak perlu membuka baju." [9]
* [P] "Dataset radar 24 GHz: sekitar 24 jam dari 30 subjek sehat, lima skenario termasuk Valsalva, apnea, dan uji meja miring." [9]
* [P] "Pada pulsa karotis, pergeseran fase radar berhubungan linear dengan perpindahan dinding pembuluh dari ultrasonografi." [34]
* [P] "Sensor 24 GHz berdaya 7 mW merekam denyut vena tanpa menekannya, tidak seperti transduser mekanis." [10]
* [P] "Bentuk gelombang JVP berubah mengikuti sudut kemiringan tubuh sampai 75 derajat." [10]
* [P] "FMCW 60 GHz dengan eigen beamforming memisahkan vena jugularis dari arteri karotis." [6]
* [P] "Penilai mutu sinyal radar mencapai akurasi 93,2 sampai 100%, dan laju detak jantung menyimpang 0 sampai 4 denyut per menit dari sensor kontak." [11]
* [P] "Kecepatan aliran vena jugularis punya dua gelombang pengosongan yang sinkron dengan lembah x dan y, jadi rekaman vena perlu diselaraskan dengan ECG." [7]
* [P] "Bentuk gelombang membawa informasi lebih kaya daripada satu angka tekanan." (2.2)
* [C] "Radar nirkontak tidak butuh sonografer terlatih seperti USG." [34]
* [!] "Tekanan vena jugularis normal 5 sampai 8 cmH2O." Rujukan belum jelas, jangan diucapkan.
* Kalimat jujur: "Bukti RADAR untuk JVP masih studi kelayakan awal dengan sampel kecil."

## Slide 3 (Bab 1.1 P3, 2.1, 2.7)

* [P] "Termometer cukup memberi satu angka. JVP butuh ECG dan konteks pasien untuk dibaca." (jawaban termometer)
* [P] "Kenaikan tekanan intravaskular sistemik (CVP dan JVP) mendahului perpindahan cairan ke jaringan." [31]
* [P] "Berat badan dan sesak napas baru tampak sekitar 24 sampai 48 jam sebelum dekompensasi. Tekanan pengisian naik bertahap beberapa pekan sebelumnya." [32]
* [P] "Telemonitoring berbasis berat badan dan keluhan memberi hasil netral pada berbagai uji besar." [32]
* [P] "Aturan berat badan hanya mendeteksi 35% kejadian perburukan. Indeks multiparameter mencapai 70%." [14]
* [P] "Penilaian gagal jantung membutuhkan lebih dari satu parameter." (1.1)
* [P] "JVP yang masih tinggi saat pulang berkaitan dengan kejadian kardiovaskular buruk dalam satu tahun." [13] (pakai hati hati)
* [P] "Pedoman ESC 2026 menekankan euvolemia berkelanjutan, integrasi data multidimensi, dan pengawasan kongesti residual." [33]
* [P] "Variasi antarpasien datang dari obat, berat badan, hasil laboratorium, kunjungan sebelumnya, dan riwayat penyakit. Semuanya ada di RME."
* [P] "Data hasil pengukuran JVP tidak bisa berdiri sendiri karena maknanya bergantung pada diagnosis komorbid, riwayat medikasi, dan dinamika berat badan." (2.7)
* [P] "CDSS yang memanfaatkan informasi tambahan pasien meningkatkan penyesuaian rencana, adjusted OR 2,67." [15]
* [C] "Rencana yang terkontekstualisasi menaikkan peluang masalah klinis teratasi 2,13 kali (aOR 2,13)." Cek ke makalah Weiner sebelum dipakai. [15]
* [C] "Durasi QRS lebih dari 130 ms tercatat sebagai faktor risiko kongesti residual." Menjustifikasi ECG sebagai konteks. Cek dulu. [4]
* [!] Jangan sebut studi dan angka Drazner. Cukup: "bukti klinis JVP saling bertentangan." [12]

## Slide 4 (Bab 1.1 P4 dan P5, 2.3, 2.4)

* [P] "Permenkes 24/2022 mewajibkan RME, sehingga setiap kunjungan menghasilkan sedikitnya satu dokumen RME." [16]
* [P] "UU 17/2023 mengharuskan teknologi dan sistem informasi kesehatan mengikuti standar interoperabilitas, dan menegaskan hak pasien mengakses isi rekam medisnya." [22]
* [P] "Setiap Puskesmas rata rata menjalankan sekitar 30 aplikasi." [18]
* [P] "49% sistem menuntut entri data berulang, 29% tanpa fitur analisis otomatis, tenaga kesehatan memasukkan data ke hingga enam sistem." [18]
* [P] "Di 12 RSUD tipe C dan D: keterikatan vendor, ragam format data perangkat, infrastruktur terbatas." [24]
* [P] "Studi RSUD menyimpulkan perlunya lapisan perantara yang ringan dan mudah dihubungkan pengembang perangkat baru." [24]
* [P] "Perangkat baru memakai format keluaran sendiri, strukturnya berbeda dari model RME." (1.1)
* [P] "Pasien dapat memberi, mencabut, dan membatasi masa berlaku akses dokter rujukan (DecMed)." [17]
* [P] "Akses pasien ke rekam medis meningkatkan kesadaran, pengelolaan mandiri penyakit kronis, dan kualitas hidup." [19]
* [P] "Data Garmin sudah dialirkan ke server FHIR lewat hub API ke Observation." [27]
* [P] "eSource: data diambil langsung dari RME lewat resource FHIR, transkripsi manual berkurang." [35]
* [P] "ICD mengklasifikasikan penyakit, SNOMED CT menamai konsep klinis, LOINC mengodekan observasi dan laboratorium." (sumber definisi masih placeholder)
* [P] "Tinjauan 49 studi FHIR: standardisasi data 41%, penangkapan data 29%, analisis klinis 12%; dipasangkan dengan LOINC 37%, SNOMED CT 29%, ICD 10 18%." [25]
* [P] "FHIR menyusun data sebagai resource modular, dibatasi lewat profil, dipertukarkan lewat REST API." [25]
* [P] "SATUSEHAT berbasis FHIR R4." [20]
* [P] "Dari 312 atribut aECG, 17 ditetapkan sebagai permukaan pertukaran inti. SNOMED CT hanya mencakup 13 dari 32 tipe sadapan, diatasi dengan provisional ValueSets." [20]
* [P] "Data perangkat bisa dipetakan ke Observation dan Device tanpa kehilangan konteks asal, tapi ada 25 tantangan teknis." [23]
* [P] "Profil yang valid secara sintaks belum tentu benar secara makna." [23]
* [P] "Sinyal sensor nirkabel ke FHIR Observation dengan latensi di bawah satu detik dan tanpa paket hilang." [26]
* [P] "FHIR adalah format kanonik: satu bentuk data yang menampung RADAR, ECG, dan RME agar dibaca bersama." (2.4)
* [C] "SMART on FHIR mengalirkan data mandiri pasien ke 3 vendor EHR di 18 klinik." [28]
* [C] "Hanya 28,9% Puskesmas punya internet stabil dan cepat." [18]

## Slide 5 (Bab 1.2 sampai 1.5)

* [P] "Data RADAR tidak bisa langsung menjadi satu rekaman klinis pasien." (1.2)
* [P] "Dibutuhkan satu tampilan yang memuat data RADAR, RME, dan ECG 12 lead." (1.2)
* [P] "Keluaran sistem adalah pendukung keputusan, bukan diagnosis, dan belum divalidasi klinis." (1.3)
* [P] "Data RME sintetis atau data uji, karena data nyata memerlukan persetujuan etik." (1.3)
* [P] "Validasi klinis memerlukan studi terpisah dengan pasien nyata." (1.3)
* [P] "Hasilnya rancangan, metode, dan prototipe yang dapat digunakan dokter." (1.4)
* [P] "Bagi pengembang sistem informasi kesehatan, hasilnya contoh cara menghubungkan data perangkat RADAR dengan RME." (1.4)
* [P] "Kontribusi di interoperabilitas dan pengelolaan data lintas sumber. Kontribusi klinis dan algoritma interpretasi tidak diklaim." (1.5)
* Kalimat batas: "Saya tidak membangun alat RADAR dan tidak menulis algoritma deteksi. Saya membangun sistem di atas keluarannya."
* Kalimat arah: "FHIR dan SATUSEHAT adalah jembatan dan ekosistem, bukan klaim utama."

## Slide 6 (Bab 2.5)

* [P] "CDSS adalah sistem berbasis pengetahuan yang aktif, memadukan data spesifik pasien untuk saran yang disesuaikan." [36]
* [P] "Dari 1.731 makalah CDSS berbasis aturan, hanya 15 yang mengevaluasi luaran klinis secara ketat." [36]
* [P] "Hanya 2 yang terintegrasi dengan EHR, hanya 3 memakai standar resmi, semuanya HL7." [36]
* [P] "51,92% CDSS dibangun sebagai aplikasi yang berdiri sendiri." [37]
* [P] "Modul berbasis aturan paling banyak dipakai dan paling transparan." [37]
* [P] "CDSS kardiovaskular yang berhasil bersifat bantuan: sintesis disajikan, keputusan di tangan dokter." [38]
* [P] "Sistem harus menyatu dengan alur kerja yang sudah berjalan." [38]
* [P] "Arsitektur aliran data: penerimaan, pemeriksaan mutu, penggabungan konteks, aturan, tampilan." (2.5)
* [P] "Platform FHIR microservices memisahkan modul komunikasi dari mesin aturan: sekitar 50.000 transaksi per hari, lebih dari 400 model aturan." [39]
* [P] "Pemeriksaan mutu penting karena sinyal radar rentan derau gerakan." [11]
* [P] "ECG 12 lead jadi acuan waktu dan pembanding, termasuk membedakan sistol dan diastol pada gelombang vena." [9][7]
* [P] "Standar CDS kontemporer memisahkan logika klinis dari perangkat lunak RME dan bisa dijalankan lintas institusi." [29]
* [P] "CDS Hooks memicu layanan saat dokter membuka rekam medis atau mencatat hasil baru." [29]
* [P] "Tiga perangkat CDSS berbasis standar: akurasi 96 sampai 100%, peringatan positif palsu 0,0 sampai 11,1%." [40]
* [P] "Pemicu CDS Hooks menaikkan pemakaian aplikasi SMART on FHIR 130% (70 dokter, tujuh bulan)." [41]
* [P] "Rekomendasi perlu hadir tepat waktu tanpa menambah beban kognitif dokter." (2.5)

## Slide 7 (Bab 2.6 dan 2.7)

* [P] "Evaluasi kongesti dan JVP berperan mendasar dalam tatalaksana gagal jantung." (2.7)
* [P] "RADAR mengatasi keterbatasan kateterisasi invasif dan variabilitas pemeriksaan visual." (2.7)
* [P] "Data JVP tidak bisa jadi indikator tunggal, signifikansinya bergantung pada konteks pasien di RME." (2.7)
* [P] "RADAR dan RME beroperasi pada format, skema metadata, dan ekosistem terpisah, maka perlu lapisan interoperabilitas berbasis HL7 FHIR." (2.7)
* [P] "Arah penelitian: rekayasa perangkat lunak pendukung keputusan dan manajemen data terpadu, bukan perangkat keras RADAR atau algoritma diagnostik baru." (2.7)
* [P] "ECG 12 lead sebagai titik acuan fisiologis." (2.7)
* [P] "Luaran rekomendasi adalah pendukung pertimbangan, bukan diagnosis otomatis maupun prediksi risiko mandiri." (2.7)
* Kalimat gap: "Alatnya ada, standarnya ada, konteksnya ada. Yang belum ada adalah sistem yang menghubungkannya."

## Slide 8 (Bab III dan penutup)

* "Proposal ini punya rasional kuat dan belum punya hasil sistem. Bab III menjelaskan cara membuktikannya."
* [P] "Empat indikator teknis: kelengkapan pemetaan, jumlah format sumber, keberhasilan berbagi rekam, akurasi ujung ke ujung." (1.4, target angka belum ditetapkan)
* [P] "Validasi makna pemetaan perlu eksplisit, bukan hanya sintaks." [23]
* [P] "Pola desain yang dijadikan acuan: pemisahan komunikasi dan aturan [39], aturan transparan [37], pemicu di alur kerja [29][41]. Sebut sebagai kandidat, bukan keputusan."
* "Satu angka tidak cukup. Gelombang, ECG, dan konteks pasien perlu dibaca bersama."
* "Data bermakna bila terhubung."

---

# Jawaban singkat untuk pertanyaan penguji

1. Kenapa tidak tampilkan angkanya saja seperti termometer?
   JVP adalah gelombang yang maknanya bergantung pada konteks dan waktunya terhadap siklus jantung [7]. Data tunggal lemah (35% berbanding 70%) [14], dan konteks pasien mengubah penanganan (aOR 2,67) [15].
2. Kontribusi Anda apa kalau alat dan standarnya sudah ada?
   Pola integrasi data perangkat baru dengan RME berbasis standar dan pengelolaan data lintas sumber. Hanya 2 dari 1.731 makalah CDSS yang terintegrasi EHR [36].
3. Kenapa arahnya berubah dari profil FHIR untuk RADAR?
   RADAR adalah alat pengukuran, jadi FHIR saja bukan kebutuhannya. Fokus dialihkan ke sistem yang menyatukan data.
4. Apakah sistem ini mendiagnosis?
   Tidak. Pendukung keputusan, dokter yang memutuskan, belum divalidasi klinis.
5. Bagaimana kalau sinyal RADAR berisik?
   Ada tahap pemeriksaan mutu [11]. Algoritma deteksi di luar lingkup.
6. Mana hasilnya?
   Belum ada, ini proposal. Yang akan diukur adalah empat indikator teknis di Bab III.
7. Datanya dari mana?
   RME sintetis atau data uji, sumber sedang ditentukan.

---

# Hindari atau ucapkan dengan hati hati

Aturan kerangka dari pembimbing:
* Pakai "pengukuran", jangan "pemantauan" untuk alat ini
* Pakai "data hasil pengukuran RADAR", jangan "citra RADAR"
* RADAR tidak mengukur CVP
* Keluaran bukan diagnosis, prediksi, atau skor risiko tervalidasi
* FHIR dan SATUSEHAT adalah jembatan, bukan klaim utama
* Tanpa tanda hubung atau tanda pisah di teks Indonesia pada slide

Klaim yang belum kuat:
* Drazner [12]: sumber belum terselesaikan
* Storrow [8]: deskripsi studi tidak konsisten, jangan sebut jumlah dokter atau pasien
* Kasai [13]: asal dan definisi luaran belum jelas
* Tung [3]: 27% dan 27,66% mungkin tertukar
* Angka two object method (82,9%, 43,3%, 67,7%) di 1.1 bertanda [new] tanpa rujukan
* Riech, Suzuki, Das, Shi: data bibliografis berbeda antar catatan
* Cakupan RME (280 juta, 2.770 RS, kunjungan BPJS): belum terverifikasi
* 5 sampai 8 cmH2O, ESC Kelas IIa, Kim dkk., nomor pasal Permenkes: sengaja tidak dipakai

---

# Perlu dirapikan di proposal sebelum sidang

1. Subbab 1.4 menyebut "diagnosa penyakit kardiovaskular" di tujuan khusus, bertabrakan dengan batasan "bukan diagnosis".
2. Subbab 2.6 kosong.
3. Subbab 1.1 masih memuat placeholder "cite" di dua tempat ("Survey oleh cite" dan "terbuktikan oleh cite") dan penanda [new].
4. Subbab 1.1 memakai [23] (Riech) untuk kewajiban mengikuti standar SATUSEHAT, padahal Riech membahas pemetaan perangkat ISO/IEEE 11073 ke FHIR.
5. Rujukan [28] (Wesley) dan [30] (Kamil) ada di daftar pustaka tetapi tidak dikutip di badan teks.
6. Subbab 2.7 menyebut ECG "memvalidasi keselarasan fase", lebih kuat dari peran "titik acuan" di 1.3. Samakan istilahnya.
7. Keputusan pembimbing terbuka: status fitur simpan dan kirim, keluaran RADAR per sesi, peran ECG, judul final.

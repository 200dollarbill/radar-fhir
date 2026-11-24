# Fishbone: fondasi dan sumber

Nomor [n] = nomor di daftar pustaka `proposal.md`. Tanda (?) = sumber belum terverifikasi atau sitasi belum lengkap, cek dulu.

## HEAD (masalah)
Data pengukuran RADAR (JVP), konteks pasien di RME, dan ECG 12 sadapan belum terhubung, sehingga dokter sulit menilai status kongesti dalam satu tampilan dan pasien sulit menyimpan atau mengirim datanya.

## Bone 1: Penilaian JVP/CVP konvensional terbatas
- Das 2024 [6]: CVP akurat butuh kateter vena sentral (invasif); penilaian visual sulit (leher tebal, posisi)
- Kenny 2025 [7]: JVP mencerminkan tekanan atrium kanan; gelombang a, c, v, x, y
- Mullens 2009 [5]: kenaikan CVP terkait perburukan fungsi ginjal
- Storrow 2007 [8] (?): penilaian JVP di sisi tempat tidur bergantung pemeriksa

## Bone 2: Satu parameter tidak cukup, butuh konteks klinis
- Drazner [12] (?): JVP tinggi penanda beban penyakit, bukan prediktor tunggal (sumber belum jelas)
- Kasai 2023 [13] (?): JVP tinggi saat pulang terkait kejadian buruk 1 tahun
- Fudim 2025 [14]: aturan berat badan 35% vs multiparameter 70% (SCALE HF 1)
- Stevenson 2023 [32]: berat badan dan sesak muncul terlambat, tekanan pengisian naik berminggu minggu lebih awal
- Núñez 2022 [31]: kenaikan tekanan intravaskular sistemik mendahului edema jaringan
- Weiner 2022 [15]: CDSS dengan konteks pasien dari RME, aOR 2,67

## Bone 3: Beban gagal jantung tinggi, risiko rawat ulang
- WHO [1]: 19,8 juta kematian CVD (2022), sekitar 32%
- Muharram 2024 [2]: kematian CVD Indonesia 292 ribu ke 659 ribu (1990 sampai 2019)
- Tung 2016 [3] (cek angka): rawat ulang 30 hari 10,9%
- Metra 2023 [4]: kongesti sisa 30,9% saat pulang; mortalitas naik lebih dari 6 kali di bulan pertama
- Køber 2026 [33]: pedoman ESC, penilaian euvolemia berkelanjutan

## Bone 4: Data RADAR modalitas baru, belum standar dan masih tahap awal
- Schellenberger 2020 [9]: radar 24 GHz, dataset tersinkron ECG
- Suzuki 2021 [10]: sensor gelombang mikro 24 GHz untuk JVP, 8 sukarelawan
- Das 2024 [6]: FMCW 60 GHz, studi kelayakan, sampel sangat kecil
- Shi 2018 [34]: pergeseran fase radar berhubungan linear dengan perpindahan dinding karotis
- Yen 2022 [11]: derau gerakan, perlu penilaian mutu sinyal
- Riech 2021 [23]: struktur data perangkat berbeda dari model RME

## Bone 5: Data RME terfragmentasi dan format berbeda
- Aisyah 2025 [18]: 10.260 Puskesmas, sekitar 30 aplikasi tiap Puskesmas, 49% entri berulang
- Savandha 2026 [24]: vendor lock-in, ragam format data perangkat di RSUD
- Kamil 2020 [30]: dokumentasi terpisah, berkas tidak lengkap, verifikasi terlambat
- Purnama 2026 [17]: data tersebar di sistem independen; akses pasien perlu kendali
- Regulasi sebagai konteks: Permenkes 24/2022 [16], Kepmenkes 1423/2022 [21], UU 17/2023 [22]

## Bone 6: Sistem pendukung keputusan terdahulu terisolasi
- Papadopoulos 2022 [36]: dari 1.731 makalah, hanya 2 terintegrasi EHR, 3 pakai standar HL7
- Hak 2022 [37]: 51,92% CDSS berdiri sendiri
- Susanto 2023 [38]: CDSS yang diadopsi bersifat bantuan dan menyatu dengan alur kerja
- Morgan 2022 [41]: CDS Hooks naikkan pemakaian aplikasi 130%
- Isabelle 2025 [40]: CDSS berbasis standar akurasi 96 sampai 100%

## Opsional: bone 7 (data pasien, jika fitur simpan dan kirim jadi inti)
- Tapuria 2021 [19]: akses pasien ke rekam medis (kesadaran, kualitas hidup, kekhawatiran berkurang)
- Purnama 2026 [17]: kendali akses oleh pasien (IOTA)
- Abedian 2025 [27]: data perangkat penderia ke server FHIR
- Wesley 2021 [28]: data pasien ke 3 vendor RME, 18 klinik (SMART on FHIR)

## Bukan penyebab, tapi pendukung solusi (untuk slide solusi, bukan tulang)
- Vorisek 2022 [25]: tinjauan FHIR untuk interoperabilitas
- Chaidir 2025 [20]: panduan FHIR R4 ECG 12 sadapan patuh SATUSEHAT
- Adochiei 2024 [26]: sinyal sensor ke FHIR, latensi di bawah 1 detik
- Strasberg 2021 [29]: FHIR, CQL, CDS Hooks untuk CDS
- Semenov 2019 [39]: platform data FHIR untuk CDS
- Garza 2021 [35]: FHIR untuk eSource

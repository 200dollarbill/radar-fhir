---
id: term-loinc-laboratory
title: LOINC Laboratory
source_url: https://satusehat.kemkes.go.id/platform/docs/id/terminology/loinc/laboratory/
group: satusehat
fhir_version: R4
fetched_at: '2026-09-11T13:33:32Z'
sha256: cd6b4f50706e3bc3c4511958d6689e4d829f718fed4490553707641c7a38e367
---
# Laboratorium

## Latar Belakang Penggunaan LOINC

SATUSEHAT merupakan platform interoperabilitas data kesehatan. Interoperabilitas memungkinkan informasi kesehatan dipertukarkan sewaktu-waktu, antara tenaga medis yang berbeda, entitas lain yang berwenang, dan pasien, dalam kondisi aman, rahasia serta perlindungan data lainnya. SATUSEHAT menggunakan standar HL7 FHIR dalam pertukaran datanya. Dalam melakukan pertukaran HL7 FHIR bekerja seperti grammar dalam sebuah pembelajaran bahasa, oleh karenanya diperlukan *vocabulary* yang mendukung. Pada kasus pertukaran data laboratorium, *vocabulary* yang dapat mendukung adalah LOINC (Logical Observation Identifiers Name and Codes)

Hingga saat ini di Indonesia terdapat institusi laboratorium terakreditasi sejumlah 1400 laboratorium. Pada 1400 laboratorium tersebut terdapat perbedaan nama pemeriksaan laboratorium serta perbedaan kode pemeriksaan kode laboratorium dalam LIS (Laboratory Information System), sehingga data yang ada sangatlah variatif dan tidak terstandar. Hal ini menyebabkan data hasil laboratorium tidak bisa dipertukarkan satu sama lain.

Sebagai contoh, laboratorium A dapat menyebut pemeriksaan laboratorium dengan istilah PCT sedangkan laboratorium lain menyebutnya dengan istilah Procalcitonin (PCT). Selain itu, setiap institusi laboratorium memiliki kode lokal yang berbeda-beda untuk masing-masing pemeriksaan dan hasil observasi laboratorium. Berikut terlampir tabel contoh perbedaan penggunaan kode pemeriksaan laboratorium antar instansi laboratorium.

Tabel 1. Perbandingan Istilah Pemeriksaan Laboratorium di Indonesia

|  | Kode Laboratorium A | Kode Laboratorium B | Kode LOINC |
| --- | --- | --- | --- |
| Kalium (K) Urin 24 jam | 1001 | 200309 | 2829-0 |
| Laju Endap Darah | 190893 | 340578 | 30341-2 |
| PCT | 717 | 203 | 33959-8 |

Oleh karenanya diperlukan suatu kamus terminologi yang dapat memfasilitasi standarisasi dan kodifikasi istilah pemeriksaan laboratorium untuk mendukung pertukaran data laboratorium di Indonesia melalui SATUSEHAT. Kamus terminologi laboratorium yang digunakan untuk pertukaran data tersebut mengacu pada Logical Observation Identifiers Names and Codes yang kemudian disebut LOINC.

## Tipe Tes LOINC Laboratorium

LOINC menyediakan terminologi untuk 2 tipe tes yaitu tes laboratorium tunggal dan tes laboratorium panel. Tes laboratorium tunggal merupakan pemeriksaan yang dilakukan untuk menguji variabel tunggal (baik untuk pengukuran klinis dan pemeriksaan laboratorium) sebagai contoh:

Tabel 2. Tes Laboratorium Tunggal

| No | Nama pemeriksaan | Variabel yang diuji dalam pemeriksaan |
| --- | --- | --- |
| 1 | Glucose [mg/dl] in urine | **Kadar glukosa** dalam urin |
| 2 | Erythrocytes [#/volume] in Blood | **Jumlah eritrosit** dalam darah |

Sedangkan tes laboratorium panel merupakan pemeriksaan laboratorium yang dilakukan untuk menguji kumpulan dari variabel-variabel tunggal tersebut, sebagai contoh:

Tabel 3. Tes Laboratorium Panel

|  |  |  |
| --- | --- | --- |
| **No** | **Nama pemeriksaan** | **Variabel yang diuji dalam pemeriksaan** |
| 1 | Complete blood count [CBC] with auto differential panel | Pemeriksaan darah rutin yang mengukur **kadar hemoglobin, hitung eritrosit, hitung leukosit**, dll. |
| 2 | Elektrolit | Pemeriksaan elektrolit yang mengukur **kadar natrium, kalium dan klorida pada tubuh** |

## Komponen LOINC

LOINC terdiri atas 6 komponen utama yaitu *component/analyte, property, timing, scale, system, method*. Berikut merupakan penjelasan untuk masing masing komponen tersebut.

### *Component/Analyte*

*Component/Analyte* merupakan bagian utama pada LOINC dan hal pertama yang akan digunakan sebagai kata kunci/*keyword* dalam melakukan pemetaan terminologi laboratorium khususnya dalam proses mencari kode LOINC. *Component/Analyte* mewakili hal yang sedang diukur atau diobservasi. Sebagai contoh: *component/analyte* bisa saja merupakan zat seperti glukosa atau sodium atau mungkin pengukuran turunan seperti hematokrit. *Component/Analyte* juga dapat sangatlah spesifik, oleh karenanya LOINC menggunakan notasi “titik” untuk memberikan keterangan spesifik sebagai contoh: Calcium.ionized, Epstein Barr virus early Ab.IgM, B.Melitensis. *Component/Analyte* terdiri atas 3 sub bagian yang tertera pada tabel berikut:

Tabel 4. Sub Bagian Component/Analyte

| No | Sub-bagian | Contoh |
| --- | --- | --- |
| 1 | Nama utama *(Principal Name)* | - Calcium - Calcium.ionized - Hepatitis A virus Ab.IgG - Mumps virus Ab.IgG+IgM - ABO & Rh group panel - Albumin/Protein.total |
| 2 | Challenge or provocation - Time delay - Substance of challenge - Amount administered - Route of administration | - Aldosterone^1H post 25 mg captopril PO - Glucose^10 AM specimen |
| 3 | Standarisasi atau pengaturan lain | - Calcium.ionized^^adjusted to pH 7.4 |

Contoh lebih lengkap terkait jenis-jenis *component* yang digunakan pada terminologi LOINC dapat dilihat pada lampiran 12.1.

### Property

*Property* mewakili atribut *component/analyte* untuk membedakan karakteristik *component/analyte* yang dapat diukur. Tipe-tipe *property* untuk pemeriksaan kuantitatif antara lain:

1. Mass
2. Substance
3. Catalytic Activity
4. Number Counts

Dengan subtipe antara lain:

1. Concentration (amount/value)
2. Contents (amount/mass)
3. Ratio
4. Fraction
5. Rate

Sedangkan tipe *property* untuk pemeriksaan kualitatif antara lain:

1. Lokasi
2. Temuan Klinis

Contoh lebih lengkap terkait jenis-jenis *component* yang digunakan pada terminologi LOINC dapat dilihat pada lampiran 12.2.

### Timing

*Timing* merupakan interval waktu pengamatan atau pengukuran dilakukan. Sebagian besar istilah LOINC (96%) diwakilkan dengan *timing* "titik waktu" (disingkat Pt/*Point in Time*). Namun di beberapa kasus komponen *timing*, seperti tes urin 24 jam komponen *timing* berisikan keterangan waktu spesifik. Adapun beberapa komponen *timing* yang disediakan oleh LOINC sebagai 24H, 12H, dll. Waktu juga dapat ditentukan untuk periode relatif, seperti jumlah prematur kontraksi ventrikel selama studi. Contoh lebih lengkap terkait jenis-jenis *component* yang digunakan pada terminologi LOINC dapat dilihat pada lampiran 12.3.

### System/Specimen

*System* merupakan komponen LOINC yang menunjukkan jenis spesimen atau “unit analisis” di mana observasi dilakukan. Untuk pemeriksaan laboratorium, komponen *system/specimen* yang sering digunakan antara lain serum, plasma, urin, CSF, darah rutin, dsb. Berikut merupakan contoh komponen *system/specimen*

Tabel 5. Komponen System/Specimen

| No | Singkatan | Deskripsi |
| --- | --- | --- |
| **1** | **Abscess** | Abscess |
| **2** | **BldV** | Blood venous |
| **3** | **CSF** | Cerebrospinal Fluid |
| **4** | **Plas** | Plasma |
| **5** | **Ser** | Serum |
| **6** | **Synv Fld** | Synovial Fluid (Joint fluid) |

Contoh lebih lengkap terkait jenis-jenis *component* yang digunakan pada terminologi LOINC dapat dilihat pada lampiran 12.4.

### Scale

*Scale* merupakan komponen LOINC yang menunjukkan bagaimana sebuah observasi dinilai. Berikut penjelasan lebih lanjut untuk komponen *scale*:

Tabel 6. komponen Scale

| Tipe | Singkatan | Deskripsi |
| --- | --- | --- |
| **Quantitative** | Qn | - Pengujian dengan titer dapat dilaporkan dalam bentuk kuantitatif - Bentuk numerik kontinu ; integer, ratio, real number, ranger - Hasil tes bisa memiliki operator relasi seperti {⇐, <, >, >=}. - Contoh nilai valid: “7”, “-7”, “7.4”, “-7.4”, “7.8912”, “0.125”, “<10”, “<10.15”, “>12000”, 1-10, 1:256 |
| **Ordinal** | Ord | - Hasil ordinal: kategori dengan tingkatan - *Scale* ordinal setara dengan semi-kuantitatif - Contoh: 1+, 2+, 3+; positive, negative; reactive, indeterminate, non reactive. |
| **Quantitative or Ordinal** | OrdQn | - Bisa dilaporkan dalam bentuk *Ord* atau *Qn* - Contoh: hasil resistensi obat dapat dilaporkan dengan kategori ordinal resisten, intermediet, dan susceptible atau dengan melaporkan ukuran diameter zona inhibisi (mm) |
| **Nominal** | Nom | - Hasil nominal: tidak ada tingkatan - Contoh: nama bakteri, tampakan spesimen seperti kuning, jernih, *bloody* |
| **Narrative** | Nar | - Teks naratif - Contoh: deskripsi mikroskopik |
| **“Multi”** | Multi | - Beberapa hasil pemeriksaan dilaporkan sebagai satu observasi |
| **Document** | Doc | - Dokumen dalam berbagai format (XML, naratif, dll) |
| **Set** | Set | - Digunakan untuk lampiran klinis |

### Method

*Method* satu-satunya komponen LOINC yang bersifat opsional. LOINC menyediakan kode yang berbeda untuk beberapa metode pemeriksaan yang menghasilkan pengukuran dengan sensitivitas berbeda atau dengan interpretasi klinis yang berbeda. Metode banyak ditemukan pada pemeriksaan serologi, mikrobiologi dan koagulasi. Berikut merupakan contoh komponen *method*:

Tabel 7. Komponen Method

| Metode | Singkatan | Keterangan |
| --- | --- | --- |
| **Latex Agglutination** | LA |  |
| **Agglutination** | Aggl |  |
| **Cytology Stain** | Cyto stain | Metode pewarnaan yang digunakan untuk pap smear, aspirasi jarum halus dan noda sel lainnya. |
| **Immunoassay** | IA | Mewakili hampir seluruh teknik *immunoassays* seperti termasuk Immune Blot dan Immunofluorescence, yang dibuat berdasarkan penggunaan historis. |
| **Veneral Disease Research Laboratory** | VDRL | Uji flokulasi mikroskopis |
| **Minimum Inhibitory Concentration** | MIC | Kerentanan Antibiotik |

Contoh lebih lengkap terkait jenis-jenis *component* yang digunakan pada terminologi LOINC dapat dilihat pada lampiran 12.5.

Berikut merupakan contoh pemetaan kode LOINC ke dalam 6 komponennya

Tabel 8. Pemetaan Kode LOINC dalam 6 Komponen

| 75410-1 Hepatitis B virus surface Ag [Presence] in Serum, Plasma or Blood by Rapid immunoassay | | |
| --- | --- | --- |
| 1 | Component/Analyte | Hepatitis B virus surface Ag |
| 2 | Property | PrThr (Presence or Threshold) |
| 3 | Time | Pt (Point in time) |
| 4 | System/Specimen | Ser/Plas/Bld |
| 5 | Scale | Ord (Ordinal) |
| 6 | Method | IA.rapid (Immunoassay.rapid) |

Tabel 9. .Pemetaan Kode LOINC dalam 6 Komponen

| 718-7 Hemoglobin [Mass/volume] in Blood | | |
| --- | --- | --- |
| 1 | Component/Analyte | Hemoglobin |
| 2 | Property | MCnc (Mass Concentration) |
| 3 | Time | Pt (Point in time) |
| 4 | System/Specimen | Bld (Blood) |
| 5 | Scale | Qn (Quantitative) |
| 6 | Method | - |

## Pengenalan Kode Pemeriksaan Penunjang Nasional

Pada proses melakukan pemetaan terminologi laboratorium terdapat 2 kondisi yang mungkin terjadi:

1. Pemetaan berhasil, terdapat kode LOINC untuk terminologi laboratorium yang dipetakan
2. Pemetaan tidak berhasil, kode LOINC untuk terminologi laboratorium yang ingin dipetakan belum tersedia di LOINC.

Oleh karenanya kementerian kesehatan menyediakan kode khusus sementara untuk mewadahi parameter yang kodenya belum tersedia di LOINC, yang disebut dengan Kode Pemeriksaan Penunjang Nasional. Adapun struktur kode untuk Kode Pemeriksaan Penunjang Nasional adalah sebagai berikut:

1. Kode dengan prefix “X” diikuti dengan 6 digit
2. Dimulai dari X099080
3. Kode ini akan diganti dengan kode LOINC ketika sudah tersedia.

![Kode Prefix](../../_images/loinc-laboratory-02.png)

Gambar 1. X099080 Titer Anti-ABO

## Langkah Pemetaan LOINC

Dalam rangka mendukung proses pertukaran data pada SATUSEHAT, pemetaan pemeriksaan Laboratorium berbasis LOINC menjadi penting. Berikut beberapa langkah dalam melakukan pemetaan LOINC:

1. Siapkan daftar pemeriksaan laboratorium dengan rincian data yang disarankan seperti pada tabel di bawah ini. Tabel ini dapat di *download* pada halaman *terminology browser* <https://s.kemkes.go.id/LOINCLaboratoriumv1o1> dengan menekan tombol **“Template LOINC Laboratorium v.1.1”** .

   Tabel 10. Rincian Data Pemeriksaan Laboratorium

   | Kategori | Kode Lokal | Nama Pemeriksaan | Permintaan/Hasil | Spesimen | Tipe Hasil Pemeriksaan | Satuan | Metode |
   | --- | --- | --- | --- | --- | --- | --- | --- |
   | **(a)** | **(b)** | **(c)** | **(d)** | **(e)** | **(f)** | **(g)** | **(h)** |
   | Hematologi | A001 | Procalcitonin (PCT) | Permintaan & Hasil | Serum | Quantitative | ng/mL | CMIA |

   Berikut merupakan keterangan pengisian tabel di atas:

   1. Kategori **(a)**: Tuliskan kelompok/kategori pemeriksaan laboratorium pada sistem lokal
   2. Kode Lokal **(b)**: Tuliskan kode pemeriksaan laboratorium pada sistem lokal
   3. Nama Pemeriksaan **(c)**: Tuliskan nama pemeriksaan laboratorium pada sistem lokal
   4. Permintaan/Hasil **(d)**: Isikan salah satu dari 3 pilihan berikut

      - Permintaan: parameter permintaan atau pemesanan pemeriksaan laboratorium
      - Hasil: parameter hasil pemeriksaan laboratorium — Permintaan & Hasil: parameter permintaan dan hasil laboratorium
   5. Spesimen **(e)**: Tuliskan spesimen yang digunakan pada parameter pemeriksaan laboratorium
   6. Tipe Hasil Pemeriksaan **(f)** : Isikan salah satu dari 5 pilihan berikut

      - Nominal
      - Ordinal
      - Quantitative
      - Narrative
      - OrdQn
   7. Satuan **(g)**: Tuliskan satuan hasil pemeriksaan apabila hasil dalam bentuk kuantitatif
   8. Metode **(h)**: Tuliskan metode analisis yang digunakan dalam pemeriksaan laboratorium.  
      Contoh: Electrophoresis, VDRL, HPLC, Manual Count, Automated Count, dsb
2. Buka dan *download* terminologi *browser* laboratorium pada tautan berikut ini: [**Lampiran LOINC Laboratorium**](https://s.kemkes.go.id/LampiranLOINC-Lab)
3. Struktur terminologi *browser* laboratorium LOINC dapat dilihat pada penjelasan berikut ini:

   - **No**  
     Tipe: Nomor  
     Kolom pertama (A), merupakan nomor urut dari terminologi laboratorium.
   - **Kategori/Kelompok Pemeriksaan**  
     Tipe: *Text*  
     Kolom kedua (B), kategori/kelompok pemeriksaan merupakan pengkategorian pemeriksaan laboratorium menjadi beberapa kelompok berdasarkan komponen yang diuji antara lain Kimia klinik, Hematologi, Imunoserologi, Mikrobiologi, dll.
   - **Nama Pemeriksaan Laboratorium**  
     Tipe: *Text*  
     Kolom ketiga © merupakan nama pemeriksaan laboratorium yang sudah distandarkan.
   - **Permintaan/Hasil**  
     Tipe: *Text*  
     Kolom keempat (D), Pada kolom ini terdapat 3 kemungkinan isian yaitu:

     1. Permintaan mewakili pemesanan pemeriksaan laboratorium *(order)*, sehingga untuk Hasilnya dibutuhkan kode tambahan.
     2. Hasil mewakili hasil uji atau observasi sebuah spesimen *(observation)* dan untuk Permintaannya dibutuhkan kode tambahan.
     3. Permintaan dan Hasil mewakili pemesanan pemeriksaan dan hasil uji/observasi sebuah spesimen, sehingga kode yang didapatkan sudah cukup (1 saja).
   - **Spesimen**  
     Tipe: *Text*  
     Kolom kelima (E), Spesimen merupakan sesuatu yang diambil dari pasien untuk kemudian diuji, diukur atau diobservasi dalam sebuah pemeriksaan laboratorium, sebagai contoh: serum, urin, dll.
   - **Tipe Hasil Pemeriksaan**  
     Tipe: *Text*  
     Kolom keenam (F), Tipe hasil pemeriksaan mewakili skala pengukuran hasil pemeriksaan laboratorium. Adapun Tipe hasil pemeriksaan yang digunakan pada terminologi *browser* laboratorium adalah: Nominal, Ordinal, Narrative, OrdQn, Quantitative.
   - **Satuan Hasil Pemeriksaan**  
     Tipe: *Text*  
     Kolom ketujuh (G), Satuan hasil pemeriksaan mewakili unit/satuan pengukuran hasil pemeriksaan laboratorium. Sebagai contoh: mg/dl
   - **Metode Analisis**  
     Tipe: *Text*  
     Kolom kedelapan (H), Metode analisis mewakili metode atau teknik yang digunakan dalam mengukur, menguji atau mengobservasi sebuah spesimen pada pemeriksaan laboratorium. Sebagai contoh: Immunoassay.
   - **Code**  
     Tipe: *Text*  
     Kolom kesembilan (I), Kode LOINC merupakan nomor unik terstandar yang mengidentifikasi pemeriksaan laboratorium. Terdiri atas 3-7 digit dengan format xxxxxx-x.
   - **Display**  
     Tipe: *Text*  
     Kolom kesepuluh (J), LOINC *Long Common Name* merupakan penamaan pemeriksaan laboratorium yang distandarkan oleh LOINC yang disarankan dan dipergunakan untuk pertukaran data melalui FHIR.
   - **Component**  
     Tipe: *Text*  
     Kolom kesebelas (K), *Component* merupakan bagian LOINC yang mewakili suatu hal yang sedang diukur, diuji atau diobservasi. Sebagai contoh: glukosa, kalium, dll.
   - **Property**  
     Tipe: *Text*  
     Kolom kedua belas (L), *Property* merupakan atribut atau karakteristik yang dapat diukur yang melekat pada suatu *component* sehingga membedakan suatu *component* dengan *component* lain. Sebagai contoh: *mass, substance,* dll.
   - **Timing**  
     Tipe: *Text*  
     Kolom ketiga belas (M), *Timing* merupakan komponen LOINC yang menjelaskan terkait interval waktu pengamatan atau pengukuran dilakukan. Sebagai contoh: 12H, 24H, Pt *(Point in Time)*, dll.
   - **System**  
     Tipe: *Text*  
     Kolom keempat belas (N), *System* merupakan komponen LOINC yang menunjukkan jenis spesimen atau “unit analisis” di mana observasi dilakukan. Sebagai contoh: *urine, serum, whole blood,* dll.
   - **Scale**  
     Tipe: *Text*  
     Kolom kelima belas (O), *Scale* merupakan komponen LOINC yang menunjukkan bagaimana sebuah observasi dinilai. Scale yang biasa terdapat pada LOINC antara lain, Narrative (Narr), Nominal (Nom), Ordinal (Ord), OrdQn, Quantitative, Document (Doc), Multi, Set.
   - **Method**  
     Tipe: *Text*  
     Kolom keenam belas (P), *Method* merupakan komponen LOINC yang menunjukkan teknik yang digunakan pada sebuah pemeriksaan laboratorium. Pada LOINC metode bersifat opsional sehingga akan ditemukan beberapa kode LOINC yang tanpa informasi metode.
   - **Unit of Measure**  
     Tipe: *Text*  
     Kolom ketujuhbelas (Q), *Unit of Measure* merupakan Satuan hasil pemeriksaan mewakili unit/satuan pengukuran hasil pemeriksaan laboratorium yang telah distandarkan oleh LOINC.
   - **Code System**  
     Tipe: *Text*  
     Kolom kedelapan belas ®, *Code System* merupakan kumpulan konsep dengan setiap konsepnya diwakili dengan kode unik dan deskripsinya.
   - **Version First Released**  
     Tipe: *Text*  
     Kolom kesembilan belas (S), *Version First Release* merupakan keterangan versi sebuah terminologi/kode di release pertama kali.
   - **Version Last Changed**  
     Tipe: *Text*  
     Kolom kedua puluh (T), *Version Last Changed* merupakan keterangan versi sebuah terminologi/kode terakhir diperbaharui.
4. Terdapat dua prinsip utama dalam melakukan pemetaan terminologi laboratorium, adapun prinsip tersebut diantaranya:

   1. Petakan ke kode LOINC yang paling spesifik berdasarkan informasi yang tersedia. Sebagai contoh **(Anti H. Pylori IgG Serum, Hasil Qualitative, Metode ELISA)**

      ![Prinsip Pertama dalam Pemetaan LOINC](../../_images/loinc-laboratory-03.png)

      Gambar 2. Contoh prinsip pertama dalam pemetaan LOINC

      Ketika melakukan pemetaan LOINC sebaiknya dilakukan pengecekan terkait ke enam komponen LOINC yang ada. Pada contoh di atas, terlihat bahwa pemeriksaan Anti H.Pylori IgG Serum dengan hasil kualitatif terdapat 3 kode LOINC, namun kasus ini menspesifikkan pemeriksaan tersebut dengan memberikan keterangan metode yaitu ELISA. Oleh karena nya kode LOINC yang tepat untuk digunakan adalah 17859-0. Sehingga dapat diambil kesimpulan, **jika parameter yang akan dipetakan memberikan keterangan spesifik, cari kode LOINC sesuai tingkat ke spesifikkan parameter tersebut.**
   2. Jangan overspesifik dengan mengasumsikan informasi yang tidak diketahui, sebagai contoh **(Anti H. Pylori IgG Serum, Result Qualitative, Metode ? (tidak diketahui))**

      ![Prinsip Kedua dalam Pemetaan LOINC](../../_images/loinc-laboratory-04.png)

      Gambar 3. Contoh prinsip kedua dalam pemetaan LOINC

      Ketika melakukan pemetaan LOINC sebaiknya dilakukan pengecekan terkait ke enam komponen LOINC yang ada. Pada contoh di atas, terlihat bahwa pemeriksaan Anti H.Pylori IgG Serum dengan hasil kualitatif terdapat 3 kode LOINC dan pada kasus ini terdapat informasi yang tidak tersedia/ tidak diketahui yaitu terkait metode pemeriksaan. Oleh karena nya kode LOINC yang tepat untuk digunakan adalah 16126-5. Sehingga dapat diambil kesimpulan, **jika terdapat informasi yang tidak diketahui/tersedia pada parameter yang akan dipetakan, jangan memberikan keterangan tambahan atau menebak nebak** metode yang digunakan. Sebaiknya dilakukan konfirmasi terkait metode yang digunakan kepada petugas institusi yang berwenang untuk pelaksanaan layanan laboratorium (**dokter Sp.PK atau analis laboratorium**) atau memetakan sesuai informasi yang ada.
5. Langkah Pemetaan

   1. Petakan pemeriksaan laboratorium menggunakan *browser* tersebut dengan mencari kata kunci dari nama pemeriksaan laboratorium ini pada kolom C.
   2. Pertimbangan pemilihan kode LOINC yang digunakan:

      1. Setelah menemukan nama pemeriksaan laboratorium, periksa pada kolom D Permintaan/Hasil untuk memilih apakah parameter yang akan dipetakan merupakan Permintaan, Hasil atau Permintaan & Hasil.
      2. Kemudian setelah Nama Pemeriksaan dan Permintaan/Hasil sudah sesuai, proses dapat dilanjutkan dengan memilih spesimen yang sesuai dengan parameter yang sedang dipetakan pada kolom E.
      3. Proses dilanjutkan dengan mengecek Tipe Hasil Pemeriksaan pada kolom F.
      4. Cek Satuan Hasil Pemeriksaan pada kolom G dan pilih yang sesuai dengan satuan yang tertera pada alat pemeriksaan laboratorium yang digunakan.
      5. Pastikan untuk memilih metode analisis yang digunakan pada kolom H sudah sesuai dengan teknik pemeriksaan laboratorium yang telah dilakukan. Jika informasi terkait teknik pemeriksaan tidak tersedia silakan pilih baris yang tidak menspesifikkan metode analisis (kolom kosong).
      6. Dan terakhir, silakan pilih kode LOINC atau Kode Pemeriksaan Penunjang Nasional pada kolom I yang sudah sesuai dengan ke 6 kriteria yang sudah dicari.

         Berikut merupakan contoh tabel yang akan dilihat pada terminologi *browser*:

         ![Tabel Terminologi Laboratorium](../../_images/loinc-laboratory-05.png)

         Gambar 4. Contoh Tabel Terminologi Browser untuk Laboratorium
   3. Jika sudah dilakukan langkah (1) hingga (6) namun kode LOINC masih belum ditemukan dan pemetaan belum berhasil, maka silakan melakukan permintaan kode LOINC sesuai dengan prosedur yang dijelaskan pada Bab 7 Buku Panduan ini.

## Answer List

Standar LOINC menyediakan kodefikasi standar untuk beberapa hasil pemeriksaan dengan tipe pemeriksaan Nominal dan Ordinal. Terdapat 3 tipe hubungan antara kode LOINC dengan daftar jawaban yang telah disediakan oleh LOINC:

1. Normative  
   Daftar jawaban yang wajib digunakan dalam pelaporan hasil pemeriksaan
2. Preferred  
   Daftar jawaban yang sangat disarankan untuk digunakan dalam pelaporan hasil pemeriksaan
3. Example  
   Contoh daftar jawaban yang dapat digunakan untuk melaporkan hasil pemeriksaan

   Daftar jawaban yang disediakan oleh LOINC dapat diunduh pada [**Lampiran LOINC Laboratorium**](https://s.kemkes.go.id/LampiranLOINC-Lab). Berikut adalah penjelasan masing-masing kolom pada sheet LOINC Answer List.

   - **LoincNumber**  
     Tipe: *Text*  
     Kolom pertama (A), Kode LOINC merupakan nomor unik terstandar yang mengidentifikasi pemeriksaan laboratorium. Terdiri atas 3-7 digit dengan format xxxxxx-x.
   - **LongCommonName**  
     Tipe: *Text*  
     Kolom kedua (B), LOINC Long Common Name merupakan penamaan pemeriksaan laboratorium yang distandarkan oleh LOINC yang disarankan dan dipergunakan untuk pertukaran data melalui FHIR.
   - **AnswerListId**  
     Tipe: *Text*  
     Kolom ketiga ©, pengenal unik (kode) untuk setiap kelompok daftar jawaban LOINC yang dimulai dengan awalan "LL".
   - **AnswerListName**  
     Tipe: *Text*  
     Kolom keempat (D), nama dari daftar jawaban LOINC
   - **AnswerListLinkType**  
     Tipe: *Text*  
     Kolom kelima (E), tipe hubungan antara kode LOINC dengan daftar jawaban yang telah disediakan oleh LOINC yaitu *Preferred* atau *Example*.
   - **AnswerStringId**  
     Tipe: *Text*  
     Kolom keenam (F), pengenal unik (kode) untuk jawaban LOINC yang dimulai dengan awalan "LA". Kode ini yang digunakan dalam pertukaran data melalui FHIR pada elemen coding.code.
   - **SequenceNumber**  
     Tipe: *Text*  
     Kolom ketujuh (G), urutan di mana jawaban muncul di daftar jawaban
   - **DisplayText**  
     Tipe: *Text*  
     Kolom kedelapan (H), jawaban dalam bentuk string/teks. Teks ini yang digunakan dalam pertukaran data melalui FHIR pada elemen coding.display.
   - **Code System**  
     Tipe: *Text*  
     Kolom kesembilan (I), URL dari LOINC yang digunakan dalam pertukaran data melalui FHIR pada elemen coding.system.

## Prosedur untuk Kode LOINC yang tidak ditemukan

Apabila terdapat kode yang belum tersedia pada master data LOINC yang digunakan pada SATUSEHAT silakan melakukan permintaan kepada Kementerian Kesehatan melalui formulir permintaan yang dapat di *download* di [**Lampiran LOINC Laboratorium**](https://s.kemkes.go.id/LampiranLOINC-Lab) dengan menekan tombol *“Request”*. Kirimkan formulir tersebut kepada tim kementerian kesehatan melalui *email* [[email protected]](/cdn-cgi/l/email-protection#acc5c4dfecc8d8c382c7c9c1c7c9df82cbc382c5c8) dengan subjek “Permintaan Terminologi Laboratorium”. Pada formulir permintaan terdapat dua bagian utama yaitu data kontak *requester* dan terminologi berikut merupakan cara pengisian formulir permintaan kode LOINC:

![Tabel Terminologi Laboratorium](../../_images/loinc-laboratory-06.png)

Gambar 5. Tampilan Bagian Data Kontak pada Formulir Permintaan Kode LOINC

![Tabel Terminologi Laboratorium](../../_images/loinc-laboratory-07.png)

Gambar 6. Tampilan Bagian Data Terminologi pada Formulir Permintaan Kode LOINC

1. Data kontak

   - **No. HP**  
     Silahkan isi dengan membubuhkan nomor HP aktif *requester* (petugas yang melakukan permintaan terminologi laboratorium).
   - **E-mail**  
     Silahkan isi dengan membubuhkan *email* aktif *requester* (petugas yang melakukan permintaan terminologi laboratorium).
   - **Nama Lengkap**  
     Silahkan isi dengan membubuhkan nama lengkap *requester* (petugas yang melakukan permintaan terminologi laboratorium).
   - **Nama Instansi**  
     Silahkan isi dengan nama instansi di mana *requester* (petugas yang melakukan permintaan terminologi laboratorium) bekerja.
   - **Tipe Instansi**  
     Silahkan pilih tipe instansi di mana *requester* (petugas yang melakukan permintaan terminologi laboratorium) bekerja. Adapun tipe instansi tersebut antara lain:

     1. Rumah Sakit
     2. Apotik / Farmasi
     3. Laboratorium
     4. Puskesmas
     5. Posyandu
     6. Klinik
     7. Tempat praktik mandiri Tenaga Kesehatan
     8. Industri kesehatan/digital kesehatan (*Health-tech*)
     9. Industri farmasi/alat kesehatan
     10. Akademik
     11. Media
     12. Asosiasi
     13. Others
   - **Apakah Anda tergabung dalam asosiasi / ikatan profesi tertentu (misal: Ikatan Dokter Indonesia, Ikatan Bidan Indonesia, dll.)?**  
     Silahkan isi dengan ya atau tidak.
2. Terminologi

   - **No**  
     Silakan isi dengan nomor urut parameter laboratorium yang diminta.
   - **Kategori Pemeriksaan**  
     Silahkan isi dengan kategori/kelompok pemeriksaan laboratorium yang ingin diminta, sebagai contoh: Kimia Klinik, Hematologi, Imunoserologi, dll.
   - **Nama Pemeriksaan**  
     Silahkan isi dengan nama pemeriksaan laboratorium yang ingin diminta.
   - **Deskripsi Pemeriksaan**  
     Silahkan isi dengan penjelasan singkat mengenai pemeriksaan laboratorium yang ingin diminta.
   - **Reference info/URL**  
     Silahkan isi dengan referensi atau URL (link) informasi mendetail mengenai pemeriksaan laboratorium yang ingin diminta.
   - **Permintaan/Hasil**  
     Silakan isi dengan tiga pilihan di bawah ini:

     1. Permintaan: mewakili pemesanan pemeriksaan laboratorium (*order*).
     2. Hasil: mewakili hasil uji atau observasi sebuah spesimen (*observation*).
     3. Permintaan & Hasil: mewakili pemesanan pemeriksaan dan hasil uji/observasi sebuah spesimen.
   - **Spesimen**  
     Silakan isi dengan spesimen yang diuji pada pemeriksaan laboratorium yang ingin diminta.
   - **Tipe Hasil Pemeriksaan**  
     Silakan pilih tipe hasil pemeriksaan pada pemeriksaan laboratorium yang ingin diminta. Adapun pilihannya antara lain: Narrative, Nominal, Ordinal, OrdQn dan Quantitative
   - **Satuan Hasil Pemeriksaan**  
     Silakan isi dengan satuan hasil pemeriksaan pada pemeriksaan laboratorium yang ingin diminta. Sebagai contoh: mg/dl, sel/mcL, dll.
   - **Metode Analisis**  
     Silakan isi dengan teknik apa yang digunakan dalam mengukur, menguji atau mengobservasi sebuah spesimen pada pemeriksaan laboratorium. Sebagai contoh: manual, otomatis,dll.

## Frequently Asked Questions (FAQ)

### LOINC Secara Umum

1. **Apakah ada translasi LOINC?**  
   Kementerian kesehatan tidak melakukan translasi LOINC, namun kami membantu melakukan pemetaan antara parameter laboratorium di Indonesia kedalam standar internasional LOINC.
2. **Apakah LOINC berbayar?**  
   Untuk saat ini terminologi LOINC gratis tidak dipungut biaya apapun
3. **Kapan terminologi LOINC akan diperbaharui?**  
   Pembaruan terminologi LOINC akan dilakukan setiap 6 bulan sekali

### Tata Cara Pemetaan LOINC

1. **Bagaimana jika kode LOINC tidak ditemukan?**  
   Jika kode LOINC tidak ditemukan silakan tanyakan kendala anda ke tim DTO melalui *email* [[email protected]](/cdn-cgi/l/email-protection#f49d9c87b490809bda9f91999f9187da939bda9d90) atau silakan buat copy dan isi formulir permintaan terminologi laboratorium dari template: [link](https://docs.google.com/spreadsheets/d/1vezxU-866WM8X_Rd9sQdjFKqstQP9pvvdxSdFaS_wNU/edit#gid=4721809) berikut kemudian kirimkan melalui *email* ke [[email protected]](/cdn-cgi/l/email-protection#432a2b300327372c6d28262e2826306d242c6d2a27) dengan subjek “Permintaan Terminologi Laboratorium
2. **Kapan kita menggunakan kode LOINC yang tidak terdapat metode pemeriksaannya?**  
   Anda dapat menggunakan kode LOINC tanpa metode pemeriksaan jika anda tidak memiliki cukup informasi terkait metode yang digunakan dalam pemeriksaan laboratorium tersebut atau LOINC hanya menyediakan kode yang tidak menspesifikkan metode pemeriksaannya.
3. **Bagaimana jika saya memiliki pemeriksaan yang hanya berlaku sebagai permintaan, hanya hasil, atau dapat digunakan sebagai pemeriksaan dan hasil?**  
   Jika parameter laboratorium yang dipetakan memiliki kode LOINC dengan tipe “hasil” , maka silakan cari hasil pemetaan dengan kode LOINC maupun kode penunjang nasional dengan klasifikasi “permintaan” Hal ini berlaku sebaliknya.

### Keterkaitan LOINC dengan Standar Terminologi Lain

1. **Bagaimana perbedaan LOINC dengan ICD 10?**  
   ICD-10 digunakan sebagai standar terminologi untuk penyakit sedangkan LOINC merupakan standar terminologi untuk observasi dan pengujian pada laboratorium.
2. **Bagaimana perbedaan LOINC dengan SNOMED CT?**  
   SNOMED CT adalah standar internasional terkait terminologi klinis yang luas dan komprehensif yang mencakup data klinis untuk penyakit, temuan klinis, dan prosedur. Dalam proses pertukaran data laboratorium, LOINC menyediakan terminologi untuk pertanyaan observasi/uji sedangkan SNOMED CT menyediakan jawaban atau hasil dari pemeriksaan laboratorium
3. **Bagaimana perbedaan LOINC dengan ICD-9 CM?**  
   ICD-9 CM digunakan sebagai standar terminologi untuk prosedur klinis dan khususnya untuk proses *billing*/pembiayaan sedangkan LOINC merupakan standar terminologi untuk permintaan dan pelaporan hasil pemeriksaan laboratorium.

### Tata Cara Melakukan Permohonan Pemetaan Kode LOINC

1. **Berapa lama waktu yang dibutuhkan hingga parameter yang diminta tersedia di terminologi *browser* LOINC?**  
   Parameter yang diminta akan diproses selama kurang lebih 1 bulan hingga tersedia di terminologi *browser* LOINC

## Unduh Dokumen LOINC Laboratorium v1.0

[Unduh](https://drive.google.com/u/0/uc?id=1365zfiuu8J6MK-HJjkdX3ewlOpAWHiMJ&export=download) [Unduh Dokumen Lainnya](https://s.kemkes.go.id/LOINCLaboratorium1o0)

## Unduh Dokumen LOINC Laboratorium v1.1

[Unduh](https://drive.google.com/u/0/uc?id=1NMpZ3NuzsrCtK2onOYXxlQ4OmUEi5KTi&export=download) [Unduh Dokumen Lainnya](https://s.kemkes.go.id/LOINCLaboratoriumv1o1)

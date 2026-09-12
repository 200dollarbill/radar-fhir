---
id: term-loinc
title: LOINC
source_url: https://satusehat.kemkes.go.id/platform/docs/id/terminology/loinc/
group: satusehat
fhir_version: R4
fetched_at: '2026-09-11T13:21:34Z'
sha256: cd6ccdd71a6b399a3fc0bee6f3d1d98c1b63717d23a30992099b04409fcaaff2
---
# LOINC

## Apa itu LOINC?

LOINC merupakan standar internasional yang diprakarsai oleh Regenstrief pada tahun 1994 untuk mengidentifikasi pemeriksaan radiologi, dokumen, survei, dll., sehingga memudahkan pemahaman kode karena terdiri dari sekelompok identifikasi, nama, dan kode untuk mengidentifikasi pengukuran kondisi, observasi, dan dokumen kesehatan.

Regenstrief membuat LOINC untuk memfasilitasi pengiriman data klinis secara elektronik dari radiologi dan produsen data lainnya ke rumah sakit, dan payer yang menggunakan data tersebut untuk perawatan klinis dan tujuan pengelolaan manajemen. Selain itu, LOINC juga dibuat untuk memfasilitasi pertukaran data radiologi sesuai standar HL7. Kini LOINC telah digunakan di berbagai institusi baik di institusi klinis, fasilitas pelayanan kesehatan, sistem kesehatan serta mitra IT , penelitian, lembaga pemerintahan, dan proyek *e-Health* skala internasional.

LOINC digunakan di lebih dari 170 negara dengan pengguna sebanyak 44000 di dunia. LOINC juga telah dijadikan sebagai standar resmi nasional di kurang lebih 30 negara dan dipergunakan untuk pertukaran data kesehatan di beberapa negara seperti Hong Kong, Italia, Spanyol, Korea, dsb. Tersedia LOINC adopsi internasional dalam bentuk translasi LOINC ke dalam 12 bahasa yaitu Bahasa Inggris, China, Korea, Portugis, Rusia, Spanyol, German, Turki, Perancis, Belanda, dll., sehingga memungkinkan data terkait pemeriksaan radiologi dapat dipertukarkan skala internasional.

Terdapat 4 kategori utama pada LOINC yaitu:

- radiologi,
- klinis,
- HIPAA *attachment*, dan
- *Standardized survey instrument*.

Ruang lingkup LOINC laboratorium mencakup apapun yang dapat diuji dan diukur serta amati terkait suatu spesimen. Ruang lingkup ini berisikan semua kategori seperti terapi antiretroviral, patologi molekuler, translokasi, hematologi dan perhitungan sel, antigen HLA, kimia, mikrobiologi (parasitologi dan virologi), serologi, urianalisis, informasi spesimen, dosis obat, toksikologi obat, etc.

Ruang lingkup untuk LOINC klinis mencakup pemeriksaan penunjang selain radiologi, pemeriksaan apapun yang bertujuan untuk menguji, mengukur dan mengamati pasien tanpa adanya pengambilan spesimen dari pasien. Ruang lingkup ini meliputi radiologi, registri tumor, pemeriksaan tanda-tanda vital, EKG, USG, patient safety, pencitraan urologi, gastroendoscopy, dll.

## Struktur Kode LOINC

Terminologi LOINC terdiri atas kode LOINC dan nama/ istilah LOINC. LOINC terdiri atas lebih dari 90.000 kode dalam format numerik (angka). Struktur kode LOINC terdiri dari 3 hingga 7 karakter dengan digit terakhir yang disebut *check* digit dan selalu terletak setelah tanda penghubung. *Check* digit selalu berupa angka 0-9 yang berfungsi untuk membantu menghindari kesalahan dalam transkripsi kode. Tanda penghubung dan seluruh angka merupakan bagian dari kode LOINC, struktur kode LOINC dapat dilihat pada gambar berikut:

![Struktur kode](../_images/loinc-radiologi-01.png)

Gambar 1. Struktur Kode LOINC

Setiap kode pada LOINC merepresentasikan sebuah istilah/ nama pemeriksaan radiologi (*display*). Kode LOINC tersebut dapat disajikan dalam 3 bentuk penamaan sesuai dengan aturan LOINC yaitu:

1. **Fully Specified Name (FSN)**

   Nama formal, terdiri dari 6 komponen LOINC antara lain analyte, property, time, system, scale, method yang kemudian akan dibahas pada bagian 4. Contoh:

   - Leukocytes: NCnc: Pt: CSF: Qn: Manual count
   - View AP: Find: Pt: Lower extremity > Femur: Doc: XR
2. **Long Common Name (LCN)**

   Nama yang lebih familiar oleh klinisi. Merupakan bentuk penamaan yang direkomendasikan untuk pertukaran data dan kamus data. Contoh:

   - XR Femur AP.
   - Leukocytes [#/volume] in Cerebral spinal fluid by Manual count.
3. **Short Name**

   Alternatif nama singkat yang biasa digunakan untuk header kolom. Namun tidak semua kode LOINC memiliki *short name*. Setiap kode LOINC memiliki FSN dan LCN namun 8000 diantaranya tidak terdapat *short name*. *Short name* kurang dianjurkan karena terdapat beberapa nama yang sama (non unique) untuk pemeriksaan kombinasi radiologi, studi analit multiple, dll. Hal ini terjadi karena short name memiliki batasan maksimal 40 karakter. Contoh: WBC # CSF Manual dan XR Femur AP.

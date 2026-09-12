---
id: term-snomed-ct
title: SNOMED-CT
source_url: https://satusehat.kemkes.go.id/platform/docs/id/terminology/snomed-ct/
group: satusehat
fhir_version: R4
fetched_at: '2026-09-11T13:21:37Z'
sha256: e1179f5105428a64025ea6348a8f993175e3f96e883a391a779ce4f3f393ea21
---
# SNOMED-CT

## Apa itu SNOMED-CT?

**SNOMED-CT** merupakan standar terminologi internasional terkait istilah klinik yang dikeluarkan oleh SNOMED International. Terminologi di SNOMED-CT merupakan standar terminologi klinis yang paling komprehensif dan dapat membantu untuk merepresentasikan konten klinis secara konsisten dalam sistem informasi kesehatan. Saat ini SNOMED-CT sudah digunakan di 44 negara secara nasional antara lain Amerika Serikat, Inggris, Australia, Singapore dan Malaysia serta *Affiliate Licenses* ke lebih dari 30.000 individu dan organisasi.

Ruang lingkup terminologi yang disediakan dari SNOMED-CT yaitu terkait temuan klinis (diagnosis, hasil pemeriksaan), struktur tubuh, nama organisme, prosedur/tindakan medis, konteks sosial, jenis zat aktif, obat, objek fisik, dan sebagainya. Dengan kelengkapan terminologi yang disediakan, SNOMED-CT dapat dipetakan ke standar internasional lain yaitu ICD-10, ICD-O, ICD-9 CM. SNOMED-CT mengakomodasi penambahan terminologi yang tersedia spesifik di konteks lokal, translasi ke bahasa lokal, dan akan selalu diperbaharui setiap tahunnya. Lisensi SNOMED-CT yang didapatkan oleh Kementerian Kesehatan dapat digunakan oleh seluruh fasilitas pelayanan kesehatan di Indonesia untuk bertukar data kesehatan di dalam SATUSEHAT Platform (SSP).

## Komponen SNOMED-CT

Setelah mengetahui ruang lingkup dari SNOMED-CT melalui ke 19 *top level concept*, pondasi istilah klinis SNOMED-CT haruslah diketahui yang merupakan detail dari 19 *top level concept*. Konten komponen dari pondasi tersebut adalah

### Concept

*Concept* merupakan komponen sentral dari ide klinis yang diasosiasikan dengan pengenal khusus SCTID. Penjelasan dari ide klinis ini dihubungkan secara spesifik dan permanen yang dinamakan *Fully Specified Name* (FSN). Tanda pengenal khusus ini (SCTID) memiliki 18 digit dan berguna dalam mengidentifikasi *Concept* itu sendiri dengan *Concept* lain. *Concept* juga mengalami versioning atau pembaharuan yang mana mempengaruhi status *Concept* baik *active* maupun *inactive*.

### Description

*Description* adalah istilah penghubung *Concept* yang dapat dimengerti manusia dan setiap *Concept* biasanya diasosiasikan dengan beberapa *description*. Layaknya *concept*, *description* juga memiliki identifikasi pengenal khusus SCTID khusus *description* dan *description* mengalami versioning. Dikarenakan memiliki fungsi sebagai penghubung *Concept*, istilah FSN dan *Synonym* merupakan bagian dari *description*. FSN sudah dijelaskan sebelumnya dan *Synonym* merupakan istilah frasa kata yang umum di dunia klinisi/kesehatan yang digunakan untuk *Concept* dan pada penggunaan langsungnya digunakan saat pencarian, pemilihan dan memperlihatkan tampilan. *description* tiap *Concept* memang unik dan berbeda terutama dengan bahasa yang berbeda. Pada bahasa SNOMED-CT International yang menggunakan bahasa inggris memiliki FSN dan *synonym* yang berbeda dengan bahasa Indonesia. Oleh karenanya, dalam penampilan FSN dan *synonym* ada istilah khusus diluar *description* yang dinamakan preferred dan acceptable. Istilah preferred digunakan untuk menentukan *synonym* mana yang secara arti default dengan FSN nya, sedangkan acceptable digunakan untuk *synonym* selain default *synonym* yang secara arti masih dapat disamakan dengan FSN. Kedua istilah ini berbeda setiap kata nya di dalam bahasa yang berbeda.

### Relationship

*Relationship* adalah istilah yang digunakan untuk mengasosiasikan antar *concept* yang memiliki makna salah satu atau kedua makna ini: apakah satu *Concept* merupakan subtipe dari *Concept* lain atau suatu *Concept* merupakan atribut khusus yang dimiliki dari *Concept* lain. Sebagai contoh, appendectomy merupakan subtipe dari procedure dan appendectomy memiliki procedure site di appendix. Penghubung ini dapat terjadi secara bersamaan atau secara sendiri-sendiri. Istilah penghubung lain yang ada SNOMED-CT sebagai contoh:

- *Relationship* *“necessarily true”*: merupakan istilah yang pasti ada dan masuk akal apabila tidak ada, sebagai contoh: *Appendectomy* adalah prosedur yang hanya terjadi di appendix, prosedur lain di appendix hanya appendectomy.
- Istilah *defined*: merupakan istilah apabila suatu *Concept* memiliki penghubung yang sudah mencukupi dalam menjelaskan dan mendefinisikan *Concept* nya
- Istilah *primitive*: merupakan istilah apabila suatu *Concept* memiliki penghubung yang tidak mencukupi dalam menjelaskan dan menjelaskan *Concept* nya

Layaknya *concept* dan *description*, *relationship* memiliki pengenal khusus \* SCTID, melakukan *versioninig*, memiliki ID *source* khusus apabila digunakan sebagai *source* *concept* atau memiliki ID destination khusus apabila digunakan sebagai destination *concept*.

### Hirarki

Setelah mengetahui ketiga pondasi dari SNOMED-CT, pengenalan selanjutnya adalah *Concept* hirarki. Polihirarki yang dianut SNOMED-CT memiliki root *concept* dengan 19 *top level concepts* dan diteruskan setiap *top level concept* memiliki subtipe lanjutan seperti gambar di bawah ini:

![dashboard](../_images/snomed-ct-01.png)

Gambar 1. Concept Model SNOMED-CT

Seperti yang sudah diketahui mengenai *relationship* antar *Concept* baik subtipe maupun secara khusus, ada istilah *domain* dan *range*. Istilah ini digunakan secara spesifik pada 10 *top level concepts* yakni:

1. Clinical finding
2. Procedure
3. Situation with explicit context
4. Event
5. Observable entity
6. Pharmaceutical / biologic product
7. Physical object
8. Body structure
9. Specimen
10. Substance

Ke-10 *top level concepts* me-*restriction* *domain*, *range* dan *attribute* nya. Istilah ini diartikan sebagai:

- *Domain*: hirarki di mana atribut terpilih dapat diaplikasikan dan dibolehkannya *concept* untuk *relationship* tertentu.
- *Range*: set of *concept* di mana diperbolehkan sebagai value oleh atribut dan mengatur destination *concept* untuk tipe *relationship* tertentu

![dashboard](../_images/snomed-ct-02.png)

Gambar 2. Level Concept

Selain itu, diagram dapat digunakan untuk menjelaskan maksud dari sebuah *concept* dan *relationship* melalui *concept* model diagram. Berikut diagramnya:

1. *Defined Concept diagram:*

   ![dashboard](../_images/snomed-ct-03.png)

   Gambar 3. Defined Concept Diagram

   Pada gambar di atas kita dapat melihat bahwa suatu Concept pneumonitis memiliki beberapa *relationship* dan memiliki *relationship* group yang mana kedua hal ini dapat menjelaskan pneumonitis sehingga dikatakan defined.
2. *Primitive Concept Diagram:*

   ![dashboard](../_images/snomed-ct-04.png)

   Gambar 4. Primitive Concept Diagram

   Pada gambar di atas dapat kita lihat bahwa *concept* dengan *relationship* nya tidak dapat menjelaskan secara detail \_concept\_nya sehingga dikatakan sebagai primitive.

### Identifiers dan Data Types

Setelah mengetahui 3 pondasi utama SNOMED-CT dan hirarki, pengenalan mengenai *identifiers* dan data types, berikut penjelasannya:

1. *Identifiers* (SCTID): atau SNOMED-CT *Identifiers* merupakan tipe data yang digunakan untuk identifikasi suatu komponen baik *concept*, *description* maupun *relationship*. Karakter SCTID adalah memiliki digit 6-18 digit, ada versi pendek maupun panjang, tidak memiliki makna digitnya dan memiliki komponen metadata.
2. Versi pendek: terbagi atas item *identifiers*, *partition identifiers* dan *check digit*.

![dashboard](../_images/snomed-ct-05.png)

Gambar 5. Indtifiers Versi Pendek

1. Versi panjang: terbagi atas item *identifiers*, *namespace identifiers*, partition *identifiers* dan *check digit*.

![dashboard](../_images/snomed-ct-06.png)

Gambar 6. Indtifiers Versi Panjang

1. Istilah penjabaran:

   1. *Item identifiers*: digunakan untuk identifikasi *individual entity*
   2. *Namespace identifiers*: digunakan untuk merepresentasikan ke organisasi yang berhak menciptakan kode SCTID
   3. *Partition identifiers*:

      - Versi pendek: 00 *concept*, 01 *description*, 02 *relationship*
      - Versi panjang: 10 *concept*, 11 *description*, 12 *relationship*
   4. *Check digit*: digunakan untuk verifikasi validasi SCTID dan menggunakan Verhoeff check
2. *Time:* adalah tipe data yang digunakan untuk menjelaskan waktu yang menganut format ISO 8601 *basic*. Penulisan Time ini berformat tahun-bulan-hari (YYYYMMDD)
3. *Boolean:* adalah tipe data yang digunakan dengan mengimpresentasikan 1 sebagai true atau 0 sebagai false
4. *String:* adalah tipe data yang digunakan di SNOMED-CT dan menganut *UTF-8 text* sistem penulisan.
5. *Integer:* adalah tipe data yang digunakan di SNOMED-CT dan menganut *32-bit signed integer*.

### Logical Model

Setelah mengetahui pondasi, hirarki dan tipe data SNOMED-CT, penjelasan secara luas adalah SNOMED-CT menganut *logical model*. *Logical model* adalah *overview* konten komponen SNOMED-CT yang mana sebuah *concept* bertautan dengan *description*, *relationship* dan *concept*.

![dashboard](../_images/snomed-ct-07.png)

Gambar 7. Component Concet Hirarki dan tipe data SNOMED-CT

Pada gambar di atas kita dapat melihat hubungan *concept* dengan *concept*, *relationship* dan *description* dan secara mendasar atribut *concept* dimiliki *concept*, *relationship* dan *description*.

![dashboard](../_images/snomed-ct-08.png)

Gambar 8. Component Concept yang berhubungan concept dengan concept, relationship dan description

Pada gambar di atas kita dapat melihat bahwa tulisan berwarna merah merupakan atribut dan tulisan berwarna biru merupakan tipe datanya. Kita dapat melihat perbedaan atribut bawaan *description*, *concept*, *relationship* yang mana merupakan ciri khas dalam penjelasan di release *file*. Penjelasan dan penggunaan atribut dan *reference set* akan dijelaskan lebih dalam di bab Spesifikasi File.

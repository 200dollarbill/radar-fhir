---
id: term-index
title: Terminologi
source_url: https://satusehat.kemkes.go.id/platform/docs/id/terminology/
group: satusehat
fhir_version: R4
fetched_at: '2026-09-11T13:21:31Z'
sha256: deac7ed46e08f585c4df13aa8f69f6c1f64707de65baa961bdbfab9ba1345382
---
# Terminologi

SATUSEHAT merupakan platform interoperabilitas data kesehatan. Interoperabilitas memungkinkan informasi kesehatan dipertukarkan sewaktu-waktu, antara tenaga medis yang berbeda, entitas lain yang berwenang, dan pasien, dalam kondisi aman, rahasia serta perlindungan data lainnya. SATUSEHAT menggunakan standar HL7 FHIR dalam pertukaran datanya. Dalam melakukan pertukaran HL7 FHIR bekerja seperti *grammar* dalam sebuah pembelajaran bahasa, oleh karenanya diperlukan *vocabulary* yang mendukung. Berikut ini standar terminologi yang digunakan pada SATUSEHAT Platform (SSP):

## [ICD-10](icd/icd-10/#icd-10)

**ICD-10** adalah Klasifikasi Statistik Internasional Tentang Penyakit dan Masalah Kesehatan Revisi ke 10 atau the 10th revision of the *International Statistical Classification of Diseases and Related Health Problems* (ICD). ICD-10 adalah daftar klasifikasi medis yang dikeluarkan oleh WHO.

|  |  |
| --- | --- |
|  | ICD-10 didalam interoperabilitas SATUSEHAT Platform (SSP) digunakan sebagai **standar diagnosis** |

|  |  |
| --- | --- |
|  | SATUSEHAT Platform (SSP) menggunakan **ICD-10 versi 2010** |

## [ICD-9 CM](icd/icd-9-cm/#icd-9-cm)

**ICD-9 CM** adalah Klasifikasi dan Kodefikasi Prosedur Internasional Revisi ke 9 Modifikasi Klinis atau *International Classification of Procedure Code*, *9th Revision*, *Clinical Modification* (ICD-9 CM). ICD-9 CM adalah standar untuk penamaan prosedur dan tindakan medis yang dikeluarkan oleh WHO.

|  |  |
| --- | --- |
|  | ICD-9 CM didalam interoperabilitas SATUSEHAT Platform (SSP) digunakan sebagai **standar penamaan prosedur & tindakan medis** |

|  |  |
| --- | --- |
|  | SATUSEHAT Platform (SSP) menggunakan **ICD-9 CM versi 2010** |

## [ICD-O](icd/icd-o/#icd-o)

**ICD-O** adalah Klasifikasi Statistik Internasional Tentang Penyakit dan Masalah Kesehatan yang dikhususkan untuk neoplasma/kanker. ICD-O adalah daftar klasifikasi medis yang dikeluarkan oleh WHO, yang digunakan sebagai standar pengkodean lokasi dan histologi pada neoplasma.

|  |  |
| --- | --- |
|  | ICD-O didalam interoperabilitas SATUSEHAT Platform (SSP) digunakan sebagai **standar pengkodean neoplasma/kanker** |

|  |  |
| --- | --- |
|  | SATUSEHAT Platform (SSP) menggunakan **ICD-O versi 3.2 tahun 2019** |

## [ICD-MM](icd/icd-mm/#icd-mm)

**ICD-MM** adalah Klasifikasi Statistik Internasional Tentang Penyakit dan Masalah Kesehatan yang didasarkan pada aturan pengkodean ICD-10 yang dikeluarkan oleh WHO untuk melakukan identifikasi pada kematian selama masa kehamilan, persalinan, dan masa nifas.

|  |  |
| --- | --- |
|  | ICD-MM didalam interoperabilitas SATUSEHAT Platform (SSP) digunakan untuk **melakukan identifikasi kematian ibu** |

|  |  |
| --- | --- |
|  | SATUSEHAT Platform (SSP) menggunakan **ICD-MM versi 2012** |

## [ICD-PM](icd/icd-pm/#icd-pm)

**ICD-PM** adalah Klasifikasi Statistik Internasional Tentang Penyakit dan Masalah Kesehatan untuk melakukan identifikasi pada kematian selama periode perinatal, yang didasarkan pada aturan pengkodean ICD-10 yang dikeluarkan oleh WHO dan dimodelkan seperti yang ada pada ICD-MM.

|  |  |
| --- | --- |
|  | ICD-PM didalam interoperabilitas SATUSEHAT Platform (SSP) digunakan untuk **melakukan identifikasi kematian perinatal** |

|  |  |
| --- | --- |
|  | SATUSEHAT Platform (SSP) menggunakan **ICD-PM versi 2016** |

## [LOINC](loinc/#loinc)

*Logical Observation Identifiers Name and Codes* (**LOINC**) adalah database dan standar universal untuk mengidentifikasi pengamatan laboratorium medis. Memudahkan pemahaman kode karena terdiri dari sekelompok identifikasi, nama, dan kode untuk mengidentifikasi pengukuran kondisi, observasi, dan dokumen kesehatan.

|  |  |
| --- | --- |
|  | LOINC didalam interoperabilitas SATUSEHAT Platform (SSP) digunakan sebagai **standar penamaan uji laboratorium** |

## [SNOMED-CT](snomed-ct/#snomed)

SNOMED Clinical Terms (**SNOMED-CT**) adalah sebuah sistem yang menyediakan kosakata komprehensif konsep medis, termasuk kondisi medis dan anatomi, serta tes medis, perawatan, dan prosedur.

|  |  |
| --- | --- |
|  | SNOMED-CT didalam interoperabilitas SATUSEHAT Platform (SSP) digunakan sebagai **standar penamaan istilah klinis** |

## [Kode Pembiayaan Tindakan dan Layanan Kesehatan Nasional (KPTL)](kptl/#kptl)

Kode Pembiayaan Tindakan dan Layanan Kesehatan Nasional (KPTL) merupakan terminologi yang disusun dengan mengumpulkan dan memperinci terminologi tindakan yang selama ini terbatas menunjuk kepada konsep klinis saja namun mengabaikan informasi dan variasi-variasi tindakan yang berbeda dalam sudut pandang biaya.

## Lampiran Terminologi

Dokumen Lampiran Terminologi adalah dokumen yang berisi daftar terminologi yang dapat digunakan dalam proses integrasi SATUSEHAT pada setiap pelayanan dan *use case* sesuai standar HL7 FHIR. Dokumentasi ini dibagi menjadi beberapa bagian yang terdiri dari:

### 1. [Resume Medis - Rawat Jalan](lampiran-terminologi/rme-rawat-jalan1/)

### 2. [Pelayanan Instalasi Gawat Darurat (IGD)](lampiran-terminologi/igd-fase-2/)

### 3. [Rawat Inap](lampiran-terminologi/rawat-inap-fase-2/)

### 4. [Antenatal Care](lampiran-terminologi/anc/)

### 5. [Data Kelahiran](lampiran-terminologi/data-kelahiran/)

### 6. [Intranatal Care](lampiran-terminologi/inc/)

### 7. [Postnatal Care](lampiran-terminologi/pnc/)

### 8. [Gigi](lampiran-terminologi/rawat-jalan-gigi/)

### 9. [Gizi](lampiran-terminologi/gizi/)

### 10. [Imunisasi](lampiran-terminologi/imunisasi-new/)

### 11. [Imunisasi COVID-19](lampiran-terminologi/imunisasi-covid/)

### 12. [Neonatus](lampiran-terminologi/neonatus-prio/)

### 13. [Kematian Maternal dan Perinatal (Faskes)](lampiran-terminologi/mpdn/)

### 14. [Manajemen Terpadu Balita Sakit](lampiran-terminologi/mtbs/)

### 15. [Pelayanan Kefarmasian](lampiran-terminologi/farmasi/)

### 16. [Pelayanan Kesehatan Peduli Remaja (PKPR) Luar Gedung](lampiran-terminologi/pkpr-luar-gedung/)

### 17. [Pembiayaan Kesehatan Klaim Asuransi Swasta/Non BPJS](lampiran-terminologi/klaim/)

### 18. [Registrasi Kanker](lampiran-terminologi/kanker/)

### 19. [Registrasi Stroke](lampiran-terminologi/registrasi-stroke/)

### 20. [Rujukan Spesimen](lampiran-terminologi/rujukan-spesimen/)

### 21. [Skrining Penyakit Tidak Menular (PTM)](lampiran-terminologi/skrining-ptm/)

### 22. [Tuberkulosis](lampiran-terminologi/tuberkulosis/)

## [Standar Terminologi](standar-terminologi/#standar-terminologi)

Dokumen Standar Terminologi adalah dokumen yang memberikan daftar terminologi yang dapat digunakan dalam proses integrasi SATUSEHAT. Dokumen ini akan memberikan daftar terminologi pada setiap elemen FHIR *resource*.

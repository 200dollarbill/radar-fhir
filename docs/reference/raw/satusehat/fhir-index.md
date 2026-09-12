---
id: fhir-index
title: FHIR
source_url: https://satusehat.kemkes.go.id/platform/docs/id/fhir/
group: satusehat
fhir_version: R4
fetched_at: '2026-09-11T13:20:30Z'
sha256: 23c12beda8177055d239836cecc5186bd7b2b4047780598f503ef994cd464f4e
---
# FHIR

**SATUSEHAT** menggunakan **HL7** FHIR dalam pengimplementasian standar data model dan Application Programming Interface (API).

*Fast Healthcare Interoperability Resources* FHIR adalah sebuah standar global (internasional) yang menetapkan format data beserta elemen-elemennya (yang disebut "*resources*") dan sebuah standar antarmuka pemrograman aplikasi (API/*Application Programming Interface*) untuk pertukaran informasi (interoperabilitas SATUSEHAT) yang pada penerapannya akan dibagi-bagi lagi menjadi beberapa alur proses sesuai penggunaannya (*use case*) baik *use case* dasar maupun *use case* tematik. FHIR dibaca “*fire*” dalam bahasa Inggris (/faier/).

Standar ini dibuat oleh *Health Level Seven International* (HL7), yaitu sebuah organisasi standar pelayanan kesehatan (*healthcare standards organization*). Situs terkait: <https://www.hl7.org/fhir/>.

Masing-masing pengguna FHIR memiliki profil di mana profil FHIR Indonesia dapat dilihat di sini Simplifier FHIR Profiles.

Akronim FHIR:  
F: Fast  
H: Healthcare  
I: Interoperability  
R: Resources

HL7 FHIR merupakan standar terkini dalam pertukaran data dan informasi kesehatan, telah digunakan di berbagai negara termasuk *World Health Organization* (WHO) dan berbagai fasilitas layanan kesehatan. Menggunakan fitur API yang sudah dikenal oleh pengembang sistem informasi.

Kemudahan pertukaran data akan mengurangi waktu pengaturan interoperabilitas antar sistem dan mendorong perkembangan teknologi yang lebih maju.

|  |  |
| --- | --- |
|  | Silakan klik setiap teks yang berwarna **biru muda**, untuk membaca panduan lebih detail/lanjut ke bagian yang direferensikan. |

## Tipe Data

Penjelasan terkait tipe data pada FHIR , diantaranya:

1. [Primitif](data-type/primitive/);
2. [Umum](data-type/general/);
3. [Metadata](data-type/metadata/);
4. [Khusus](data-type/special/).

## Resources - Prerequisites

Tahap ini disebut tahap persiapan sebelum Anda masuk kedalam proses interoperabilitas lebih dalam (Integrasi) berdasarkan modul pelayanan maupun penerapan (use case) sesuai dengan panduan interoperabilitas. Informasi lebih lengkap silakan klik [**di sini**](prerequisites/#prerequisites).

## Resources - Interoperability (Integrasi)

Setelah resource yang terkait dengan proses orientasi (Prerequisites) terpenuhi, maka tahap selanjutnya adalah interoperabilitas (transaksi data/integrasi), yang pada penerapannya akan dibagi-bagi lagi menjadi beberapa alur proses sesuai penggunaannya (use case) baik use case dasar (Modul Pelayanan) maupun use case tematik (Modul Penerapan). Informasi lebih lengkap silakan klik [**di sini**](resources/#interoperability).

## Framework FHIR

Pada bagian ini akan dijelaskan secara singkat beberapa landasan yang mendefinisikan framework FHIR beserta struktur JSON-nya, yaitu `Element`, `Resource`, `DomainResource`, dan `Bundle`. Informasi lebih lengkap silakan klik [**di sini**](framework/).

---
id: fhir-prerequisites
title: Orientasi/Onboarding/Prerequisites
source_url: https://satusehat.kemkes.go.id/platform/docs/id/fhir/prerequisites/
group: satusehat
fhir_version: R4
fetched_at: '2026-09-11T13:20:34Z'
sha256: 502d503faad939b97e7d770badd48b82106242f5b33d243b37a762685fb7d5c4
---
# Orientasi/*Onboarding*/*Prerequisites*

Tahap ini disebut tahap **persiapan** sebelum Anda masuk kedalam proses interoperabilitas lebih dalam berdasarkan modul pelayanan maupun penerapan (*use case*)

Sebelum melakukan pengiriman data terkait pendaftaran pasien dan diagnosis, terdapat 4 langkah yang perlu dilakukan yaitu:

1. Autentikasi ke SATUSEHAT,
2. Registrasi Struktur Organisasi,
3. Registrasi Struktur Lokasi,
4. Menyimpan Nomor IHS untuk Tenaga Kesehatan.
5. Mendapatkan Nomor IHS Pasien

## Autentikasi

Autentikasi atau pertukaran/transaksi data akan dibahas lebih lanjut [**di sini**](../../api-catalogue/authentication/#auth-fhir)

## Registrasi Struktur Organisasi (`Organization`)

- Informasi terkait pemetaan nilai, penjelasan tipe mandatoris, deskripsi dan format pengisian dari setiap elemen data/*path* di dalam resource `Organization` (data suborganisasi), dapat dilihat [**di sini**](../resources/organization/#organization).
- Dapat dilihat juga pada Postman SATUSEHAT, silakan klik [**di sini**](../../postman-workshop/#postman-collection-satusehat).
- Dokumentasi ReST API SATUSEHAT (Katalog ReST API SATUSEHAT) dapat dilihat [**di sini**](../../api-catalogue/onboardings/apis/organization/).
- Silahkan tonton video tutorial [**di sini**](https://drive.google.com/file/d/1LSQ7yvM9bwT-6oJt80KtCy3hsUlAsD3w/view?usp=drive_link) untuk mendapatkan informasi tambahan terkait **POST** `Organization`.

## Registrasi Struktur Lokasi (`Location`)

- Informasi terkait pemetaan nilai, penjelasan tipe mandatoris, deskripsi dan format pengisian dari setiap elemen data/*path* di dalam resource `Location` (data sublokasi), dapat dilihat [**di sini**](../resources/location/#location).
- Dapat dilihat juga pada Postman SATUSEHAT, silakan klik [**di sini**](../../postman-workshop/#postman-collection-satusehat).
- Dokumentasi ReST API SATUSEHAT (Katalog ReST API SATUSEHAT) dapat dilihat [**di sini**](../../api-catalogue/onboardings/apis/location/).
- Silahkan tonton video tutorial [**di sini**](https://drive.google.com/file/d/1m8TfS5lt1P7nsCUj-3c06DwuhMnKCMZh/view?usp=drive_link) untuk mendapatkan informasi tambahan terkait **POST** `Location`.

## Nomor IHS untuk Tenaga Kesehatan (`Practitioner`)

|  |  |
| --- | --- |
|  | Proses pencarian SATUSEHAT ID dari tenaga kesehatan `{practitioner-ihs-number}` dapat dilakukan melalui FHIR API dengan metode **GET**.  - Penjelasan tipe mandatoris, deskripsi dan format pengisian dari setiap elemen data/path di dalam resource `Practitioner` dapat dilihat [**di sini**](../resources/practitioner/#practitioner). - Dapat dilihat juga pada Postman SATUSEHAT, silakan klik [**di sini**](../../postman-workshop/#postman-collection-satusehat). - Dokumentasi ReST API SATUSEHAT (Katalog ReST API SATUSEHAT) dapat dilihat [**di sini**](../../api-catalogue/onboardings/apis/practitioner/). - Silahkan tonton video tutorial [**di sini**](https://drive.google.com/file/d/1okQ1mmB5-1D_ZMOl0Yr1UdTmwFkC0ssp/view?usp=drive_link) untuk mendapatkan informasi tambahan terkait **GET** `Practitioner`. |

## Nomor IHS Pasien (`Patient`)

Apabila melakukan pengiriman data kesehatan melalui SATUSEHAT yang memiliki elemen data terkait resource [`Patient`](../resources/patient/#patient), maka diperlukan informasi `{patient-ihs-number}` dari pasien yang bersangkutan.

|  |  |
| --- | --- |
|  | Proses pencarian `{patient-ihs-number}` dari resource [`Patient`](../resources/patient/#patient) dapat dilakukan melalui FHIR API dengan metode **GET**.  - Penjelasan tipe mandatoris, deskripsi dan format pengisian dari setiap elemen data/path di dalam resource `Patient` dapat dilihat [**di sini**](../resources/patient/#patient). - Metode pencarian data pasien di SATUSEHAT secara detail dapat dilihat pada panduan/playbook Master Patient Index (MPI), silakan klik [**di sini**](../../master-data/master-patient-index/preliminary/#prem-mpi). - Dapat dilihat juga pada Postman SATUSEHAT, silakan klik [**di sini**](../../postman-workshop/#postman-collection-satusehat). - Dokumentasi ReST API SATUSEHAT (Katalog ReST API SATUSEHAT) dapat dilihat [**di sini**](../../api-catalogue/onboardings/apis/patient/). |

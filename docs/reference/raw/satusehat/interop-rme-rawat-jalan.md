---
id: interop-rme-rawat-jalan
title: Resume Medis - Rawat Jalan
source_url: https://satusehat.kemkes.go.id/platform/docs/id/interoperability/rme-rawat-jalan/
group: satusehat
fhir_version: R4
fetched_at: '2026-09-11T13:21:27Z'
sha256: 9b91f574a19d4d81017f61f84cf58a14bfde4c32cccf1ce609c83aebe0840951
---
# Resume Medis - Rawat Jalan

## Riwayat Perubahan

Details

Tabel 1. Riwayat Perubahanan Resume Medis - Rawat Jalan

| Versi | Tanggal Pembaruan | Deskripsi Perubahan | Penanggung Jawab |
| --- | --- | --- | --- |
| v6.3 | 30 Oktober 2025 | - Penambahan variabel tipe pelayanan pada pendaftaran kunjungan dengan path `Encounter.serviceType.coding`. | Anisatul ‘Afifah |
| v6.2 | 23 Desember 2024 | - Penambahan variabel identitas umum pasien pada tabel Bab C. Integrasi. - Perbaikan path `Encounter.diagnosis.condition` pada Diagnosis Sekunder/Penyerta. - Perubahan narasi terkait `MedicationStatement.medicationReference` pada Ketentuan Pengisian Riwayat Pengobatan. - Perbaikan path `Goal.category.coding`, `Goal.description.coding`, `Goal.outcomeCode.coding`, dan `Goal.target.measure.coding` pada Tujuan Perawatan. - Perbaikan path `Procedure.category.coding` dan terminologi yang digunakan pada Status Puasa pasien. - Perbaikan path `Observation.interpretation.coding.display` pada Interpretasi Hasil Pemeriksaan dan Nilai Normal/ Tidak Normal. - Perbaikan path `Medication.ingredient.itemCodeableConcept.coding` pada tabel contoh pengisian pengiriman data obat. - Perbaikan nomor `QuestionnaireResponse.item.item.linkId` dan penambahan path pada Pengkajian Resep. - Penambahan narasi terkait metode pengiriman Medication secara terpisah sudah tidak bisa digunakan di peresepan dan pengeluaran obat. - Perbaikan path pada `ServiceRequest.locationCode.coding` pada Sarana Transportasi untuk Rujuk. - Perbaikan judul tabel pada pemetaan variabel Bab 15. Pengiriman Data Tindakan/Prosedur Medis. - Penyesuaian penulisan format pengisian referensi pada tabel pemetaan variabel. - Penyesuaian url sistem terminologi <http://loinc.org> pada pemetaan variabel Bab 28. Pengiriman Data Resume Medis | Silvia Alvinia |
| v6.1 | 24 Oktober 2024 | - Penyesuaian skema alur pada Bab C. Integrasi - Penarikan variabel Skor ADL dari Bab 5. Pemeriksaan Fungsional - Penyesuaian deskripsi kode Riwayat Alergi dan Perencanaan Perawatan, dan perubahan kode tipe resume medis pada Bab 28. Pengiriman Data Resume Medis - Perubahan path variabel Jenis Bahan Kontras pada Bab 11. Pengiriman Data Pemeriksaan Penunjang Radiologi - Penyesuaian variabel Tanggal dan Waktu Tindakan serta Farmasi dan Alat Medis yang digunakan pada Bab 15. Pengiriman Data Tindakan/Prosedur Medis - Penyesuaian narasi pada Bab 27. Pembaharuan Data Kunjungan | Silvia Alvinia Anisatul ‘Afifah |
| v6.0 | 27 September 2024 | - Perubahan tahapan alur integrasi, resource FHIR yang digunakan, alur, dan tabel variabel pada Bab C. Integrasi - Penambahan Bab 6. Pengiriman Data Riwayat Perjalanan Penyakit, Bab 7. Pengiriman Data Tujuan Perawatan, Bab 12. Pengiriman Data Rasional Klinis, Bab 14. Pengiriman Data Penilaian Risiko, Bab 19. Pengiriman Data Pemberian Obat, dan Bab 28. Pengiriman Data Resume Medis - Penambahan subbab pemetaan variabel dan terminologi spesifik pada Bab 2. Pendaftaran Kunjungan Pasien, Bab 10. Pengiriman Data Pemeriksaan Penunjang Laboratorium, Bab 11. Pengiriman Data Pemeriksaan Penunjang Radiologi, Bab 16. Pengiriman Data Peresepan Obat, Bab 18. Pengiriman Data Pengeluaran Obat - Pembaharuan variabel dan pemetaan Bab 3. Pengiriman Data Anamnesis - Pembaharuan variabel dan judul Bab 5. Pengiriman Data Pemeriksaan Fungsional - Pembaharuan variabel dan pemetaan Bab 15. Pengiriman Data Tindakan/ Prosedur Medis - Pembaharuan narasi Bab 16. Pengiriman Data Peresepan Obat - Penambahan variabel pada Bab 17. Pengiriman Data Pengkajian Resep - Perubahan resource dan pemetaan pada Bab 20. Pengiriman Data Diet - Pembaharuan ketentuan pada Bab 21. Pengiriman Data Edukasi - Pembaharuan ketentuan pada Bab 22. Pengiriman Data Prognosis | Silvia Alvinia |
| v5.1 | 12 Juni 2024 | - Pembaharuan Alur Integrasi Rawat Jalan : Penambahan Pemeriksaan Psikologis. - Pembaharuan Variabel Pemeriksaan Psikologis dalam Bab 4. Pemeriksaan Fisik menjadi tambahan Bab 5. Pemeriksaan Psikologis - Pembaharuan alur dan narasi untuk pengiriman radiologi Pembaharuan narasi terkait Ketentuan pengiriman permintaan ServiceRequest ditentukan berdasarkan ketersediaan MWL pada fasilitas pelayanan kesehatan - Pembaharuan lampiran 4 dan 5 terkait alur pengiriman DICOM - Pembaharuan Judul Bab 18. Rencana Tindak Lanjut dan Bab.19 Instruksi Tindak Lanjut dan Sarana Transportasi untuk Rujuk | - Sania Fitria - Anisatul ‘Afifah - Luthfi Nabilah Qonita - Jaisyullah Rafiul Islam |
| v5.0 | 28 Maret 2024 | - Pembaharuan Pengiriman Data Tindakan pada Bab.11 Tindakan menjadi 2 Jenis, yaitu Sub-Bab 11.2 Tindakan Diagnostik dan Sub-Bab 11.3 Tindakan Terapeutik | - Sania Fitria - Anisatul ‘Afifah |
| v4.0 | 15 Februari 2024 | - Pembaruan alur integrasi pelayanan rawat jalan - Penambahan narasi definisi dan tahapan pengiriman pelayanan rawat jalan di Bab C. Integrasi - Pembaruan alur untuk pengiriman radiologi - Pembaruan narasi pengiriman data Radiologi dengan DICOM - Penambahan lampiran 4 dan 5 terkait alur pengiriman DICOM | - Anisatul ‘Afifah - Jaisyullah Rafiul Islam |
| v3.0 | 18 Januari 2024 | - Pembaruan Playbook Resume Medis Rawat Jalan Jilid 1 dan 2 menjadi Playbook Modul Rawat Jalan (Jilid 1 dan 2 disatukan) - Penambahan Variabel dalam Bab C.3 Pengiriman Data Anamnesis, yaitu Riwayat Penyakit dan Riwayat Pengobatan - Penambahan Variabel dalam Bab C.4 Pengiriman Data Pemeriksaan Fisik, yaitu Pemeriksaan Fisik *Head to Toe*, Pemeriksaan Psikologis, Tinggi Badan, Berat Badan, dan Luas Permukaan Tubuh untuk Anak-Anak - Penambahan Bab C.5 Pengiriman Data Rencana Rawat Pasien - Penambahan Bab C.6 Pengiriman Data Instruksi Medik dan Keperawatan - Penambahan Variabel Status Puasa dalam Pemeriksaan Penunjang Laboratorium dan Radiologi - Penambahan Variabel Status Alergi Pasien terhadap Bahan Kontras/Zat Lainnya dan Status Kehamilan dalam Pemeriksaan Penunjang Radiologi - Penambahan Variabel Pengkajian Resep dalam Bab C.20 Pengiriman Data Peresepan Obat | Sania Fitria |
| v2.0 | 03 Mei 2023 | - Perubahan kode terminologi dengan SNOMED CT untuk variabel Prognosis, Kondisi Saat Meninggalkan Rumah Sakit, Tingkat Kesadaran, Rencana Tindak Lanjut/Cara Keluar dari Rumah Sakit, dan Edukasi. - Penambahan variabel keluhan utama. | Nindya Widita Ayuningtyas |
| v1.3 | 20 Maret 2023 | Penyesuaian *cardinality resources simplifier*. | Nindya Widita Ayuningtyas |
| v1.2 | 08 Maret 2023 | Penambahan informasi 6 fase integrasi SATUSEHAT pada Bab C Integrasi. | Nindya Widita Ayuningtyas |
| v1.1 | 16 Februari 2023 | Perubahan struktur pada dokumen, adanya sub-bab “Pemetaan Nilai” dan “Pemetaan Variabel”/ “Terminologi Spesifik”/ “Ketentuan Pengisian”. | Nindya Widita Ayuningtyas |
| v1.0 | 14 Februari 2023 | **Rilis** dokumen awal (Modul Rawat Jalan) *Resource*: `Patient`, `Encounter`, `AllergyIntolerance`, `Observation`, `Procedure`, `Medication`, `MedicationRequest`, `MedicationDispense`, `Condition`, `Composition`, `ClincalImpression`, `ServiceRequest`, `Specimen`, `DiagnosticReport`, `ImagingStudy`. | Nindya Widita Ayuningtyas |

|  |  |
| --- | --- |
|  | Silakan klik setiap teks yang berwarna **biru muda**, untuk membaca panduan lebih detail/lanjut ke bagian yang direferensikan. |

## POSTMAN SATUSEHAT

Kami menyediakan **Postman SATUSEHAT** yang berisi **Environment** dan **Postman Collection SATUSEHAT**. Anda dapat menggunakan Postman SATUSEHAT tersebut untuk mempermudah proses pemaham alur/skema dari pengiriman data SATUSEHAT pada modul ini ketika melakukan *workshop* secara mandiri.

|  |  |
| --- | --- |
|  | Silakan terlebih dahulu **men-*download*/mengunduh/*froking* *environment* dan Postman Collection SATUSEHAT** sebelum mempelajari modul ini lebih dalam:  1. **Postman SATUSEHAT Public** klik [**di sini**](https://www.postman.com/satusehat/workspace/satusehat-public/overview). 2. Sesuaikan *environment* yang digunakan, apabila masih dalam proses *workshop* secara mandiri (uji coba) maka *download*/unduh dan gunakan *environment* Sandbox. 3. Pastikan men-*download*/mengunduh Postman Collection SATUSEHAT sesuai dengan modul yang saat ini Anda pelajari. |

|  |  |
| --- | --- |
|  | 1. **Postman SATUSEHAT Public** klik [**di sini**](https://www.postman.com/satusehat/workspace/satusehat-public/overview). 2. **Environment SATUSEHAT s.link By ©Kemenkes** klik [**di sini**](https://s.kemkes.go.id/EnvironmentPostmanSATUSEHAT). 3. **Postman Collection SATUSEHAT s.link By ©Kemenkes** terkait **Modul Pelayanan-Rawat Jalan** klik [**di sini**](https://s.kemkes.go.id/PostmanModulPelayananRawatJalan). |

## PREREQUISITES

Sebelum melakukan pengiriman data SATUSEHAT, terdapat 4 langkah yang perlu dilakukan yaitu:

1. Autentikasi ke SATUSEHAT,
2. Registrasi Struktur Organisasi,
3. Registrasi Struktur Lokasi,
4. Menyimpan Nomor IHS untuk Tenaga Kesehatan (`Practitioner`).

### Autentikasi

Informasi autentikasi atau pertukaran/transaksi data akan dibahas lebih lanjut pada [**Autentikasi**](../../api-catalogue/authentication/#auth-fhir)

### Registrasi Struktur Organisasi

#### Berikut ini adalah struktur organisasi dari resume medis rawat jalan 1.

![Registrasi Struktur Organisasi](../_images/struktur-organisasi-rme1.png)

Gambar 1. Registrasi Struktur Organisasi

#### Berikut ini adalah struktur organisasi dari resume medis rawat jalan 2.

![Registrasi Struktur Organisasi](../_images/struktur-organisasi-rme2.png)

Gambar 2. Registrasi Struktur Organisasi

|  |  |
| --- | --- |
|  | - Informasi terkait pemetaan nilai, penjelasan tipe mandatoris, deskripsi dan format pengisian dari setiap elemen data/*path* di dalam resource `Organization` (data suborganisasi), dapat dilihat [**di sini**](../../fhir/resources/organization/#organization). - Dapat dilihat juga pada Postman SATUSEHAT, silakan klik [**di sini**](../../postman-workshop/#postman-collection-satusehat). - Dokumentasi ReST API SATUSEHAT (Katalog ReST API SATUSEHAT) dapat dilihat [**di sini**](../../api-catalogue/onboardings/apis/organization/). - Silahkan tonton video tutorial [**di sini**](https://drive.google.com/file/d/1LSQ7yvM9bwT-6oJt80KtCy3hsUlAsD3w/view?usp=drive_link) untuk mendapatkan informasi tambahan terkait **POST** `Organization`. |

### Registrasi Struktur Lokasi

#### Berikut ini adalah struktur lokasi dari resume medis rawat jalan 1,

![Registrasi Struktur Lokasi](../_images/struktur-lokasi-rme1.png)

Gambar 3. Registrasi Struktur Lokasi

#### Berikut ini adalah struktur lokasi dari resume medis rawat jalan 2,

![Registrasi Struktur Lokasi](../_images/struktur-lokasi-rme2.png)

Gambar 4. Registrasi Struktur Lokasi

|  |  |
| --- | --- |
|  | - Informasi terkait pemetaan nilai, penjelasan tipe mandatoris, deskripsi dan format pengisian dari setiap elemen data/*path* di dalam resource `Location` (data sublokasi), dapat dilihat [**di sini**](../../fhir/resources/location/#location). - Dapat dilihat juga pada Postman SATUSEHAT, silakan klik [**di sini**](../../postman-workshop/#postman-collection-satusehat). - Dokumentasi ReST API SATUSEHAT (Katalog ReST API SATUSEHAT) dapat dilihat [**di sini**](../../api-catalogue/onboardings/apis/location/). - Silahkan tonton video tutorial [**di sini**](https://drive.google.com/file/d/1m8TfS5lt1P7nsCUj-3c06DwuhMnKCMZh/view?usp=drive_link) untuk mendapatkan informasi tambahan terkait **POST** `Location`. |

### Nomor IHS untuk Tenaga Kesehatan

|  |  |
| --- | --- |
|  | Proses pencarian SATUSEHAT ID dari tenaga kesehatan `{practitioner-ihs-number}` dapat dilakukan melalui FHIR API dengan metode **GET**.  - Penjelasan tipe mandatoris, deskripsi dan format pengisian dari setiap elemen data/path di dalam resource `Practitioner` dapat dilihat [**di sini**](../../fhir/resources/practitioner/#practitioner). - Dapat dilihat juga pada Postman SATUSEHAT, silakan klik [**di sini**](../../postman-workshop/#postman-collection-satusehat). - Dokumentasi ReST API SATUSEHAT (Katalog ReST API SATUSEHAT) dapat dilihat [**di sini**](../../api-catalogue/onboardings/apis/practitioner/). - Silahkan tonton video tutorial [**di sini**](https://drive.google.com/file/d/1okQ1mmB5-1D_ZMOl0Yr1UdTmwFkC0ssp/view?usp=drive_link) untuk mendapatkan informasi tambahan terkait **GET** `Practitioner`. |

## INTEGRASI

Pelayanan rawat jalan merupakan pelayanan kepada pasien untuk observasi, diagnosis, pengobatan, rehabilitasi medis, dan pelayanan kesehatan lainnya tanpa tinggal di ruang rawat inap[[1](#_footnotedef_1 "View footnote.")][[2](#_footnotedef_2 "View footnote.")].

Playbook pelayanan Rawat Jalan dibuat sebagai panduan teknis untuk fasilitas pelayanan kesehatan atau pengembang rekam medis elektronik lainnya dalam melakukan proses integrasi dan interoperabilitas di dalam SATUSEHAT Platform (SSP), khususnya informasi terkait pelayanan rawat jalan. Playbook ini menjelaskan secara detail mengenai standar tahapan alur integrasi dan format pengiriman data, mulai dari:

1. Pendaftaran Pasien (\* [`Patient`](../../fhir/resources/patient/#patient))
2. Pendaftaran Kunjungan (\* [`Encounter`](../../fhir/resources/encounter/#encounter))
3. Pengiriman Data Anamnesis (\* [`Condition`](../../fhir/resources/condition/#condition), \* [`FamilyMemberHistory`](../../fhir/resources/family-member-history/#familymemberhistory), \* [`AllergyIntolerance`](../../fhir/resources/allergy-intolerance/#allegryintolerance) , \* [`MedicationStatement`](../../fhir/resources/medication-statement/#medicationstatement))
4. Pengiriman Data Hasil Pemeriksaan Fisik (\* [`Observation`](../../fhir/resources/observation/#observation))
5. Pengiriman Data Pemeriksaan Fungsional (\* [`Observation`](../../fhir/resources/observation/#observation))
6. Pengiriman Data Riwayat Perjalanan Penyakit (\* [`ClinicalImpression`](../../fhir/resources/clinical-impression/#clinicalimpression))
7. Pengiriman Data Tujuan Perawatan (\* [`Goal`](../../fhir/resources/goal/#goal))
8. Pengiriman Data Rencana Rawat Pasien (\* [`CarePlan`](../../fhir/resources/care-plan/#careplan))
9. Pengiriman Data Instruksi Medik dan Keperawatan (\* [`CarePlan`](../../fhir/resources/care-plan/#careplan))
10. Pengiriman Data Pemeriksaan Penunjang Laboratorium  
    10.1. Skema Pengiriman Data Terkait Pemeriksaan Penunjang Laboratorium (\* [`ServiceRequest`](../../fhir/resources/service-request/#servicerequest), \* [`Specimen`](../../fhir/resources/specimen/#specimen), \* [`Observation`](../../fhir/resources/observation/#observation), \* [`DiagnosticReport`](../../fhir/resources/diagnostic-report/#diagnosticreport))  
    10.2. Pengiriman Data Permintaan Pemeriksaan Penunjang Laboratorium (\* [`ServiceRequest`](../../fhir/resources/service-request/#servicerequest))  
    10.3. Pengiriman Data Spesimen (\* [`Specimen`](../../fhir/resources/specimen/#specimen), \* [`Substance`](../../fhir/resources/substance/#substance))  
    10.4. Pengiriman Data Hasil Pemeriksaan Penunjang Laboratorium (\* [`Observation`](../../fhir/resources/observation/#observation))  
    10.5. Pengiriman Data Laporan Pemeriksaan Penunjang Laboratorium (\* [`DiagnosticReport`](../../fhir/resources/diagnostic-report/#diagnosticreport))
11. Pengiriman Data Pemeriksaan Penunjang Radiologi  
    11.1. Pengantar DICOM  
    11.2. Alur Pengiriman Data Pemeriksaan Radiologi ke SATUSEHAT (\* [`ServiceRequest`](../../fhir/resources/service-request/#servicerequest), \* [`Observation`](../../fhir/resources/observation/#observation), \* [`DiagnosticReport`](../../fhir/resources/diagnostic-report/#diagnosticreport))  
    11.3. Pengiriman Data Permintaan Pemeriksaan Penunjang Radiologi (\* [`ServiceRequest`](../../fhir/resources/service-request/#servicerequest))  
    11.4. Pengiriman Data Citra DICOM oleh DICOM router menuju National Imaging Data Repository (NIDR) (\* [`ImagingStudy`](../../fhir/resources/imaging-study/#imagingstudy))  
    11.5. Pengiriman Data Bacaan Hasil Pemeriksaan Penunjang Radiologi (\* [`Observation`](../../fhir/resources/observation/#observation))  
    11.6. Pengiriman Data Kesimpulan atau Kesan Hasil Pemeriksaan Penunjang Radiologi (\* [`DiagnosticReport`](../../fhir/resources/diagnostic-report/#diagnosticreport))
12. Pengiriman Data Rasional Klinis (\* [`ClinicalImpression`](../../fhir/resources/clinical-impression/#clinicalimpression))
13. Pengiriman Data Diagnosis (\* [`Condition`](../../fhir/resources/condition/#condition))
14. Pengiriman Data Penilaian Risiko (\* [`RiskAssessment`](../../fhir/resources/risk-assessment/#riskassessment))
15. Pengiriman Data Tindakan/Prosedur Medis (\* [`ServiceRequest`](../../fhir/resources/service-request/#servicerequest), \* [`Procedure`](../../fhir/resources/procedure/#procedure), \* [`Observation`](../../fhir/resources/observation/#observation))
16. Pengiriman Data Peresepan Obat (\* [`Medication`](../../fhir/resources/medication/#medication), \* [`MedicationRequest`](../../fhir/resources/medication-request/#medicationrequest), \* [`MedicationDispense`](../../fhir/resources/medication-dispense/#medicationdispense))
17. Pengiriman Data Pengkajian Resep (\* [`QuestionnaireResponse`](../../fhir/resources/questionnaire-response/#questionnaireresponse))
18. Pengiriman Data Pengeluaran Obat (\* [`Medication`](../../fhir/resources/medication/#medication), \* [`MedicationDispense`](../../fhir/resources/medication-dispense/#medicationdispense))
19. Pengiriman Data Pemberian Obat (\* [`Medication`](../../fhir/resources/medication/#medication), \* [`MedicationAdministration`](../../fhir/resources/medication-administration/#medicationadministration))
20. Pengiriman Data Diet (\* [`NutritionOrder`](../../fhir/resources/nutrition-order/#nutritionorder))
21. Pengiriman Data Edukasi (\* [`Procedure`](../../fhir/resources/procedure/#procedure))
22. Pengiriman Data Prognosis (\* [`ClinicalImpression`](../../fhir/resources/clinical-impression/#clinicalimpression))
23. Pengiriman Data Rencana Tindak Lanjut (\* [`ServiceRequest`](../../fhir/resources/service-request/#servicerequest))
24. Pengiriman Data Instruksi Tindak Lanjut dan Sarana Transportasi untuk Rujuk (\* [`ServiceRequest`](../../fhir/resources/service-request/#servicerequest))
25. Pengiriman Data Kondisi Saat Meninggalkan Rumah Sakit (\* [`Condition`](../../fhir/resources/condition/#condition), \* [`Encounter`](../../fhir/resources/encounter/#encounter))
26. Pengiriman Data Cara Keluar dari Rumah Sakit (\* [`Encounter`](../../fhir/resources/encounter/#encounter), \* [`ServiceRequest`](../../fhir/resources/service-request/#servicerequest))
27. Pembaharuan Data Kunjungan (\* [`Encounter`](../../fhir/resources/encounter/#encounter))
28. Pengiriman Data Resume Medis (\* [`Composition`](../../fhir/resources/composition/#composition))

Tahapan alur integrasi dan resource yang digunakan untuk resume medis rawat jalan dapat dilihat dalam Gambar 3.

![Diagram Resume Medis Rawat Jalan](../_images/alur-integrasi-rajal.svg)

Gambar 5. Alur Integrasi Resume Medis Rawat Jalan

### Informasi Variabel

Variabel pada Modul Rawat Jalan yang dapat dipertukarkan dalam SATUSEHAT sebagai berikut:

[Unduh](https://drive.google.com/u/0/uc?id=1l9TpJx2pvrPPD-oaANVs2bjDYrC7USS7rPf4wsG6P9U&export=download)

## 1. Pendaftaran Pasien

Apabila melakukan pengiriman data kesehatan melalui SATUSEHAT yang memiliki elemen data terkait resource [`Patient`](../../fhir/resources/patient/#patient), maka diperlukan informasi `{patient-ihs-number}` dari pasien yang bersangkutan. `{patient-ihs-number}` seorang pasien didapatkan dari *Master Patient Index* (MPI) Kementerian Kesehatan. MPI menyimpan data-data demografi pasien berskala nasional, mulai dari nama, tanggal lahir, alamat, identitas resmi yang diterbitkan pemerintah, dan lain lain. Setelah mendapatkan `{patient-ihs-number}`, ID dapat disimpan secara di masing-masing sistem internal fasyankes maupun partner non-fasyankes. `{patient-ihs-number}` akan mempermudah pelaporan pelayanan kesehatan yang berhubungan dengan pasien, karena partner tidak diwajibkan menyertakan data diri setiap ada pengiriman data `{patient-ihs-number}` juga dapat digunakan untuk melihat data diri pasien secara menyeluruh.

|  |  |
| --- | --- |
|  | Proses pencarian `{patient-ihs-number}` dari resource [`Patient`](../../fhir/resources/patient/#patient) dapat dilakukan melalui FHIR API dengan metode **GET**.  - Penjelasan tipe mandatoris, deskripsi dan format pengisian dari setiap elemen data/path di dalam resource `Patient` dapat dilihat [**di sini**](../../fhir/resources/patient/#patient). - Metode pencarian data pasien di SATUSEHAT secara detail dapat dilihat pada panduan/playbook Master Patient Index (MPI), silakan klik [**di sini**](../../master-data/master-patient-index/preliminary/#prem-mpi). - Dapat dilihat juga pada Postman SATUSEHAT, silakan klik [**di sini**](../../postman-workshop/#postman-collection-satusehat). - Dokumentasi ReST API SATUSEHAT (Katalog ReST API SATUSEHAT) dapat dilihat [**di sini**](../../api-catalogue/onboardings/apis/patient/). |

## 2. Pendaftaran Kunjungan Pasien

Kunjungan pasien dapat didefinisikan sebagai interaksi pasien terhadap suatu layanan fasyankes. Sebagai contoh, dalam satu rangkaian rawat jalan, seluruh rangkaian dapat didefinisikan sebagai satu `Encounter`. Data-data kunjungan pasien yang direkam meliputi kapan pertemuan tersebut mulai dan selesai, siapa tenaga kesehatan yang melayani, siapa subjek dari pelayanannya, dan informasi pendukung lainnya.

### Pemetaan Nilai Encounter

Berikut pemetaan nilai untuk `Encounter` yang direpresentasikan dalam peta referensi *(path)* ke properti *(element id)* terkait, untuk konteks data kunjungan:

|  |  |
| --- | --- |
|  | 1. Setiap terdapat simbol asterik `*` sebelum nama variabel/parameter/element FHIR yang disebutkan, maka variabel/parameter/element FHIR tersebut bersifat **WAJIB**, **harus ada**, atau **pasti selalu ada**, contoh: **`*Location.identifier`**. 2. **Standar format Waktu** yang digunakan dalam pengiriman data adalah **UTC +00**. Misalnya waktu **WIB**, maka format yang digunakan adalah **waktu sekarang dikurangi 7**, jika **WITA**, maka **waktu sekarang dikurangi 8**, dan Jika **WIT**, maka **waktu sekarang dikurangi 9**.  **Contoh:** Pukul 17.35 WIB tanggal 23 Agustus 2023 maka yang dikirimkan adalah waktunya perlu diubah ke UTC +00 menjadi 10.35, berarti menjadi `2023-08-23T10:35:00+00:00`. 3. **Standar format pengiriman Tanggal** tidak bisa kurang dari 03 Juni 2014. |

|  |  |
| --- | --- |
|  | Silakan klik setiap teks variabel/parameter/element FHIR pada daftar pemetaan nilai di bawah ini (berwarna **merah**), untuk membaca panduan lebih detail/lanjut ke bagian yang direferensikan. |

- [`*Encounter.identifier[i]`](../../fhir/resources/encounter/#encounter-identifier)
- [`*Encounter.status`](../../fhir/resources/encounter/#encounter-status)
- [`*Encounter.statusHistory[i].status`](../../fhir/resources/encounter/#encounter-statushistory-status)
- [`*Encounter.statusHistory[i].period`](../../fhir/resources/encounter/#encounter-statushistory-status)
- [`*Encounter.class`](../../fhir/resources/encounter/#encounter-class)
- [`*Encounter.classHistory[i].class`](../../fhir/resources/encounter/#encounter-classHistory-class)
- [`*Encounter.classHistory[i].period`](../../fhir/resources/encounter/#encounter-classHistory-period)
- [`Encounter.type`](../../fhir/resources/encounter/#encounter-type)
- [`Encounter.serviceType`](../../fhir/resources/encounter/#encounter-serviceType)
- [`Encounter.priority`](../../fhir/resources/encounter/#encounter-priority)
- [`*Encounter.subject`](../../fhir/resources/encounter/#encounter-subject)
- [`Encounter.episodeOfCare`](../../fhir/resources/encounter/#encounter-episodeOfCare)
- [`Encounter.basedOn`](../../fhir/resources/encounter/#encounter-basedOn)
- [`*Encounter.participant[i].type`](../../fhir/resources/encounter/#encounter-participant.type)
- [`*Encounter.participant[i].individual`](../../fhir/resources/encounter/#encounter-participant-individual)
- [`*Encounter.period`](../../fhir/resources/encounter/#encounter-period)
- [`Encounter.length`](../../fhir/resources/encounter/#encounter-length)
- [`Encounter.reasonCode`](../../fhir/resources/encounter/#encounter-reasonCOde)
- [`Encounter.reasonReference`](../../fhir/resources/encounter/#encounter-reasonReference)
- [`*Encounter.diagnosis[i].condition`](../../fhir/resources/encounter/#encounter-diagnosis-condition)
- [`Encounter.diagnosis[i].use`](../../fhir/resources/encounter/#encounter-diagnosis-use)
- [`Encounter.diagnosis[i].rank`](../../fhir/resources/encounter/#encounter-diagnosis-rank)
- [`Encounter.account`](../../fhir/resources/encounter/#encounter-account)
- [`Encounter.hospitalization.preAdmissionIdentifier`](../../fhir/resources/encounter/#encounter-hospitalization-preAdmissionIdentifier)
- [`Encounter.hospitalization.origin`](../../fhir/resources/encounter/#encounter-hospitalization-origin)
- [`Encounter.hospitalization.admitSource`](../../fhir/resources/encounter/#encounter-hospitalization-admitSource)
- [`Encounter.hospitalization.reAdmission`](../../fhir/resources/encounter/#encounter-hospitalization-reAdmission)
- [`Encounter.hospitalization.dietPreference`](../../fhir/resources/encounter/#encounter-hospitalization-dietPreference)
- [`Encounter.hospitalization.specialArrangement`](../../fhir/resources/encounter/#encounter-hospitalization-specialArrangement)
- [`Encounter.hospitalization.destination`](../../fhir/resources/encounter/#encounter-hospitalization-destination)
- [`*Encounter.hospitalization.dischargeDisposition`](../../fhir/resources/encounter/#encounter-hospitalization-dischargeDisposition)
- [`*Encounter.location`](../../fhir/resources/encounter/#encounter-location)
- [`*Encounter.serviceProvider`](../../fhir/resources/encounter/#encounter-serviceProvider)
- [`Encounter.partOf`](../../fhir/resources/encounter/#encounter-partOf)

Penjelasan tipe mandatoris, deskripsi dan format pengisian dari setiap elemen data/*path* di dalam resource `Encounter` (data pendaftaran kunjungan pasien), dapat dilihat dalam resource [`Encounter`](../../fhir/resources/encounter/#encounter). Untuk contoh pengiriman data atau *payload* dari `Encounter` dapat dilihat dalam [Postman SATUSEHAT](../../postman-workshop/#postman-collection-satusehat) SATUSEHAT.

### Pemetaan Variabel dan Terminologi Spesifik

Terminologi spesifik yang digunakan dalam pengiriman data kunjungan melalui resource `Encounter` dapat dilihat dalam tabel berikut:

Tabel 2. Informasi Variabel

| Pemetaan Variabel *Resource* `Encounter` | | | | |
| --- | --- | --- | --- | --- |
| **Elemen/Path FHIR** | **Terminologi/Format Pengisian** | | | |
| **Pendaftaran Kunjungan** | | | | |
| **1. Nomor Kunjungan** | | | | |
| **`Encounter.identifier.system`** | **<http://sys-ids.kemkes.go.id/encounter/{{Organization_ID}}>** | | | |
| **`Encounter.identifier.value`** | **(Tipe data *string*)** | | | |
| **2. Status Kunjungan** | | | | |
| **`Encounter.status`** | ***arrived*** | | ***in-progress*** | |
| **Keterangan** | **Pasien datang namun belum bertemu dokter** | | **Pasien dalam proses pelayanan/sedang bertemu dokter** | |
| **3. Jenis Kunjungan** | | | | |
| **`Encounter.class.system`** | **<http://terminology.hl7.org/CodeSystem/v3-ActCode>** | | | |
| **`Encounter.class.code`** | **AMB** | | | |
| **`Encounter.class.display`** | **ambulatory** | | | |
| **4. Tipe Pelayanan** | | | | |
| **`Encounter.serviceType.coding`** | **Terminologi dapat dilihat pada [Dokumen Lampiran Standar Terminologi SATUSEHAT](https://satusehat.kemkes.go.id/platform/docs/id/terminology/standar-terminologi/)** | | | |
| **5. Ruangan/Poli** | | | | |
| **`Encounter.location`** | **Referensi ke resource `Location`** | | | |
| **6. Kelas** | | | | |
| **`Encounter.location.extension.serviceClass.value.valueCodeableConcept.coding.system`** | **<http://terminology.kemkes.go.id/CodeSystem/locationServiceClass-Outpatient>** | | | |
| **`Encounter.location.extension.serviceClass.value.valueCodeableConcept.coding.code`** | ***reguler*** | | ***eksekutif*** | |
| **`Encounter.location.extension.serviceClass.value.valueCodeableConcept.coding.display`** | **Kelas Reguler** | | **Kelas Eksekutif** | |
| **a. Perubahan Kelas** | | | | |
| **`Encounter.location.extension.serviceClass.upgradeClassIndicator.valueCodeableConcept.coding.system`** | **<http://terminology.kemkes.go.id/CodeSystem/locationUpgradeClass>** | | | |
| **`Encounter.location.extension.serviceClass.upgradeClassIndicator.valueCodeableConcept.coding.code`** | **kelas-tetap** | **naik-kelas** | **turun-kelas** | **titip-rawat** |
| **`Encounter.location.extension.serviceClass.upgradeClassIndicator.valueCodeableConcept.coding.display`** | **Kelas Tetap Perawatan** | **Kenaikan Kelas Perawatan** | **Penurunan Kelas Perawatan** | **Titip Kelas Perawatan** |
| **7. Tanggal dan Waktu Masuk** | | | | |
| **`Encounter.period.start`** | **Tipe data *dateTime*** | | | |

## 3. Pengiriman Data Anamnesis

Data Anamnesis mencakup keluhan utama, keluhan penyerta, riwayat penyakit pribadi, riwayat penyakit keluarga, riwayat pengobatan, dan riwayat alergi. Data yang dimiliki pasien tersebut dapat dikirimkan menggunakan resource `Condition`, `FamilyMemberHistory`, `AllergyIntolerance`, dan `MedicationStatement`.

### Pemetaan Nilai Condition

Berikut pemetaan nilai untuk `Condition` yang direpresentasikan dalam peta referensi *(path)* ke properti *(element id)* terkait, untuk konteks pengiriman data diagnosis pasien:

|  |  |
| --- | --- |
|  | 1. Setiap terdapat simbol asterik `*` sebelum nama variabel/parameter/element FHIR yang disebutkan, maka variabel/parameter/element FHIR tersebut bersifat **WAJIB**, **harus ada**, atau **pasti selalu ada**, contoh: **`*Location.identifier`**. 2. **Standar format Waktu** yang digunakan dalam pengiriman data adalah **UTC +00**. Misalnya waktu **WIB**, maka format yang digunakan adalah **waktu sekarang dikurangi 7**, jika **WITA**, maka **waktu sekarang dikurangi 8**, dan Jika **WIT**, maka **waktu sekarang dikurangi 9**.  **Contoh:** Pukul 17.35 WIB tanggal 23 Agustus 2023 maka yang dikirimkan adalah waktunya perlu diubah ke UTC +00 menjadi 10.35, berarti menjadi `2023-08-23T10:35:00+00:00`. 3. **Standar format pengiriman Tanggal** tidak bisa kurang dari 03 Juni 2014. |

|  |  |
| --- | --- |
|  | Silakan klik setiap teks variabel/parameter/element FHIR pada daftar pemetaan nilai di bawah ini (berwarna **merah**), untuk membaca panduan lebih detail/lanjut ke bagian yang direferensikan. |

- [`Condition.identifier`](../../fhir/resources/condition/#condition-identifier)
- [`Condition.clinicalStatus`](../../fhir/resources/condition/#condition-clinicalStatus)
- [`Condition.verificationStatus`](../../fhir/resources/condition/#condition-verificationStatus)
- [`Condition.category`](../../fhir/resources/condition/#condition-category)
- [`Condition.severity`](../../fhir/resources/condition/#condition-severity)
- [`*Condition.code`](../../fhir/resources/condition/#condition-code)
- [`Condition.bodySite`](../../fhir/resources/condition/#condition-bodySite)
- [`*Condition.subject`](../../fhir/resources/condition/#condition-subject)
- [`*Condition.encounter`](../../fhir/resources/condition/#condition-encounter)
- [`Condition.onsetDateTime`](../../fhir/resources/condition/#condition-onsetDateTime)
- [`Condition.onsetAge`](../../fhir/resources/condition/#condition-onsetAge)
- [`Condition.onsetPeriod`](../../fhir/resources/condition/#condition-onsetPeriod)
- [`Condition.onsetRange`](../../fhir/resources/condition/#condition-onsetRange)
- [`Condition.onsetString`](../../fhir/resources/condition/#condition-onsetString)
- [`Condition.abatementDateTime`](../../fhir/resources/condition/#condition-abatementDateTime)
- [`Condition.abatementAge`](../../fhir/resources/condition/#condition-abatementAge)
- [`Condition.abatementPeriod`](../../fhir/resources/condition/#condition-abatementPeriod)
- [`Condition.abatementRange`](../../fhir/resources/condition/#condition-abatementRange)
- [`Condition.abatementString`](../../fhir/resources/condition/#condition-abatementString)
- [`Condition.recordedDate`](../../fhir/resources/condition/#condition-recordedDate)
- [`Condition.recorder`](../../fhir/resources/condition/#condition-recorder)
- [`Condition.asserter`](../../fhir/resources/condition/#condition-asserter)
- [`Condition.stage[i].summary`](../../fhir/resources/condition/#condition-stage-summary)
- [`Condition.stage[i].assessment`](../../fhir/resources/condition/#condition-stage-assessment)
- [`Condition.stage[i].type`](../../fhir/resources/condition/#condition-stage-type)
- [`Condition.evidence[i].code`](../../fhir/resources/condition/#condition-evidence-code)
- [`Condition.evidence[i].detail`](../../fhir/resources/condition/#condition-evidence-detail)
- [`Condition.note`](../../fhir/resources/condition/#condition-note)

Penjelasan tipe mandatoris, deskripsi dan format pengisian dari setiap elemen data/*path* di dalam resource `Condition` (data diagnosis), dapat dilihat dalam resource [`Condition`](../../fhir/resources/condition/#condition). Untuk contoh pengiriman data atau *payload* dari `Condition` dapat dilihat dalam [Postman SATUSEHAT](../../postman-workshop/#postman-collection-satusehat) SATUSEHAT.

### Pemetaan Nilai AllergyIntolerance

Berikut pemetaan nilai untuk `AllergyIntolerance` yang direpresentasikan dalam peta referensi *(path)* ke properti *(element id)* terkait, untuk konteks Pengiriman Data Alergi:

|  |  |
| --- | --- |
|  | 1. Setiap terdapat simbol asterik `*` sebelum nama variabel/parameter/element FHIR yang disebutkan, maka variabel/parameter/element FHIR tersebut bersifat **WAJIB**, **harus ada**, atau **pasti selalu ada**, contoh: **`*Location.identifier`**. 2. **Standar format Waktu** yang digunakan dalam pengiriman data adalah **UTC +00**. Misalnya waktu **WIB**, maka format yang digunakan adalah **waktu sekarang dikurangi 7**, jika **WITA**, maka **waktu sekarang dikurangi 8**, dan Jika **WIT**, maka **waktu sekarang dikurangi 9**.  **Contoh:** Pukul 17.35 WIB tanggal 23 Agustus 2023 maka yang dikirimkan adalah waktunya perlu diubah ke UTC +00 menjadi 10.35, berarti menjadi `2023-08-23T10:35:00+00:00`. 3. **Standar format pengiriman Tanggal** tidak bisa kurang dari 03 Juni 2014. |

|  |  |
| --- | --- |
|  | Silakan klik setiap teks variabel/parameter/element FHIR pada daftar pemetaan nilai di bawah ini (berwarna **merah**), untuk membaca panduan lebih detail/lanjut ke bagian yang direferensikan. |

- [`AllergyIntolerance.identifier`](../../fhir/resources/allergy-intolerance/#allergyintolerance-identifier)
- [`AllergyIntolerance.clinicalStatus`](../../fhir/resources/allergy-intolerance/#allergyintolerance-clinicalstatus)
- [`AllergyIntolerance.verificationStatus`](../../fhir/resources/allergy-intolerance/#allergyintolerance-verificationstatus)
- [`AllergyIntolerance.type`](../../fhir/resources/allergy-intolerance/#allergyintolerance-type)
- [`*AllergyIntolerance.category`](../../fhir/resources/allergy-intolerance/#allergyintolerance-category)
- [`AllergyIntolerance.criticality`](../../fhir/resources/allergy-intolerance/#allergyintolerance-criticality)
- [`*AllergyIntolerance.code`](../../fhir/resources/allergy-intolerance/#allergyintolerance-code)
- [`*AllergyIntolerance.patient`](../../fhir/resources/allergy-intolerance/#allergyintolerance-patient)
- [`*AllergyIntolerance.encounter`](../../fhir/resources/allergy-intolerance/#allergyintolerance-encounter)
- [`AllergyIntolerance.onsetDateTime`](../../fhir/resources/allergy-intolerance/#allergyintolerance-onsetdatetime)
- [`AllergyIntolerance.onsetAge`](../../fhir/resources/allergy-intolerance/#allergyintolerance-onsetage)
- [`AllergyIntolerance.onsetPeriod`](../../fhir/resources/allergy-intolerance/#allergyintolerance-onsetperiod)
- [`AllergyIntolerance.onsetRange`](../../fhir/resources/allergy-intolerance/#allergyintolerance-onsetrange)
- [`AllergyIntolerance.onsetString`](../../fhir/resources/allergy-intolerance/#allergyintolerance-onsetstring)
- [`AllergyIntolerance.recordedDate`](../../fhir/resources/allergy-intolerance/#allergyintolerance-recordeddate)
- [`*AllergyIntolerance.recorder`](../../fhir/resources/allergy-intolerance/#allergyintolerance-recorder)
- [`AllergyIntolerance.asserter`](../../fhir/resources/allergy-intolerance/#allergyintolerance-asserter)
- [`AllergyIntolerance.lastOccurrence`](../../fhir/resources/allergy-intolerance/#allergyintolerance-lastoccurrence)
- [`AllergyIntolerance.note`](../../fhir/resources/allergy-intolerance/#allergyintolerance-note)
- [`AllergyIntolerance.reaction[i].substance`](../../fhir/resources/allergy-intolerance/#allergyintolerance-reaction-substance)
- [`*AllergyIntolerance.reaction[i].manifestation`](../../fhir/resources/allergy-intolerance/#allergyintolerance-reaction-manifestation)
- [`AllergyIntolerance.reaction[i].description`](../../fhir/resources/allergy-intolerance/#allergyintolerance-reaction-description)
- [`AllergyIntolerance.reaction[i].onset`](../../fhir/resources/allergy-intolerance/#allergyintolerance-reaction-onset)
- [`AllergyIntolerance.reaction[i].severity`](../../fhir/resources/allergy-intolerance/#allergyintolerance-reaction-severity)
- [`AllergyIntolerance.reaction[i].exposureRoute`](../../fhir/resources/allergy-intolerance/#allergyintolerance-reaction-exposureroute)
- [`AllergyIntolerance.reaction[i].note`](../../fhir/resources/allergy-intolerance/#allergyintolerance-reaction-note)

Penjelasan tipe mandatoris, deskripsi dan format pengisian dari setiap elemen data/*path* di dalam resource `AllergyIntolerance` (data alergi), dapat dilihat dalam [resource `AllergyIntolerance`](../../fhir/resources/allergy-intolerance/#allergyintolerance). Untuk contoh pengiriman data atau *payload* dari `AllergyIntolerance` dapat dilihat dalam [Postman SATUSEHAT](../../postman-workshop/#postman-collection-satusehat) SATUSEHAT.

### Pemetaan Nilai FamilyMemberHistory

Berikut pemetaan nilai untuk `FamilyMemberHistory` yang direpresentasikan dalam peta referensi (path) ke properti (element id) terkait, untuk konteks Pengiriman Data Riwayat Penyakit Keluarga:

|  |  |
| --- | --- |
|  | 1. Setiap terdapat simbol asterik `*` sebelum nama variabel/parameter/element FHIR yang disebutkan, maka variabel/parameter/element FHIR tersebut bersifat **WAJIB**, **harus ada**, atau **pasti selalu ada**, contoh: **`*Location.identifier`**. 2. **Standar format Waktu** yang digunakan dalam pengiriman data adalah **UTC +00**. Misalnya waktu **WIB**, maka format yang digunakan adalah **waktu sekarang dikurangi 7**, jika **WITA**, maka **waktu sekarang dikurangi 8**, dan Jika **WIT**, maka **waktu sekarang dikurangi 9**.  **Contoh:** Pukul 17.35 WIB tanggal 23 Agustus 2023 maka yang dikirimkan adalah waktunya perlu diubah ke UTC +00 menjadi 10.35, berarti menjadi `2023-08-23T10:35:00+00:00`. 3. **Standar format pengiriman Tanggal** tidak bisa kurang dari 03 Juni 2014. |

|  |  |
| --- | --- |
|  | Silakan klik setiap teks variabel/parameter/element FHIR pada daftar pemetaan nilai di bawah ini (berwarna **merah**), untuk membaca panduan lebih detail/lanjut ke bagian yang direferensikan. |

- [`FamilyMemberHistory.identifier[i]`](../../fhir/resources/family-member-history/#familymemberhistory-identifier)
- [`FamilyMemberHistory.instantiatesCanonical[i]`](../../fhir/resources/family-member-history/#familymemberhistory-instantiatescanonical)
- [`FamilyMemberHistory.instantiatesUri[i]`](../../fhir/resources/family-member-history/#familymemberhistory-instantiatesuri)
- [`*FamilyMemberHistory.status`](../../fhir/resources/family-member-history/#familymemberhistory-status)
- [`FamilyMemberHistory.dataAbsentReason`](../../fhir/resources/family-member-history/#familymemberhistory-dataabsentreason)
- [`*FamilyMemberHistory.patient`](../../fhir/resources/family-member-history/#familymemberhistory-patient)
- [`FamilyMemberHistory.date`](../../fhir/resources/family-member-history/#familymemberhistory-date)
- [`FamilyMemberHistory.name`](../../fhir/resources/family-member-history/#familymemberhistory-name)
- [`*FamilyMemberHistory.relationship`](../../fhir/resources/family-member-history/#familymemberhistory-relationship)
- [`FamilyMemberHistory.sex`](../../fhir/resources/family-member-history/#familymemberhistory-sex)
- [`FamilyMemberHistory.born<?>`](../../fhir/resources/family-member-history/#familymemberhistory-born)
- [`FamilyMemberHistory.bornPeriod`](../../fhir/resources/family-member-history/#familymemberhistory-bornperiod)
- [`FamilyMemberHistory.bornDate`](../../fhir/resources/family-member-history/#familymemberhistory-borndate)
- [`FamilyMemberHistory.bornString`](../../fhir/resources/family-member-history/#familymemberhistory-bornstring)
- [`FamilyMemberHistory.age<?>`](../../fhir/resources/family-member-history/#familymemberhistory-age)
- [`FamilyMemberHistory.ageAge`](../../fhir/resources/family-member-history/#familymemberhistory-ageage)
- [`FamilyMemberHistory.ageRange`](../../fhir/resources/family-member-history/#familymemberhistory-agerange)
- [`FamilyMemberHistory.ageString`](../../fhir/resources/family-member-history/#familymemberhistory-agestring)
- [`FamilyMemberHistory.estimatedAge`](../../fhir/resources/family-member-history/#familymemberhistory-estimatedage)
- [`FamilyMemberHistory.deceased<?>`](../../fhir/resources/family-member-history/#familymemberhistory-deceased)
- [`FamilyMemberHistory.deceasedBoolean`](../../fhir/resources/family-member-history/#familymemberhistory-deceasedboolean)
- [`FamilyMemberHistory.deceasedAge`](../../fhir/resources/family-member-history/#familymemberhistory-deceasedage)
- [`FamilyMemberHistory.deceasedRange`](../../fhir/resources/family-member-history/#familymemberhistory-deceasedrange)
- [`FamilyMemberHistory.deceasedDate`](../../fhir/resources/family-member-history/#familymemberhistory-deceaseddate)
- [`FamilyMemberHistory.deceasedString`](../../fhir/resources/family-member-history/#familymemberhistory-deceasedstring)
- [`FamilyMemberHistory.reasonCode[i]`](../../fhir/resources/family-member-history/#familymemberhistory-reasoncode)
- [`FamilyMemberHistory.reasonReference[i]`](../../fhir/resources/family-member-history/#familymemberhistory-reasonreference)
- [`FamilyMemberHistory.note[i]`](../../fhir/resources/family-member-history/#familymemberhistory-note)
- [`FamilyMemberHistory.condition[i]`](../../fhir/resources/family-member-history/#familymemberhistory-condition)
- [`*FamilyMemberHistory.condition.code`](../../fhir/resources/family-member-history/#familymemberhistory-condition-code)
- [`FamilyMemberHistory.condition.outcome`](../../fhir/resources/family-member-history/#familymemberhistory-condition-outcome)
- [`FamilyMemberHistory.condition.contributedToDeath`](../../fhir/resources/family-member-history/#familymemberhistory-condition.contributedtodeath)
- [`FamilyMemberHistory.condition.onset<?>`](../../fhir/resources/family-member-history/#familymemberhistory-condition-onset)
- [`FamilyMemberHistory.condition.onsetAge`](../../fhir/resources/family-member-history/#familymemberhistory-condition-onsetage)
- [`FamilyMemberHistory.condition.onsetRange`](../../fhir/resources/family-member-history/#familymemberhistory-condition-onsetrange)
- [`FamilyMemberHistory.condition.onsetPeriod`](../../fhir/resources/family-member-history/#familymemberhistory-condition-onsetperiod)
- [`FamilyMemberHistory.condition.onsetString`](../../fhir/resources/family-member-history/#familymemberhistory-condition-onsetstring)
- [`FamilyMemberHistory.condition.note[i]`](../../fhir/resources/family-member-history/#familymemberhistory-condition-note)

### Pemetaan Nilai MedicationStatement

Berikut pemetaan nilai untuk `MedicationStatement` yang direpresentasikan dalam peta referensi (*path*) ke properti (*element id*) terkait, untuk konteks catatan pengobatan pasien:

|  |  |
| --- | --- |
|  | 1. Setiap terdapat simbol asterik `*` sebelum nama variabel/parameter/element FHIR yang disebutkan, maka variabel/parameter/element FHIR tersebut bersifat **WAJIB**, **harus ada**, atau **pasti selalu ada**, contoh: **`*Location.identifier`**. 2. **Standar format Waktu** yang digunakan dalam pengiriman data adalah **UTC +00**. Misalnya waktu **WIB**, maka format yang digunakan adalah **waktu sekarang dikurangi 7**, jika **WITA**, maka **waktu sekarang dikurangi 8**, dan Jika **WIT**, maka **waktu sekarang dikurangi 9**.  **Contoh:** Pukul 17.35 WIB tanggal 23 Agustus 2023 maka yang dikirimkan adalah waktunya perlu diubah ke UTC +00 menjadi 10.35, berarti menjadi `2023-08-23T10:35:00+00:00`. 3. **Standar format pengiriman Tanggal** tidak bisa kurang dari 03 Juni 2014. |

|  |  |
| --- | --- |
|  | Silakan klik setiap teks variabel/parameter/element FHIR pada daftar pemetaan nilai di bawah ini (berwarna **merah**), untuk membaca panduan lebih detail/lanjut ke bagian yang direferensikan. |

- [`MedicationStatement.identifier`](../../fhir/resources/medication-statement/#medicationstatement-identifier)
- [`MedicationStatement.basedOn`](../../fhir/resources/medication-statement/#medicationstatement-basedon)
- [`MedicationStatement.partOf`](../../fhir/resources/medication-statement/#medicationstatement-partof)
- [`*MedicationStatement.status`](../../fhir/resources/medication-statement/#medicationstatement-status)
- [`MedicationStatement.statusReason`](../../fhir/resources/medication-statement/#medicationstatement-statusreason)
- [`MedicationStatement.category`](../../fhir/resources/medication-statement/#medicationstatement-category)
- [`*MedicationStatement.medication[x]`](../../fhir/resources/medication-statement/#medicationstatement-medication)
- [`MedicationStatement.medicationCodeableConcept`](../../fhir/resources/medication-statement/#medicationstatement-medicationcodeableconcept)
- [`MedicationStatement.medicationReference`](../../fhir/resources/medication-statement/#medicationstatement-medicationreference)
- [`*MedicationStatement.subject`](../../fhir/resources/medication-statement/#medicationstatement-subject)
- [`MedicationStatement.context`](../../fhir/resources/medication-statement/#medicationstatement-context)
- [`MedicationStatement.effective[x]`](../../fhir/resources/medication-statement/#medicationstatement-effective)
- [`MedicationStatement.effectiveDateTime`](../../fhir/resources/medication-statement/#medicationstatement-effectivedatetime)
- [`MedicationStatement.effectivePeriod`](../../fhir/resources/medication-statement/#medicationstatement-effectiveperiod)
- [`MedicationStatement.dateAsserted`](../../fhir/resources/medication-statement/#medicationstatement-dateasserted)
- [`MedicationStatement.informationSource`](../../fhir/resources/medication-statement/#medicationstatement-informationsource)
- [`MedicationStatement.derivedFrom`](../../fhir/resources/medication-statement/#medicationstatement-derivedfrom)
- [`MedicationStatement.reasonCode`](../../fhir/resources/medication-statement/#medicationstatement-reasoncode)
- [`MedicationStatement.reasonReference`](../../fhir/resources/medication-statement/#medicationstatement-reasonreference)
- [`MedicationStatement.note`](../../fhir/resources/medication-statement/#medicationstatement-note)
- [`MedicationStatement.dosage`](../../fhir/resources/medication-statement/#medicationstatement-dosage)

### Pemetaan Variabel dan Terminologi Spesifik

Terminologi spesifik yang digunakan dalam pengiriman data keluhan utama, keluhan penyerta, riwayat penyakit pribadi, riwayat penyakit keluarga, riwayat alergi, dan riwayat pengobatan melalui resource `Condition`, `FamilyMemberHistory`, `AllergyIntolerance`, dan `MedicationStatement` dapat dilihat dalam tabel berikut:

Tabel 3. Variabel dan Terminologi Spesifik

| Pemetaan Variabel *Resource* `Condition`, `FamilyMemberHistory`, `AllergyIntolerance`, `MedicationStatement` | | | | |
| --- | --- | --- | --- | --- |
| **Elemen/*Path* FHIR** | **Terminologi/Format Pengisian** | | | |
| **Anamnesis** | | | | |
| **1. Keluhan Utama** | | | | |
| **`Condition.category.coding.system`** | **<http://terminology.kemkes.go.id>** | | | |
| **`Condition.category.coding.code`** | **chief-complaint** | | | |
| **`Condition.category.coding.display`** | **Chief Complaint** | | | |
| **`Condition.code.coding.system`** | **<http://snomed.info/sct>** | | | |
| **`Condition.code.coding.code`** | **SNOMED-CT Code Ruang lingkup kode SNOMED CT yang dapat dipakai: Expression Constraint Language (ECL) Query: < 404684003 |Clinical finding (finding)|>**  **(Untuk Kode Lengkapnya dapat dilihat pada Dokumen Lampiran [Standar Terminologi](../../terminology/standar-terminologi/#standar-terminologi) SATUSEHAT)** | | | |
| **`Condition.code.coding.display`** | **SNOMED-CT Description** | | | |
| **`Condition.onsetDateTime`** | **Tipe data *dateTime*** | | | |
| **`Encounter.diagnosis.condition`** | **Referensi ke `Condition`/{{id keluhan utama}}** | | | |
| **`Encounter.diagnosis.use.coding.system`** | **<http://terminology.hl7.org/CodeSystem/diagnosis-role>** | | | |
| **`Encounter.diagnosis.use.coding.code`** | **CC** | | | |
| **`Encounter.diagnosis.use.coding.display`** | **Chief Complaint** | | | |
| ****Keterangan**: Setiap keluhan utama yang berkaitan langsung dengan kondisi pasien maka maka ketika `PUT` `Encounter` dengan status finished perlu menyertakan `Encounter.diagnosis` untuk keluhan utama yang terkait.** | | | | |
| **2. Keluhan Penyerta** | | | | |
| **`Condition.category.coding.system`** | **<http://terminology.hl7.org/CodeSystem/condition-category>** | | | |
| **`Condition.category.coding.code`** | **problem-list-item** | | | |
| **`Condition.category.coding.display`** | **Problem List Item** | | | |
| **`Condition.code.coding.system`** | **<http://snomed.info/sct>** | | | |
| **`Condition.code.coding.code`** | **SNOMED-CT Code**  **Ruang lingkup kode SNOMED CT yang dapat dipakai: Expression Constraint Language (ECL) Query: < 404684003 |Clinical finding (finding)|**  **(Untuk Kode Lengkapnya dapat dilihat pada Dokumen Lampiran [Standar Terminologi](../../terminology/standar-terminologi/#standar-terminologi) SATUSEHAT)** | | | |
| **`Condition.code.coding.display`** | **SNOMED-CT Description** | | | |
| **3. Riwayat Penyakit Pribadi** | | | | |
| **`Condition.category.coding.system`** | **<http://terminology.kemkes.go.id>** | | | |
| **`Condition.category.coding.code`** | **previous-condition** | | | |
| **`Condition.category.coding.display`** | **Previous Condition** | | | |
| **`Condition.code.coding.system`** | **<http://snomed.info/sct>** | | | |
| **`Condition.code.coding.code`** | **SNOMED-CT Code**  **Ruang lingkup kode SNOMED CT yang dapat dipakai: Expression Constraint Language (ECL) Query: < 417662000 | History of clinical finding in subject (situation) | OR < 443508001 | No history of clinical finding in subject (situation) |**  **(Untuk Kode Lengkapnya dapat dilihat di Dokumen Lampiran [Standar Terminologi](../../terminology/standar-terminologi/#standar-terminologi) SATUSEHAT)** | | | |
| **`Condition.code.coding.display`** | **SNOMED-CT Description** | | | |
| **`Condition.clinicalStatus.coding.system`** | **<http://terminology.hl7.org/CodeSystem/condition-clinical>** | | | |
| **`Condition.clinicalStatus.coding.code`** | **active** | | **inactive** | |
| **`Condition.clinicalStatus.coding.display`** | **Active** | | **Inactive** | |
| ****Keterangan**: Riwayat Penyakit Pribadi yang masih berlangsung dapat menggunakan `Condition.clinicalStatus` dengan status active, sedangkan Riwayat Penyakit Pribadi yang sudah berakhir dapat menggunakan `Condition.clinicalStatus` dengan status inactive.** | | | | |
| **4. Riwayat Penyakit Keluarga** | | | | |
| **`FamilyMemberHistory.relationship.coding.system`** | **<http://terminology.hl7.org/CodeSystem/v3-RoleCode>** | | | |
| **`FamilyMemberHistory.relationship.coding.code`** | **FAMMEMB** | | | |
| **`FamilyMemberHistory.relationship.coding.display`** | **Family member** | | | |
| **`FamilyMemberHistory.condition.code.coding.system`** | **<http://snomed.info/sct>** | | | |
| **`FamilyMemberHistory.condition.code.coding.code`** | **SNOMED-CT Code**  **Ruang lingkup kode SNOMED CT yang dapat dipakai: Expression Constraint Language (ECL) Query: < 416471007 | Family history of clinical finding (situation) | OR < 160266009 | No family history of clinical finding (situation) |**  **(Untuk Kode Lengkapnya dapat dilihat di Dokumen Lampiran [Standar Terminologi](../../terminology/standar-terminologi/#standar-terminologi) SATUSEHAT)** | | | |
| **`FamilyMemberHistory.condition.code.coding.display`** | **SNOMED-CT Description** | | | |
| **`FamilyMemberHistory.condition.outcome.system`** | **<http://snomed.info/sct>** | | | |
| **`FamilyMemberHistory.condition.outcome.code`** | **SNOMED-CT Code**  **Ruang lingkup kode SNOMED CT yang dapat dipakai: Expression Constraint Language (ECL) Query: < 418138009 | Patient condition finding (finding) |**  **(Untuk Kode Lengkapnya dapat dilihat di Dokumen Lampiran [Standar Terminologi](../../terminology/standar-terminologi/#standar-terminologi) SATUSEHAT)** | | | |
| **`FamilyMemberHistory.condition.outcome.display`** | **SNOMED-CT Description** | | | |
| **`FamilyMemberHistory.condition.contributedToDeath`** | **Tipe data *boolean*** | | | |
| **`FamilyMemberHistory.condition.onset[x]`** | **Tipe data *Age* | *Range* | *Period* | *String*** | | | |
| **`FamilyMemberHistory.deceasedbooelan`** | **Tipe data *boolean*** | | | |
| **5. Riwayat Alergi** | | | | |
| **`AllergyIntolerance.code.coding`** | **Lihat di Dokumen Lampiran [Standar Terminologi](../../terminology/standar-terminologi/#standar-terminologi) SATUSEHAT** | | | |
| **`AllergyIntolerance.category`** | **medication** | **food** | **environment** | **biologic** |
| **`AllergyIntolerance.clinicalStatus.system`** | **<http://terminology.hl7.org/CodeSystem/allergyintolerance-clinical>** | | | |
| **`AllergyIntolerance.clinicalStatus.code`** | **active** | | **inactive** | |
| **`AllergyIntolerance.clinicalStatus.display`** | **Active** | | **Inactive** | |
| **Pilihan jawaban yang divisualisasikan** | **Ya** | | **Tidak** | |
| **6. Riwayat Pengobatan** | | | | |
| **`MedicationStatement.status`** | **Lihat di Dokumen Lampiran [Standar Terminologi](../../terminology/standar-terminologi/#standar-terminologi) SATUSEHAT** | | | |
| **`MedicationStatement.medication[x]`** | **Lihat di Sub-Bab 3.4.1 Ketentuan Pengisian Riwayat Pengobatan** | | | |
| **`MedicationStatement.note.text`** | **(Tipe Data *String*)** | | | |

#### Ketentuan Pengisian Riwayat Pengobatan

Ketentuan pengisian secara spesifik untuk pengisian resource `MedicationStatement` adalah sebagai berikut:

1. `MedicationStatement.medicationReference` `MedicationStatement.medicationReference` dapat digunakan saat :

   - Obat yang dikonsumsi Pasien sebelumnya berasal dari Fasyankes tempat dilakukan pelayanan.  
     Fasyankes dapat melakukan GET `MedicationDispense` dengan `{patient-ihs-number}`, dan mendapatkan Referensi `Medication` sebelumnya yang akan dikirimkan dalam `MedicationStatement.contain` pengiriman data Riwayat Pengobatan.
2. `MedicationStatement.medicationCodeableConcept` `MedicationStatement.medicationCodeableConcept` digunakan saat pasien mengkonsumsi obat yang bukan berasal dari Fasyankes tempat dilakukan pelayanan. Pengiriman data `MedicationStatement.medicationCodeableConcept` menggunakan Kode Produk Obat Aktual (93xxxxxx) dan Kode Produk Obat Template (92xxxxxx). Daftar kode obat aktual dan template dapat dilihat pada [browser kamus KFA](https://dto.kemkes.go.id/kfa-browser). Berikut adalah variasi pengiriman data menggunakan `MedicationStatement.medicationCodeableConcept`:

   - Jika pasien membawa obat yang dikonsumsi dan diketahui merk obat yang digunakan, maka kode yang akan digunakan adalah kode awalan 93.  
     **Contoh** : 93005512 → Ampicillin Trihydrate 500 mg Tablet (PHARMA LABORATORIES)
   - Jika pasien hanya menyebutkan obat yang dikonsumsi tanpa mengetahui merk obat yang digunakan, maka kode yang akan digunakan adalah kode awalan 92.  
     **Contoh** : 92001087 → Ampicillin Trihydrate 500 mg Tablet

Tabel 4. Tabel Skenario Pengiriman Data `MedicationStatement.medicationCodeableConcept`

| Skenario | `MedicationStatement.medicationCodeableConcept.coding.system` | `MedicationStatement.medicationCodeableConcept.coding.code` | `MedicationStatement.medicationCodeableConcept.coding.display` |
| --- | --- | --- | --- |
| Jika pasien membawa obat yang dikonsumsi dan diketahui merk obat yang digunakan | **Ampicillin Trihydrate 500 mg** | | |
| <http://sys-ids.kemkes.go.id/kfa> | 93005512 | Ampicillin Trihydrate 500 mg Tablet (PHARMA LABORATORIES) |
| Jika pasien hanya menyebutkan obat yang dikonsumsi tanpa mengetahui merk obat yang digunakan | **Ampicillin Trihydrate 500 mg** | | |
| <http://sys-ids.kemkes.go.id/kfa> | 92001087 | Ampicillin Trihydrate 500 mg Tablet |

## 4. Pengiriman Data Hasil Pemeriksaan Fisik

Setelah sesi anamnesis, dokter akan melakukan beberapa pemeriksaan fisik. Data hasil pemeriksaan fisik dapat dikirimkan melalui resource `Observation`.

### Pemetaan Nilai Observation

Berikut pemetaan nilai untuk `Observation` yang direpresentasikan dalam peta referensi *(path)* ke properti *(element id)* terkait, untuk konteks pemeriksaan laboratorium:

|  |  |
| --- | --- |
|  | 1. Setiap terdapat simbol asterik `*` sebelum nama variabel/parameter/element FHIR yang disebutkan, maka variabel/parameter/element FHIR tersebut bersifat **WAJIB**, **harus ada**, atau **pasti selalu ada**, contoh: **`*Location.identifier`**. 2. **Standar format Waktu** yang digunakan dalam pengiriman data adalah **UTC +00**. Misalnya waktu **WIB**, maka format yang digunakan adalah **waktu sekarang dikurangi 7**, jika **WITA**, maka **waktu sekarang dikurangi 8**, dan Jika **WIT**, maka **waktu sekarang dikurangi 9**.  **Contoh:** Pukul 17.35 WIB tanggal 23 Agustus 2023 maka yang dikirimkan adalah waktunya perlu diubah ke UTC +00 menjadi 10.35, berarti menjadi `2023-08-23T10:35:00+00:00`. 3. **Standar format pengiriman Tanggal** tidak bisa kurang dari 03 Juni 2014. |

|  |  |
| --- | --- |
|  | Silakan klik setiap teks variabel/parameter/element FHIR pada daftar pemetaan nilai di bawah ini (berwarna **merah**), untuk membaca panduan lebih detail/lanjut ke bagian yang direferensikan. |

- [`Observation.identifier`](../../fhir/resources/observation/#observation-identifier)
- [`Observation.basedOn`](../../fhir/resources/observation/#observation-basedOn)
- [`Observation.partOf`](../../fhir/resources/observation/#observation-partOf)
- [`*Observation.status`](../../fhir/resources/observation/#observation-status)
- [`Observation.category`](../../fhir/resources/observation/#observation-category)
- [`*Observation.code`](../../fhir/resources/observation/#observation-code)
- [`*Observation.subject`](../../fhir/resources/observation/#observation-subject)
- [`Observation.focus`](../../fhir/resources/observation/#observation-focus)
- [`*Observation.encounter`](../../fhir/resources/observation/#observation-encounter)
- [`Observation.effectiveDateTime`](../../fhir/resources/observation/#observation-effectiveDateTime)
- [`Observation.effectivePeriod`](../../fhir/resources/observation/#observation-effectivePeriod)
- [`Observation.effectiveTiming`](../../fhir/resources/observation/#observation-effectiveTiming)
- [`Observation.effectiveInstant`](../../fhir/resources/observation/#observation-effectiveInstant)
- [`Observation.issued`](../../fhir/resources/observation/#observation-issued)
- [`*Observation.performer`](../../fhir/resources/observation/#observation-performer)
- [`Observation.valueQuantity`](../../fhir/resources/observation/#observation-valueQuantity)
- [`Observation.valueCodeableConcept`](../../fhir/resources/observation/#observation-valueCodeableConcept)
- [`Observation.valueString`](../../fhir/resources/observation/#observation-valueString)
- [`Observation.valueBoolean`](../../fhir/resources/observation/#observation-valueBoolean)
- [`Observation.valueInteger`](../../fhir/resources/observation/#observation-valueInteger)
- [`Observation.valueRange`](../../fhir/resources/observation/#observation-valueRange)
- [`Observation.valueRatio`](../../fhir/resources/observation/#observation-valueRatio)
- [`Observation.valueSampledData`](../../fhir/resources/observation/#observation-valueSampledData)
- [`Observation.valueTime`](../../fhir/resources/observation/#observation-valueTime)
- [`Observation.valueDateTime`](../../fhir/resources/observation/#observation-valueDateTime)
- [`Observation.valuePeriod`](../../fhir/resources/observation/#observation-valuePeriod)
- [`Observation.dataAbsentReason`](../../fhir/resources/observation/#observation-dataAbsentReason)
- [`Observation.interpretation`](../../fhir/resources/observation/#observation-interpretation)
- [`Observation.note`](../../fhir/resources/observation/#observation-note)
- [`Observation.bodySite`](../../fhir/resources/observation/#observation-bodySite)
- [`Observation.method`](../../fhir/resources/observation/#observation-method)
- [`Observation.specimen`](../../fhir/resources/observation/#observation-specimen)
- [`Observation.device`](../../fhir/resources/observation/#observation-device)
- [`Observation.referenceRange`](../../fhir/resources/observation/#observation-referenceRange)
- [`Observation.referenceRange.type`](../../fhir/resources/observation/#observation-referenceRange-type)
- [`Observation.hasMember`](../../fhir/resources/observation/#observation-hasMember)
- [`Observation.derivedFrom`](../../fhir/resources/observation/#observation-derivedFrom)

Penjelasan tipe mandatoris, deskripsi dan format pengisian dari setiap elemen data/*path* di dalam resource `Observation` (data tanda vital), dapat dilihat dalam resource [`Observation`](../../fhir/resources/observation/#observation). Untuk contoh pengiriman data atau *payload* dari `Observation` dapat dilihat dalam [Postman SATUSEHAT](../../postman-workshop/#postman-collection-satusehat) SATUSEHAT.

### Pemetaan Variabel dan Terminologi Spesifik

Terminologi spesifik yang digunakan dalam pengiriman data pemeriksaan fisik melalui resource [`Observation`](../../fhir/resources/observation/#observation) dapat dilihat dalam tabel berikut:

Tabel 5. Terminologi spesifik yang digunakan dalam pengiriman data tanda vital melalui resource `Observation`

| Pemetaan Variabel *Resource* `Observation` | | | |
| --- | --- | --- | --- |
| **Elemen/*Path* FHIR** | **Terminologi/Format Pengisian** | | |
| **Pemeriksaan Fisik** | | | |
| **1. Tanda Vital** | | | |
| **a. Denyut Jantung** | | | |
| **`Observation.category[i].coding[i].system`** | **<http://terminology.hl7.org/CodeSystem/observation-category>** | | |
| **`Observation.category[i].coding[i].code`** | **vital-signs** | | |
| **`Observation.category[i].coding[i].display`** | **Vital Signs** | | |
| **`*Observation.code.coding.system`** | **<http://loinc.org>** | | |
| **`*Observation.code.coding.code`** | **8867-4** | | |
| **`*Observation.code.coding.display`** | **Heart rate** | | |
| **`Observation.valueQuantity.value`** | ***(Tipe data Decimal)*** | | |
| **`Observation.valueQuantity.unit`** | **beats/min** | | |
| **`Observation.valueQuantity.system`** | **<http://unitsofmeasure.org>** | | |
| **`Observation.valueQuantity.code`** | **/min** | | |
| **b. Pernapasan** | | | |
| **`Observation.category[i].coding[i].system`** | **<http://terminology.hl7.org/CodeSystem/observation-category>** | | |
| **`Observation.category[i].coding[i].code`** | **vital-signs** | | |
| **`Observation.category[i].coding[i].display`** | **Vital Signs** | | |
| **`*Observation.code.coding.system`** | **<http://loinc.org>** | | |
| **`*Observation.code.coding.code`** | **9279-1** | | |
| **`*Observation.code.coding.display`** | **Respiratory rate** | | |
| **`Observation.valueQuantity.value`** | ***(Tipe data Decimal)*** | | |
| **`Observation.valueQuantity.unit`** | **breaths/min** | | |
| **`Observation.valueQuantity.system`** | **<http://unitsofmeasure.org>** | | |
| **`Observation.valueQuantity.code`** | **/min** | | |
| **c. Tekanan Darah** | | | |
| **1) Sistole** | | | |
| **`Observation.category[i].coding[i].system`** | **<http://terminology.hl7.org/CodeSystem/observation-category>** | | |
| **`Observation.category[i].coding[i].code`** | **vital-signs** | | |
| **`Observation.category[i].coding[i].display`** | **Vital Signs** | | |
| **`*Observation.code.coding.system`** | **<http://loinc.org>** | | |
| **`*Observation.code.coding.code`** | **8480-6** | | |
| **`*Observation.code.coding.display`** | **Systolic blood pressure** | | |
| **`Observation.valueQuantity.value`** | ***(Tipe data Decimal)*** | | |
| **`Observation.valueQuantity.unit`** | **mm[Hg]** | | |
| **`Observation.valueQuantity.system`** | **<http://unitsofmeasure.org>** | | |
| **`Observation.valueQuantity.code`** | **mm[Hg]** | | |
| **2) Diastole** | | | |
| **`Observation.category[i].coding[i].system`** | **<http://terminology.hl7.org/CodeSystem/observation-category>** | | |
| **`Observation.category[i].coding[i].code`** | **vital-signs** | | |
| **`Observation.category[i].coding[i].display`** | **Vital Signs** | | |
| **`*Observation.code.coding.system`** | **<http://loinc.org>** | | |
| **`*Observation.code.coding.code`** | **8462-4** | | |
| **`*Observation.code.coding.display`** | **Diastolic blood pressure** | | |
| **`Observation.valueQuantity.value`** | ***(Tipe data Decimal)*** | | |
| **`Observation.valueQuantity.unit`** | **mm[Hg]** | | |
| **`Observation.valueQuantity.system`** | **<http://unitsofmeasure.org>** | | |
| **`Observation.valueQuantity.code`** | **mm[Hg]** | | |
| **d. Suhu Tubuh** | | | |
| **`Observation.category[i].coding[i].system`** | **<http://terminology.hl7.org/CodeSystem/observation-category>** | | |
| **`Observation.category[i].coding[i].code`** | **vital-signs** | | |
| **`Observation.category[i].coding[i].display`** | **Vital Signs** | | |
| **`*Observation.code.coding.system`** | **<http://loinc.org>** | | |
| **`*Observation.code.coding.code`** | **8310-5** | | |
| **`*Observation.code.coding.display`** | **Body temperature** | | |
| **`Observation.valueQuantity.value`** | ***(Tipe data Decimal)*** | | |
| **`Observation.valueQuantity.unit`** | **C** | | |
| **`Observation.valueQuantity.system`** | **<http://unitsofmeasure.org>** | | |
| **`Observation.valueQuantity.code`** | **Cel** | | |
| **2. Tingkat Kesadaran** | | | |
| **`Observation.category[i].coding.system`** | | **<http://terminology.hl7.org/CodeSystem/observation-category>** | |
| **`Observation.category[i].coding.code`** | | **exam** | |
| **`Observation.category[i].coding.display`** | | **Exam** | |
| **`*Observation.code.coding.system`** | | **<http://loinc.org>** | |
| **`*Observation.code.coding.code`** | | **67775-7** | |
| **`*Observation.code.coding.display`** | | **Level of responsiveness** | |
| **`Observation.valueCodeableConcept[i].coding.system`** | **`Observation.valueCodeableConcept[i].coding.code`** | **`Observation.valueCodeableConcept[i].coding.display`** | **Keterangan** |
| **<http://snomed.info/sct>** | **248234008** | **Mentally alert** | **1. Sadar Baik/Alert: 0** |
| **<http://snomed.info/sct>** | **300202002** | **Response to voice** | **2. Berespon dengan kata-kata/Voice** |
| **<http://snomed.info/sct>** | **450847001** | **Responds to pain** | **3. Hanya berespons jika dirangsang nyeri/pain: 2** |
| **<http://snomed.info/sct>** | **422768004** | **Unresponsive** | **4. Pasien tidak sadar/unresponsive:** |
| **<http://snomed.info/sct>** | **130987000** | **Acute confusion** | **5. Gelisah atau bingung: 4** |
| **<http://snomed.info/sct>** | **2776000** | **Delirium** | **6. Acute Confusional States: 5** |
| **3. Pemeriksaan Fisik Head to Toe** | | | |
| **a. Kepala** | | | |
| **`Observation.category[i].coding[i].system`** | **<http://terminology.hl7.org/CodeSystem/observation-category>** | | |
| **`Observation.category[i].coding[i].code`** | **exam** | | |
| **`Observation.category[i].coding[i].display`** | **Exam** | | |
| **`*Observation.code.coding.system`** | **<http://loinc.org>** | | |
| **`*Observation.code.coding.code`** | **10199-8** | | |
| **`*Observation.code.coding.display`** | **Physical findings of Head Narrative** | | |
| **`Observation.valueQuantity.value`** | ***(Tipe data String)*** | | |
| **b. Mata** | | | |
| **`Observation.category[i].coding[i].system`** | **<http://terminology.hl7.org/CodeSystem/observation-category>** | | |
| **`Observation.category[i].coding[i].code`** | **exam** | | |
| **`Observation.category[i].coding[i].display`** | **Exam** | | |
| **`*Observation.code.coding.system`** | **<http://loinc.org>** | | |
| **`*Observation.code.coding.code`** | **10197-2** | | |
| **`*Observation.code.coding.display`** | **Physical findings of Eye Narrative** | | |
| **`Observation.valueQuantity.value`** | ***(Tipe data String)*** | | |
| **c. Telinga** | | | |
| **`Observation.category[i].coding[i].system`** | **<http://terminology.hl7.org/CodeSystem/observation-category>** | | |
| **`Observation.category[i].coding[i].code`** | **exam** | | |
| **`Observation.category[i].coding[i].display`** | **Exam** | | |
| **`*Observation.code.coding.system`** | **<http://loinc.org>** | | |
| **`*Observation.code.coding.code`** | **10195-6** | | |
| **`*Observation.code.coding.display`** | **Physical findings of Ear Narrative** | | |
| **`Observation.valueQuantity.value`** | ***(Tipe data String)*** | | |
| **d. Hidung** | | | |
| **`Observation.category[i].coding[i].system`** | **<http://terminology.hl7.org/CodeSystem/observation-category>** | | |
| **`Observation.category[i].coding[i].code`** | **exam** | | |
| **`Observation.category[i].coding[i].display`** | **Exam** | | |
| **`*Observation.code.coding.system`** | **<http://loinc.org>** | | |
| **`*Observation.code.coding.code`** | **10203-8** | | |
| **`*Observation.code.coding.display`** | **Physical findings of Nose Narrative** | | |
| **`Observation.valueQuantity.value`** | ***(Tipe data String)*** | | |
| **e. Rambut** | | | |
| **`Observation.category[i].coding[i].system`** | **<http://terminology.hl7.org/CodeSystem/observation-category>** | | |
| **`Observation.category[i].coding[i].code`** | **exam** | | |
| **`Observation.category[i].coding[i].display`** | **Exam** | | |
| **`*Observation.code.coding.system`** | **<http://loinc.org>** | | |
| **`*Observation.code.coding.code`** | **32436-8** | | |
| **`*Observation.code.coding.display`** | **Physical findings of Hair** | | |
| **`Observation.valueQuantity.value`** | ***(Tipe data String)*** | | |
| **f. Bibir** | | | |
| **`Observation.category[i].coding[i].system`** | **<http://terminology.hl7.org/CodeSystem/observation-category>** | | |
| **`Observation.category[i].coding[i].code`** | **exam** | | |
| **`Observation.category[i].coding[i].display`** | **Exam** | | |
| **`*Observation.code.coding.system`** | **<http://loinc.org>** | | |
| **`*Observation.code.coding.code`** | **32446-7** | | |
| **`*Observation.code.coding.display`** | **Physical findings of Lip** | | |
| **`Observation.valueQuantity.value`** | ***(Tipe data String)*** | | |
| **g. Gigi geling** | | | |
| **`Observation.category[i].coding[i].system`** | **<http://terminology.hl7.org/CodeSystem/observation-category>** | | |
| **`Observation.category[i].coding[i].code`** | **exam** | | |
| **`Observation.category[i].coding[i].display`** | **Exam** | | |
| **`*Observation.code.coding.system`** | **<http://loinc.org>** | | |
| **`*Observation.code.coding.code`** | **85910-8** | | |
| **`*Observation.code.coding.display`** | **Physical findings of Teeth and Gum Narrative** | | |
| **`Observation.valueQuantity.value`** | ***(Tipe data String)*** | | |
| **h. Lidah** | | | |
| **`Observation.category[i].coding[i].system`** | **<http://terminology.hl7.org/CodeSystem/observation-category>** | | |
| **`Observation.category[i].coding[i].code`** | **exam** | | |
| **`Observation.category[i].coding[i].display`** | **Exam** | | |
| **`*Observation.code.coding.system`** | **<http://loinc.org>** | | |
| **`*Observation.code.coding.code`** | **32483-0** | | |
| **`*Observation.code.coding.display`** | **Physical findings of Tongue** | | |
| **`Observation.valueQuantity.value`** | ***(Tipe data String)*** | | |
| **i. Langit-Langit** | | | |
| **`Observation.category[i].coding[i].system`** | **<http://terminology.hl7.org/CodeSystem/observation-category>** | | |
| **`Observation.category[i].coding[i].code`** | **exam** | | |
| **`Observation.category[i].coding[i].display`** | **Exam** | | |
| **`*Observation.code.coding.system`** | **<http://loinc.org>** | | |
| **`*Observation.code.coding.code`** | **10201-2** | | |
| **`*Observation.code.coding.display`** | **Physical findings of Mouth and Throat and Teeth Narrative** | | |
| **`*Observation.code.coding.system`** | **<http://snomed.info/sct>** | | |
| **`*Observation.code.coding.code`** | **72914001** | | |
| **`*Observation.code.coding.display`** | **Palatal structure** | | |
| **`Observation.valueQuantity.value`** | ***(Tipe data String)*** | | |
| **j. Leher** | | | |
| **`Observation.category[i].coding[i].system`** | **<http://terminology.hl7.org/CodeSystem/observation-category>** | | |
| **`Observation.category[i].coding[i].code`** | **exam** | | |
| **`Observation.category[i].coding[i].display`** | **Exam** | | |
| **`*Observation.code.coding.system`** | **<http://loinc.org>** | | |
| **`*Observation.code.coding.code`** | **11411-6** | | |
| **`*Observation.code.coding.display`** | **Physical findings of Neck Narrative** | | |
| **`Observation.valueQuantity.value`** | ***(Tipe data String)*** | | |
| **k. Tenggorokan** | | | |
| **`Observation.category[i].coding[i].system`** | **<http://terminology.hl7.org/CodeSystem/observation-category>** | | |
| **`Observation.category[i].coding[i].code`** | **exam** | | |
| **`Observation.category[i].coding[i].display`** | **Exam** | | |
| **`*Observation.code.coding.system`** | **<http://loinc.org>** | | |
| **`*Observation.code.coding.code`** | **56867-5** | | |
| **`*Observation.code.coding.display`** | **Physical findings of Throat Narrative** | | |
| **`Observation.valueQuantity.value`** | ***(Tipe data String)*** | | |
| **l. Tonsil** | | | |
| **`Observation.category[i].coding[i].system`** | **<http://terminology.hl7.org/CodeSystem/observation-category>** | | |
| **`Observation.category[i].coding[i].code`** | **exam** | | |
| **`Observation.category[i].coding[i].display`** | **Exam** | | |
| **`*Observation.code.coding.system`** | **<http://loinc.org>** | | |
| **`*Observation.code.coding.code`** | **10201-2** | | |
| **`*Observation.code.coding.display`** | **Physical findings of Mouth and Throat and Teeth Narrative** | | |
| **`*Observation.code.coding.system`** | **<http://snomed.info/sct>** | | |
| **`*Observation.code.coding.code`** | **91636008** | | |
| **`*Observation.code.coding.display`** | **Bilateral palatine tonsils** | | |
| **`Observation.valueQuantity.value`** | ***(Tipe data String)*** | | |
| **m. Dada** | | | |
| **`Observation.category[i].coding[i].system`** | **<http://terminology.hl7.org/CodeSystem/observation-category>** | | |
| **`Observation.category[i].coding[i].code`** | **exam** | | |
| **`Observation.category[i].coding[i].display`** | **Exam** | | |
| **`*Observation.code.coding.system`** | **<http://loinc.org>** | | |
| **`*Observation.code.coding.code`** | **11391-0** | | |
| **`*Observation.code.coding.display`** | **Physical findings of Chest Narrative** | | |
| **`Observation.valueQuantity.value`** | ***(Tipe data String)*** | | |
| **n. Payudara** | | | |
| **`Observation.category[i].coding[i].system`** | **<http://terminology.hl7.org/CodeSystem/observation-category>** | | |
| **`Observation.category[i].coding[i].code`** | **exam** | | |
| **`Observation.category[i].coding[i].display`** | **Exam** | | |
| **`*Observation.code.coding.system`** | **<http://loinc.org>** | | |
| **`*Observation.code.coding.code`** | **10193-1** | | |
| **`*Observation.code.coding.display`** | **Physical findings of Breasts Narrative** | | |
| **`Observation.valueQuantity.value`** | ***(Tipe data String)*** | | |
| **o. Punggung** | | | |
| **`Observation.category[i].coding[i].system`** | **<http://terminology.hl7.org/CodeSystem/observation-category>** | | |
| **`Observation.category[i].coding[i].code`** | **exam** | | |
| **`Observation.category[i].coding[i].display`** | **Exam** | | |
| **`*Observation.code.coding.system`** | **<http://loinc.org>** | | |
| **`*Observation.code.coding.code`** | **10192-3** | | |
| **`*Observation.code.coding.display`** | **Physical findings of Back Narrative** | | |
| **`Observation.valueQuantity.value`** | ***(Tipe data String)*** | | |
| **p. Perut** | | | |
| **`Observation.category[i].coding[i].system`** | **<http://terminology.hl7.org/CodeSystem/observation-category>** | | |
| **`Observation.category[i].coding[i].code`** | **exam** | | |
| **`Observation.category[i].coding[i].display`** | **Exam** | | |
| **`*Observation.code.coding.system`** | **<http://loinc.org>** | | |
| **`*Observation.code.coding.code`** | **10191-5** | | |
| **`*Observation.code.coding.display`** | **Physical findings of Abdomen Narrative** | | |
| **`Observation.valueQuantity.value`** | ***(Tipe data String)*** | | |
| **q. Genital** | | | |
| **`Observation.category[i].coding[i].system`** | **<http://terminology.hl7.org/CodeSystem/observation-category>** | | |
| **`Observation.category[i].coding[i].code`** | **exam** | | |
| **`Observation.category[i].coding[i].display`** | **Exam** | | |
| **`*Observation.code.coding.system`** | **<http://loinc.org>** | | |
| **`*Observation.code.coding.code`** | **11400-9** | | |
| **`*Observation.code.coding.display`** | **Physical findings of Genitalia Narrative** | | |
| **`Observation.valueQuantity.value`** | ***(Tipe data String)*** | | |
| **r. Anus/Dubur** | | | |
| **`Observation.category[i].coding[i].system`** | **<http://terminology.hl7.org/CodeSystem/observation-category>** | | |
| **`Observation.category[i].coding[i].code`** | **exam** | | |
| **`Observation.category[i].coding[i].display`** | **Exam** | | |
| **`*Observation.code.coding.system`** | **<http://loinc.org>** | | |
| **`*Observation.code.coding.code`** | **11388-6** | | |
| **`*Observation.code.coding.display`** | **Physical findings of Buttocks Narrative** | | |
| **`*Observation.code.coding.system`** | **<http://snomed.info/sct>** | | |
| **`*Observation.code.coding.code`** | **53505006** | | |
| **`*Observation.code.coding.display`** | **Anal structure** | | |
| **`Observation.valueQuantity.value`** | ***(Tipe data String)*** | | |
| **s. Lengan Atas** | | | |
| **`Observation.category[i].coding[i].system`** | **<http://terminology.hl7.org/CodeSystem/observation-category>** | | |
| **`Observation.category[i].coding[i].code`** | **exam** | | |
| **`Observation.category[i].coding[i].display`** | **Exam** | | |
| **`*Observation.code.coding.system`** | **<http://loinc.org>** | | |
| **`*Observation.code.coding.code`** | **11386-0** | | |
| **`*Observation.code.coding.display`** | **Physical findings of Upper Arm Narrative** | | |
| **`Observation.valueQuantity.value`** | ***(Tipe data String)*** | | |
| **t. Lengan Bawah** | | | |
| **`Observation.category[i].coding[i].system`** | **<http://terminology.hl7.org/CodeSystem/observation-category>** | | |
| **`Observation.category[i].coding[i].code`** | **exam** | | |
| **`Observation.category[i].coding[i].display`** | **Exam** | | |
| **`*Observation.code.coding.system`** | **<http://loinc.org>** | | |
| **`*Observation.code.coding.code`** | **11398-5** | | |
| **`*Observation.code.coding.display`** | **Physical findings of Forearm Narrative** | | |
| **`Observation.valueQuantity.value`** | ***(Tipe data String)*** | | |
| **u. Jari Tangan** | | | |
| **`Observation.category[i].coding[i].system`** | **<http://terminology.hl7.org/CodeSystem/observation-category>** | | |
| **`Observation.category[i].coding[i].code`** | **exam** | | |
| **`Observation.category[i].coding[i].display`** | **Exam** | | |
| **`*Observation.code.coding.system`** | **<http://loinc.org>** | | |
| **`*Observation.code.coding.code`** | **11404-1** | | |
| **`*Observation.code.coding.display`** | **Physical findings of Hand Narrative** | | |
| **`*Observation.code.coding.system`** | **<http://snomed.info/sct>** | | |
| **`*Observation.code.coding.code`** | **7569003** | | |
| **`*Observation.code.coding.display`** | **Finger structure** | | |
| **`Observation.valueQuantity.value`** | ***(Tipe data String)*** | | |
| **v. Kuku tangan** | | | |
| **`Observation.category[i].coding[i].system`** | **<http://terminology.hl7.org/CodeSystem/observation-category>** | | |
| **`Observation.category[i].coding[i].code`** | **exam** | | |
| **`Observation.category[i].coding[i].display`** | **Exam** | | |
| **`*Observation.code.coding.system`** | **<http://loinc.org>** | | |
| **`*Observation.code.coding.code`** | **32456-6** | | |
| **`*Observation.code.coding.display`** | **Physical findings of Nail** | | |
| **`*Observation.code.coding.system`** | **<http://snomed.info/sct>** | | |
| **`*Observation.code.coding.code`** | **770812000** | | |
| **`*Observation.code.coding.display`** | **Entire nail unit of finger** | | |
| **`Observation.valueQuantity.value`** | ***(Tipe data String)*** | | |
| **w. Persendian tangan** | | | |
| **`Observation.category[i].coding[i].system`** | **<http://terminology.hl7.org/CodeSystem/observation-category>** | | |
| **`Observation.category[i].coding[i].code`** | **exam** | | |
| **`Observation.category[i].coding[i].display`** | **Exam** | | |
| **`*Observation.code.coding.system`** | **<http://loinc.org>** | | |
| **`*Observation.code.coding.code`** | **11415-7** | | |
| **`*Observation.code.coding.display`** | **Physical findings of Wrist Narrative** | | |
| **`Observation.valueQuantity.value`** | ***(Tipe data String)*** | | |
| **x. Tungkai atas** | | | |
| **`Observation.category[i].coding[i].system`** | **<http://terminology.hl7.org/CodeSystem/observation-category>** | | |
| **`Observation.category[i].coding[i].code`** | **exam** | | |
| **`Observation.category[i].coding[i].display`** | **Exam** | | |
| **`*Observation.code.coding.system`** | **<http://loinc.org>** | | |
| **`*Observation.code.coding.code`** | **11414-0** | | |
| **`*Observation.code.coding.display`** | **Physical findings of Thigh Narrative** | | |
| **`Observation.valueQuantity.value`** | ***(Tipe data String)*** | | |
| **y. Tungkai Bawah** | | | |
| **`Observation.category[i].coding[i].system`** | **<http://terminology.hl7.org/CodeSystem/observation-category>** | | |
| **`Observation.category[i].coding[i].code`** | **exam** | | |
| **`Observation.category[i].coding[i].display`** | **Exam** | | |
| **`*Observation.code.coding.system`** | **<http://loinc.org>** | | |
| **`*Observation.code.coding.code`** | **11389-4** | | |
| **`*Observation.code.coding.display`** | **Physical findings of Calf Narrative** | | |
| **`Observation.valueQuantity.value`** | ***(Tipe data String)*** | | |
| **z. Jari Kaki** | | | |
| **`Observation.category[i].coding[i].system`** | **<http://terminology.hl7.org/CodeSystem/observation-category>** | | |
| **`Observation.category[i].coding[i].code`** | **exam** | | |
| **`Observation.category[i].coding[i].display`** | **Exam** | | |
| **`*Observation.code.coding.system`** | **<http://loinc.org>** | | |
| **`*Observation.code.coding.code`** | **11397-7** | | |
| **`*Observation.code.coding.display`** | **Physical findings of Foot Narrative** | | |
| **`*Observation.code.coding.system`** | **<http://snomed.info/sct>** | | |
| **`*Observation.code.coding.code`** | **29707007** | | |
| **`*Observation.code.coding.display`** | **Toe structure** | | |
| **`Observation.valueQuantity.value`** | ***(Tipe data String)*** | | |
| **aa. Kuku Kaki** | | | |
| **`Observation.category[i].coding[i].system`** | **<http://terminology.hl7.org/CodeSystem/observation-category>** | | |
| **`Observation.category[i].coding[i].code`** | **exam** | | |
| **`Observation.category[i].coding[i].display`** | **Exam** | | |
| **`*Observation.code.coding.system`** | **<http://loinc.org>** | | |
| **`*Observation.code.coding.code`** | **32456-6** | | |
| **`*Observation.code.coding.display`** | **Physical findings of Nail** | | |
| **`*Observation.code.coding.system`** | **<http://snomed.info/sct>** | | |
| **`*Observation.code.coding.code`** | **770805009** | | |
| **`*Observation.code.coding.display`** | **Structure of nail unit of toe** | | |
| **`Observation.valueQuantity.value`** | ***(Tipe data String)*** | | |
| **ab. Persendian Kaki** | | | |
| **`Observation.category[i].coding[i].system`** | **<http://terminology.hl7.org/CodeSystem/observation-category>** | | |
| **`Observation.category[i].coding[i].code`** | **exam** | | |
| **`Observation.category[i].coding[i].display`** | **Exam** | | |
| **`*Observation.code.coding.system`** | **<http://loinc.org>** | | |
| **`*Observation.code.coding.code`** | **11385-2** | | |
| **`*Observation.code.coding.display`** | **Physical findings of Ankle Narrative** | | |
| **`*Observation.code.coding.system`** | **<http://snomed.info/sct>** | | |
| **`*Observation.code.coding.code`** | **26552008** | | |
| **`*Observation.code.coding.display`** | **Foot joint structure** | | |
| **`Observation.valueQuantity.value`** | ***(Tipe data String)*** | | |
| **4. Pemeriksaan Antropometri** | | | |
| **a. Tinggi Badan** | | | |
| **`Observation.category[i].coding[i].system`** | **<http://terminology.hl7.org/CodeSystem/observation-category>** | | |
| **`Observation.category[i].coding[i].code`** | **vital-signs** | | |
| **`Observation.category[i].coding[i].display`** | **Vital Signs** | | |
| **`*Observation.code.coding.system`** | **<http://loinc.org>** | | |
| **`*Observation.code.coding.code`** | **8302-2** | | |
| **`*Observation.code.coding.display`** | **Body height** | | |
| **`Observation.valueQuantity.value`** | ***(Tipe data Decimal)*** | | |
| **`Observation.valueQuantity.unit`** | **cm** | | |
| **`Observation.valueQuantity.system`** | **<http://unitsofmeasure.org>** | | |
| **`Observation.valueQuantity.code`** | **cm** | | |
| **b. Berat Badan** | | | |
| **`Observation.category[i].coding[i].system`** | **<http://terminology.hl7.org/CodeSystem/observation-category>** | | |
| **`Observation.category[i].coding[i].code`** | **vital-signs** | | |
| **`Observation.category[i].coding[i].display`** | **Vital Signs** | | |
| **`*Observation.code.coding.system`** | **<http://loinc.org>** | | |
| **`*Observation.code.coding.code`** | **29463-7** | | |
| **`*Observation.code.coding.display`** | **Body weight** | | |
| **`Observation.valueQuantity.value`** | ***(Tipe data Decimal)*** | | |
| **`Observation.valueQuantity.unit`** | **kg** | | |
| **`Observation.valueQuantity.system`** | **<http://unitsofmeasure.org>** | | |
| **`Observation.valueQuantity.code`** | **kg** | | |
| **c. Luas Permukaan Tubuh untuk Anak-Anak** | | | |
| **`Observation.category[i].coding[i].system`** | **<http://terminology.hl7.org/CodeSystem/observation-category>** | | |
| **`Observation.category[i].coding[i].code`** | **vital-signs** | | |
| **`Observation.category[i].coding[i].display`** | **Vital Signs** | | |
| **`*Observation.code.coding.system`** | **<http://loinc.org>** | | |
| **`*Observation.code.coding.code`** | **8277-6** | | |
| **`*Observation.code.coding.display`** | **Body surface area** | | |
| **`Observation.valueQuantity.value`** | ***(Tipe data Decimal)*** | | |
| **`Observation.valueQuantity.unit`** | **m²** | | |
| **`Observation.valueQuantity.system`** | **<http://unitsofmeasure.org>** | | |
| **`Observation.valueQuantity.code`** | **m²** | | |

## 5. Pengiriman Data Pemeriksaan Fungsional

Setelah pemeriksaan fisik, selanjutnya dokter akan melakukan pemeriksaan fungsional. Data hasil pemeriksaan fungsional dapat dikirimkan melalui resource `Observation`. Pemetaan nilai resource `Observation` dapat merujuk pada Data Hasil Pemeriksaan Fisik.

### Pemetaan Variabel dan Terminologi Spesifik

Terminologi spesifik yang digunakan dalam pengiriman data pemeriksaan fungsional melalui resource `Observation` dapat dilihat dalam tabel berikut:

| Pemetaan Variabel *Resource* `Observation` | | | |
| --- | --- | --- | --- |
| **Elemen/*Path* FHIR** | | **Terminologi/Format Pengisian** | |
| **Pemeriksaan Fungsional** | | | |
| **1. Status Psikologis** | | | |
| **`Observation.category[i].coding.system`** | | **<http://terminology.hl7.org/CodeSystem/observation-category>** | |
| **`Observation.category[i].coding.code`** | | **survey** | |
| **`Observation.category[i].coding.display`** | | **Survey** | |
| **`Observation.code.coding.system`** | | **<http://loinc.org>** | |
| **`Observation.code.coding.code`** | | **8693-4** | |
| **`Observation.code.coding.display`** | | **Mental Status** | |
| **`Observation.valueCodeableConcept[i].coding.system`** | **`Observation.valueCodeableConcept[i].coding.code`** | **`Observation.valueCodeableConcept[i].coding.display`** | **Keterangan** |
| **<http://snomed.info/sct>** | **17326005** | **Well in self** | **1. Tidak ada kelainan** |
| **<http://snomed.info/sct>** | **48694002** | **Feeling anxious** | **2. Cemas** |
| **<http://snomed.info/sct>** | **1402001** | **Afraid** | **3. Takut** |
| **<http://snomed.info/sct>** | **75408008** | **Feeling angry** | **4. Marah** |
| **<http://snomed.info/sct>** | **420038007** | **Feeling unhappy** | **5. Sedih** |
| **<http://snomed.info/sct>** | **74964007** | **Other** | **6. Lain-lain (Free Text)** |
| **`Observation.valueCodeableConcept[i].coding.text`** | | ***(Tipe data String)*** | |

## 6. Pengiriman Data Riwayat Perjalanan Penyakit

Data riwayat perjalanan penyakit berisi narasi mengenai perkembangan penyakit yang dialami oleh pasien. Data riwayat perjalanan penyakit dapat dikirimkan melalui resource `ClinicalImpression`.

### Pemetaan Nilai ClinicalImpression

Berikut pemetaan nilai untuk `ClinicalImpression` yang direpresentasikan dalam peta referensi (path) ke properti (element id) terkait:

|  |  |
| --- | --- |
|  | 1. Setiap terdapat simbol asterik `*` sebelum nama variabel/parameter/element FHIR yang disebutkan, maka variabel/parameter/element FHIR tersebut bersifat **WAJIB**, **harus ada**, atau **pasti selalu ada**, contoh: **`*Location.identifier`**. 2. **Standar format Waktu** yang digunakan dalam pengiriman data adalah **UTC +00**. Misalnya waktu **WIB**, maka format yang digunakan adalah **waktu sekarang dikurangi 7**, jika **WITA**, maka **waktu sekarang dikurangi 8**, dan Jika **WIT**, maka **waktu sekarang dikurangi 9**.  **Contoh:** Pukul 17.35 WIB tanggal 23 Agustus 2023 maka yang dikirimkan adalah waktunya perlu diubah ke UTC +00 menjadi 10.35, berarti menjadi `2023-08-23T10:35:00+00:00`. 3. **Standar format pengiriman Tanggal** tidak bisa kurang dari 03 Juni 2014. |

|  |  |
| --- | --- |
|  | Silakan klik setiap teks variabel/parameter/element FHIR pada daftar pemetaan nilai di bawah ini (berwarna **merah**), untuk membaca panduan lebih detail/lanjut ke bagian yang direferensikan. |

- [`ClinicalImpression.identifier`](../../fhir/resources/clinical-impression/#clinicalimpression-identifier)
- [`*ClinicalImpression.status`](../../fhir/resources/clinical-impression/#clinicalimpression-status)
- [`ClinicalImpression.statusReason`](../../fhir/resources/clinical-impression/#clinicalimpression-statusreason)
- [`ClinicalImpression.code`](../../fhir/resources/clinical-impression/#clinicalimpression-code)
- [`ClinicalImpression.description`](../../fhir/resources/clinical-impression/#clinicalimpression-description)
- [`*ClinicalImpression.subject`](../../fhir/resources/clinical-impression/#clinicalimpression-subject)
- [`*ClinicalImpression.encounter`](../../fhir/resources/clinical-impression/#clinicalimpression-encounter)
- [`ClinicalImpression.effective<?>`](../../fhir/resources/clinical-impression/#clinicalimpression-effective)
- [`ClinicalImpression.effectiveDateTime`](../../fhir/resources/clinical-impression/#clinicalimpression-effectivedatetime)
- [`ClinicalImpression.effectivePeriod`](../../fhir/resources/clinical-impression/#clinicalimpression-effectiveperiod)
- [`ClinicalImpression.date`](../../fhir/resources/clinical-impression/#clinicalimpression-date)
- [`ClinicalImpression.assessor`](../../fhir/resources/clinical-impression/#clinicalimpression-assessor)
- [`ClinicalImpression.previous`](../../fhir/resources/clinical-impression/#clinicalimpression-previous)
- [`ClinicalImpression.problem`](../../fhir/resources/clinical-impression/#clinicalimpression-problem)
- [`*ClinicalImpression.investigation.code`](../../fhir/resources/clinical-impression/#clinicalimpression-investigation-code)
- [`ClinicalImpression.investigation.item`](../../fhir/resources/clinical-impression/#clinicalimpression-investigation-item)
- [`ClinicalImpression.protocol`](../../fhir/resources/clinical-impression/#clinicalimpression-protocol)
- [`ClinicalImpression.summary`](../../fhir/resources/clinical-impression/#clinicalimpression-summary)
- [`ClinicalImpression.finding.itemCodeableConcept`](../../fhir/resources/clinical-impression/#clinicalimpression-finding-itemcodeableconcept)
- [`ClinicalImpression.finding.itemReference`](../../fhir/resources/clinical-impression/#clinicalimpression-finding-itemreference)
- [`ClinicalImpression.finding.basis`](../../fhir/resources/clinical-impression/#clinicalimpression-finding-basis)
- [`*ClinicalImpression.prognosisCodeableConcept`](../../fhir/resources/clinical-impression/#clinicalimpression-prognosiscodeableconcept)
- [`ClinicalImpression.prognosisReference`](../../fhir/resources/clinical-impression/#clinicalimpression-prognosisreference)
- [`ClinicalImpression.supportingInfo`](../../fhir/resources/clinical-impression/#clinicalimpression-supportinginfo)
- [`ClinicalImpression.note`](../../fhir/resources/clinical-impression/#clinicalimpression-note)

Penjelasan tipe mandatoris, deskripsi dan format pengisian dari setiap elemen data/*path* di dalam resource `ClinicalImpression`, dan contoh pengiriman data atau *payload* dari data prognosis dapat dilihat dalam *Postman Collection*.

### Pemetaan Variabel dan Terminologi Spesifik

Terminologi spesifik yang digunakan dalam pengiriman data riwayat perjalanan penyakit melalui resource `ClinicalImpression` dapat dilihat dalam tabel berikut:

Tabel 6. Pemetaan Variabel dan Terminologi Spesifik

| Pemetaan Variabel *Resource* `ClinicalImpression ` | |
| --- | --- |
| **Elemen/Path FHIR** | **Terminologi/Format Pengisian** |
| Riwayat Perjalanan Penyakit | |
| `ClinicalImpression.code.coding.system` | <http://snomed.info/sct> |
| `ClinicalImpression.code.coding.code` | 312850006 |
| `ClinicalImpression.code.coding.display` | History of disorder |
| `ClinicalImpression.summary` | *(Tipe data string)* |

## 7. Pengiriman Data Tujuan Perawatan

Data tujuan perawatan berisi detail sasaran yang ingin dicapai dalam perawatan pasien. Data tujuan perawatan dapat dikirimkan melalui resource `Goal`.

### Pemetaan Nilai Goal

Berikut pemetaan nilai untuk `Goal` yang direpresentasikan dalam peta referensi (path) ke properti (element id) terkait:

|  |  |
| --- | --- |
|  | 1. Setiap terdapat simbol asterik `*` sebelum nama variabel/parameter/element FHIR yang disebutkan, maka variabel/parameter/element FHIR tersebut bersifat **WAJIB**, **harus ada**, atau **pasti selalu ada**, contoh: **`*Location.identifier`**. 2. **Standar format Waktu** yang digunakan dalam pengiriman data adalah **UTC +00**. Misalnya waktu **WIB**, maka format yang digunakan adalah **waktu sekarang dikurangi 7**, jika **WITA**, maka **waktu sekarang dikurangi 8**, dan Jika **WIT**, maka **waktu sekarang dikurangi 9**.  **Contoh:** Pukul 17.35 WIB tanggal 23 Agustus 2023 maka yang dikirimkan adalah waktunya perlu diubah ke UTC +00 menjadi 10.35, berarti menjadi `2023-08-23T10:35:00+00:00`. 3. **Standar format pengiriman Tanggal** tidak bisa kurang dari 03 Juni 2014. |

|  |  |
| --- | --- |
|  | Silakan klik setiap teks variabel/parameter/element FHIR pada daftar pemetaan nilai di bawah ini (berwarna **merah**), untuk membaca panduan lebih detail/lanjut ke bagian yang direferensikan. |

- [`Goal.identifier`](../../fhir/resources/goal/#goal-identifier)
- [`*Goal.lifecycleStatus`](../../fhir/resources/goal/#goal-lifecyclestatus)
- [`Goal.achievementStatus`](../../fhir/resources/goal/#goal-achievementstatus)
- [`Goal.category`](../../fhir/resources/goal/#goal-category)
- [`Goal.priority`](../../fhir/resources/goal/#goal-priority)
- [`*Goal.description`](../../fhir/resources/goal/#goal-description)
- [`*Goal.subject`](../../fhir/resources/goal/#goal-subject)
- [`Goal.start[x]`](../../fhir/resources/goal/#goal-start)
- [`Goal.startDate`](../../fhir/resources/goal/#goal-startdate)
- [`Goal.startCodeableConcept`](../../fhir/resources/goal/#goal-startcodeableconcept)
- [`Goal.target`](../../fhir/resources/goal/#goal-target)
- [`Goal.target.measure`](../../fhir/resources/goal/#goal-target-measure)
- [`Goal.target.detail[x]`](../../fhir/resources/goal/#goal-target-detail)
- [`Goal.target.detailQuantity`](../../fhir/resources/goal/#goal-target-detailquantity)
- [`Goal.target.detailRange`](../../fhir/resources/goal/#goal-target-detailrange)
- [`Goal.target.detailCodeableConcept`](../../fhir/resources/goal/#goal-target-detailcodeableconcept)
- [`Goal.target.detailString`](../../fhir/resources/goal/#goal-target-detailstring)
- [`Goal.target.detailBoolean`](../../fhir/resources/goal/#goal-target-detailboolean)
- [`Goal.target.detailInteger`](../../fhir/resources/goal/#goal-target-detailinteger)
- [`Goal.target.detailRatio`](../../fhir/resources/goal/#goal-target-detailratio)
- [`Goal.target.due[x]`](../../fhir/resources/goal/#goal-target-due)
- [`Goal.target.dueDate`](../../fhir/resources/goal/#goal-target-duedate)
- [`Goal.target.dueDuration`](../../fhir/resources/goal/#goal-target-dueduration)
- [`Goal.statusDate`](../../fhir/resources/goal/#goal-statusdate)
- [`Goal.statusReason`](../../fhir/resources/goal/#goal-statusreason)
- [`Goal.expressedBy`](../../fhir/resources/goal/#goal-expressedby)
- [`Goal.addresses`](../../fhir/resources/goal/#goal-addresses)
- [`Goal.note`](../../fhir/resources/goal/#goal-note)
- [`Goal.outcomeCode`](../../fhir/resources/goal/#goal-outcomecode)
- [`Goal.outcomeReference`](../../fhir/resources/goal/#goal-outcomereference)

### Pemetaan Variabel dan Terminologi Spesifik

Terminologi spesifik yang digunakan dalam pengiriman data tujuan perawatan melalui resource `Goal` dapat dilihat dalam tabel berikut:

Tabel 7. Pemetaan Variabel dan Terminologi Spesifik

| Pemetaan Variabel *Resource* `Goal` | |
| --- | --- |
| **Elemen/Path FHIR** | **Terminologi/Format Pengisian** |
| 1. Tujuan Perawatan | |
| `Goal.lifecycleStatus` | *planned* |
| `Goal.achievementStatus.system` | <http://terminology.hl7.org/CodeSystem/goal-achievement> |
| `Goal.achievementStatus.code` | Kode ketercapaian tujuan  Kode dapat diisi dengan kode ketercapaian tujuan dari FHIR Terminology.  (Untuk Kode Lengkapnya dapat dilihat pada Dokumen Lampiran [Standar Terminologi](../../terminology/standar-terminologi/#standar-terminologi) SATUSEHAT) |
| `Goal.achievementStatus.display` | Deskripsi ketercapaian tujuan |
| `Goal.category.coding.system` | <http://terminology.hl7.org/CodeSystem/goal-category> |
| `Goal.category.coding.code` | nursing |
| `Goal.category.coding.display` | Nursing |
| `Goal.addresses` | Referensi ke resource `Condition` |
| `Goal.description.coding.system` | <http://snomed.info/sct> |
| `Goal.description.coding.code` | SNOMED-CT Code  Ruang lingkup kode SNOMED CT yang dapat dipakai: Expression Constraint Language (ECL) Query : < 404684003 |Clinical finding (finding)|  (Untuk Kode Lengkapnya dapat dilihat pada Dokumen Lampiran [Standar Terminologi](../../terminology/standar-terminologi/#standar-terminologi) SATUSEHAT) |
| `Goal.description.coding.display` | SNOMED-CT Description |
| `Goal.outcomeCode.system` | <http://snomed.info/sct> |
| `Goal.outcomeCode.code` | SNOMED-CT Code  Ruang lingkup kode SNOMED CT yang dapat dipakai: Expression Constraint Language (ECL) Query : < 390800000 | Goal achievement finding (finding) |  (Untuk Kode Lengkapnya dapat dilihat pada Dokumen Lampiran [Standar Terminologi](../../terminology/standar-terminologi/#standar-terminologi) SATUSEHAT) |
| `Goal.outcomeCode.display` | SNOMED-CT Description |
| `Goal.outcomeReference` | Referensi ke resource `Observation` |
| `Goal.target.measure.system` | <http://loinc.org> |
| `Goal.target.measure.code` | LOINC Code  (Untuk ketentuan lebih lanjut dapat dilihat pada Dokumen Lampiran [Standar Terminologi](../../terminology/standar-terminologi/#standar-terminologi) SATUSEHAT) |
| `Goal.target.measure.display` | LOINC Description |
| `Goal.target.detail[x]` | Detail target kuantitatif, dapat menggunakan tipe data `Quantity` | `Range` | `CodeableConcept` | `String` | `Boolean` | `Integer` | `Ratio` |
| `Goal.target.dueDate` | (Tipe data *dateTime*) |
| `Goal.expressedBy` | Referensi ke resource `Practitioner` |

## 8. Pengiriman Data Rencana Rawat Pasien

Rencana Rawat Pasien merupakan variabel yang mencakup Rencana tata laksana perawatan pasien, ringkasan cara rawatan (rencana terapi, rencana tindakan, rencana lama hari rawat). Data tersebut dapat dikirimkan menggunakan resource [`CarePlan`](../../fhir/resources/care-plan/#careplan).

### Pemetaan Nilai CarePlan

Berikut pemetaan nilai untuk `CarePlan` yang direpresentasikan dalam peta referensi (*path*) ke properti (*element id*) terkait, untuk konteks pengiriman data rencana tindak lanjut:

|  |  |
| --- | --- |
|  | 1. Setiap terdapat simbol asterik `*` sebelum nama variabel/parameter/element FHIR yang disebutkan, maka variabel/parameter/element FHIR tersebut bersifat **WAJIB**, **harus ada**, atau **pasti selalu ada**, contoh: **`*Location.identifier`**. 2. **Standar format Waktu** yang digunakan dalam pengiriman data adalah **UTC +00**. Misalnya waktu **WIB**, maka format yang digunakan adalah **waktu sekarang dikurangi 7**, jika **WITA**, maka **waktu sekarang dikurangi 8**, dan Jika **WIT**, maka **waktu sekarang dikurangi 9**.  **Contoh:** Pukul 17.35 WIB tanggal 23 Agustus 2023 maka yang dikirimkan adalah waktunya perlu diubah ke UTC +00 menjadi 10.35, berarti menjadi `2023-08-23T10:35:00+00:00`. 3. **Standar format pengiriman Tanggal** tidak bisa kurang dari 03 Juni 2014. |

|  |  |
| --- | --- |
|  | Silakan klik setiap teks variabel/parameter/element FHIR pada daftar pemetaan nilai di bawah ini (berwarna **merah**), untuk membaca panduan lebih detail/lanjut ke bagian yang direferensikan. |

- [`CarePlan.identifier`](../../fhir/resources/care-plan/#careplan-identifier)
- [`CarePlan.instantiatesCanonical`](../../fhir/resources/care-plan/#careplan-instantiatescanonical)
- [`CarePlan.instantiatesUri`](../../fhir/resources/care-plan/#careplan-instantiatesuri)
- [`CarePlan.basedOn`](../../fhir/resources/care-plan/#careplan-basedon)
- [`CarePlan.replaces`](../../fhir/resources/care-plan/#careplan-replaces)
- [`CarePlan.partOf`](../../fhir/resources/care-plan/#careplan-partof)
- [`*CarePlan.status`](../../fhir/resources/care-plan/#careplan-status)
- [`*CarePlan.intent`](../../fhir/resources/care-plan/#careplan-intent)
- [`CarePlan.category`](../../fhir/resources/care-plan/#careplan-category)
- [`*CarePlan.title`](../../fhir/resources/care-plan/#careplan-title)
- [`*CarePlan.description`](../../fhir/resources/care-plan/#careplan-description)
- [`*CarePlan.subject`](../../fhir/resources/care-plan/#careplan-subject)
- [`*CarePlan.encounter`](../../fhir/resources/care-plan/#careplan-encounter)
- [`CarePlan.period`](../../fhir/resources/care-plan/#careplan-period)
- [`CarePlan.created`](../../fhir/resources/care-plan/#careplan-created)
- [`*CarePlan.author`](../../fhir/resources/care-plan/#careplan-author)
- [`CarePlan.contributor`](../../fhir/resources/care-plan/#careplan-contributor)
- [`CarePlan.careTeam`](../../fhir/resources/care-plan/#careplan-careteam)
- [`CarePlan.addresses`](../../fhir/resources/care-plan/#careplan-addresses)
- [`CarePlan.supportingInfo`](../../fhir/resources/care-plan/#careplan-supportinginfo)
- [`CarePlan.goal`](../../fhir/resources/care-plan/#careplan-goal)
- [`CarePlan.activity`](../../fhir/resources/care-plan/#careplan-activity)
- [`CarePlan.activity[i].outcomeCodeableConcept`](../../fhir/resources/care-plan/#careplan-activity-outcomecodeableconcept)
- [`CarePlan.activity[i].outcomeReference`](../../fhir/resources/care-plan/#careplan-activity-outcomereference)
- [`CarePlan.activity[i].progress`](../../fhir/resources/care-plan/#careplan-activity-progress)
- [`CarePlan.activity[i].reference`](../../fhir/resources/care-plan/#careplan-activity-reference)
- [`CarePlan.activity[i].detail`](../../fhir/resources/care-plan/#careplan-activity-detail)
- [`CarePlan.activity[i].detail.kind`](../../fhir/resources/care-plan/#careplan-activity-detail-kind)
- [`CarePlan.activity[i].detail.instantiatesCanonical`](../../fhir/resources/care-plan/#careplan-activity-detail-instantiatescanonical)
- [`CarePlan.activity[i].detail.instantiatesUri`](../../fhir/resources/care-plan/#careplan-activity-detail-instantiatesuri)
- [`CarePlan.activity[i].detail.code`](../../fhir/resources/care-plan/#careplan-activity-detail-code)
- [`CarePlan.activity[i].detail.reasonCode`](../../fhir/resources/care-plan/#careplan-activity-detail-reasoncode)
- [`CarePlan.activity[i].detail.reasonReference`](../../fhir/resources/care-plan/#careplan-activity-detail-reasonreference)
- [`CarePlan.activity[i].detail.goal`](../../fhir/resources/care-plan/#careplan-activity-detail-goal)
- [`*CarePlan.activity[i].detail.status`](../../fhir/resources/care-plan/#careplan-activity-detail-status)
- [`CarePlan.activity[i].detail.statusReason`](../../fhir/resources/care-plan/#careplan-activity-detail-statusreason)
- [`CarePlan.activity.detail.doNotPerform`](../../fhir/resources/care-plan/#careplan-activity-detail-donotperform)
- [`CarePlan.activity[i].detail.scheduled[x]`](../../fhir/resources/care-plan/#careplan-activity-detail-scheduled)
- [`CarePlan.activity[i].detail.scheduledTiming`](../../fhir/resources/care-plan/#careplan-activity-detail-scheduledtiming)
- [`CarePlan.activity[i].detail.scheduledPeriod`](../../fhir/resources/care-plan/#careplan-activity-detail-scheduledperiod)
- [`CarePlan.activity[i].detail.scheduledString`](../../fhir/resources/care-plan/#careplan-activity-detail-scheduledstring)
- [`CarePlan.activity[i].detail.location`](../../fhir/resources/care-plan/#careplan-activity-detail-location)
- [`CarePlan.activity[i].detail.performer`](../../fhir/resources/care-plan/#careplan-activity-detail-performer)
- [`CarePlan.activity[i].detail.product[x]`](../../fhir/resources/care-plan/#careplan-activity-detail-product)
- [`CarePlan.activity[i].detail.productCodeableConcept`](../../fhir/resources/care-plan/#careplan-activity-detail-productcodeableconcept)
- [`CarePlan.activity[i].detail.productReference`](../../fhir/resources/care-plan/#careplan-activity-detail-productreference)
- [`CarePlan.activity[i].detail.dailyAmount`](../../fhir/resources/care-plan/#careplan-activity-detail-dailyamount)
- [`CarePlan.activity[i].detail.quantity`](../../fhir/resources/care-plan/#careplan-activity-detail-quantity)
- [`CarePlan.activity[i].detail.description`](../../fhir/resources/care-plan/#careplan-activity-detail-description)
- [`CarePlan.note`](../../fhir/resources/care-plan/#careplan-note)

Penjelasan tipe mandatoris, deskripsi dan format pengisian dari setiap elemen data/*path* di dalam resource `CarePlan`, dan contoh pengiriman data atau *payload* dari pengiriman data alergi dapat dilihat dalam Postman Collection.

### Pemetaan Variabel dan Terminologi Spesifik

Terminologi spesifik yang digunakan dalam pengiriman Rencana Rawat melalui resource `CarePlan` dapat dilihat dalam tabel berikut:

Tabel 8. Pemetaan Variabel dan Terminologi Spesifik

| Pemetaan Variabel *Resource* `CarePlan` | |
| --- | --- |
| **Elemen/Path FHIR** | **Terminologi/Format Pengisian** |
| 1. Rencana Rawat | |
| `CarePlan.category.coding.system` | <http://snomed.info/sct> |
| `CarePlan.category.coding.code` | 736271009 |
| `CarePlan.category.coding.display` | Outpatient care plan |
| `CarePlan.description` | *(Tipe data String)* |
| `CarePlan.goal` | Referensi ke `Goal` |

## 9. Pengiriman Data Instruksi Medik dan Keperawatan

Data Instruksi Medik dan Keperawatan menjelaskan penjabaran instruksi dari rencana tata laksana perawatan pasien, keterangan rinci terkait dengan tindakan medis dan keperawatan. Instruksi medik dan keperawatan ini dapat dikirimkan harian sebagai pencatatan dari asuhan keperawatan pasien. Pengiriman data instruksi medik dan keperawatan dikirimkan menggunakan resource [`CarePlan`](../../fhir/resources/care-plan/#careplan). Pemetaan Nilai resource [`CarePlan`](../../fhir/resources/care-plan/#careplan) dapat dilihat pada Bab 3. Rencana Rawat.

### Pemetaan Variabel dan Terminologi Spesifik

Terminologi spesifik yang digunakan dalam pengiriman data Instruksi Medik dan Keperawatan melalui resource `CarePlan` dapat dilihat dalam tabel berikut:

Tabel 9. Pemetaan Variabel dan Terminologi Spesifik

| Pemetaan Variabel *Resource* `CarePlan` | |
| --- | --- |
| **Elemen/Path FHIR** | **Terminologi/Format Pengisian** |
| 1. Instruksi Medik dan Keperawatan | |
| `CarePlan.category.coding.system` | <http://snomed.info/sct> |
| `CarePlan.category.coding.code` | 736271009 |
| `CarePlan.category.coding.display` | Outpatient care plan |
| `CarePlan.description` | *(Tipe data String)* |

## 10. Pengiriman Data Pemeriksaan Penunjang Laboratorium

Data pemeriksaan penunjang mencakup pemeriksaan laboratorium dan radiologi yang dilakukan terhadap seorang pasien. Berikut alur integrasi dan pemetaan nilai pengiriman data pemeriksaan penunjang laboratorium.

### Skema Pengiriman Data Terkait Pemeriksaan Penunjang Laboratorium

Pengiriman data terkait pemeriksaan penunjang memiliki 2 skema, yaitu:

1. Pemeriksaan Penunjang Tunggal

   1. Data yang perlu dikirimkan, yaitu:

      1. 1 data permintaan (`ServiceRequest`)
      2. 1 data spesimen (`Specimen`)
      3. 1 data hasil pemeriksaan (`Observation`)
      4. 1 data laporan pemeriksaan (`DiagnosticReport`) Data permintaan (`ServiceRequest`), data spesimen (`Specimen`), dan data hasil pemeriksaan (`Observation`) akan di referensi dalam data laporan pemeriksaan (`DiagnosticReport`)

![Pemeriksaan Penunjang Tunggal](../_images/penunjang-tunggal.png)

Gambar 6. Skema Pemeriksaan Penunjang Tunggal

2. Pemeriksaan Penunjang Panel/Paket

   1. Contoh kasus: Seorang dokter melakukan permintaan pemeriksaan panel elektrolit darah yang terdiri dari 3 parameter yaitu natrium, kalium, dan klorida darah. Maka, data yang perlu dikirimkan yaitu:

      1. 1 data permintaan (`ServiceRequest`) dengan kode LOINC untuk panel elektrolit darah
      2. 1 data spesimen (`Specimen`)
      3. 3 data hasil pemeriksaan (`Observation`) terdiri dari kode LOINC untuk natrium darah, kalium darah, klorida darah
      4. 1 data laporan pemeriksaan (`DiagnosticReport`) dengan kode LOINC untuk panel elektrolit darah. 3 data hasil pemeriksaan (`Observation`) akan di referensi dalam data `DiagnosticReport`.

![Pemeriksaan Penunjang Panel](../_images/penunjang-panel.png)

Gambar 7. Skema Pemeriksaan Penunjang Panel

### Pengiriman Data Permintaan Pemeriksaan Penunjang Laboratorium

Sebelum melakukan pemeriksaan penunjang seperti laboratorium, diperlukan langkah permintaan pemeriksaan penunjang. Pengiriman data terkait permintaan pemeriksaan penunjang dapat dilakukan menggunakan resource [`ServiceRequest`](../../fhir/resources/service-request/#servicerequest). Data permintaan pemeriksaan penunjang laboratorium yang dapat dikirimkan antara lain nama pemeriksaan, pasien terkait, kunjungan terkait, tanggal permintaan akan dilakukan, tanggal permintaan dibuat, dan tenaga kesehatan yang melakukan permintaan.

Kode LOINC atau kode Pemeriksaan Penunjang Nasional digunakan pada elemen `ServiceRequest.code` untuk merepresentasikan nama pemeriksaan yang diminta. Referensi pemetaan pemeriksaan laboratorium dengan kode LOINC dapat dilihat melalui [**Lampiran LOINC Laboratorium**](https://s.kemkes.go.id/LampiranLOINC-Lab). Gunakan parameter pemeriksaan dengan kategori “Permintaan” atau “Permintaan & Hasil” pada *file* Terminologi Laboratorium ketika mengirimkan data melalui resource [`ServiceRequest`](../../fhir/resources/service-request/#servicerequest).

Satu *payload* atau satu *record* dari resource `ServiceRequest` hanya dapat digunakan untuk 1 kode/permintaan parameter laboratorium. Sehingga, apabila dilakukan permintaan 2 parameter laboratorium, sebagai contoh panel elektrolit dan hemoglobin, maka perlu mengirimkan 2 *payload* di mana 1 *payload* berisi 1 kode panel elektrolit dan 1 *payload* berisi kode parameter hemoglobin.

Berikut pemetaan nilai untuk `ServiceRequest` yang direpresentasikan dalam peta referensi *(path)* ke properti *(element id)* terkait, untuk konteks jenis perawatan:

|  |  |
| --- | --- |
|  | 1. Setiap terdapat simbol asterik `*` sebelum nama variabel/parameter/element FHIR yang disebutkan, maka variabel/parameter/element FHIR tersebut bersifat **WAJIB**, **harus ada**, atau **pasti selalu ada**, contoh: **`*Location.identifier`**. 2. **Standar format Waktu** yang digunakan dalam pengiriman data adalah **UTC +00**. Misalnya waktu **WIB**, maka format yang digunakan adalah **waktu sekarang dikurangi 7**, jika **WITA**, maka **waktu sekarang dikurangi 8**, dan Jika **WIT**, maka **waktu sekarang dikurangi 9**.  **Contoh:** Pukul 17.35 WIB tanggal 23 Agustus 2023 maka yang dikirimkan adalah waktunya perlu diubah ke UTC +00 menjadi 10.35, berarti menjadi `2023-08-23T10:35:00+00:00`. 3. **Standar format pengiriman Tanggal** tidak bisa kurang dari 03 Juni 2014. |

|  |  |
| --- | --- |
|  | Silakan klik setiap teks variabel/parameter/element FHIR pada daftar pemetaan nilai di bawah ini (berwarna **merah**), untuk membaca panduan lebih detail/lanjut ke bagian yang direferensikan. |

- [`ServiceRequest.identifier`](../../fhir/resources/service-request/#servicerequest-identifier)
- [`ServiceRequest.basedOn`](../../fhir/resources/service-request/#servicerequest-basedon)
- [`ServiceRequest.replaces`](../../fhir/resources/service-request/#servicerequest-replaces)
- [`ServiceRequest.requisition`](../../fhir/resources/service-request/#servicerequest-requisition)
- [`*ServiceRequest.status`](../../fhir/resources/service-request/#servicerequest-status)
- [`*ServiceRequest.intent`](../../fhir/resources/service-request/#servicerequest-intent)
- [`ServiceRequest.category`](../../fhir/resources/service-request/#servicerequest-category)
- [`ServiceRequest.priority`](../../fhir/resources/service-request/#servicerequest-priority)
- [`ServiceRequest.doNotPerform`](../../fhir/resources/service-request/#servicerequest-donotperform)
- [`*ServiceRequest.code`](../../fhir/resources/service-request/#servicerequest-code)
- [`ServiceRequest.orderDetail`](../../fhir/resources/service-request/#servicerequest-orderdetail)
- [`ServiceRequest.quantityQuantity`](../../fhir/resources/service-request/#servicerequest-quantityquantity)
- [`ServiceRequest.quantityRatio`](../../fhir/resources/service-request/#servicerequest-quantityratio)
- [`ServiceRequest.quantityRange`](../../fhir/resources/service-request/#servicerequest-quantityrange)
- [`*ServiceRequest.subject`](../../fhir/resources/service-request/#servicerequest-subject)
- [`*ServiceRequest.encounter`](../../fhir/resources/service-request/#servicerequest-encounter)
- [`ServiceRequest.occurrenceDateTime`](../../fhir/resources/service-request/#servicerequest-occurrencedatetime)
- [`ServiceRequest.occurrencePeriod`](../../fhir/resources/service-request/#servicerequest-occurrenceperiod)
- [`ServiceRequest.occurrenceTiming`](../../fhir/resources/service-request/#servicerequest-occurrencetiming)
- [`ServiceRequest.asNeededBoolean`](../../fhir/resources/service-request/#servicerequest-asneededboolean)
- [`ServiceRequest.authoredOn`](../../fhir/resources/service-request/#servicerequest-authoredon)
- [`*ServiceRequest.requester`](../../fhir/resources/service-request/#servicerequest-requester)
- [`ServiceRequest.performerType`](../../fhir/resources/service-request/#servicerequest-performertype)
- [`*ServiceRequest.performer`](../../fhir/resources/service-request/#servicerequest-performer)
- [`ServiceRequest.locationCode`](../../fhir/resources/service-request/#servicerequest-locationcode)
- [`ServiceRequest.locationReference`](../../fhir/resources/service-request/#servicerequest-locationreference)
- [`ServiceRequest.reasonCode`](../../fhir/resources/service-request/#servicerequest-reasoncode)
- [`ServiceRequest.reasonReference`](../../fhir/resources/service-request/#servicerequest-reasonreference)
- [`ServiceRequest.insurance`](../../fhir/resources/service-request/#servicerequest-insurance)
- [`ServiceRequest.supportingInfo`](../../fhir/resources/service-request/#servicerequest-supportinginfo)
- [`ServiceRequest.specimen`](../../fhir/resources/service-request/#servicerequest-specimen)
- [`ServiceRequest.bodySite`](../../fhir/resources/service-request/#servicerequest-bodysite)
- [`ServiceRequest.note`](../../fhir/resources/service-request/#servicerequest-note)
- [`ServiceRequest.patientInstruction`](../../fhir/resources/service-request/#servicerequest-patientinstruction)
- [`ServiceRequest.relevantHistory`](../../fhir/resources/service-request/#servicerequest-relevanthistory)

Penjelasan tipe mandatoris, deskripsi dan format pengisian dari setiap elemen data/*path* di dalam resource `ServiceRequest` (data permintaan pemeriksaan penunjang laboratorium), dapat dilihat dalam resource [`ServiceRequest`](../../fhir/resources/service-request/#servicerequest). Untuk contoh pengiriman data atau *payload* dari `ServiceRequest` dapat dilihat dalam [Postman SATUSEHAT](../../postman-workshop/#postman-collection-satusehat) SATUSEHAT.

### Pengiriman Data Spesimen

Pengiriman data spesimen yang digunakan pada pemeriksaan laboratorium dapat dikirimkan menggunakan resource [`Specimen`](../../fhir/resources/specimen/#specimen). Data spesimen yang dapat dikirimkan antara lain jenis spesimen, waktu pengambilan spesimen, metode pengambilan spesimen, pasien terkait, kunjungan terkait, waktu spesimen diterima, tenaga kesehatan yang melakukan pengambilan sampel, permintaan terkait.

Jika terdapat proses fiksasi pada spesimen, maka data mengenai cairan fiksasi yang digunakan dapat dikirimkan dengan {resources} `Substance`.

Satu *payload* atau satu *record* dari resource `Specimen` hanya dapat digunakan untuk 1 kode jenis spesimen. Sehingga, apabila diambil 2 jenis spesimen, sebagai contoh spesimen darah dan urin, maka perlu mengirimkan 2 *payload* di mana 1 *payload* berisi 1 kode spesimen darah dan 1 *payload* berisi kode spesimen urin.

#### Pemetaan Nilai Substance

Berikut pemetaan nilai untuk `Substance` yang direpresentasikan dalam peta referensi (*path*) ke properti (*element id*) terkait, untuk mengirimkan representasi data material atau zat homogen dengan komposisi tertentu:

|  |  |
| --- | --- |
|  | 1. Setiap terdapat simbol asterik `*` sebelum nama variabel/parameter/element FHIR yang disebutkan, maka variabel/parameter/element FHIR tersebut bersifat **WAJIB**, **harus ada**, atau **pasti selalu ada**, contoh: **`*Location.identifier`**. 2. **Standar format Waktu** yang digunakan dalam pengiriman data adalah **UTC +00**. Misalnya waktu **WIB**, maka format yang digunakan adalah **waktu sekarang dikurangi 7**, jika **WITA**, maka **waktu sekarang dikurangi 8**, dan Jika **WIT**, maka **waktu sekarang dikurangi 9**.  **Contoh:** Pukul 17.35 WIB tanggal 23 Agustus 2023 maka yang dikirimkan adalah waktunya perlu diubah ke UTC +00 menjadi 10.35, berarti menjadi `2023-08-23T10:35:00+00:00`. 3. **Standar format pengiriman Tanggal** tidak bisa kurang dari 03 Juni 2014. |

|  |  |
| --- | --- |
|  | Silakan klik setiap teks variabel/parameter/element FHIR pada daftar pemetaan nilai di bawah ini (berwarna **merah**), untuk membaca panduan lebih detail/lanjut ke bagian yang direferensikan. |

- [`Substance.identifier`](../../fhir/resources/substance/#substance-identifier)
- [`*Substance.status`](../../fhir/resources/substance/#substance-status)
- [`*Substance.category`](../../fhir/resources/substance/#substance-category)
- [`*Substance.code`](../../fhir/resources/substance/#substance-code)
- [`Substance.description`](../../fhir/resources/substance/#substance-description)
- [`Substance.instance`](../../fhir/resources/substance/#substance-instance)
- [`Substance.instance.identifier`](../../fhir/resources/substance/#substance-instance-identifier)
- [`Substance.instance.expiry`](../../fhir/resources/substance/#substance-instance-expiry)
- [`Substance.instance.quantity`](../../fhir/resources/substance/#substance-instance-quantity)
- [`Substance.ingredient`](../../fhir/resources/substance/#substance-ingredient)
- [`Substance.ingredient.quantity`](../../fhir/resources/substance/#substance-ingredient-quantity)
- [`Substance.ingredient.substance[x]`](../../fhir/resources/substance/#substance-ingredient-substance)
- [`Substance.ingredient.substanceCodeableConcept`](../../fhir/resources/substance/#substance-ingredient-substancecodeableconcept)
- [`Substance.ingredient.substanceReference`](../../fhir/resources/substance/#substance-ingredient-substancereference)

#### Pemetaan Nilai Specimen

Berikut pemetaan nilai untuk `Specimen` yang direpresentasikan dalam peta referensi *(path)* ke properti *(element id)* terkait, untuk konteks Pengiriman Data Spesimen:

|  |  |
| --- | --- |
|  | 1. Setiap terdapat simbol asterik `*` sebelum nama variabel/parameter/element FHIR yang disebutkan, maka variabel/parameter/element FHIR tersebut bersifat **WAJIB**, **harus ada**, atau **pasti selalu ada**, contoh: **`*Location.identifier`**. 2. **Standar format Waktu** yang digunakan dalam pengiriman data adalah **UTC +00**. Misalnya waktu **WIB**, maka format yang digunakan adalah **waktu sekarang dikurangi 7**, jika **WITA**, maka **waktu sekarang dikurangi 8**, dan Jika **WIT**, maka **waktu sekarang dikurangi 9**.  **Contoh:** Pukul 17.35 WIB tanggal 23 Agustus 2023 maka yang dikirimkan adalah waktunya perlu diubah ke UTC +00 menjadi 10.35, berarti menjadi `2023-08-23T10:35:00+00:00`. 3. **Standar format pengiriman Tanggal** tidak bisa kurang dari 03 Juni 2014. |

|  |  |
| --- | --- |
|  | Silakan klik setiap teks variabel/parameter/element FHIR pada daftar pemetaan nilai di bawah ini (berwarna **merah**), untuk membaca panduan lebih detail/lanjut ke bagian yang direferensikan. |

- [`Specimen.identifier`](../../fhir/resources/specimen/#specimen-identifier)
- [`Specimen.accessionIdentifier`](../../fhir/resources/specimen/#specimen-accessionidentifier)
- [`*Specimen.status`](../../fhir/resources/specimen/#specimen-status)
- [`*Specimen.type`](../../fhir/resources/specimen/#specimen-type)
- [`*Specimen.subject`](../../fhir/resources/specimen/#specimen-subject)
- [`Specimen.receivedTime`](../../fhir/resources/specimen/#specimen-receivedtime)
- [`Specimen.parent`](../../fhir/resources/specimen/#specimen-parent)
- [`Specimen.request`](../../fhir/resources/specimen/#specimen-request)
- [`Specimen.collection.collector`](../../fhir/resources/specimen/#specimen-collection-collector)
- [`Spec imen.collection.collected<?>`](../../fhir/resources/specimen/#specimen-collection-collected)
- [`Specimen.collection.collectedDateTime`](../../fhir/resources/specimen/#specimen-collection-collecteddatetime)
- [`Specimen.collection.collectedPeriod`](../../fhir/resources/specimen/#specimen-collection-collectedperiod)
- [`Specimen.collection.duration`](../../fhir/resources/specimen/#specimen-collection-duration)
- [`Specimen.collection.quantity`](../../fhir/resources/specimen/#specimen-collection-quantity)
- [`Specimen.collection.method`](../../fhir/resources/specimen/#specimen-collection-method)
- [`Specimen.collection.bodySite`](../../fhir/resources/specimen/#specimen-collection-bodysite)
- [`Specimen.collection.fastingStatus<?>`](../../fhir/resources/specimen/#specimen-collection-fastingstatus)
- [`Specimen.collection.fastingStatusCodeableConcept`](../../fhir/resources/specimen/#specimen-collection-fastingstatuscodeableconcept)
- [`Specimen.collection.fastingStatusDuration`](../../fhir/resources/specimen/#specimen-collection-fastingstatusduration)
- [`Specimen.processing`](../../fhir/resources/specimen/#specimen-processing)
- [`Specimen.processing[i].description`](../../fhir/resources/specimen/#specimen-processing-description)
- [`Specimen.processing[i].procedure`](../../fhir/resources/specimen/#specimen-processing-procedure)
- [`Specimen.processing[i].additive`](../../fhir/resources/specimen/#specimen-processing-additive)
- [`Specimen.processing[i].time<?>`](../../fhir/resources/specimen/#specimen-processing-time)
- [`Specimen.processing[i].timeDateTime`](../../fhir/resources/specimen/#specimen-processing-timedatetime)
- [`Specimen.processing[i].timePeriod`](../../fhir/resources/specimen/#specimen-processing-timeperiod)
- [`Specimen.container`](../../fhir/resources/specimen/#specimen-container)
- [`Specimen.container[i].identifier`](../../fhir/resources/specimen/#specimen-container-identifier)
- [`Specimen.container[i].description`](../../fhir/resources/specimen/#specimen-container-description)
- [`Specimen.container[i].type`](../../fhir/resources/specimen/#specimen-container-type)
- [`Specimen.container[i].capacity`](../../fhir/resources/specimen/#specimen-container-capacity)
- [`Specimen.container[i].specimenQuantity`](../../fhir/resources/specimen/#specimen-container-specimenquantity)
- [`Specimen.container[i].additive<?>`](../../fhir/resources/specimen/#specimen-container-additive)
- [`Specimen.container[i].additiveCodeableConcept`](../../fhir/resources/specimen/#specimen-container-additivecodeableconcept)
- [`Specimen.container.additiveReference`](../../fhir/resources/specimen/#specimen-container-additivereference)
- [`Specimen.condition`](../../fhir/resources/specimen/#specimen-condition)
- [`Specimen.note`](../../fhir/resources/specimen/#specimen-note)

Penjelasan tipe mandatoris, deskripsi dan format pengisian dari setiap elemen data/*path* di dalam resource `Specimen` (data permintaan spesimen), dapat dilihat dalam resource [`Specimen`](../../fhir/resources/specimen/#specimen). Untuk contoh pengiriman data atau *payload* dari `ServiceRequest` dapat dilihat dalam [Postman SATUSEHAT](../../postman-workshop/#postman-collection-satusehat) SATUSEHAT.

### Pengiriman Data Hasil Pemeriksaan Penunjang Laboratorium

Hasil pemeriksaan penunjang dapat dikirimkan menggunakan resource [`Observation`](../../fhir/resources/observation/#observation). Berikut adalah ketentuan pengisian data hasil pemeriksaan laboratorium melalui resource [`Observation`](../../fhir/resources/observation/#observation):

1. Kode LOINC atau kode Pemeriksaan Penunjang Nasional digunakan pada elemen `Observation.code` untuk merepresentasikan nama pemeriksaan yang dihasilkan. Referensi pemetaan pemeriksaan laboratorium dengan kode LOINC dapat dilihat melalui [**Lampiran LOINC Laboratorium**](https://s.kemkes.go.id/LampiranLOINC-Lab). Gunakan parameter pemeriksaan dengan kategori “Hasil” atau “Permintaan & Hasil” pada *file* Terminologi Laboratorium ketika mengirimkan data melalui resource [`Observation`](../../fhir/resources/observation/#observation).
2. Elemen `Observation.category.coding` diisi dengan kode *laboratory*.
3. Pemilihan elemen `Observation.value[x]` disesuaikan dengan Tipe hasil pemeriksaan laboratorium.

   1. `Observation.valueCodeableConcept` untuk tipe hasil Nominal
   2. `Observation.valueCodeableConcept` untuk tipe hasil Ordinal
   3. `Observation.valueQuantity` untuk tipe hasil Kuantitatif/*Quantitative*
   4. `Observation.valueString` untuk tipe hasil Naratif/*Narrative*
4. Elemen `Observation.referenceRange` direkomendasikan untuk selalu diisikan guna mempermudah interpretasi hasil laboratorium oleh tenaga kesehatan lainnya. Nilai normal yang dicantumkan disesuaikan dengan nilai normal yang ada dimasing-masing laboratorium berdasarkan alat maupun reagen yang tersedia.

Satu *payload* atau satu *record* dari resource `Observation` hanya dapat digunakan untuk 1 kode hasil parameter laboratorium. Sehingga, apabila terdapat 2 hasil laboratorium, sebagai contoh hasil pemeriksaan hemoglobin dan hematokrit, maka perlu mengirimkan 2 *payload* di mana 1 *payload* berisi 1 kode pemeriksaan hemoglobin dan 1 *payload* berisi kode pemeriksaan hematokrit.

Berikut pemetaan nilai untuk `Observation` yang direpresentasikan dalam peta referensi *(path)* ke properti *(element id)* terkait:

|  |  |
| --- | --- |
|  | 1. Setiap terdapat simbol asterik `*` sebelum nama variabel/parameter/element FHIR yang disebutkan, maka variabel/parameter/element FHIR tersebut bersifat **WAJIB**, **harus ada**, atau **pasti selalu ada**, contoh: **`*Location.identifier`**. 2. **Standar format Waktu** yang digunakan dalam pengiriman data adalah **UTC +00**. Misalnya waktu **WIB**, maka format yang digunakan adalah **waktu sekarang dikurangi 7**, jika **WITA**, maka **waktu sekarang dikurangi 8**, dan Jika **WIT**, maka **waktu sekarang dikurangi 9**.  **Contoh:** Pukul 17.35 WIB tanggal 23 Agustus 2023 maka yang dikirimkan adalah waktunya perlu diubah ke UTC +00 menjadi 10.35, berarti menjadi `2023-08-23T10:35:00+00:00`. 3. **Standar format pengiriman Tanggal** tidak bisa kurang dari 03 Juni 2014. |

|  |  |
| --- | --- |
|  | Silakan klik setiap teks variabel/parameter/element FHIR pada daftar pemetaan nilai di bawah ini (berwarna **merah**), untuk membaca panduan lebih detail/lanjut ke bagian yang direferensikan. |

- [`Observation.identifier`](../../fhir/resources/observation/#observation-identifier)
- [`Observation.basedOn`](../../fhir/resources/observation/#observation-basedon)
- [`Observation.partOf`](../../fhir/resources/observation/#observation-partof)
- [`*Observation.status`](../../fhir/resources/observation/#observation-status)
- [`Observation.category`](../../fhir/resources/observation/#observation-category)
- [`*Observation.code`](../../fhir/resources/observation/#observation-code)
- [`*Observation.subject`](../../fhir/resources/observation/#observation-subject)
- [`Observation.focus`](../../fhir/resources/observation/#observation-focus)
- [`*Observation.encounter`](../../fhir/resources/observation/#observation-encounter)
- [`Observation.effective<?>`](../../fhir/resources/observation/#observation-effective)
- [`Observation.effectiveDateTime`](../../fhir/resources/observation/#observation-effectivedatetime)
- [`Observation.effectivePeriod`](../../fhir/resources/observation/#observation-effectiveperiod)
- [`Observation.effectiveTiming`](../../fhir/resources/observation/#observation-effectivetiming)
- [`Observation.effectiveInstant`](../../fhir/resources/observation/#observation-effectiveinstant)
- [`Observation.issued`](../../fhir/resources/observation/#observation-issued)
- [`*Observation.performer`](../../fhir/resources/observation/#observation-performer)
- [`*Observation.value<x>`](../../fhir/resources/observation/#observation-value)
- [`Observation.valueQuantity`](../../fhir/resources/observation/#observation-valuequantity)
- [`Observation.valueCodeableConcept`](../../fhir/resources/observation/#observation-valuecodeableconcept)
- [`Observation.valueString`](../../fhir/resources/observation/#observation-valuestring)
- [`Observation.valueBoolean`](../../fhir/resources/observation/#observation-valueboolean)
- [`Observation.valueInteger`](../../fhir/resources/observation/#observation-valueinteger)
- [`Observation.valueRange`](../../fhir/resources/observation/#observation-valuerange)
- [`Observation.valueRatio`](../../fhir/resources/observation/#observation-valueratio)
- [`Observation.valueSampledData`](../../fhir/resources/observation/#observation-valuesampleddata)
- [`Observation.valueTime`](../../fhir/resources/observation/#observation-valuetime)
- [`Observation.valueDateTime`](../../fhir/resources/observation/#observation-valuedatetime)
- [`Observation.valuePeriod`](../../fhir/resources/observation/#observation-valueperiod)
- [`Observation.dataAbsentReason`](../../fhir/resources/observation/#observation-dataabsentreason)
- [`Observation.interpretation`](../../fhir/resources/observation/#observation-interpretation)
- [`Observation.note`](../../fhir/resources/observation/#observation-note)
- [`Observation.bodySite`](../../fhir/resources/observation/#observation-bodysite)
- [`Observation.method`](../../fhir/resources/observation/#observation-method)
- [`Observation.specimen`](../../fhir/resources/observation/#observation-specimen)
- [`Observation.device`](../../fhir/resources/observation/#observation-device)
- [`Observation.referenceRange`](../../fhir/resources/observation/#observation-referencerange)
- [`Observation.referenceRange.type`](../../fhir/resources/observation/#observation-referencerange-type)
- [`Observation.hasMember`](../../fhir/resources/observation/#observation-hasmember)
- [`Observation.derivedFrom`](../../fhir/resources/observation/#observation-derivedfrom)

Penjelasan tipe mandatoris, deskripsi dan format pengisian dari setiap elemen data/*path* di dalam resource `Observation` (data hasil pemeriksaan laboratorium), dapat dilihat dalam resource [`Observation`](../../fhir/resources/observation/#observation). Untuk contoh pengiriman data atau *payload* dari `Observation` dapat dilihat dalam [Postman SATUSEHAT](../../postman-workshop/#postman-collection-satusehat) SATUSEHAT.

### Pengiriman Data Laporan Pemeriksaan Penunjang Laboratorium

Laporan hasil pemeriksaan akan dikirimkan melalui resource [`DiagnosticReport`](../../fhir/resources/diagnostic-report/#diagnosticreport). Berikut adalah ketentuan pengisian laporan pemeriksaan penunjang laboratorium melalui resource [`DiagnosticReport`](../../fhir/resources/diagnostic-report/#diagnosticreport):

1. Data di resource `DiagnosticReport` akan mereferensi ke hasil pemeriksaan laboratorium terkait pada resource `Observation` melalui `DiagnosticReport.result`, spesimen terkait pada resource `Specimen` melalui `DiagnosticReport.specimen`, dan permintaan pemeriksaan penunjang terkait pada resource `ServiceRequest` melalui `DiagnosticReport.basedOn`.
2. Kode LOINC atau kode Pemeriksaan Penunjang Nasional digunakan pada elemen `DiagnosticReport.code` untuk merepresentasikan nama pemeriksaan yang dilaporkan. Referensi pemetaan parameter laboratorium ke kode LOINC dapat dilihat melalui [**Lampiran LOINC Laboratorium**](https://s.kemkes.go.id/LampiranLOINC-Lab). Gunakan parameter pemeriksaan dengan kategori “Permintaan” atau “Permintaan & Hasil” pada *file* Terminologi Laboratorium melalui resource [`DiagnosticReport`](../../fhir/resources/diagnostic-report/#diagnosticreport).
3. Kode yang dicantumkan dalam `DiagnosticReport.code` akan sama dengan kode yang dicantumkan pada `ServiceRequest.code` terkait.

Satu *payload* atau satu *record* dari resource `DiagnosticReport` hanya dapat digunakan untuk 1 kode/laporan parameter laboratorium. Sehingga, apabila dilakukan permintaan 2 parameter laboratorium, sebagai contoh panel elektrolit dan hemoglobin, maka perlu mengirimkan 2 *payload* laporan melalui resource [`DiagnosticReport`](../../fhir/resources/diagnostic-report/#diagnosticreport) di mana 1 *payload* berisi 1 kode panel elektrolit dan 1 *payload* berisi kode parameter hemoglobin.

Berikut pemetaan nilai untuk `DiagnosticReport` yang direpresentasikan dalam peta referensi *(path)* ke properti *(element id)* terkait, untuk konteks pengiriman data laporan pemeriksaan penunjang laboratorium:

|  |  |
| --- | --- |
|  | 1. Setiap terdapat simbol asterik `*` sebelum nama variabel/parameter/element FHIR yang disebutkan, maka variabel/parameter/element FHIR tersebut bersifat **WAJIB**, **harus ada**, atau **pasti selalu ada**, contoh: **`*Location.identifier`**. 2. **Standar format Waktu** yang digunakan dalam pengiriman data adalah **UTC +00**. Misalnya waktu **WIB**, maka format yang digunakan adalah **waktu sekarang dikurangi 7**, jika **WITA**, maka **waktu sekarang dikurangi 8**, dan Jika **WIT**, maka **waktu sekarang dikurangi 9**.  **Contoh:** Pukul 17.35 WIB tanggal 23 Agustus 2023 maka yang dikirimkan adalah waktunya perlu diubah ke UTC +00 menjadi 10.35, berarti menjadi `2023-08-23T10:35:00+00:00`. 3. **Standar format pengiriman Tanggal** tidak bisa kurang dari 03 Juni 2014. |

|  |  |
| --- | --- |
|  | Silakan klik setiap teks variabel/parameter/element FHIR pada daftar pemetaan nilai di bawah ini (berwarna **merah**), untuk membaca panduan lebih detail/lanjut ke bagian yang direferensikan. |

- [`DiagnosticReport.identifier`](../../fhir/resources/diagnostic-report/#diagnosticreport-identifier)
- [`*DiagnosticReport.basedOn`](../../fhir/resources/diagnostic-report/#diagnosticreport-basedon)
- [`*DiagnosticReport.status`](../../fhir/resources/diagnostic-report/#diagnosticreport-status)
- [`DiagnosticReport.category[i].coding`](../../fhir/resources/diagnostic-report/#diagnosticreport-category)
- [`*DiagnosticReport.code`](../../fhir/resources/diagnostic-report/#diagnosticreport-code)
- [`*DiagnosticReport.subject`](../../fhir/resources/diagnostic-report/#diagnosticreport-subject)
- [`*DiagnosticReport.encounter`](../../fhir/resources/diagnostic-report/#diagnosticreport-encounter)
- [`DiagnosticReport.effective<?>`](../../fhir/resources/diagnostic-report/#diagnosticreport-effective)
- [`DiagnosticReport.effectiveDateTime`](../../fhir/resources/diagnostic-report/#diagnosticreport-effectiveDateTime)
- [`DiagnosticReport.effectivePeriod`](../../fhir/resources/diagnostic-report/#diagnosticreport-effectivePeriod)
- [`DiagnosticReport.issued`](../../fhir/resources/diagnostic-report/#diagnosticreport-issued)
- [`*DiagnosticReport.performer`](../../fhir/resources/diagnostic-report/#diagnosticreport-performer)
- [`DiagnosticReport.resultsInterpreter`](../../fhir/resources/diagnostic-report/#diagnosticreport-resultsinterpreter)
- [`*DiagnosticReport.specimen`](../../fhir/resources/diagnostic-report/#diagnosticreport-specimen)
- [`*DiagnosticReport.result`](../../fhir/resources/diagnostic-report/#diagnosticreport-result)
- [`DiagnosticReport.imagingStudy`](../../fhir/resources/diagnostic-report/#diagnosticreport-imagingstudy)
- [`DiagnosticReport.media`](../../fhir/resources/diagnostic-report/#diagnosticreport-media)
- [`DiagnosticReport.conclusion`](../../fhir/resources/diagnostic-report/#diagnosticreport-conclusion)
- [`DiagnosticReport.conclusionCode`](../../fhir/resources/diagnostic-report/#diagnosticreport-conclusioncode)
- [`DiagnosticReport.presentedForm`](../../fhir/resources/diagnostic-report/#diagnosticreport-presentedform)

Penjelasan tipe mandatoris, deskripsi dan format pengisian dari setiap elemen data/*path* di dalam resource `DiagnosticReport` (data laporan pemeriksaan laboratorium), dapat dilihat dalam resource [`DiagnosticReport`](../../fhir/resources/diagnostic-report/#diagnosticreport). Untuk contoh pengiriman data atau *payload* dari `DiagnosticReport` dapat dilihat dalam [Postman SATUSEHAT](../../postman-workshop/#postman-collection-satusehat) SATUSEHAT.

### Pemetaan Variabel dan Terminologi Spesifik

Terminologi spesifik yang digunakan dalam pengiriman data pemeriksaan penunjang laboratorium dapat dilihat dalam tabel berikut:

Tabel 10. Terminologi Spesifik

| *Resource* `ServiceRequest`, `Specimen`, `Substance`, `Observation`, `DiagnosticReport` | | |
| --- | --- | --- |
| **Elemen/*Path* FHIR** | **Terminologi/Format Pengisian** | |
| **Permintaan Pemeriksaan Penunjang Laboratorium** | | |
| **1. Nomor Permintaan** | | |
| **`ServiceRequest.identifier.system`** | **<http://sys-ids.kemkes.go.id/servicerequest/{{Organization_ID}}>** | |
| **`ServiceRequest.identifier.value`** | **Nomor Permintaan dengan tipe data string** | |
| **2. Nama Pemeriksaan** | | |
| **`ServiceRequest.category.coding.system`** | **<http://snomed.info/sct>** | |
| **`ServiceRequest.category.coding.code`** | **108252007** | |
| **`ServiceRequest.category.coding.display`** | **Laboratory procedure** | |
| **`ServiceRequest.code.coding.system`** | **<http://loinc.org>** | |
| **`ServiceRequest.code.coding.code`** | **LOINC Code**  **(Untuk ketentuan lebih lanjut dapat dilihat pada Dokumen Lampiran [Standar Terminologi](../../terminology/standar-terminologi/#standar-terminologi) SATUSEHAT)** | |
| **`ServiceRequest.code.coding.display`** | **LOINC Description** | |
| **`ServiceRequest.code.coding.system`** | **<http://terminology.kemkes.go.id/CodeSystem/kptl>** | |
| **`ServiceRequest.code.coding.code`** | **Kode KPTL**  **Ruang lingkup kode KPTL yang dapat dipakai mencakup kode terkait pemeriksaan laboratorium yang bersifat sepadan dengan kode LOINC yang digunakan**  **(Untuk Kode Lengkapnya dapat dilihat pada Buku Panduan Kode Pembiayaan Tindakan dan Layanan Kesehatan (KPTL))** | |
| **`ServiceRequest.code.coding.display`** | **Deskripsi KPTL** | |
| **3. Waktu Permintaan** | | |
| **`ServiceRequest.authoredOn`** | **Tanggal dan waktu permintaan dengan tipe data *dateTime*** | |
| **4. Dokter Pengirim** | | |
| **`ServiceRequest.requester`** | **Referensi ke resource `Practitioner` - ID SATUSEHAT Practitioner** | |
| **5. Nomor Telepon Dokter Pengirim** | | |
| ****Keterangan:** Nomor telepon tenaga kesehatan yang membuat permintaan didapatkan dengan menarik data dari ID SATUSEHAT Practitioner yang direferensikan pada elemen `ServiceRequest.requester`** | | |
| **6. Nama Fasilitas Pelayanan Kesehatan yang Mengirim Spesimen Klinis** | | |
| ****Keterangan:** Nama fasilitas pelayanan kesehatan yang membuat permintaan didapatkan dengan menarik data detail kunjungan dari ID Encounter yang direferensikan pada elemen `ServiceRequest.encounter`** | | |
| **7. Unit Pengirim** | | |
| ****Keterangan:** Unit pengirim didapatkan dengan menarik data detail kunjungan dari ID Encounter yang direferensikan pada elemen `ServiceRequest.encounter`** | | |
| **8. Prioritas Pemeriksaan** | | |
| **`ServiceRequest.priority`** | ***stat*** | ***routine*** |
| **Pilihan jawaban yang divisualisasikan** | **CITO** | **Non CITO** |
| **9. Diagnosis/Masalah** | | |
| **`ServiceRequest.reasonReference`** | **Referensi ke resource `Condition`**  **`ServiceRequest.reasonCode` dapat digunakan jika alasan permintaan tidak dikirimkan dalam *payload* tersendiri** | |
| **10. Catatan Permintaan** | | |
| **`ServiceRequest.note`** | **(Tipe data *string*)** | |
| **11. Data Pendukung Pemeriksaan** | | |
| **`ServiceRequest.supportingInfo`** | **Referensi ke Status Puasa Pasien (`Procedure`)** | |
| **Status Puasa Pasien** | | |
| **`Procedure.category.coding.system`** | **<http://snomed.info/sct>** | |
| **`Procedure.category.coding.code`** | **103693007** | |
| **`Procedure.category.coding.display`** | **Diagnostic procedure** | |
| **`Procedure.code.coding.system`** | **<http://snomed.info/sct>** | |
| **`Procedure.code.coding.code`** | **792805006** | |
| **`Procedure.code.coding.display`** | **Fasting** | |
| **`Procedure.status`** | ***done*** | ***not-done*** |
| **Pilihan jawaban yang divisualisasikan** | **Puasa** | **Tidak Puasa** |
| **`Specimen.collection.fastingStatusCodeableConcept.coding.system`** | **<http://terminology.hl7.org/CodeSystem/v2-0916>** | |
| **`Specimen.collection.fastingStatusCodeableConcept.coding.code`** | **F** | **NF** |
| **`Specimen.collection.fastingStatusCodeableConcept.coding.display`** | **Patient was fasting prior to the procedure.** | **The patient indicated they did not fast prior to the procedure.** |
| **Pilihan jawaban yang divisualisasikan** | **Puasa** | **Tidak Puasa** |
| **Spesimen** | | |
| **1. Asal Sumber Spesimen Klinis** | | |
| **`Specimen.type.coding.system`** | **<http://snomed.info/sct>** | |
| **`Specimen.type.coding.code`** | **SNOMED-CT Code**  **Ruang lingkup kode SNOMED CT yang dapat dipakai: Expression Constraint Language (ECL) Query : < 123038009 |Specimen (specimen)|**  **(Untuk Kode Lengkapnya dapat dilihat pada Dokumen Lampiran [Standar Terminologi](../../terminology/standar-terminologi/#standar-terminologi) SATUSEHAT)** | |
| **`Specimen.type.coding.display`** | **SNOMED-CT Description** | |
| **2. Lokasi Pengambilan Spesimen Klinis** | | |
| **`Specimen.collection.bodySite.coding.system`** | **<http://snomed.info/sct>** | |
| **`Specimen.collection.bodySite.coding.code`** | **SNOMED-CT Code**  **Ruang lingkup kode SNOMED CT yang dapat dipakai: Expression Constraint Language (ECL) Query : < 123037004 |Body structure (body structure)|**  **(Untuk Kode Lengkapnya dapat dilihat pada Dokumen Lampiran [Standar Terminologi](../../terminology/standar-terminologi/#standar-terminologi) SATUSEHAT)** | |
| **`Specimen.collection.bodySite.coding.display`** | **SNOMED-CT Description** | |
| **3. Jumlah dan Volume Spesimen Klinis** | | |
| **`Specimen.collection.quantity.value`** | **Tipe data *decimal*** | |
| **`Specimen.collection.quantity.unit`** | **UCUM unit**  **Kode satuan atau unit dapat menggunakan kode yang disediakan oleh *Unified Code for Units of Measure* (UCUM). Daftar kode satuan dapat diakses melalui link berikut:https://docs.google.com/spreadsheets/d/1OHM4ICgQ3hseGLrqi9GQzcREddU5SDKto50dhkhOjnc/edit?gid=0#gid=0[Observation.valueQuantity (UCUM)]**  **(Untuk Kode Lengkapnya dapat dilihat pada Dokumen Lampiran [Standar Terminologi](../../terminology/standar-terminologi/#standar-terminologi) SATUSEHAT)** | |
| **`Specimen.collection.quantity.system`** | **<http://unitsofmeasure.org>** | |
| **`Specimen.collection.quantity.code`** | **UCUM Code** | |
| **4. Cara/Metode Pengambilan Spesimen Klinis** | | |
| **`Specimen.collection.method.coding.system`** | **<http://snomed.info/sct>** | |
| **`Specimen.collection.method.coding.code`** | **SNOMED-CT Code**  **Ruang lingkup kode SNOMED CT yang dapat dipakai: Expression Constraint Language (ECL) Query : < 118292001 | Removal (procedure) |**  **(Untuk Kode Lengkapnya dapat dilihat pada Dokumen Lampiran [Standar Terminologi](../../terminology/standar-terminologi/#standar-terminologi) SATUSEHAT)** | |
| **`Specimen.collection.method.coding.display`** | **SNOMED-CT Description** | |
| **5. Waktu Pengambilan Spesimen Klinis** | | |
| **`Specimen.collection.collectedDateTime`** | **(Tipe data *dateTime*)** | |
| **6. Kondisi Spesimen Klinis pada saat Pengambilan** | | |
| **`Specimen.condition.coding.text`** | **(Tipe data *string*)** | |
| **7. Fiksasi Spesimen Klinis** | | |
| **a. Prosedur Fiksasi Spesimen Klinis** | | |
| **`Specimen.processing.procedure.coding.system`** | **<http://snomed.info/sct>** | |
| **`Specimen.processing.procedure.coding.code`** | **787378005** | |
| **`Specimen.processing.procedure.coding.display`** | **Fixation of specimen** | |
| **b. Tanggal dan Jam Fiksasi Spesimen Klinis** | | |
| **`Specimen.processing.timeDateTime`** | **(Tipe data *dateTime*)** | |
| **c. Jenis Cairan Fiksasi** | | |
| **`Specimen.processing.additive`** | **Referensi ke resource `Substance`** | |
| **`Substance.code.coding.system`** | **<http://sys-ids.kemkes.go.id/kfa>** | |
| **`Substance.code.coding.code`** | **Kode Alat Kesehatan KFA** | |
| **`Substance.code.coding.display`** | **Deskripsi Alat Kesehatan KFA** | |
| ****Keterangan:** Penggunaan kode KFA terkait alat kesehatan untuk sementara dapat menggunakan kode khusus yaitu kode 32999999 (Kode Produk Virtual) dan 33999999 (Kode Produk Aktual) dengan menggunakan display sesuai dengan nama alat kesehatan yang digunakan pada pelayanan yang diberikan kepada pasien. Penggunaan kode yang sesungguhnya akan diinformasikan lebih lanjut ketika sudah dapat dipublikasikan.** | | |
| **d. Volume Cairan Fiksasi** | | |
| **`Specimen.processing.additive`** | **Referensi ke resource `Substance`** | |
| **`Substance.instance.quantity.value`** | **(Tipe data *decimal*)** | |
| **`Substance.instance.quantity.unit`** | **mL** | |
| **`Substance.instance.quantity.system`** | **<http://unitsofmeasure.org>** | |
| **`Substance.instance.quantity.code`** | **mL** | |
| **8. Nama Petugas yang Mengambil Spesimen Klinis** | | |
| **`Specimen.collection.collector`** | **Referensi ke resource `Practitioner`** | |
| **9. Nama Petugas yang Mengantarkan Spesimen Klinis** | | |
| **`Specimen.extension:transportedPerson.valueContactDetail.name`** | **(Tipe data *string*)** | |
| **10. Nama Petugas yang Menerima Spesimen Klinis** | | |
| **`Specimen.extension:receivedPerson.valueReference`** | **Referensi ke resource `Practitioner`** | |
| **11. Pemeriksaan/Pengujian dan Pengolahan Spesimen Klinis** | | |
| **a. Prosedur Pemeriksaan/Pengujian dan Pengolahan Spesimen Klinis** | | |
| **`Specimen.processing.procedure.coding.system`** | **<http://snomed.info/sct>** | |
| **`Specimen.processing.procedure.coding.code`** | **SNOMED-CT Code**  **Ruang lingkup kode SNOMED CT yang dapat dipakai: Expression Constraint Language (ECL) Query : ≤ 9265001 | Specimen processing (procedure) |**  **(Untuk Kode Lengkapnya dapat dilihat pada Dokumen Lampiran [Standar Terminologi](../../terminology/standar-terminologi/#standar-terminologi) SATUSEHAT)** | |
| **`Specimen.processing.procedure.coding.display`** | **SNOMED-CT Description** | |
| **b. Tanggal dan Jam Pemeriksaan/Pengujian dan Pengolahan Spesimen Klinis** | | |
| **`Specimen.processing.timeDateTime`** | **Tipe data *dateTime*** | |
| **Hasil Pemeriksaan Penunjang Laboratorium** | | |
| **1. Jenis Pemeriksaan** | | |
| **`Observation.category.coding.system`** | **<http://terminology.hl7.org/CodeSystem/observation-category>** | |
| **`Observation.category.coding.code`** | **laboratory** | |
| **`Observation.category.coding.display`** | **Laboratory** | |
| **`Observation.code.coding.system`** | **<http://loinc.org>** | |
| **`Observation.code.coding.code`** | **LOINC Code**  **(Untuk ketentuan lebih lanjut dapat dilihat pada Dokumen Lampiran [Standar Terminologi](../../terminology/standar-terminologi/#standar-terminologi) SATUSEHAT)** | |
| **`Observation.code.coding.display`** | **LOINC Description** | |
| **2. Nilai Hasil Pemeriksaan** | | |
| **`Observation.value[x]`** | **Mengacu pada ketentuan di subbab 10.4 Pengiriman Data Hasil Pemeriksaan Penunjang Laboratorium** | |
| **3. Nilai Normal/Tidak Normal** | | |
| **`Observation.interpretation.coding.system`** | **<http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation>** | |
| **`Observation.interpretation.coding.code`** | **Kode interpretasi hasil pemeriksaan**  **Kode dapat diisi dengan kode interpretasi hasil pemeriksaan dari FHIR Terminology.**  **(Untuk Kode Lengkapnya dapat dilihat pada Dokumen Lampiran [Standar Terminologi](../../terminology/standar-terminologi/#standar-terminologi) SATUSEHAT)** | |
| **`Observation.interpretation.coding.value`** | **Deskripsi interpretasi hasil pemeriksaan** | |
| **4. Nilai Rujukan** | | |
| **`Observation.referenceRange`** | **Mengacu pada ketentuan di subbab 10.4 Pengiriman Data Hasil Pemeriksaan Penunjang Laboratorium** | |
| **5. Nilai Kritis** | | |
| **`Observation.referenceRange`** | **Mengacu pada ketentuan di subbab 10.4 Pengiriman Data Hasil Pemeriksaan Penunjang Laboratorium** | |
| **6. Interpretasi Hasil Pemeriksaan** | | |
| **`Observation.interpretation.coding.system`** | **<http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation>** | |
| **`Observation.interpretation.coding.code`** | **Kode interpretasi hasil pemeriksaan**  **Kode dapat diisi dengan kode interpretasi hasil pemeriksaan dari FHIR Terminology.**  **(Untuk Kode Lengkapnya dapat dilihat pada Dokumen Lampiran [Standar Terminologi](../../terminology/standar-terminologi/#standar-terminologi) SATUSEHAT)** | |
| **`Observation.interpretation.coding.value`** | **Deskripsi interpretasi hasil pemeriksaan** | |
| **7. Nama Petugas yang Menganalisis Spesimen Klinis** | | |
| **`Observation.performer`** | **Referensi ke resource `Practitioner`** | |
| **8. Nama Dokter yang Memvalidasi/Memverifikasi Hasil Pemeriksaan** | | |
| **`Observation.performer`** | **Referensi ke resource `Practitioner`** | |
| **9. Nama Dokter yang Menginterpretasi Hasil Pemeriksaan** | | |
| **`Observation.performer`** | **Referensi ke resource `Practitioner`** | |
| **10. Waktu Hasil Pemeriksaan Keluar dari Laboratorium** | | |
| **`Observation.effectiveDateTime`** | **(Tipe data *dateTime*)** | |
| **11. Waktu Hasil Pemeriksaan Laboratorium Diterima Unit Pengirim** | | |
| **`Observation.issued`** | **(Tipe data *dateTime*)** | |
| **12. Nama Fasilitas Kesehatan yang Melakukan Pemeriksaan** | | |
| **`Observation.performer`** | **Referensi ke resource `Organization`** | |
| **Laporan Pemeriksaan Penunjang Laboratorium** | | |
| **`DiagnosticReport.category.coding.system`** | **`http://terminology.hl7.org/CodeSystem/v2-0074`** | |
| **`DiagnosticReport.category.coding.code`** | **Kode kategori laporan**  **Kode dapat diisi dengan kode kategori laporan dari FHIR Terminology.**  **(Untuk Kode Lengkapnya dapat dilihat pada Dokumen Lampiran [Standar Terminologi](../../terminology/standar-terminologi/#standar-terminologi) SATUSEHAT)** | |
| **`DiagnosticReport.category.coding.display`** | **Deskripsi kategori laporan** | |
| **`DiagnosticReport.code.coding.system`** | **<http://loinc.org>** | |
| **`DiagnosticReport.code.coding.code`** | **LOINC Code**  **(Untuk ketentuan lebih lanjut dapat dilihat pada Dokumen Lampiran [Standar Terminologi](../../terminology/standar-terminologi/#standar-terminologi) SATUSEHAT)** | |
| **`DiagnosticReport.code.coding.display`** | **LOINC Description** | |
| **`DiagnosticReport.result`** | **Referensi ke resource `Observation` untuk Hasil Pemeriksaan Penunjang Laboratorium** | |
| **`DiagnosticReport.specimen`** | **Referensi ke resource `Specimen` untuk data Spesimen** | |
| **`DiagnosticReport.basedOn`** | **Referensi ke resource `ServiceRequest` untuk Permintaan Pemeriksaan Penunjang Laboratorium** | |
| **`DiagnosticReport.conclusionCode`** | **Kode kesimpulan atau interpretasi dari hasil laboratorium**  **Kode dapat diisi dengan kode FHIR Terminology, SNOMED-CT, dan Kode Terminologi Kemkes.**  **(Untuk Kode Lengkapnya dapat dilihat pada Dokumen Lampiran [Standar Terminologi](../../terminology/standar-terminologi/#standar-terminologi) SATUSEHAT)** | |
| **`DiagnosticReport.conclusion`** | **(Tipe data *string*)** | |

## 11. Pengiriman Data Pemeriksaan Penunjang Radiologi

Data pemeriksaan penunjang mencakup pemeriksaan laboratorium dan radiologi yang dilakukan terhadap seorang pasien. Berikut alur integrasi dan pemetaan nilai pengiriman data pemeriksaan penunjang radiologi.

### Pengantar DICOM

*Digital Imaging and Communications in Medicine* (DICOM) merupakan standar komunikasi dan manajemen informasi pencitraan medis dan data terkait. DICOM memfasilitasi interoperabilitas antar alat pencitraan dan sistem lainnya dengan mengatur spesifikasi sebagai berikut:

1. Protokol yang harus diikuti perangkat untuk jaringan komunikasi
2. Sintaks dan semantik untuk *Commands* dan informasi terkait yang dipertukarkan dalam protokol
3. Layanan penyimpanan media, format *file*, dan struktur direktori untuk memfasilitasi akses ke gambar dan informasi terkait yang disimpan dalam media yang dipertukarkan
4. Informasi yang harus diberikan dalam implementasi yang sesuai dengan standar yang sudah ditetapkan

Hierarki Pencitraan DICOM

Informasi lebih lanjut dapat dilihat pada [Link](https://www.youtube.com/watch?v=5Ihj2wA9kvE) berikut. image::hierarki-pencitraan.png[DICOM,1000,600,align=center]

Hierarki pencitraan pada DICOM terdiri dari 4 level yaitu:

1. *Patient*
2. *Study*
3. *Series*
4. *Instance*

### Alur Pengiriman Data Pemeriksaan Radiologi ke SATUSEHAT

Alur Interoperabilitas pengiriman hasil pencitraan dalam bentuk DICOM dapat dilihat dalam gambar 5.

![Pemeriksaan Radiologi](../_images/pemeriksaan-radiologi.svg)

Gambar 8. Alur Pengiriman Data Pemeriksaan Radiologi ke SATUSEHAT

Alur pengiriman data terkait pemeriksaan radiologi dapat dilihat dalam Gambar 5. Alur ini ditentukan oleh di mana *Accession Number* dari pemeriksaan radiologi dihasilkan. *Accession Number* adalah nomor untuk mengidentifikasi urutan permintaan/*order* dari *study*. Berikut 2 alur pengiriman data radiologi ke SATUSEHAT:

1. *Accession Number* dikeluarkan oleh SIMRS/SIMPUS atau dikeluarkan oleh *Radiology Information System* (RIS) namun SIMRS/SIMPUS terhubung dengan RIS. Alur atau proses pengiriman data untuk skema ini adalah:

   1. Permintaan atau order pemeriksaan radiologi dilakukan oleh SIMRS/SIMPUS.
   2. a. SIMRS/SIMPUS mengeluarkan *accession number* **ATAU**

      1. RIS mengeluarkan *accession number* dan SIMRS mendapatkan *accession number* yang dikeluarkan RIS
   3. Pembuatan *work list* untuk modalitas. *Work list* merupakan daftar permintaan yang perlu dilakukan oleh masing-masing modalitas atau alat radiologi.
   4. Pelaksanaan atau pengambilan pencitraan radiologi oleh masing-masing modalitas
   5. Hasil dalam format DICOM akan disimpan dalam *Picture Archiving and Communications System* (PACS).
   6. File DICOM yang telah tersimpan akan dikirimkan oleh DICOM Router ke SATUSEHAT atau secara spesifik ke *National Imaging Data Repository* (NIDR). DICOM Router juga akan mengirimkan informasi *file* DICOM tersebut ke SATUSEHAT dengan format FHIR.
   7. Bacaan hasil radiologi atau *expertise* dan kesan bacaan radiologi yang dilakukan oleh dokter spesialis radiologi akan dikirimkan ke SATUSEHAT.

Berdasarkan Gambar 5A, maka seluruh pengiriman data ke SATUSEHAT melalui resource [`ServiceRequest`](../../fhir/resources/service-request/#servicerequest), [`Observation`](../../fhir/resources/observation/#observation), dan [`DiagnosticReport`](../../fhir/resources/diagnostic-report/#diagnosticreport) akan dilakukan oleh SIMPUS/SIMRS.

1. *Accession Number* dikeluarkan oleh SIMPUS/SIMRS ke Modality melalui *DICOM Router* Alur atau proses pengiriman data untuk skema ini adalah:

   1. Permintaan atau *order* pemeriksaan Penunjang / Ultrasonografi (USG) dilakukan oleh SIMPUS/SIMRS.
   2. SIMPUS/SIMRS mengeluarkan *accession number*.
   3. Pembuatan *work list* untuk modalitas USG. *Work list* merupakan daftar permintaan yang perlu dilakukan oleh modalitas (USG).
   4. Pelaksanaan atau pengambilan pencitraan USG oleh masing-masing modalitas.
   5. Hasil dalam format DICOM akan disimpan dalam Penyimpanan di Modalitas.
   6. File DICOM yang telah tersimpan akan dikirimkan oleh *DICOM Router* ke SATUSEHAT atau secara spesifik ke *National Imaging Data Repository* (NIDR). *DICOM Router* juga akan mengirimkan informasi file DICOM tersebut ke SATUSEHAT dengan format FHIR.
   7. Bacaan hasil radiologi atau *expertise* dan kesan bacaan USG yang dilakukan oleh dokter spesialis Kandungan dan Kebidanan akan dikirimkan ke SATUSEHAT.

Selengkapnya dapat dilihat pada Gambar 5B, dengan teknis pengiriman data ke SATUSEHAT melalui resource [`ServiceRequest`](../../fhir/resources/service-request/#servicerequest), [`Observation`](../../fhir/resources/observation/#observation), dan [`DiagnosticReport`](../../fhir/resources/diagnostic-report/#diagnosticreport) akan dilakukan oleh SIMPUS/SIMRS.

Alur Pengiriman DICOM pada Fasilitas Pelayanan Kesehatan yang Memiliki MWL dapat dilihat pada [Lampiran 2](../../terminology/lampiran-terminologi/rawat-inap-fase-2/#lampiran-2-ranap) dan Alur Pengiriman DICOM pada Fasilitas Pelayanan Kesehatan yang Tidak Memiliki MWL dapat dilihat pada [Lampiran 3](../../terminology/lampiran-terminologi/rawat-inap-fase-2/#lampiran-3-ranap).

### Pengiriman Data Permintaan Pemeriksaan Penunjang Radiologi

Sebelum melakukan pemeriksaan penunjang seperti radiologi, diperlukan langkah permintaan pemeriksaan penunjang. Pengiriman data terkait permintaan pemeriksaan penunjang dapat dilakukan menggunakan resource [`ServiceRequest`](../../fhir/resources/service-request/#servicerequest). Data permintaan pemeriksaan penunjang radiologi yang dapat dikirimkan antara lain nama pemeriksaan, pasien terkait, kunjungan terkait, tanggal permintaan akan dilakukan, tanggal permintaan dibuat, dan tenaga kesehatan yang melakukan permintaan.

Kode LOINC atau kode Pemeriksaan Penunjang Nasional digunakan pada elemen `ServiceRequest.code` untuk merepresentasikan nama pemeriksaan yang diminta. Referensi pemetaan pemeriksaan radiologi dengan kode LOINC dapat dilihat melalui [**Lampiran LOINC Laboratorium**](https://s.kemkes.go.id/LampiranLOINC-Lab). Gunakan parameter pemeriksaan dengan kategori “Permintaan” atau “Permintaan & Hasil” pada *file* Terminologi Radiologi ketika mengirimkan data melalui resource [`ServiceRequest`](../../fhir/resources/service-request/#servicerequest).

Satu *payload* atau satu *record* dari resource `ServiceRequest` hanya dapat digunakan untuk 1 kode/permintaan parameter radiologi. Sehingga, apabila dilakukan permintaan 2 parameter radiologi, sebagai contoh *X-ray thorax* atau *rontgen* dada dan *X-ray abdomen* atau *rontgen* perut, maka perlu mengirimkan 2 *payload* di mana 1 *payload* berisi 1 kode *X-ray thorax* dan 1 *payload* berisi kode *X-ray abdomen*.

Ketentuan pengiriman permintaan `ServiceRequest` ditentukan berdasarkan ketersediaan MWL pada fasilitas pelayanan kesehatan. Berikut ketentuan spesifik pengiriman permintaan pemeriksaan radiologi berdasarkan ketersediaan MWL.

1. Pengiriman Permintaan Pemeriksaan Radiologi pada Fasilitas Pelayanan Kesehatan yang Memiliki MWL

   1. SIMPUS/SIMRS mengirimkan `ServiceRequest` kepada SATUSEHAT dengan ketentuan pengisian berikut:

      1. Pada elemen `ServiceRequest.identifier` wajib diisi dengan ID Lokal Permintaan Pemeriksaan Penunjang pada Fasilitas Kesehatan dan *Accession number*. *Accession number* merupakan nomor yang dihasilkan oleh *Radiology Information System* (RIS) untuk mengidentifikasi urutan permintaan/order dari study. Nomor ini selalu unik untuk setiap permintaan yang di fasyankes tersebut.
      2. Pada `ServiceRequest.orderDetail.coding` digunakan untuk mengirimkan data terkait jenis modalitas radiologi dan kode identitas modalitas radiologi (*AE Title*). Sedangkan untuk `ServiceRequest.orderDetail.text` digunakan untuk mengirimkan data keterangan tambahan terkait dengan jenis modalitas radiologi.
2. Pengiriman Permintaan Pemeriksaan Radiologi pada Fasilitas Pelayanan Kesehatan yang Tidak Memiliki MWL

   1. SIMPUS/SIMRS mengirimkan `ServiceRequest` kepada SATUSEHAT dengan format pengisian seperti yang dijelaskan pada poin A.1.a
   2. SIMPUS/SIMRS mengirimkan `ServiceRequest` kepada MWL dalam DICOM Router dengan ketentuan pengisian berikut:

      1. Pada `ServiceRequest.identifier` wajib diisi dengan ID Lokal Permintaan Pemeriksaan Penunjang pada Fasilitas Kesehatan dan *Accession number*. *Accession number* merupakan nomor yang dihasilkan oleh *Radiology Information System* (RIS) untuk mengidentifikasi urutan permintaan/order dari study. Nomor ini selalu unik untuk setiap permintaan yang di fasyankes tersebut.
      2. Pada `ServiceRequest.orderDetail.coding` digunakan untuk mengirimkan data terkait jenis modalitas radiologi dan kode identitas modalitas radiologi (*AE Title*). Sedangkan untuk `ServiceRequest.orderDetail.text` digunakan untuk mengirimkan data keterangan tambahan terkait dengan jenis modalitas radiologi.
      3. Pada `ServiceRequest.contained` digunakan untuk menambahkan data identitas pasien pada hasil radiologi, `ServiceRequest.contained` berisi data nomor rekam medis, nama, jenis kelamin, dan tanggal lahir pasien.

Berikut pemetaan nilai untuk `ServiceRequest` yang direpresentasikan dalam peta referensi *(path)* ke properti *(element id)* terkait, untuk konteks pemeriksaan penunjang:

|  |  |
| --- | --- |
|  | 1. Setiap terdapat simbol asterik `*` sebelum nama variabel/parameter/element FHIR yang disebutkan, maka variabel/parameter/element FHIR tersebut bersifat **WAJIB**, **harus ada**, atau **pasti selalu ada**, contoh: **`*Location.identifier`**. 2. **Standar format Waktu** yang digunakan dalam pengiriman data adalah **UTC +00**. Misalnya waktu **WIB**, maka format yang digunakan adalah **waktu sekarang dikurangi 7**, jika **WITA**, maka **waktu sekarang dikurangi 8**, dan Jika **WIT**, maka **waktu sekarang dikurangi 9**.  **Contoh:** Pukul 17.35 WIB tanggal 23 Agustus 2023 maka yang dikirimkan adalah waktunya perlu diubah ke UTC +00 menjadi 10.35, berarti menjadi `2023-08-23T10:35:00+00:00`. 3. **Standar format pengiriman Tanggal** tidak bisa kurang dari 03 Juni 2014. |

|  |  |
| --- | --- |
|  | Silakan klik setiap teks variabel/parameter/element FHIR pada daftar pemetaan nilai di bawah ini (berwarna **merah**), untuk membaca panduan lebih detail/lanjut ke bagian yang direferensikan. |

- [`ServiceRequest.identifier`](../../fhir/resources/service-request/#servicerequest-identifier)
- [`*ServiceRequest.status`](../../fhir/resources/service-request/#servicerequest-status)
- [`*ServiceRequest.intent`](../../fhir/resources/service-request/#servicerequest-intent)
- [`*ServiceRequest.category`](../../fhir/resources/service-request/#servicerequest-category)
- [`ServiceRequest.priority`](../../fhir/resources/service-request/#servicerequest-priority)
- [`*ServiceRequest.code`](../../fhir/resources/service-request/#servicerequest-code)
- [`*ServiceRequest.subject`](../../fhir/resources/service-request/#servicerequest-subject)
- [`*ServiceRequest.encounter`](../../fhir/resources/service-request/#servicerequest-encounter)
- [`ServiceRequest.authoredOn`](../../fhir/resources/service-request/#servicerequest-authoredon)
- [`*ServiceRequest.requester`](../../fhir/resources/service-request/#servicerequest-requester)
- [`*ServiceRequest.performer`](../../fhir/resources/service-request/#servicerequest-performer)
- [`ServiceRequest.locationReference`](../../fhir/resources/service-request/#servicerequest-locationreference)
- [`ServiceRequest.reasonCode`](../../fhir/resources/service-request/#servicerequest-reasoncode)
- [`ServiceRequest.reasonReference`](../../fhir/resources/service-request/#servicerequest-reasonreference)
- [`ServiceRequest.insurance`](../../fhir/resources/service-request/#servicerequest-insurance)
- [`ServiceRequest.specimen`](../../fhir/resources/service-request/#servicerequest-specimen)
- [`ServiceRequest.bodySite`](../../fhir/resources/service-request/#servicerequest-bodysite)

Penjelasan tipe mandatoris, deskripsi dan format pengisian dari setiap elemen data/*path* di dalam resource `ServiceRequest` (data permintaan pemeriksaan penunjang radiologi), dapat dilihat dalam resource [`ServiceRequest`](../../fhir/resources/service-request/#servicerequest). Untuk contoh pengiriman data atau *payload* dari `ServiceRequest` dapat dilihat dalam [Postman SATUSEHAT](../../postman-workshop/#postman-collection-satusehat) SATUSEHAT.

### Pengiriman Data Citra DICOM oleh DICOM router menuju National Imaging Data Repository (NIDR)

Pengiriman informasi hasil radiologi dalam format DICOM akan dikirimkan oleh DICOM *router*. Setelah mendapatkan *file* DICOM dari PACS, DICOM *router* akan mengirimkan *file* tersebut ke *National Imaging Data Repository* (NIDR). NIDR akan mengembalikan *Web Access to DICOM Objects* (Wado) URL yang nantinya dapat digunakan untuk melihat hasil pencitraan yang telah tersimpan di NIDR. DICOM router kemudian akan melakukan POST informasi terkait DICOM melalui resource [`ImagingStudy`](../../fhir/resources/imaging-study/#imagingstudy) ke SATUSEHAT. SATUSEHAT akan merespon dengan mengembalikan `ImagingStudy.id` ke DICOM Router. `ImagingStudy.id` ini perlu disimpan dan nantinya akan direferensikan ketika melakukan pengiriman data bacaan atau ekspertise dari hasil pemeriksaan radiologi.

Berikut pemetaan nilai untuk `ImagingStudy` yang direpresentasikan dalam peta referensi *(path)* ke properti *(element id)* terkait, untuk konteks pengiriman data informasi DICOM:

|  |  |
| --- | --- |
|  | 1. Setiap terdapat simbol asterik `*` sebelum nama variabel/parameter/element FHIR yang disebutkan, maka variabel/parameter/element FHIR tersebut bersifat **WAJIB**, **harus ada**, atau **pasti selalu ada**, contoh: **`*Location.identifier`**. 2. **Standar format Waktu** yang digunakan dalam pengiriman data adalah **UTC +00**. Misalnya waktu **WIB**, maka format yang digunakan adalah **waktu sekarang dikurangi 7**, jika **WITA**, maka **waktu sekarang dikurangi 8**, dan Jika **WIT**, maka **waktu sekarang dikurangi 9**.  **Contoh:** Pukul 17.35 WIB tanggal 23 Agustus 2023 maka yang dikirimkan adalah waktunya perlu diubah ke UTC +00 menjadi 10.35, berarti menjadi `2023-08-23T10:35:00+00:00`. 3. **Standar format pengiriman Tanggal** tidak bisa kurang dari 03 Juni 2014. |

|  |  |
| --- | --- |
|  | Silakan klik setiap teks variabel/parameter/element FHIR pada daftar pemetaan nilai di bawah ini (berwarna **merah**), untuk membaca panduan lebih detail/lanjut ke bagian yang direferensikan. |

- [`*ImagingStudy.identifier[i]`](../../fhir/resources/imaging-study/#imagingstudy-identifier)
- [`*ImagingStudy.status`](../../fhir/resources/imaging-study/#imagingstudy-status)
- [`*ImagingStudy.modality`](../../fhir/resources/imaging-study/#imagingstudy-modality)
- [`*ImagingStudy.subject`](../../fhir/resources/imaging-study/#imagingstudy-subject)
- [`ImagingStudy.encounter`](../../fhir/resources/imaging-study/#imagingstudy-encounter)
- [`*ImagingStudy.started`](../../fhir/resources/imaging-study/#imagingstudy-started)
- [`*ImagingStudy.basedOn`](../../fhir/resources/imaging-study/#imagingstudy-basedon)
- [`ImagingStudy.referrer`](../../fhir/resources/imaging-study/#imagingstudy-referrer)
- [`ImagingStudy.interpreter`](../../fhir/resources/imaging-study/#imagingstudy-interpreter)
- [`*ImagingStudy.endpoint`](../../fhir/resources/imaging-study/#imagingstudy-endpoint)
- [`ImagingStudy.numberOfSeries`](../../fhir/resources/imaging-study/#imagingstudy-numberofseries)
- [`ImagingStudy.numberOfInstances`](../../fhir/resources/imaging-study/#imagingstudy-numberofinstances)
- [`ImagingStudy.procedureReferences`](../../fhir/resources/imaging-study/#imagingstudy-procedurereferences)
- [`ImagingStudy.procedureCode`](../../fhir/resources/imaging-study/#imagingstudy-procedurecode)
- [`ImagingStudy.location`](../../fhir/resources/imaging-study/#imagingstudy-location)
- [`ImagingStudy.reasonCode`](../../fhir/resources/imaging-study/#imagingstudy-reasoncode)
- [`ImagingStudy.reasonReference`](../../fhir/resources/imaging-study/#imagingstudy-reasonreference)
- [`ImagingStudy.note`](../../fhir/resources/imaging-study/#imagingstudy-note)
- [`ImagingStudy.description`](../../fhir/resources/imaging-study/#imagingstudy-description)
- [`ImagingStudy.series`](../../fhir/resources/imaging-study/#imagingstudy-series)
- [`*ImagingStudy.series.uid`](../../fhir/resources/imaging-study/#imagingstudy-series-uid)
- [`ImagingStudy.series.number`](../../fhir/resources/imaging-study/#imagingstudy-series-number)
- [`*ImagingStudy.series.modality`](../../fhir/resources/imaging-study/#imagingstudy-series-modality)
- [`ImagingStudy.series.description`](../../fhir/resources/imaging-study/#imagingstudy-series-description)
- [`ImagingStudy.series.numberOfInstances`](../../fhir/resources/imaging-study/#imagingstudy-series-numberofinstances)
- [`ImagingStudy.series.endpoint`](../../fhir/resources/imaging-study/#imagingstudy-series-endpoint)
- [`ImagingStudy.series.bodySite`](../../fhir/resources/imaging-study/#imagingstudy-series-bodysite)
- [`ImagingStudy.series.laterality`](../../fhir/resources/imaging-study/#imagingstudy-series-laterality)
- [`ImagingStudy.series.specimen`](../../fhir/resources/imaging-study/#imagingstudy-series-specimen)
- [`ImagingStudy.series.started`](../../fhir/resources/imaging-study/#imagingstudy-series-started)
- [`ImagingStudy.series.performer.function`](../../fhir/resources/imaging-study/#imagingstudy-series-performer-function)

Penjelasan tipe mandatoris, deskripsi dan format pengisian dari setiap elemen data/*path* di dalam resource `ImagingStudy` (dan contoh *payload* dari data citra DICOM), dapat dilihat dalam resource [`ImagingStudy`](../../fhir/resources/imaging-study/#imagingstudy). Untuk contoh pengiriman data atau *payload* dari `ImagingStudy` dapat dilihat dalam [Postman SATUSEHAT](../../postman-workshop/#postman-collection-satusehat) SATUSEHAT.

### Pengiriman Data Bacaan Hasil Pemeriksaan Penunjang Radiologi

Bacaan hasil pemeriksaan penunjang radiologi dikirimkan menggunakan resource [`Observation`](../../fhir/resources/observation/#observation). Berikut adalah ketentuan pengisian data hasil pemeriksaan radiologi melalui resource [`Observation`](../../fhir/resources/observation/#observation).

1. Kode LOINC atau kode Pemeriksaan Penunjang Nasional digunakan pada elemen `Observation.code` untuk merepresentasikan nama pemeriksaan yang dihasilkan. Referensi pemetaan pemeriksaan laboratorium dengan kode LOINC dapat dilihat melalui [**Lampiran LOINC Laboratorium**](https://s.kemkes.go.id/LampiranLOINC-Lab). Gunakan parameter pemeriksaan dengan kategori “Hasil” atau “Permintaan & Hasil” pada terminologi radiologi ketika mengirimkan data melalui resource [`Observation`](../../fhir/resources/observation/#observation).
2. Elemen `Observation.category.coding` diisi dengan kode *imaging*.
3. Pemilihan elemen `Observation.value[x]` disesuaikan dengan Tipe hasil pemeriksaan radiologi.

   1. `Observation.valueCodeableConcept` untuk tipe hasil Nominal
   2. `Observation.valueCodeableConcept` untuk tipe hasil Ordinal
   3. `Observation.valueQuantity` untuk tipe hasil Kuantitatif/*Quantitative*
   4. `Observation.valueString` untuk tipe hasil Naratif/*Narrative*

Satu *payload* atau satu *record* dari resource `Observation` hanya dapat digunakan untuk 1 kode hasil parameter radiologi. Sehingga, apabila terdapat 2 hasil radiologi, sebagai contoh *X-ray thorax* atau *rontgen* dada dan *X-ray abdomen* atau *rontgen* perut, maka perlu mengirimkan 2 *payload* di mana 1 *payload* berisi 1 kode *X-ray thorax* dan 1 *payload* berisi kode *X-ray abdomen*.

Berikut pemetaan nilai untuk `Observation` yang direpresentasikan dalam peta referensi *(path)* ke properti *(element id)* terkait, untuk konteks jenis perawatan:

|  |  |
| --- | --- |
|  | 1. Setiap terdapat simbol asterik `*` sebelum nama variabel/parameter/element FHIR yang disebutkan, maka variabel/parameter/element FHIR tersebut bersifat **WAJIB**, **harus ada**, atau **pasti selalu ada**, contoh: **`*Location.identifier`**. 2. **Standar format Waktu** yang digunakan dalam pengiriman data adalah **UTC +00**. Misalnya waktu **WIB**, maka format yang digunakan adalah **waktu sekarang dikurangi 7**, jika **WITA**, maka **waktu sekarang dikurangi 8**, dan Jika **WIT**, maka **waktu sekarang dikurangi 9**.  **Contoh:** Pukul 17.35 WIB tanggal 23 Agustus 2023 maka yang dikirimkan adalah waktunya perlu diubah ke UTC +00 menjadi 10.35, berarti menjadi `2023-08-23T10:35:00+00:00`. 3. **Standar format pengiriman Tanggal** tidak bisa kurang dari 03 Juni 2014. |

|  |  |
| --- | --- |
|  | Silakan klik setiap teks variabel/parameter/element FHIR pada daftar pemetaan nilai di bawah ini (berwarna **merah**), untuk membaca panduan lebih detail/lanjut ke bagian yang direferensikan. |

- [`Observation.identifier`](../../fhir/resources/observation/#observation-identifier)
- [`Observation.basedOn`](../../fhir/resources/observation/#observation-basedon)
- [`Observation.partOf`](../../fhir/resources/observation/#observation-partof)
- [`*Observation.status`](../../fhir/resources/observation/#observation-status)
- [`Observation.category`](../../fhir/resources/observation/#observation-category)
- [`*Observation.code`](../../fhir/resources/observation/#observation-code)
- [`*Observation.subject`](../../fhir/resources/observation/#observation-subject)
- [`Observation.focus`](../../fhir/resources/observation/#observation-focus)
- [`*Observation.encounter`](../../fhir/resources/observation/#observation-encounter)
- [`Observation.effective<?>`](../../fhir/resources/observation/#observation-effective)
- [`Observation.effectiveDateTime`](../../fhir/resources/observation/#observation-effectivedatetime)
- [`Observation.effectivePeriod`](../../fhir/resources/observation/#observation-effectiveperiod)
- [`Observation.effectiveTiming`](../../fhir/resources/observation/#observation-effectivetiming)
- [`Observation.effectiveInstant`](../../fhir/resources/observation/#observation-effectiveinstant)
- [`*Observation.issued`](../../fhir/resources/observation/#observation-issued)
- [`*Observation.performer`](../../fhir/resources/observation/#observation-performer)
- [`*Observation.value<x>`](../../fhir/resources/observation/#observation-value)
- [`Observation.valueQuantity`](../../fhir/resources/observation/#observation-valuequantity)
- [`Observation.valueCodeableConcept`](../../fhir/resources/observation/#observation-valuecodeableconcept)
- [`Observation.valueString`](../../fhir/resources/observation/#observation-valuestring)
- [`Observation.valueBoolean`](../../fhir/resources/observation/#observation-valueboolean)
- [`Observation.valueInteger`](../../fhir/resources/observation/#observation-valueinteger)
- [`Observation.valueRange`](../../fhir/resources/observation/#observation-valuerange)
- [`Observation.valueRatio`](../../fhir/resources/observation/#observation-valueratio)
- [`Observation.valueSampledData`](../../fhir/resources/observation/#observation-valuesampleddata)
- [`Observation.valueTime`](../../fhir/resources/observation/#observation-valuetime)
- [`Observation.valueDateTime`](../../fhir/resources/observation/#observation-valuedatetime)
- [`Observation.valuePeriod`](../../fhir/resources/observation/#observation-valueperiod)
- [`Observation.dataAbsentReason`](../../fhir/resources/observation/#observation-dataabsentreason)
- [`Observation.interpretation[i]`](../../fhir/resources/observation/#observation-interpretation)
- [`Observation.note`](../../fhir/resources/observation/#observation-note)
- [`Observation.bodySite`](../../fhir/resources/observation/#observation-bodysite)
- [`Observation.method`](../../fhir/resources/observation/#observation-method)
- [`Observation.specimen`](../../fhir/resources/observation/#observation-specimen)
- [`Observation.device`](../../fhir/resources/observation/#observation-device)
- [`Observation.referenceRange`](../../fhir/resources/observation/#observation-referencerange)
- [`Observation.referenceRange.type`](../../fhir/resources/observation/#observation-referencerange-type)
- [`Observation.hasMember`](../../fhir/resources/observation/#observation-hasmember)
- [`Observation.derivedFrom`](../../fhir/resources/observation/#observation-derivedfrom)

Penjelasan tipe mandatoris, deskripsi dan format pengisian dari setiap elemen data/*path* di dalam resource `Observation` (data hasil pemeriksaan laboratorium), dapat dilihat dalam resource [`Observation`](../../fhir/resources/observation/#observation). Untuk contoh pengiriman data atau *payload* dari `Observation` dapat dilihat dalam [Postman SATUSEHAT](../../postman-workshop/#postman-collection-satusehat) SATUSEHAT.

### Pengiriman Data Kesimpulan atau Kesan Hasil Pemeriksaan Penunjang Radiologi

Laporan hasil pemeriksaan atau *expertise* penunjang radiologi dapat dikirimkan akan dikirimkan melalui resource [`DiagnosticReport`](../../fhir/resources/diagnostic-report/#diagnosticreport). Berikut adalah ketentuan pengisian laporan pemeriksaan penunjang radiologi melalui resource [`DiagnosticReport`](../../fhir/resources/diagnostic-report/#diagnosticreport).

1. Data di resource `DiagnosticReport` akan mereferensi ke hasil pemeriksaan radiologi terkait pada resource `Observation` melalui `DiagnosticReport.result`, permintaan pemeriksaan penunjang terkait pada resource `ServiceRequest` melalui `DiagnosticReport.basedOn`, serta informasi DICOM pada resource `ImagingStudy` melalui `DiagnosticReport.imagingStudy`.
2. Kode LOINC atau kode Pemeriksaan Penunjang Nasional digunakan pada elemen `DiagnosticReport.code` untuk merepresentasikan nama pemeriksaan yang dilaporkan. Referensi pemetaan parameter radiologi ke kode LOINC dapat dilihat melalui [**Lampiran LOINC Laboratorium**](https://s.kemkes.go.id/LampiranLOINC-Lab). Gunakan parameter pemeriksaan dengan kategori “Permintaan” atau “Permintaan & Hasil” pada *file* untuk Radiologi melalui resource [`DiagnosticReport`](../../fhir/resources/diagnostic-report/#diagnosticreport).
3. Kode yang dicantumkan dalam `DiagnosticReport.code` akan sama dengan kode yang dicantumkan pada `ServiceRequest.code` terkait.

Satu *payload* atau satu *record* dari resource `DiagnosticReport` hanya dapat digunakan untuk 1 kode/laporan parameter radiologi. Sehingga, apabila dilakukan permintaan 2 parameter radiologi, sebagai contoh *X-ray thorax* atau *rontgen* dada dan *X-ray abdomen* atau *rontgen* perut, maka perlu mengirimkan 2 *payload* laporan melalui resource [`DiagnosticReport`](../../fhir/resources/diagnostic-report/#diagnosticreport) di mana 1 *payload* berisi 1 kode *X-ray thorax* dan 1 *payload* berisi kode *X-ray abdomen*.

Berikut pemetaan nilai untuk `DiagnosticReport` yang direpresentasikan dalam peta referensi *(path)* ke properti *(element id)* terkait, untuk konteks data laporan hasil pemeriksaan:

|  |  |
| --- | --- |
|  | 1. Setiap terdapat simbol asterik `*` sebelum nama variabel/parameter/element FHIR yang disebutkan, maka variabel/parameter/element FHIR tersebut bersifat **WAJIB**, **harus ada**, atau **pasti selalu ada**, contoh: **`*Location.identifier`**. 2. **Standar format Waktu** yang digunakan dalam pengiriman data adalah **UTC +00**. Misalnya waktu **WIB**, maka format yang digunakan adalah **waktu sekarang dikurangi 7**, jika **WITA**, maka **waktu sekarang dikurangi 8**, dan Jika **WIT**, maka **waktu sekarang dikurangi 9**.  **Contoh:** Pukul 17.35 WIB tanggal 23 Agustus 2023 maka yang dikirimkan adalah waktunya perlu diubah ke UTC +00 menjadi 10.35, berarti menjadi `2023-08-23T10:35:00+00:00`. 3. **Standar format pengiriman Tanggal** tidak bisa kurang dari 03 Juni 2014. |

|  |  |
| --- | --- |
|  | Silakan klik setiap teks variabel/parameter/element FHIR pada daftar pemetaan nilai di bawah ini (berwarna **merah**), untuk membaca panduan lebih detail/lanjut ke bagian yang direferensikan. |

- [`DiagnosticReport.identifier`](../../fhir/resources/diagnostic-report/#diagnosticreport-identifier)
- [`*DiagnosticReport.basedOn`](../../fhir/resources/diagnostic-report/#diagnosticreport-basedon)
- [`*DiagnosticReport.status`](../../fhir/resources/diagnostic-report/#diagnosticreport-status)
- [`DiagnosticReport.category`](../../fhir/resources/diagnostic-report/#diagnosticreport-category)
- [`*DiagnosticReport.code`](../../fhir/resources/diagnostic-report/#diagnosticreport-code)
- [`*DiagnosticReport.subject`](../../fhir/resources/diagnostic-report/#diagnosticreport-subject)
- [`*DiagnosticReport.encounter`](../../fhir/resources/diagnostic-report/#diagnosticreport-encounter)
- [`DiagnosticReport.effective<?>`](../../fhir/resources/diagnostic-report/#diagnosticreport-effective)
- [`DiagnosticReport.effectiveDateTime`](../../fhir/resources/diagnostic-report/#diagnosticreport-effectivedatetime)
- [`DiagnosticReport.effectivePeriod`](../../fhir/resources/diagnostic-report/#diagnosticreport-effectiveperiod)
- [`DiagnosticReport.issued`](../../fhir/resources/diagnostic-report/#diagnosticreport-issued)
- [`*DiagnosticReport.performer`](../../fhir/resources/diagnostic-report/#diagnosticreport-performer)
- [`DiagnosticReport.resultsInterpreter`](../../fhir/resources/diagnostic-report/#diagnosticreport-resultsinterpreter)
- [`DiagnosticReport.specimen`](../../fhir/resources/diagnostic-report/#diagnosticreport-specimen)
- [`*DiagnosticReport.result`](../../fhir/resources/diagnostic-report/#diagnosticreport-result)
- [`*DiagnosticReport.imagingStudy`](../../fhir/resources/diagnostic-report/#diagnosticreport-imagingstudy)
- [`DiagnosticReport.media`](../../fhir/resources/diagnostic-report/#diagnosticreport-media)
- [`*DiagnosticReport.conclusion`](../../fhir/resources/diagnostic-report/#diagnosticreport-conclusion)
- [`DiagnosticReport.conclusionCode`](../../fhir/resources/diagnostic-report/#diagnosticreport-conclusioncode)
- [`DiagnosticReport.presentedForm`](../../fhir/resources/diagnostic-report/#diagnosticreport-presentedform)

Penjelasan tipe mandatoris, deskripsi dan format pengisian dari setiap elemen data/*path* di dalam resource `DiagnosticReport` (data laporan pemeriksaan laboratorium), dapat dilihat dalam [resource `DiagnosticReport`](../../fhir/resources/diagnostic-report/#diagnosticreport). Untuk contoh pengiriman data atau *payload* dari `DiagnosticReport` dapat dilihat dalam [Postman SATUSEHAT](../../postman-workshop/#postman-collection-satusehat) SATUSEHAT.

### Pemetaan Variabel dan Terminologi Spesifik

Terminologi spesifik yang digunakan dalam pengiriman data pemeriksaan penunjang radiologi dapat dilihat dalam tabel berikut:

Tabel 11. Terminologi Spesifik

| *Resource* `ServiceRequest`, `ImagingStudy`, `Observation`, `DiagnosticReport` | | |
| --- | --- | --- |
| **Elemen/*Path* FHIR** | **Terminologi/Format Pengisian** | |
| **Permintaan Pemeriksaan Penunjang Radiologi** | | |
| **1. Nomor Permintaan Radiologi** | | |
| **`ServiceRequest.identifier[0].system`** | **<http://sys-ids.kemkes.go.id/servicerequest/{{Organization_ID}}>** | |
| **`ServiceRequest.identifier[0].value`** | **Nomor Permintaan dengan tipe data string** | |
| **`ServiceRequest.identifier[1].type.coding.system`** | **<http://terminology.hl7.org/CodeSystem/v2-0203>** | |
| **`ServiceRequest.identifier[1].type.coding.code`** | **ACSN** | |
| **`ServiceRequest.identifier[1].system`** | **<http://sys-ids.kemkes.go.id/acsn/{{Organization_ID}}>** | |
| **`ServiceRequest.identifier[1].value`** | **Nomor ACSN dengan tipe data string** | |
| **2. Nama Pemeriksaan Radiologi** | | |
| **`ServiceRequest.category.coding.system`** | **<http://snomed.info/sct>** | |
| **`ServiceRequest.category.coding.code`** | **363679005** | |
| **`ServiceRequest.category.coding.display`** | **Imaging** | |
| **`ServiceRequest.code.coding.system`** | **<http://loinc.org>** | |
| **`ServiceRequest.code.coding.code`** | **LOINC Code**  **(Untuk ketentuan lebih lanjut dapat dilihat pada Dokumen Lampiran [Standar Terminologi](../../terminology/standar-terminologi/#standar-terminologi) SATUSEHAT)** | |
| **`ServiceRequest.code.coding.display`** | **LOINC Description** | |
| **`ServiceRequest.code.coding.system`** | **<http://terminology.kemkes.go.id/CodeSystem/kptl>** | |
| **`ServiceRequest.code.coding.code`** | **Kode KPTL**  **Ruang lingkup kode KPTL yang dapat dipakai mencakup kode terkait pemeriksaan laboratorium yang bersifat sepadan dengan kode LOINC yang digunakan**  **(Untuk Kode Lengkapnya dapat dilihat pada Buku Panduan Kode Pembiayaan Tindakan dan Layanan Kesehatan (KPTL))** | |
| **`ServiceRequest.code.coding.display`** | **Deskripsi KPTL** | |
| **3. Waktu Pemeriksaan Radiologi** | | |
| **`ServiceRequest.authoredOn`** | **Tanggal dan waktu permintaan dengan tipe data *dateTime*** | |
| **4. Dokter Pengirim** | | |
| **`ServiceRequest.requester`** | **Referensi ke resource `Practitioner` - ID SATUSEHAT Practitioner** | |
| **5. Nomor Telepon Dokter Pengirim** | | |
| ****Keterangan:** Nomor telepon tenaga kesehatan yang membuat permintaan didapatkan dengan menarik data dari ID SATUSEHAT Practitioner yang direferensikan pada elemen `ServiceRequest.requester`** | | |
| **6. Nama Fasilitas Pelayanan Kesehatan yang Membuat Permintaan** | | |
| ****Keterangan:** Nama fasilitas pelayanan kesehatan yang membuat permintaan didapatkan dengan menarik data detail kunjungan dari ID Encounter yang direferensikan pada elemen `ServiceRequest.encounter`** | | |
| **7. Unit Pengirim** | | |
| ****Keterangan:** Unit pengirim didapatkan dengan menarik data detail kunjungan dari ID Encounter yang direferensikan pada elemen `ServiceRequest.encounter`** | | |
| **8. Prioritas Pemeriksaan** | | |
| **`ServiceRequest.priority`** | ***stat*** | ***routine*** |
| **Pilihan jawaban yang divisualisasikan** | **CITO** | **Non CITO** |
| **9. Diagnosis Kerja/ Masalah** | | |
| **`ServiceRequest.reasonReference`** | **Referensi ke resource `Condition`**  **`ServiceRequest.reasonCode` dapat digunakan jika alasan permintaan tidak dikirimkan dalam *payload* tersendiri** | |
| **10. Catatan Permintaan** | | |
| **`ServiceRequest.note`** | **(Tipe data *string*)** | |
| **11. Data Pendukung Pemeriksaan** | | |
| **`ServiceRequest.supportingInfo`** | **Referensi ke Status Alergi Pasien terhadap Bahan Kontras/Zat Lainnya (`AllergyIntolerance`), Status Kehamilan (`Observation`), dan Status Puasa (`Procedure`)** | |
| **12. Tanggal dan Waktu Pemeriksaan Radiologi** | | |
| **`ServiceRequest.occurenceDateTime`** | **(Tipe data *dateTime*)** | |
| **13. Jenis Bahan Kontras** | | |
| **`ServiceRequest.orderDetail.coding.system`** | **<http://sys-ids.kemkes.go.id/kfa>** | |
| **`ServiceRequest.orderDetail.coding.code`** | **Kode KFA** | |
| **`ServiceRequest.orderDetail.coding.display`** | **Deskripsi Kode KFA** | |
| **14. Jenis Modalitas Radiologi** | | |
| **`ServiceRequest.orderDetail[0].coding.system`** | **<http://dicom.nema.org/resources/ontology/DCM>** | |
| **`ServiceRequest.orderDetail[0].coding.code`** | **Kode DICOM**  **(Untuk ketentuan lebih lanjut dapat dilihat pada Dokumen Lampiran [Standar Terminologi](../../terminology/standar-terminologi/#standar-terminologi) SATUSEHAT)** | |
| **15. Kode Identitas Modalitas (*AE Title*)** | | |
| **`ServiceRequest.orderDetail[1].coding.system`** | **<http://sys-ids.kemkes.go.id/ae-title>** | |
| **`ServiceRequest.orderDetail[1].coding.display`** | **Kode Identitas Modalitas (*AE Title*) dengan tipe data *string*** | |
| **Status Alergi Pasien terhadap Bahan Kontras/Zat Lainnya** | | |
| **`AllergyIntolerance.category`** | **medication** | |
| **`AllergyIntolerance.code.coding`** | **Lihat di Dokumen Lampiran [Standar Terminologi](../../terminology/standar-terminologi/#standar-terminologi) SATUSEHAT** | |
| **Status Kehamilan** | | |
| **`Observation.category.coding.system`** | **<http://snomed.info/sct>** | |
| **`Observation.category.coding.code`** | ***survey*** | |
| **`Observation.category.coding.display`** | **Survey** | |
| **`Observation.code.coding.system`** | **<http://loinc.org>** | |
| **`Observation.code.coding.code`** | **82810-3** | |
| **`Observation.code.coding.display`** | **Pregnancy status** | |
| **`Observation.valueCodeableConcept.coding.system`** | **<http://snomed.info/sct>** | |
| **`Observation.valueCodeableConcept.coding.code`** | **77386006** | **60001007** |
| **`Observation.valueCodeableConcept.coding.display`** | **Pregnancy** | **Not pregnant** |
| **Status Puasa** | | |
| **`Procedure.category.coding.system`** | **<http://snomed.info/sct>** | |
| **`Procedure.category.coding.code`** | **103693007** | |
| **`Procedure.category.coding.display`** | **Diagnostic procedure** | |
| **`Procedure.code.coding.system`** | **<http://snomed.info/sct>** | |
| **`Procedure.code.coding.code`** | **792805006** | |
| **`Procedure.code.coding.display`** | **Fasting** | |
| **`Procedure.status`** | ***done*** | ***not-done*** |
| **Pilihan jawaban yang divisualisasikan** | **Puasa** | **Tidak Puasa** |
| **Hasil Gambar Pemeriksaan Penunjang Radiologi** | | |
| **`ImagingStudy.series.uid`** | **DICOM Series Instance UID** | |
| **`ImagingStudy.interpreter`** | **Referensi ke resource `Practitioner`** | |
| **Hasil Pemeriksaan Penunjang Radiologi** | | |
| **`Observation.category.coding.system`** | **<http://terminology.hl7.org/CodeSystem/observation-category>** | |
| **`Observation.category.coding.code`** | ***imaging*** | |
| **`Observation.category.coding.display`** | **Imaging** | |
| **`Observation.code.coding.system`** | **<http://loinc.org>** | |
| **`Observation.code.coding.code`** | **LOINC Code**  **(Untuk ketentuan lebih lanjut dapat dilihat pada Dokumen Lampiran [Standar Terminologi](../../terminology/standar-terminologi/#standar-terminologi) SATUSEHAT)** | |
| **`Observation.code.coding.display`** | **LOINC Description** | |
| **`Observation.derivedFrom`** | **Referensi ke `ImagingStudy` untuk Hasil Gambar Pemeriksaan Penunjang Radiologi** | |
| **`Observation.valueString`** | **(Tipe data *string*)** | |
| **Laporan Pemeriksaan Penunjang Radiologi** | | |
| **`DiagnosticReport.category.coding.system`** | **<http://terminology.hl7.org/CodeSystem/v2-0074>** | |
| **`DiagnosticReport.category.coding.code`** | **Kode kategori laporan**  **Kode dapat diisi dengan kode kategori laporan dari FHIR Terminology.**  **(Untuk Kode Lengkapnya dapat dilihat pada Dokumen Lampiran [Standar Terminologi](../../terminology/standar-terminologi/#standar-terminologi) SATUSEHAT)** | |
| **`DiagnosticReport.category.coding.display`** | **Deskripsi kategori laporan** | |
| **`DiagnosticReport.code.coding.system`** | **<http://loinc.org>** | |
| **`DiagnosticReport.code.coding.code`** | **LOINC Code**  **(Untuk ketentuan lebih lanjut dapat dilihat pada Dokumen Lampiran [Standar Terminologi](../../terminology/standar-terminologi/#standar-terminologi) SATUSEHAT)** | |
| **`DiagnosticReport.code.coding.display`** | **LOINC Description** | |
| **`DiagnosticReport.result`** | **Referensi ke resource `Observation` untuk Hasil Pemeriksaan Penunjang Radiologi** | |
| **`DiagnosticReport.imagingStudy`** | **Referensi ke resource `ImagingStudy` untuk Hasil Gambar Pemeriksaan Penunjang Radiologi** | |
| **`DiagnosticReport.basedOn`** | **Referensi ke resource `ServiceRequest` untuk Permintaan Pemeriksaan Penunjang Radiologi** | |
| **`DiagnosticReport.conclusionCode`** | **Kode kesimpulan atau interpretasi dari hasil radiologi**  **Kode dapat diisi dengan kode FHIR Terminology, SNOMED-CT, dan Kode Terminologi Kemkes.**  **(Untuk Kode Lengkapnya dapat dilihat pada Dokumen Lampiran [Standar Terminologi](../../terminology/standar-terminologi/#standar-terminologi) SATUSEHAT)** | |
| **`DiagnosticReport.conclusion`** | **(Tipe data *string*)** | |

## 12. Pengiriman Data Rasional Klinis

Data Rasional Klinis berisi narasi mengenai dasar penegakan diagnosis yang dilakukan oleh dokter. Data rasional klinis dapat dikirimkan melalui resource `ClinicalImpression`. Pemetaan nilai resource `ClinicalImpression` dapat dilihat pada bab Riwayat Perjalanan Penyakit.

### Pemetaan Variabel dan Terminologi Spesifik

Terminologi spesifik yang digunakan dalam pengiriman data rasional klinis melalui resource `ClinicalImpression` dapat dilihat dalam tabel berikut:

Tabel 12. Terminologi Spesifik

| Pemetaan Variabel *Resource* `ClinicalImpression` | |
| --- | --- |
| **Elemen/*Path* FHIR** | **Terminologi/Format Pengisian** |
| **Rasional Klinis** | |
| **`ClinicalImpression.code.coding.system`** | **<http://terminology.kemkes.go.id>** |
| **`ClinicalImpression.code.coding.code`** | **TK000056** |
| **`ClinicalImpression.code.coding.display`** | **Rasional Klinis** |
| **`ClinicalImpression.summary`** | **(Tipe data *string*)** |
| **`ClinicalImpression.investigation.item`** | **Referensi ke resource `Observation` | `QuestionnaireResponse` | `FamilyMemberHistory` | `DiagnosticReport` | `RiskAssessment` | `ImagingStudy`** |
| **`ClinicalImpression.problem`** | **Referensi ke resource `Condition` | `AllergyIntolerance` (Anamnesis)** |

## 13. Pengiriman Data Diagnosis

Data diagnosis pasien dapat dikirimkan menggunakan resource `Condition`. Informasi diagnosis yang dimiliki pasien dilaporkan menggunakan kode ICD-10 dan padanan dari kode SNOMED-CT. Satu *payload* `Condition` hanya dapat digunakan untuk melaporkan 1 diagnosis, sehingga apabila pasien memiliki 2 diagnosis, maka dikirimkan 2 *payload* `Condition` dengan 2 pasang kode yang berbeda.

### Pemetaan Nilai Condition

Berikut pemetaan nilai untuk `Condition` yang direpresentasikan dalam peta referensi *(path)* ke properti *(element id)* terkait, untuk konteks pengiriman data diagnosis pasien:

|  |  |
| --- | --- |
|  | 1. Setiap terdapat simbol asterik `*` sebelum nama variabel/parameter/element FHIR yang disebutkan, maka variabel/parameter/element FHIR tersebut bersifat **WAJIB**, **harus ada**, atau **pasti selalu ada**, contoh: **`*Location.identifier`**. 2. **Standar format Waktu** yang digunakan dalam pengiriman data adalah **UTC +00**. Misalnya waktu **WIB**, maka format yang digunakan adalah **waktu sekarang dikurangi 7**, jika **WITA**, maka **waktu sekarang dikurangi 8**, dan Jika **WIT**, maka **waktu sekarang dikurangi 9**.  **Contoh:** Pukul 17.35 WIB tanggal 23 Agustus 2023 maka yang dikirimkan adalah waktunya perlu diubah ke UTC +00 menjadi 10.35, berarti menjadi `2023-08-23T10:35:00+00:00`. 3. **Standar format pengiriman Tanggal** tidak bisa kurang dari 03 Juni 2014. |

|  |  |
| --- | --- |
|  | Silakan klik setiap teks variabel/parameter/element FHIR pada daftar pemetaan nilai di bawah ini (berwarna **merah**), untuk membaca panduan lebih detail/lanjut ke bagian yang direferensikan. |

- [`Condition.identifier`](../../fhir/resources/condition/#condition-identifier)
- [`Condition.clinicalStatus`](../../fhir/resources/condition/#condition-clinicalStatus)
- [`Condition.verificationStatus`](../../fhir/resources/condition/#condition-verificationStatus)
- [`Condition.category`](../../fhir/resources/condition/#condition-category)
- [`Condition.severity`](../../fhir/resources/condition/#condition-severity)
- [`*Condition.code`](../../fhir/resources/condition/#condition-code)
- [`Condition.bodySite`](../../fhir/resources/condition/#condition-bodySite)
- [`*Condition.subject`](../../fhir/resources/condition/#condition-subject)
- [`*Condition.encounter`](../../fhir/resources/condition/#condition-encounter)
- [`Condition.onsetDateTime`](../../fhir/resources/condition/#condition-onsetDateTime)
- [`Condition.onsetAge`](../../fhir/resources/condition/#condition-onsetAge)
- [`Condition.onsetPeriod`](../../fhir/resources/condition/#condition-onsetPeriod)
- [`Condition.onsetRange`](../../fhir/resources/condition/#condition-onsetRange)
- [`Condition.onsetString`](../../fhir/resources/condition/#condition-onsetString)
- [`Condition.abatementDateTime`](../../fhir/resources/condition/#condition-abatementDateTime)
- [`Condition.abatementAge`](../../fhir/resources/condition/#condition-abatementAge)
- [`Condition.abatementPeriod`](../../fhir/resources/condition/#condition-abatementPeriod)
- [`Condition.abatementRange`](../../fhir/resources/condition/#condition-abatementRange)
- [`Condition.abatementString`](../../fhir/resources/condition/#condition-abatementString)
- [`Condition.recordedDate`](../../fhir/resources/condition/#condition-recordedDate)
- [`Condition.recorder`](../../fhir/resources/condition/#condition-recorder)
- [`Condition.asserter`](../../fhir/resources/condition/#condition-asserter)
- [`Condition.stage[i].summary`](../../fhir/resources/condition/#condition-stage-summary)
- [`Condition.stage[i].assessment`](../../fhir/resources/condition/#condition-stage-assessment)
- [`Condition.stage[i].type`](../../fhir/resources/condition/#condition-stage-type)
- [`Condition.evidence[i].code`](../../fhir/resources/condition/#condition-evidence-code)
- [`Condition.evidence[i].detail`](../../fhir/resources/condition/#condition-evidence-detail`)
- [`Condition.note`](../../fhir/resources/condition/#condition-note)

Penjelasan tipe mandatoris, deskripsi dan format pengisian dari setiap elemen data/*path* di dalam resource `Condition` (data diagnosis), dapat dilihat dalam resource [`Condition`](../../fhir/resources/condition/#condition). Untuk contoh pengiriman data atau *payload* dari `Condition` dapat dilihat dalam [Postman SATUSEHAT](../../postman-workshop/#postman-collection-satusehat) SATUSEHAT.

### Pemetaan Variabel dan Terminologi Spesifik

Terminologi spesifik yang digunakan dalam pengiriman data diagnosis melalui resource [`Condition`](../../fhir/resources/condition/#condition) dapat dilihat dalam tabel berikut:

Tabel 13. Terminologi Spesifik

| Pemetaan Variabel *Resource* `Condition` | |
| --- | --- |
| **Elemen/*Path* FHIR** | **Terminologi/Format Pengisian** |
| **1. Diagnosis** | |
| **`Condition.category.coding.system`** | **<http://terminology.hl7.org/CodeSystem/condition-category>** |
| **`Condition.category.coding.code`** | **encounter-diagnosis** |
| **`Condition.category.coding.display`** | **Encounter Diagnosis** |
| **`Condition.code.coding.system`** | **<http://hl7.org/fhir/sid/icd-10>** |
| **`Condition.code.coding.code`** | **ICD-10 code** |
| **`Condition.code.coding.display`** | **ICD-10 Code Description** |
| **`Condition.code.coding.system`** | **<http://snomed.info/sct>** |
| **`Condition.code.coding.code`** | **SNOMED-CT Code**  **Ruang lingkup kode SNOMED CT yang dapat dipakai: Expression Constraint Language (ECL) Query : < 404684003 | Clinical finding (finding)|**  **(Untuk Kode Lengkapnya dapat dilihat pada Dokumen Lampiran [Standar Terminologi](../../terminology/standar-terminologi/#standar-terminologi) SATUSEHAT)** |
| **`Condition.code.coding.display`** | **SNOMED-CT Description** |
| **`Condition.stage.assessment`** | **Referensi ke Rasional Klinis (`ClinicalImpression`)** |

## 14. Pengiriman Data Penilaian Risiko

Data penilaian risiko dapat berupa prediksi maupun mitigasi yang akan dilakukan atas kondisi pasien. Data penilaian risiko dapat dikirimkan melalui resource `RiskAssessment`.

### Pemetaan Nilai RiskAssessment

Berikut pemetaan nilai untuk `RiskAssessment` yang direpresentasikan dalam peta referensi (*path*) ke properti (*element id*) terkait:

|  |  |
| --- | --- |
|  | 1. Setiap terdapat simbol asterik `*` sebelum nama variabel/parameter/element FHIR yang disebutkan, maka variabel/parameter/element FHIR tersebut bersifat **WAJIB**, **harus ada**, atau **pasti selalu ada**, contoh: **`*Location.identifier`**. 2. **Standar format Waktu** yang digunakan dalam pengiriman data adalah **UTC +00**. Misalnya waktu **WIB**, maka format yang digunakan adalah **waktu sekarang dikurangi 7**, jika **WITA**, maka **waktu sekarang dikurangi 8**, dan Jika **WIT**, maka **waktu sekarang dikurangi 9**.  **Contoh:** Pukul 17.35 WIB tanggal 23 Agustus 2023 maka yang dikirimkan adalah waktunya perlu diubah ke UTC +00 menjadi 10.35, berarti menjadi `2023-08-23T10:35:00+00:00`. 3. **Standar format pengiriman Tanggal** tidak bisa kurang dari 03 Juni 2014. |

|  |  |
| --- | --- |
|  | Silakan klik setiap teks variabel/parameter/element FHIR pada daftar pemetaan nilai di bawah ini (berwarna **merah**), untuk membaca panduan lebih detail/lanjut ke bagian yang direferensikan. |

- [`RiskAssessment.identifier`](../../fhir/resources/risk-assessment/#riskassessment-identifier)
- [`RiskAssessment.basedOn`](../../fhir/resources/risk-assessment/#riskassessment-basedon)
- [`RiskAssessment.parent`](../../fhir/resources/risk-assessment/#riskassessment-parent)
- [`*RiskAssessment.status`](../../fhir/resources/risk-assessment/#riskassessment-status)
- [`RiskAssessment.method`](../../fhir/resources/risk-assessment/#riskassessment-method)
- [`RiskAssessment.code`](../../fhir/resources/risk-assessment/#riskassessment-code)
- [`*RiskAssessment.subject`](../../fhir/resources/risk-assessment/#riskassessment-subject)
- [`RiskAssessment.encounter`](../../fhir/resources/risk-assessment/#riskassessment-encounter)
- [`RiskAssessment.occurence[x]`](../../fhir/resources/risk-assessment/#riskassessment-occurence)
- [`RiskAssessment.occurenceDateTime`](../../fhir/resources/risk-assessment/#riskassessment-occurencedatetime)
- [`RiskAssessment.occurencePeriod`](../../fhir/resources/risk-assessment/#riskassessment-occurenceperiod)
- [`RiskAssessment.condition`](../../fhir/resources/risk-assessment/#riskassessment-condition)
- [`RiskAssessment.performer`](../../fhir/resources/risk-assessment/#riskassessment-performer)
- [`RiskAssessment.reasonCode`](../../fhir/resources/risk-assessment/#riskassessment-reasoncode)
- [`RiskAssessment.reasonReference`](../../fhir/resources/risk-assessment/#riskassessment-reasonreference)
- [`RiskAssessment.basis`](../../fhir/resources/risk-assessment/#riskassessment-basis)
- [`RiskAssessment.prediction`](../../fhir/resources/risk-assessment/#riskassessment-prediction)
- [`RiskAssessment.prediction.outcome`](../../fhir/resources/risk-assessment/#riskassessment-prediction-outcome)
- [`RiskAssessment.prediction.probability[x]`](../../fhir/resources/risk-assessment/#riskassessment-prediction-probability)
- [`RiskAssessment.prediction.probabilityDecimal`](../../fhir/resources/risk-assessment/#riskassessment-prediction-probabilitydecimal)
- [`RiskAssessment.prediction.probabilityRange`](../../fhir/resources/risk-assessment/#riskassessment-prediction-probabilityrange)
- [`RiskAssessment.prediction.qualitativeRisk`](../../fhir/resources/risk-assessment/#riskassessment-prediction-qualitativerisk)
- [`RiskAssessment.prediction.relativeRisk`](../../fhir/resources/risk-assessment/#riskassessment-prediction-relativerisk)
- [`RiskAssessment.prediction.when[x]`](../../fhir/resources/risk-assessment/#riskassessment-prediction-when)
- [`RiskAssessment.prediction.whenPeriod`](../../fhir/resources/risk-assessment/#riskassessment-prediction-whenperiod)
- [`RiskAssessment.prediction.whenRange`](../../fhir/resources/risk-assessment/#riskassessment-prediction-whenrange)
- [`RiskAssessment.prediction.rationale`](../../fhir/resources/risk-assessment/#riskassessment-prediction-rationale)
- [`RiskAssessment.mitigation`](../../fhir/resources/risk-assessment/#riskassessment-mitigation)
- [`RiskAssessment.note`](../../fhir/resources/risk-assessment/#riskassessment-note)

### Pemetaan Variabel dan Terminologi Spesifik

Terminologi spesifik yang digunakan dalam pengiriman data penilaian risiko melalui resource `RiskAssessment` dapat dilihat dalam tabel berikut:

Tabel 14. Variabel dan Terminologi Spesifik

| Pemetaan Variabel *Resource* `Procedure` | |
| --- | --- |
| **Elemen/*Path* FHIR** | **Terminologi/Format Pengisian** |
| **Penilaian Risiko** | |
| **`RiskAssesment.code.coding.system`** | **<http://snomed.info/sct>** |
| **`RiskAssesment.code.coding.code`** | **SNOMED-CT Code**  **Ruang lingkup kode SNOMED CT yang dapat dipakai: Expression Constraint Language (ECL) Query: < 225338004 | Risk assessment (procedure) |**  **(Untuk Kode Lengkapnya dapat dilihat pada Dokumen Lampiran [Standar Terminologi](../../terminology/standar-terminologi/#standar-terminologi) SATUSEHAT)** |
| **`RiskAssesment.code.coding.display`** | **SNOMED-CT Description** |
| **`RiskAssessment.condition`** | **Referensi ke Diagnosis (resource `Condition`)** |
| **`RiskAssesment.reasonReference`** | **Referensi ke kondisi spesifik yang memerlukan penilaian risiko (resource `Condition` | `Observation`)** |
| **`RiskAssessment.prediction.outcome.coding.system`** | **<http://snomed.info/sct>** |
| **`RiskAssessment.prediction.outcome.coding.code`** | **SNOMED-CT Code**  **Ruang lingkup kode SNOMED CT yang dapat dipakai: Expression Constraint Language (ECL) Query: < 64572001 |Disease (disorder)|**  **(Untuk Kode Lengkapnya dapat dilihat pada Dokumen Lampiran [Standar Terminologi](../../terminology/standar-terminologi/#standar-terminologi) SATUSEHAT)** |
| **`RiskAssessment.prediction.outcome.coding.display`** | **SNOMED-CT Description** |
| **`RiskAssessment.prediction.probabilityDecimal`** | **(Tipe data *decimal*)** |
| **`RiskAssessment.prediction.qualitativeRisk.coding.system`** | **<http://terminology.hl7.org/CodeSystem/risk-probability>** |
| **`RiskAssessment.prediction.qualitativeRisk.coding.code`** | **Kode prediksi risiko kualitatif**  **Kode dapat diisi dengan kode prediksi risiko kualitatif dari FHIR Terminology.**  **(Untuk Kode Lengkapnya dapat dilihat pada Dokumen Lampiran [Standar Terminologi](../../terminology/standar-terminologi/#standar-terminologi) SATUSEHAT)** |
| **`RiskAssessment.prediction.qualitativeRisk.coding.display`** | **Deskripsi prediksi risiko kualitatif** |
| **`RiskAssessment.prediction.relativeRisk`** | **(Tipe data *decimal*)** |
| **`RiskAssessment.prediction.whenPeriod.start`** | **(Tipe data *dateTime*)** |
| **`RiskAssessment.prediction.whenPeriod.end`** | **(Tipe data *dateTime*)** |
| **`RiskAssessment.prediction.whenRange.low`** | **(Tipe data Quantity)** |
| **`RiskAssessment.prediction.whenRange.high`** | **(Tipe data Quantity)** |
| **`RiskAssesment.mitigation`** | **(Tipe data *string*)** |
| **`RiskAssesment.note`** | **(Tipe data *`string`*)** |
| **`ClinicalImpression.prognosisReference`** | **Referensi ke `RiskAssessment` (menambahkan referensi pada Pengiriman Data Rasional Klinis)** |

## 15. Pengiriman Data Tindakan/Prosedur Medis

Data terkait Tindakan/Prosedur Medis terdiri dari Permintaan Tindakan/ Prosedur Medis, Pelaksanaan Tindakan/ Prosedur Medis, dan Hasil Tindakan/Prosedur Medis. Data permintaan tindakan/prosedur medis dikirimkan dengan menggunakan resource `ServiceRequest`. Pemetaan nilai resource `ServiceRequest` dapat dilihat pada Bab 10. Pengiriman Data Pemeriksaan Penunjang Laboratorium maupun Bab 11. Pengiriman Data Pemeriksaan Penunjang Radiologi.

Data pelaksanaan tindakan/prosedur medis yang dilakukan terhadap seorang pasien baik tindakan diagnostik maupun tindakan terapetik dapat dikirimkan melalui resource `Procedure`. Tindakan yang dilaporkan dapat berupa tindakan non-invasif (konsultasi, edukasi) maupun invasif (contoh operasi). Standar kode tindakan/prosedur medis yang dikirimkan ke SATUSEHAT menggunakan kode ICD-9 CM.

Untuk tindakan/prosedur medis yang dilakukan untuk mendukung penentuan diagnosis maka perlu dikirimkan dengan data hasil tindakan/prosedur medis. Data hasil tindakan/prosedur medis dikirimkan dengan menggunakan resource `Observation`. Pemetaan nilai resource `Observation` dapat dilihat pada dapat dilihat pada Bab 10. Pengiriman Data Pemeriksaan Penunjang Laboratorium maupun Bab 11. Pengiriman Data Pemeriksaan Penunjang Radiologi.

### Pemetaan Nilai Procedure

Berikut pemetaan nilai untuk `Procedure` yang direpresentasikan dalam peta referensi *(path)* ke properti *(element id)* terkait, untuk konteks data tindakan/prosedur medis:

|  |  |
| --- | --- |
|  | 1. Setiap terdapat simbol asterik `*` sebelum nama variabel/parameter/element FHIR yang disebutkan, maka variabel/parameter/element FHIR tersebut bersifat **WAJIB**, **harus ada**, atau **pasti selalu ada**, contoh: **`*Location.identifier`**. 2. **Standar format Waktu** yang digunakan dalam pengiriman data adalah **UTC +00**. Misalnya waktu **WIB**, maka format yang digunakan adalah **waktu sekarang dikurangi 7**, jika **WITA**, maka **waktu sekarang dikurangi 8**, dan Jika **WIT**, maka **waktu sekarang dikurangi 9**.  **Contoh:** Pukul 17.35 WIB tanggal 23 Agustus 2023 maka yang dikirimkan adalah waktunya perlu diubah ke UTC +00 menjadi 10.35, berarti menjadi `2023-08-23T10:35:00+00:00`. 3. **Standar format pengiriman Tanggal** tidak bisa kurang dari 03 Juni 2014. |

|  |  |
| --- | --- |
|  | Silakan klik setiap teks variabel/parameter/element FHIR pada daftar pemetaan nilai di bawah ini (berwarna **merah**), untuk membaca panduan lebih detail/lanjut ke bagian yang direferensikan. |

- [`Procedure.identifier`](../../fhir/resources/procedure/#procedure-identifier)
- [`Procedure.basedOn`](../../fhir/resources/procedure/#procedure-basedOn)
- [`Procedure.partOf`](../../fhir/resources/procedure/#procedure-partOf)
- [`*Procedure.status`](../../fhir/resources/procedure/#procedure-status)
- [`Procedure.statusReason`](../../fhir/resources/procedure/#procedure-statusReason)
- [`Procedure.category`](../../fhir/resources/procedure/#procedure-category)
- [`*Procedure.code`](../../fhir/resources/procedure/#procedure-code)
- [`*Procedure.subject`](../../fhir/resources/procedure/#procedure-subject)
- [`*Procedure.encounter`](../../fhir/resources/procedure/#procedure-encounter)
- [`Procedure.performedDateTime`](../../fhir/resources/procedure/#procedure-performedDateTime)
- [`Procedure.performedPeriod`](../../fhir/resources/procedure/#procedure-performedPeriod)
- [`Procedure.performedString`](../../fhir/resources/procedure/#procedure-performedString)
- [`Procedure.performedAge`](../../fhir/resources/procedure/#procedure-performedAge)
- [`Procedure.performedRange`](../../fhir/resources/procedure/#procedure-performedRange)
- [`Procedure.recorder`](../../fhir/resources/procedure/#procedure-recorder)
- [`Procedure.asserter`](../../fhir/resources/procedure/#procedure-asserter)
- [`Procedure.performer[i].function`](../../fhir/resources/procedure/#procedure-performer-function)
- [`*Procedure.performer[i].actor`](../../fhir/resources/procedure/#procedure-performer-actor)
- [`Procedure.performer[i].onBehalfOf`](../../fhir/resources/procedure/#procedure-performer-onBehalfOf)
- [`Procedure.location`](../../fhir/resources/procedure/#procedure-location)
- [`Procedure.reasonCode`](../../fhir/resources/procedure/#procedure-reasonCode)
- [`Procedure.reasonReference`](../../fhir/resources/procedure/#procedure-reasonReference)
- [`Procedure.bodySite`](../../fhir/resources/procedure/#procedure-bodySite)
- [`Procedure.outcome`](../../fhir/resources/procedure/#procedure-outcome)
- [`Procedure.report`](../../fhir/resources/procedure/#procedure-report)
- [`Procedure.complication`](../../fhir/resources/procedure/#procedure-complication)
- [`Procedure.complicationDetail`](../../fhir/resources/procedure/#procedure-complicationDetail)
- [`Procedure.followUp`](../../fhir/resources/procedure/#procedure-followUp)
- [`Procedure.note[i].authorReference`](../../fhir/resources/procedure/#procedure-note-authorReference)
- [`Procedure.note[i].note.time`](../../fhir/resources/procedure/#procedure-note-time)
- [`Procedure.note[i].note.text`](../../fhir/resources/procedure/#procedure-note-text)
- [`Procedure.focalDevice[i].action`](../../fhir/resources/procedure/#procedure-focalDevice-action)
- [`*Procedure.focalDevice[i].manipulated`](../../fhir/resources/procedure/#procedure-focalDevice-manipulated)
- [`Procedure.usedReference`](../../fhir/resources/procedure/#procedure-usedReference)
- [`Procedure.usedCode`](../../fhir/resources/procedure/#procedure-usedCode)

Penjelasan tipe mandatoris, deskripsi dan format pengisian dari setiap elemen data/*path* di dalam resource `Procedure` (data tindakan/prosedur medis), dapat dilihat dalam resource [`Procedure`](../../fhir/resources/procedure/#procedure). Untuk contoh pengiriman data atau *payload* dari `Procedure` dapat dilihat dalam [Postman SATUSEHAT](../../postman-workshop/#postman-collection-satusehat) SATUSEHAT.

### Pemetaan Variabel dan Terminologi Spesifik

Terminologi spesifik yang digunakan dalam pengiriman data Tindakan melalui resource `Procedure` dapat dilihat dalam tabel berikut:

Tabel 15. Variabel dan Terminologi Spesifik

| Pemetaan Variabel *Resource* `Procedure` | |
| --- | --- |
| **Elemen/*Path* FHIR** | **Terminologi/Format Pengisian** |
| **Permintaan Tindakan** | |
| **`ServiceRequest.category.coding.system`** | **<http://snomed.info/sct>** |
| **`ServiceRequest.category.coding.code`** | **SNOMED-CT Code**  **Ruang lingkup kode SNOMED CT yang dapat dipakai mengacu pada daftar kode kategori pemeriksaan yang terdapat pada Dokumen Lampiran [Standar Terminologi](../../terminology/standar-terminologi/#standar-terminologi) SATUSEHAT** |
| **`ServiceRequest.category.coding.display`** | **SNOMED-CT Description** |
| **`ServiceRequest.code.coding.system`** | **<http://hl7.org/fhir/sid/icd-9-cm>** |
| **`ServiceRequest.code.coding.code`** | **ICD-9 CM Code** |
| **`ServiceRequest.code.coding.display`** | **ICD-9 CM Code Description** |
| **`ServiceRequest.code.coding.system`** | **<http://terminology.kemkes.go.id/CodeSystem/kptl>** |
| **`ServiceRequest.code.coding.code`** | **Kode KPTL**  **Ruang lingkup kode KPTL yang dapat dipakai mencakup kode terkait tindakan/prosedur medis yang bersifat sepadan dengan kode ICD-9 CM yang digunakan**  **(Untuk Kode Lengkapnya dapat dilihat pada Buku Panduan Kode Pembiayaan Tindakan dan Layanan Kesehatan (KPTL))** |
| **`ServiceRequest.code.coding.display`** | **Deskripsi KPTL** |
| **Pelaksanaan Tindakan** | |
| **1. Nama Tindakan** | |
| **`Procedure.category.coding.system`** | **<http://snomed.info/sct>** |
| **`Procedure.category.coding.code`** | **SNOMED-CT Code**  **Ruang lingkup kode SNOMED CT yang dapat dipakai: Expression Constraint Language (ECL) Query: < 71388002 |Procedure (procedure)|**  **(Untuk Kode Lengkapnya dapat dilihat di Dokumen Lampiran [Standar Terminologi](../../terminology/standar-terminologi/#standar-terminologi) SATUSEHAT)** |
| **`Procedure.category.coding.display`** | **SNOMED-CT Description** |
| **`Procedure.code.coding.system`** | **<http://hl7.org/fhir/sid/icd-9-cm>** |
| **`Procedure.code.coding.code`** | **ICD-9 CM Code** |
| **`Procedure.code.coding.display`** | **ICD-9 CM Code Description** |
| **`Procedure.code.coding.system`** | **<http://snomed.info/sct>** |
| **`Procedure.code.coding.code`** | **SNOMED-CT Code**  **Ruang lingkup kode SNOMED CT yang dapat dipakai: Expression Constraint Language (ECL) Query: < 71388002 |Procedure (procedure)|**  **(Untuk Kode Lengkapnya dapat dilihat di Dokumen Lampiran [Standar Terminologi](../../terminology/standar-terminologi/#standar-terminologi) SATUSEHAT)** |
| **`Procedure.code.coding.display`** | **SNOMED-CT Description** |
| **2. Petugas yang Melaksanakan Tindakan** | |
| **`Procedure.performer.actor`** | **Referensi ke resource `Practitioner`** |
| **3. Tanggal dan Waktu Pelaksanaan Tindakan** | |
| **a. Tanggal dan Waktu Mulai Tindakan** | |
| **`Procedure.performedPeriod.start`** | ***(Tipe data dateTime)*** |
| **b. Tanggal dan Waktu Selesai Tindakan** | |
| **`Procedure.performedPeriod.end`** | ***(Tipe data dateTime)*** |
| **4. Farmasi dan Alat Medis yang Digunakan** | |
| **`Procedure.usedCode.coding.system`** | **<http://sys-ids.kemkes.go.id/kfa>** |
| **`Procedure.usedCode.coding.code`** | **Kode KFA** |
| **`Procedure.usedCode.coding.display`** | **Deskripsi Kode KFA** |
| ****Keterangan:** Penggunaan kode KFA terkait alat kesehatan untuk sementara dapat menggunakan kode khusus yaitu kode 32999999 (Kode Produk Virtual) dan 33999999 (Kode Produk Aktual) dengan menggunakan display sesuai dengan nama alat kesehatan yang digunakan pada pelayanan yang diberikan kepada pasien. Penggunaan kode yang sesungguhnya akan diinformasikan lebih lanjut ketika sudah dapat dipublikasikan.** | |
| **5. Hasil Tindakan/Prosedur Medis** | |
| **Lihat di subbab 15.2.1 untuk Ketentuan Pengisian Hasil Tindakan** | |

#### Ketentuan Pengisian Hasil Tindakan

Jika terdapat hasil tindakan yang perlu dilaporkan secara mendetail (misalnya dalam tindakan diagnostik), pengiriman dapat dilakukan menggunakan resource `Observation`. Berikut adalah ketentuan pengisian data hasil tindakan melalui resource `Observation`:

1. Kode LOINC, kode Pemeriksaan Penunjang Nasional, maupun kode SNOMED-CT digunakan pada elemen `Observation.code` untuk merepresentasikan nama tindakan yang dilakukan dan elemen `Observation.component.code` untuk merepresentasikan komponen hasil tindakan diagnostik. Referensi pemetaan dapat dilihat pada [Lampiran Terminologi Tindakan/Prosedur Diagnostik](https://docs.google.com/spreadsheets/u/0/d/1YaWjyQS5G4dMq9kl-In5Mc-U4njnZcBkxu2KOA56TaU/edit) Elemen `Observation.category.coding` diisi dengan kode `procedure`.
2. Pemilihan elemen `Observation.value[x]` dan `Observation.component.value[x]` disesuaikan dengan tipe hasil pemeriksaan laboratorium.

   1. `Observation.valueCodeableConcept` atau `Observation.component.valueCodeableConcept` untuk tipe hasil *Nominal*
   2. `Observation.valueCodeableConcept` atau `Observation.component.valueCodeableConcept` untuk tipe hasil *Ordinal*
   3. `Observation.valueQuantity` atau `Observation.component.valueQuantity` untuk tipe hasil Kuantitatif/*Quantitative*
   4. `Observation.valueString` atau `Observation.component.valueString` untuk tipe hasil Naratif/*Narrative*
   5. `Observation.valueBoolean` atau `Observation.component.valueBoolean` untuk tipe pilihan jawaban ya/tidak

Teknis Pengiriman Data

- Satu *payload* atau satu record data resource `Observation` hanya dapat digunakan untuk 1 kode nama tindakan diagnostik yang dilakukan. Jika dilakukan lebih dari satu tindakan diagnostik maka perlu dikirimkan dalam 2 *payload* berbeda
- **Contoh:** Dilakukan 2 tindakan diagnostik, misal tindakan EKG dan Ekokardiografi, maka data hasil tindakan EKG dan Ekokardiografi perlu dikirimkan dalam 2 *payload* berbeda. Payload pertama berisi 1 kode tindakan diagnostik EKG dan *payload* kedua berisi kode tindakan Ekokardiografi.

## 16. Pengiriman Data Peresepan Obat

Data terkait Farmasi meliputi pengiriman data peresepan obat, dan pengeluaran obat. Data terkait Farmasi dikirimkan menggunakan resource `Medication`, `MedicationRequest`, dan `Medication Dispense`.

**Skema Proses Peresepan dan Pengeluaran Obat**  
Data proses peresepan dan pengeluaran obat pada fasilitas pelayanan kesehatan akan menggunakan kamus farmasi dan alat kesehatan (KFA) yang dikeluarkan oleh Kementerian Kesehatan. KFA merupakan kamus master data produk farmasi dan alat kesehatan yang memuat kode unik untuk setiap produk farmasi dan alat kesehatan sehingga dapat digunakan dan diintegrasikan pada semua sistem yang digunakan pelaku industri kesehatan. Berikut merupakan Struktur Model KFA.

![Struktur Model KFA](../_images/struktur-model-kfa.png)

Gambar 9. Struktur Model KFA

Struktur Model KFA untuk Obat memiliki Format Kode Obat SATUSEHAT, yaitu berisi Numerik 8 digit dengan 2 digit prefiks dan 6 digit nomor urut.

1. BZA adalah Bahan Zat Aktif dengan kode 91xxxxxx. Kode obat awalan 91 memuat tentang nama bahan zat aktif, UCUM, dan jenis farmalkes. Contoh kode 91000101 untuk mewakili nama bahan zat aktif Paracetamol.
2. POV adalah Produk Obat Virtual dengan kode 92xxxxxx. Kode obat awalan 92 memuat informasi tentang penamaan produk template dengan format penamaan bahan zat aktif, kekuatan, satuan, dan bentuk sediaan. Kode awalan 92 berfungsi untuk mencari informasi mengenai bentuk sediaan, golongan obat, rute pemberian, info ATC, ATC/DDD, Info Dagang, Bahan Zat aktif dan kekuatan, dan dosis pemakaian. Contoh kode 92000511 mewakili produk Paracetamol 120 mg/5 mL Sirup.
3. POA adalah Produk Obat Aktual dengan kode 93xxxxxx. Kode obat awalan 93 merupakan turunan dari produk template yang lebih detail dengan menambahkan atribut brand, volume, rasa, dan varian lainnya. Contoh kode 93002205 mewakili produk Paracetamol 120 mg/5 mL Sirup (ERPHAMOL).
4. POAK adalah Produk Obat Aktual dalam Kemasan dengan kode 94xxxxxx. Kode obat awalan 94 menjelaskan produk aktual berdasarkan kemasan dari masing-masing obat atau vaksin. Contoh kode 94002470 mewakili kemasan dus isi 1 pada obat Paracetamol 120 mg/5 mL Sirup (ERPHAMOL).

Berikut merupakan alur detail penukaran resep dokter di apotek/instalasi farmasi:

![Alur Detail Penukaran Resep Dokter di Apotek/Instalasi Farmasi](../_images/alur-penukaran-resep-apotek.png)

Gambar 10. Alur Detail Penukaran Resep Dokter di Apotek/Instalasi Farmasi

**Pengiriman Data Peresepan Obat**  
Pengiriman data peresepan obat akan menggunakan 2 *resources* yaitu `Medication` dan `MedicationRequest`. resource [`Medication`](../../fhir/resources/medication/#medication) akan mencatatkan data umum terkait obat yang akan diresepkan. Sedangkan resource [`MedicationRequest`](../../fhir/resources/medication-request/#medicationrequest) akan digunakan untuk mengirimkan data terkait peresepan obat seperti jumlah yang diresepkan, instruksi minum obat dan lain-lain. Kedua data ini dikirimkan secara bersamaan sebagai 1 paket yaitu `Medication` dan `MedicationRequest`. Satu *payload* `Medication` dan `MedicationRequest` hanya dapat digunakan untuk peresepan 1 jenis obat saja. Apabila terdapat 2 jenis obat yang diresepkan, maka dikirimkan 2 paket `Medication` dan `MedicationRequest`.

![Skema Peresepan 1 Obat](../_images/skema-peresepan1.png)

Gambar 11. Skema Peresepan 1 Obat

![Skema Peresepan 2 Obat](../_images/skema-peresepan2.png)

Gambar 12. Skema Peresepan 2 Obat

Pengiriman data dapat dilakukan dengan 2 cara yaitu:

1. Mengirimkan *payload* `Medication` dan `MedicationRequest` secara terpisah (2 kali POST)
2. Mengirimkan *payload* `MedicationRequest` yang mengandung resource `Medication` dalam `MedicationRequest.contained` (1 kali POST)

Contoh pengiriman data atau *payload* untuk pengiriman data peresepan obat dapat dilihat dalam Postman Collection.

### Pemetaan Nilai Medication

Berikut pemetaan nilai untuk `Medication` yang direpresentasikan dalam peta referensi *(path)* ke properti *(element id)* terkait, untuk konteks data kode lokal obat di masing-masing institusi:

|  |  |
| --- | --- |
|  | Setiap terdapat simbol asterik `*` sebelum nama variabel/parameter/element FHIR yang disebutkan, maka variabel/parameter/element FHIR tersebut bersifat **WAJIB**, **harus ada**, atau **pasti selalu ada**, contoh: **`*Location.identifier`**. |

|  |  |
| --- | --- |
|  | Silakan klik setiap teks variabel/parameter/element FHIR pada daftar pemetaan nilai di bawah ini (berwarna **merah**), untuk membaca panduan lebih detail/lanjut ke bagian yang direferensikan. |

- [`*Medication.identifier[i]`](../../fhir/resources/medication/#medication-identifier)
- [`Medication.code`](../../fhir/resources/medication/#medication-code)
- [`Medication.status`](../../fhir/resources/medication/#medication-status)
- [`Medication.manufacturer`](../../fhir/resources/medication/#medication-manufacturer)
- [`Medication.form`](../../fhir/resources/medication/#medication-form)
- [`Medication.ingredient`](../../fhir/resources/medication/#medication-ingredient)
- [`Medication.batch`](../../fhir/resources/medication/#medication-batch)
- [`Medication.batch.lotNumber`](../../fhir/resources/medication/#medication-batch-lotNumber)
- [`Medication.batch.expirationDate`](../../fhir/resources/medication/#medication-batch-expirationDate)
- [`*Medication.extension:medicationType`](../../fhir/resources/medication/#medication-extension)

Penjelasan tipe mandatoris, deskripsi dan format pengisian dari setiap elemen data/*path* di dalam resource `Medication` (data peresepan obat), dapat dilihat dalam resource [`Medication`](../../fhir/resources/medication/#medication). Untuk contoh pengiriman data atau *payload* dari `Medication` dapat dilihat dalam [Postman SATUSEHAT](../../postman-workshop/#postman-collection-satusehat) SATUSEHAT.

### Pemetaan Nilai MedicationRequest

Berikut pemetaan nilai untuk `MedicationRequest` yang direpresentasikan dalam peta referensi *(path)* ke properti *(element id)* terkait, untuk konteks data pengobatan yang diberikan:

|  |  |
| --- | --- |
|  | 1. Setiap terdapat simbol asterik `*` sebelum nama variabel/parameter/element FHIR yang disebutkan, maka variabel/parameter/element FHIR tersebut bersifat **WAJIB**, **harus ada**, atau **pasti selalu ada**, contoh: **`*Location.identifier`**. 2. **Standar format Waktu** yang digunakan dalam pengiriman data adalah **UTC +00**. Misalnya waktu **WIB**, maka format yang digunakan adalah **waktu sekarang dikurangi 7**, jika **WITA**, maka **waktu sekarang dikurangi 8**, dan Jika **WIT**, maka **waktu sekarang dikurangi 9**.  **Contoh:** Pukul 17.35 WIB tanggal 23 Agustus 2023 maka yang dikirimkan adalah waktunya perlu diubah ke UTC +00 menjadi 10.35, berarti menjadi `2023-08-23T10:35:00+00:00`. 3. **Standar format pengiriman Tanggal** tidak bisa kurang dari 03 Juni 2014. |

|  |  |
| --- | --- |
|  | Silakan klik setiap teks variabel/parameter/element FHIR pada daftar pemetaan nilai di bawah ini (berwarna **merah**), untuk membaca panduan lebih detail/lanjut ke bagian yang direferensikan. |

- [`*MedicationRequest.identifier[i]`](../../fhir/resources/medication-request/#medicationrequest-identifier)
- [`*MedicationRequest.status`](../../fhir/resources/medication-request/#medicationrequest-status)
- [`MedicationRequest.statusReason`](../../fhir/resources/medication-request/#medicationrequest-statusReason)
- [`*MedicationRequest.intent`](../../fhir/resources/medication-request/#medicationrequest-intent)
- [`MedicationRequest.category`](../../fhir/resources/medication-request/#medicationrequest-category)
- [`MedicationRequest.priority`](../../fhir/resources/medication-request/#medicationrequest-priority)
- [`MedicationRequest.reportedBoolean`](../../fhir/resources/medication-request/#medicationrequest-reportedBoolean)
- [`*MedicationRequest.medicationReference`](../../fhir/resources/medication-request/#medicationrequest-medicationReference)
- [`*MedicationRequest.subject`](../../fhir/resources/medication-request/#medicationrequest-subject)
- [`MedicationRequest.encounter`](../../fhir/resources/medication-request/#medicationrequest-encounter)
- [`MedicationRequest.authoredOn`](../../fhir/resources/medication-request/#medicationrequest-authoredOn)
- [`MedicationRequest.requester`](../../fhir/resources/medication-request/#medicationrequest-requester)
- [`MedicationRequest.performer`](../../fhir/resources/medication-request/#medicationrequest-performer)
- [`MedicationRequest.performerType`](../../fhir/resources/medication-request/#medicationrequest-performerType)
- [`MedicationRequest.recorder`](../../fhir/resources/medication-request/#medicationrequest-recorder)
- [`MedicationRequest.reasonCode`](../../fhir/resources/medication-request/#medicationrequest-reasonCode)
- [`MedicationRequest.reasonReference`](../../fhir/resources/medication-request/#medicationrequest-reasonReference)
- [`MedicationRequest.basedOn`](../../fhir/resources/medication-request/#medicationrequest-basedOn)
- [`MedicationRequest.courseOfTherapyType`](../../fhir/resources/medication-request/#medicationrequest-courseOfTherapyType)
- [`MedicationRequest.insurance`](../../fhir/resources/medication-request/#medicationrequest-insurance)
- [`MedicationRequest.note`](../../fhir/resources/medication-request/#medicationrequest-note)
- [`MedicationRequest.dosageInstruction[i].sequence`](../../fhir/resources/medication-request/#medicationrequest-dosageInstruction-sequence)
- [`MedicationRequest.dosageInstruction[i].text`](../../fhir/resources/medication-request/#medicationrequest-dosageInstruction-text)
- [`MedicationRequest.dosageInstruction[i].additionalInstruction`](../../fhir/resources/medication-request/#medicationrequest-identifier)
- [`MedicationRequest.dosageInstrution[i].patientInstruction`](../../fhir/resources/medication-request/#medicationrequest-dosageInstruction-patientInstruction)
- [`MedicationRequest.dosageInstruction[i].timing`](../../fhir/resources/medication-request/#medicationrequest-dosageInstruction-timing)
- [`MedicationRequest.dosageInstruction.timing[i].event`](../../fhir/resources/medication-request/#medicationrequest-dosageInstruction-timing-event)
- [`*MedicationRequest.dosageInstruction[i].timing.repeat`](../../fhir/resources/medication-request/#medicationrequest-dosageInstruction-timing-repeat)
- [`MedicationRequest.dosageInstruction[i].timing.code`](../../fhir/resources/medication-request/#medicationrequest-dosageInstruction-timing-code)
- [`MedicationRequest.dosageInstruction[i].site`](../../fhir/resources/medication-request/#medicationrequest-dosageInstruction)
- [`*MedicationRequest.dosageInstruction[i].route`](../../fhir/resources/medication-request/#medicationrequest-dosageInstruction)
- [`MedicationRequest.dosageInstruction[i].method`](../../fhir/resources/medication-request/#medicationrequest-dosageInstruction-doseAndRate-method)
- [`MedicationRequest.dosageInstruction[i].doseAndRate.type`](../../fhir/resources/medication-request/#medicationrequest-dosageInstruction-doseAndRate-type)
- [`MedicationRequest.dosageInstruction[i].doseAndRate.dose<?>`](../../fhir/resources/medication-request/#medicationrequest-dosageInstruction-doseAndRate-dose)
- [`MedicationRequest.dosageInstruction[i].doseAndRate.rate<?>`](../../fhir/resources/medication-request/#medicationrequest-dosageInstruction-doseAndRate-rate)
- [`MedicationRequest.dosageInstruction[i].doseAndRate.rateRatio`](../../fhir/resources/medication-request/#medicationrequest-dosageInstruction-doseAndRate-rateRatio)
- [`MedicationRequest.dosageInstruction[i].doseAndRate.rateRange`](../../fhir/resources/medication-request/#medicationrequest-dosageInstruction-doseAndRate-rateRange)
- [`MedicationRequest.dosageInstruction[i].doseAndRate.rateQuantity`](../../fhir/resources/medication-request/#medicationrequest-dosageInstruction-doseAndRate-rateQuantity)
- [`MedicationRequest.dosageInstruction[i].maxDosePerPeriod`](../../fhir/resources/medication-request/#medicationrequest-dosageInstruction-maxDosePerPeriod)
- [`MedicationRequest.dosageInstruction[i].maxDosePerAdministration`](../../fhir/resources/medication-request/#medicationrequest-dosageInstruction-maxDosePerAdministration)
- [`MedicationRequest.dosageInstruction[i].maxDosePerLifeTime`](../../fhir/resources/medication-request/#medicationrequest-dosageInstruction-maxDosePerLifeTime)
- [`MedicationRequest.dispenseRequest.dispenseInterval`](../../fhir/resources/medication-request/#medicationrequest-dispenseRequest-dispenseInterval)
- [`MedicationRequest.dispenseRequest.validityPeriod`](../../fhir/resources/medication-request/#medicationrequest-dispenseRequest-validityPeriod)
- [`MedicationRequest.dispenseRequest.numberOfRepeatsAllowed`](../../fhir/resources/medication-request/#medicationrequest-dispenseRequest-numberOfRepeatsAllowed)
- [`MedicationRequest.dispenseRequest.quantity`](../../fhir/resources/medication-request/#medicationrequest-dispenseRequest-quantity-numberOfRepeatsAllowed)
- [`MedicationRequest.dispenseRequest.expectedSupplyDuration`](../../fhir/resources/medication-request/#medicationrequest-dispenseRequest-expectedSupplyDuration)
- [`MedicationRequest.dispenseRequest.performer`](../../fhir/resources/medication-request/#medicationrequest-dispenseRequest-performer)
- [`*MedicationRequest.substitution.allowed<?>`](../../fhir/resources/medication-request/#medicationrequest-substitution-allowed)
- [`MedicationRequest.substitution.allowedBoolean`](../../fhir/resources/medication-request/#medicationrequest-substitution-allowedBoolean)
- [`MedicationRequest.substitution.allowedCodeableConcept`](../../fhir/resources/medication-request/#medicationrequest-substitution-allowedCodeableConcept)
- [`MedicationRequest.substitution.reason`](../../fhir/resources/medication-request/#medicationrequest-substitution-reason)

Penjelasan tipe mandatoris, deskripsi dan format pengisian dari setiap elemen data/*path* di dalam resource `MedicationRequest` (data peresepan obat), dapat dilihat dalam resource [`MedicationRequest`](../../fhir/resources/medication-request/#medicationrequest). Untuk contoh pengiriman data atau *payload* dari `MedicationRequest` dapat dilihat dalam [Postman SATUSEHAT](../../postman-workshop/#postman-collection-satusehat) SATUSEHAT.

### Pemetaan Variabel dan Terminologi Spesifik

Terminologi spesifik yang digunakan dalam pengiriman data peresepan obat melalui resource `MedicationRequest` dapat dilihat dalam tabel berikut:

Tabel 16. Variabel dan Terminologi Spesifik

| *Resource* `Medication`, `MedicationRequest` | |
| --- | --- |
| **Elemen/*Path* FHIR** | **Terminologi/Format Pengisian** |
| **Peresepan Obat** | |
| **1. ID Resep** | |
| **`MedicationRequest.identifier`** | **Lihat di subbab 16.3.2 Ketentuan Pengisian resource `MedicationRequest` poin A. `MedicationRequest.identifier`** |
| **2. ID Obat dan Nama Obat** | |
| **`Medication.code.coding.system`** | **<http://sys-ids.kemkes.go.id/kfa>** |
| **`Medication.code.coding.code`** | **ID Obat dengan Kode Obat KFA**  **Lihat di subbab 16.3.1 Ketentuan Pengisian resource `Medication` poin A.a. `Medication.code` untuk `MedicationRequest`** |
| **`Medication.code.coding.display`** | **Nama Obat dengan Deskripsi Obat KFA** |
| **`MedicationRequest.medicationReference`** | **Referensi ke resource `Medication`** |
| **3. Bentuk/Sediaan** | |
| **`Medication.form.coding.system`** | **<http://terminology.kemkes.go.id/CodeSystem/medication-form>** |
| **`Medication.form.coding.code`** | **Kode bentuk/sediaan obat**  **(Untuk Kode Lengkapnya dapat dilihat pada Dokumen Lampiran [Standar Terminologi](../../terminology/standar-terminologi/#standar-terminologi) SATUSEHAT)** |
| **`Medication.form.coding.display`** | **Deskripsi bentuk/sediaan obat** |
| **`MedicationRequest.medicationReference`** | **Referensi ke resource `Medication`** |
| **4. Jumlah Obat** | |
| **`MedicationRequest.dispenseRequest.quantity.value`** | **(Tipe data *decimal*)** |
| **`MedicationRequest.dispenseRequest.quantity.unit`** | **UCUM unit**  **Kode satuan atau unit dapat menggunakan kode yang disediakan oleh *Unified Code for Units of Measure* (UCUM). Daftar kode satuan dapat diakses melalui link berikut : [Observation.valueQuantity](https://docs.google.com/spreadsheets/d/1OHM4ICgQ3hseGLrqi9GQzcREddU5SDKto50dhkhOjnc/edit?gid=0#gid=0) (UCUM)**  **(Untuk Kode Lengkapnya dapat dilihat pada Dokumen Lampiran [Standar Terminologi](../../terminology/standar-terminologi/#standar-terminologi) SATUSEHAT)** |
| **`MedicationRequest.dispenseRequest.quantity.system`** | **<http://unitsofmeasure.org>** |
| **`MedicationRequest.dispenseRequest.quantity.code`** | **UCUM Code** |
| **5. Metode/Rute Pemberian** | |
| **`MedicationRequest.dosageInstruction.route.coding.system`** | **<http://www.whocc.no/atc>** |
| **`MedicationRequest.dosageInstruction.route.coding.code`** | **Kode Rute Pemberian Obat WHO ATC**  **(Untuk Kode Lengkapnya dapat dilihat pada Dokumen Lampiran [Standar Terminologi](../../terminology/standar-terminologi/#standar-terminologi) SATUSEHAT)** |
| **`MedicationRequest.dosageInstruction.route.coding.display`** | **Deskripsi Rute Pemberian Obat WHO ATC** |
| **6. Dosis Obat yang Diberikan** | |
| **`MedicationRequest.dosageInstruction.doseAndRate.doseQuantity.value`** | **(Tipe data *decimal*)** |
| **7. Unit** | |
| **`MedicationRequest.dosageInstruction.doseAndRate.doseQuantity.unit`** | **UCUM unit**  **Kode satuan atau unit dapat menggunakan kode yang disediakan oleh *Unified Code for Units of Measure* (UCUM). Daftar kode satuan dapat diakses melalui link berikut : [Observation.valueQuantity](https://docs.google.com/spreadsheets/d/1OHM4ICgQ3hseGLrqi9GQzcREddU5SDKto50dhkhOjnc/edit?gid=0#gid=0) (UCUM)**  **(Untuk Kode Lengkapnya dapat dilihat pada Dokumen Lampiran [Standar Terminologi](../../terminology/standar-terminologi/#standar-terminologi) SATUSEHAT)** |
| **8. Frekuensi/Interval** | |
| **`MedicationRequest.dosageInstruction.timing`** | **Lihat di subbab 16.3.1 Ketentuan Pengisian** |
| **9. Aturan Tambahan** | |
| **`MedicationRequest.dosageInstruction.additionalInstruction.coding.system`** | **<http://snomed.info/sct>** |
| **`MedicationRequest.dosageInstruction.additionalInstruction.coding.code`** | **SNOMED-CT Code**  **Ruang lingkup kode SNOMED CT yang dapat dipakai: Expression Constraint Language (ECL) Query : < 419492006 |Additional dosage instructions (qualifier value)|**  **(Untuk Kode Lengkapnya dapat dilihat pada Dokumen Lampiran [Standar Terminologi](../../terminology/standar-terminologi/#standar-terminologi) SATUSEHAT)** |
| **`MedicationRequest.dosageInstruction.additionalInstruction.coding.display`** | **SNOMED-CT Description** |
| **`MedicationRequest.dosageInstruction.additionalInstruction.text`** | **(Tipe data *string*)** |
| **10. Catatan Resep** | |
| **`MedicationRequest.note`** | **(Tipe data *string*)** |
| **11. Dokter Penulis Resep** | |
| **`MedicationRequest.requester`** | **Referensi ke resource `Practitioner`** |
| **12. Nomor Telepon Seluler Dokter Penulis Resep** | |
| ****Keterangan:** Nomor telepon dokter penulis resep didapatkan dengan menarik data dari ID Practitioner yang direferensikan pada elemen `MedicationRequest.requester`.** | |
| **13. Tanggal Penulisan Resep** | |
| **`MedicationRequest.authoredOn`** | **(Tipe data *dateTime*)** |
| **14. Jam Penulisan Resep** | |
| **`MedicationRequest.authoredOn`** | **(Tipe data *dateTime*)** |
| **15. Status Resep** | |
| **`MedicationRequest.status`** | **Kode status peresepan obat**  **Kode dapat diisi dengan kode FHIR Terminology.**  **(Untuk Kode Lengkapnya dapat dilihat pada Dokumen Lampiran [Standar Terminologi](../../terminology/standar-terminologi/#standar-terminologi) SATUSEHAT)** |

#### Ketentuan Pengisian resource Medication

Ketentuan pengisian secara spesifik untuk pengisian resource [`Medication`](../../fhir/resources/medication/#medication) adalah sebagai berikut:

1. `Medication.code`  
   `Medication.code` dapat diisi dengan kode obat yang digunakan akan menggunakan kode obat yang tersedia pada KFA (kamus farmasi dan alat kesehatan). Daftar kode obat KFA dapat dilihat dalam [browser kamus KFA](https://dto.kemkes.go.id/kfa-browser). `Medication.code` wajib diisi apabila mengirimkan **data obat non-racikan** dengan ketentuan penggunaan kode sebagai berikut:

   1. `Medication.code` untuk `MedicationRequest` dapat menggunakan Kode Produk Obat Template (92xxxxxx) atau Kode Produk Obat Aktual (93xxxxxx), tergantung kesiapan sistem masing-masing fasyankes. Karena tidak semua sistem fasyankes memiliki dua struktur level untuk proses `MedicationRequest`, untuk `MedicationRequest` yang menggunakan kode awalan 93 dapat menggunakan kode 93 (Umum) atau kode 93 (Merek) sebagai pengganti kode 92. Hal ini dikarenakan setiap kode 92 memiliki padanan kode 93 (Umum).
   2. `Medication.code` untuk `MedicationDispense` wajib menggunakan Kode Produk Obat Aktual (93xxxxxx). Apabila tidak memiliki merek maka fasyankes dapat menggunakan kode 93 (Umum). Jika peresepan obat menggunakan kode awalan 92 maka kode 93 untuk penebusan obat sebaiknya merupakan turunan kode 92 dari obat yang diresepkan. Akan tetapi, jika farmasi tidak memiliki stok obat kode 93 dengan dosis yang sesuai, tetapi ada obat dengan zat aktif sama namun beda kekuatan maka dapat digunakan sesuai kebutuhan. Misalnya, peresepan menggunakan kode 92 Paracetamol 500mg, tetapi saat penebusan obat hanya tersedia kode 93 Paracetamol 250mg maka farmasi dapat mengeluarkan obat kode 93 Paracetamol 250mg dengan tata cara minum 2 tablet. Adapun jika memang benar-benar tidak ada maka pihak farmasi perlu memberikan copy resep agar penebusan obat dilakukan di apotek di luar fasyankes untuk mendapatkan obat yang sesuai. Adapun untuk pengiriman **data obat racikan**, `Medication.code` dapat dikosongkan.
2. `Medication.ingredient`  
   Terdapat 3 cara pengisian `Medication.ingredient` yaitu:

   1. Peresepan/pengeluaran **obat non-racikan**.

      - `Medication.ingredient` tidak wajib diisi apabila data yang dikirimkan adalah obat non-racikan.
      - `Medication.ingredient[i].itemCodeableConcept` apabila akan diisi untuk digunakan pada `MedicationRequest` dan `MedicationDispense` maka diisikan kode zat aktif dari KFA (91xxxxxx). Daftar kode zat aktif dapat dilihat pada browser kamus KFA pada link berikut: <https://dto.kemkes.go.id/kfa-browser>.
      - Pada proses peresepan dan pengeluaran obat, `Medication.ingredient.strength.numerator` dan `Medication.ingredient.strength.denominator` berisi unit dosis yang harus dipecah menjadi angka & satuan baik digunakan ketika pada `MedicationRequest` maupun pada `MedicationDispense`.
      - Contoh pengisian dapat dilihat pada tabel berikut:

.

|  |  |  |
| --- | --- | --- |
| **Medication.ingredient pada Obat Non Racikan (`MedicationRequest` dan `MedicationDispense`)** | | |
| **Azithromycin 500 mg Tablet Salut Selaput (ZITHRAX)** | | |
| **1** | **`Medication.ingredient.itemCodeableConcept`** | |
| **`Medication.ingredient.itemCodeableConcept.system`** | **<http://sys-ids.kemkes.go.id/kfa>** |
| **`Medication.ingredient.itemCodeableConcept.code`** | **91000235** |
| **`Medication.ingredient.itemCodeableConcept.display`** | **Azithromycin** |
| **2** | **`Medication.ingredient.strength.numerator`** | |
| **`Medication.ingredient.strength.numerator.value`** | **500** |
| **`Medication.ingredient.strength.numerator.system`** | **<http://unitsofmeasure.org>** |
| **`Medication.ingredient.strength.numerator.code`** | **mg** |
| **3** | **`Medication.ingredient.strength.denominator`** | |
| **`Medication.ingredient.strength.denominator.value`** | **1** |
| **`Medication.ingredient.strength.denominator.system`** | **<http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm>** |
| **`Medication.ingredient.strength.denominator.code`** | **TAB** |

1. Peresepan/pengeluaran **obat racikan** dengan instruksi berikan dalam dosis demikian/ d.t.d.

   - `Medication.ingredient` wajib diisi apabila data yang dikirimkan adalah obat racikan.
   - `Medication.ingredient[i].itemCodeableConcept` yang digunakan untuk `MedicationRequest` diisikan kode zat aktif dari KFA (91xxxxxx). Daftar kode zat aktif dapat dilihat pada browser kamus KFA pada link berikut: <https://dto.kemkes.go.id/kfa-browser>.
   - `Medication.ingredient[i].itemCodeableConcept` yang digunakan untuk `MedicationDispense` diisikan Kode Produk Obat Aktual (93xxxxxx). Daftar kode obat aktual dapat dilihat pada browser kamus KFA pada link berikut: <https://dto.kemkes.go.id/kfa-browser>.
   - Pada proses peresepan obat, `Medication.ingredient.strength.numerator` berisi unit dosis yang diresepkan dokter (Contoh: 125/mg), sedangkan `Medication.ingredient.strength.denominator` berisi banyaknya obat yang mengandung unit dosis pada numerator (Contoh: 1/kap). Adapun pada proses pengeluaran obat, `Medication.ingredient.strength.numerator` berisi banyaknya obat yang dikeluarkan dan perlu dipecah (Contoh: 5/tab), sedangkan `Medication.ingredient.strength.denominator` berisi banyaknya obat setelah dihasilkan sesuai resep dokter (Contoh: 20/cap).
   - Contoh pengisian dapat dilihat pada tabel berikut:

.

|  |  |  |
| --- | --- | --- |
| **Medication.ingredient pada Obat Racikan d.t.d (`MedicationRequest`)** | | |
| **Dokter meresepkan obat dengan kandungan Paracetamol 125 mg/ kapsul dengan jumlah 20 kapsul** | | |
| **1** | **`Medication.ingredient.itemCodeableConcept`** | |
| **`Medication.ingredient.itemCodeableConcept.system`** | **<http://sys-ids.kemkes.go.id/kfa>** |
| **`Medication.ingredient.itemCodeableConcept.code`** | **91000101** |
| **`Medication.ingredient.itemCodeableConcept.display`** | **Paracetamol** |
| **2** | **`Medication.ingredient.strength.numerator`** | |
| **`Medication.ingredient.strength.numerator.value`** | **125** |
| **`Medication.ingredient.strength.numerator.system`** | **<http://unitsofmeasure.org>** |
| **`Medication.ingredient.strength.numerator.code`** | **mg** |
| **3** | **`Medication.ingredient.strength.denominator`** | |
| **`Medication.ingredient.strength.denominator.value`** | **1** |
| **`Medication.ingredient.strength.denominator.system`** | **<http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm>** |
| **`Medication.ingredient.strength.denominator.code`** | **CAP** |

.

|  |  |  |
| --- | --- | --- |
| **Medication.ingredient pada Obat Racikan d.t.d (`MedicationDispense`)** | | |
| **Dokter meresepkan obat dengan kandungan Paracetamol 125 mg/ kapsul dengan jumlah 20 kapsul. Peresepan ini menggunakan Parasetamol 500 mg Tablet (OMEGRIP) dengan jumlah 5 tablet yang dibagi menjadi 20 kapsul.** | | |
| **1** | **`Medication.ingredient.itemCodeableConcept`** | |
| **`Medication.ingredient.itemCodeableConcept.system`** | **<http://sys-ids.kemkes.go.id/kfa>** |
| **`Medication.ingredient.itemCodeableConcept.code`** | **93002225** |
| **`Medication.ingredient.itemCodeableConcept.display`** | **Paracetamol 500 mg Tablet (OMEGRIP)** |
| **2** | **`Medication.ingredient.strength.numerator`** | |
| **`Medication.ingredient.strength.numerator.value`** | **5** |
| **`Medication.ingredient.strength.numerator.system`** | **<http://unitsofmeasure.org>** |
| **`Medication.ingredient.strength.numerator.code`** | **TAB** |
| **3** | **`Medication.ingredient.strength.denominator`** | |
| **`Medication.ingredient.strength.denominator.value`** | **20** |
| **`Medication.ingredient.strength.denominator.system`** | **<http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm>** |
| **`Medication.ingredient.strength.denominator.code`** | **CAP** |

1. Peresepan/pengeluaran **obat racikan non-d.t.d** (bagi dalam bagian-bagian yang sama).

   - `Medication.ingredient` wajib diisi apabila data yang dikirimkan adalah obat racikan.
   - `Medication.ingredient[i].itemCodeableConcept` yang digunakan untuk `MedicationRequest` dapat diisikan Kode Produk Obat Virtual (92xxxxxx) atau Kode Produk Obat Aktual (93xxxxxx), sedangkan untuk `MedicationDispense` diisikan Kode Produk Obat Aktual (93xxxxxx). Daftar kode obat aktual dapat dilihat pada browser kamus KFA pada link berikut: <https://dto.kemkes.go.id/kfa-browser>.
   - Numerator dan Denominator pada proses peresepan dan pengeluaran obat racikan non-d.t.d sama, yaitu `Medication.ingredient.strength.numerator` berisi unit dosis yang harus dipecah menjadi angka dan satuan (Contoh: 10/tab), sedangkan `Medication.ingredient.strength.denominator` berisi banyaknya obat yang perlu dibuat sesuai yang diresepkan dokter (Contoh: 30/cap).
   - Contoh pengisian dapat dilihat pada tabel berikut.

.

|  |  |  |
| --- | --- | --- |
| **Medication.ingredient pada Obat Racikan non d.t.d (`MedicationRequest` dan `MedicationDispense`)** | | |
| **Dokter meresepkan Paracetamol 500 mg Tablet (OMEGRIP) sejumlah 10 tab dibuat menjadi 30 kapsul** | | |
| **1** | **`Medication.ingredient.itemCodeableConcept`** | |
| **`Medication.ingredient.itemCodeableConcept.system`** | **<http://sys-ids.kemkes.go.id/kfa>** |
| **`Medication.ingredient.itemCodeableConcept.code`** | **93002225** |
| **`Medication.ingredient.itemCodeableConcept.display`** | **Paracetamol 500 mg Tablet (OMEGRIP)** |
| **2** | **`Medication.ingredient.strength.numerator`** | |
| **`Medication.ingredient.strength.numerator.value`** | **10** |
| **`Medication.ingredient.strength.numerator.system`** | **<http://unitsofmeasure.org>** |
| **`Medication.ingredient.strength.numerator.code`** | **TAB** |
| **3** | **`Medication.ingredient.strength.denominator`** | |
| **`Medication.ingredient.strength.denominator.value`** | **30** |
| **`Medication.ingredient.strength.denominator.system`** | **<http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm>** |
| **`Medication.ingredient.strength.denominator.code`** | **CAP** |

Matriks skenario peresepan dan pengeluaran obat dapat dilihat pada [Lampiran 3](../../terminology/lampiran-terminologi/rme-rawat-jalan1/#lampiran-3-rajal).

#### Ketentuan Pengisian resource MedicationRequest

Ketentuan pengisian secara spesifik untuk pengisian resource [`MedicationRequest`](../../fhir/resources/medication-request/#medicationrequest) adalah sebagai berikut:

1. `MedicationRequest.identifier`  
   `MedicationRequest.identifier` diisi dengan nomor lokal peresepan obat (ID resep). Terdapat 2 nomor lokal peresepan obat yang perlu dikirimkan dengan **array**, yaitu:

.

| 1. Nomor Lokal Peresepan Obat | |
| --- | --- |
| **`MedicationRequest.identifier.system`** | **<http://sys-ids.kemkes.go.id/prescription/{{Organization_ID}}>** |
| **`MedicationRequest.identifier.use`** | ***official*** |
| **`MedicationRequest.identifier.value`** | **Nomor lokal peresepan obat** |
| ****Keterangan:** Merupakan ID lokal di masing-masing institusi yang merepresentasikan satu resep yang dibuat oleh dokter (dapat terdiri dari lebih dari 1 obat dalam 1 resep).** | |
| **2. Nomor Lokal Peresepan per-item Obat** | |
| **`MedicationRequest.identifier.system`** | **<http://sys-ids.kemkes.go.id/prescription-item/{{Organization_ID}}>** |
| **`MedicationRequest.identifier.use`** | ***official*** |
| **`MedicationRequest.identifier.value`** | **Nomor lokal dari setiap item peresepan obat** |
| ****Keterangan:** Merupakan ID lokal di masing-masing institusi untuk setiap obat yang diresepkan dalam suatu resep.** | |

1. `MedicationRequest.dosageInstruction[i].sequence`  
   `MedicationRequest.dosageInstruction[i].sequence` menjelaskan urutan aturan pemakaian dari obat.

   - Apabila dalam peresepan aturan pakai akan selalu sama dari awal sampai akhir, maka cukup menuliskan 1 paket aturan pakai dengan nilai sequence=1.
   - Apabila terdapat perubahan aturan pakai dalam peresepan, contoh *tapering-down*, maka perlu dituliskan 2 paket aturan pakai dengan paket pertama nilai sequence=1, sedangkan paket aturan pakai kedua dengan nilai sequence=2
2. `MedicationRequest.dosageInstruction[i].timing.repeat`  
   `MedicationRequest.dosageInstruction[i].timing.repeat` berisi aturan kapan suatu obat harus dikonsumsi. Cara Pengisian dapat dilihat dalam Gambar 4.

Tabel 17. Tatacara pengisian MedicationRequest.dosageInstruction[i].timing.repeat

| description | duration | durationUnit | frequency | frequencyMax | period | periodUnit | periodMax | DayofWeek | TimeOfDay | when | offset | bounds[x] | count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Every 8 hours** |  |  | **1** |  | **8** | **h** |  |  |  |  |  |  |  |
| **Every 7 days** |  |  | **1** |  | **7** | **d** |  |  |  |  |  |  |  |
| **3 times a day** |  |  | **3** |  | **1** | **d** |  |  |  |  |  |  |  |
| **3-4 times a day** |  |  | **3** | **4** | **1** | **d** |  |  |  |  |  |  |  |
| **Every 4-6 hours** |  |  | **1** |  | **4** | **h** | **6** |  |  |  |  |  |  |
| **Every 21 days for 1 hours** | **1** | **hr** | **1** |  | **21** | **d** |  |  |  |  |  |  |  |
| **Three times a week for 1/2 hour** | **0.5** | **hr** | **3** |  | **1** | **wk** |  |  |  |  |  |  |  |
| **With breakfast** |  |  |  |  |  |  |  |  |  | **CM** |  |  |  |
| **For 5 minutes, 10 minutes before meals** | **5** | **min** |  |  |  |  |  |  |  | **AC** | **10** |  |  |
| **1 tablet 3 times daily, 30 minutes before meals** |  |  | **3** |  | **1** | **d** |  |  |  | **AC** | **30** |  |  |
| **BID, 30 mins before meal, for next 10 days** |  |  | **2** |  | **1** | **d** |  |  |  | **AC** | **30** | **Duration = 10 days** |  |
| **TID, for 14 days** |  |  | **3** |  | **1** | **d** |  |  |  |  |  | **Duration = 14 days** |  |
| **BID, start on 7/1/2015 at 1:00 PM** |  |  | **2** |  | **1** | **d** |  |  |  |  |  | **Period.start = 2015-07-01T13:00:00** |  |
| **Mon, Wed, Fri, Morning** |  |  | **1** |  | **1** | **d** |  | **mon l wed l fri** |  | **MORN** |  |  |  |
| **Every day at 10am** |  |  | **1** |  | **1** | **d** |  |  | **10:00** |  |  |  |  |
| **Take once, at any time** |  |  |  |  |  |  |  |  |  |  |  |  | **1** |
| **Take every second day, in the morning, until 20 have been taken** |  |  | **1** |  | **2** | **d** |  |  |  | **MORN** |  |  | **20** |

1. `MedicationRequest.dosageInstruction[i].timing.code`  
   `MedicationRequest.dosageInstruction[i].timing.code` berisi kode untuk aturan kapan suatu obat harus dikonsumsi. Apabila mengirimkan data menggunakan `MedicationRequest.dosageInstruction[i].timing.code`, elemen `MedicationRequest.dosageInstruction[i].timing.repeat` harus tetap diisi yang ekuivalen. Hubungan antara `MedicationRequest.dosageInstruction[i].timing.code` dengan `MedicationRequest.dosageInstruction[i].timing.repeat` dapat dilihat dalam Gambar 5.

Tabel 18. Hubungan antara MedicationRequest.dosageInstruction[i].timing.code dengan MedicationRequest.dosageInstruction[i].timing.repeat

| description | duration | durationUnit | frequency | frequencyMax | period | periodUnit | periodMax | when | bounds[x] |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **QOD** |  |  | **1** |  | **2** | **d** |  |  |  |
| **QD** |  |  | **1** |  | **1** | **d** |  |  |  |
| **BID** |  |  | **2** |  | **1** | **d** |  |  |  |
| **TID** |  |  | **3** |  | **1** | **d** |  |  |  |
| **QID** |  |  | **4** |  | **1** | **d** |  |  |  |
| **Q4H** |  |  | **1** |  | **4** | **h** |  |  |  |
| **Q6H** |  |  | **1** |  | **6** | **h** |  |  |  |
| **AM** |  |  | **1** |  | **1** | **d** |  | **MORN** |  |
| **PM** |  |  | **1** |  | **1** | **d** |  | **AFT or EVE** |  |

Berikut adalah daftar contoh variasi pengiriman data peresepan obat dapat dilihat pada *Postman Collection*:

1. Obat racikan salep d.t.d
2. Obat luar sekali pakai, dipakai malam hari
3. Obat racikan dengan peresepan d.t.d
4. Obat racikan non-d.t.d dimasukkan dalam kapsul
5. Obat racikan d.t.d dalam bentuk pulveres
6. Obat insulin short acting disuntik sebelum makan
7. Obat steroid dengan dosis tapering down
8. Obat single dose
9. Obat tetes mata
10. Obat tablet vagina
11. Obat suppositoria
12. Obat sirup diminum bila demam

## 17. Pengiriman Data Pengkajian Resep

Data Pengkajian Resep terdiri atas data pengkajian administrasi, farmasetik, dan persyaratan klinis. Data tersebut dapat dikirimkan menggunakan resource [`QuestionnaireResponse`](../../fhir/resources/questionnaire-response/#questionnaireresponse).

### Pemetaan Nilai QuestionnaireResponse

Berikut pemetaan nilai untuk `QuestionnaireResponse` yang direpresentasikan dalam peta referensi *(path)* ke properti *(element id)* terkait, untuk konteks pengiriman data pelayanan kehamilan pemeriksaan Ibu:

- [`QuestionnaireResponse.identifier`](../../fhir/resources/questionnaire-response/#questionnaireresponse-identifier)
- [`QuestionnaireResponse.basedOn[i]`](../../fhir/resources/questionnaire-response/#questionnaireresponse-basedon)
- [`QuestionnaireResponse.partOf[i]`](../../fhir/resources/questionnaire-response/#questionnaireresponse-partof)
- [`QuestionnaireResponse.questionnaire`](../../fhir/resources/questionnaire-response/#questionnaireresponse-questionnaire)
- [`*QuestionnaireResponse.status`](../../fhir/resources/questionnaire-response/#questionnaireresponse-status)
- [`*QuestionnaireResponse.subject`](../../fhir/resources/questionnaire-response/#questionnaireresponse-subject)
- [`*QuestionnaireResponse.encounter`](../../fhir/resources/questionnaire-response/#questionnaireresponse-encounter)
- [`QuestionnaireResponse.authored`](../../fhir/resources/questionnaire-response/#questionnaireresponse-authored)
- [`*QuestionnaireResponse.author`](../../fhir/resources/questionnaire-response/#questionnaireresponse-author)
- [`*QuestionnaireResponse.source`](../../fhir/resources/questionnaire-response/#questionnaireresponse-source)
- [`QuestionnaireResponse.item[i]`](../../fhir/resources/questionnaire-response/#questionnaireresponse-item)
- [`*QuestionnaireResponse.item.item`](../../fhir/resources/questionnaire-response/#questionnaireresponse-item-item)

### Pemetaan Variabel dan Terminologi Spesifik

Daftar variabel dan terminologi yang digunakan dalam pengiriman data Pengkajian Resep menggunakan *resources* `QuestionnaireResponse` yaitu:

Tabel 19. Pemetaan Variabel

| Pemetaan Variabel *Resource* `QuestionnaireResponse` | | |
| --- | --- | --- |
| **Elemen/*Path* FHIR** | **Terminologi/Format Pengisian** | |
| **Pengkajian Resep** | | |
| **1. Persyaratan Administrasi** | | |
| **a. Nama, umur, jenis kelamin, berat badan dan tinggi badan pasien** | | |
| **`QuestionnaireResponse.questionnaire`** | **<https://fhir.kemkes.go.id/Questionnaire/Q0007>** | |
| **`QuestionnaireResponse.item.item.linkId`** | **1** | |
| **`QuestionnaireResponse.item.item.text`** | **Apakah nama, umur, jenis kelamin, berat badan dan tinggi badan pasien sudah sesuai?** | |
| **`QuestionnaireResponse.item.item.answer.valueCoding.system`** | **<http://terminology.kemkes.go.id/CodeSystem/clinical-term>** | |
| **`QuestionnaireResponse.item.item.answer.valueCoding.code`** | **OV000052** | **OV000053** |
| **`QuestionnaireResponse.item.item.answer.valueCoding.display`** | **Sesuai** | **Tidak Sesuai** |
| **Pilihan Jawaban yang divisualisasikan** | **Sesuai** | **Tidak Sesuai** |
| **`QuestionnaireResponse.item.item.answer.valueString`** | ***(Tipe data String)*** | |
| **b. Nama, nomor ijin, alamat dan paraf dokter** | | |
| **`QuestionnaireResponse.questionnaire`** | **<https://fhir.kemkes.go.id/Questionnaire/Q0007>** | |
| **`QuestionnaireResponse.item.item.linkId`** | **2** | |
| **`QuestionnaireResponse.item.item.text`** | **Apakah nama, nomor ijin, alamat dan paraf dokter sudah sesuai?** | |
| **`QuestionnaireResponse.item.item.answer.valueCoding.system`** | **<http://terminology.kemkes.go.id/CodeSystem/clinical-term>** | |
| **`QuestionnaireResponse.item.item.answer.valueCoding.code`** | **OV000052** | **OV000053** |
| **`QuestionnaireResponse.item.item.answer.valueCoding.display`** | **Sesuai** | **Tidak Sesuai** |
| **Pilihan Jawaban yang divisualisasikan** | **Sesuai** | **Tidak Sesuai** |
| **`QuestionnaireResponse.item.item.answer.valueString`** | ***(Tipe data String)*** | |
| **c. Tanggal resep** | | |
| **`QuestionnaireResponse.questionnaire`** | **<https://fhir.kemkes.go.id/Questionnaire/Q0007>** | |
| **`QuestionnaireResponse.item.item.linkId`** | **3** | |
| **`QuestionnaireResponse.item.item.text`** | **Apakah tanggal resep sudah sesuai?** | |
| **`QuestionnaireResponse.item.item.answer.valueCoding.system`** | **<http://terminology.kemkes.go.id/CodeSystem/clinical-term>** | |
| **`QuestionnaireResponse.item.item.answer.valueCoding.code`** | **OV000052** | **OV000053** |
| **`QuestionnaireResponse.item.item.answer.valueCoding.display`** | **Sesuai** | **Tidak Sesuai** |
| **Pilihan Jawaban yang divisualisasikan** | **Sesuai** | **Tidak Sesuai** |
| **`QuestionnaireResponse.item.item.answer.valueString`** | ***(Tipe data String)*** | |
| **d. Ruangan/unit asal resep** | | |
| **`QuestionnaireResponse.questionnaire`** | **<https://fhir.kemkes.go.id/Questionnaire/Q0007>** | |
| **`QuestionnaireResponse.item.item.linkId`** | **4** | |
| **`QuestionnaireResponse.item.item.text`** | **Apakah ruangan/unit asal resep sudah sesuai?** | |
| **`QuestionnaireResponse.item.item.answer.valueCoding.system`** | **<http://terminology.kemkes.go.id/CodeSystem/clinical-term>** | |
| **`QuestionnaireResponse.item.item.answer.valueCoding.code`** | **OV000052** | **OV000053** |
| **`QuestionnaireResponse.item.item.answer.valueCoding.display`** | **Sesuai** | **Tidak Sesuai** |
| **Pilihan Jawaban yang divisualisasikan** | **Sesuai** | **Tidak Sesuai** |
| **`QuestionnaireResponse.item.item.answer.valueString`** | ***(Tipe data String)*** | |
| **2. Persyaratan Farmasetik** | | |
| **a. Nama obat, bentuk dan kekuatan sediaan** | | |
| **`QuestionnaireResponse.questionnaire`** | **<https://fhir.kemkes.go.id/Questionnaire/Q0007>** | |
| **`QuestionnaireResponse.item.item.linkId`** | **1** | |
| **`QuestionnaireResponse.item.item.text`** | **Apakah nama obat, bentuk dan kekuatan sediaan sudah sesuai?** | |
| **`QuestionnaireResponse.item.item.answer.valueCoding.system`** | **<http://terminology.kemkes.go.id/CodeSystem/clinical-term>** | |
| **`QuestionnaireResponse.item.item.answer.valueCoding.code`** | **OV000052** | **OV000053** |
| **`QuestionnaireResponse.item.item.answer.valueCoding.display`** | **Sesuai** | **Tidak Sesuai** |
| **Pilihan Jawaban yang divisualisasikan** | **Sesuai** | **Tidak Sesuai** |
| **`QuestionnaireResponse.item.item.answer.valueString`** | ***(Tipe data String)*** | |
| **b. Dosis dan jumlah obat** | | |
| **`QuestionnaireResponse.questionnaire`** | **<https://fhir.kemkes.go.id/Questionnaire/Q0007>** | |
| **`QuestionnaireResponse.item.item.linkId`** | **2** | |
| **`QuestionnaireResponse.item.item.text`** | **Apakah dosis dan jumlah obat sudah sesuai?** | |
| **`QuestionnaireResponse.item.item.answer.valueCoding.system`** | **<http://terminology.kemkes.go.id/CodeSystem/clinical-term>** | |
| **`QuestionnaireResponse.item.item.answer.valueCoding.code`** | **OV000052** | **OV000053** |
| **`QuestionnaireResponse.item.item.answer.valueCoding.display`** | **Sesuai** | **Tidak Sesuai** |
| **Pilihan Jawaban yang divisualisasikan** | **Sesuai** | **Tidak Sesuai** |
| **`QuestionnaireResponse.item.item.answer.valueString`** | ***(Tipe data String)*** | |
| **c. Stabilitas** | | |
| **`QuestionnaireResponse.questionnaire`** | **<https://fhir.kemkes.go.id/Questionnaire/Q0007>** | |
| **`QuestionnaireResponse.item.item.linkId`** | **3** | |
| **`QuestionnaireResponse.item.item.text`** | **Apakah stabilitas obat sudah sesuai?** | |
| **`QuestionnaireResponse.item.item.answer.valueCoding.system`** | **<http://terminology.kemkes.go.id/CodeSystem/clinical-term>** | |
| **`QuestionnaireResponse.item.item.answer.valueCoding.code`** | **OV000052** | **OV000053** |
| **`QuestionnaireResponse.item.item.answer.valueCoding.display`** | **Sesuai** | **Tidak Sesuai** |
| **Pilihan Jawaban yang divisualisasikan** | **Sesuai** | **Tidak Sesuai** |
| **`QuestionnaireResponse.item.item.answer.valueString`** | ***(Tipe data String)*** | |
| **d. Aturan dan cara penggunaan** | | |
| **`QuestionnaireResponse.questionnaire`** | **<https://fhir.kemkes.go.id/Questionnaire/Q0007>** | |
| **`QuestionnaireResponse.item.item.linkId`** | **4** | |
| **`QuestionnaireResponse.item.item.text`** | **Apakah aturan dan cara penggunaan obat sudah sesuai?** | |
| **`QuestionnaireResponse.item.item.answer.valueCoding.system`** | **<http://terminology.kemkes.go.id/CodeSystem/clinical-term>** | |
| **`QuestionnaireResponse.item.item.answer.valueCoding.code`** | **OV000052** | **OV000053** |
| **`QuestionnaireResponse.item.item.answer.valueCoding.display`** | **Sesuai** | **Tidak Sesuai** |
| **Pilihan Jawaban yang divisualisasikan** | **Sesuai** | **Tidak Sesuai** |
| **`QuestionnaireResponse.item.item.answer.valueString`** | ***(Tipe data String)*** | |
| **3. Persyaratan Klinis** | | |
| **a. Ketepatan indikasi, dosis, dan waktu penggunaan obat** | | |
| **`QuestionnaireResponse.questionnaire`** | **<https://fhir.kemkes.go.id/Questionnaire/Q0007>** | |
| **`QuestionnaireResponse.item.item.linkId`** | **1** | |
| **`QuestionnaireResponse.item.item.text`** | **Apakah ketepatan indikasi, dosis, dan waktu penggunaan obat sudah sesuai?** | |
| **`QuestionnaireResponse.item.item.answer.valueCoding.system`** | **<http://terminology.kemkes.go.id/CodeSystem/clinical-term>** | |
| **`QuestionnaireResponse.item.item.answer.valueCoding.code`** | **OV000052** | **OV000053** |
| **`QuestionnaireResponse.item.item.answer.valueCoding.display`** | **Sesuai** | **Tidak Sesuai** |
| **Pilihan Jawaban yang divisualisasikan** | **Sesuai** | **Tidak Sesuai** |
| **`QuestionnaireResponse.item.item.answer.valueString`** | ***(Tipe data String)*** | |
| **b. Duplikasi pengobatan** | | |
| **`QuestionnaireResponse.questionnaire`** | **<https://fhir.kemkes.go.id/Questionnaire/Q0007>** | |
| **`QuestionnaireResponse.item.item.linkId`** | **2** | |
| **`QuestionnaireResponse.item.item.text`** | **Apakah terdapat duplikasi pengobatan?** | |
| **`QuestionnaireResponse.item.item.answer.valueBoolean`** | ***(Tipe data Boolean)*** | |
| **Pilihan Jawaban yang divisualisasikan** | **Ya** | **Tidak** |
| **`QuestionnaireResponse.item.item.answer.valueString`** | ***(Tipe data String)*** | |
| **c. Alergi dan Reaksi Obat yang Tidak Dikehendaki (ROTD)** | | |
| **`QuestionnaireResponse.questionnaire`** | **<https://fhir.kemkes.go.id/Questionnaire/Q0007>** | |
| **`QuestionnaireResponse.item.item.linkId`** | **3** | |
| **`QuestionnaireResponse.item.item.text`** | **Apakah terdapat Alergi dan Reaksi Obat yang Tidak Dikehendaki (ROTD)?** | |
| **`QuestionnaireResponse.item.item.answer.valueBoolean`** | ***(Tipe data Boolean)*** | |
| **Pilihan Jawaban yang divisualisasikan** | **Ya** | **Tidak** |
| **`QuestionnaireResponse.item.item.answer.valueString`** | ***(Tipe data String)*** | |
| **d. Kontraindikasi** | | |
| **`QuestionnaireResponse.questionnaire`** | **<https://fhir.kemkes.go.id/Questionnaire/Q0007>** | |
| **`QuestionnaireResponse.item.item.linkId`** | **4** | |
| **`QuestionnaireResponse.item.item.text`** | **Apakah terdapat kontraindikasi pengobatan?** | |
| **`QuestionnaireResponse.item.item.answer.valueBoolean`** | ***(Tipe data Boolean)*** | |
| **Pilihan Jawaban yang divisualisasikan** | **Ya** | **Tidak** |
| **`QuestionnaireResponse.item.item.answer.valueString`** | ***(Tipe data String)*** | |
| **e. Interaksi obat** | | |
| **`QuestionnaireResponse.questionnaire`** | **<https://fhir.kemkes.go.id/Questionnaire/Q0007>** | |
| **`QuestionnaireResponse.item.item.linkId`** | **5** | |
| **`QuestionnaireResponse.item.item.text`** | **Apakah terdapat interaksi obat?** | |
| **`QuestionnaireResponse.item.item.answer.valueBoolean`** | ***(Tipe data Boolean)*** | |
| **Pilihan Jawaban yang divisualisasikan** | **Ya** | **Tidak** |
| **`QuestionnaireResponse.item.item.answer.valueString`** | ***(Tipe data String)*** | |
| **4. Resep yang dilakukan pengkajian resep** | | |
| **`QuestionnaireResponse.questionnaire`** | **<https://fhir.kemkes.go.id/Questionnaire/Q0007>** | |
| **`QuestionnaireResponse.item.text`** | **Resep yang dilakukan pengkajian resep** | |
| **`QuestionnaireResponse.item.linkId`** | **4** | |
| **`QuestionnaireResponse.item.answer.valueReference`** | **Referensi ke resource `MedicationRequest`** | |

## 18. Pengiriman Data Pengeluaran Obat

Pengiriman data pengeluaran/*dispense* obat akan menggunakan 2 *resources* yaitu `Medication` dan `MedicationDispense`. resource [`Medication`](../../fhir/resources/medication/#medication) akan mencatatkan data umum terkait obat yang akan di *dispense*. Sedangkan resource [`MedicationDispense`](../../fhir/resources/medication-dispense/#medicationdispense) akan digunakan untuk mengirimkan data terkait proses *dispense* obat, seperti jumlah yang di *dispense*, instruksi minum obat dan lain-lain. Kedua data ini dikirimkan secara bersamaan sebagai 1 paket yaitu `Medication` dan `MedicationDispense`. Satu *payload* `Medication` dan `MedicationDispense` hanya digunakan untuk *dispense*/pengeluaran 1 jenis obat saja. Apabila terdapat 2 jenis obat yang dikeluarkan, maka dikirimkan 2 paket `Medication` dan `MedicationDispense`.

![Skema Pengeluaran 1 Obat](../_images/skema-pengeluaran1.png)

Gambar 13. Skema Pengeluaran 1 Obat

![Skema Pengeluaran 2 Obat](../_images/skema-pengeluaran2.png)

Gambar 14. Skema Pengeluaran 2 Obat

Pengiriman data dapat dilakukan dengan 2 cara yaitu:

1. Mengirimkan *payload* `Medication` dan `MedicationDispense` secara terpisah (2 kali POST)
2. Mengirimkan *payload* `MedicationDispense` yang mengandung resource `Medication` dalam `MedicationDispense.contained` (1 kali POST)

Contoh pengiriman data atau *payload* untuk pengiriman data pengeluaran obat dapat dilihat dalam Postman Collection.

Penjelasan ketentuan spesifik pengiriman data pada resource `Medication` dapat dilihat dalam bab Peresepan Obat.

### Pemetaan Nilai MedicationDispense

|  |  |
| --- | --- |
|  | 1. Setiap terdapat simbol asterik `*` sebelum nama variabel/parameter/element FHIR yang disebutkan, maka variabel/parameter/element FHIR tersebut bersifat **WAJIB**, **harus ada**, atau **pasti selalu ada**, contoh: **`*Location.identifier`**. 2. **Standar format Waktu** yang digunakan dalam pengiriman data adalah **UTC +00**. Misalnya waktu **WIB**, maka format yang digunakan adalah **waktu sekarang dikurangi 7**, jika **WITA**, maka **waktu sekarang dikurangi 8**, dan Jika **WIT**, maka **waktu sekarang dikurangi 9**.  **Contoh:** Pukul 17.35 WIB tanggal 23 Agustus 2023 maka yang dikirimkan adalah waktunya perlu diubah ke UTC +00 menjadi 10.35, berarti menjadi `2023-08-23T10:35:00+00:00`. 3. **Standar format pengiriman Tanggal** tidak bisa kurang dari 03 Juni 2014. |

|  |  |
| --- | --- |
|  | Silakan klik setiap teks variabel/parameter/element FHIR pada daftar pemetaan nilai di bawah ini (berwarna **merah**), untuk membaca panduan lebih detail/lanjut ke bagian yang direferensikan. |

Berikut pemetaan nilai untuk `MedicationDispense` yang direpresentasikan dalam peta referensi *(path)* ke properti *(element id)* terkait, untuk konteks data pengeluaran obat:

- [`*MedicationDispense.identifier[i]`](../../fhir/resources/medication-dispense/#medicationdispense-identifier)
- [`MedicationDispense.partOf[i]`](../../fhir/resources/medication-dispense/#medicationdispense-partof)
- [`*MedicationDispense.status`](../../fhir/resources/medication-dispense/#medicationdispense-status)
- [`MedicationDispense.category`](../../fhir/resources/medication-dispense/#medicationdispense-category)
- [`*MedicationDispense.medicationReference`](../../fhir/resources/medication-dispense/#medicationdispense-medicationreference)
- [`*MedicationDispense.subject`](../../fhir/resources/medication-dispense/#medicationdispense-subject)
- [`*MedicationDispense.context`](../../fhir/resources/medication-dispense/#medicationdispense-context)
- [`MedicationDispense.performer[i]`](../../fhir/resources/medication-dispense/#medicationdispense-performer)
- [`MedicationDispense.performer[i].function`](../../fhir/resources/medication-dispense/#medicationdispense-performer-function)
- [`MedicationDispense.location`](../../fhir/resources/medication-dispense/#medicationdispense-location)
- [`MedicationDispense.authorizingPrescription[i]`](../../fhir/resources/medication-dispense/#medicationdispense-authorizingprescription)
- [`MedicationDispense.quantity`](../../fhir/resources/medication-dispense/#medicationdispense-quantity)
- [`MedicationDispense.daysSupply`](../../fhir/resources/medication-dispense/#medicationdispense-dayssupply)
- [`MedicationDispense.whenPrepared`](../../fhir/resources/medication-dispense/#medicationdispense-whenprepared)
- [`MedicationDispense.whenHandedOver`](../../fhir/resources/medication-dispense/#medicationdispense-whenhandedover)
- [`MedicationDispense.dosageInstruction[i].sequence`](../../fhir/resources/medication-dispense/#medicationdispense-dosageinstruction-sequence)
- [`MedicationDispense.dosageInstruction[i].text`](../../fhir/resources/medication-dispense/#medicationdispense-dosageinstruction-text)
- [`MedicationDispense.dosageInstruction[i].additionalInstruction`](../../fhir/resources/medication-dispense/#medicationdispense-dosageinstruction-additionalinstruction)
- [`MedicationDispense.dosageInstrution[i].patientInstruction`](../../fhir/resources/medication-dispense/#medicationdispense-dosageinstrution-patientinstruction)
- [`MedicationDispense.dosageInstruction[i].timing`](../../fhir/resources/medication-dispense/#medicationdispense-dosageinstruction-timing)
- [`MedicationDispense.dosageInstruction[i].timing.event`](../../fhir/resources/medication-dispense/#medicationdispense-dosageinstruction-timing-event)
- [`MedicationDispense.dosageInstruction[i].timing.repeat`](../../fhir/resources/medication-dispense/#medicationdispense-dosageinstruction-timing-repeat)
- [`MedicationDispense.dosageInstruction[i].timing.code`](../../fhir/resources/medication-dispense/#medicationdispense-dosageinstruction-timing-code)
- [`MedicationDispense.dosageInstruction[i].site`](../../fhir/resources/medication-dispense/#medicationdispense-dosageinstruction-site)
- [`MedicationDispense.dosageInstruction[i].route`](../../fhir/resources/medication-dispense/#medicationdispense-dosageinstruction-route)
- [`MedicationDispense.dosageInstruction[i].method`](../../fhir/resources/medication-dispense/#medicationdispense-dosageinstruction-method)
- [`MedicationDispense.dosageInstruction[i].doseAndRate.type`](../../fhir/resources/medication-dispense/#medicationdispense-dosageinstruction-doseandrate-type)
- [`MedicationDispense.dosageInstruction[i].doseAndRate.dose<?>`](../../fhir/resources/medication-dispense/#medicationdispense-dosageinstruction-doseandrate-dose)
- [`MedicationDispense.dosageInstruction[i].doseAndRate.doseRange`](../../fhir/resources/medication-dispense/#medicationdispense-dosageinstruction-doseandrate-doserange)
- [`MedicationDispense.dosageInstruction[i].doseAndRate.doseQuantity`](../../fhir/resources/medication-dispense/#medicationdispense-dosageinstruction-doseandrate-dosequantity)
- [`MedicationDispense.dosageInstruction[i].doseAndRate.rate<?>`](../../fhir/resources/medication-dispense/#medicationdispense-dosageinstruction-doseandrate-rate)
- [`MedicationDispense.dosageInstruction[i].doseAndRate.rateRatio`](../../fhir/resources/medication-dispense/#medicationdispense-dosageinstruction-doseandrate-rateratio)
- [`MedicationDispense.dosageInstruction[i].doseAndRate.rateRange`](../../fhir/resources/medication-dispense/#medicationdispense-dosageinstruction-doseandrate-raterange)
- [`MedicationDispense.dosageInstruction[i].doseAndRate.rateQuantity`](../../fhir/resources/medication-dispense/#medicationdispense-dosageinstruction-doseandrate-ratequantity)
- [`MedicationDispense.dosageInstruction[i].maxDosePerPeriod`](../../fhir/resources/medication-dispense/#medicationdispense-dosageinstruction-maxdoseperperiod)
- [`MedicationDispense.dosageInstruction[i].maxDosePerAdministration`](../../fhir/resources/medication-dispense/#medicationdispense-dosageinstruction-maxdoseperadministration)
- [`MedicationDispense.dosageInstruction[i].maxDosePerLifeTime`](../../fhir/resources/medication-dispense/#medicationdispense-dosageinstruction-maxdoseperlifetime)
- [`MedicationDispense.substitution.wasSubstituted`](../../fhir/resources/medication-dispense/#medicationdispense-substitution-wassubstituted)
- [`MedicationDispense.substitution.type`](../../fhir/resources/medication-dispense/#medicationdispense-substitution-type)
- [`MedicationDispense.substitution.reason`](../../fhir/resources/medication-dispense/#medicationdispense-substitution-reason)
- [`MedicationDispense.substitution.responsibleParty`](../../fhir/resources/medication-dispense/#medicationdispense-substitution-responsibleparty)

### Pemetaan Variabel dan Terminologi Spesifik

Terminologi spesifik yang digunakan dalam pengiriman data pengeluaran obat melalui resource `MedicationDispense` dapat dilihat dalam tabel berikut:

Tabel 20. Pemetaan Variabel

| Pemetaan Variabel *Resource* `Procedure`, `Immunization`, dan `QuestionnaireResponse` | |
| --- | --- |
| **Elemen/*Path* FHIR** | **Terminologi/Format Pengisian** |
| **Pengeluaran Obat** | |
| **1. ID Resep** | |
| **`MedicationDispense.identifier`** | **Diisi dengan ID resep dari obat yang dikeluarkan**  **Lihat di subbab 16.3.2 Ketentuan Pengisian resource `MedicationRequest` poin A. `MedicationRequest.identifier`** |
| **2. Detail Obat** | |
| **`MedicationDispense.medicationReference`** | **Referensi ke resource `Medication`** |
| **a. ID Obat dan Nama Obat** | |
| **`Medication.code.coding.system`** | **<http://sys-ids.kemkes.go.id/kfa>** |
| **`Medication.code.coding.code`** | **ID Obat dengan Kode Obat KFA**  **Lihat di subbab 16.3.1 Ketentuan Pengisian resource `Medication` poin A.b. `Medication.code` untuk `MedicationDispense`** |
| **`Medication.code.coding.display`** | **Nama Obat dengan Deskripsi Obat KFA** |
| **b. Bentuk/Sediaan** | |
| **`Medication.form.coding.system`** | **<http://terminology.kemkes.go.id/CodeSystem/medication-form>** |
| **`Medication.form.coding.code`** | **Kode bentuk/sediaan obat**  **(Untuk Kode Lengkapnya dapat dilihat pada Dokumen Lampiran [Standar Terminologi](../../terminology/standar-terminologi/#standar-terminologi) SATUSEHAT)** |
| **`Medication.form.coding.display`** | **Deskripsi bentuk/sediaan obat** |
| **c. Nomor Batch** | |
| **`Medication.batch.lotNumber`** | **(Tipe data *string*)** |
| **d. Tanggal Kedaluwarsa** | |
| **`Medication.batch.expirationDate`** | **(Tipe data *dateTime*)** |
| **3. Jumlah Obat** | |
| **`MedicationDispense.quantity.value`** | **(Tipe data *decimal*)** |
| **`MedicationDispense.quantity.unit`** | **UCUM unit**  **Kode satuan atau unit dapat menggunakan kode yang disediakan oleh *Unified Code for Units of Measure* (UCUM). Daftar kode satuan dapat diakses melalui link berikut : [Observation.valueQuantity](https://docs.google.com/spreadsheets/d/1OHM4ICgQ3hseGLrqi9GQzcREddU5SDKto50dhkhOjnc/edit?gid=0#gid=0) (UCUM)**  **(Untuk Kode Lengkapnya dapat dilihat pada Dokumen Lampiran [Standar Terminologi](../../terminology/standar-terminologi/#standar-terminologi) SATUSEHAT)** |
| **`MedicationDispense.quantity.system`** | **<http://unitsofmeasure.org>** |
| **`MedicationDispense.quantity.code`** | **UCUM Code** |
| **4. Metode/Rute Pemberian** | |
| **`MedicationDispense.dosageInstruction.route.coding.system`** | **<http://www.whocc.no/atc>** |
| **`MedicationDispense.dosageInstruction.route.coding.code`** | **Kode Rute Pemberian Obat WHO ATC**  **(Untuk Kode Lengkapnya dapat dilihat pada Dokumen Lampiran [Standar Terminologi](../../terminology/standar-terminologi/#standar-terminologi) SATUSEHAT)** |
| **`MedicationDispense.dosageInstruction.route.coding.display`** | **Deskripsi Rute Pemberian Obat WHO ATC** |
| **5. Dosis Obat yang Diberikan** | |
| **`MedicationDispense.dosageInstruction.doseAndRate.doseQuantity.value`** | **(Tipe data *decimal*)** |
| **6. Unit** | |
| **`MedicationDispense.dosageInstruction.doseAndRate.doseQuantity.unit`** | **UCUM unit**  **Kode satuan atau unit dapat menggunakan kode yang disediakan oleh *Unified Code for Units of Measure* (UCUM). Daftar kode satuan dapat diakses melalui link berikut : [Observation.valueQuantity](https://docs.google.com/spreadsheets/d/1OHM4ICgQ3hseGLrqi9GQzcREddU5SDKto50dhkhOjnc/edit?gid=0#gid=0) (UCUM)**  **(Untuk Kode Lengkapnya dapat dilihat pada Dokumen Lampiran [Standar Terminologi](../../terminology/standar-terminologi/#standar-terminologi) SATUSEHAT)** |
| **7. Frekuensi/Interval** | |
| **`MedicationDispense.dosageInstruction.timing`** | **Lihat di subbab 18.2.1 Ketentuan Pengisian** |
| **8. Aturan Tambahan** | |
| **`MedicationDispense.dosageInstruction.additionalInstruction.coding.system`** | **<http://snomed.info/sct>** |
| **`MedicationDispense.dosageInstruction.additionalInstruction.coding.code`** | **SNOMED-CT Code**  **Ruang lingkup kode SNOMED CT yang dapat dipakai: Expression Constraint Language (ECL) Query : < 419492006 |Additional dosage instructions (qualifier value)|**  **(Untuk Kode Lengkapnya dapat dilihat pada Dokumen Lampiran [Standar Terminologi](../../terminology/standar-terminologi/#standar-terminologi) SATUSEHAT)** |
| **`MedicationDispense.dosageInstruction.additionalInstruction.coding.display`** | **SNOMED-CT Description** |
| **`MedicationDispense.dosageInstruction.additionalInstruction.text`** | **(Tipe data *string*)** |
| **9. Dokter yang Mengeluarkan Obat** | |
| **`MedicationDispense.performer.actor`** | **Referensi ke resource `Practitioner`** |
| **10. Tanggal dan Jam Penyiapan Obat** | |
| **`MedicationDispense.whenPrepared`** | **(Tipe data *dateTime*)** |
| **11. Tanggal dan Jam Pengeluaran Obat** | |
| **`MedicationDispense.whenHandedOver`** | **(Tipe data *dateTime*)** |
| **12. Status Pengeluaran Obat** | |
| **`MedicationDispense.status`** | **Kode status pengeluaran obat**  **Kode dapat diisi dengan kode FHIR Terminology.**  **(Untuk Kode Lengkapnya dapat dilihat pada Dokumen Lampiran [Standar Terminologi](../../terminology/standar-terminologi/#standar-terminologi) SATUSEHAT)** |
| **13. Resep yang Diacu** | |
| **`MedicationDispense.authorizingPrescription`** | **Referensi ke resource `MedicationRequest`** |

#### Ketentuan Pengisian

Ketentuan pengisian secara spesifik untuk pengisian resource `MedicationDispense` adalah sebagai berikut:

1. `MedicationDispense.dosageInstruction[i].sequence`  
   `MedicationRequest.dosageInstruction[i].sequence` menjelaskan urutan aturan pemakaian dari obat.

   - Apabila dalam peresepan aturan pakai akan selalu sama dari awal sampai akhir, maka cukup menuliskan 1 paket aturan pakai dengan nilai sequence=1.
   - Apabila terdapat perubahan aturan pakai dalam peresepan, contoh *tapering-down*, maka perlu dituliskan 2 paket aturan pakai dengan paket pertama nilai sequence=1, sedangkan paket aturan pakai kedua dengan nilan sequence=2
2. `MedicationDispense.dosageInstruction[i].timing.repeat`  
   `MedicationDispense.dosageInstruction[i].timing.repeat` berisi aturan kapan suatu obat harus dikonsumsi. Cara Pengisian dapat dilihat dalam Gambar 6.

Tabel 21. Tatacara pengisian MedicationDispense.dosageInstruction[i].timing.repeat

| description | duration | durationUnit | frequency | frequencyMax | period | periodUnit | periodMax | DayofWeek | TimeOfDay | when | offset | bounds[x] | count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Every 8 hours** |  |  | **1** |  | **8** | **h** |  |  |  |  |  |  |  |
| **Every 7 days** |  |  | **1** |  | **7** | **d** |  |  |  |  |  |  |  |
| **3 times a day** |  |  | **3** |  | **1** | **d** |  |  |  |  |  |  |  |
| **3-4 times a day** |  |  | **3** | **4** | **1** | **d** |  |  |  |  |  |  |  |
| **Every 4-6 hours** |  |  | **1** |  | **4** | **h** | **6** |  |  |  |  |  |  |
| **Every 21 days for 1 hours** | **1** | **hr** | **1** |  | **21** | **d** |  |  |  |  |  |  |  |
| **Three times a week for 1/2 hour** | **0.5** | **hr** | **3** |  | **1** | **wk** |  |  |  |  |  |  |  |
| **With breakfast** |  |  |  |  |  |  |  |  |  | **CM** |  |  |  |
| **For 5 minutes, 10 minutes before meals** | **5** | **min** |  |  |  |  |  |  |  | **AC** | **10** |  |  |
| **1 tablet 3 times daily, 30 minutes before meals** |  |  | **3** |  | **1** | **d** |  |  |  | **AC** | **30** |  |  |
| **BID, 30 mins before meal, for next 10 days** |  |  | **2** |  | **1** | **d** |  |  |  | **AC** | **30** | **Duration = 10 days** |  |
| **TID, for 14 days** |  |  | **3** |  | **1** | **d** |  |  |  |  |  | **Duration = 14 days** |  |
| **BID, start on 7/1/2015 at 1:00 PM** |  |  | **2** |  | **1** | **d** |  |  |  |  |  | **Period.start = 2015-07-01T13:00:00** |  |
| **Mon, Wed, Fri, Morning** |  |  | **1** |  | **1** | **d** |  | **mon l wed l fri** |  | **MORN** |  |  |  |
| **Every day at 10am** |  |  | **1** |  | **1** | **d** |  |  | **10:00** |  |  |  |  |
| **Take once, at any time** |  |  |  |  |  |  |  |  |  |  |  |  | **1** |
| **Take every second day, in the morning, until 20 have been taken** |  |  | **1** |  | **2** | **d** |  |  |  | **MORN** |  |  | **20** |

1. `MedicationDispense.dosageInstruction[i].timing.code`  
   `MedicationDispense.dosageInstruction[i].timing.code` berisi kode untuk aturan kapan suatu obat harus dikonsumsi. Apabila mengirimkan data menggunakan `MedicationDispense.dosageInstruction[i].timing.code`, elemen `MedicationDispense.dosageInstruction[i].timing.repeat` harus tetap diisi yang ekuivalen. Hubungan antara `MedicationDispense.dosageInstruction[i].timing.code` dengan `MedicationDispense.dosageInstruction[i].timing.repeat` dapat dilihat dalam Gambar 7.

Tabel 22. Hubungan antara MedicationRequest.dosageInstruction[i].timing.code dengan MedicationRequest.dosageInstruction[i].timing.repeat

| description | duration | durationUnit | frequency | frequencyMax | period | periodUnit | periodMax | when | bounds[x] |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **QOD** |  |  | **1** |  | **2** | **d** |  |  |  |
| **QD** |  |  | **1** |  | **1** | **d** |  |  |  |
| **BID** |  |  | **2** |  | **1** | **d** |  |  |  |
| **TID** |  |  | **3** |  | **1** | **d** |  |  |  |
| **QID** |  |  | **4** |  | **1** | **d** |  |  |  |
| **Q4H** |  |  | **1** |  | **4** | **h** |  |  |  |
| **Q6H** |  |  | **1** |  | **6** | **h** |  |  |  |
| **AM** |  |  | **1** |  | **1** | **d** |  | **MORN** |  |
| **PM** |  |  | **1** |  | **1** | **d** |  | **AFT or EVE** |  |

Penjelasan tipe mandatoris, deskripsi dan format pengisian dari setiap elemen data/*path* di dalam resource `Medication` dan `MedicationDispense`, dan contoh pengiriman data atau *payload* dari data pengeluaran obat dapat dilihat dalam [Postman SATUSEHAT](../../postman-workshop/#postman-collection-satusehat) SATUSEHAT.

## 19. Pengiriman Data Pemberian Obat

Pengiriman data pemberian obat akan menggunakan 2 resource yaitu `Medication` dan `MedicationAdministration`. *Resource* `Medication` akan mencatatkan data umum terkait obat yang akan diberikan. Sedangkan resource `MedicationAdministration` akan digunakan untuk mengirimkan data terkait proses pemberian obat, seperti jumlah obat yang diberikan. Kedua data ini dikirimkan secara bersamaan sebagai 1 paket yaitu `Medication` dan `MedicationAdministration`. Satu *payload* `Medication` dan `MedicationAdministration` hanya digunakan untuk *dispense*/pengeluaran 1 jenis obat saja. Apabila terdapat 2 jenis obat yang dikeluarkan, maka dikirimkan 2 paket `Medication` dan `MedicationAdministration`. Penjelasan ketentuan spesifik pengiriman data pada resource `Medication` dapat dilihat dalam bab Peresepan Obat.

### Pemetaan Nilai MedicationAdministration

Berikut pemetaan nilai untuk `MedicationAdministration` yang direpresentasikan dalam peta referensi (path) ke properti (element id) terkait:

|  |  |
| --- | --- |
|  | 1. Setiap terdapat simbol asterik `*` sebelum nama variabel/parameter/element FHIR yang disebutkan, maka variabel/parameter/element FHIR tersebut bersifat **WAJIB**, **harus ada**, atau **pasti selalu ada**, contoh: **`*Location.identifier`**. 2. **Standar format Waktu** yang digunakan dalam pengiriman data adalah **UTC +00**. Misalnya waktu **WIB**, maka format yang digunakan adalah **waktu sekarang dikurangi 7**, jika **WITA**, maka **waktu sekarang dikurangi 8**, dan Jika **WIT**, maka **waktu sekarang dikurangi 9**.  **Contoh:** Pukul 17.35 WIB tanggal 23 Agustus 2023 maka yang dikirimkan adalah waktunya perlu diubah ke UTC +00 menjadi 10.35, berarti menjadi `2023-08-23T10:35:00+00:00`. 3. **Standar format pengiriman Tanggal** tidak bisa kurang dari 03 Juni 2014. |

|  |  |
| --- | --- |
|  | Silakan klik setiap teks variabel/parameter/element FHIR pada daftar pemetaan nilai di bawah ini (berwarna **merah**), untuk membaca panduan lebih detail/lanjut ke bagian yang direferensikan. |

- [`MedicationAdministration.identifier`](../../fhir/resources/medication-administration/#medicationadministration-identifier)
- [`MedicationAdministration.instantiates`](../../fhir/resources/medication-administration/#medicationadministration-instantiates)
- [`MedicationAdministration.partOf`](../../fhir/resources/medication-administration/#medicationadministration-partof)
- [`*MedicationAdministration.status`](../../fhir/resources/medication-administration/#medicationadministration-status)
- [`MedicationAdministration.statusReason`](../../fhir/resources/medication-administration/#medicationadministration-statusreason)
- [`MedicationAdministration.category`](../../fhir/resources/medication-administration/#medicationadministration-category)
- [`MedicationAdministration.medicationCodeableConcept`](../../fhir/resources/medication-administration/#medicationadministration-medicationcodeableconcept)
- [`MedicationAdministration.medicationReference`](../../fhir/resources/medication-administration/#medicationadministration-medicationreference)
- [`MedicationAdministration.subject`](../../fhir/resources/medication-administration/#medicationadministration-subject)
- [`MedicationAdministration.context`](../../fhir/resources/medication-administration/#medicationadministration-context)
- [`MedicationAdministration.supportingInformation`](../../fhir/resources/medication-administration/#medicationadministration-supportinginformation)
- [`MedicationAdministration.effectiveDateTime`](../../fhir/resources/medication-administration/#medicationadministration-effectivedatetime)
- [`MedicationAdministration.effectivePeriod`](../../fhir/resources/medication-administration/#medicationadministration-effectiveperiod)
- [`MedicationAdministration.performer`](../../fhir/resources/medication-administration/#medicationadministration-performer)
- [`MedicationAdministration.performer.function`](../../fhir/resources/medication-administration/#medicationadministration-performer-function)
- [`MedicationAdministration.performer.actor`](../../fhir/resources/medication-administration/#medicationadministration-performer-actor)
- [`MedicationAdministration.reasonCode`](../../fhir/resources/medication-administration/#medicationadministration-reasoncode)
- [`MedicationAdministration.reasonReference`](../../fhir/resources/medication-administration/#medicationadministration-reasonreference)
- [`MedicationAdministration.request`](../../fhir/resources/medication-administration/#medicationadministration-request)
- [`MedicationAdministration.device`](../../fhir/resources/medication-administration/#medicationadministration-device)
- [`MedicationAdministration.note`](../../fhir/resources/medication-administration/#medicationadministration-note)
- [`MedicationAdministration.dosage`](../../fhir/resources/medication-administration/#medicationadministration-dosage)
- [`MedicationAdministration.dosage.text`](../../fhir/resources/medication-administration/#medicationadministration-dosage-text)
- [`MedicationAdministration.dosage.site`](../../fhir/resources/medication-administration/#medicationadministration-dosage-site)
- [`MedicationAdministration.dosage.route`](../../fhir/resources/medication-administration/#medicationadministration-dosage-route)
- [`MedicationAdministration.dosage.method`](../../fhir/resources/medication-administration/#medicationadministration-dosage-method)
- [`MedicationAdministration.dosage.dose`](../../fhir/resources/medication-administration/#medicationadministration-dosage-dose)
- [`MedicationAdministration.dosage.rateRatio`](../../fhir/resources/medication-administration/#medicationadministration-dosage-rateratio)
- [`MedicationAdministration.dosage.rateQuantity`](../../fhir/resources/medication-administration/#medicationadministration-dosage-ratequantity)
- [`MedicationAdministration.eventHistory`](../../fhir/resources/medication-administration/#medicationadministration-eventhistory)

### Pemetaan Variabel dan Terminologi Spesifik

Terminologi spesifik yang digunakan dalam pengiriman data pemberian obat melalui resource `MedicationAdministration` dapat dilihat dalam tabel berikut:

Tabel 23. Terminologi Spesifik

| *Resource* `Composition` | |
| --- | --- |
| **Elemen/*Path* FHIR** | **Terminologi/Format Pengisian** |
| **Pemberian Obat** | |
| **1. Nama Obat** | |
| **`Medication.code.coding.system`** | **<http://sys-ids.kemkes.go.id/kfa>** |
| **`Medication.code.coding.code`** | **Kode Obat KFA**  **Lihat di subbab 16.3.1 Ketentuan Pengisian resource `Medication`** |
| **`Medication.code.coding.display`** | **Deskripsi Obat KFA** |
| **`MedicationAdministration.medicationReference`** | **Referensi ke resource `Medication`** |
| **2. Bentuk/Sediaan** | |
| **`Medication.form.coding.system`** | **<http://terminology.kemkes.go.id/CodeSystem/medication-form>** |
| **`Medication.form.coding.code`** | **Kode bentuk/sediaan obat**  **(Untuk Kode Lengkapnya dapat dilihat pada Dokumen Lampiran [Standar Terminologi](../../terminology/standar-terminologi/#standar-terminologi) SATUSEHAT)** |
| **`Medication.form.coding.display`** | **Deskripsi bentuk/sediaan obat** |
| **`MedicationAdministration.medicationReference`** | **Referensi ke resource `Medication`** |
| **3. Metode/Rute Pemberian** | |
| **`MedicationAdministration.dosage.route.coding.system`** | **<http://www.whocc.no/atc>** |
| **`MedicationAdministration.dosage.route.coding.code`** | **Kode Rute Pemberian Obat WHO ATC**  **(Untuk Kode Lengkapnya dapat dilihat pada Dokumen Lampiran [Standar Terminologi](../../terminology/standar-terminologi/#standar-terminologi) SATUSEHAT)** |
| **`MedicationAdministration.dosage.route.coding.display`** | **Deskripsi Rute Pemberian Obat WHO ATC** |
| **4. Dosis Obat yang Diberikan** | |
| **`MedicationAdministration.dosage.dose.value`** | **(Tipe data *decimal*)** |
| **5. Unit** | |
| **`MedicationAdministration.dosage.dose.unit`** | **UCUM unit**  **Kode satuan atau unit dapat menggunakan kode yang disediakan oleh *Unified Code for Units of Measure* (UCUM). Daftar kode satuan dapat diakses melalui link berikut : [Observation.valueQuantity](https://docs.google.com/spreadsheets/d/1OHM4ICgQ3hseGLrqi9GQzcREddU5SDKto50dhkhOjnc/edit?gid=0#gid=0) (UCUM)**  **(Untuk Kode Lengkapnya dapat dilihat pada Dokumen Lampiran [Standar Terminologi](../../terminology/standar-terminologi/#standar-terminologi) SATUSEHAT)** |
| **6. Dokter Pemberi Obat** | |
| **`MedicationAdministration.performer.actor`** | **Referensi ke resource `Practitioner`** |
| **7. Tanggal Pemberian Obat** | |
| **`MedicationAdministration.effecticePeriod`** | **(Tipe data *dateTime*)** |
| **8. Jam Pemberian Obat** | |
| **`MedicationAdministration.effecticePeriod`** | **(Tipe data *dateTime*)** |
| **9. Status Pemberian Obat** | |
| **`MedicationAdministration.status`** | **Kode status pemberian obat**  **Kode dapat diisi dengan kode FHIR Terminology.**  **(Untuk Kode Lengkapnya dapat dilihat pada Dokumen Lampiran [Standar Terminologi](../../terminology/standar-terminologi/#standar-terminologi) SATUSEHAT)** |

## 20. Pengiriman Data Diet

Rekomendasi diet dapat diberikan oleh dokter kepada dietisien untuk dilaksanakan di fasyankes atau kepada pasien untuk dilakukan secara mandiri di rumah. Rekomendasi diet dikirimkan melalui resource `NutritionOrder`. Ketentuan lengkap mengenai pengiriman data Diet dapat dilihat pada *use case* Gizi.

### Pemetaan Nilai NutritionOrder

Berikut pemetaan nilai untuk `NutritionOrder` yang direpresentasikan dalam peta referensi (*path*) ke properti (*element id*) terkait:

|  |  |
| --- | --- |
|  | 1. Setiap terdapat simbol asterik `*` sebelum nama variabel/parameter/element FHIR yang disebutkan, maka variabel/parameter/element FHIR tersebut bersifat **WAJIB**, **harus ada**, atau **pasti selalu ada**, contoh: **`*Location.identifier`**. 2. **Standar format Waktu** yang digunakan dalam pengiriman data adalah **UTC +00**. Misalnya waktu **WIB**, maka format yang digunakan adalah **waktu sekarang dikurangi 7**, jika **WITA**, maka **waktu sekarang dikurangi 8**, dan Jika **WIT**, maka **waktu sekarang dikurangi 9**.  **Contoh:** Pukul 17.35 WIB tanggal 23 Agustus 2023 maka yang dikirimkan adalah waktunya perlu diubah ke UTC +00 menjadi 10.35, berarti menjadi `2023-08-23T10:35:00+00:00`. 3. **Standar format pengiriman Tanggal** tidak bisa kurang dari 03 Juni 2014. |

|  |  |
| --- | --- |
|  | Silakan klik setiap teks variabel/parameter/element FHIR pada daftar pemetaan nilai di bawah ini (berwarna **merah**), untuk membaca panduan lebih detail/lanjut ke bagian yang direferensikan. |

- [`NutritionOrder.identifier`](../../fhir/resources/nutrition-order/#nutritionorder-identifier)
- [`NutritionOrder.instantiatesCanonical`](../../fhir/resources/nutrition-order/#nutritionorder-identifier)
- [`NutritionOrder.instantiatesUri`](../../fhir/resources/nutrition-order/#nutritionorder-identifier)
- [`NutritionOrder.instantiates`](../../fhir/resources/nutrition-order/#nutritionorder-identifier)
- [`*NutritionOrder.status`](../../fhir/resources/nutrition-order/#nutritionorder-identifier)
- [`*NutritionOrder.intent`](../../fhir/resources/nutrition-order/#nutritionorder-identifier)
- [`*NutritionOrder.patient`](../../fhir/resources/nutrition-order/#nutritionorder-identifier)
- [`*NutritionOrder.encounter`](../../fhir/resources/nutrition-order/#nutritionorder-identifier)
- [`*NutritionOrder.dateTime`](../../fhir/resources/nutrition-order/#nutritionorder-identifier)
- [`NutritionOrder.orderer`](../../fhir/resources/nutrition-order/#nutritionorder-identifier)
- [`NutritionOrder.allergyIntolerance`](../../fhir/resources/nutrition-order/#nutritionorder-identifier)
- [`NutritionOrder.foodPreferenceModifier`](../../fhir/resources/nutrition-order/#nutritionorder-identifier)
- [`NutritionOrder.excludeFoodModifier`](../../fhir/resources/nutrition-order/#nutritionorder-identifier)
- [`NutritionOrder.oralDiet`](../../fhir/resources/nutrition-order/#nutritionorder-identifier)
- [`NutritionOrder.oralDiet.type`](../../fhir/resources/nutrition-order/#nutritionorder-identifier)
- [`NutritionOrder.oralDiet.schedule`](../../fhir/resources/nutrition-order/#nutritionorder-identifier)
- [`NutritionOrder.oralDiet.nutrient`](../../fhir/resources/nutrition-order/#nutritionorder-identifier)
- [`NutritionOrder.oralDiet.nutrient.modifier`](../../fhir/resources/nutrition-order/#nutritionorder-identifier)
- [`NutritionOrder.oralDiet.nutrient.amount`](../../fhir/resources/nutrition-order/#nutritionorder-identifier)
- [`NutritionOrder.oralDiet.texture`](../../fhir/resources/nutrition-order/#nutritionorder-identifier)
- [`NutritionOrder.oralDiet.texture.modifier`](../../fhir/resources/nutrition-order/#nutritionorder-identifier)
- [`NutritionOrder.oralDiet.texture.foodType`](../../fhir/resources/nutrition-order/#nutritionorder-identifier)
- [`NutritionOrder.oralDiet.fluidConsistencyType`](../../fhir/resources/nutrition-order/#nutritionorder-identifier)
- [`NutritionOrder.oralDiet.instruction`](../../fhir/resources/nutrition-order/#nutritionorder-identifier)
- [`NutritionOrder.supplement`](../../fhir/resources/nutrition-order/#nutritionorder-identifier)
- [`NutritionOrder.supplement.type`](../../fhir/resources/nutrition-order/#nutritionorder-identifier)
- [`NutritionOrder.supplement.productName`](../../fhir/resources/nutrition-order/#nutritionorder-identifier)
- [`NutritionOrder.supplement.schedule`](../../fhir/resources/nutrition-order/#nutritionorder-identifier)
- [`NutritionOrder.supplement.quantity`](../../fhir/resources/nutrition-order/#nutritionorder-identifier)
- [`NutritionOrder.supplement.instruction`](../../fhir/resources/nutrition-order/#nutritionorder-identifier)
- [`NutritionOrder.enteralFormula`](../../fhir/resources/nutrition-order/#nutritionorder-identifier)
- [`NutritionOrder.enteralFormula.baseFormulaType`](../../fhir/resources/nutrition-order/#nutritionorder-identifier)
- [`NutritionOrder.enteralFormula.baseFormulaProductName`](../../fhir/resources/nutrition-order/#nutritionorder-identifier)
- [`NutritionOrder.enteralFormula.additiveType`](../../fhir/resources/nutrition-order/#nutritionorder-identifier)
- [`NutritionOrder.enteralFormula.additiveProductName`](../../fhir/resources/nutrition-order/#nutritionorder-identifier)
- [`NutritionOrder.enteralFormula.caloricDensity`](../../fhir/resources/nutrition-order/#nutritionorder-identifier)
- [`NutritionOrder.enteralFormula.routeofAdministration`](../../fhir/resources/nutrition-order/#nutritionorder-identifier)
- [`NutritionOrder.enteralFormula.administration`](../../fhir/resources/nutrition-order/#nutritionorder-identifier)
- [`NutritionOrder.enteralFormula.administration.schedule`](../../fhir/resources/nutrition-order/#nutritionorder-identifier)
- [`NutritionOrder.enteralFormula.administration.quantity`](../../fhir/resources/nutrition-order/#nutritionorder-identifier)
- [`NutritionOrder.enteralFormula.administration.rate[\x`](../../fhir/resources/nutrition-order/#nutritionorder-identifier)]
- [`NutritionOrder.enteralFormula.maxVolumeToDeliver`](../../fhir/resources/nutrition-order/#nutritionorder-identifier)
- [`NutritionOrder.enteralFormula.administrationInstruction`](../../fhir/resources/nutrition-order/#nutritionorder-identifier)
- [`NutritionOrder.note`](../../fhir/resources/nutrition-order/#nutritionorder-identifier)

Penjelasan tipe mandatoris, deskripsi dan format pengisian dari setiap elemen data/path di dalam resource `NutritionOrder`, dan contoh pengiriman data atau *payload* dari data diet dapat dilihat dalam Postman Collection.

### Pemetaan Variabel dan Terminologi Spesifik

Terminologi spesifik yang digunakan dalam pengiriman data diet melalui resource `NutritionOrder` dapat dilihat dalam tabel berikut:

Tabel 24. Terminologi Spesifik

| *Resource* `Composition` | | |
| --- | --- | --- |
| **Elemen/*Path* FHIR** | **Terminologi/Format Pengisian** | |
| **Diet** | | |
| **`NutritionOrder.intent`** | ***proposal*** | ***order*** |
| **Keterangan** | **Digunakan hanya sebagai rekomendasi** | **Digunakan sebagai arahan untuk dilakukan oleh dietisien** |
| **`NutritionOrder.oralDiet.type.coding`** | **Diisi dengan kode jenis diet yang diberikan, dengan menggunakan kode SNOMED-CT maupun Kode Terminologi Kemkes. Daftar kode jenis diet dapat diakses melalui link berikut: [Lampiran Terminologi NutritionOrder.oralDiet.type](https://docs.google.com/spreadsheets/d/1Uo1yxIxL2fGxS0lLA44npiCLV8VwpUZ5/edit?gid=1729291661#gid=1729291661) untuk Jenis Diet**  **(Untuk Kode Lengkapnya dapat dilihat pada Dokumen Lampiran [Standar Terminologi](../../terminology/standar-terminologi/#standar-terminologi) SATUSEHAT)** | |
| **`NutritionOrder.oralDiet.nutrient.modifier.coding.system`** | **<http://snomed.info/sct>** | |
| **`NutritionOrder.oralDiet.nutrient.modifier.coding.code`** | **SNOMED-CT Code**  **Ruang lingkup kode SNOMED CT yang dapat dipakai: Expression Constraint Language (ECL) Query : < 226355009 | Nutrients (substance) and < 87918000 | Mineral (substance)**  **(Untuk Kode Lengkapnya dapat dilihat pada Dokumen Lampiran [Standar Terminologi](../../terminology/standar-terminologi/#standar-terminologi) SATUSEHAT)** | |
| **`NutritionOrder.oralDiet.nutrient.modifier.coding.display`** | **SNOMED-CT Description** | |
| **`NutritionOrder.oralDiet.nutrition.amount.value`** | **(Tipe data *decimal*)** | |
| **`NutritionOrder.oralDiet.nutrition.amount.unit`** | **UCUM unit**  **Kode satuan atau unit dapat menggunakan kode yang disediakan oleh *Unified Code for Units of Measure* (UCUM). Daftar kode satuan dapat diakses melalui link berikut : [Observation.valueQuantity](https://docs.google.com/spreadsheets/d/1OHM4ICgQ3hseGLrqi9GQzcREddU5SDKto50dhkhOjnc/edit?gid=0#gid=0) (UCUM)**  **(Untuk Kode Lengkapnya dapat dilihat pada Dokumen Lampiran [Standar Terminologi](../../terminology/standar-terminologi/#standar-terminologi) SATUSEHAT)** | |
| **`NutritionOrder.oralDiet.nutrition.amount.system`** | **<http://unitsofmeasure.org>** | |
| **`NutritionOrder.oralDiet.nutrition.amount.code`** | **UCUM Code** | |
| **`NutritionOrder.excludeFoodModifier.coding.system`** | **<http://snomed.info/sct>** | |
| **`NutritionOrder.excludeFoodModifier.coding.code`** | **SNOMED-CT Code**  **Ruang lingkup kode SNOMED CT yang dapat dipakai: Expression Constraint Language (ECL) Query : < 255620007|Food (substance)|**  **(Untuk Kode Lengkapnya dapat dilihat pada Dokumen Lampiran [Standar Terminologi](../../terminology/standar-terminologi/#standar-terminologi) SATUSEHAT)** | |
| **`NutritionOrder.excludeFoodModifier.coding.display`** | **SNOMED-CT Description** | |
| **`NutritionOrder.note.text`** | **Tipe data *string*** | |

## 21. Pengiriman Data Edukasi

Variabel edukasi menunjukkan edukasi dan instruksi kerja untuk membantu individu dan keluarga dalam meningkatkan kemampuan untuk mencapai kesehatan secara optimal dan bersedia berpartisipasi dalam proses penyembuhan pada saat pulang. Data terkait edukasi yang diberikan kepada pasien dikirimkan menggunakan resource [`Procedure`](../../fhir/resources/procedure/#procedure). Pemetaan nilai resource `Procedure` dapat merujuk pada bab terkait Tindakan/Prosedur Medis.

#### Pemetaan Variabel dan Terminologi Spesifik

Terminologi spesifik yang digunakan dalam data edukasi melalui resource [`Procedure`](../../fhir/resources/procedure/#procedure) dapat dilihat dalam tabel berikut:

Tabel 25. Terminologi spesifik yang digunakan dalam data edukasi melalui resource `Procedure`

| Pemetaan Variabel *Resource* `Procedure` | | | |
| --- | --- | --- | --- |
| **1. Edukasi** | | | |
| **`Procedure.category.coding.system`** | | **<http://snomed.info/sct>** | |
| **`Procedure.category.coding.code`** | | **409073007** | |
| **`Procedure.category.coding.display`** | | **Education** | |
| **`Procedure.code.coding.system`** | | **<http://terminology.kemkes.go.id/CodeSystem/kptl>** | |
| **`Procedure.code.coding.code`** | | **10913** | |
| **`Procedure.code.coding.display`** | | **Edukasi Kesehatan Individu** | |
| **`Procedure.code.coding.system`** | **`Procedure.code.coding.code`** | **`Procedure.code.coding.display`** | **Keterangan** |
| **<http://snomed.info/sct>** | **84635008** | **Disease process or condition education** | **1. Proses penyakit, diagnosis, dan rencana asuhan** |
| **<http://snomed.info/sct>** | **967006** | **Medication education** | **2. Obat-obatan** |
| **<http://snomed.info/sct>** | **410082002** | **Rehabilitation therapy education** | **3. Rehabilitasi medis** |
| **<http://snomed.info/sct>** | **712651001** | **Education about pain** | **4. Manajemen nyeri** |
| **<http://snomed.info/sct>** | **61310001** | **Nutrition education** | **5. Gizi** |
| **<http://snomed.info/sct>** | **698608004** | **Hand washing education** | **6. Cuci tangan** |
| **<http://snomed.info/sct>** | **362978005** | **Medical equipment or device education** | **7. Penggunaan alat medis** |
| **Keterangan:**  - Perlu dikirimkan 2 `Procedure.code` dalam 1 *payload* terkait Edukasi, yaitu dengan menggunakan kode KPTL dan kode SNOMED-CT - Kode KPTL yang disebutkan di atas merupakan kode KPTL untuk edukasi secara umum, namun jika diperlukan kode KPTL untuk edukasi secara spesifik dapat menggunakan acuan dari Buku Panduan Kode Pembiayaan Tindakan dan Layanan Kesehatan Nasional (KPTL) - Kode SNOMED-CT yang disebutkan di atas merupakan beberapa contoh kode yang dapat digunakan. Ruang lingkup kode SNOMED CT yang dapat dipakai: Expression Constraint Language (ECL) Query : < 409073007 | Education (procedure) | (Untuk Kode Lengkapnya dapat dilihat pada Dokumen Lampiran [Standar Terminologi](../../terminology/standar-terminologi/#standar-terminologi) SATUSEHAT) | | | |

## 22. Pengiriman Data Prognosis

Data prognosis berisi prediksi mengenai perkembangan kondisi pasien. Data prognosis dapat dikirimkan melalui resource `ClinicalImpression`. Pemetaan nilai resource `ClinicalImpression` dapat merujuk pada bab Riwayat Perjalanan Penyakit.

### Pemetaan nilai dan Terminologi Spesifik

Terminologi spesifik yang digunakan dalam pengiriman data prognosis melalui resource [`ClinicalImpression`](../../fhir/resources/clinical-impression/#clinicalimpression) dapat dilihat dalam tabel berikut:

Tabel 26. Terminologi spesifik yang digunakan dalam pengiriman data prognosis melalui resource `ClinicalImpression`

| *Resource* `ClinicalImpression` | | | |
| --- | --- | --- | --- |
| **Nama Variabel: Prognosis** | | | |
| **`ClinicalImpression.code.coding.system`** | | **<http://snomed.info/sct>** | |
| **`ClinicalImpression.code.coding.code`** | | **20481000** | |
| **`ClinicalImpression.code.coding.display`** | | **Determination of prognosis** | |
| **`*ClinicalImpression.prognosisCodeableConcept[i].coding.system`** | **`*ClinicalImpression.prognosisCodeableConcept[i].coding.code`** | **`*ClinicalImpression.prognosisCodeableConcept[i].coding.display`** | **Keterangan** |
| **<http://snomed.info/sct>** | **170968001** | **Prognosis good** | **1. Baik;** |
| **<http://snomed.info/sct>** | **65872000** | **Fair prognosis** | **2. Dubia et bonam / cenderung baik;** |
| **<http://snomed.info/sct>** | **67334001** | **Guarded prognosis** | **3. Dubia et malam / cenderung tidak baik;** |
| **<http://snomed.info/sct>** | **170969009** | **Prognosis bad** | **4. Tidak baik** |

## 23. Pengiriman Data Rencana Tindak Lanjut

Data rencana tindak lanjut menunjukkan rencana perawatan selanjutnya yang akan diterima oleh pasien setelah pulang. Data terkait dengan rencana tindak lanjut ini dikirimkan menggunakan resource [`ServiceRequest`](../../fhir/resources/service-request/#servicerequest).

### Pemetaan Nilai ServiceRequest

Berikut pemetaan nilai untuk `ServiceRequest` yang direpresentasikan dalam peta referensi (*path*) ke properti (*element id*) terkait, untuk konteks jenis perawatan:

|  |  |
| --- | --- |
|  | 1. Setiap terdapat simbol asterik `*` sebelum nama variabel/parameter/element FHIR yang disebutkan, maka variabel/parameter/element FHIR tersebut bersifat **WAJIB**, **harus ada**, atau **pasti selalu ada**, contoh: **`*Location.identifier`**. 2. **Standar format Waktu** yang digunakan dalam pengiriman data adalah **UTC +00**. Misalnya waktu **WIB**, maka format yang digunakan adalah **waktu sekarang dikurangi 7**, jika **WITA**, maka **waktu sekarang dikurangi 8**, dan Jika **WIT**, maka **waktu sekarang dikurangi 9**.  **Contoh:** Pukul 17.35 WIB tanggal 23 Agustus 2023 maka yang dikirimkan adalah waktunya perlu diubah ke UTC +00 menjadi 10.35, berarti menjadi `2023-08-23T10:35:00+00:00`. 3. **Standar format pengiriman Tanggal** tidak bisa kurang dari 03 Juni 2014. |

|  |  |
| --- | --- |
|  | Silakan klik setiap teks variabel/parameter/element FHIR pada daftar pemetaan nilai di bawah ini (berwarna **merah**), untuk membaca panduan lebih detail/lanjut ke bagian yang direferensikan. |

Berikut pemetaan nilai untuk `ServiceRequest` yang direpresentasikan dalam peta referensi *(path)* ke properti *(element id)* terkait, untuk konteks jenis perawatan:

- [`ServiceRequest.identifier`](../../fhir/resources/service-request/#servicerequest-identifier)
- [`*ServiceRequest.status`](../../fhir/resources/service-request/#servicerequest-status)
- [`*ServiceRequest.intent`](../../fhir/resources/service-request/#servicerequest-intent)
- [`*ServiceRequest.code`](../../fhir/resources/service-request/#servicerequest-code)
- [`*ServiceRequest.subject`](../../fhir/resources/service-request/#servicerequest-subject)
- [`*ServiceRequest.encounter`](../../fhir/resources/service-request/#servicerequest-encounter)
- [`ServiceRequest.authoredOn`](../../fhir/resources/service-request/#servicerequest-authoredOn)
- [`ServiceRequest.locationCode`](../../fhir/resources/service-request/#servicerequest-locationCode)

Penjelasan tipe mandatoris, deskripsi dan format pengisian dari setiap elemen data/*path* di dalam resource `Encounter` (data pendaftaran kunjungan pasien), dapat dilihat dalam resource [`Encounter`](../../fhir/resources/encounter/#encounter). Untuk contoh pengiriman data atau *payload* dari data rencana tindak lanjut/cara keluar dari rumah sakit dengan pilihan jawaban “Pulang atas persetujuan dokter” dan “Pulang atas permintaan sendiri”, dan “lain-lain” dapat dilihat dalam [Postman SATUSEHAT](../../postman-workshop/#postman-collection-satusehat) SATUSEHAT.

### Pemetaan Variabel dan Terminologi Spesifik

Terminologi spesifik yang digunakan dalam rencana tindak lanjut dengan melalui resource `ServiceRequest` dapat dilihat dalam tabel berikut:

Tabel 27. Pemetaan Variabel dan Terminologi Spesifik

| *Resource* `ServiceRequest` | |
| --- | --- |
| **Elemen/Path FHIR** | **Terminologi/Format Pengisian** |
| **Rujukan Internal** | |
| **1. Rawat Inap** | |
| **`ServiceRequest.category.coding.system`** | **<http://snomed.info/sct>** |
| **`ServiceRequest.category.coding.code`** | **3457005** |
| **`ServiceRequest.category.coding.display`** | **Patient referral** |
| **`ServiceRequest.code.coding.system`** | **<http://snomed.info/sct>** |
| **`ServiceRequest.code.coding.code`** | **737481003** |
| **`ServiceRequest.code.coding.display`** | **Inpatient care management** |
| **2. Kontrol Ulang** | |
| **`ServiceRequest.category.coding.system`** | **<http://snomed.info/sct>** |
| **`ServiceRequest.category.coding.code`** | **3457005** |
| **`ServiceRequest.category.coding.display`** | **Patient referral** |
| **`ServiceRequest.code.coding.system`** | **<http://snomed.info/sct>** |
| **`ServiceRequest.code.coding.code`** | **185389009** |
| **`ServiceRequest.code.coding.display`** | **Follow-up visit** |
| **3.Konsultasi** | |
| **`ServiceRequest.category.coding.system`** | **<http://snomed.info/sct>** |
| **`ServiceRequest.category.coding.code`** | **3457005** |
| **`ServiceRequest.category.coding.display`** | **Patient referral** |
| **`ServiceRequest.code.coding.system`** | **<http://snomed.info/sct>** |
| **`ServiceRequest.code.coding.code`** | **11429006** |
| **`ServiceRequest.code.coding.display`** | **Consultation** |
| **Rujukan Eksternal** | |
| **1. Rawat Inap** | |
| **`ServiceRequest.category.coding.system`** | **<http://snomed.info/sct>** |
| **`ServiceRequest.category.coding.code`** | **3457005** |
| **`ServiceRequest.category.coding.display`** | **Patient referral** |
| **`ServiceRequest.code.coding.system`** | **<http://snomed.info/sct>** |
| **`ServiceRequest.code.coding.code`** | **737481003** |
| **`ServiceRequest.code.coding.display`** | **Inpatient care management** |
| **2. Rawat Jalan** | |
| **`ServiceRequest.category.coding.system`** | **<http://snomed.info/sct>** |
| **`ServiceRequest.category.coding.code`** | **3457005** |
| **`ServiceRequest.category.coding.display`** | **Patient referral** |
| **`ServiceRequest.code.coding.system`** | **<http://snomed.info/sct>** |
| **`ServiceRequest.code.coding.code`** | **737492002** |
| **`ServiceRequest.code.coding.display`** | **Outpatient care management** |

## 24. Pengiriman Data Instruksi untuk Tindak Lanjut & Sarana Transportasi Untuk Rujuk

Variabel Instruksi untuk tindak lanjut dan resource yang digunakan dapat dilihat dalam tabel berikut:

Tabel 28. Variabel instruksi untuk tindak lanjut dan resources yang digunakan

| Variabel | | Format/*Value* | *Path* FHIR |
| --- | --- | --- | --- |
| **Instruksi untuk Tindak Lanjut** | **Kontrol ke** | **1. Poli** | **`ServiceRequest.locationCode`** |
| **2. Fasyankes** |
| **3. Lain-lain (*free text*)** |
| **Sarana Transportasi untuk Rujuk** | **4. Ambulance** | **`ServiceRequest.locationCode`** |
| **Tanggal** |  | **`ServiceRequest.occurrenceDateTime`** |
| **Dalam Keadaan Darurat dapat Menghubungi** |  | **`ServiceRequest.patientInstruction`** |

### Pemetaan Nilai ServiceRequest

Berikut pemetaan nilai untuk `ServiceRequest` yang direpresentasikan dalam peta referensi *(path)* ke properti *(element id)* terkait, untuk konteks jenis perawatan:

|  |  |
| --- | --- |
|  | Setiap terdapat simbol asterik `*` sebelum nama variabel/parameter/element FHIR yang disebutkan, maka variabel/parameter/element FHIR tersebut bersifat **WAJIB**, **harus ada**, atau **pasti selalu ada**, contoh: **`*Location.identifier`**. |

|  |  |
| --- | --- |
|  | Silakan klik setiap teks variabel/parameter/element FHIR pada daftar pemetaan nilai di bawah ini (berwarna **merah**), untuk membaca panduan lebih detail/lanjut ke bagian yang direferensikan. |

- [`ServiceRequest.identifier`](../../fhir/resources/service-request/#servicerequest-identifier)
- [`*ServiceRequest.status`](../../fhir/resources/service-request/#servicerequest-status)
- [`*ServiceRequest.intent`](../../fhir/resources/service-request/#servicerequest-intent)
- [`*ServiceRequest.code`](../../fhir/resources/service-request/#servicerequest-code)
- [`*ServiceRequest.subject`](../../fhir/resources/service-request/#servicerequest-subject)
- [`*ServiceRequest.encounter`](../../fhir/resources/service-request/#servicerequest-encounter)
- [`ServiceRequest.occurrenceDateTime`](../../fhir/resources/service-request/#servicerequest-occurrence-date-time)
- [`ServiceRequest.authoredOn`](../../fhir/resources/service-request/#servicerequest-authoredOn)
- [`*ServiceRequest.performer`](../../fhir/resources/service-request/#servicerequest-performer)
- [`ServiceRequest.locationCode`](../../fhir/resources/service-request/#servicerequest-locationCode)
- [`ServiceRequest.locationReference`](../../fhir/resources/service-request/#servicerequest-location-reference)
- [`ServiceRequest.patientInstruction`](../../fhir/resources/service-request/#servicerequest-patientinstruction)

Pengiriman data instruksi tindak lanjut dikirimkan melalui resource [`ServiceRequest`](../../fhir/resources/service-request/#servicerequest). Penjelasan tipe mandatoris, deskripsi dan format pengisian dari setiap elemen data/*path* di dalam resource `ServiceRequest` (rencana/intruksi tindak lanjut/cara keluar dari rumah sakit), dapat dilihat dalam resource [`ServiceRequest`](../../fhir/resources/service-request/#servicerequest). Untuk contoh pengiriman data atau *payload* dari `ServiceRequest` dapat dilihat dalam [Postman SATUSEHAT](../../postman-workshop/#postman-collection-satusehat) SATUSEHAT.

#### Pemetaan Variabel dan Terminologi Spesifik

Terminologi spesifik yang digunakan dalam instruksi tindak lanjut melalui resource [`ServiceRequest`](../../fhir/resources/service-request/#servicerequest) dapat dilihat dalam tabel berikut:

Tabel 29. Pemetaan Variabel dan Terminologi Spesifik

| *Resource* `ServiceRequest` | | | |
| --- | --- | --- | --- |
| **Elemen/*Path* FHIR** | **Terminologi/Format Pengisian** | | |
| **Instruksi Tindak Lanjut** | | | |
| **`ServiceRequest.locationCode.coding.system`** | **<http://terminology.hl7.org/CodeSystem/v3-RoleCode>** | | |
| **`ServiceRequest.locationCode.code.coding.code`** | **OF** | **HOSP** | **PC** |
| **`ServiceRequest.locationCode.code.coding.display`** | **Outpatient facility** | **Hospital** | **Primary care clinic** |
| **Keterangan `ServiceRequest.locationCode`** | **1. Poli** | **2. Fasyankes** | **2. Fasyankes** |
| **Untuk pilihan jawaban “3. Lain-lain (free-text)”, maka tuliskan keterangan melalui elemen ServiceRequest.locationCode.text** | | |
| **Keterangan `ServiceRequest.locationReference`** | **ID Referensi Lokasi dapat digunakan saat jika pasien melakukan Rujukan Internal antar poli** | | |
| **Sarana Transportasi untuk Rujuk** | | | |
| **`ServiceRequest.locationCode.coding.system`** | **<http://terminology.hl7.org/CodeSystem/v3-RoleCode>** | | |
| **`ServiceRequest.locationCode.code.coding.code`** | **AMB** | | |
| **`ServiceRequest.locationCode.code.coding.display`** | **Ambulance** | | |

## 25. Pengiriman Data Kondisi Saat Meninggalkan Rumah Sakit

Data kondisi saat meninggalkan rumah sakit menunjukkan keadaan pasien saat meninggalkan rumah sakit. Pengisian pilihan jawaban dari kondisi saat meninggalkan rumah sakit dan resource yang digunakan dapat dilihat dalam tabel berikut:

Tabel 30. Pilihan jawaban dari kondisi saat meninggalkan rumah sakit dan resource yang digunakan

| Variabel | Format/*Value* | *Resource* | Elemen Data / *Path* |
| --- | --- | --- | --- |
| **Kondisi Saat Meninggalkan Rumah Sakit** | **1. Stabil** | **`Condition`** | **`Condition.code.coding`** |
| **2. Tidak stabil** | **`Condition`** | **`Condition.code.coding`** |
| **3. Perbaikan** | **`Condition`** | **`Condition.code.coding`** |
| **4. Pulang paksa** | **`Encounter`** | **`Encounter.hospitalization.dischargeDisposition.coding`** |
| **5. Dirujuk** | **`Encounter`** | **`Encounter.hospitalization.dischargeDisposition.coding`** |
| **6. Meninggal<48 jam** | **`Encounter`** | **`Encounter.hospitalization.dischargeDisposition.coding`** |
| **7. Meninggal>48 jam** | **`Encounter`** | **`Encounter.hospitalization.dischargeDisposition.coding`** |
| **8. Lain-lain (free text)** | **`Encounter`** | **`Encounter.hospitalization.dischargeDisposition.coding`** |

Kondisi saat meninggalkan rumah sakit dengan pilihan jawaban “Stabil”, “Tidak stabil”, dan “Perbaikan” akan dikirimkan menggunakan resource [`Condition`](../../fhir/resources/condition/#condition).

### Pemetaan Nilai Condition

Berikut pemetaan nilai untuk `Condition` yang direpresentasikan dalam peta referensi *(path)* ke properti *(element id)* terkait, untuk konteks jenis perawatan:

|  |  |
| --- | --- |
|  | Setiap terdapat simbol asterik `*` sebelum nama variabel/parameter/element FHIR yang disebutkan, maka variabel/parameter/element FHIR tersebut bersifat **WAJIB**, **harus ada**, atau **pasti selalu ada**, contoh: **`*Location.identifier`**. |

|  |  |
| --- | --- |
|  | Silakan klik setiap teks variabel/parameter/element FHIR pada daftar pemetaan nilai di bawah ini (berwarna **merah**), untuk membaca panduan lebih detail/lanjut ke bagian yang direferensikan. |

- [`Condition.clinicalStatus`](../../fhir/resources/condition/#condition-clinicalStatus)
- [`Condition.category`](../../fhir/resources/condition/#condition-category)
- [`*Condition.code`](../../fhir/resources/condition/#condition-code)
- [`*Condition.subject`](../../fhir/resources/condition/#condition-subject)
- [`*Condition.encounter`](../../fhir/resources/condition/#condition-encounter)

Penjelasan tipe mandatoris, deskripsi dan format pengisian dari setiap elemen data/*path* di dalam resource `Condition` (data diagnosis), dapat dilihat dalam resource [`Condition`](../../fhir/resources/condition/#condition). Untuk contoh pengiriman data atau *payload* dari `Condition` seperti contoh pengiriman data atau *payload* dari data kondisi saat meninggalkan rumah sakit dengan pilihan jawaban “Stabil”, “Tidak stabil”, dan “Perbaikan” dapat dilihat dalam [Postman SATUSEHAT](../../postman-workshop/#postman-collection-satusehat) SATUSEHAT.

### Pemetaan Variabel dan Terminologi Spesifik

Terminologi spesifik yang digunakan dalam pengiriman data kondisi saat meninggalkan rumah sakit dengan pilihan jawaban “Stabil”, “Tidak stabil”, dan “Perbaikan” melalui resource [`Condition`](../../fhir/resources/condition/#condition) dapat dilihat dalam tabel berikut:

Tabel 31. Terminologi spesifik yang digunakan dalam pengiriman data kondisi saat meninggalkan rumah sakit melalui resource `Condition`

| *Resource* `Condition` | | | |
| --- | --- | --- | --- |
| **Elemen/*Path* FHIR** | **Terminologi/Format Pengisian** | | |
| **Nama Variabel: Kondisi Saat Meninggalkan Rumah Sakit** | | | |
| **`Condition.category.coding.system`** | **<http://terminology.hl7.org/CodeSystem/condition-category>** | | |
| **`Condition.category.coding.code`** | **problem-list-item** | | |
| **`Condition.category.coding.display`** | **Problem List Item** | | |
| **`Condition.code.coding.system`** | **<http://snomed.info/sct>** | | |
| **`Condition.code.coding.code`** | **359746009** | **162668006** | **268910001** |
| **`Condition.code.coding.display`** | **Patient’s condition stable** | **Patient’s condition unstable** | **Patient’s condition improved** |
| **Keterangan** | **Stabil** | **Tidak stabil** | **Perbaikan** |

Kondisi saat meninggalkan rumah sakit dengan pilihan jawaban “Pulang paksa”, “Dirujuk”, “Meninggal <48 jam”, “Meninggal > 48 jam”, dan “lain-lain” akan dikirimkan menggunakan resource [`Encounter`](../../fhir/resources/encounter/#encounter) pada elemen `Encounter.hospitalization.dischargeDisposition.coding`. Sedangkan untuk pilihan jawaban lain-lain, keterangan tambahan dapat dikirimkan dengan tipe data `String` melalui elemen `Encounter.hospitalization.dischargeDisposition.text`.

Penjelasan tipe mandatoris, deskripsi dan format pengisian dari setiap elemen data/*path* di dalam resource `Encounter` (data pendaftaran kunjungan pasien), dapat dilihat dalam resource [`Encounter`](../../fhir/resources/encounter/#encounter). Untuk contoh pengiriman data atau *payload* dari data kondisi saat meninggalkan rumah sakit dengan pilihan jawaban “Pulang paksa”, “Dirujuk”, “Meninggal <48 jam”, “Meninggal > 48 jam”, dan “lain-lain” dapat dilihat dalam [Postman SATUSEHAT](../../postman-workshop/#postman-collection-satusehat) SATUSEHAT.

Terminologi spesifik yang digunakan dalam pengiriman data kondisi saat meninggalkan rumah sakit dengan pilihan jawaban “Dirujuk”, “Meninggal <48 jam”, “Meninggal > 48 jam” melalui resource [`Encounter`](../../fhir/resources/encounter/#encounter) dapat dilihat dalam tabel berikut:

Tabel 32. Terminologi spesifik yang digunakan dalam pengiriman data kondisi saat meninggalkan rumah sakit melalui resource `Encounter`

| Pemetaan Variabel *Resource* `Encounter` | | | |
| --- | --- | --- | --- |
| **Kondisi Saat Meninggalkan Rumah Sakit** | | | |
| **`Encounter.hospitalization.dischargeDisposition.coding.system`** | **`Encounter.hospitalization.dischargeDisposition.coding.code`** | **`Encounter.hospitalization.dischargeDisposition.coding.display`** | **Keterangan** |
| **<http://terminology.hl7.org/CodeSystem/discharge-disposition>** | **aadvice** | **Left against advice** | **4. Pulang paksa** |
| **<http://terminology.hl7.org/CodeSystem/discharge-disposition>** | **other-hcf** | **Other healthcare facility** | **5. Dirujuk** |
| **<http://terminology.kemkes.go.id/CodeSystem/discharge-disposition>** | **exp-lt48h** | **Meninggal <48 jam** | **6. Meninggal <48 jam;** |
| **<http://terminology.kemkes.go.id/CodeSystem/discharge-disposition>** | **exp-gt48h** | **Meninggal >48 jam** | **7. Meninggal >48 jam** |
| **<http://terminology.hl7.org/CodeSystem/discharge-disposition>** | **oth** | **Other** | **8. Lain- lain (free text)** |

## 26. Pengiriman Data Cara Keluar dari Rumah Sakit

Data cara keluar dari rumah sakit menjelaskan terkait cara pasien keluar dari rumah sakit. Data cara keluar dari rumah sakit diisi dengan pilihan jawaban “Pulang atas persetujuan dokter” dan “Pulang atas permintaan sendiri”. Data tersebut akan dikirimkan menggunakan resource `Encounter` pada elemen `Encounter.hospitalization.dischargeDisposition.coding`. Sedangkan untuk pilihan jawaban “Lain-lain”, keterangan tambahan dapat dikirimkan dengan tipe data String melalui elemen `Encounter.hospitalization.dischargeDisposition.text`.

### Pemetaan Variabel dan Terminologi Spesifik

Tabel 33. Terminologi spesifik yang digunakan dalam pengiriman data kondisi saat meninggalkan rumah sakit melalui resource `Encounter`

| *Resource* `Encounter` | | | |
| --- | --- | --- | --- |
| **Cara keluar dari rumah sakit** | | | |
| **`Encounter.hospitalization. dischargeDisposition. coding.system`** | **`Encounter.hospitalization. dischargeDisposition. coding.code`** | **`Encounter.hospitalization. dischargeDisposition. coding.display`** | **Keterangan** |
| **<http://terminology.hl7.org/CodeSystem/discharge-disposition>** | **home** | **Home** | **1. Pulang atas persetujuan dokter** |
| **<http://terminology.hl7.org/CodeSystem/discharge-disposition>** | **aadvice** | **Left against advice** | **2. Pulang atas permintaan sendiri** |
| **<http://terminology.hl7.org/CodeSystem/discharge-disposition>** | **oth** | **Other** | **3. Lain-lain (free text)** |

Penjelasan tipe mandatoris, deskripsi dan format pengisian dari setiap elemen data/*path* di dalam resource `ServiceRequest` (rencana tindak lanjut/cara keluar dari rumah sakit), dapat dilihat dalam resource [`ServiceRequest`](../../fhir/resources/service-request/#servicerequest). Untuk contoh pengiriman data atau *payload* dari data rencana tindak lanjut/cara keluar dari rumah sakit dengan pilihan jawaban “Dirujuk ke” dan “Rawat Inap” dapat dilihat dalam [Postman SATUSEHAT](../../postman-workshop/#postman-collection-satusehat) SATUSEHAT.

## 27. Pembaharuan Data Kunjungan

Setelah pasien selesai melakukan kunjungan ke fasyankes, maka perlu dilakukan pembaharuan data kunjungan dengan menambahkan informasi seperti keluhan utama, diagnosis primer, diagnosis sekunder, periode kunjungan selesai, lama perawatan (menit), Kondisi Saat Meninggalkan Rumah Sakit, dan Rencana Tindak Lanjut serta Cara Keluar dari Rumah Sakit, atau informasi lainnya yang belum tersedia di awal kunjungan dengan metode `PUT`. Pastikan dalam *payload* yang akan dilakukan pembaharuan, dimasukkan elemen `Encounter.id` yang berisi ID balikan dari SATUSEHAT setelah pengiriman data kunjungan di awal.

Penjelasan tipe mandatoris, deskripsi dan format pengisian dari setiap elemen data/*path* dapat dilihat dalam resource `Encounter`. Untuk contoh pengiriman data atau *payload* dari pembaharuan data kunjungan dapat dilihat dalam [**Postman SATUSEHAT**](../../postman-workshop/#postman-collection-satusehat).

## 28. Pengiriman Data Resume Medis

Resume medis berisi informasi mengenai kegiatan pelayanan medis yang diberikan kepada pasien oleh tenaga kesehatan, dari pasien datang hingga pasien pulang. Data resume medis dikirimkan menggunakan resource `Composition` dengan mereferensikan data-data yang didapatkan dalam kunjungan tersebut pada *section* yang sesuai dalam 1 *payload*.

### Pemetaan Nilai Composition

Berikut pemetaan nilai untuk `Composition` yang direpresentasikan dalam peta referensi (*path*) ke properti (*element id*) terkait:

|  |  |
| --- | --- |
|  | 1. Setiap terdapat simbol asterik `*` sebelum nama variabel/parameter/element FHIR yang disebutkan, maka variabel/parameter/element FHIR tersebut bersifat **WAJIB**, **harus ada**, atau **pasti selalu ada**, contoh: **`*Location.identifier`**. 2. **Standar format Waktu** yang digunakan dalam pengiriman data adalah **UTC +00**. Misalnya waktu **WIB**, maka format yang digunakan adalah **waktu sekarang dikurangi 7**, jika **WITA**, maka **waktu sekarang dikurangi 8**, dan Jika **WIT**, maka **waktu sekarang dikurangi 9**.  **Contoh:** Pukul 17.35 WIB tanggal 23 Agustus 2023 maka yang dikirimkan adalah waktunya perlu diubah ke UTC +00 menjadi 10.35, berarti menjadi `2023-08-23T10:35:00+00:00`. 3. **Standar format pengiriman Tanggal** tidak bisa kurang dari 03 Juni 2014. |

|  |  |
| --- | --- |
|  | Silakan klik setiap teks variabel/parameter/element FHIR pada daftar pemetaan nilai di bawah ini (berwarna **merah**), untuk membaca panduan lebih detail/lanjut ke bagian yang direferensikan. |

- [`Composition.identifier`](../../fhir/resources/composition/#composition-identifier)
- [`*Composition.status`](../../fhir/resources/composition/#composition-status)
- [`*Composition.type`](../../fhir/resources/composition/#composition-type)
- [`Composition.category`](../../fhir/resources/composition/#composition-category)
- [`*Composition.subject`](../../fhir/resources/composition/#composition-subject)
- [`Composition.encounter`](../../fhir/resources/composition/#composition-encounter)
- [`*Composition.date`](../../fhir/resources/composition/#composition-date)
- [`*Composition.author[i]`](../../fhir/resources/composition/#composition-author)
- [`*Composition.title`](../../fhir/resources/composition/#composition-title)
- [`Composition.confidentiality`](../../fhir/resources/composition/#composition-confidentiality)
- [`*Composition.attester.mode`](../../fhir/resources/composition/#composition-attester-mode)
- [`Composition.attester.time`](../../fhir/resources/composition/#composition-attester-time)
- [`Composition.attester.party`](../../fhir/resources/composition/#composition-attester-party)
- [`Composition.custodian`](../../fhir/resources/composition/#composition-custodian)
- [`*Composition.relatesTo[i].code`](../../fhir/resources/composition/#composition-relatesTo-code)

|  |  |
| --- | --- |
|  | Penjelasan tipe mandatoris, deskripsi dan format pengisian dari setiap elemen data/*path* di dalam resource tersebut, dapat dilihat dalam [**Resources - Interoperability**](../../fhir/resources/#interoperability). Contoh pengiriman data atau *payload* dari pengiriman data sesuai dengan resource atau *use case* tersebut dapat dilihat dalam [**Postman SATUSEHAT**](../../postman-workshop/#postman-collection-satusehat) |

- [`*Composition.relatesTo[i].target<?>`](../../fhir/resources/composition/#composition-relatesTo-target)
- [`Composition.event[i].code`](../../fhir/resources/composition/#composition-event-code)
- [`Composition.event[i].period`](../../fhir/resources/composition/#composition-event-period)
- [`Composition.event[i].detail`](../../fhir/resources/composition/#composition-event-detail)
- [`Composition.section[i].title`](../../fhir/resources/composition/#composition-section-title)
- [`Composition.section[i].code`](../../fhir/resources/composition/#composition-section-code)
- [`Composition.section[i].author`](../../fhir/resources/composition/#composition-section-author)
- [`Composition.section[i].text`](../../fhir/resources/composition/#composition-section-text)
- [`Composition.section[i].mode`](../../fhir/resources/composition/#composition-section-mode)
- [`Composition.section[i].orderedBy`](../../fhir/resources/composition/#composition-section-orderedBy)
- [`Composition.section[i].entry`](../../fhir/resources/composition/#composition-section-entry)
- [`Composition.section[i].emptyReason`](../../fhir/resources/composition/#composition-section-emptyReason)

### Pemetaan Variabel dan Terminologi Spesifik

Pemetaan variabel yang digunakan dalam pengiriman data resume medis melalui resource `Composition` dapat dilihat dalam tabel berikut:

Tabel 34. Terminologi Spesifik

| Pemetaan Variabel *Resource* `Composition` | |
| --- | --- |
| **Elemen/*Path* FHIR** | **Terminologi/Format Pengisian** |
| **Resume Medis** | |
| **`Composition.type.coding.system`** | **<http://loinc.org>** |
| **`Composition.type.coding.code`** | **88645-7** |
| **`Composition.type.coding.display`** | **Outpatient hospital Discharge summary** |
| **`Composition.category.coding.system`** | **<http://loinc.org>** |
| **`Composition.category.coding.code`** | **LP173421-1** |
| **`Composition.category.coding.display`** | **Report** |
| **1. Anamnesis** | |
| **`Composition.section.title`** | ***Anamnesis*** |
| **`Composition.section.code.coding.system`** | **<http://terminology.kemkes.go.id>** |
| **`Composition.section.code.coding.code`** | **TK000003** |
| **`Composition.section.code.coding.display`** | **Anamnesis** |
| **a. Keluhan Utama** | |
| **`Composition.section.section.title`** | ***Keluhan Utama*** |
| **`Composition.section.section.code.coding.system`** | **<http://loinc.org>** |
| **`Composition.section.section.code.coding.code`** | **10154-3** |
| **`Composition.section.section.code.coding.display`** | **Chief complaint Narrative - Reported** |
| **`Composition.section.section.entry`** | **Reference ke resource `Condition` (Keluhan Utama)** |
| **b. Keluhan Penyerta** | |
| **`Composition.section.section.title`** | ***Keluhan Penyerta*** |
| **`Composition.section.section.code.coding.system`** | **<http://loinc.org>** |
| **`Composition.section.section.code.coding.code`** | **11450-4** |
| **`Composition.section.section.code.coding.display`** | **Problem list - Reported** |
| **`Composition.section.section.entry`** | **Reference ke resource `Condition` (Keluhan Penyerta)** |
| **c. Riwayat Alergi** | |
| **`Composition.section.section.title`** | ***Riwayat Alergi*** |
| **`Composition.section.section.code.coding.system`** | **<http://loinc.org>** |
| **`Composition.section.section.code.coding.code`** | **48765-2** |
| **`Composition.section.section.code.coding.display`** | **Allergies** |
| **`Composition.section.section.entry`** | **Reference ke resource `AllergyIntolerance` (Riwayat Alergi)** |
| **d. Riwayat Penyakit Pribadi (terdahulu)** | |
| **`Composition.section.section.title`** | ***Riwayat Penyakit Pribadi Terdahulu*** |
| **`Composition.section.section.code.coding.system`** | **<http://loinc.org>** |
| **`Composition.section.section.code.coding.code`** | **11348-0** |
| **`Composition.section.section.code.coding.display`** | **History of Past illness Narrative** |
| **`Composition.section.section.entry`** | **Reference ke resource `Condition` (Riwayat Penyakit Pribadi dengan status *inactive*)** |
| **e. Riwayat Penyakit Pribadi (sekarang)** | |
| **`Composition.section.section.title`** | ***Riwayat Penyakit Pribadi Sekarang*** |
| **`Composition.section.section.code.coding.system`** | **<http://loinc.org>** |
| **`Composition.section.section.code.coding.code`** | **10164-2** |
| **`Composition.section.section.code.coding.display`** | **History of Present illness Narrative** |
| **`Composition.section.section.entry`** | **Reference ke resource `Condition` (Riwayat Penyakit Pribadi dengan status *active*)** |
| **f. Riwayat Penyakit Keluarga** | |
| **`Composition.section.section.title`** | ***Riwayat Penyakit Keluarga*** |
| **`Composition.section.section.code.coding.system`** | **<http://loinc.org>** |
| **`Composition.section.section.code.coding.code`** | **10157-6** |
| **`Composition.section.section.code.coding.display`** | **History of family member diseases Narrative** |
| **`Composition.section.section.entry`** | **Reference ke resource `FamilyMemberHistory` (Riwayat Penyakit Keluarga)** |
| **g. Riwayat Pengobatan** | |
| **`Composition.section.section.title`** | ***Riwayat Pengobatan*** |
| **`Composition.section.section.code.coding.system`** | **<http://loinc.org>** |
| **`Composition.section.section.code.coding.code`** | **10160-0** |
| **`Composition.section.section.code.coding.display`** | **History of Medication use Narrative** |
| **`Composition.section.section.entry`** | **Reference ke resource `MedicationStatement` (Riwayat Pengobatan)** |
| **2. Pemeriksaan Fisik** | |
| **`Composition.section.title`** | ***Pemeriksaan Fisik*** |
| **`Composition.section.code.coding.system`** | **<http://terminology.kemkes.go.id>** |
| **`Composition.section.code.coding.code`** | **TK000007** |
| **`Composition.section.code.coding.display`** | **Pemeriksaan Fisik** |
| **a. Tanda vital** | |
| **`Composition.section.section.title`** | ***Tanda Vital*** |
| **`Composition.section.section.code.coding.system`** | **<http://loinc.org>** |
| **`Composition.section.section.code.coding.code`** | **8716-3** |
| **`Composition.section.section.code.coding.display`** | **Vital signs** |
| **`Composition.section.section.entry`** | **Reference ke resource `Observation` (hasil pemeriksaan tanda-tanda vital, tingkat kesadaran, dan antropometri)** |
| **b. Pemeriksaan Fisik *Head to Toe*** | |
| **`Composition.section.section.title`** | ***Pemeriksaan Fisik Head to Toe*** |
| **`Composition.section.section.code.coding.system`** | **<http://loinc.org>** |
| **`Composition.section.section.code.coding.code`** | **10187-3** |
| **`Composition.section.section.code.coding.display`** | **Review of systems Narrative - Reported** |
| **`Composition.section.section.entry`** | **Reference ke resource `Observation` (hasil pemeriksaan fisik *head to toe*)** |
| **3. Pemeriksaan Fungsional** | |
| **`Composition.section.title`** | ***Pemeriksaan Fungsional*** |
| **`Composition.section.code.coding.system`** | **<http://loinc.org>** |
| **`Composition.section.code.coding.code`** | **47420-5** |
| **`Composition.section.code.coding.display`** | **Functional status assessment note** |
| **`Composition.section.entry`** | **Reference ke resource `Observation` (status psikologis)** |
| **4. Perencanaan Perawatan** | |
| **`Composition.section.title`** | ***Perencanaan Perawatan*** |
| **`Composition.section.code.coding.system`** | **<http://loinc.org>** |
| **`Composition.section.code.coding.code`** | **18776-5** |
| **`Composition.section.code.coding.display`** | **Plan of care note** |
| **`Composition.section.entry`** | **Reference ke resource `ClinicalImpression`, `Goal`, `CarePlan` (riwayat perjalanan penyakit, tujuan perawatan, rencana rawat, serta instruksi medik dan keperawatan)** |
| **5. Pemeriksaan Penunjang** | |
| **`Composition.section.title`** | ***Pemeriksaan Penunjang*** |
| **`Composition.section.code.coding.system`** | **<http://terminology.kemkes.go.id>** |
| **`Composition.section.code.coding.code`** | **TK000009** |
| **`Composition.section.code.coding.display`** | **Hasil Pemeriksaan Penunjang** |
| **a. Pemeriksaan Laboratorium** | |
| **`Composition.section.section.title`** | ***Hasil Pemeriksaan Laboratorium*** |
| **`Composition.section.section.code.coding.system`** | **<http://loinc.org>** |
| **`Composition.section.section.code.coding.code`** | **11502-2** |
| **`Composition.section.section.code.coding.display`** | **Laboratory report** |
| **`Composition.section.section.entry`** | **Reference ke resource `ServiceRequest`, `Procedure`, `Specimen`, `Observation`, `DiagnosticReport` (permintaan, status puasa, spesimen, hasil, dan laporan pemeriksaan penunjang)** |
| **b. Pemeriksaan Radiologi** | |
| **`Composition.section.section.title`** | ***Hasil Pemeriksaan Radiologi*** |
| **`Composition.section.section.code.coding.system`** | **<http://loinc.org>** |
| **`Composition.section.section.code.coding.code`** | **18782-3** |
| **`Composition.section.section.code.coding.display`** | **Radiology Study observation (narrative)** |
| **`Composition.section.section.entry`** | **Reference ke resource `ServiceRequest`, `Observation`, `Procedure`, `AllergyIntolerance`, `Observation` dan `DiagnosticReport`(permintaan, status puasa, status kehamilan, status alergi bahan kontras, hasil, dan laporan pemeriksaan penunjang radiologi)** |
| **6. Diagnosis** | |
| **`Composition.section.title`** | ***Diagnosis*** |
| **`Composition.section.code.coding.system`** | **<http://terminology.kemkes.go.id>** |
| **`Composition.section.code.coding.code`** | **TK000004** |
| **`TK000004`** | **Diagnosis** |
| **a. Diagnosis Awal** | |
| **`Composition.section.section.title`** | ***Diagnosis Awal*** |
| **`Composition.section.section.code.coding.system`** | **<http://loinc.org>** |
| **`Composition.section.section.code.coding.code`** | **42347-5** |
| **`Composition.section.section.code.coding.display`** | **Admission diagnosis (narrative)** |
| **`Composition.section.section.entry`** | **Reference ke resource `Condition` (diagnosis masuk)** |
| **b. Diagnosis Akhir** | |
| **`Composition.section.section.title`** | ***Diagnosis Akhir*** |
| **`Composition.section.section.code.coding.system`** | **<http://loinc.org>** |
| **`Composition.section.section.code.coding.code`** | **78375-3** |
| **`Composition.section.section.code.coding.display`** | **Discharge diagnosis Narrative** |
| **`Composition.section.section.entry`** | **Reference ke resource `ClinicalImpression`, `Condition`, `RiskAssessment` (rasional klinis, diagnosis akhir, dan penilaian risiko)** |
| **7. Tindakan/Prosedur Medis** | |
| **`Composition.section.title`** | ***Tindakan/Prosedur Medis*** |
| **`Composition.section.code.coding.system`** | **<http://terminology.kemkes.go.id>** |
| **`Composition.section.code.coding.code`** | **TK000005** |
| **`Composition.section.code.coding.display`** | **Tindakan/Prosedur Medis** |
| **`Composition.section.entry`** | **Reference ke resource `ServiceRequest`, `Procedure`, `Observation` (permintaan tindakan/ prosedur medis, pelaksanaan dan hasilnya)** |
| **8. Farmasi** | |
| **`Composition.section.title`** | ***Farmasi*** |
| **`Composition.section.code.coding.system`** | **<http://terminology.kemkes.go.id>** |
| **`Composition.section.code.coding.code`** | **TK000013** |
| **`Composition.section.code.coding.display`** | **Obat** |
| **a. Obat Saat Kunjungan** | |
| **`Composition.section.section.title`** | ***Obat Saat Kunjungan*** |
| **`Composition.section.section.code.coding.system`** | **<http://loinc.org>** |
| **`Composition.section.section.code.coding.code`** | **42346-7** |
| **`Composition.section.section.code.coding.display`** | **Medications on admission (narrative)** |
| **`Composition.section.section.entry`** | **Reference ke resource `MedicationRequest`, `MedicationDispense`, `MedicationAdministration` (peresapan, pengeluaran, dan pemberian obat)** |
| **b. Obat Pulang** | |
| **`Composition.section.section.title`** | ***Obat Pulang*** |
| **`Composition.section.section.code.coding.system`** | **<http://loinc.org>** |
| **`Composition.section.section.code.coding.code`** | **75311-1** |
| **`Composition.section.section.code.coding.display`** | **Discharge medications Narrative** |
| **`Composition.section.section.entry`** | **Reference ke resource `MedicationRequest`, `MedicationDispense` (peresepan dan pengeluaran obat)** |
| **9. Diet** | |
| **`Composition.section.title`** | ***Diet*** |
| **a. Rekomendasi Diet** | |
| **`Composition.section.section.title`** | ***Rekomendasi Diet*** |
| **`Composition.section.code.coding.system`** | **<http://loinc.org>** |
| **`Composition.section.code.coding.code`** | **42344-2** |
| **`Composition.section.code.coding.display`** | **Discharge diet (narrative)** |
| **`Composition.section.section.entry`** | **Reference ke resource `NutritionOrder`(Diet dengan intent *proposal*)** |
| **b. Diet yang Diberikan** | |
| **`Composition.section.section.title`** | ***Diet yang diberikan*** |
| **`Composition.section.code.coding.system`** | **<http://loinc.org>** |
| **`Composition.section.code.coding.code`** | **61144-2** |
| **`Composition.section.code.coding.display`** | **Diet and nutrition Narrative** |
| **`Composition.section.section.entry`** | **Reference ke resource `NutritionOrder` (diet dengan intent *order*)** |
| **10. Edukasi** | |
| **`Composition.section.title`** | ***Edukasi*** |
| **`Composition.section.code.coding.system`** | **<http://loinc.org>** |
| **`Composition.section.code.coding.code`** | **34895-3** |
| **`Composition.section.code.coding.display`** | **Education note** |
| **`Composition.section.entry`** | **Reference ke resource `Procedure` (edukasi)** |
| **11. Kondisi Saat Meninggalkan Rumah Sakit** | |
| **`Composition.section.title`** | ***Kondisi Saat Meninggalkan Rumah Sakit*** |
| **`Composition.section.code.coding.system`** | **<http://loinc.org>** |
| **`Composition.section.code.coding.code`** | **10184-0** |
| **`Composition.section.code.coding.display`** | **Hospital discharge physical findings Narrative** |
| **`Composition.section.entry`** | **Referensi ke *resource* `ClinicalImpression`, `Condition` (prognosis dan kondisi saat meninggalkan rumah sakit)** |
| **12. Rencana Tindak Lanjut** | |
| **`Composition.section.title`** | ***Rencana Tindak Lanjut*** |
| **`Composition.section.code.coding.system`** | **<http://loinc.org>** |
| **`Composition.section.code.coding.code`** | **8653-8** |
| **`Composition.section.code.coding.display`** | **Hospital Discharge instructions** |
| **`Composition.section.entry`** | **Referensi ke *resource* `Observation`, `CarePlan`, `ServiceRequest` (perencanaan pemulangan, rencana tindak lanjut dan instruksi untuk tindak lanjut)** |
| **13. Perjalanan Kunjungan Pasien** | |
| **`Composition.section.title`** | ***Perjalanan Kunjungan Pasien*** |
| **`Composition.section.code.coding.system`** | **<http://loinc.org>** |
| **`Composition.section.code.coding.code`** | **8648-8** |
| **`Composition.section.code.coding.display`** | **Hospital course Narrative** |
| **`Composition.section.text.status`** | ***generated*** |
| **`Composition.section.text.div`** | **Tipe data *string*** |

---

[1](#_footnoteref_1). Permenkes Nomor 12 Tahun 2013 tentang Pola Tarif Tarif Badan Layanan Umum Rumah Sakit di Lingkungan Kementerian Kesehatan

[2](#_footnoteref_2). Peraturan Menteri Kesehatan Nomor 71 Tahun 2013 tentang Pelayanan Kesehatan pada Jaminan Kesehatan Nasional

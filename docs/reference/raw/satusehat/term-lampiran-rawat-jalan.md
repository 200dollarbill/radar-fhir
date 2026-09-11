---
id: term-lampiran-rawat-jalan
title: Lampiran Terminologi Resume Medis Rawat Jalan
source_url: https://satusehat.kemkes.go.id/platform/docs/id/terminology/lampiran-terminologi/rme-rawat-jalan1/
group: satusehat
fhir_version: R4
fetched_at: '2026-09-11T13:21:42Z'
sha256: 9bf1017cb8803dfc321a32c065ba5fa6a33359cee8107adfd174cc5b6588f673
---
# Lampiran Terminologi Resume Medis Rawat Jalan

## Struktur Kamus KFA

![Struktur Kamus KFA](../../_images/struktur-kamus-kfa.png)

Gambar 1. Struktur Kamus KFA

Tabel 1. Deskripsi Bahan Zat Aktif

| Deskripsi | Bahan Zat Aktif |
| --- | --- |
| Tag (singkatan) | BZA |
| Format kode (numbering/ digit) | 91xxxxxx |
| Tata cara penamaan | Nama Molekul Kimia |
| Contoh penulisan penamaan | Paracetamol |
| Atribut | - Satuan ukur (UCUM) - Referensi Kode dari Sumber Lain **mis.** PubChem, CAS, ATC |

Tabel 2. Deskripsi Bahan Zat Aktif

| Deskripsi | Produk Obat Virtual |
| --- | --- |
| Tag (singkatan) | POV |
| Format kode (numbering/ digit) | 92xxxxxx |
| Tata cara penamaan | Zat Aktif + Kekuatan + Satuan + Bentuk Sediaan |
| Contoh penulisan penamaan | Paracetamol 500 mg Tablet |
| Atribut | - Zat Aktif - Kekuatan - Satuan Kekuatan (UCUM) - Satuan Produk (unit terkecil) - Golongan Obat - Bentuk Sediaan - Kelas Terapi (5 Level ATC - WHO) |

Tabel 3. Deskripsi Bahan Zat Aktif

| Deskripsi | Produk Obat Aktual |
| --- | --- |
| Tag (singkatan) | POA |
| Format kode (numbering/ digit) | 93xxxxxx |
| Tata cara penamaan | Zat Aktif + Kekuatan + Satuan + Bentuk Sediaan + (Merek Dagang) |
| Contoh penulisan penamaan | Paracetamol 500 mg Tablet (Panadol) |
| Atribut | - Semua atribut di POV - Nama Dagang - Eksipien - Formula Nasional - Program Kesehatan - Tayang LKPP - Produksi buatan (impor / lokal) - TKDN - Skor TKDN - Skor BMP - Referensi Kode dari Sumber lain **mis.** BPOM, LKPP |

## Pemetaan Perubahan Kode Resume Medis Rawat Jalan

### Variabel Prognosis

Tabel 4. Prognosis

| Value Set | ClinicalImpression.prognosisCodeableConcept[i].coding.system | ClinicalImpression.prognosisCodeableConcept[i].coding.code | ClinicalImpression.prognosisCodeableConcept[i].coding.display | Versi |
| --- | --- | --- | --- | --- |
| 1. Baik; | <http://terminology.kemkes.go.id/CodeSystem/clinical-term> | PR000001 | Prognosis baik | Versi 1.2 |
| <http://snomed.info/sct> | 170968001 | Prognosis good | Versi 2.0 |
| 2. Dubia et bonam / cenderung baik; | <http://terminology.kemkes.go.id/CodeSystem/clinical-term> | PR000002 | Prognosis dubia et bonam / cenderung baik | Versi 1.2 |
| <http://snomed.info/sct> | 65872000 | Fair prognosis | Versi 2.0 |
| 3. Dubia et malam / cenderung tidak baik; | <http://terminology.kemkes.go.id/CodeSystem/clinical-term> | PR000003 | Prognosis dubia et malam / cenderung tidak baik | Versi 1.2 |
| <http://snomed.info/sct> | 67334001 | Guarded prognosis | Versi 2.0 |
| 4. Tidak baik | <http://terminology.kemkes.go.id/CodeSystem/clinical-term> | PR000004 | Prognosis tidak baik | Versi 1.2 |
| <http://snomed.info/sct> | 170969009 | Prognosis bad | Versi 2.0 |

### Variabel Kondisi Saat Meninggalkan Rumah Sakit

Tabel 5. Kondisi Saat Meninggalkan Rumah Sakit

| Value Set | Condition.code.coding.system | Condition.code.coding.code | Condition.code.coding.display | Versi |
| --- | --- | --- | --- | --- |
| 1. Stabil; | <http://terminology.kemkes.go.id/CodeSystem/clinical-term> | MN000001 | Stabil | Versi 1.2 |
| <http://snomed.info/sct> | 359746009 | Patient’s condition stable | Versi 2.0 |
| 2. Tidak stabil; | <http://terminology.kemkes.go.id/CodeSystem/clinical-term> | MN000002 | Tidak stabil | Versi 1.2 |
| <http://snomed.info/sct> | 162668006 | Patient’s condition unstable | Versi 2.0 |
| 3. Perbaikan; | <http://terminology.kemkes.go.id/CodeSystem/clinical-term> | MN000003 | Perbaikan | Versi 1.2 |
| <http://snomed.info/sct> | 268910001 | Patient’s condition improved | Versi 2.0 |

### Variabel Tingkat kesadaran

Tabel 6. Tingkat kesadaran

| Value Set | Observation.code.coding.system | Observation.code.coding.code | Observation.code.coding.display | Versi |
| --- | --- | --- | --- | --- |
| 1. Sadar Baik/Alert : 0 | <http://terminology.kemkes.go.id/CodeSystem/clinical-term> | TK000001 | Alert | Versi 1.2 |
| <http://snomed.info/sct> | 248234008 | Mentally alert | Versi 2.0 |
| 2. Berespon dengan kata-kata/Voice : 1 | <http://terminology.kemkes.go.id/CodeSystem/clinical-term> | TK000002 | Voice | Versi 1.2 |
| <http://snomed.info/sct> | 300202002 | Response to voice | Versi 2.0 |
| 3. Hanya berespons jika dirangsang nyeri/pain : 2 | <http://terminology.kemkes.go.id/CodeSystem/clinical-term> | TK000003 | Pain | Versi 1.2 |
| <http://snomed.info/sct> | 450847001 | Response to pain | Versi 2.0 |
| 4. Pasien tidak sadar/unresponsive : 3 | <http://terminology.kemkes.go.id/CodeSystem/clinical-term> | TK000004 | Unresponsive | Versi 1.2 |
| <http://snomed.info/sct> | 422768004 | Unresponsive | Versi 2.0 |
| 5. Gelisah atau bingung : 4 | <http://terminology.kemkes.go.id/CodeSystem/clinical-term> | TK000005 | Gelisah | Versi 1.2 |
| <http://snomed.info/sct> | 130987000 | Acute confusion | Versi 2.0 |
| 6. Acute Confusional States : 5 | <http://terminology.kemkes.go.id/CodeSystem/clinical-term> | TK000006 | Acute Confusional States | Versi 1.2 |
| <http://snomed.info/sct> | 2776000 | Delirium | Versi 2.0 |

### Variabel Rencana Tindak Lanjut / Cara Keluar dari Rumah Sakit

Tabel 7. Rencana Tindak Lanjut / Cara Keluar dari Rumah Sakit

| Value Set | ServiceRequest.code.coding.system | ServiceRequest.code.coding.code | ServiceRequest.code.coding.display | Versi |
| --- | --- | --- | --- | --- |
| 4. Rawat inap; | <http://terminology.kemkes.go.id/CodeSystem/clinical-term> | TL000001 | Rawat inap | Versi 1.2 |
| <http://snomed.info/sct> | 737481003 | Inpatient care management | Versi 2.0 |

### Variabel Edukasi

Tabel 8. Edukasi

| Value Set | Procedure.code.coding.system | Procedure.code.coding.code | Procedure.code.coding.display | Versi |
| --- | --- | --- | --- | --- |
| 1. Proses penyakit, diagnosis, dan rencana asuhan; | <http://terminology.kemkes.go.id/CodeSystem/clinical-term> | ED000001 | Edukasi Proses penyakit, diagnosis, dan rencana asuhan; | Versi 1.2 |
| <http://snomed.info/sct> | 84635008 | Disease process or condition education | Versi 2.0 |
| 2. Obat-obatan; | <http://terminology.kemkes.go.id/CodeSystem/clinical-term> | ED000002 | Edukasi obat-obatan | Versi 1.2 |
| <http://snomed.info/sct> | 967006 | Medication education | Versi 2.0 |
| 3. Rehabilitasi medis; | <http://terminology.kemkes.go.id/CodeSystem/clinical-term> | ED000003 | Edukasi Rehabilitasi Medis | Versi 1.2 |
| <http://snomed.info/sct> | 410082002 | Rehabilitation therapy education | Versi 2.0 |
| 4. Manajemen nyeri; | <http://terminology.kemkes.go.id/CodeSystem/clinical-term> | ED000004 | Edukasi Manajemen Nyeri | Versi 1.2 |
| <http://snomed.info/sct> | 712651001 | Education about pain | Versi 2.0 |
| 5. Gizi; | <http://terminology.kemkes.go.id/CodeSystem/clinical-term> | ED000005 | Edukasi Gizi | Versi 1.2 |
| <http://snomed.info/sct> | 61310001 | Nutrition education | Versi 2.0 |
| 6. Cuci tangan; | <http://terminology.kemkes.go.id/CodeSystem/clinical-term> | ED000006 | Edukasi Cuci Tangan | Versi 1.2 |
| <http://snomed.info/sct> | 698608004 | Hand washing education | Versi 2.0 |
| 7. Penggunaan alat medis; | <http://terminology.kemkes.go.id/CodeSystem/clinical-term> | ED000007 | Edukasi Penggunaan Alat Medis | Versi 1.2 |
| <http://snomed.info/sct> | 362978005 | Medical equipment or device education (procedure) | Versi 2.0 |

## Matriks Skenario Peresepan dan Pengeluaran Obat

```
Keterangan : +
* NC : Non-compound (non racikan)
* SD : Give of such doses (dtd)
* EP : Divide into equal part (tablet dipecah).
```

Tabel 9. Matriks Skenario Peresepan dan Pengeluaran Obat

| Use Case | Medication.code MedicationRequest | Medication.ingredient MedicationRequest | MedicationRequest | Medication.code MedicationDispense | Medication.ingredient MedicationDispense | MedicationDispense (Instruction) | Valid/Invalid |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Obat Pakem Tunggal (NC) | R/ Paracetamol 500 mg | | | | | | |
| 93xxx | - | - | 93xxx | - |  | Valid |
| 92xxx | - | - | 93xxx | - |  | Valid (Dengan ketentuan kode 93 untuk Medication.code MedicationDispense sebaiknya merupakan turunan dari kode 92 di Medication.code MedicationRequest) |
| 91xxx | - | - | 93xxx | - |  | Invalid |
| Racikan Non-dtd (EP) | - R/ Paracetamol 500 mg 10 tab - Vitamin B6 10mg 10 tab - Dibuat 30 kapsul | | | | | | |
| - | Paracetamol:  - Medication.ingredient.itemCodeableConcept → 93xxx - Medication.ingredient.strength.num : 10/tab - Medication.ingredient.strength.denominator : 30/kap | MedicationRequest.dispenseRequest.quantity → 30 | - | - Medication.ingredient.itemCodeableConcept → 93xxx - Medication.ingredient.strength.numerator : 10/tab - Medication.ingredient.strength.denominator : 30/kap | MedicationDispense.quantity → 30 | Valid |
| - | Vitamin B6:\  - Medication.ingredient.itemCodeableConcept→ 92xxx - Medication.ingredient.strength.numerator: 10/tab - Medication.ingredient.strength.denominator: 30/kap | MedicationRequest.dispenseRequest.quantity → 30 | - | - Medication.ingredient.itemCodeableConcept→ 93xxx - Medication.ingredient.strength.numerator: 10/tab - Medication.ingredient.strength.denominator: 30/kap | MedicationDispense.quantity → 30 | Valid |
| Racikan dtd (SD/ tidak ada sisa) | - R/ Paracetamol 125 mg/ kapsul > perlu 5 tab (20 kapsul x 125 / 500mg) - Vitamin B6 20 mg/ kapsul > perlu 40 tab (20 kapsul x 20 / 10mg) - Dibuat 20 kapsul | | | | | | |
| - | Paracetamol:  - Medication.ingredient.itemCodeableConcept→ 91xxx - Medication.ingredient.strength.numerator: 125/mg - Medication.ingredient.strength.denominator: 1/kap | MedicationRequest.dispenseRequest.quantity → 20 | - | - Medication.ingredient.itemCodeableConcept→ 93xxx - Medication.ingredient.strength.numerator: 5/tab - Medication.ingredient.strength.denominator: 20/kap | MedicationDispense.quantity → 20 | Valid |
| - | Vitamin B6:  - Medication.ingredient.itemCodeableConcept→ 91xxx - Medication.ingredient.strength.numerator: 20/mg - Medication.ingredient.strength.denominator: 1/kap | MedicationRequest.dispenseRequest.quantity → 20 | - | - Medication.ingredient.itemCodeableConcept→ 93xxx - Medication.ingredient.strength.numerator: 40/tab - Medication.ingredient.strength.denominator: 20/kap | MedicationDispense.quantity → 20 | Valid |
| Racikan dtd (SD/ ada sisa) |  |  |  |  |  |  |  |
| Narkotika | - R/ Morphine Hydrochloride 3 mg > perlu 7.5 tab (25 kapsul x 3 / 10mg) - Diazepam 1 mg Tablet > perlu 12,5 tab (25 kapsul x 1 / 2mg) - Dibuat 25 kapsul | | | | | | |
| - | Morphine Hydrochloride  - Medication.ingredient.itemCodeableConcept→ 91xxx - Medication.ingredient.strength.numerator: 3/mg - Medication.ingredient.strength.denominator: 1/tab | MedicationRequest.dispenseRequest.quantity → 25 | - | - Medication.ingredient.itemCodeableConcept→ 93xxx - Medication.ingredient.strength.numerator: 7,5/tab - Medication.ingredient.strength.denominator: 25/kapsul | MedicationDispense.quantity → 25 | Valid (Penulisan di Medication.ingredient.strength.numerator Medication Dispense sesuai yaitu 7.5tab, tidak dilakukan pembulatan) |
| - | Diazepam  - Medication.ingredient.itemCodeableConcept→ 91xxx - Medication.ingredient.strength.numerator: 3/mg - Medication.ingredient.strength.denominator: 1/tab | MedicationRequest.dispenseRequest.quantity → 25 | - | - Medication.ingredient.itemCodeableConcept→ 93xxx - Medication.ingredient.strength.numerator: 12,5/tab - Medication.ingredient.strength.denominator: 25/kapsul | MedicationDispense.quantity → 25 | Valid (Penulisan di Medication.ingredient.strength.numerator Medication Dispense sesuai yaitu 12.5tab, tidak dilakukan pembulatan) |
| Non-Narkotika | - R/ Paracetamol 125 mg/ kapsul > perlu 7.5 tab (30 kapsul x 125 /500mg) - Vitamin B6 12,5 mg/ kapsul > perlu 37,5 tab (30 kapsul x 12,5 / 10mg) - Dibuat 30 kapsul | | | | | | |
| - | Paracetamol:  - Medication.ingredient.itemCodeableConcept→ 91xxx - Medication.ingredient.strength.numerator: 125/mg - Medication.ingredient.strength.denominator: 1/tab | MedicationRequest.dispenseRequest.quantity → 30 | - | - Medication.ingredient.itemCodeableConcept→ 93xxx - Medication.ingredient.strength.numerator: 8/tab - Medication.ingredient.strength.denominator: 30/kapsul | MedicationDispense.quantity → 30 | Valid (Penulisan di Medication.ingredient.strength.numerator Medication Dispense adalah pembulatan ke atas yaitu dari 7.5 tab menjadi 8tab, tetapi yang digunakan tetap 7,5tab) |
| - | Vitamin B6:  - Medication.ingredient.itemCodeableConcept→ 91xxx - Medication.ingredient.strength.numerator: 12.5/mg - Medication.ingredient.strength.denominator: 1/tab | MedicationRequest.dispenseRequest.quantity → 30 | - | - Medication.ingredient.itemCodeableConcept→ 93xxx - Medication.ingredient.strength.numerator: 37.5/tab - Medication.ingredient.strength.denominator: 30/kap | MedicationDispense.quantity → 30 | Valid (Penulisan di Medication.ingredient.strength.numerator Medication Dispense adalah pembulatan ke atas yaitu dari 37.5 tab menjadi 38tab, tetapi yang digunakan tetap 37,5tab) |
| Obat Minum (NC tidak sisa) | - R/ Paracetamol 120 mg/5 mL Sirup - Paracetamol 5 ml diminum 4-6 jam sekali bila demam selama 24 hari | | | | | | |
| 93xxx | Paracetamol Sirup  - Medication.ingredient.itemCodeableConcept → 91xxx - Medication.ingredient.strength.numerator : 120 mg - Medication.ingredient.strength.denominator : 5mL | - | 93xxx | Paracetamol Sirup  Medication.ingredient.itemCodeableConcept → 91xxx \* Medication.ingredient.strength.numerator : 120 mg \* Medication.ingredient.strength.denominator : 5mL | - | Valid |
| 92xxx | Paracetamol Sirup  - Medication.ingredient.itemCodeableConcept → 91xxx - Medication.ingredient.strength.numerator : 120 mg - Medication.ingredient.strength.denominator : 5mL | - | 93xxx | Paracetamol Sirup  - Medication.ingredient.itemCodeableConcept → 91xxx - Medication.ingredient.strength.numerator : 120 mg - Medication.ingredient.strength.denominator : 5mL | - | Valid |
| Obat Minum (NC sisa) | - R/ Paracetamol 120 mg/5 mL Sirup - Paracetamol 5 ml diminum 4-6 jam sekali bila demam selama 30 hari - 1 botol 60 ml maka diperlukan 5mlx30 / 60ml = 2.5 | | | | | | |
|  | 93xxx | Paracetamol Sirup  - Medication.ingredient.itemCodeableConcept → 91xxx - Medication.ingredient.strength.numerator : 120 mg - Medication.ingredient.strength.denominator : 5mL | - | 93xxx | Paracetamol Sirup  - Medication.ingredient.itemCodeableConcept → 91xxx - Medication.ingredient.strength.numerator : 120 mg - Medication.ingredient.strength.denominator : 5mL | - | Valid (Perlu catatan dari dokter obatnya harus dihabiskan atau tidak) |
| 92xxx | Paracetamol Sirup  - Medication.ingredient.itemCodeableConcept → 91xxx - Medication.ingredient.strength.numerator : 120 mg - Medication.ingredient.strength.denominator : 5mL | - | 93xxx | Paracetamol Sirup  - Medication.ingredient.itemCodeableConcept → 91xxx - Medication.ingredient.strength.numerator : 120 mg - Medication.ingredient.strength.denominator : 5mL | - | Valid |
| Obat Suntik (NC tidak sisa) | - R/ Insulin Human Analog (Rapid Acting) 100 IU/mL Injeksi (NOVORAPID, 3 mL) - Suntik 3 kali sehari 10 Unit sebelum makan selama 30 hari - perlu 3 cartridge (100IU/ml x 3 mL / (3x10IU) = 10 hari 1 cartridge - 30 hari maka perlu 30/10 = 3 cartridge | | | | | | |
|  | 93xxx | Insulin Human Analog:  - Medication.ingredient.itemCodeableConcept→ 91xxx - Medication.ingredient.strength.numerator: 100[U] - Medication.ingredient.strength.denominator: 1/mL | - | 93xxx | Insulin Human Analog :  - Medication.ingredient.itemCodeableConcept→ 91xxx - Medication.ingredient.strength.numerator: 3/cartridge - Medication.ingredient.strength.denominator: 9/mL | - | Valid |
| 92xxx | Insulin Human Analog:  - Medication.ingredient.itemCodeableConcept→ 91xxx - Medication.ingredient.strength.numerator: 100[U] - Medication.ingredient.strength.denominator: 1/mL | - | 93xxx | Insulin Human Analog :  - Medication.ingredient.itemCodeableConcept→ 91xxx - Medication.ingredient.strength.numerator: 3/cartridge - Medication.ingredient.strength.denominator: 9/mL | - | Valid |
| Obat Suntik (NC sisa) | - R/ Insulin Human Analog (Rapid Acting) 100 IU/mL Injeksi (NOVORAPID, 3 mL) - Suntik 3 kali sehari 8 Unit sebelum makan selama 30 hari - perlu 3 cartridge (100IU/ml x 3 mL / (3x8IU) = 12,5 hari 1 cartridge - 30 hari maka perlu 30/12.5= 2.4 cartridge | | | | | | |
|  | 93xxx | Insulin Human Analog:  - Medication.ingredient.itemCodeableConcept→ 91xxx - Medication.ingredient.strength.numerator: 100[U] - Medication.ingredient.strength.denominator: 1/mL | - | 93xxx | Insulin Human Analog :  - Medication.ingredient.itemCodeableConcept→ 91/xxx - Medication.ingredient.strength.numerator: 2.4 cartridge - Medication.ingredient.strength.denominator: 7.2/mL | - | Valid (Perlu catatan dari dokter obatnya harus dihabiskan atau tidak) |
| 92xxx | Insulin Human Analog:  - Medication.ingredient.itemCodeableConcept→ 91xxx - Medication.ingredient.strength.numerator: 100[U] - Medication.ingredient.strength.denominator: 1/mL | - | 93xxx | Insulin Human Analog :  - Medication.ingredient.itemCodeableConcept→ 91/xxx - Medication.ingredient.strength.numerator: 2.4 cartridge - Medication.ingredient.strength.denominator: 7.2/mL | - | Valid |

## Alur Pengiriman DICOM pada Fasilitas Pelayanan Kesehatan Yang Memiliki MWL

![Alur Pengiriman DICOM](../../_images/alur-dicom-rs.svg)

Gambar 2. Alur Pengiriman DICOM

## Alur Pengiriman DICOM pada Fasilitas Pelayanan Kesehatan Yang Tidak Memiliki MWL

![Alur Pengiriman DICOM](../../_images/alur-dicom-puskes.svg)

Gambar 3. Alur Pengiriman DICOM

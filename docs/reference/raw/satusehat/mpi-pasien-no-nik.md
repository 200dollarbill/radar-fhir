---
id: mpi-pasien-no-nik
title: MPI Pasien tanpa NIK
source_url: https://satusehat.kemkes.go.id/platform/docs/id/master-data/master-patient-index/pasien-no-nik/
group: satusehat
fhir_version: R4
fetched_at: '2026-09-11T13:21:49Z'
sha256: a553b614fba4d7805defec69f585d4f123f63053914ccc391187dd5194f349cb
---
# Pasien tanpa NIK

### 1. Ruang Lingkup

**Pasien tanpa NIK** akan memiliki proses sebagai berikut:

- Get Patient Data.

#### 1.1. Persyaratan Data Minimum

Berikut ini persyaratan data minimum untuk pasien tanpa NIK:

|  |  |
| --- | --- |
|  | Setiap terdapat simbol asterik `*` sebelum nama variabel atau parameter yang disebutkan, maka variabel atau parameter tersebut bersifat **WAJIB** , **harus ada**, atau **pasti selalu ada**, contoh: `*variabel`. |

Tabel 1. Persyaratan data minimum pasien tanpa NIK

| Data Point | Keterangan |
| --- | --- |
| `*name` | Berisi nama, baik sebagian atau lengkap, dari pasien yang akan dicari.  Contoh: `Budi` |
| `*birthDate` | Berisi tanggal lahir dengan format salah satu dari `YYYY`, `YYYY-MM`, atau `YYYY-MM-DD`.  Contoh: `1976-01-06` |
| `*gender` | Berisi jenis kelamin dari pasien, terdiri dari `male` (laki-laki)/ `female` (perempuan). |

|  |  |
| --- | --- |
|  | Setiap data harus unik / **TIDAK BOLEH** terdapat duplikasi |

### 2. Alur Mendapatkan Data

fasyankes dapat memperoleh data pasien tanpa menggunakan NIK di SATUSEHAT, dengan menggunakan opsi berikut:

Tabel 1. Alur mendapatkan data

| Options | Approach |
| --- | --- |
| Option 1: Gunakan `Nama Lengkap`, `Tanggal Lahir`, serta `Jenis Kelamin` dari Pasien. | **Nama Lengkap Pasien:**  - Pencarian nama pasien menggunakan *similar case*. - Dimana ketentuan jumlah minimum pencarian berdasarkan karakter adalah **TIDAK BOLEH** kurang dari tiga karakter. |
| **Tanggal Lahir Pasien:**  - Pencarian dengan tanggal lahir dari pasien sesuai KTP/NIK, dengan format : `YYYY-MM-DD` dimana bersifat *exact*/akurat/tepat/persis (**TIDAK BOLEH** di luar ketentuan). |
| **Jenis Kelamin Pasien:**  - Pencarian dengan jenis kelamin dari pasien, hanya terdiri dari `male`, dan `female` dimana bersifat *exact*/akurat/tepat/persis (**TIDAK BOLEH** di luar ketentuan) |

Tabel 2. Informasi yang akan dikirim kembali ke APIGEE (Response JSON)

| Parameter | Tipe Data | Keterangan |
| --- | --- | --- |
| `identifier` | `string` | Hanya akan menampilkan IHS Number patient. |
| `name` | `string` | Nama pasien. |
| `gender` | `string` | Jenis kelamin pasien: `male` (laki-laki) / `female` (perempuan) |
| `birthdate` | `date` | Tanggal lahir pasien.  Contoh: `1976-01-06` (`YYYY-MM-DD`) |
| `multipleBirthInteger` | `int` | Urutan kelahiran, untuk pasien lahir kembar. Jika bukan kelahiran kembar, maka terisi dengan angka `0`. |
| `address` | `string` | Alamat pasien (ditampilkan dengan masking). |
| `maritalStatus` | `string` | Status pasien: `Married` / `unmarried`. |

---
id: mpi-pasien-nik
title: MPI Pasien dengan NIK
source_url: https://satusehat.kemkes.go.id/platform/docs/id/master-data/master-patient-index/pasien-nik/
group: satusehat
fhir_version: R4
fetched_at: '2026-09-11T13:21:47Z'
sha256: fbaba2de73a3f44f37c344106005a8eec39cf9f259dd2ad0f1e94689cd021974
---
# Pasien dengan NIK

## 1. Ruang Lingkup

**Pasien dengan NIK** akan memiliki proses sebagai berikut:

- Create Patient Data.
- Get Patient Data.
- Update/Patch Patient Data.

### 1.1. Persyaratan Data Minimum

Berikut ini persyaratan data minimum untuk pasien baru dengan NIK:

|  |  |
| --- | --- |
|  | Setiap terdapat simbol asterik `*` sebelum nama variabel atau parameter yang disebutkan, maka variabel atau parameter tersebut bersifat **WAJIB** , **harus ada**, atau **pasti selalu ada**, contoh: `*variabel`. |

Tabel 1. Persyaratan data minimum pasien baru dengan NIK

| Data Point | Keterangan |
| --- | --- |
| `*identifier` | Identitas yang digunakan oleh Pasien, saat ini Identitas yang dapat digunakan yaitu: NIK (`nik`) |
| `*name` | Nama lengkap pasien sesuai KTP/NIK yang diberikan di fasyankes. |
| `*birthDate` | Tanggal Lahir dari Pasien sesuai KTP/NIKi. dengan format: `YYYY-MM-DD` |
| `birthPlace` | Digunakan untuk menyimpan informasi Tempat lahir dari Pasien, sesuai standar penulisan NIK/KTP |
| `*gender` | Jenis Kelamin dari Pasien, terdiri dari `male`, dan `female` |
| `Nomor Kartu Keluarga` | Nomor administrasi keluarga yang diterbitkan DUKCAPIL |
| `*address` | Alamat pasien sesuai dengan KTP/NIK, informasi alamat terdiri dari komponen:  - `use` - peruntukan alamat dalam hal ini menggunakan rumah atau `home` - `line` - alamat lengkap sesuai KTP/NIK - `city` - nama kota - `postalCode` - kode pos - `country` - negara, dalam hal ini menggunakan `ID` - `extension` - penerapan kode administratif wilayah |
| `*address-extension` | Digunakan untuk memuat informasi kode administratif wilayah dari alamat pasien sesuai NIK/KTP, yang terdiri dari:  - `province` - Kode Provinsi - `city` - Kode Kab/Kota - `district` - Kode Kecamatan - `village` - Kode Desa/Kelurahan - `rt` - Nomor RT - `rw` - Nomor RW  Kode administratif mengacu ke kode wilayah kemendagri. Daftar kode wilayah terbaru dapat didapatkan di tautan berikut [Kode Wilayah KEMENDAGRI](https://docs.google.com/spreadsheets/d/13F87ScHgEikqYgv65ZAU1vsRLmXNFo1i/edit?usp=sharing&ouid=116173098464208547917&rtpof=true&sd=true) |
| `telecom` | Digunakan untuk menyimpan informasi kontak pasien yang dapat dihubungi seperti telepon atau *email* |
| `maritalStatus` | Digunakan untuk menyimpan informasi status pernikahan dari Pasien, seperti:  - `S` - Never Married - `M` - Married - `W` - Widowed - `D` - Divorced |
| `citizenshipStatus` | Digunakan untuk menyimpan informasi status kewarganegaraan, dalam hal ini `WNI` atau `WNA`\*  - WNA yang dapat didaftarkan adalah WNA yang mempunyai NIK dan KTP elektronik |
| `communication-language` | Mengindikasikan bahasa yang digunakan pasien untuk berkomunikasi sehari-hari, kodifikasi bahasa menggunakan [BCP 47 language tag](https://simplifier.net/packages/ufp.core/0.6.0/files/1940712), seperti:   | Code | Display | | --- | --- | | en | English | | id-ID | Indonesian | | zh-CN | Chinese (Simplified) | |

|  |  |
| --- | --- |
|  | Setiap data harus unik / **TIDAK BOLEH** terdapat duplikasi |

## 2. Alur Pembuatan Data

Untuk membuat data pasien baru dengan NIK di SATUSEHAT, silakan ikut langkah-langkah berikut:

Tabel 1. Alur pembuatan data (NIK)

| Langkah | Approach |
| --- | --- |
| Langkah 1: `GET` *Patient Record* dari Pasien berdasarkan NIK  (*Pastikan data pasien ada di FHIR SATUSEHAT*) | - **Search by** `nomor IHS` atau - **Search by NIK** untuk `GET` `nomor IHS` - Parameter yang didapatkan:  - `Nomor IHS` - Jika nomor IHS ditemukan, gunakan nomor IHS pasien untuk pengiriman data RME ke SATUSEHAT - Jika nomor IHS tidak ditemukan, lakukan Langkah 2 **POST** *Create Patient record* |
| Langkah 2: `POST` *Create Patient record* dari Pasien yang memiliki NIK ke *request* | - Parameter ini diperlukan untuk *create patient record*:  - `NIK` sebagai `Identifier`   - `Nama`   - `Tanggal Lahir`   - `Tempat Lahir`   - `Jenis Kelamin`   - `Alamat` sesuai KTP (opsional)   - `Provinsi` sesuai KTP   - `Kota` sesuai KTP   - `Kecamatan` sesuai KTP   - `Desa/Kelurahan` sesuai KTP   - `Nomor telepon`   - `Status kematian pasien` (Default: False)   - `Status pernikahan pasien` (Opsional)   - `Tempat lahir pasien` (Opsional)   - `Kewarganegaraan pasien` (Default: WNI)   - `Bahasa` (Default: Indonesian) - Elemen data di atas akan dikirimkan ke API Dukcapil untuk diverifikasi kesamaan data sesuai dengan data KTP di DUKCAPIL - Jika seluruh elemen data sesuai, maka SATUSEHAT akan *generate* **Nomor IHS baru**  - **Nomor IHS baru** akan dikirimkan sebagai response API - Jika terdapat satu atau lebih elemen data yang tidak sesuai, maka SATUSEHAT akan mengembalikan *error response* sesuai dengan elemen data yang tidak terverifikasi DUKCAPIL  - Perbaiki *value* data dari variabel yang tidak sesuai dan pastikan penulisan data sama dengan informasi yang tertera pada KTP   - Kirim ulang **POST** *Create Patient record* dengan data yang benar |

## 3. Alur Mendapatkan Data

fasyankes dapat memperoleh nomor IHS pasien dengan NIK di SATUSEHAT, dengan menggunakan opsi berikut:

Tabel 1. Alur mendapatkan data

| Options | Approach |
| --- | --- |
| Option 1: Gunakan `Nomor IHS` Pasien ke SATUSEHAT. (Use Patient IHS Number to SATUSEHAT) | - Menggunakan Nomor IHS Pasien - Informasi yang perlu ke API `GET` Patient - By ID:  - `Nomor IHS Pasien` |
| Option 2a: Gunakan NIK Pasien sebagai parameter `Identifier` untuk SATUSEHAT. | - Menggunakan NIK - Informasi yang perlu dikirim ke API `GET` Patient - Search NIK:  - `NIK` |
| Option 2b: Gunakan NIK Pasien sebagai parameter `Identifier` untuk SATUSEHAT dan informasi Nama serta Tanggal Lahir sesuai KTP. | - Menggunakan NIK, Nama, dan Tanggal Lahir Pasien. - Informasi yang akan dikirim kembali ke API `GET` Patient - Search Name, Birthdate, NIK:  - `NIK`   - `Nama Pasien`   - `Tanggal Lahir Pasien` |
| Option 2c: Gunakan informasi Nama, Tanggal Lahir serta Jenis Kelamin pasien sesuai KTP | - Menggunakan Nama, Tanggal Lahir dan Jenis Kelamin. - Informasi yang dikirimkan ke API GET Patient - Search by Name, Birthdate, Gender:  - `Nama Pasien`   - `Tanggal Lahir Pasien`   - `Jenis Kelamin Pasien` |

## 4. Update/Patch Data Pasien dengan NIK

fasyankes dapat melakukan pemutakhiran data pasien dengan NIK, jika kondisi ini terpenuhi:

- Terdapat pemutakhiran data pasien di DUKCAPIL yang belum ada di master data pasien SATUSEHAT.

Informasi pasien yang dapat diperbarui adalah:

- Nama lengkap
- Tanggal lahir
- Tempat Lahir
- Jenis kelamin
- Alamat
- Status pernikahan
- Kewarganegaraan

Data pasien dapat diperbarui per variabel atau keseluruhan.

Tabel 1. Cara memperbarui data pasien

| Options | Approach |
| --- | --- |
| Option 1: Memperbarui Informasi Pasien menggunakan Nomor IHS Pasien oleh petugas fasyankes. | - `GET` data pasien pada API `GET` Patient - By ID menggunakan Nomor IHS, Jika nomor IHS sudah benar, maka akan mengembalikan data Pasien. - Fasyankes dapat memperbarui data dengan menggunakan API `PATCH` Patient. - Data berikut wajib dikirimkan:  - `Nomor IHS pasien`   - Data existing pasien (untuk validasi):  - `Nama lengkap pasien`     - `Tanggal lahir pasien`     - `Jenis kelamin pasien`   - Data baru (untuk memperbarui data), bisa pilih salah satu atau beberapa variabel:  - `NIK`     - `Nama lengkap`     - `Tanggal lahir`     - `Jenis kelamin`     - `Alamat`     - `Status pernikahan`     - `Tempat lahir`     - `Kewarganegaraan` - Jika data existing pasien yang dikirim kan tervalidasi, maka pembaruan data akan dilanjutkan - Jika terdapat Nomor NIK, maka NIK, nama lengkap dan tanggal lahir wajib diisi dan akan divalidasi ke DUKCAPIL  - Jika data berhasil divalidasi, maka data pasien akan diperbarui Jika data tidak berhasil divalidasi, maka akan dikembalikan *error response* - Jika tidak terdapat NIK, maka data akan diperbarui sesuai dengan variabel data yang dikirimkan |

## 5. Proses Verifikasi

Ada beberapa data NIK yang perlu diverifikasi oleh DUKCAPIL sebagai *single source of truth* (SSOT)

Tabel 1. NIK yang diverifikasi oleh DUKCAPIL

| Options | Process |
| --- | --- |
| `NIK Pasien` | - Setiap data Pasien Baru dibuat atau informasi NIK Baru diperbarui. - Data yang akan dikirim untuk verifikasi:  - `NIK`   - `Nama Lengkap`   - `Tanggal Lahir`   - `Jenis Kelamin`   - `Kode Provinsi`   - `Kode Kab/Kota`   - `Kode Kecamatan`   - `Kode Desa/Kelurahan` - Data Pasien akan diverifikasi ke DUKCAPIL. - Jika data *record* pasien telah terverifikasi maka data tersebut akan disimpan di Master Data Pasien. |

|  |  |
| --- | --- |
|  | Untuk Identifier lain, tidak akan ada proses verifikasi, dan akan menggunakan proses penggabungan untuk menautkan lebih dari satu profil pasien yang cocok. |

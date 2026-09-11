---
id: mpi-pasien-bayi
title: MPI Pasien Bayi
source_url: https://satusehat.kemkes.go.id/platform/docs/id/master-data/master-patient-index/pasien-bayi/
group: satusehat
fhir_version: R4
fetched_at: '2026-09-11T13:21:51Z'
sha256: 9303d1d35a7ad82681562e9e64a5cfd81e9e2f2a3dd1730cc3b5089dd1d1d316
---
# Pasien Bayi Baru Lahir

## 1. Ruang Lingkup

**Pasien bayi baru lahir** akan memiliki proses sebagai berikut:

- Create Patient Data.
- Get Patient Data.
- Update/Patch Patient Data.

### 1.1. Persyaratan Data Minimum

Berikut ini persyaratan data minimum untuk pasien bayi baru lahir:

|  |  |
| --- | --- |
|  | Setiap terdapat simbol asterik `*` sebelum nama variabel atau parameter yang disebutkan, maka variabel atau parameter tersebut bersifat **WAJIB** , **harus ada**, atau **pasti selalu ada**, contoh: `*variabel`. |

Tabel 1. Persyaratan data minimum pasien bayi baru lahir

| Data Point | Keterangan |
| --- | --- |
| `*identifier` | Identitas yang digunakan oleh Pasien, saat ini Identitas yang dapat digunakan hanya ada 2 (dua) jenis yaitu: NIK (`nik`) dan NIK Ibu (`nik-ibu`) |
| `*name` | Nama pasien bayi baru lahir yang diberikan di fasyankes.  Penamaan yang mungkin:  - Nama lengkap diberikan oleh keluarga - Penamaan generik dari fasyankes, contoh `Bayi Ny. [Nama ibu]` |
| `*birthDate` | Tanggal Lahir dari Pasien Bayi. dengan format: `YYYY-MM-DD` |
| `birthPlace` | Digunakan untuk menyimpan informasi Tempat lahir dari Pasien, sesuai standar penulisan NIK/KTP |
| `*gender` | Jenis Kelamin dari Pasien, terdiri dari `male`, dan `female` |
| `Nomor Kartu Keluarga` | Nomor administrasi keluarga yang diterbitkan DUKCAPIL |
| `*multipleBirthInteger` | Digunakan untuk menyimpan informasi urutan kelahiran untuk pasien Bayi baru lahir, berisi nominal `1`, `2`, dan seterusnya sesuai dengan urutan kelahiran dalam kasus kelahiran kembar.  Untuk kasus kelahiran tidak kembar dapat memasukkan nilai `0` |
| `*address` | Alamat pasien sesuai dengan KTP/NIK, untuk pasien Bayi baru lahir dapat menggunakan informasi alamat dari Orang Tua Bayi, informasi alamat terdiri dari komponen:  - `use` - peruntukan alamat dalam hal ini menggunakan rumah atau `home` - `line` - alamat lengkap sesuai KTP/NIK - `city` - nama kota - `postalCode` - kode pos - `country` - negara, dalam hal ini menggunakan `ID` - `extension` - penerapan kode administratif wilayah  Kode administratif mangacu ke kode wilayah kemendagri. Daftar kode wilayah terbaru dapat didapatkan di tahun berikut [Kode Wilayah KEMENDAGRI](https://docs.google.com/spreadsheets/d/13F87ScHgEikqYgv65ZAU1vsRLmXNFo1i/edit?usp=sharing&ouid=116173098464208547917&rtpof=true&sd=true) |
| `*address-extension` | Digunakan untuk memuat informasi kode administratif wilayah dari alamat pasien sesuai NIK/KTP, yang terdiri dari:  - `province` - Kode Provinsi - `city` - Kode Kab/Kota - `district` - Kode Kecamatan - `village` - Kode Desa/Kelurahan - `rt` - Nomor RT - `rw` - Nomor RW |
| `telecom` | Digunakan untuk menyimpan informasi kontak pasien yang dapat dihubungi seperti telepon atau *email* |
| `maritalStatus` | Digunakan untuk menyimpan informasi status pernikahan dari Pasien, untuk Bayi baru lahir pastikan data yang terkirim adalah:  - `S` - Never Married |
| `citizenshipStatus` | Digunakan untuk menyimpan informasi status kewarganegaraan, dalam hal ini `WNI` atau `WNA` |

|  |  |
| --- | --- |
|  | Setiap data harus unik / **TIDAK BOLEH** terdapat duplikasi |

#### 1.2. Persyaratan Data Minimum - Orang Terkait

Berikut ini persyaratan data minimum untuk orang yang berkaitan dengan bayi baru lahir (Ibu/ Ayah):

|  |  |
| --- | --- |
|  | Setiap terdapat simbol asterik `*` sebelum nama variabel atau parameter yang disebutkan, maka variabel atau parameter tersebut bersifat **WAJIB** , **harus ada**, atau **pasti selalu ada**, contoh: `*variabel`. |

Tabel 2. Persyaratan data minimum orang terkait

| Data Points | Rationale |
| --- | --- |
| `*ID Related Person` | *An unique identifier* dari *record* orang yang terkait (Ibu/ Ayah) - *Generate* UUID dari FHIR |
| `*Related person’s Identifier` | Identitas pasien dari orang yang terkait (Ibu/ Ayah) (`Nomor IHS`) |
| `*Patient’s Identifier` | Identifier pasien (`Nomor IHS`) |
| `*Relationship type` | Hubungan pasien dengan orang yang terkait (Ibu/ Ayah) |
| `*Name` | Nama lengkap orang yang terkait (Ibu/ Ayah) |
| `*Gender` | Jenis kelamin orang yang terkait (Ibu/ Ayah) |
| `*Birth Date` | Tanggal lahir orang yang terkait (Ibu/ Ayah) |
| `*Address` | Alamat orang yang terkait (Ibu/ Ayah) |
| `*Phone Number` | Nomor telepon orang yang terkait (Ibu/ Ayah) |

|  |  |
| --- | --- |
|  | Orang terkait mengacu pada pasien terkait, misalnya Ibu, atau Ayah dari bayi yang baru lahir. |

## 2. Alur Pembuatan Data

Untuk membuat data pasien bayi baru lahir di SATUSEHAT, silakan ikut langkah-langkah berikut:

Tabel 1. Alur pembuatan data (NIK Ibu)

| Langkah | Approach |
| --- | --- |
| Langkah 1: **GET** informasi Ibu pasien dari SATUSEHAT  (*Untuk memastikan data Pasien Ibu sudah ada di SATUSEHAT*) | - ***Search by*** `nomor IHS` atau - ***Search by* NIK** untuk **GET** `nomor IHS`  - Parameter yang didapatkan:  - `Nomor IHS` - Jika nomor IHS tidak ditemukan, lakukan langkah 1.a **POST** *Create Patient record* untuk Pasien dengan NIK - Jika nomor IHS ditemukan, lanjutkan ke langkah 2.b |
| Langkah 1.a: **POST** *Create Patient record* dari Ibu ke API Request  (Jika *record* Ibu pasien tidak ditemukan) | - Parameter ini diperlukan untuk *create patient record*:  - `NIK` sebagai `Identifier`   - `Nama`   - `Tanggal Lahir`   - `Tempat Lahir`   - `Jenis Kelamin`   - `Alamat` sesuai KTP (Opsional)   - `Provinsi` sesuai KTP   - `Kota` sesuai KTP   - `Kecamatan` sesuai KTP   - `Desa/Kelurahan` sesuai KTP   - `Nomor Telepon`   - `Status kematian pasien` (Default: False)   - `Status pernikahan pasien` (Opsional)   - `Tempat lahir pasien` (Opsional)   - `Kewarganegaraan pasien` (Default: WNI)   - `Bahasa` (Default: Indonesian) - Elemen data di atas akan dikirimkan ke API Dukcapil untuk diverifikasi kesamaan data sesuai dengan data KTP di DUKCAPIL - Jika seluruh elemen data sesuai, maka SATUSEHAT akan *generate* **Nomor IHS baru**  - **Nomor IHS baru** akan dikirimkan sebagai response API - Jika terdapat satu atau lebih elemen data yang tidak sesuai, maka SATUSEHAT akan mengembalikan *error response* sesuai dengan elemen data yang tidak terverifikasi DUKCAPIL  - Perbaiki *value* data dari variabel yang tidak sesuai dan pastikan penulisan data sama dengan informasi yang tertera pada KTP - Kirim ulang `POST` *Create Patient record* dengan data yang benar |
| Step 2.a: **POST** Informasi Pasien Bayi Baru Lahir ke API Request | - Parameter ini diperlukan untuk membuat *record* pasien bayi baru lahir  - `NIK Ibu` sebagai `Identifier`   - `Nama`   - `Tanggal Lahir`   - `Tempat Lahir*`   - `Jenis Kelamin`   - `Urutan Kelahiran`   - `Alamat (gunakan Alamat Ibu)`   - `Provinsi`   - `Kota`   - `Daerah`   - `Kecamatan`   - `Desa/Kelurahan`   - `Nomor KK (Opsional)` - Pemeriksaan duplikasi data pasien bayi baru lahir akan dicek berdasarkan parameter:  - `Nama`   - `Tanggal Lahir`   - `Jenis Kelamin`   - `Urutan Kelahiran` - Jika tidak ditemukan duplikasi, maka: `Nomor IHS` untuk Pasien Bayi Baru Lahir di MPI akan dibuat  - Jika ditemukan duplikasi, maka `Nomor IHS` *existing* akan ditampilkan - `Nomor IHS` akan ditampilkan sebagai API Response - Lanjutkan ke langkah 2.b untuk membuat *resources* `RelatedPerson` |
| Step 2.b: **POST** *Create record* `RelatedPerson` ke API Request dan menghubungkan ke *record* Ibu dari Bayi Baru Lahir (dari backend) | - Parameter ini diperlukan untuk membuat *record* `RelatedPerson`:  - `Nomor IHS Ibu`   - `Nomor IHS Pasien`   - `Relation Type: MTH`   - `Nama Ibu`   - `Tanggal Lahir Ibu`   - `Jenis Kelamin Ibu`   - `Alamat Ibu`   - `Nomor Telepon Ibu` - `POST` `RelatedPerson` resource record ke FHIR SATUSEHAT dari MPI API *service*  - *Generate* `RelatedPerson` ID - **PUT** *record* `RelatedPerson` sebagai LINK ke *record* Ibu Pasien - **SAVE** `RelatedPerson` resource record ke MPI Database (MongoDB) - Return Success sebagai API Response |

## 3. Alur Mendapatkan Data

fasyankes dapat memperoleh data pasien bayi baru lahir di SATUSEHAT, dengan menggunakan opsi berikut:

Tabel 1. Alur mendapatkan data

| Options | Approach |
| --- | --- |
| Option 1: Gunakan `Nomor IHS` Pasien ke SATUSEHAT. (Use Patient IHS Number to SATUSEHAT) | - Menggunakan Nomor IHS Pasien. - Informasi yang perlu dikirim ke API `GET` Patient - By ID:  - `Nomor IHS Pasien` |
| Option 2a: Gunakan NIK Pasien sebagai parameter `Identifier` untuk SATUSEHAT. | - Memeriksa NIK - Informasi yang perlu dikirim ke API `GET` Patient - Search NIK:  - `NIK Pasien` |
| Option 2b: Gunakan Informasi Pasien sebagai parameter `Identifier` untuk SATUSEHAT. | - Memeriksa Nama, Jenis Kelamin, dan Tanggal Lahir Pasien. - Informasi yang perlu dikirim ke API `GET` Patient - Search Name, Birthdate, Gender:  - `Nama Pasien`   - `Tanggal Lahir Pasien`   - `Jenis Kelamin Pasien` |
| Option 3a: Gunakan NIK Ibu untuk mendapatkan Data Pasien Bayi Baru Lahir. | - **GET** dengan menggunakan `identifier` system NIK Ibu. - Jika ditemukan, maka mengembalikan parameter pasien:  - `Nomor IHS`   - `Nama`   - `Urutan Kelahiran` - Jika kasus kelahiran kembar, akan ditampilkan semua pasien yang menggunakan NIK Ibu tersebut. - Jika terdapat lebih dari satu pasien dengan NIK ibu yang sama, Fasyankes perlu memeriksa urutan kelahiran agar dapat merujuk ke pasien yang sesuai. - Gunakan `nomor IHS` untuk mendapatkan Informasi Pasien. |
| Option 3b: Gunakan Informasi Ibu Pasien untuk mendapatkan informasi `RelatedPerson`. | - Mendapatkan data Ibu pasien, dengan menggunakan metode ini:  - `Nomor IHS Ibu`, atau   - `Kombinasi NIK Ibu`, `Nama`, dan `Tanggal Lahir` - Dilakukan pengecekan NIK Ibu, Nama, dan Tanggal Lahir. - Jika sesuai, maka akan ditampilkan `nomor IHS` Pasien yang berasal dari daftar `RelatedPersons` dari informasi Ibu yang memiliki tipe relasi “MTH” atau “Ibu”. - Informasi yang akan ditampilkan pada response:  - `Nomor IHS Pasien`   - `Nama Pasien`   - `Urutan Kelahiran Pasien` - Fasyankes perlu memeriksa pasien mana (jika lebih dari satu) yang perlu dirujuk. - Gunakan `nomor IHS` untuk mendapatkan informasi Pasien. |

## 4. Update/Patch Data Pasien Bayi Baru Lahir

|  |  |
| --- | --- |
|  | fasyankes dapat melakukan pemutakhiran data pasien bayi baru lahir, jika kondisi ini terpenuhi:  - Data pasien bayi baru lahir **BELUM** mempunyai NIK sebelumnya dan belum divalidasi oleh DUKCAPIL |

|  |  |
| --- | --- |
|  | Informasi pasien yang dapat diperbarui adalah:  - NIK (identifier) - Nama lengkap - Tanggal lahir - Tempat Lahir - Jenis kelamin - Alamat - Status pernikahan - Kewarganegaraan  Data pasien dapat diperbarui per variabel atau keseluruhan. |

|  |  |
| --- | --- |
|  | Jika NIK Pasien telah divalidasi oleh DUKCAPIL, opsi ubah data pasien mengikuti alur Update/Patch Patient dengan NIK. |

Tabel 1. Alur *Update* Data

| Options | Approach |
| --- | --- |
| Option 1: Memperbarui Informasi Pasien menggunakan `Nomor IHS` Pasien oleh petugas fasyankes. | - `GET` data pasien pada API `GET` Patient - By ID menggunakan `Nomor IHS`, Jika nomor IHS sudah benar, maka akan mengembalikan data Pasien. - Fasyankes dapat memperbarui data dengan menggunakan API `PATCH` Patient. - Data berikut wajib dikirimkan:  - `Nomor IHS pasien`   - Data existing pasien (untuk validasi):  - `Nama lengkap pasien`     - `Tanggal lahir pasien`     - `Jenis kelamin pasien`   - Data baru (untuk memperbarui data), bisa pilih salah satu atau beberapa variabel:  - `NIK`     - `Nama lengkap`     - `Tanggal lahir`     - `Jenis kelamin`     - `Alamat`     - `Status pernikahan`     - `Tempat lahir`     - `Kewarganegaraan` - Jika data existing pasien yang dikirimkan tervalidasi, maka pembaruan data akan dilanjutkan - Jika terdapat Nomor NIK, maka NIK, nama lengkap dan tanggal lahir wajib diisi dan akan divalidasi ke DUKCAPIL  - Jika data berhasil divalidasi, maka data pasien akan diperbarui   - Jika data tidak berhasil divalidasi, maka akan dikembalikan error response - Jika tidak terdapat NIK, maka data akan diperbarui sesuai dengan variabel data yang dikirimkan |

## 5. Proses Verifikasi

Ada beberapa data NIK yang perlu diverifikasi oleh DUKCAPIL sebagai *single source of truth* (SSOT)

Tabel 1. NIK yang diverifikasi oleh DUKCAPIL

| Options | Process |
| --- | --- |
| Option 1: NIK Pasien. | - Setiap data Pasien Baru dibuat atau informasi NIK Baru diperbarui. - Data yang akan dikirim untuk verifikasi:  - `NIK`   - `Nama Lengkap`   - `Tanggal Lahir`   - `Jenis Kelamin`   - `Kode Provinsi`   - `Kode Kab/Kota`   - `Kode Kecamatan`   - `Kode Desa/Kelurahan` - Data Pasien akan diverifikasi ke DUKCAPIL. - Jika data *record* pasien telah terverifikasi maka data tersebut akan disimpan di Master Data Pasien. |
| Option 2: NIK Ibu dari Pasien Bayi Baru Lahir. | - Saat NIK Ibu dimasukkan sebagai parameter untuk Bayi Baru Lahir. - NIK Ibu akan diperiksa ke data MPI jika sudah ada data pasien tersebut disana. - Jika tidak ada kecocokan pada NIK pasien, maka perlu dikirim ke DUKCAPIL untuk diverifikasi. - Data yang akan dikirim untuk diverifikasi:  - `NIK Ibu`   - `Nama Ibu` - Jika NIK dan nama tidak cocok, NIK Ibu tidak dapat digunakan. |

|  |  |
| --- | --- |
|  | Untuk `Identifier` lain, tidak akan ada proses verifikasi, dan akan menggunakan proses penggabungan untuk menautkan lebih dari satu profil pasien yang cocok. |

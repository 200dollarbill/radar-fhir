---
id: playbook-preface
title: Pengantar Teknis
source_url: https://satusehat.kemkes.go.id/platform/docs/id/playbook/preface/
group: satusehat
fhir_version: R4
fetched_at: '2026-09-11T13:20:21Z'
sha256: 74c3404511333f71640edebce16dc1fd940e45b1f6b7e6635613fdf5ffe9303c
---
# Pengantar Teknis

Beberapa simbol, istilah, dan konvensi digunakan pada pedoman ini agar penyampaian konsep, struktur data, sehingga menjadi lebih jelas. Pada bagian ini akan dijelaskan lebih lanjut terkait hal tersebut.

## Kata Kunci Prioritas

Dalam banyak dokumen terkait standar, beberapa kata digunakan untuk menandakan persyaratan dalam spesifikasi. Kata-kata ini sering dikapitalisasi dan/atau ditebalkan. Pada bagian ini akan didefinisikan kata-kata ini seperti yang dilakukan pada banyak dokumen RFC (*Request for Comment*), dengan beracuan pada standar di **RFC 2119**[<https://www.ietf.org/rfc/rfc2119.txt>] beberapa kata-kata tersebut dialihbahasakan ke bahasa Indonesia.

- **WAJIB**, berarti definisi tersebut merupakan persyaratan mutlak dari spesifikasi.
- **TIDAK BOLEH**, berarti definisi tersebut merupakan larangan mutlak terhadap spesifikasi.
- **SEBAIKNYA**, berarti bahwa ada alasan yang sah dan kuat dalam keadaan tertentu untuk mengesampingkan hal tertentu lainnya, tetapi implikasi dari perilaku tersebut harus dipahami dan dipertimbangkan dengan cermat sebelum memilih alur yang berbeda.
- **SEBAIKNYA TIDAK**, berarti bahwa ada alasan yang sah dan kuat dalam keadaan tertentu ketika perilaku tertentu dapat diterima atau bahkan berguna, tetapi implikasi dari perilaku harus dipahami dan kasusnya dipertimbangkan dengan cermat sebelum menerapkan perilaku apa pun yang dijelaskan dengan label ini.
- **DIREKOMENDASIKAN**, sama definisinya dengan **SEBAIKNYA**.
- **TIDAK DIREKOMENDASIKAN**, sama definisinya dengan **SEBAIKNYA TIDAK**.
- **BOLEH**, berarti bahwa suatu spesifikasi benar-benar opsional. Satu mitra dapat memilih untuk memasukkan spesifikasi tersebut karena kondisi tertentu membutuhkannya atau karena mitra merasa bahwa itu meningkatkan performa tertentu sementara mitra lain mungkin menghilangkan spesifikasi yang sama. Implementasi yang tidak menyertakan opsi tertentu **PERLU** siap untuk beroperasi dengan implementasi lain yang menyertakan opsi, meskipun mungkin dengan fungsionalitas yang berkurang. Dalam hal yang sama, implementasi yang menyertakan opsi tertentu **PERLU** siap untuk beroperasi dengan implementasi lain yang tidak menyertakan opsi (kecuali, tentu saja, untuk fitur yang disediakan opsi.)
- **OPSIONAL**, sama definisinya dengan **BOLEH**.

Penggunaan kata-kata tadi biasanya untuk panduan dari suatu spesifikasi agar berjalan sesuai yang diharapkan. Bisa juga terkait pertimbangan keamanan, di mana kata-kata tersebut sering digunakan untuk menentukan perilaku dengan implikasi keamanan. Efek pada keamanan karena tidak menerapkan **WAJIB** atau **SEBAIKNYA**, atau melakukan sesuatu yang menurut spesifikasi **TIDAK BOLEH** atau **SEBAIKNYA TIDAK** dilakukan mungkin sangat bijak.

## Simbol dan Istilah

Berikut beberapa simbol dan istilah yang digunakan dalam dokumentasi ini.

Tabel 1. Penamaan dan Simbol

| Penamaan | Simbol/Nilai | Penjelasan |
| --- | --- | --- |
| `string` | `""` atau `''` | Representasi dari kumpulan karakter/huruf/simbol. |
| `number` | `"1"`, `"-1"`, `"1.0"`, `'1'`, `'-1'`, `'1.0'`, | Representasi dari kumpulan angka baik dari bilangan bulat atau desimal, dalam bentuk `string`. |
| `uuid` | `uuid`, `uuid1`, `uuid2`, `uuid3`, `uuid4` | Merepresentasikan ID universal unik dari suatu entitas, yang terdiri dari 36 karakter (32 karakter heksadesimal dan 4 tanda minus), lebih lengkapnya silakan lihat di <https://en.wikipedia.org/wiki/Universally_unique_identifier>. Contoh data `uuid`: `123e4567-e89b-12d3-a456-426614174000` |

## ReST API

ReST adalah akronim dari *Representational State Transfer* dan salah satu tipe arsitektur untuk sistem hypermedia terdistribusi. Roy Fielding pertama kali mempresentasikannya pada tahun 2000 dalam disertasinya yang terkenal [[restfulapi.net]](#restfulapi.net) [[wikipedia-rest]](#wikipedia-rest).

ReST melakukan pertukaran data sesuai standar yang ada pada *HTTP Specification*, sehingga perlu dijelaskan secara singkat terkait beberapa HTTP *method* dan HTTP *status code* yang diantaranya digunakan dalam dokumentasi teknis ini.

#### HTTP Method

*HTTP Method* mendefinisikan metode untuk menunjukan aksi yang sesuai yang akan dilakukan pada *resource* yang telah terindentifikasi. *Resource* sendiri merepresentasikan data yang sudah ada atau data dinamis yang tergantung dari apa yang sudah disepakati dan diterapkan pada *server* yang dituju [[wikipedia-http-method]](#wikipedia-http-method).

Tabel 2. HTTP Method

| *Method* | Penjelasan |
| --- | --- |
| `GET` | Meminta representasi *resource* dari sumber tertentu untuk di ***READ*** oleh peminta. |
| `POST` | Meminta server menerima entitas yang terlampir dalam *request* sesuai struktur yang disepakati sebelumnya dan memprosesnya sebagai proses ***CREATE***. |
| `PUT` | Meminta server menerima entitas yang terlampir dalam *request* sesuai struktur yang disepakati sebelumnya dan memprosesnya sebagai proses ***UPDATE*** dari data yang dimaksud. |
| `PATCH` | Meminta server menerima sebagian entitas yang terlampir dalam *request* sesuai struktur yang disepakati sebelumnya dan memprosesnya sebagai proses ***PARTIAL UPDATE*** dari data yang dimaksud. |
| `DELETE` | Meminta agar *resource* yang dimaksud di-***DELETE***. |

#### HTTP Status Codes

*HTTP Status Codes* dikeluarkan dari *server* sebagai bentuk *response* dari *request* yang berasal dari *client* [[wikipedia-http-status-code]](#wikipedia-http-status-code). Kode-kode ini dikategorikan menjadi 5 kelas yang dibedakan dari digit pertamanya yaitu: **1xx** *informational response*, **2xx** *successful*, **3xx** *redirection*, **4xx** *client error*, dan **5xx** *server error*. Pada bagian ini, hanya akan dijelaskan 3 *HTTP Status Codes* yang sering digunakan di ReST yaitu **2xx**, **4xx**, dan **5xx**.

Tabel 3. HTTP Method

| Method | Penjelasan |
| --- | --- |
| `200 OK` | Respon standar untuk permintaan yang berhasil. |
| `201 Created` | Permintaan berhasil dan *resource* yang dimaksud telah dibuat. Biasanya akan ada header `location` yang menunjukan letak *resource* yang sudah dibuat. |
| `202 Accepted` | Permintaan berhasil dan *resource* yang dimaksud telah dijadwalkan akan diproses. Biasanya akan ada header `location` yang menunjukan letak *resource* yang akan menunjukan status atau hasil proses yang sudah atau akan dikerjakan. |
| `204 No Content` | Permintaan berhasil dan *resource* yang dimaksud telah dibuat, tetapi server tidak menyediakan data kembalian/response apapun (pesan di `body` kosong). |
| `206 Partial Content` | Biasanya digunakan dalam proses *download* data secara partial ([*byte serving*](https://en.wikipedia.org/wiki/Byte_serving)) sesuai rentang yang didefinisikan di-*header*. |
| `400 Bad Request` | Permintaan gagal dikarenakan ada kesalahan di bagian *client*, seperti struktur data yang tidak sesuai, masukkan data yang tidak sah, atau ukuran *resource* yang dikirim terlalu besar. |
| `401 Unauthorized` | Permintaan gagal dikarenakan perlu ada proses autentikasi (*authentication*) tertentu untuk mengaksesnya atau hasil autentikasi tidak sah. |
| `403 Forbidden` | Permintaan gagal dikarenakan perlu ada proses otorisasi (*authorization*) tertentu untuk mengaksesnya atau otorisasi tidak ditolak. |
| `404 Not Found` | Permintaan gagal dikarenakan *resource* yang dimaksud tidak ditemukan. |
| `405 Method Not Allowed` | Permintaan gagal dikarenakan *HTTP Method* yang digunakan untuk meminta *resource* tidak sesuai atau tidak diperbolehkan. |
| `409 Conflict` | Permintaan gagal dikarenakan adanya konflik terkait *resource* yang diakses, misal pembaruan *resource* yang sama secara berbarengan. |
| `413 Payload Too Large` | Permintaan gagal dikarenakan ukuran *payload* yang dikirimkan melebihi batas yang bisa diproses oleh *server*. |
| `415 Unsupported Media Type` | Permintaan gagal dikarenakan *server* tidak mendukung jenis *resource* yang dikirimkan. |
| `422 Unprocessable Entity` | Permintaan gagal dikarenakan adanya galat terkait semantik dari data atau *resource* yang dikirimkan saat diproses. |
| `429 Too Many Requests` | Permintaan gagal dikarenakan *client* terlalu cepat atau banyak mengakses *server*, biasanya galat ini terkait dengan ketentuan dari skema *rate-limmiter*. |
| `500 Internal Server Error` | Permintaan gagal dikarenakan ada kesalahan dibagian server. |
| `501 Not Implemented` | Target permintaan yang dimaksud belum diimplementasikan di server. |
| `503 Service Unavailable` | *Server* dalam kondisi mati atau dalam pemeliharaan (*maintenance*). |
| `504 Gateway Timeout` | *Server* hanya bertindak sebagai *gateway* atau *proxy* dan menerima *response* yang salah dari *server* sumber. |

## ISO 8601

ISO 8601 adalah sebuah standar internasional yang digunakan pada pertukaran data terkait tanggal dan waktu [[wikipedia-iso8601]](#wikipedia-iso8601). Format tanggal yang digunakan pada dokumentasi teknis ini sebagian besar mengacu pada standar ISO 8601 untuk merepresentasikan tanggal dan waktu.

#### Format Tanggal dan Waktu

Tabel 4. Format ISO8601 untuk tanggal dan waktu

| Simbol | Penjelasan |
| --- | --- |
| `YYYY` | Merepresentasikan 4 digit tahun, *zero-padded* dibagian kiri, mulai dari `0000` hingga `9999`. Tahun `0000` sama dengan tahun 1 Sebelum Masehi (SM). Representasi tahun Sebelum Masehi harus mengunakan tanda minus `-0000 = 1 SM`, `-0001 = 2 SM`, dst. |
| `MM` | Merepresentasikan 2 digit bulan, *zero-padded* dibagian kiri, dalam satu tahun mulai dari `01` hingga `12`. Secara berurutan merepresentasikan bulan: `01 Januari`, `02 Februari`, `03 Maret`, `04 April`, `05 Mei`, `06 Juni`, `07 Juli`, `08 Agustus`, `09 September`, `10 Oktober`, `11 November`, `12 Desember`. |
| `DD` | Merepresentasikan 2 digit hari, *zero-padded* dibagian kiri, dalam satu bulan mulai dari `01` hingga `31` tergantung dari bulan yang dimaksud. |
| `hh` | Merepresentasikan 2 digit jam, *zero-padded* dibagian kiri, dari `00` hingga `23`. |
| `mm` | Merepresentasikan 2 digit menit, *zero-padded* dibagian kiri, dari `00` hingga `59`. |
| `ss` | Merepresentasikan 2 digit detik, *zero-padded* dibagian kiri, dari `00` hingga `60`. |
| `.sss` | Merepresentasikan 3 digit milidetik, *zero-padded* dibagian kiri. |
| `.ssssss` | Merepresentasikan 6 digit nanodetik, *zero-padded* dibagian kiri. |

Contoh penggunaan dari format yang telah dijelaskan sebelumnya:

- `YYYY-MM-DD` untuk merepresentasikan tanggal, contoh: `2021-01-01` (2 Januari 2021).
- `hh:mm:ss` untuk merepresentasikan waktu lokal, contoh: `22:10:58` (pukul 22 lewat 10 menit 58 detik).
- `YYYY-MM-DD hh:mm:ss` untuk merepresentasikan tanggal dan waktu lokal, contoh: `2021-01-02 22:10:58` (2 Januari 2021, pukul 22 lewat 10 menit 58 detik).
- `hh:mm:ssZ` atau `hh:mm:ss+0000` untuk merepresentasikan waktu UTC/GMT, contoh: `10:10:58Z` (pukul 10 lewat 10 menit 58 detik UTC) bila dikonversi ke zona `Asia/Jakarta (UTC+7)` menjadi `17:10:58+0700`.
- `YYYY-MM-DD hh:mm:ssZ` untuk merepresentasikan tanggal dan waktu lokal, contoh: `2021-01-02 10:10:58Z` (2 Januari 2021, pukul 10 lewat 10 menit 58 detik UTC) bila dikonversi ke zona `Asia/Jakarta (UTC+7)` menjadi `2 Januari 2021, 17:10:58+0700`.
- `YYYY-MM-DD hh:mm:ss.ssssss` untuk merepresentasikan tanggal dan waktu lokal hingga ke 3 digit mili detik, contoh: `2021-01-02 10:10:58.353` (2 Januari 2021, pukul 10 lewat 10 menit 58 detik 353 mili detik).

## Pesan Prioritas

Portal dokumentasi SATUSEHAT ini menggunakan beberapa pesan prioritas (*Admonitions*) untuk menekankan informasi tertentu.

Beberapa pesan prioritas berisi pernyataan, peringatan, perhatian, atau teguran tertentu sebagai salah satu cara untuk menekankan beberapa penjelasan yang dianggap penting, digunakan pada dokumentasi ini. Pada bagian ini akan dijelaskan secara singkat tipe-tipe dari kotak pesan prioritas tersebut antara lain:

#### Catatan

Memberikan catatan singkat terkait informasi tertentu. Contoh:

|  |  |
| --- | --- |
|  | Postman adalah salah satu aplikasi untuk melakukan *testing* terkait ReST API yang *user-friendly* dibandingkan cURL. |

#### Tips

Memberikan saran kepada pembaca yang terkait *best practices* atau tips tertentu. Contoh:

|  |  |
| --- | --- |
|  | Untuk versi cURL terbaru, gunakan parameter `--oauth2-bearer` untuk melakukan *request* yang membutuhkan *token bearer*. |

#### Penting

Memberikan saran kepada pembaca bahwa anjuran yang disebutkan penting untuk dibaca. Contoh:

|  |  |
| --- | --- |
|  | Selalu pakai *token bearer* yang didapatkan setiap melakukan *request* API yang bukan untuk autentikasi. |

#### Perhatian

Memberikan saran kepada pembaca agar anjuran yang telah dijelaskan dilakukan dengan hati-hati. Contoh:

|  |  |
| --- | --- |
|  | Mohon diperhatikan saat melakukan *request* data, dikarenakan ada perbedaan target URL untuk versi Production dan Development. |

#### Peringatan

Memberikan tekanan kepada pembaca agar anjuran yang telah dijelaskan dilakukan dengan serius dan hati-hati, dikarenakan kemungkinan akan ada efek samping. Contoh:

|  |  |
| --- | --- |
|  | Cek apakah *payload* yang akan dikirimkan sudah sesuai standar yang disepakati sebelumnya, karena bila tidak sesuai *payload* tersebut tidak akan dapat diproses. |

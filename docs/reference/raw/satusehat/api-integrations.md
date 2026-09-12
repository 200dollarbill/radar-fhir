---
id: api-integrations
title: API Integrations
source_url: https://satusehat.kemkes.go.id/platform/docs/id/api-catalogue/integrations/
group: satusehat
fhir_version: R4
fetched_at: '2026-09-11T13:21:10Z'
sha256: 1dbdd469e212bedf90d6c5429c760a4dbb75829f08769012220730cdddeee66a
---
# Interoperabilitas

Setelah resource yang terkait dengan proses orientasi (*Prerequisites*) terpenuhi, maka tahap selanjutnya adalah interoperabilitas (transaksi data), yang pada penerapannya akan dibagi-bagi lagi menjadi beberapa alur proses sesuai penggunaannya (*use case*) baik *use case* dasar (Modul Pelayanan) maupun *use case* tematik (Modul Penerapan). Penjelasan terkait ReST API mana saja yang akan digunakan sesuai *use case*-nya tidak termasuk dalam cakupan dokumentasi ini. Pembahasan mengenai hal tersebut akan dijelaskan pada dokumentasi tersendiri.

Semua resource dari ReST API yang akan dijelaskan di bagian ini, digunakan untuk keperluan interoperabilitas (transaksi data), ke atau dari ekosistem SATUSEHAT. Dalam proses interoperabilitas ini, sebagian besar resource yang berkaitan dengan proses *onboarding* akan secara intensif dipakai, terutama yang berkaitan dengan resource *Patient*.

|  |  |
| --- | --- |
|  | Setiap teks yang berwarna **biru muda**, dapat diklik untuk melompat ke bagian yang direferensikan. |

Akses alamat URL untuk **ReST API SATUSEHAT Terkait Integrasi** mempunyai tiga *endpoint* berdasarkan jenis lingkungan pengembangannya (*development environment*) yaitu:

- **Sandbox**: <https://api-satusehat-stg.dto.kemkes.go.id/fhir-r4/v1>
- **Production**: <https://api-satusehat.kemkes.go.id/fhir-r4/v1>

|  |  |
| --- | --- |
|  | Semua penerapan, penjelasan, dan contoh yang akan dibahas akan menggunakan *environment sandbox*. |

|  |  |
| --- | --- |
|  | Untuk melakukan beberapa *request* ke ReST API SATUSEHAT yang akan dijelaskan atau dicontohkan di bagian ini, **WAJIB** melakukan proses autentikasi terlebih dahulu.  Setiap *request* diperlukan sebuah nilai token bertipe `Bearer` yang akan dimasukkan pada *header* `Authorization: Bearer <access_token>`.  Nilai `<access_token>` didapatkan dari properti `access_token` dari hasil *response* yang secara detail dijelaskan di artikel terkait [Akses Token](../authentication/apis/token/). |

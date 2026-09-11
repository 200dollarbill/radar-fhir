---
id: api-onboardings
title: API Onboardings
source_url: https://satusehat.kemkes.go.id/platform/docs/id/api-catalogue/onboardings/
group: satusehat
fhir_version: R4
fetched_at: '2026-09-11T13:21:02Z'
sha256: e5051b6b3120f189feb5d4a8a18371f29b1661eaa045587dcc1e21b6706c3f8b
---
# Prerequisites

Semua resource dari ReST API yang akan dijelaskan di bagian ini, adalah inti dari semua transaksi data yang akan dilakukan pada bagian integrasi nanti, ke atau dari ekosistem SATUSEHAT. Dalam proses orientasi (*onboarding*) ini (yang selanjutnya disebut *prerequisites*), resource yang harus tersedia datanya adalah: *Patient*, *Practicioner*, *Organization*, dan *Location*.

|  |  |
| --- | --- |
|  | Setiap teks yang berwarna **biru muda**, dapat diklik untuk melompat ke bagian yang direferensikan. |

Akses alamat URL untuk **ReST API SATUSEHAT Terkait Orientasi (*Onboarding*)** mempunyai tiga *endpoint* berdasarkan jenis lingkungan pengembangannya (*development environment*) yaitu:

- **Sandbox**: <https://api-satusehat-stg.dto.kemkes.go.id/fhir-r4/v1>
- **Production**: <https://api-satusehat.kemkes.go.id/fhir-r4/v1>

|  |  |
| --- | --- |
|  | Semua penerapan, penjelasan, dan contoh yang akan dibahas akan menggunakan *environment sandbox*. |

|  |  |
| --- | --- |
|  | Untuk melakukan beberapa *request* ke ReST API SATUSEHAT yang akan dijelaskan atau dicontohkan di bagian ini, **WAJIB** melakukan proses autentikasi terlebih dahulu.  Setiap *request* diperlukan sebuah nilai token bertipe `Bearer` yang akan dimasukkan pada *header* `Authorization: Bearer <access_token>`.  Nilai `<access_token>` didapatkan dari properti `access_token` dari hasil *response* yang secara detail dijelaskan di artikel terkait [Akses Token](../authentication/apis/token/). |

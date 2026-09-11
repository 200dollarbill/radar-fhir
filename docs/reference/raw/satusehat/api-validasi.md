---
id: api-validasi
title: Validasi
source_url: https://satusehat.kemkes.go.id/platform/docs/id/api-catalogue/validasi/
group: satusehat
fhir_version: R4
fetched_at: '2026-09-11T13:21:20Z'
sha256: bcd7f2c2c1f6a0fbeadde0e7ca874a201d018f067c28a1a74d25c91421165e03
---
# Validasi Interoperabilitas

Ketika melakukan pengiriman data FHIR melalui ReST API yang disediakan, khususnya terkait *resource* Interoperabilitas, sistem akan melakukan proses validasi terhadap kode-kode terminologi yang digunakan. Kode-kode terminologi ini mencakup ICD-10, ICD-9 CM, LOINC, SNOMED-CT, dan *codesystem* lainnya sesuai standar FHIR HL7 yang dapat dilihat pada menu [**Terminologi**](../../terminology/#terminologi)

|  |  |
| --- | --- |
|  | Setiap teks yang berwarna **biru muda**, dapat diklik untuk melompat ke bagian yang direferensikan. |

## Proses Validasi

![Alur Validasi Interoperabilitas FHIR](../_images/diagram-validasi-fhir.png)

Gambar 1. Alur Validasi Interoperabilitas FHIR

Berdasarkan alur di atas dapat dijelaskan sebagai berikut:

1. Faskes melakukan pemanggilan terhadap API SATUSEHAT.
2. API *Gateway* SATUSEHAT melakukan pengecekan terlebih dahulu ke FHIR *Processor* SATUSEHAT, terhadap *request* yang dikirimkan fasyankes.
3. Jika terdapat kesalahan pada *request*, maka SATUSEHAT akan mengembalikan pesan kegagalan.
4. Jika tidak terdapat kesalahan pada *request*, maka *request* akan dilanjutkan ke FHIR *Server* SATUSEHAT.
5. Setelah data berhasil tersimpan, maka API SATUSEHAT akan mengembalikan pesan sukses.

## Response 4xx

Sistem akan mengembalikan pesan *error* bila pengiriman data tidak sesuai dengan format atau ketentuan yang berlaku pada sistem.

### Struktur Data

```
DATA STRUCTURE:
{ (1)
  *resourceType: string (2)
  *issue: [{ (3)
    *severity: string
    *code: string
    *details: {
      *text: string
    }
    expression: [
      string
    ]
  }]
}
```

|  |  |
| --- | --- |
| **1** | Respon yang diterima berupa `object`. |
| **2** | Properti `resourceType` bertipe `string`, berisi nilai `OperationOutcome` (Resource FHIR untuk informasi hasil pemrosesan sistem). |
| **3** | Properti `issue` bertipe `array of objects` berisi informasi terkait galat yang terjadi. |
| **4** | Properti `issue.severity` bertipe `string`, terkait jenis isu yang diinformasikan: - `error` terdapat kesalahan yg ditemukan oleh sistem. |
| **5** | Properti `issue.code` bertipe `string`, menandakan kode kategori validasi: - `duplicate`, mengirim *encounter* yang berulang dengan nilai yang sama; - `format`, format yang dikirimkan tidak sesuai; - `value`, nilai yang dikirimkan tidak sesuai atau tidak diperbolehkan. |
| **6** | Properti `issue.details` bertipe `object`, berisi informasi detail terkait kesalahan yang ditemukan oleh sistem. |
| **7** | Properti `issue.expression` bertipe `array of string`, berisi informasi `resource` dan `field` yang ditemukan oleh sistem. |

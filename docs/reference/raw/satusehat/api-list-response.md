---
id: api-list-response
title: List Response
source_url: https://satusehat.kemkes.go.id/platform/docs/id/api-catalogue/validasi/list-response/
group: satusehat
fhir_version: R4
fetched_at: '2026-09-11T13:21:24Z'
sha256: 05cb51c35a22dd590e25bcaf6f44780745dabe3637a455829fea0543589c369a
---
# Daftar Response Validasi

## Contoh Response (JSON)

### Found duplicate resource

*Error* ini terjadi ketika fasyankes mengirimkan *payload request* lebih dari satu kali ke SATUSEHAT.

|  |  |
| --- | --- |
|  | Pengiriman *payload request* **TIDAK BOLEH** lebih dari satu kali. |

```
{
  "resourceType": "OperationOutcome",
  "text": {
    "status": "generated"
  },
  "issue": [{
    "severity": "error",
    "code": "duplicate",
    "details": {
      "text": "Found duplicate resource: Encounter"
    }
  }]
}
```

### Code not found

*Error* ini terjadi jika kode yang dikirimkan fasyankes pada *payload request* ke SATUSEHAT tidak tersedia. Untuk memperbaiki *error* ini, silakan cek kode yang tersedia pada lampiran terminologi atau *valueset* terkait.

|  |  |
| --- | --- |
|  | **WAJIB** menggunakan *codesystem* atau *valueset* lainnya sesuai standar SATUSEHAT dan/atau FHIR HL7 yang dapat dilihat pada menu [**Terminologi**](../../../terminology/#terminologi). |

```
{
  "resourceType": "OperationOutcome",
  "text": {
    "status": "generated"
  },
  "issue": [{
    "severity": "error",
    "code": "value",
    "details": {
      "text": "Code not found: 'xxx' in system: http://terminology.hl7.org/CodeSystem/v3-ActCode (RuleNumber: 10001)"
    },
    "expression": [
      "Encounter.class.code"
    ]
  }]
}
```

### Invalid date time format

*Error* ini terjadi ketika fasyankes mengirimkan tanggal yang tidak sesuai dengan format yang diperbolehkan `YYYY-MM-DDThh:mm:ss+00:00`. Standar format Waktu yang digunakan dalam pengiriman data adalah `UTC +00:00` agar tidak terdeteksi sebagai tanggal dimasa depan, kecuali periode seperti appointment, masa kadaluarsa obat, masa berlaku kepesertaan jaminan, dan lainnya yang memungkinkan sebagai pengecualian.

|  |  |
| --- | --- |
|  | **Standard format Waktu** yang digunakan dalam pengiriman data adalah **UTC +00**. Misalnya waktu **WIB**, maka format yang digunakan adalah **waktu sekarang dikurangi 7**, jika **WITA**, maka **waktu sekarang dikurangi 8**, dan Jika **WIT**, maka **waktu sekarang dikurangi 9**.  **Contoh:** Pukul 17.35 WIB tanggal 23 Agustus 2023 maka yang dikirimkan adalah waktunya perlu diubah ke UTC +00 menjadi 10.35, berarti menjadi `2023-08-23T10:35:00+00:00`. |

```
{
  "resourceType": "OperationOutcome",
  "text": {
    "status": "generated"
  },
  "issue": [{
    "severity": "error",
    "code": "format",
    "details": {
      "text": "Invalid date time format : 2022-06-14 (RuleNumber: 10132). Format allowed : YYYY-MM-DDThh:mm:ss+00:00"
    },
    "expression": [
      "Composition.date"
    ]
  }]
}
```

### Invalid date time value

*Error* ini terjadi ketika fasyankes mengirimkan tanggal yang tidak sesuai berdasarkan standar format Waktu.

|  |  |
| --- | --- |
|  | **WAJIB** menggunakan **Standard format Waktu** dalam pengiriman data (**UTC +00**). |

```
{
  "resourceType": "OperationOutcome",
  "text": {
    "status": "generated"
  },
  "issue": [{
    "severity": "error",
    "code": "value",
    "details": {
      "text": "Invalid date time value : 2021-06-02T12:28:03Z (RuleNumber: 10132) Not Allowed : Future Date or Past Date older than 31st August 2022"
    },
    "expression": [
      "Composition.date"
    ]
  }]
}
```

### Reference is mandatory

*Error* ini terjadi ketika *element* pada *payload request* menyertakan *referensi resource* yang tidak valid.

|  |  |
| --- | --- |
|  | **WAJIB** menyertakan *referensi resource* yang **VALID** pada *element* saat akan melakukan *payload request*. |

```
{
  "resourceType": "OperationOutcome",
  "text": {
    "status": "generated"
  },
  "issue": [{
    "severity": "error",
    "code": "value",
    "details": {
      "text": "Reference is mandatory : Encounter.serviceProvider (RuleNumber: 10124)"
    },
    "expression": [
      "Encounter.serviceProvider"
    ]
  }]
}
```

### Invalid Coding System

*Error* tersebut berkaitan dengan penggunaan *codesystem* pada *payload request* ke SATUSEHAT, yang tidak diperbolehkan untuk *element* yang disebutkan pada *payload response* tersebut.

|  |  |
| --- | --- |
|  | **WAJIB** menggunakan *codesystem* atau *valueset* lainnya sesuai standar SATUSEHAT dan/atau FHIR HL7 yang dapat dilihat pada menu [**Terminologi**](../../../terminology/#terminologi). |

```
{
  "resourceType": "OperationOutcome",
  "text": {
    "status": "generated"
  },
  "issue": [{
    "severity": "error",
    "code": "value",
    "details": {
      "text": "Invalid coding system: http://xxx.org (RuleNumber: 10002)"
    },
    "expression": [
      "Encounter.participant[0].type[0].coding[0].system"
    ]
  }]
}
```

### Element not found

*Error* tersebut dikarenakan *element* pada *payload request* yang seharusnya *mandatory* tidak terkirim/tidak diisi/tidak terdapat pada pengiriman data ke SATUSEHAT.

|  |  |
| --- | --- |
|  | 1. Setiap terdapat simbol asterik `*` sebelum nama variabel/parameter/element FHIR yang disebutkan, maka variabel/parameter/element FHIR tersebut bersifat **WAJIB** , **harus ada**, atau **pasti selalu ada**, contoh: **`*Location.identifier`**. 2. Harap perhatikan simbol asterik `*` tersebut pada **Daftar Pemetaan Nilai** didalam [**Panduan Interoperabilitas**](../../../interoperability/#panduan-interoperabilitas) yang penggunaannya disesuaikan dengan pelayanan esensial (**Modul Pelayanan**) atau penerapan jenis/kategori penyakit tertentu (**Penerapan (*Use cCase*)**). |

```
{
  "resourceType": "OperationOutcome",
  "text": {
    "status": "generated"
  },
  "issue": [{
    "severity": "error",
    "code": "value",
    "details": {
      "text": "Element not found: Claim.insurance[0].focal (RuleNumber: 10263)"
    },
    "expression": [
      "Claim.insurance[0].focal"
    ]
  }]
}
```

### Invalid identifier System

*Error* ini terjadi jika *codesystem* yang digunakan pada `Identifier` tidak mengikuti standar yang ditetapkan. Untuk memperbaiki *error* ini, silakan cek kode yang tersedia pada [**Panduan Interoperabilitas**](../../../interoperability/#panduan-interoperabilitas) atau menu [**Terminologi**](../../../terminology/#terminologi).

|  |  |
| --- | --- |
|  | **WAJIB** menggunakan *codesystem* yang **VALID** pada `Identifier`. |

```
{
  "resourceType": "OperationOutcome",
  "text": {
    "status": "generated"
  },
  "issue": [{
    "severity": "error",
    "code": "value",
    "details": {
      "text": "Invalid identifier system: http://xxx.org (RuleNumber: 10117)"
    },
    "expression": [
      "Encounter.identifier[0].system"
    ]
  }]
}
```

### Integer formated as a string

*Error* ini terjadi jika `value` yang dikirimkan tidak bernilai `integer` dan tanpa tanda petik.

|  |  |
| --- | --- |
|  | Perbaiki `value` yang disebutkan dan pastikan bernilai `integer` dan tanpa petik. |

```
{
  "resourceType": "OperationOutcome",
  "text": {
    "status": "generated"
  },
  "issue": [{
    "severity": "error",
    "code": "value",
    "details": {
      "text": "Integer formated as a string: 'Satu' (RuleNumber: 10254)"
    },
    "expression": [
      "Claim.supportingInfo[0].sequence"
    ]
  }]
}
```

### Text is empty

*Error* ini terjadi ketika *element* yang dikiriman ke SATUSEHAT `empty string`.

|  |  |
| --- | --- |
|  | Element pada kiriman **TIDAK BOLEH** `empty string`. |

```
{
  "resourceType": "OperationOutcome",
  "text": {
    "status": "generated"
  },
  "issue": [{
    "severity": "error",
    "code": "value",
    "details": {
      "text": "Text is empty: '' (RuleNumber: 10134)"
    },
    "expression": [
      "Composition.title"
    ]
  }]
}
```

### Use xxx instead of xxx to patch Location

*Error* ini terjadi jika **PATCH** yang dikirimkan pada *resource* `Location` tidak mengikuti *public* POSTMAN yang terbaru.

|  |  |
| --- | --- |
|  | Periksa kiriman **PATCH** pada *resource* `Location` mengikuti *public* POSTMAN yang terbaru. |

```
{
  "resourceType": "OperationOutcome",
  "text": {
    "status": "generated"
  },
  "issue": [{
    "severity": "error",
    "code": "value",
    "details": {
      "text": "Use /operationalStatus instead of /operationalStatus/system to patch Location (RuleNumber: 10171)"
    },
    "expression": [
      "Location.operationalStatus"
    ]
  }]
}
```

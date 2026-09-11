---
id: api-kamus-validasi
title: Kamus Validasi
source_url: https://satusehat.kemkes.go.id/platform/docs/id/api-catalogue/validasi/kamus-validasi/
group: satusehat
fhir_version: R4
fetched_at: '2026-09-11T13:21:22Z'
sha256: e9aeb758123477b2c6f513c74b898d875f333cf7e67c11aeb7cdab69cd31e1cd
---
# Kamus Rule Number Validasi

Kamus Rule Number adalah dokumen yang berisi daftar Rule Number Validasi yang diterapkan untuk menjaga kualitas pengiriman data. Kamus ini dapat digunakan ketika user melakukan pengiriman data dan menemukan Rule Number pada response. Setiap rule number bersifat unik dan memiliki ketentuan yang berbeda.

### Contoh Response dengan Rule Number

```
{ "resourceType": "OperationOutcome",
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

User dapat menemukan Deksripsi Error untuk setiap Rule Number pada dokumen berikut:

## Dokumen Kamus Rule Number Validasi

[Unduh](https://docs.google.com/spreadsheets/d/1vnYFL2Ho1lICEgWmE2HFwkbEgiRvw1uaYBBW8NvwzjI/edit?gid=0#gid=0)

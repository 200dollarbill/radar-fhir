# Claude view — INDEX

One line per file. Format: `- <filename> — <topic>. Load when: <hint>`

- satusehat-observation.md — SATUSEHAT Observation profile (wajib elements, LOINC/UCUM systems) and its REST API. Load when: building or validating Observation / vital-sign endpoints.
- satusehat-patient.md — SATUSEHAT Patient profile, identifier systems (NIK, IHS number, nik-ibu, paspor, kk), MPI minimum data and the four search modes. Load when: implementing patient registration, lookup, or identifier validation.
- satusehat-practitioner.md — SATUSEHAT Practitioner profile (read-only master data, NIK search) and the PractitionerRole API (no profile page). Load when: modelling doctor accounts, practitioner lookup, or practitioner-organization links.
- satusehat-organization-location.md — SATUSEHAT Organization (suborganisation hierarchy, partOf) and Location (rooms/beds, serviceClass, position) profiles and APIs. Load when: designing facility structure, admin setup of organisations/locations, or Encounter.location / serviceProvider references.
- satusehat-encounter.md — SATUSEHAT Encounter profile (wajib identifier/status/class/subject/period/location/serviceProvider, statusHistory arrived→in-progress→finished, diagnosis) and API. Load when: designing visit lifecycle, Encounter validation, or the reference hub for clinical resources.
- satusehat-condition.md — SATUSEHAT Condition profile (one ICD-10 code per Condition; wajib code/subject/encounter) and API. Load when: implementing diagnosis entry or Condition validation.

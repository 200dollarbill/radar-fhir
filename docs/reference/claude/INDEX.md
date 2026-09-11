# Claude view — INDEX

One line per file. Format: `- <filename> — <topic>. Load when: <hint>`

- satusehat-observation.md — SATUSEHAT Observation profile (wajib elements, LOINC/UCUM systems) and its REST API. Load when: building or validating Observation / vital-sign endpoints.
- satusehat-patient.md — SATUSEHAT Patient profile, identifier systems (NIK, IHS number, nik-ibu, paspor, kk), MPI minimum data and the four search modes. Load when: implementing patient registration, lookup, or identifier validation.
- satusehat-practitioner.md — SATUSEHAT Practitioner profile (read-only master data, NIK search) and the PractitionerRole API (no profile page). Load when: modelling doctor accounts, practitioner lookup, or practitioner-organization links.

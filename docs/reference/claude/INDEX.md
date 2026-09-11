# Claude view — INDEX

One line per file. Format: `- <filename> — <topic>. Load when: <hint>`

- satusehat-observation.md — SATUSEHAT Observation profile (wajib elements, LOINC/UCUM systems) and its REST API. Load when: building or validating Observation / vital-sign endpoints.
- satusehat-patient.md — SATUSEHAT Patient profile, identifier systems (NIK, IHS number, nik-ibu, paspor, kk), MPI minimum data and the four search modes. Load when: implementing patient registration, lookup, or identifier validation.
- satusehat-practitioner.md — SATUSEHAT Practitioner profile (read-only master data, NIK search) and the PractitionerRole API (no profile page). Load when: modelling doctor accounts, practitioner lookup, or practitioner-organization links.
- satusehat-organization-location.md — SATUSEHAT Organization (suborganisation hierarchy, partOf) and Location (rooms/beds, serviceClass, position) profiles and APIs. Load when: designing facility structure, admin setup of organisations/locations, or Encounter.location / serviceProvider references.
- satusehat-encounter.md — SATUSEHAT Encounter profile (wajib identifier/status/class/subject/period/location/serviceProvider, statusHistory arrived→in-progress→finished, diagnosis) and API. Load when: designing visit lifecycle, Encounter validation, or the reference hub for clinical resources.
- satusehat-condition.md — SATUSEHAT Condition profile (one ICD-10 code per Condition; wajib code/subject/encounter) and API. Load when: implementing diagnosis entry or Condition validation.
- satusehat-procedure.md — SATUSEHAT Procedure profile (ICD-9 CM code; wajib status/code/subject/encounter, performer.actor) and API. Load when: implementing medical-action recording or Procedure validation.
- satusehat-related-person.md — SATUSEHAT RelatedPerson profile (NIK identifier, wajib patient reference, relationship codes; no API page). Load when: modelling guardians/family links to a Patient.
- satusehat-identifiers-and-master-data.md — Identifier system URIs (nik, nik-ibu, ihs-number, paspor, kk), IHS Number, MPI minimum data + create/search/patch rules for NIK / newborn / no-NIK patients, MSI facility lookup API, wilayah code formats. Load when: designing patient identity, registration flows, facility master data, or region codes.
- satusehat-datatypes.md — FHIR data types as the playbook restates them: primitive formats (date/dateTime/instant/id), complex-type JSON structures with wajib (*) / conditional (?) markers, Quantity/Reference rules. Load when: writing validators or serializers for element values.
- satusehat-rest-api-and-validation.md — Base URLs (sandbox/production), Bearer auth header, onboarding vs interoperability resource sets, validation pipeline, OperationOutcome shape and the printed RuleNumber → message table, UTC+00 time rule. Load when: designing the API gateway, auth, or error/validation responses.

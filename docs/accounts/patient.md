# Patient accounts

## Create the account

A patient account is linked to a Patient record that already exists. Find its ID first:
on **Sessions** (logged in as admin), the patient list shows `name · id`, for example
`Sesi S001 · P123...`. The seeded patient *Budi Santoso* is `P10000000001`.

```bash
source .env/prata.env
.venv/bin/python -m fhir_server add-account --role patient --username budi --ref Patient/P10000000001
```

It asks for the password twice and prints
`created patient budi (Patient/P10000000001)`. If the Patient does not exist it prints
`no Patient/...` and creates nothing.

The seeded database already has one patient login, `patient` (password `patient-pw`
unless `FHIR_PATIENT_PASSWORD` was set at seed time), linked to `Patient/P10000000001`.

## Log in

The login form is on the **Sessions** page (<http://127.0.0.1:8000/capture/sessions.html>
or <https://prata.haifa.workers.dev>).

## What this account can do today

- Logging in works, but the website has no patient page yet: after login, Sessions shows
  *This page is for admins and doctors.*
- Through the FHIR API, the patient can read **only their own** Patient record,
  Encounters and Observations, and nothing else:

  ```bash
  curl -s https://prata.haifa.workers.dev/fhir-r4/v1/Patient/P10000000001 \
    -H "Authorization: Bearer <login token from /auth/token>"
  ```

## Not built yet

> **Placeholder (not implemented yet):** the patient's own-record page: what a patient
> sees after logging in (their visits and recordings). Describe it here once designed.

> **Placeholder (not implemented yet):** how a real patient is registered and linked to
> their login. Today only test patients (*Sesi ...*) and the seeded *Budi Santoso* exist,
> and no real patient data is used.

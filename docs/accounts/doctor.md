# Doctor accounts

## Create the account

```bash
source .env/prata.env
.venv/bin/python -m fhir_server add-account --role doctor --username dr_ana --name "dr. Ana Putri"
```

It asks for the password twice and prints
`created doctor dr_ana (Practitioner/...)`. The command also creates the doctor's
**Practitioner** record (the FHIR record for a health worker), named as `--name` and with
a synthetic NIK starting `9900`, and links the login to it.

The seeded database already has one doctor login, `doctor`, linked to `Practitioner/N10000000`. Its
password is random, printed once in the JSON line `seed` ends with (`doctor_password`).
Databases seeded before 2026-11-19 used a published default instead: change it or disable
the login before the site goes online (`docs/RUN-GUIDE.md`, *Before going public*).

## Before the first login: give the doctor a patient

A doctor only sees patients they take part in. A new doctor therefore sees no patients
and cannot open a session yet. An admin does this once:

1. Log in as an admin on **Sessions**.
2. Open a session with the patient, a free board, a label, and this doctor in the
   **Doctor** field.

From then on the doctor sees that patient and can open further sessions for them.

## Log in

- On this laptop: <http://127.0.0.1:8000/capture/sessions.html>.
- From anywhere: <https://prata.haifa.workers.dev> (the laptop must be running
  `make server` and `make tunnel`).

## What this account can do today

- **Open sessions** on **Sessions** for patients they already take part in, and **end
  their own** sessions.
- **Record** on **Capture** with a board that has an open session.
- **Read** their patients, their own Encounters (sessions) and those sessions'
  Observations (recordings), through the FHIR API. The Review page shows a saved
  recording file.
- A doctor cannot register boards, create test patients, delete anything or manage
  accounts.

## Not built yet

> **Placeholder (not implemented yet):** the doctor's integrated patient view: the
> patient's RME (medical record), RADAR JVP and 12-lead ECG shown together in one view.
> This is the thesis goal; its design has not started. Describe here how a doctor opens
> a patient and reads the view.

> **Placeholder (not implemented yet):** a page listing the doctor's own patients and
> past recordings. Today this needs the FHIR API (`docs/RUN-GUIDE.md`, Step 10).

# Admin accounts

## Create the account

You already have one: `admin`, made when the database was seeded. Its password is the
`FHIR_ADMIN_PASSWORD` that was set at seed time. To give someone else admin rights,
create a named admin:

```bash
source .env/prata.env
.venv/bin/python -m fhir_server add-account --role admin --username supervisor1
```

It asks for the password twice and prints `created admin supervisor1`.

## Log in

- On this laptop: <http://127.0.0.1:8000/capture/sessions.html> (needs `make server`).
- From anywhere: <https://prata.haifa.workers.dev> (needs `make server` and
  `make tunnel` running on the laptop).

Log in on the **Sessions** page. The login lasts one hour and is shared by all tabs.

## What this account can do today

- **Register a board** (once per board): on **Capture**, connect the board (or **Use
  simulated board**), then click **Register this board**.
- **Create test patients:** on **Sessions**, *Test patients* → a label such as `S001` →
  **Create test patient**. This makes *Sesi S001* with a synthetic NIK. Only test patients
  are used; no real patient data.
- **Open a session for a doctor:** on **Sessions**, pick the patient, a free board, a
  label and the **doctor**, then **Open session**. This is also how a new doctor gets
  their first patient (see [doctor.md](doctor.md)).
- **End any session**, and see every session, board and patient.
- **Read and write every record** through the FHIR API (`/fhir-r4/v1/...`).
- **Manage accounts** with the laptop commands in [README.md](README.md). This works only
  on the laptop, never through the website.

## Not built yet

> **Placeholder (not implemented yet):** account management in the website. Today
> accounts are created only with `add-account` on the laptop, by design (the hosted
> Worker blocks the account API). Fill this in if a page for it is ever designed.

> **Placeholder (not implemented yet):** loading RME (medical record) and 12-lead ECG
> data for a patient. Describe here how an admin brings that data in once the doctor's
> integrated view is designed.

# Accounts

Anyone can open the PRATA site, but only accounts you create can log in. You create
them on the laptop, with commands. There is no sign-up page, and the account API is
blocked on the hosted site (the Worker answers 403
*Account management is only available on the PRATA laptop.*).

| Role | For | Linked to | Guide |
|---|---|---|---|
| admin | you, and anyone who manages boards, test patients and sessions | nothing | [admin.md](admin.md) |
| doctor | a doctor who opens sessions and reads their patients' recordings | a Practitioner record, made for them | [doctor.md](doctor.md) |
| patient | a person reading their own records | an existing Patient record | [patient.md](patient.md) |

What each role may see and do: `docs/HOW-IT-WORKS.md`, section 3.

## The three commands

Run them from the repo root, in a terminal where you have loaded your secrets file
(`source .env/prata.env`). They work on `data/fhir_server.db` and can run while the
server is running.

```bash
# create an account (the password is asked twice and never shown)
.venv/bin/python -m fhir_server add-account --role doctor --username dr_ana --name "dr. Ana Putri"
.venv/bin/python -m fhir_server add-account --role admin --username supervisor1
.venv/bin/python -m fhir_server add-account --role patient --username budi --ref Patient/P10000000001

# see every account
.venv/bin/python -m fhir_server list-accounts

# stop an account from logging in
.venv/bin/python -m fhir_server disable-account --username dr_ana
```

`list-accounts` prints one line per account, tab-separated:

```
username	role	ref	active
admin	admin	-	yes
doctor	doctor	Practitioner/N10000000	yes
```

## Rules

- **Usernames** are 3 to 32 letters, digits, dots, underscores or hyphens
  (`^[A-Za-z0-9._-]{3,32}$`). A username is never reused, even after the account is
  disabled.
- **Passwords** are typed twice at a hidden prompt. For scripts, put the password in an
  environment variable and pass its name: `--from-env NEW_PW`. Never put a password on
  the command line itself, where it would stay in the shell history.
- **Nothing is half-done.** A wrong username, a missing `--name` or `--ref`, a Patient
  that does not exist, or two different passwords at the prompt write nothing.
- **Disabling is immediate.** The person's next request is refused, even if they are
  logged in (their one-hour login token stops working at once).
- **Changing a password:** `set-password --username <name>` reads the new password from
  `FHIR_ADMIN_PASSWORD`, or from another variable with `--from-env NAME`
  (`docs/RUN-GUIDE.md`, setup note).

Exit codes, for scripts: `0` done, `1` the account already exists or the Patient was not
found, `2` the command was used wrongly.

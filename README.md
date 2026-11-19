# PRATA

A website that brings a patient's medical record (RME), RADAR JVP measurements and 12-lead
ECG into one view for the doctor. Final-year thesis project; the goal is in `CLAUDE.md`.

## Start here

You need Python 3.12+, Node 22 and `make`. From the repo root:

1. Install the server (once):

   ```bash
   make setup
   ```

2. Make your secrets file (once). The folder `.env/` is never committed:

   ```bash
   cat > .env/prata.env <<'EOF'
   export FHIR_JWT_SECRET=pick-any-long-random-string
   export FHIR_ADMIN_PASSWORD=pick-an-admin-password
   EOF
   ```

3. Start the server and leave the terminal open (`Ctrl+C` stops it):

   ```bash
   make server
   ```

4. Open <http://127.0.0.1:8000/capture/sessions.html> and log in as `admin`.

The first time, the database has to be created: see Step 1 of `docs/RUN-GUIDE.md`. That
guide also covers flashing the board, recording and troubleshooting.

## Hosted site

The same website is online at <https://prata.haifa.workers.dev>. Anyone can open it, but
only accounts you create can log in (`docs/accounts/`). The data stays in this laptop's
database: the site is a Cloudflare Worker that passes every request to the laptop.

It works only while the laptop runs both, each in its own terminal:

```bash
make server     # terminal 1
make tunnel     # terminal 2: connects the laptop to Cloudflare
```

After changing pages in `website/` or the Worker in `hosting/`, publish them with
`make deploy`. Server changes need no deploy, only a restart of `make server`.

## Folder map

```
PRATA/
├── README.md        you are here
├── Makefile         every command: run `make` to list them
├── fhir_server/     the server (Python, FastAPI): stores and checks all data
├── website/         the pages: Sessions, Capture, Review (served at /capture/)
├── firmware/        radar_json/: the AtomS3R board's program
├── hosting/         the Cloudflare Worker that puts the website online
├── device_client/   a Python stand-in for the board, used by tests
├── tests/           server tests
├── tools/scrape/    scraper and linter for the FHIR/SATUSEHAT reference pages
├── data/            sample recordings (CSV) and the local databases (*.db, never committed)
├── docs/
│   ├── RUN-GUIDE.md full walkthrough: server, board, website
│   ├── HOW-IT-WORKS.md how the parts fit together
│   ├── accounts/    setting up admin, doctor and patient logins
│   ├── design/      specs/, plans/, reports/: how each part was designed and built
│   ├── reference/   FHIR and SATUSEHAT reference (raw pages, condensed notes, guides)
│   ├── eval/        generated evaluation reports (do not edit by hand)
│   └── proposal_md/, papers/, presentation/, notul/, handover/ ...   thesis material
├── Local/           owner's notes and the Android apk (apk is never committed)
└── CLAUDE.md, proposal_CLAUDE.md   instructions for Claude
```

## Everyday commands

```
make help       list commands
make setup      create .venv, install the server and the hosting tools
make server     run the server on http://127.0.0.1:8000 (website at /capture/)
make test       run every test suite
make firmware   compile the board firmware
make flash      compile and upload to the board (PORT=/dev/ttyACM0)
make eval       rescore the display methods (rewrites docs/eval/)
make tunnel     connect this laptop to Cloudflare (keep running next to `make server`)
make deploy     build the website and deploy the Worker
```

## Secrets

All secrets live in `.env/prata.env`, which you make yourself (step 2 above). The whole
`.env/` folder is gitignored, so it never reaches GitHub. `make server` loads it for you.
Never put a password or token in a command line, a commit or a document.

## Old names

Older specs, plans and handovers use the names from before 2026-11-19:

| Old | New |
|---|---|
| `receiver/` | `website/` |
| `arduino/radar_json/` | `firmware/radar_json/` |
| `docs/.superpowers/` | `docs/design/` |
| `.superpowers/sdd/` | `docs/design/reports/` |
| `docs/implementation/` | `docs/design/plans/` |
| `.tools/scrape/` | `tools/scrape/` |
| `fhir_server.db` (repo root) | `data/fhir_server.db` |
| `python_receiver/` | removed (still in git history) |

## Read next

- `docs/HOW-IT-WORKS.md`: how the whole program fits together, from radar to database.
- `docs/accounts/README.md`: creating admin, doctor and patient accounts.
- `docs/RUN-GUIDE.md`: the full walkthrough.
- `docs/design/specs/`: why each part works the way it does.
- `CLAUDE.md`: project brief and conventions.
- `proposal_CLAUDE.md`: the thesis direction.

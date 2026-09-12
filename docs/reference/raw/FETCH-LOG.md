# Fetch log

| Run date (UTC) | Sources | Written | Failed |
|---|---|---|---|
| 2026-09-11 | 94 | 93 | 1 |

## Failed sources

| id | url | reason | action |
|---|---|---|---|
| res-device | https://satusehat.kemkes.go.id/platform/docs/id/fhir/resources/device/ | HTTP 200 but page title is "Redirect Notice" — SATUSEHAT has no published Device resource page | kept in `sources.yaml` as `expected_missing: true`; verified by `curl -sL -A "fhir-reference-compiler/0.1 (student project)"` — confirmed with `grep -o '<title>...'` that the response is a redirect-notice stub, not a real resource page; no working alternate URL exists on the site navigation |
| res-practitioner-role | https://satusehat.kemkes.go.id/platform/docs/id/fhir/resources/practitioner-role/ | HTTP 200 but page title is "Redirect Notice" — SATUSEHAT has an API page for PractitionerRole (`api-catalogue/integrations/apis/practitioner-role/`) but no profile page | added to `sources.yaml` as `expected_missing: true`; probed 2026-09-12 with `curl -sL -A "fhir-reference-compiler/0.1 (student project)"` — confirmed with `grep -o '<title>...'` that the response is a redirect-notice stub; no working profile-page URL exists on the site navigation |

## check.py verification

Ran `python3 tools/scrape/check.py` immediately after the scrape (2026-09-11):

```
changed: 1, missing-local: 1, unchanged: 92
```

- `missing-local res-device` — expected: `res-device` failed in Step 1 and was never written, so there is no local file to hash.
- `changed term-loinc-laboratory` — investigated by diffing two consecutive raw HTML fetches of
  `https://satusehat.kemkes.go.id/platform/docs/id/terminology/loinc/laboratory/` seconds apart: the page embeds three
  Cloudflare "email-protection" obfuscation links (`/cdn-cgi/l/email-protection#<hex>`), and Cloudflare re-randomizes the
  XOR key on every request, so the hex fragment (and therefore the extracted Markdown body, which includes the link) differed
  on every single fetch even though the visible content ("[email protected]" placeholder text) was identical. Re-ran `check.py`
  twice more at the time — it reported `changed` for `term-loinc-laboratory` every time.

**Fixed 2026-09-12.** Rather than leave this as a permanent false positive, `tools/scrape/convert.py::html_to_markdown` now
normalises `email-protection#[0-9a-fA-F]+` → `email-protection` before hashing, so the unstable hex fragment never reaches
the stored Markdown or its sha256. `term-loinc-laboratory` was re-fetched with `python3 tools/scrape/scrape.py --only
term-loinc-laboratory` (new `sha256: 4746a67bdb50...`, `fetched_at: 2026-09-12T09:37:20Z`). A full `python3
tools/scrape/check.py` run afterwards reports:

```
expected-missing: 2, unchanged: 93
```

`term-loinc-laboratory` is now `unchanged` like every other source; the two `expected-missing` entries are `res-device` and
`res-practitioner-role` (see Failed sources above and `expected_missing: true` in `sources.yaml`) — both now correctly
skipped rather than counted as failures or drift.

## Spot-check (Step 2)

- `docs/reference/raw/satusehat/res-observation.md` and `docs/reference/raw/fhir-r4/observation.md` both start with `---`
  front matter containing all seven keys (`id`, `title`, `source_url`, `group`, `fhir_version`, `fetched_at`, `sha256`),
  followed by readable Indonesian / English body text.
- Total line count across all raw files: `wc -l docs/reference/raw/*/*.md` → **48163** (including the per-file total line).
- `grep -L '^sha256:' docs/reference/raw/*/*.md` → no output (every written file has a sha256 line).
- `grep -ril '<script' docs/reference/raw/*/*.md` → one hit, `raw/fhir-r4/security.md` — a quoted XSS example in the
  spec's own prose ("...content-type \"text/html\" and has content like \"<script>send\_to\_attacker(document.cookie);</script>\"."),
  not a leaked live `<script>` tag; benign.
- No site-wide nav menus were found. Note: `fhir-r4/observation.md` (and other HL7-published pages) include a short,
  page-local sub-navigation list copied from the source page itself (e.g. `- [Content](#)`, `- [Examples](...)`,
  `- [Detailed Descriptions](...)`) — these are the FHIR spec's own in-page section tabs, not a site-wide menu, and were
  already accepted by the extractors built and tested in Tasks 1-4.

## Notes

- 94 sources were defined in `tools/scrape/sources.yaml` at the time of the original 2026-09-11 run; 93 written
  successfully, 1 documented failure (`res-device`). A second gap (`res-practitioner-role`) was added on 2026-09-12
  (see F2/S2), bringing the total to 95 sources with 93 written and 2 documented, structurally-tracked gaps.
- No source URLs needed to be corrected in `sources.yaml` during either run — both failures (`res-device`,
  `res-practitioner-role`) were confirmed to be genuinely missing pages, not moved ones.
- Re-run `python3 tools/scrape/scrape.py` and `python3 tools/scrape/check.py` to detect upstream changes.
  `scrape.py` exits `0` when the only per-source problems are `expected_missing` sources (printed as
  `skip  <id>: expected missing` and excluded from the failure count); any other failure still makes it exit `1`.
  `check.py` exits `0` when every source reports `unchanged` or `expected-missing`, and prints a summary line like
  `expected-missing: 2, unchanged: 93`. Expect `res-device` and `res-practitioner-role` to always report
  `expected-missing` — that is not drift. Treat any id reported `changed` or `failed` as a real signal worth
  investigating for the validity review. (The Cloudflare email-obfuscation instability that used to make
  `term-loinc-laboratory` falsely report `changed` on every run was fixed on 2026-09-12 by normalising the unstable
  hex fragment in `convert.py`; see the check.py verification section above.)

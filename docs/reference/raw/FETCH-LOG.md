# Fetch log

| Run date (UTC) | Sources | Written | Failed |
|---|---|---|---|
| 2026-09-11 | 94 | 93 | 1 |

## Failed sources

| id | url | reason | action |
|---|---|---|---|
| res-device | https://satusehat.kemkes.go.id/platform/docs/id/fhir/resources/device/ | HTTP 200 but page title is "Redirect Notice" — SATUSEHAT has no published Device resource page | kept in `sources.yaml` as a documented gap; verified by `curl -sL -A "fhir-reference-compiler/0.1 (student project)"` — confirmed with `grep -o '<title>...'` that the response is a redirect-notice stub, not a real resource page; no working alternate URL exists on the site navigation |

## check.py verification

Ran `python3 tools/scrape/check.py` immediately after the scrape:

```
changed: 1, missing-local: 1, unchanged: 92
```

- `missing-local res-device` — expected: `res-device` failed in Step 1 and was never written, so there is no local file to hash.
- `changed term-loinc-laboratory` — **not a real content change**. Investigated by diffing two consecutive raw HTML fetches of
  `https://satusehat.kemkes.go.id/platform/docs/id/terminology/loinc/laboratory/` seconds apart: the page embeds three
  Cloudflare "email-protection" obfuscation links (`/cdn-cgi/l/email-protection#<hex>`), and Cloudflare re-randomizes the
  XOR key on every request, so the hex fragment (and therefore the extracted Markdown body, which includes the link) differs
  on every single fetch even though the visible content ("[email protected]" placeholder text) is identical. Re-ran `check.py`
  twice more — it reported `changed` for `term-loinc-laboratory` every time. This is the only file in the raw corpus containing
  a `cdn-cgi/l/email-protection` link (`grep -l 'cdn-cgi/l/email-protection' docs/reference/raw/*/*.md`). Documenting this as a
  known limitation rather than fixing the extractor, since Task 5 is scrape-and-commit only: future `check.py` runs will always
  flag this one id as "changed" and that should be treated as a false positive, not a real upstream edit, unless the rest of
  the page's visible text also differs.

Excluding these two expected/explained entries, all 92 other sources were reported `unchanged` on the immediate re-check.

## Spot-check (Step 2)

- `docs/reference/raw/satusehat/res-observation.md` and `docs/reference/raw/fhir-r4/observation.md` both start with `---`
  front matter containing all seven keys (`id`, `title`, `source_url`, `group`, `fhir_version`, `fetched_at`, `sha256`),
  followed by readable Indonesian / English body text.
- Total line count across all raw files: `wc -l docs/reference/raw/*/*.md` → **48163** (including the per-file total line).
- `grep -L '^sha256:' docs/reference/raw/*/*.md` → no output (every written file has a sha256 line).
- `grep -ril '<script' docs/reference/raw/*/*.md` → no output (no raw `<script` tags leaked into any Markdown file).
- No site-wide nav menus were found. Note: `fhir-r4/observation.md` (and other HL7-published pages) include a short,
  page-local sub-navigation list copied from the source page itself (e.g. `- [Content](#)`, `- [Examples](...)`,
  `- [Detailed Descriptions](...)`) — these are the FHIR spec's own in-page section tabs, not a site-wide menu, and were
  already accepted by the extractors built and tested in Tasks 1-4.

## Notes

- 94 sources defined in `tools/scrape/sources.yaml`; 93 written successfully, 1 documented failure (`res-device`).
- No source URLs needed to be corrected in `sources.yaml` during this run — the only failure (`res-device`) was confirmed
  to be a genuinely missing page, not a moved one.
- Re-run `python3 tools/scrape/check.py` to detect upstream changes. Expect `term-loinc-laboratory` to always show as
  `changed` due to Cloudflare's per-request email obfuscation (see above); treat any *other* id reported as `changed` as a
  real signal worth investigating for the validity review.

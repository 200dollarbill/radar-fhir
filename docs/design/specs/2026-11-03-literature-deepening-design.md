# Literature deepening for research justification and urgency

## Purpose

Find papers that strengthen the justification and urgency of the thesis,
especially the link between JVP signal features and cardiovascular health. The
owner reads and downloads the papers. This work supplies links, abstracts and a
view of where the argument is strong or weak.

## Argument chain

Searches are organised by the claim each paper would support, so gaps in the
argument are visible. Effort is weighted towards L3 and L4.

| Link | Claim to test | Priority |
|---|---|---|
| L1 | Heart failure burden and readmission are high, including Indonesian figures (still missing) | Normal |
| L2 | Residual congestion drives readmission, and venous pressure rises before symptoms | Normal |
| L3 | JVP waveform features (a, c, v, x, y, intervals, ratios) carry cardiovascular information beyond a single height value, and which conditions each maps to | **Highest** |
| L4 | A single JVP measurement at discharge or in clinic has value. This answers the professor's "measurement, not monitoring" and thermometer objections | **Highest** |
| L5 | Bedside JVP assessment is limited, so objective quantitative measurement is needed | Normal |
| L6 | RADAR can capture those waveform features, not only the pulse. Includes signal derivation, quality and validation against USG or catheter | High |
| L7 | JVP is only meaningful with patient context, so combining it with RME and ECG is justified | High |
| L8 | Integrated display and CDSS design: visual synthesis, clinician burden, adoption of assistive systems | Normal |

**Counter-evidence is required for every link**, especially L3, L4 and L7. For
example, source [12] argues JVP has no independent prognostic value after
matching. Examiners will raise this, so the owner needs to see it first.

## Method

1. Build the exclusion list of known papers from `docs/papers/` and
   `docs/proposal_md/daftar_sumber_dan_klaim.md`.
2. Run several differently worded Exa searches per link, using clinical and
   engineering vocabulary (for example "jugular venous waveform", "right atrial
   pressure waveform", "x descent", "y descent", "FMCW radar jugular").
3. Follow citations from the strongest L3 and L6 results.
4. Fetch the abstract and metadata from the publisher, PubMed or PMC page.
5. Deduplicate by DOI, then by normalised title.

**Source filter:** prefer peer-reviewed papers, reviews and guidelines. Label
preprints as preprints. Exclude patents and SlideShare, per the proposal guide.

**Volume:** about 15 to 25 candidates each for L3 and L4, and about 8 to 15 for
the other links. Fewer is acceptable and is reported as a finding.

## Output

All files go in `docs/papers/search/`:

| File | Content |
|---|---|
| `README.md` | Argument chain, per-link strength assessment, gaps, search log (query, date, result count) |
| `L3-jvp-waveform.md` and one file per other link | The entries for that link |
| `download-list.md` | All entries in one list, by priority, with links for downloading |

Each entry contains:

- Title, authors, year, venue, publication type, DOI and URL.
- Abstract, copied as found.
- Link, and whether it supports, contradicts or qualifies the claim.
- Whether the owner already has it (P-number).
- A one-line relevance note, labelled as Claude's note.

## Integrity rules

- Abstracts are copied from the source. If one cannot be retrieved, the entry
  says "abstract not retrieved" and nothing is written in its place.
- Bibliographic details come from the source page. A DOI that was not seen on a
  source page is left blank.
- Strength assessments are based on abstracts only, and say so.
- Nothing is added to `proposal.md`, `citations.md` or
  `daftar_sumber_dan_klaim.md`. The owner reads the papers first.
- Absence claims, such as "no study combines radar JVP with RME", are reported
  as "not found in these searches", not as proof of absence.

## Dependencies

Exa access through the installed plugin, which needs the owner's authentication.
If it is unavailable, stop and report it. Do not substitute another source
without telling the owner.

## Success criteria

- Every link in the chain has a strength assessment and any gaps are named.
- L3 states which waveform features have evidence for which conditions, and how
  good that evidence is.
- L4 gives the owner evidence for or against the value of a single measurement.
- Every entry has a working link for downloading.

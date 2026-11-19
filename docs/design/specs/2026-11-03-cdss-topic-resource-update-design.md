# Align Claude's resources with the CDSS topic

## Problem

The thesis moved from a FHIR profile for the RADAR JVP device to a clinical
decision support system (CDSS). `docs/proposal_md/proposal.md` (2026-10-26) has
the new topic, but the files that brief Claude still describe the old one. One
of them, `proposal_CLAUDE.md`, explicitly instructs "do not frame the thesis as
diagnosis or decision support". There is also no auto-loaded brief:
`CLAUDE.md` is deleted in the working tree and `project_CLAUDE.md` is an
identical copy under a name that does not load.

## Decisions

| Topic | Decision |
|---|---|
| Title | *Pengembangan Sistem Pendukung Keputusan Klinis Berbasis Interoperabilitas Data Rekam Medis Elektronik dan Pengukuran Kardiovaskular RADAR* (still a working title) |
| Final objective | A working website that takes in RME, RADAR JVP and 12-lead ECG data and displays it visually and efficiently in one view for the doctor |
| Meaning of decision support | The integrated display is the decision support. The doctor decides |
| Rule-based flags or recommendations | Not required. Optional only if time remains |
| Output framing | Never diagnosis, prediction or a validated risk score |
| Device wording | "Pengukuran", not "monitoring", for the RADAR device |
| FHIR and SATUSEHAT | The interoperability bridge and canonical data format, not the headline contribution |
| Contribution | The system: data management, integration, interoperability. Not the RADAR device and not an interpretation algorithm |
| Existing FHIR server | The base the website builds on |
| Next phase | Literature deepening, with the JVP signal link to cardiovascular health first. See `2026-11-03-literature-deepening-design.md` |
| Website architecture | Not designed here. It gets its own brainstorm after the literature phase |

## Changes

### `CLAUDE.md` (restored, rewritten, under about 120 lines)

Auto-loaded every session, so it holds only what every session needs:

- Current topic, final objective and next phase.
- Repo map, pointing to `proposal_CLAUDE.md` for thesis work and
  `docs/reference/claude/INDEX.md` for FHIR facts.
- The server constraints, process rules, execution techniques, commands and
  conventions carried over from `project_CLAUDE.md`.
- Server status: walking skeleton implemented. Public-exposure spec
  (2026-10-08) written but not implemented. The device-profile roadmap item is
  no longer the headline goal.

`project_CLAUDE.md` is deleted once its content is merged, since `CLAUDE.md`
replaces it.

### `proposal_CLAUDE.md` (rewritten as the CDSS handoff)

| Section | Treatment |
|---|---|
| Project summary, title | Rewrite for the CDSS topic and final objective |
| Direction history | Keep V1 and the professor's critique, then record the CDSS as current so it is not relitigated |
| Scope boundary | Rewrite: integrated display required, rule-based flags optional, synthetic RME data, no clinical validation |
| Fishbone | Replace with a pointer to `docs/presentation/ets/fishbone.md`, the current version |
| Urgency defense | Rewrite around the argument chain in the literature spec. Keep the "concede measurement, not monitoring" stance and the honest-weakness note |
| Draft status and fix list | Replace with the fix list below, after checking each old item against the current `proposal.md` |
| Evidence gathered, FHIR background | Keep what still applies, keep TODO-verify marks |
| Open questions | Replace with current ones |
| Working preferences | Replace the "no decision support" rule with the framing rules above. Add the style rules pointer to `docs/proposal_guide/panduan_proposal.md` |

New section, research logistics from `docs/notul/konsultasi_15okt.txt`: four
students share the research tree, data collection is at Soetomo in a polyclinic
rather than inpatient, USG is the JVP validator, the notes suggest about 100
samples, and the named clinical contacts and their roles.

### Open items to record, not fix

`proposal.md` is not edited. These go in the handoff's fix list:

1. Section 1.4 says "diagnosa penyakit kardiovaskular", while 1.3 and 2.7 say
   the output is not a diagnosis.
2. Section 2.7 mentions "luaran rekomendasi", which should be softened to match
   the display-first objective.
3. Section 1.1 gives 27% as six-month readmission, while BAB II gives 27.66% as
   six-month mortality from the same source [3]. Check against the paper.
4. Section 1.1 calls heart failure a "gejala fisiologis" of stroke and IHD.
   Check the wording and the claim.
5. Section 1.1 still says "pergerakan akustik jantung", flagged earlier as
   wrong because the motion is mechanical.
6. Unresolved placeholders: `[new]`, "Survey oleh cite", "terbuktikan oleh cite",
   the `[cite: ...]` markers, and the citation-repair notes at the end of the file.
7. Section 2.6 is empty and BAB III is not written.
8. The PGHD definition says "diluar kunjungan klinis", while the data collection
   plan is in a polyclinic. Decide whether RADAR data counts as PGHD here.
9. Whether patient save-and-send is a committed feature. The supervisor has not
   confirmed it.

### `docs/reference/human/16-project-proposal-brief.md` and its README line

Update the goal, the contribution statement and the roadmap to the CDSS topic.
Keep the claim-boundary text and the FHIR methodology, which still apply.

### `docs/reference/claude/INDEX.md`

Reword the "load when" notes so a device profile is one possible use, not the
assumed goal. Add a line stating that these files are FHIR and SATUSEHAT facts,
independent of the thesis topic. The linter must still print `0 problem(s)`.

## Not changed

- `proposal.md`, `panduan_proposal.md`, `bab2_outline.md`, `fishbone.md`.
- `docs/reference/raw/` and the fact content of `docs/reference/claude/*`.
- Past specs and plans, which stay as history.
- Server code.
- The published human-reference site. Republishing is a separate step for the
  owner to request.

## Security item for the owner

`.env/notes.env` is tracked in git even though `.env` is in `.gitignore`. It has
not been opened. The owner should check whether it holds real secrets. Any fix
is a separate decision, because removing it from history rewrites commits.

## Verification

- `grep` the rewritten files for the old title and for instructions against
  decision support. Mentions may remain only in the direction history.
- `python3 .tools/scrape/lint_views.py` prints `0 problem(s)`.
- Every file path named in `CLAUDE.md` and `proposal_CLAUDE.md` exists.
- Every fix-list item is re-checked against `proposal.md` when written.

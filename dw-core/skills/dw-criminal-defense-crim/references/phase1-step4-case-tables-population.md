# Phase 1 Step 4 — Build Case Tables (Population Detail)

Read from SKILL.md **Phase 1 Step 4** — Evidence Table column-by-column population, Review Priority and Defense Relevance rules, Witness List columns and 1–5 ranking, and the Step 4 Check.

⚠ **Follow the Case Tables Write Protocol before modifying this file.** See "Case Tables Write Protocol" section above.

**4a — Evidence Table**
Populate the **Evidence Table Sheet** with the full exhibit catalog. As of v6.1 this sheet is an **admissibility worksheet**, not a discovery-intake index: it answers "how does this exhibit get in, through whom, and what is the State going to say about it." Discovery-intake tracking (what arrived, when, in which set, whether it is complete) lives in the Download Log and the `Bate Stamp Master Log.xlsx`; substantive triage lives in the Phase 2 Step 1A Triage Routing Memo.

| # | Column | How Populated |
|---|--------|---------------|
| 1 | Evidence Number | Auto — 3-digit file name prefix (001, 002, …), matching the document naming convention |
| 2 | Evidence Name | Auto — file name. Append `— SUPERSEDED by [Evidence Number]` when a later production replaces it (Phase 3 Step 3) |
| 3 | Number of Pages | Auto — page count. For audio/video, enter runtime as `A/V — HH:MM:SS`; for a transcript of that media, the transcript's own page count |
| 4 | Bate Stamp Range | Auto — cross-referenced to `Bate Stamp Master Log.xlsx`, written as a range (`DW-000123–000145`). Single-page items repeat the number |
| 5 | Sponsoring Witness ★ | **Cowork proposes, attorney confirms** — the witness through whom this exhibit is offered. Must match a `Witness Name` on the Witness List exactly (`Last, First`); if no sponsor is identified yet, enter `UNASSIGNED` |
| 6 | Authentication Route ★ | **Cowork proposes, attorney confirms** — dropdown; see the legend below |
| 7 | Anticipated Objections ★ | **Cowork proposes, attorney confirms** — comma-separated shorthand codes; see the legend below |

*Cowork's proposals on columns 5–7 are preliminary. Attorney confirmation is required on every row before the exhibit list is treated as trial-ready.*

**Authentication Route legend** — the dropdown values and the La. C.E. article each one runs on:

| Dropdown Value | Governing Article | Use When |
|---|---|---|
| Witness with Knowledge | La. C.E. art. 901(B)(1) `[VERIFY]` | A witness can testify the item is what it is claimed to be |
| Chain of Custody | La. C.E. art. 901(A) `[VERIFY]` | Fungible or seized physical evidence requiring custodial continuity |
| Distinctive Characteristics | La. C.E. art. 901(B)(4) `[VERIFY]` | Appearance, contents, substance, or internal patterns identify it |
| Voice or Speaker ID | La. C.E. art. 901(B)(5)–(6) `[VERIFY]` | Recorded calls, jail calls, voicemail |
| Process or System | La. C.E. art. 901(B)(9) `[VERIFY]` | Body cam, surveillance systems, forensic extraction output, lab instrumentation |
| Certified Public Record | La. C.E. art. 902 `[VERIFY]` | Certified court, agency, or public records |
| Certified Business Record | La. C.E. art. 902(11) with the art. 803(6) hearsay exception `[VERIFY]` | Medical, phone, bank, or other business records with a custodian certificate |
| Self-Authenticating | La. C.E. art. 902 `[VERIFY]` | Any other art. 902 category |
| Stipulated | — | Written stipulation on file; note the stipulation's document number in the objections cell |
| Contested — Motion Required | — | Authentication will be fought. Route to **dw-suppression-motion-crim** or **dw-expert-witness-evaluator-crim** |
| TBD | — | Not yet assessed |

⚠ **These article numbers are cited from memory and must be verified against the current Code before any filing or trial use — Louisiana amends the Code of Evidence frequently.** Treat every `[VERIFY]` above as an open item until checked.

**Anticipated Objections legend** — comma-separated shorthand:

| Code | Meaning |
|---|---|
| `HEARSAY` | La. C.E. arts. 801–806 `[VERIFY]` |
| `RELEVANCE` | La. C.E. arts. 401–402 `[VERIFY]` |
| `403` | Probative value substantially outweighed by prejudice `[VERIFY]` |
| `AUTH` | Authentication or foundation defect, La. C.E. art. 901 `[VERIFY]` |
| `BEST EVIDENCE` | La. C.E. arts. 1002–1004 `[VERIFY]` |
| `404(B)` | Other crimes evidence — route to **dw-404b-opposition-crim** |
| `CONFRONTATION` | Testimonial hearsay, *Crawford v. Washington*, 541 U.S. 36 (2004) |
| `PRIVILEGE` | La. C.E. arts. 501 et seq. `[VERIFY]` |
| `CUMULATIVE` | Duplicative of an already-admitted exhibit |
| `NONE ANTICIPATED` | No objection expected |

**4b — Witness List** (`Witness List` sheet — single consolidated sheet, 4 columns)
Extract every witness name encountered during discovery organization and transcription. Enter each on the one `Witness List` sheet, sorted **alphabetically by Last, First**. `Priority` is a sortable column — do not keep separate alpha/priority sheets.

| # | Column | How Populated |
|---|--------|---------------|
| 1 | Witness Name | Auto/Staff — `Last, First` |
| 2 | Role in Case | Auto/Staff — the witness's function (e.g. lead detective, eyewitness, DNA analyst, records custodian, defendant, co-defendant) |
| 3 | Priority | **Cowork** — `N – Label` per `references/witness-priority-rubric.md`; attorney confirms |
| 4 | Key Evidence Sources | Auto — Bate refs and file names of every statement, report, recording, and exhibit tied to this witness, comma-separated |

**Rank every witness 1–5** using the first-match decision rule in `references/witness-priority-rubric.md` (1 – Critical … 5 – Peripheral). Read the selected defense theory from the Case Profile FIRST, then rank each witness by importance to that theory and to the State's burden. Write the rank as `N – Label`. Flag unconfirmed roles as `5 (prov.)` and re-rank as discovery arrives.

Ranking rationale, impeachment material, addresses, and exam-prep tracking are **not** kept on this sheet — they belong in Report 8 (Key Witness Impeachment Plan) and the per-witness worksheets in `01 - Trial Notebook/03 - Witnesses/`.

**✓ Step 4 Check:**
- [ ] Evidence Table row count matches file count in Evidence Folder
- [ ] Bate Stamp Range populated for every row and reconciled against `Bate Stamp Master Log.xlsx`
- [ ] Sponsoring Witness populated for every row (`UNASSIGNED` is acceptable at this stage) and every named sponsor appears on the Witness List
- [ ] Authentication Route and Anticipated Objections populated for every row (`TBD` acceptable at this stage)
- [ ] Witness List populated (all 4 columns), sorted alphabetically, and ranked 1–5 per witness-priority-rubric.md

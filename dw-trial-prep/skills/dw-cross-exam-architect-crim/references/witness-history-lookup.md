# Witness History Lookup — Have We Crossed This Witness Before?

**Applied at Step 0.58, before drafting. Cheap to run, compounding in value.**

The firm practices in seven parishes with a finite number of officers, forensic analysts, and expert witnesses. The same Calcasieu deputy, the same SWLA analyst, the same State expert will appear across matters for years. **Every prior cross of that witness is an asset the firm already owns.** A rotating prosecutor's office cannot build the equivalent.

This is also a defense against the opposite risk: crossing a witness on a theory that already failed against him, or repeating a question he has now had two years to prepare an answer for.

---

## 1. Where to Look

Prior cross-examination deliverables follow a fixed filename pattern (`deliverable-formatting.md` §4), which makes them findable:

```
Cross-Examination — [Witness Name].docx
```

Outlines built before this skill dropped the companion PDFs may still have a `Source Catalog — [Witness Name].pdf` and a `Combined Sources — [Witness Name].pdf` beside them. Read those where they exist; never create new ones.

They live under each matter's `01 - Trial Notebook/03 - Witnesses/Prosecution Witnesses/`.

**Search all three case sources** — a witness crossed on a public defender case may reappear on a private retainer, and the firm's memory should not be siloed by billing arrangement:

| Source | Where |
|---|---|
| Calcasieu PDO | `Shared drives/CALCASIEU PDO Files/` |
| NOLA Conflict | `Shared drives/NOLA Conflict Cases/` |
| D&W private | `Shared drives/D&W Law Firm (CJW)/` |

Search by **witness surname** across `03 - Witnesses/` subfolders in all three. Also check for the witness's name inside prior Master Witness Tables, DMARs, and auditor reports — a witness may have been analyzed in a matter that never reached a cross outline.

**DEVONthink:** if the firm indexes case files (not only the `Law Library-Criminal` template database), search there as well. Query by surname plus a role term:

```
query: "[Surname]" AND ("cross-examination" OR "officer" OR "analyst")
```

Consult `dw-shared-protocols-crim/references/devonthink-search-patterns.md` for current database names and conventions.

**Multi-case and co-defendant matters:** route through `dw-dmar-synthesizer-crim`, which performs cross-case witness comparison across DMARs and will surface overlapping witnesses the folder search may miss.

---

## 2. What to Extract From a Prior Cross

When a prior outline is found, pull:

- **Chapters used** and, if the Preservation Log was completed, **which lines the court allowed**
- **Rulings** — a sustained objection last time is a preview of the objection this time. Come with the ground pre-briefed
- **Concessions the witness actually made** — a concession given once under oath is a prior statement now (La. C.E. art. 613), and it is sworn
- **Where the witness fought** — the Fragility scores from the prior LE module, if recorded
- **Impeachment that was used and burned** — a contradiction already confronted has a rehearsed answer waiting
- **The transcript of the prior cross itself**, if the matter was tried. This is the single most valuable artifact: the witness's own sworn words, obtained by this firm, on a subject you are about to raise again

---

## 3. Conflicts and Ethics Check — Run Before Using Anything

**Stop and confirm with the attorney before importing any material from another client's file.**

Prior case files belong to prior clients. Work product from Client A's matter is Client A's confidential information, and using it in Client B's matter is not automatically permissible.

- **Public record is always safe.** Trial transcripts, filed pleadings, and open-court testimony are public. A witness's sworn testimony in an open proceeding may be used freely.
- **The firm's own analysis is not automatically portable.** A cross outline, a witness card, or an investigator memo prepared for a prior client is that client's work product. Whether it can inform a new matter is a judgment call for the attorney, not for this skill.
- **A former client's confidential information is protected** and does not become usable because the same officer is testifying. `[VERIFY]` — the applicable analysis runs through the Louisiana Rules of Professional Conduct (Rules 1.6, 1.9, and 1.7 as relevant). **Confirm with the attorney before proceeding; this skill does not resolve conflicts questions.**

**Practical rule for this skill:** surface *that* a prior cross exists and *where*, extract freely from public-record material, and **ask before importing firm work product from another client's matter.** Never silently merge it into a new outline.

---

## 4. Output — Witness History Note

When a prior encounter is found, add this block to the Step 2 Pre-Draft Confirmation:

> **WITNESS HISTORY:** [Witness Name] was crossed by this firm in [Matter], [Parish], [Date].
> - Prior outline: `[path]`
> - Chapters used: [list]
> - Rulings, if logged: [sustained/overruled by chapter]
> - Concessions obtained: [list — these are prior sworn statements now]
> - Impeachment already burned: [list — expect a rehearsed answer]
> - Public-record material available: [trial transcript / hearing transcript / none]
> - **Conflicts check required before importing firm work product — attorney to confirm.**

When nothing is found, say so explicitly: `WITNESS HISTORY: no prior D&W cross located for this witness.` Silence is ambiguous — the attorney cannot tell whether the search ran.

---

## 5. Build the Asset Going Forward

The lookup only pays if the underlying record is maintained.

- Every cross outline this skill produces is already saved under a predictable name and path — that is what makes this search work. **Do not deviate from the naming convention.**
- Record the completed **Preservation Log** in the outline after trial. Rulings are the most valuable thing in a prior cross and the most easily lost.
- Where the firm keeps a witness index or Case Tables workbook, add a row for each witness crossed: name, agency, matter, date, parish, division, outcome, link. Route through `dw-case-brain-crim` for registration.
- Over time this becomes a firm-specific database of how particular officers and analysts perform under cross in particular divisions. That is a durable advantage.

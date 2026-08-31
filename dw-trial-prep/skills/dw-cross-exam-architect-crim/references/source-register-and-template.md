# Source Register & Cross-Examination Outline Template

## Source Register (Mandatory — Build Before Drafting Any Chapter)

Before writing any chapter, build a **Source Register** — a numbered master list of every source document that will be cited in the cross-examination. Each source receives a permanent number `(1)`, `(2)`, `(3)`, etc. that is used as a prefix in every SOURCE/EXHIBIT cell throughout the outline. This register also drives the companion deliverables produced in Steps 7 and 8.

**Source Register format:**

| # | Document / Evidence Item | Bates / Reference | Date |
|---|--------------------------|-------------------|------|
| (1) | [Document title as it actually appears, or evidence item # / filing description] | [Bates range or N/A] | [Date of document] |
| (2) | ... | ... | ... |

**No short-name column.** Do not maintain a separate shorthand alias for each document. Cite the document by its actual title — one name per document, everywhere. Two competing names for the same exhibit is how a source gets mis-pulled at counsel table.

**Rules for Source Register numbering:**
- Assign numbers in the order sources are first expected to appear in the outline
- Once a source number is assigned, it never changes — it persists across all chapters, the catalog, and the combined PDF
- Every source document cited anywhere in the outline MUST have an entry in the register
- Civil filings, transcripts, and non-Bates-stamped items receive numbers just like evidence items
- The Source Register is printed as a reference table on the second page of the cross-examination outline (after the cover page, before Chapter 1)

## Template Structure

Every cross-examination outline uses the D&W Cross Exam Template — one chapter per page block. Do not deviate from this structure.

**Formatting:** Times New Roman **14 pt** body and table text, 1" margins, landscape orientation for chapter table pages, each chapter starting on a new page, **page numbers bottom right of every page** (`Page N of M`). Full spec in `deliverable-formatting.md`. Output to `{{CASE_ROOT}}/01 - Trial Notebook/03 - Witnesses/Prosecution Witnesses/`.

### Every cell is a list — never a paragraph

**All three columns are bulleted or numbered. No column contains running prose.** A cross-examination outline is read standing up, mid-examination, while a witness waits. Prose forces the attorney to re-parse a block of text to find the next question. Lists do not.

| Column | Format | Why |
|---|---|---|
| **SOURCE/EXHIBIT** | **Bulleted.** One bullet per source, each beginning with its `(N)` register number | The attorney's hand goes to the right exhibit without reading a sentence |
| **QUESTIONS** | **Numbered.** One number per question, sequential within the chapter (1, 2, 3…) | Numbered questions can be called out loud, skipped, or returned to — "back to 4" is unambiguous |
| **NOTES/IMPEACHMENT** | **Bulleted.** One bullet per note, expected answer, or impeachment flag | Each note pairs visually with the question row it serves |

**Alignment rule:** the numbered question and its supporting source bullet and note bullet sit on the same row. If a question needs no note, leave that cell's bullet as `—` rather than merging rows or letting text wrap across question boundaries.

**One idea per bullet.** If a bullet contains "and," check whether it is two bullets. If a question contains "and," it is almost certainly two questions — split it. Short-question sequencing (see `witness-type-modules.md`) depends on one fact per question.

### Chapter layout

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CHAPTER TITLE: [Title tied to case theme]
Witness: [Name / Role]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

CHAPTER GOALS:
[per assets/chapter-goals-and-scoring.md — canonical]
• Goal 1 — what this chapter must establish
• Goal 2
[Law Enforcement only: Impact: _/3 | Fragility: _/3]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SOURCE/EXHIBIT        | QUESTIONS                  | NOTES/IMPEACHMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
• (1) [Document       | 1. [Question — one fact,   | • Expected: [answer]
  Title], p. 4        |    leading form]           | • If denied: go to (3)
                      |                            |
• (1) [Document       | 2. [Question]              | • Locks precondition
  Title], p. 4        |                            |
                      |                            |
• (3) [Document       | 3. [Question revealing     | • ⚠ IMPEACHMENT:
  Title], Bates 0033  |    the contradiction]      |   compare (1) vs. (3)
                      |                            | • IF ADMITS → bank it,
                      |                            |   move to next chapter
                      |                            | • IF DENIES → confront
                      |                            |   with (3), Bates 0033
                      |                            | • IF NO RECALL → refresh
                      |                            |   with (3), then confront
                      |                            | • La. C.E. art. 613 —
                      |                            |   foundation only before
                      |                            |   EXTRINSIC proof
                      |                            | • IF EXCLUDED — PRESERVE:
                      |                            |   ground + proffer
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
NOTES:
• [Strategic note]
• [Scope or evidentiary flag]
• [Attorney action item]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                                              Page N of M  (bottom right)
```

## Outline Assembly Order

**Canonical: `assets/outline-assembly.md`.** Summarized here for context; that file governs.

Every cross-examination outline .docx is assembled in this order:

1. **Cover page** — case caption, witness name, witness type, build date, attorney. On a **Fast Path** build (Step 0.52), the Fast Path notice goes here, directly under the caption. **Use the exact text in `assets/fast-path-notice.md`.**
2. **Source Register** — page 2, before Chapter 1
3. **Chapters** — one per page, in the sequence below
4. **Discovery Gap Report** (Step 6)
5. **Preservation Log** (Step 5.5) — the last appendix, blank, with Chapter and Question # rows pre-filled for every flagged question:

   | Chapter | Question # | Ruling | Ground stated | Proffer made | Form of proffer | Issue code |
   |---|---|---|---|---|---|---|

Items 1, 2, 4, and 5 are mandatory on every build, Fast Path included.

## Branch Logic — Every Impeachment Question Needs All Three Answers

An outline that assumes the witness cooperates fails on the witness who fights. **Every question at an impeachment point carries all three branches.** Write both branches before trial, when there is time to think, not at the podium.

Format in the NOTES/IMPEACHMENT column:

```
• IF ADMITS → [next move: bank it and move on, or press one level deeper]
• IF DENIES → confront with (N) [Document Title], [page/ref]
• IF NO RECALL → [refresh recollection with the document, then confront]
```

### The three answers and what each opens

| Answer | What it means | Your move |
|---|---|---|
| **Admits** | You have the concession | Bank it. Do **not** keep going — asking one more question after you get the answer is how concessions get taken back. Move to the next chapter |
| **Denies** | The document is now impeachment | Confront. The denial is what makes the exhibit powerful — the witness has committed against a document the jury is about to see |
| **"I don't recall"** | Evasion, or genuine memory failure | Refresh recollection with the document. If memory is still not revived, the prior statement may come in on its own terms. Either way, "I don't recall" from a witness who wrote the report is itself an answer the jury notices |

### Special branches worth pre-drafting

- **The conviction denial** — a denial or a claimed lack of recollection opens the **details** of the conviction under La. C.E. art. 609.1(C)(1). Pre-draft the detail questions and hold them in the NOTES column marked as reserve. Do not ask them unless the door opens.
- **The exculpatory explanation** — when a witness volunteers circumstances surrounding a conviction, art. 609.1(C)(2) opens the details. Same reserve treatment.
- **The expansion** — a witness who answers beyond the question has given you new material. Note: `IF EXPANDS → new material; do not interrupt, follow it`.
- **The fight** — for chapters scored Fragility 3, pre-draft the second and third questions of the confrontation, not just the first. A witness who resists the first confrontation will resist the follow-up, and improvising it in front of the jury is where crosses go wrong.

### Rule

**No impeachment question ships with only an expected answer.** "Expected: yes" is a prediction, not a plan. If the skill cannot write the denial branch, the question is not ready — surface it to the attorney rather than shipping it half-built.

## Source/Exhibit Citation Rule — `(N)` Prefix Format (MANDATORY)

**Every bullet in the SOURCE/EXHIBIT column MUST begin with the source register number in parentheses**, followed by the document's actual title, then the specific page, Bates number, or timestamp. This applies to ALL bullets without exception — standard question rows AND impeachment rows.

**Format:** `(N) Document Title, [page/Bates/timestamp]`

Use the document's title exactly as it appears in the Source Register. **No short names, no aliases, no abbreviations invented for the outline** — one name per document, everywhere. A second name for the same exhibit is how the wrong document gets pulled at counsel table.

**Examples (illustrative only — not case facts):**
- `(1) Recorded Interview of Complainant, 00:57` — source 1, timestamp 00:57
- `(2) SANE Examination Records, Bates 0042` — source 2, Bates page 0042
- `(3) Initial Incident Report, Bates 0033` — source 3, Bates page 0033
- `(5) Arrest Affidavit, Bates 0013` — source 5, Bates page 0013
- `(7) Protective Order Filing, p. 3` — source 7 (civil filing), page 3
- `Compare: (1) vs. (2) vs. (5)` — impeachment bullet comparing multiple sources

**Never omit the `(N)` prefix.** Never cite a document without its source register number. If page is unknown, flag it: `(N) [Document Title], [PAGE UNCONFIRMED — verify before trial]`.

## Chapter Sequencing

Default chapter order (adjust based on strategy):
1. Establish the favorable — lock in concessions the witness must give
2. Perception/memory conditions (civilian) OR scene/report conditions (LE)
3. Inconsistencies and omissions
4. SOP violations or methodology flaws (LE/Expert)
5. Prior inconsistent statements (impeachment)
6. Scene Control & Contamination (LE — if applicable)
7. Closing concession — end on your best point

## Case Theme Integration

The case theme must appear in at least one chapter title per outline and be referenced in the Chapter Goals of every substantive chapter. Example: if the theme is *"shortcuts and sloppy police work,"* a chapter might be titled **"The Shortcuts That Contaminated This Scene."**

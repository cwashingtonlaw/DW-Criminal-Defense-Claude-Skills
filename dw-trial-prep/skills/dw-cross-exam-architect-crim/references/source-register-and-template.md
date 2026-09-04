# Source Register & Cross-Examination Outline Template

## Source Register (Mandatory — Build Before Drafting Any Chapter)

Before writing any chapter, build a **Source Register** — a numbered master list of every source document that will be cited in the cross-examination. Each source receives a permanent number `(1)`, `(2)`, `(3)`, etc. that is used as a prefix in every SOURCE/EXHIBIT cell throughout the outline.

**The register is the outline's only index.** This skill produces no Source Catalog and no Combined Sources PDF, so nothing else in the package says what `(3)` is or where to find it. Every row must identify its document unambiguously by title and give a Reference/Bates entry precise enough to pull it from the case file at counsel table.

**Source Register format — three columns, exactly these headers:**

| Source Number | Evidence Item | Reference/Bates |
|---|---|---|
| (1) | [Document title as it actually appears, or evidence item # / filing description] | [Bates range, page span, timestamp range, or N/A] |
| (2) | ... | ... |

Header row shaded **blue** (`D6E4F0`) — the register is source data, and blue is the source colour throughout the outline. → `deliverable-formatting.md` §1.1

**Three columns only.** No short-name column and no date column.

- **Source Number** — the permanent `(N)`, written with the parentheses so it matches the citation form used in every chapter.
- **Evidence Item** — the document or item itself, by its actual title. One name per document, everywhere. Do not maintain a separate shorthand alias; two competing names for the same exhibit is how a source gets mis-pulled at counsel table.
- **Reference/Bates** — where it lives: Bates range, page span, recording timestamp range, evidence item number, or filing/record citation. `N/A` where the item carries none.

**Where the date goes now that the register has no date column.** Inside the **Evidence Item** entry, as part of the title: `Supplemental Incident Report (03/14/2024)`. There is nowhere else — with no catalog and no combined PDF, the register is the only record of the document anywhere in the package. Carry the date whenever it is material, and always where the case file holds more than one version of a document. Never leave a date-sensitive document identified by a bare title.

**Rules for Source Register numbering:**
- Assign numbers in the order sources are first expected to appear in the outline
- Once a source number is assigned, it never changes — it persists across all chapters, the catalog, and the combined PDF
- Every source document cited anywhere in the outline MUST have an entry in the register
- Civil filings, transcripts, and non-Bates-stamped items receive numbers just like evidence items
- The Source Register is printed as a reference table on the second page of the cross-examination outline (after the cover page, before Chapter 1)

---

## Template Structure

Every cross-examination outline uses the D&W Cross Exam Template — **one chapter per page**. Do not deviate from this structure.

**Formatting:** Times New Roman **12 pt** body and table text, 1" margins, landscape orientation for chapter pages, each chapter starting on a new page, **page numbers bottom right of every page** (`Page N of M`). Full spec in `deliverable-formatting.md`. Output to `{{CASE_ROOT}}/01 - Trial Notebook/03 - Witnesses/Prosecution Witnesses/`.

### The chapter page carries three things and nothing else

1. The **chapter heading block** — title, witness, CHAPTER GOALS, and (Law Enforcement only) the Impact / Fragility score.
2. The **two-column table** — `SOURCE/EXHIBIT | QUESTIONS`.
3. The **NOTES box** — a blank, bordered, full-width band roughly five lines deep, where the attorney writes the witness's actual answers during the examination.

Nothing else goes on the chapter page. **No expected answers, no branch logic, no impeachment bullets, no evidentiary flags, no preservation bullets, no strategy notes.** This page is a courtroom instrument, not a prep memo — it is read standing up while a witness waits, and every line on it is either an exhibit to pick up or a question to ask. Where that analysis goes is set out in **§ Where the prep analysis lives** below.

### The two-column table

| Column | Header colour | Format | Why |
|---|---|---|---|
| **SOURCE/EXHIBIT** | **Blue** `D6E4F0` | **Bulleted.** One bullet per source, each beginning with its `(N)` register number | The attorney's hand goes to the right exhibit without reading a sentence |
| **QUESTIONS** | **Red** `F4CCCC` | **Numbered.** One number per question, restarting at 1 in each chapter | Numbered questions can be called out loud, skipped, or returned to — "back to 4" is unambiguous |

There is no third column. Do not create one.

**Neither column contains running prose.** Prose forces the attorney to re-parse a block of text to find the next question. Lists do not.

**Alignment rule:** the numbered question and its supporting source bullet sit on the same row. Group consecutive questions that ride on the same exhibit into a single row rather than repeating the citation, and use `—` in the SOURCE/EXHIBIT cell where a row genuinely rides on an exhibit already in hand.

**One idea per bullet.** If a bullet contains "and," check whether it is two bullets. If a question contains "and," it is almost certainly two questions — split it. Short-question sequencing (see `witness-type-modules.md`) depends on one fact per question.

**Question numbering restarts at 1 in every chapter.** `Q3` in Chapter 4 and `Q3` in Chapter 5 are different questions; the Preservation Log identifies a question by Chapter **and** number, never by number alone.

### The NOTES box

The last two rows of the chapter table, both spanning the full width:

1. A label row reading **NOTES — WITNESS RESPONSES**, shaded **yellow** (`FFF2CC`).
2. A blank row, minimum height 1300 twips (roughly five lines at 12 pt), left empty.

The box is **blank on delivery and stays blank**. Never pre-fill it, never seed it with expected answers or reminders, never shade the writing area itself. It is where the attorney writes what the witness actually said — the one part of the page that belongs to the examination rather than to the preparation.

Set the blank row `cantSplit` so the box never breaks across a page.

### One chapter, one page

A chapter must fit on a single page **with its notes box**. If it does not, the chapter is too long — split it into two chapters rather than letting it run over. Two to four goals and roughly eight to fourteen questions is a chapter; more than that is two.

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

┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ SOURCE/EXHIBIT      [blue] ┃ QUESTIONS                       [red] ┃
┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
┃ • (1) [Document Title],    ┃ 1. [Question — one fact, leading form]┃
┃   Bates 0028               ┃ 2. [Question]                         ┃
┃                            ┃ 3. [Question]                         ┃
┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
┃ • (3) [Document Title],    ┃ 4. [Question revealing the            ┃
┃   Bates 0033               ┃    contradiction]                     ┃
┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
┃ NOTES — WITNESS RESPONSES                              [yellow]    ┃
┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
┃                                                                    ┃
┃                        (blank — ~5 lines)                          ┃
┃                                                                    ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
                                              Page N of M  (bottom right)
```

---

## Where the prep analysis lives

Removing the third column removed the printed home for branch logic, impeachment bullets, evidentiary flags, and preservation bullets. **The analysis is not removed — only its place on the chapter page.** It still runs, and it surfaces in three places:

| What | Where it goes now |
|---|---|
| Expected answers; `IF ADMITS` / `IF DENIES` / `IF NO RECALL` branches; the Fragility-3 second and third confrontation questions | **Reported to the attorney in the build conversation** at Step 5, chapter by chapter, and not printed into the outline |
| Impeachment findings — prior inconsistent statements, omissions, prior sworn contradictions | Step 5 auto-scan report to the attorney, cross-referenced against the Witness Analysis Card and DMAR §4 |
| `[608(B) REVIEW REQUIRED]`, `[SCOPE FLAG]`, art. 609.1(C) details held in reserve | Step 5 report to the attorney, plus a row in the Preservation Log for the affected question |
| **Ground to state on the record and substance to proffer** | **Pre-filled in the Preservation Log** (Step 5.5), the outline's final appendix — see `assets/preservation-log.md` |
| Chapter strategy, sequencing, scope posture, attorney action items | Step 5 report to the attorney; discovery items also go to the Discovery Gap Report (Step 6) |

**The Preservation Log is the one place where prep text still prints inside the outline**, and it does so because art. 841 and art. 103(A)(2) protection cannot be reconstructed at the podium. It is an appendix at the back, not part of any chapter page. Its `Ground to state` and `Proffer substance` columns arrive pre-filled; the rest is filled in during trial.

**Guardrail.** Because the chapter page no longer carries branch logic, an attorney working only from the chapter pages is working without it. Say so plainly when delivering the package: name which chapters carry flagged questions and point to the Preservation Log rows that cover them.

---

## Outline Assembly Order

**Canonical: `assets/outline-assembly.md`.** Summarized here for context; that file governs.

1. **Cover page** — case caption, witness name, witness type, build date, attorney. On a **Fast Path** build (Step 0.52), the Fast Path notice goes here, directly under the caption. **Use the exact text in `assets/fast-path-notice.md`.**
2. **Source Register** — page 2, before Chapter 1. Three columns: Source Number | Evidence Item | Reference/Bates
3. **Chapters** — one per page: heading block, two-column table, blank NOTES box
4. **Discovery Gap Report** (Step 6)
5. **Preservation Log** (Step 5.5) — the last appendix, with `Ground to state` and `Proffer substance` pre-filled for every flagged question

Items 1, 2, 4, and 5 are mandatory on every build, Fast Path included.

---

## Branch Logic — Every Impeachment Question Still Needs All Three Answers

An outline that assumes the witness cooperates fails on the witness who fights. **Every question at an impeachment point is still worked through all three branches** — the branches simply are not printed on the chapter page. Write all three during the build, when there is time to think, and report them to the attorney at Step 5.

```
Q[N]
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

### Special branches worth working through

- **The conviction denial** — a denial or a claimed lack of recollection opens the **details** of the conviction under La. C.E. art. 609.1(C)(1). Draft the detail questions, report them to the attorney as reserve, and **keep them out of the QUESTIONS column** so nothing is read aloud that the door has not opened.
- **The exculpatory explanation** — when a witness volunteers circumstances surrounding a conviction, art. 609.1(C)(2) opens the details. Same reserve treatment.
- **The expansion** — a witness who answers beyond the question has given you new material: do not interrupt, follow it.
- **The fight** — for chapters scored Fragility 3, work out the second and third questions of the confrontation, not just the first, and report them. A witness who resists the first confrontation will resist the follow-up.

### Rule

**No impeachment question is finished with only an expected answer.** "Expected: yes" is a prediction, not a plan. If the skill cannot articulate the denial branch, the question is not ready — surface it to the attorney rather than shipping it half-built.

---

## Source/Exhibit Citation Rule — `(N)` Prefix Format (MANDATORY)

**Every bullet in the SOURCE/EXHIBIT column MUST begin with the source register number in parentheses**, followed by the document's actual title, then the specific page, Bates number, or timestamp. This applies to every bullet without exception, and to every citation in the Preservation Log and in the Step 5 report.

**Format:** `(N) Document Title, [page/Bates/timestamp]`

Use the document's title exactly as it appears in the Source Register **Evidence Item** column. **No short names, no aliases, no abbreviations invented for the outline** — one name per document, everywhere. A second name for the same exhibit is how the wrong document gets pulled at counsel table.

**Examples (illustrative only — not case facts):**
- `(1) Recorded Interview of Complainant, 00:57`
- `(2) SANE Examination Records, Bates 0042`
- `(3) Initial Incident Report, Bates 0033`
- `(7) Protective Order Filing, p. 3` — civil filing
- `—` — row riding on the exhibit already in hand

**Never omit the `(N)` prefix.** If page is unknown, flag it: `(N) [Document Title], [PAGE UNCONFIRMED — verify before trial]`.

---

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

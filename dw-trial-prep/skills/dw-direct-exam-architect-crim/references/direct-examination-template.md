# D&W Direct-Examination Outline Template — Detailed Specification

Consumed by `dw-direct-exam-architect-crim/SKILL.md` STEP 4 and STEP 6.

**This template is the D&W Cross-Exam Template.** Same one deliverable, same three-column Source Register, same two-column chapter table, same blank notes box, same 12 pt Times New Roman, same colour bands. Direct and cross outlines sit in the same trial notebook tab and are read the same way at counsel table, so they look the same. The differences are in the *content*: questions are open-ended rather than leading, and what cross calls impeachment, direct calls cross-attack anticipation — which, like cross's branch logic, does not print on the chapter page.

---

## Document-Level Structure

One file, assembled in this order:

1. **Cover page** — case caption, witness name, witness type, build date, attorney
2. **Source Register** — page 2, before Chapter 1
3. **Chapters** — one per page: heading block, two-column table, blank notes box
4. **Discovery & Notice Gap Report**
5. **Preservation Log** — with `Ground to state` and `Proffer substance` pre-filled
6. **Rehearsal & Prep Schedule** — last, for witnesses requiring rehearsal

Items 1, 2, 4 and 5 are mandatory on every build.

**No Source Catalog and no Combined Sources PDF.** This skill produces one file. The Source Register on page 2 is the outline's only index, and exhibits are pulled from the case file by the Reference/Bates entry the register gives.

---

## Page 2 — Source Register

A numbered master list of every corroborating document and exhibit cited anywhere in the outline. Each source receives a permanent number `(1)`, `(2)`, `(3)`, etc., used as the citation prefix in every SOURCE/EXHIBIT cell.

**Three columns, exactly these headers.** Header row shaded **blue** (`D6E4F0`).

| Source Number | Evidence Item | Reference/Bates |
|---|---|---|
| (1) | Alibi Affidavit of Jane Doe | DEF 00045–00048 |
| (2) | Sonic Drive-In Receipt (03/15/2026) | DEF 00049 |
| (3) | GPS Log — Defendant's Vehicle (03/15/2026) | DEF 00050–00055 |
| (4) | Curriculum Vitae of Dr. Smith | DEF 00100–00115 |
| (5) | Expert Report of Dr. Smith | DEF 00116–00134 |
| (6) | Bank of America Business Records Certification | Self-authenticating, La. C.E. art. 902(11) |

**No short-name column and no date column.**

- **Source Number** — the permanent `(N)`, written with parentheses so it matches the citation form used in every chapter.
- **Evidence Item** — the document by its actual title. One name per document, everywhere. Where a date distinguishes one version from another — a supplemental affidavit, an amended expert report — carry it inside this entry, as in `(2)` above. With no catalog, there is nowhere else for it to live.
- **Reference/Bates** — Bates range, page span, timestamp range, evidence item number, or self-authentication citation. `N/A` where the item carries none.

**Rules**
- Numbers assigned in the order sources first appear in the outline; once assigned, a number never changes
- Every source cited anywhere in the outline MUST appear here
- **"Personal knowledge" is not a register entry.** It appears in the SOURCE/EXHIBIT cell as `Personal knowledge — foundation at Q[#]`
- The register is the outline's only index, so each row's Evidence Item title and Reference/Bates entry must be enough to pull the document from the case file cold

---

## Chapter Pages

Every chapter page carries three things and nothing else:

1. **Heading block** — chapter title, witness and role, case theme, CHAPTER GOALS
2. **Two-column table** — `SOURCE/EXHIBIT | QUESTIONS`
3. **NOTES box** — blank, bordered, full width, about five lines, where the attorney writes what the witness actually said

Nothing else goes on the chapter page. **No anticipated cross-attack vectors, no anticipated answers, no strategic notes, no rehearsal items, no evidentiary flags, no foundation reminders, no technique notes.** This page is a courtroom instrument, not a prep memo — every line on it is either an exhibit to pick up or a question to ask. Where that material goes is set out in **§ Where the prep analysis lives** below.

### The two-column table

| Column | Header colour | Format | Why |
|---|---|---|---|
| **SOURCE/EXHIBIT** | **Blue** `D6E4F0` | **Bulleted.** One bullet per source, each beginning with its `(N)` register number — or `Personal knowledge — foundation at Q[#]` | The attorney's hand goes to the right exhibit without reading a sentence |
| **QUESTIONS** | **Red** `F4CCCC` | **Numbered.** One number per question, restarting at 1 in each chapter | Numbered questions can be called out loud, skipped, or returned to — "back to 4" is unambiguous |

There is no third column. Do not create one.

**Neither column contains running prose.** Group consecutive questions riding on the same exhibit into one row rather than repeating the citation; use `—` in the SOURCE/EXHIBIT cell where a row rides on the exhibit already in hand or on foundation already laid.

**Question numbering restarts at 1 in every chapter.** The Preservation Log identifies a question by chapter **and** number, never by number alone.

### The one deliberate divergence from cross: permitted-leading tags

Direct questions are open-ended. Two flags exist, and they are treated differently:

- `⚠ LEADING — REPHRASE (La. C.E. art. 611(C))` — **a draft-time defect, never shipped.** Rewrite the question open-ended before delivery. If it genuinely cannot be rewritten, do not put it in the QUESTIONS column at all — surface it to the attorney in the STEP 4.5 report.
- `[LEADING OK — Preliminary]` · `[LEADING OK — Refreshing]` · `[LEADING OK — Hostile]` · `[LEADING OK — Adverse]` · `[LEADING OK — Communication difficulty]` — **stays inline in the QUESTIONS cell**, appended to the question it governs.

That second tag is the only annotation permitted on a direct chapter page, and it earns its place: on direct, whether you may lead is a live question at the moment you open your mouth, in a way it never is on cross. It tells the attorney how to ask the question in front of him. Everything else is prep and goes off the page.

### The NOTES box

The last two rows of the chapter table, both spanning the full width:

1. A label row reading **NOTES — WITNESS RESPONSES**, shaded **yellow** (`FFF2CC`).
2. A blank row, minimum height 1300 twips (about five lines at 12 pt), left empty.

**Blank on delivery and it stays blank.** Never pre-fill it, never seed it with anticipated answers or rehearsal reminders, never shade the writing area. Set the blank row `cantSplit` so the box never breaks across a page.

### One chapter, one page

A chapter must fit a single page **with its notes box**. If it does not, it is two chapters. Open-ended questions run longer than leading ones, so direct chapters hit this ceiling sooner than cross chapters — split rather than spill.

### Chapter layout

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CHAPTER 3: THE NIGHT OF MARCH 15
Witness: Jane Doe — Alibi Witness
Case theme: "He was where he said he was."
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

CHAPTER GOALS:
• Establish the witness was with the defendant from 8:00 p.m. to 11:30 p.m.
• Establish the locations and the corroboration anchors
• Establish the basis for her memory of the evening

┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ SOURCE/EXHIBIT      [blue] ┃ QUESTIONS                       [red] ┃
┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
┃ • Personal knowledge —     ┃ 1. Where were you on the evening of   ┃
┃   foundation at Q1         ┃    March 15?                          ┃
┃                            ┃ 2. Who were you with?                 ┃
┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
┃ • (2) Sonic Drive-In       ┃ 3. Describe how the two of you got    ┃
┃   Receipt (03/15/2026),    ┃    there.                             ┃
┃   DEF 00049                ┃ 4. What did you order?                ┃
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

Reducing the chapter to two columns removed the printed home for cross-attack vectors, anticipated answers, and strategic notes. **The analysis is not removed — only its place on the page.**

| What | Where it goes now |
|---|---|
| **Anticipated Cross-Attack Vectors** — the attack, the direct-exam preempt, the redirect plan | **Reported to the attorney in the build conversation at STEP 5**, chapter by chapter. Never printed on a chapter page |
| Anticipated answers; where a witness tends to rush, volunteer, or go quiet | STEP 5 report, and the Rehearsal & Prep Schedule appendix |
| Foundation requirements — "establish vehicle ownership before the GPS testimony" | Built into the **question order itself**. A foundation requirement is a question sequence, so it belongs in the QUESTIONS column as questions, not as a note about questions |
| Evidentiary flags — hearsay limits, authentication, `[SCOPE FLAG — opens door to X]` | STEP 5 report, plus a Preservation Log row for any question that could draw an objection |
| Technique notes — narrative start, Art. 612 refreshing procedure, tendering the expert | STEP 4.5 report |
| Rehearsal items | The Rehearsal & Prep Schedule appendix |
| **Ground to state on the record and substance to proffer** | **Pre-filled in the Preservation Log** — see `error-preservation-direct.md` |
| Discovery and notice gaps | The Discovery & Notice Gap Report appendix |

**Guardrail.** Because the chapter page no longer carries cross-attack vectors, an attorney working only from the chapter pages is working without them. Say so plainly on delivery: name the chapters whose propositions carry a live cross attack, and point to the STEP 5 report and the Preservation Log rows.

---

## Story-Arc Sequencing

Defense direct tells a story. Default chapter order:

1. **Background / context** — who the witness is and how they are connected; rapport with the jury, foundation for credibility
2. **Setup for the key event** — what was happening before; scene-setting
3. **Key event** — the heart of the testimony: alibi, expert opinion, character trait
4. **Corroboration** — the documents and data that back the witness up
5. **Close on the strongest point** — end on the most memorable proposition

### Story-arc principles

- Chronology is the jury's default. Depart from it only for a reason you can name.
- Every chapter should be able to answer "what does the jury now know that it did not know before this chapter?"
- Corroboration lands harder after the account than before it — the witness says it, then the document confirms it.
- End the witness on the proposition you want the jury carrying into cross.

---

## Cross-Attack Anticipation — Detailed Specification

For every proposition established on direct, identify the State's most likely cross attack and prepare the rebuttal. This work is mandatory. **It is delivered in the STEP 5 report, not on the chapter page.**

For each proposition:

1. **The attack** — a specific cross question or line the State is likely to use, phrased as the State would phrase it. Sourced from the STEP 5 auto-scan.
2. **The direct-exam preempt** — what this chapter or an earlier one does to defuse it: acknowledge the vulnerability on direct, anchor the proposition to multiple sources, establish the witness's basis in advance, or sanitize the issue by motion in limine.
3. **The redirect plan** — if the attack lands, what redirect does to clean it up: the document or witness that rehabilitates, the redirect question, and La. C.E. art. 611(D) for redirect scope.

**Report format (illustrative only — not case facts):**

```
Ch. 3 · Q2   ⚠ CROSS-ATTACK VECTOR
• Attack: "You're his girlfriend, so you'll say anything to help him."
• Direct preempt: Chapter 1 owns the relationship — she acknowledges she loves him
  and testifies consistently with (2) and (3).
• Redirect plan: If cross presses, redirect to how she would describe her interest in
  seeing justice done. La. C.E. art. 611(D).

Ch. 5 · Q7   ⚠ CROSS-ATTACK VECTOR
• Attack: "Doctor, you're being paid $5,000 for your testimony, correct?"
• Direct preempt: Qualifications chapter discloses the fee and the balance of prior
  testimony between defense and prosecution.
• Redirect plan: Re-emphasize methodology independence and prior prosecution testimony.
```

Every vector keyed to a chapter and question that exists. A vector reported for a question that is not in the outline is a defect; so is a proposition with a known attack and no vector.

---

## Discovery & Notice Gap Report (Appended)

After the final chapter:

```
DISCOVERY & NOTICE GAP REPORT — [Witness Name]

| Missing Item | Rule | Deadline | Consequence | Action Required |
|---|---|---|---|---|
| Art. 727 alibi notice | La. C.Cr.P. art. 727 | 30 days pre-trial | Exclusion of alibi evidence | File by [date] |
| State rebuttal disclosure | La. C.Cr.P. art. 727(B) | 20 days pre-trial | Surprise rebuttal blocked | Demand if not received |
| Expert disclosure package | La. C.Cr.P. arts. 716–729 `[VERIFY article — NOT 705]` | 30 days pre-trial | Exclusion or limited testimony | Serve and confirm |
| Subpoena issued and served | La. C.Cr.P. art. 731 et seq. | 7 days pre-trial | Witness no-show | Confirm service |
```

Required checks by witness type are in **§ Discovery & Notice Gap Report — Required Checks** below.

---

## Preservation Log (Appended)

Same table and same discipline as `dw-cross-exam-architect-crim`, and it matters more here: on direct the ruling excludes **your own** evidence, and art. 103(A)(2) preserves nothing without a proffer.

| Chapter | Question # | Ground to state | Proffer substance | Ruling | Proffer made | Form of proffer | Issue code |
|---|---|---|---|---|---|---|---|
| *pre-filled* | *pre-filled* | *pre-filled* | *pre-filled* | Sustained / Overruled | Yes / No | Q&A / statement / document | |

The first four columns arrive filled in; the rest is completed during trial. Full detail, including the art. 615 sequestration check, in `error-preservation-direct.md`.

---

## Rehearsal & Prep Schedule (Appended Last)

For witnesses requiring rehearsal — defendant, expert, alibi:

| # | Session | Focus | Duration | Date | Status |
|---|---|---|---|---|---|
| 1 | Outline walk-through | Read the entire outline with the witness | 2–3 hours | | [ ] |
| 2 | Practice direct | Full direct; identify the bumps | 90 min | | [ ] |
| 3 | Mock cross | Second chair plays the prosecutor | 2 hours | | [ ] |
| 4 | Video review | Identify tells; sparring | 90 min | | [ ] |
| 5 | Second mock cross | Adjustments | 90 min | | [ ] |
| 6 | Eve of trial | Light review | 30 min | | [ ] |

Rehearsal observations from the STEP 5 report belong here, not on the chapter pages.

---

## Document-Wide Formatting Specifications

| Element | Spec |
|---|---|
| **Body and table text** | **Times New Roman, 12 pt** |
| Chapter titles | Times New Roman, 12 pt, **bold**, ALL CAPS |
| Section headers (CHAPTER GOALS) | Times New Roman, 12 pt, **bold** |
| Table headers | Times New Roman, 12 pt, bold, ALL CAPS |
| Work product header | Times New Roman, 9 pt |
| Page numbers (bottom right) | Times New Roman, 10 pt |

**Colour bands** — identical to the cross-exam package, same meaning:

| Band | Colour | Hex | Where |
|---|---|---|---|
| Source | Blue | `D6E4F0` | Source Register header row; SOURCE/EXHIBIT header cell |
| Questions | Red | `F4CCCC` | QUESTIONS header cell |
| Notes | Yellow | `FFF2CC` | NOTES — WITNESS RESPONSES label row |

Light tints, black text, header/label rows only. Never shade a question, source, or the blank writing area. Apply with `ShadingType.CLEAR` and an explicit `fill`; `SOLID` renders black.

**Page setup**
- Margins 1" all sides
- **Landscape** for chapter pages; portrait for cover page and Source Register
- Column widths (landscape, 12960 DXA usable): SOURCE/EXHIBIT 4320, QUESTIONS 8640. Set `columnWidths` on the table **and** `width` on every cell, both `WidthType.DXA`
- Page numbers bottom right, `Page N of M`
- Work product marking in the **header** of every page; the footer carries the page number alone
- Each chapter starts on a new page and fits one page with its notes box; `cantSplit` on every row

**Flags**
- `[LEADING OK — basis]` — italic, inline in the QUESTIONS cell
- `[UNSOURCED — VERIFY BEFORE USING AT TRIAL]` — bold, in the SOURCE/EXHIBIT cell
- `⚠ LEADING — REPHRASE` — never appears in a delivered outline

---

## Filename Convention

- **Outline:** `Direct-Examination — [Witness Name].docx`
- **Saved to:** `{{CASE_ROOT}}/01 - Trial Notebook/03 - Witnesses/Defense Witnesses/`
- **Indexing copy:** `Direct-Exam Summary - [Witness Name] - [YYYY-MM-DD].docx` to `{{CASE_ROOT}}/01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/`

Version with a ` - v2` suffix rather than overwriting — a prior outline may already carry handwritten annotations.

---

## Source/Exhibit Citation Rule — `(N)` Prefix Format (MANDATORY)

**Every bullet in the SOURCE/EXHIBIT column begins with the source register number in parentheses**, followed by the document's Evidence Item title exactly as the register writes it, then the page, Bates number, or timestamp.

**Format:** `(N) Evidence Item Title, [page/Bates/timestamp]`

**Examples (illustrative only — not case facts):**
- `(2) Sonic Drive-In Receipt (03/15/2026), DEF 00049`
- `(3) GPS Log — Defendant's Vehicle (03/15/2026), DEF 00052`
- `(5) Expert Report of Dr. Smith, p. 11`
- `Personal knowledge — foundation at Q4` — not a register entry
- `—` — row riding on the exhibit already in hand

No short names, no aliases. If page is unknown, flag it: `(N) [Title], [PAGE UNCONFIRMED — verify before trial]`.

---

## Case Theme Integration

The case theme appears in at least one chapter title per outline and is referenced in the Chapter Goals of every substantive chapter. **The direct theme must match the cross theme** — the defense story is one story.

---

## Discovery & Notice Gap Report — Required Checks

For each gap: name the missing filing or disclosure, cite the rule, compute the deadline relative to trial, flag the consequence.

| Witness Type | Required Filing / Disclosure | Rule | Consequence |
|--------------|------------------------------|------|-------------|
| Alibi | Notice of alibi defense served on State | La. C.Cr.P. art. 727 | Exclusion of alibi evidence; mistrial risk |
| Alibi | State's response disclosing rebuttal witnesses | La. C.Cr.P. art. 727(B) | Surprise rebuttal blocked |
| Defense expert | Disclosure package (CV, qualifications, opinion summary, basis) | La. C.Cr.P. arts. 716–729 `[VERIFY article — NOT 705]` | Exclusion or limited testimony |
| Defense expert | Daubert challenge anticipated — methodology disclosure | La. C.E. arts. 702–703 | Voir dire of expert; possible exclusion |
| Character witness | Notice of intent to introduce art. 404(A) character evidence, where a pretrial order requires it | La. C.E. art. 404(A) / scheduling order | Limit on scope of character testimony |
| Custodian / foundation | Stipulation offered to the State on authentication | La. C.E. arts. 901–902 | If refused, the witness must testify; budget the time |
| Defendant | Waiver advisement confirmed on the record | 5th Amendment; *Brooks v. Tennessee* | Appellate issue if not documented |
| All | Subpoena issued and served | La. C.Cr.P. art. 731 et seq. | Witness no-show; defense rests with a gap |

Statutes cited from this skill's references — `[VERIFY current text]` before relying on any of them; Louisiana amends frequently.

---

*End of `direct-examination-template.md`. Return to SKILL.md STEP 4.*

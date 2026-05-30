# D&W Direct-Examination Outline Template — Detailed Specification

Consumed by `dw-direct-exam-architect-crim/SKILL.md` STEP 4. This is the detailed template specification for the firm Direct-Examination Outline document. The template mirrors the firm Cross-Exam Template but with one column substitution: where cross has "Impeachment Hooks," direct has "Anticipated Cross-Attack Vectors."

---

## Document-Level Structure

Every direct-exam outline (.docx) has the following pages in this order:

1. **Cover Page** — single page
2. **Source Register page** — second page; numbered list of every source document
3. **Chapter pages** — one chapter per page block (longer chapters span multiple pages)
4. **Discovery & Notice Gap Report** — appended after final chapter
5. **Rehearsal & Prep Schedule** — appended last

---

## Page 1 — Cover Page

The cover page identifies the outline at a glance.

**Required elements:**

```
══════════════════════════════════════════════════════════════
                  ATTORNEY WORK PRODUCT
              PRIVILEGED AND CONFIDENTIAL
            PREPARED IN ANTICIPATION OF LITIGATION
══════════════════════════════════════════════════════════════

              DANIELS & WASHINGTON, LLC
              Criminal Defense Law Firm

         DIRECT EXAMINATION OUTLINE

         Witness:       [Witness Full Name]
         Witness Type:  [Defendant / Alibi / Defense Expert /
                          Character / Foundation]
         Case:          STATE OF LOUISIANA v. [DEFENDANT]
         Docket No.:    [Docket Number]
         Parish:        [Parish Name]
         Court:         [Judicial District]
         Division:      [Division Letter]
         Judge:         [Judge Name]
         Trial Date:    [Trial Date]
         Attorney:      [Lead Counsel Name]
         Drafted:       [Date Drafted]
         Version:       [v1 / v2 / Final]

══════════════════════════════════════════════════════════════
```

**Formatting:**
- 11pt Times New Roman or document body font
- Work-product header banner top of page (per `dw-shared-protocols-crim/references/attorney-work-product-marking.md`)
- Vertical center on page
- Bold for "DIRECT EXAMINATION OUTLINE"
- All other text non-bold

---

## Page 2 — Source Register

A numbered master table of every source document referenced anywhere in the outline. Each source has a permanent `(N)` number used as the citation prefix throughout the outline.

**Format:**

```
SOURCE REGISTER
[Witness Name] Direct Examination
═══════════════════════════════════════════════════════════════════════════════

| #   | Short Name                | Evidence Item             | Bates / Ref    | Date       |
|-----|---------------------------|---------------------------|----------------|------------|
| (1) | Alibi Affidavit – Doe     | DEF-ALIBI-001             | DEF 00045–48   | 2026-04-01 |
| (2) | Sonic Receipt             | DEF-CORROB-002            | DEF 00049      | 2026-03-15 |
| (3) | GPS Log – Defendant Truck | DEF-CORROB-003            | DEF 00050–55   | 2026-03-15 |
| (4) | Expert CV – Dr. Smith     | DEF-EXP-001               | DEF 00100–115  | 2026-04-10 |
| (5) | Expert Report – Smith     | DEF-EXP-002               | DEF 00116–134  | 2026-04-10 |
| (6) | Bus. Records Cert. – BoA  | DEF-FND-001               | Self-auth 902(11) | 2026-04-15 |
| ... | ...                       | ...                       | ...            | ...        |
═══════════════════════════════════════════════════════════════════════════════
```

**Rules:**
- Numbers assigned in order sources first appear in the outline
- Once assigned, numbers never change
- Every source cited anywhere in the outline MUST appear here
- "Personal knowledge" foundation is NOT a source register entry — it is referenced inline in the SOURCE column
- The register is also used to drive the companion Source/Exhibit Document Catalog PDF and the Combined Source Documents PDF

---

## Chapter Pages — 8-Column Structure

Every chapter follows the same structure. The chapter is the unit of direct exam — one chapter per discrete proposition or story-arc beat.

### Chapter header block

```
═══════════════════════════════════════════════════════════════════════════════
CHAPTER 3: THE NIGHT OF MARCH 15                          Page 3 of 12
═══════════════════════════════════════════════════════════════════════════════
Witness: Jane Doe (Alibi Witness)
Case Theme: "He was where he said he was."

CHAPTER GOALS:
• Establish Jane Doe was with defendant from 8:00 pm to 11:30 pm on 03/15/2026
• Establish location: Sonic Drive-In, Sulphur, LA, and Jane's home
• Establish corroboration anchors: Sonic receipt, GPS log, doorbell cam
• Anticipate cross: relationship bias, late disclosure

═══════════════════════════════════════════════════════════════════════════════
```

### Chapter row block — 8 columns

The row table is the core of the chapter. Each row represents one question or one cluster of related questions (typically 1–3 closely related questions).

```
┌──────────────┬──────┬─────────┬─────────────┬──────────┬─────────────┬─────────────────────────┬─────────────┐
│ Chapter Title│ Page │ Witness │ Goals       │ Source   │ Questions   │ Anticipated Cross-Attack│ Notes       │
│              │      │         │             │          │             │ Vectors                 │             │
├──────────────┼──────┼─────────┼─────────────┼──────────┼─────────────┼─────────────────────────┼─────────────┤
│ March 15     │ 3    │ J. Doe  │ Establish   │ (1) Doe  │ Q: Tell us  │ Cross: "You're his      │ Open-ended  │
│              │      │         │ Doe with    │ Affidavit│ what you   │ girlfriend, so you'll   │ — narrative │
│              │      │         │ Def 8-11:30 │ p.2 ¶3   │ were doing │ say anything." Direct   │ start.      │
│              │      │         │             │          │ that       │ preempt: chap 1 owns    │             │
│              │      │         │             │          │ evening.   │ relationship.           │             │
├──────────────┼──────┼─────────┼─────────────┼──────────┼─────────────┼─────────────────────────┼─────────────┤
│ March 15     │ 3    │ J. Doe  │ Establish   │ (2) Sonic│ Q: How did │ Cross: "Receipt could   │ Show witness│
│              │      │         │ Sonic       │ Receipt  │ you and    │ have been planted/      │ Receipt to  │
│              │      │         │ corroborate │ DEF 49   │ defendant  │ kept after the fact."   │ refresh if  │
│              │      │         │             │          │ get there? │ Direct preempt: contem- │ needed (Art │
│              │      │         │             │          │            │ poraneous photo at      │ 612).       │
│              │      │         │             │          │            │ Sonic with timestamp.   │             │
├──────────────┼──────┼─────────┼─────────────┼──────────┼─────────────┼─────────────────────────┼─────────────┤
│ March 15     │ 3    │ J. Doe  │ Establish   │ (3) GPS  │ Q: Whose   │ Cross: "GPS could be    │ Foundation: │
│              │      │         │ GPS corrob  │ Log      │ vehicle    │ wrong; could be someone │ Q to estab- │
│              │      │         │             │ DEF 50-55│ did you    │ else driving." Direct   │ lish vehicle│
│              │      │         │             │          │ take?      │ preempt: chap 4 has     │ ownership   │
│              │      │         │             │          │            │ Custodial witness for   │ first.      │
│              │      │         │             │          │            │ GPS company.            │             │
└──────────────┴──────┴─────────┴─────────────┴──────────┴─────────────┴─────────────────────────┴─────────────┘
```

### Column-by-column specification

#### Column 1 — Chapter Title
- Tied to case theme
- Short (3–6 words)
- Repeated for every row within the chapter (for table portability if rows are extracted)

#### Column 2 — Page
- Outline page number where this row appears
- Useful for cross-referencing in the catalog

#### Column 3 — Witness
- Witness name
- Repeated for every row (for table portability)

#### Column 4 — Goals
- The proposition this row establishes
- 1 sentence
- Drives the questions in Column 6

#### Column 5 — Source
- The corroborating document or foundation reference
- Format: `(N) Short Name, page/Bates/timestamp` (from source register)
- OR: `Personal knowledge — foundation laid at Q[#]`
- OR: `[UNSOURCED — VERIFY BEFORE USING AT TRIAL]` if no source identified
- Multiple sources permitted: list each on its own line within the cell

#### Column 6 — Questions
- The actual question(s) to be asked
- OPEN-ENDED (non-leading) per La. C.E. Art. 611(C) — see SKILL.md STEP 4.5
- Approved opening words: Who, What, When, Where, Why, How, Describe, Tell, Explain
- Leading questions flagged: `⚠ LEADING — REPHRASE (La. C.E. Art. 611(C))`
- Permissible exceptions flagged: `[LEADING OK — Preliminary]`, `[LEADING OK — Refreshing]`, `[LEADING OK — Hostile]`, `[LEADING OK — Adverse]`
- One row may contain 1–3 closely related questions

#### Column 7 — Anticipated Cross-Attack Vectors
- This is the column that distinguishes direct from cross — replaces cross-exam's "Impeachment Hooks"
- For each goal/proposition, identify:
  - The most likely State cross attack on this point
  - The rebuttal preparation (direct-exam preempt, redirect plan, motion in limine status)
- Format:
  > Cross: "[Specific cross question or attack]."
  > Direct preempt: [How direct exam gets out in front]
  > Redirect plan: [How to clean up if cross succeeds]
- Sourced from STEP 5 auto-scan

#### Column 8 — Notes
- Strategic considerations
- Evidentiary flags (hearsay, foundation, scope)
- Rehearsal items (witness needs more drill on this)
- Attorney action items (motion in limine pending, subpoena status)
- Open-ended technique notes (narrative start, narrowing, clarifying)

### Chapter footer

```
═══════════════════════════════════════════════════════════════════════════════
NOTES:
[Strategic notes for this chapter as a whole — scope concerns, evidentiary
flags, rehearsal items, attorney action items not tied to a specific row]
═══════════════════════════════════════════════════════════════════════════════
```

---

## Story-Arc Sequencing

The chapters within an outline follow a default story arc. Adjust per witness and strategy.

| Order | Chapter Type | Purpose | Typical Length |
|-------|-------------|---------|----------------|
| 1 | Background / Context | Who the witness is, foundation for credibility, rapport with jury | 1–2 pages |
| 2 | Setup for Key Event | Scene-setting, what was happening before the key moment | 1–2 pages |
| 3 | Key Event | The heart of the testimony (the alibi observation, the expert opinion, the character trait) | 2–4 pages |
| 4 | Corroboration | The documents and data that back the witness up | 1–3 pages |
| 5 | (Optional) Get-Out-In-Front | Address any vulnerability the State will exploit | 1 page |
| 6 | Close on Strongest Point | End on the most jury-memorable proposition | 1 page |

### Story-arc principles

- **Open strong.** Chapter 1 builds witness credibility (who they are, why they matter). This is the rapport phase. Open-ended narrative questions invite the witness to introduce themselves to the jury.
- **Pace down.** Chapter 2 slows the pace, sets scene, and primes the jury for the key moment. Granular detail builds vividness.
- **Detonate in the middle.** Chapter 3 delivers the key proposition. Tight question-cluster cadence. Specific times, specific places, specific actions.
- **Corroborate immediately after.** Chapter 4 anchors the key proposition to documents and data. Each anchor reinforces credibility.
- **Get out in front.** If there's a vulnerability the State will attack, address it here — after the jury has accepted the witness, before the State attacks.
- **Close on the strongest point.** Whatever the jury will REMEMBER. Often a single propositional sentence the attorney wants in closing.

### Sequencing variants

- **Defendant outline:** Background chapter is short or skipped (jury already knows defendant from State case). Story-arc begins with setup. Get-out-in-front for any 609 prior is often Chapter 2 or 3 (early, before key event).
- **Defense expert outline:** Chapter 1 = qualifications colloquy (tender). Chapter 2 = materials reviewed. Chapter 3 = methodology. Chapter 4 = opinion. Chapter 5 = anticipated state cross preempt.
- **Alibi witness outline:** Chapter 1 = relationship to defendant (own it). Chapter 2 = background of the day. Chapter 3 = key alibi event. Chapter 4 = corroboration anchors. Chapter 5 = disclosure timing (when first told the story, to whom).
- **Character witness outline:** Chapter 1 = foundation for personal/community knowledge. Chapter 2 = trait testimony (reputation or opinion form only). Very short outline — 1–3 pages total.
- **Foundation witness outline:** Single chapter, 4-prong business records or 902 self-auth predicate, immediate offer. Target 4 minutes total.

---

## Cross-Attack Anticipation Column — Detailed Specification

The Anticipated Cross-Attack Vectors column is the column that makes a direct-exam outline complete. For every goal/proposition established on direct, identify the State's most likely cross attack and prepare the rebuttal.

### What goes in the column

For each row:

1. **The attack:** A specific cross-examination question or line the State is likely to use against this proposition. Phrased as the State would phrase it. Sourced from STEP 5 auto-scan.

2. **The direct-exam preempt:** What does THIS chapter (or an earlier chapter) do to defuse the attack? Common preempts:
   - Acknowledge the vulnerability on direct ("get out in front")
   - Anchor the proposition to multiple sources
   - Establish witness's basis for the proposition in advance
   - Sanitize the issue via motion in limine

3. **The redirect plan:** If the State's cross succeeds in landing the attack, what does redirect do to clean it up?
   - Identify document or witness that rehabilitates
   - Plan the redirect question
   - Cite La. C.E. Art. 611(D) for redirect scope (matters covered on cross)

### Example entries

```
Cross: "You're his girlfriend, so you'll say anything to help him."
Direct preempt: Chapter 1 owns the relationship; witness acknowledged
  she loves him AND testified consistently with documents.
Redirect plan: If cross presses, redirect to Q: "How would you describe
  your interest in seeing justice done in this case?"
```

```
Cross: "Doctor, you're being paid $5,000 for your testimony, correct?"
Direct preempt: Qualifications chapter disclosed fee ($350/hour, total
  estimated $5,000) and balance of prior testimony (60% defense, 40% prosec).
Redirect plan: La. C.E. Art. 611(D) redirect — re-emphasize methodology
  independence and prior prosecution testimony.
```

```
Cross: "You have a felony conviction from 2019 for theft, don't you?"
Direct preempt: Motion in limine denied; defendant acknowledged conviction
  on direct in Chapter 2, sanitized to "I made a mistake when I was 22."
Redirect plan: Redirect to underline the change since 2019 (employment,
  family, no further incidents).
```

---

## Notes Column — Detailed Specification

The Notes column captures everything that does not fit elsewhere. Common content:

**Strategic considerations:**
- "Pace down — witness tends to rush this section"
- "Pause after this Q for the jury to absorb"
- "If witness emotional, let them recover before next Q"

**Evidentiary flags:**
- "Hearsay — only admit for state of mind, not truth"
- "Authentication needed before offering Exhibit 7"
- "Court may sustain objection; have backup foundation"

**Foundation requirements:**
- "Establish vehicle ownership before GPS testimony"
- "Establish witness's familiarity with defendant's voice before identifying call"

**Rehearsal items:**
- "Drill witness on this — tendency to volunteer info"
- "Witness needs to maintain eye contact"
- "Slow down — witness gets quiet here in rehearsal"

**Attorney action items:**
- "Subpoena business records custodian if no stipulation"
- "Motion in limine on prior conviction — ruling pending"
- "Confirm Art. 727 supplement filed"

**Technique notes:**
- "Open-ended start to invite narrative"
- "Refreshing recollection — Art. 612 procedure"
- "Tendering as expert — formal statement on record"

---

## Discovery & Notice Gap Report (Appended)

After the final chapter, append a Discovery & Notice Gap Report in this format:

```
═══════════════════════════════════════════════════════════════════════════════
DISCOVERY & NOTICE GAP REPORT
[Witness Name] Direct Examination
═══════════════════════════════════════════════════════════════════════════════

| Missing Item               | Rule              | Deadline       | Consequence     | Action Required        |
|----------------------------|-------------------|----------------|-----------------|------------------------|
| Art. 727 alibi notice      | La. C.Cr.P. 727   | 30 days pre-tr | Exclusion       | File by [date]         |
| State rebuttal disclosure  | La. C.Cr.P. 727(B)| 20 days pre-tr | Surprise lockout| Demand if not received |
| Daubert hearing transcript | Art. 702          | n/a            | Preserve record | Order from court rep   |
| Expert CV current          | La. C.Cr.P. 705   | 30 days pre-tr | Limited test.   | Update and reserve     |
| Subpoena issued/served     | La. C.Cr.P. 731   | 7 days pre-tr  | No-show         | Confirm service        |
═══════════════════════════════════════════════════════════════════════════════
```

---

## Rehearsal & Prep Schedule (Appended Last)

For witnesses requiring rehearsal (defendant, expert, alibi), append a schedule:

```
═══════════════════════════════════════════════════════════════════════════════
REHEARSAL & PREP SCHEDULE
[Witness Name]
═══════════════════════════════════════════════════════════════════════════════

| #  | Session              | Focus                        | Duration   | Date     | Status |
|----|----------------------|------------------------------|------------|----------|--------|
| 1  | Outline walk-through | Read entire outline w/witness| 2-3 hours  | [date]   | [ ]    |
| 2  | Practice direct      | Full direct, identify bumps  | 90 min     | [date]   | [ ]    |
| 3  | Mock cross           | 2d chair plays prosecutor    | 2 hours    | [date]   | [ ]    |
| 4  | Video review         | Identify tells, sparring     | 90 min     | [date]   | [ ]    |
| 5  | Second mock cross    | Adjustments                  | 90 min     | [date]   | [ ]    |
| 6  | Eve of trial         | Light review                 | 30 min     | [date]   | [ ]    |
═══════════════════════════════════════════════════════════════════════════════
```

---

## Document-Wide Formatting Specifications

- **Font:** Times New Roman 11pt body; 14pt chapter headers; 9pt header/footer
- **Margins:** 1" all sides
- **Header:** ATTORNEY WORK PRODUCT — PRIVILEGED AND CONFIDENTIAL (per shared protocol)
- **Footer:** Case caption + page number (e.g., "State v. Smith — Docket No. 2026-1234 — Direct of J. Doe — Page X of Y")
- **Tables:** Light gray (RGB 230/230/230) header row; black borders; text wraps within cells
- **Chapter dividers:** Double-line `═══` between chapters
- **Citation format:** `(N) Short Name, page/Bates/timestamp` — never omit the `(N)` prefix
- **Leading-question flags:** `⚠ LEADING — REPHRASE` in red or bold
- **Permitted-leading flags:** `[LEADING OK — basis]` in italic
- **Unsourced flags:** `[UNSOURCED — VERIFY BEFORE USING AT TRIAL]` in red or bold
- **Save format:** `.docx`

---

## Filename Convention

- **Primary outline:** `Direct-Examination - [Witness Name].docx`
- **Saved to:** `{{CASE_ROOT}}/01 - Trial Notebook/03 - Witnesses/Defense Witnesses/`
- **Indexing copy:** `Direct-Exam Summary - [Witness Name] - [YYYY-MM-DD].docx`
- **Saved to:** `{{CASE_ROOT}}/01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/`

---

*End of `direct-examination-template.md`. Return to SKILL.md STEP 4.*

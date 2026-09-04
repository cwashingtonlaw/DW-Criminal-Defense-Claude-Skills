# Daniels & Washington — Skills Operations Guide
**Version 1.4 | September 2026 | Internal Use Only**

This is the canonical operations manual for the Daniels & Washington Claude skill suite. It supersedes v1.3 (May 2026), which superseded v1.2 (`DW_Skills_Operations_Guide_v1.2.docx`). Use this guide to understand:

- The two intersecting workflows (3-phase D&W + 9-step Barone)
- What every skill does and when to invoke it
- How skills hand off to each other
- The shared protocols every skill enforces
- Practical recipes for the case scenarios you see most often

For development conventions and repository structure, see `CLAUDE.md` at the repo root. For the searchable trigger-phrase routing table, ask Claude for the skill index ("what skills do we have").

---

## What changed in v1.4 (September 2026)

**Current inventory:** 76 skills across 9 criminal-practice plugins — `dw-core` (7), `dw-trial-prep` (17), `dw-evidence-audit` (16), `dw-disposition` (9), `dw-ops` (8), `dw-intake-discovery` (5), `dw-offense-specialists` (5), `dw-transcription` (5), `dw-pleadings` (4).

**Witness-exam outlines were rebuilt.** Cross and direct now use one identical template and each produce **one file**:

| | Before | Now |
|---|---|---|
| Deliverables per witness | 3 (outline .docx + Source Catalog .pdf + Combined Sources .pdf) | **1** (`… — [Witness Name].docx`) |
| Source Register | 4–5 columns incl. short name and date | **3**: Source Number \| Evidence Item \| Reference/Bates |
| Chapter table | Cross: 3 columns · Direct: 8 columns | **2**: SOURCE/EXHIBIT \| QUESTIONS |
| Notes | printed column of prep text | **blank write-in box**, ~5 lines, at the foot of every chapter |
| Type | 14 pt Times New Roman | **12 pt** Times New Roman |
| Colour | none | blue `D6E4F0` = source · red `F4CCCC` = questions · yellow `FFF2CC` = notes |

The chapter page now carries only the exhibit to pick up and the question to ask. Branch logic, impeachment bullets and cross-attack vectors are **reported to the attorney during the build** rather than printed; ground-to-state and proffer-substance are **pre-filled columns in the Preservation Log** so art. 841 / art. 103(A)(2) protection survives off the page. Contracts 3 and 3A in `dw-data-contracts-crim` carry the full schema.

**Because the catalogs are gone, the Source Register is the only index.** Every register row's Evidence Item title and Reference/Bates entry must be enough to pull that document from the case file cold, and a document's date now lives inside the Evidence Item entry.

**`dw-exhibit-manager-crim` is retired** (at `dw-trial-prep` v1.9 / `dw-criminal-defense-crim` v6.2). Pre-trial exhibit metadata — sponsoring witness, authentication route, anticipated objections — lives on the **Evidence Table** in `Case Tables.xlsx`; live offer/admission status is `dw-trial-day-assistant-crim` **Module D**, the exhibit tracker of record. The appellate objection-preservation chain is unbroken.

---

## Table of Contents

1. [Philosophy & Inviolable Rules](#1-philosophy--inviolable-rules)
2. [The Two Workflows at a Glance](#2-the-two-workflows-at-a-glance)
3. [The Barone Discovery Workflow (9 Steps)](#3-the-barone-discovery-workflow-9-steps)
4. [The D&W 3-Phase Workflow](#4-the-dw-3-phase-workflow)
5. [Skill Catalog by Function](#5-skill-catalog-by-function)
6. [Cross-Skill Integration Map](#6-cross-skill-integration-map)
7. [Shared Protocols (Read These First)](#7-shared-protocols-read-these-first)
8. [Practical Recipes](#8-practical-recipes)
9. [Reference Appendices](#9-reference-appendices)

---

## 1. Philosophy & Inviolable Rules

The skill suite operates under five rules that override anything else in this manual. If a skill ever appears to violate one of these, stop and flag it.

### Rule 1 — Cowork drafts; attorney approves
Every output is a draft for attorney review. Cowork never represents work as final or filed. The attorney verifies facts, confirms legal arguments, signs, and files.

### Rule 2 — No fabricated citations
Every Louisiana statute, code article, and case citation must be verifiable. If you cannot verify a citation, flag it `[VERIFY CITATION]` and the attorney will confirm before reliance. Well-established anchor authorities (*Miranda*, *Brady*, *Giglio*, *Strickland*, *Daubert*, *Foret*, *Crawford*, *Batson*, *Padilla*) may be cited unflagged.

### Rule 3 — Source Citation Mandate
Every factual assertion in any deliverable must trace to a specific source document — discovery file, transcript page/line, BWC timestamp, lab report. Unsourced claims must be marked `[UNSOURCED — VERIFY]`.

### Rule 4 — Verification Protocol ([VERIFIED] / [UNVERIFIED])
Introduced with the Barone audit. Every catalog entry, fact extraction, and evidence reference must be marked `[VERIFIED]` (source directly reviewed in this session) or `[UNVERIFIED]` (referenced in other documents but not directly reviewed). See `dw-shared-protocols-crim/references/verification-protocol.md`.

### Rule 5 — Attorney work-product marking
Every analytical or motion deliverable carries the firm's standard work-product header. The marking is enforced at Step 0.5 of every skill via `dw-shared-protocols-crim/references/attorney-work-product-marking.md`.

---

## 2. The Two Workflows at a Glance

D&W runs two interlocking workflows. The **3-phase workflow** is the macro structure of every case from intake to verdict. The **Barone Discovery Workflow** is a 9-step analytical pipeline that runs inside Phase 2 and bridges into Phase 3.

```
┌─────────────────────────────────────────────────────────────────┐
│                  D&W 3-PHASE WORKFLOW                           │
├─────────────────────────────────────────────────────────────────┤
│  PHASE 1: Intake & Setup                                        │
│    • Folder structure, Bate-stamping, Case Profile, Case Tables │
│                                                                 │
│  PHASE 2: Case Processing & Analysis                            │
│    ┌───────────────────────────────────────────────────────┐    │
│    │      BARONE DISCOVERY WORKFLOW (runs here)            │    │
│    │  Step 1: Report 0  — Neutral Inventory                │    │
│    │  Step 2: Report 1  — Timeline (with Certainty)        │    │
│    │  Step 3: Report 2  — Prosecution Case Summary         │    │
│    │  Step 4: Report 2a — Theory Deconstruction            │    │
│    │  Step 5: Report 3  — Red Flags                        │    │
│    │  Step 6: Report 4  — Competing Defense Theories       │    │
│    │  Step 7: Report 4a — Theory Selection Memo (attorney) │    │
│    │  Step 8: Theory-to-Workplan (7 streams)               │    │
│    │  Step 9: Adversarial Stress Test                      │    │
│    └───────────────────────────────────────────────────────┘    │
│                                                                 │
│  PHASE 3: Trial Notebook & Attorney Preparation                 │
│    • Timeline, witness tables, defense shield, cross/direct,    │
│      opening/closing, jury instructions, voir dire, trial day   │
└─────────────────────────────────────────────────────────────────┘
```

The Barone workflow does not replace Phase 2's existing reports — it sequences and adds to them, adding theory-neutral inventory (Report 0), theory deconstruction (Report 2a), competing-theory analysis (revised Report 4), theory selection (new Report 4a), and adversarial testing.

---

## 3. The Barone Discovery Workflow (9 Steps)

The Barone workflow is the firm's structured approach to processing criminal discovery in a way that minimizes confirmation bias and maximizes preparation. Every step is theory-neutral until Report 4a, where the attorney makes the strategic decision to commit.

### Step 1: Report 0 — Neutral Inventory
**Skill**: `dw-neutral-inventory-crim`
**Trigger**: "neutral inventory," "catalog the evidence," "what do we have," "Report 0"

Builds a theory-neutral catalog of everything in discovery. Six modules:

- **A — Document Catalog**: every paper document with Doc #, Bate range, type, date, source, one-line factual summary
- **B — Media Catalog**: every audio/video/digital file with duration, type, participants, content summary
- **C — Physical Evidence Catalog**: every physical evidence item referenced in discovery
- **D — Witness Roster**: every person mentioned across all discovery with role and source documents
- **E — Completeness Flags**: items referenced but not produced (BWC mentioned but not delivered, lab report cited but not provided, etc.)
- **F — Verification Status**: marks every entry [VERIFIED] / [UNVERIFIED]

**Why before strategy**: Catalogue first, theorize later. This prevents the defense team from overlooking evidence that doesn't fit an emerging theory.

**Output**: `01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/Report 0 — Neutral Discovery Inventory.docx`

---

### Step 2: Report 1 — Timeline with Certainty Column
**Skill**: `dw-timeline-builder-crim`
**Trigger**: "build the timeline," "master timeline," "chronology"

Aggregates timestamps from every source — incident reports, BWC, 911 CAD, cell records, witness statements, jail calls — into a single chronological record with conflict flagging.

**Barone enhancement — Certainty column**:

| Rating | Meaning |
|---|---|
| CONFIRMED | Multiple independent sources corroborate, or device-generated record with no contradiction |
| PROBABLE | Single reliable source (Tier 1-2) with no contradiction, or multiple Tier 3-4 sources in agreement |
| DISPUTED | Sources disagree on whether or when an event occurred |
| UNCONFIRMED | Single Tier 3-4 source only, or based on inference |
| ALLEGED | Assertion by a party with interest in the outcome (victim, informant, co-defendant) |

Certainty is distinct from Confidence (which tracks timestamp precision) — an event can have a precise timestamp but uncertain occurrence.

**Output**: Timeline sheet in `Case Tables.xlsx` + optional visual timeline (interactive HTML or static Mermaid)

---

### Step 3: Report 2 — Prosecution's Case Summary
**Skill**: `dw-criminal-defense-crim` (Phase 2 Step 2)

Synthesizes the prosecution's likely theory, the charged elements, the State's key evidence, and the State's timeline. Feeds Report 2a.

**Output**: `01 - Trial Notebook/09 - Case Analysis/Report 2 — Prosecution Case Summary.docx`

---

### Step 4: Report 2a — Theory Deconstruction
**Skill**: `dw-theory-deconstructor-crim`
**Trigger**: "deconstruct the theory," "facts vs inferences," "Report 2a," "assumption audit"

Decomposes the prosecution's theory into three categories:

- **Facts** — verifiable, documented, [VERIFIED]
- **Inferences** — conclusions drawn from facts (strong / moderate / weak link)
- **Assumptions** — unsupported by evidence (high / medium / low challenge viability)

Six modules ending with the **Gap Analysis Matrix** (element-by-element vulnerability map) and **Alternative Inference Table** (for each prosecution inference, the strongest defense counter-inference from the same facts).

**Why this matters**: The Alternative Inference Table feeds directly into Report 4 (Competing Theories). Theory deconstruction surfaces the inferential leaps a jury would need to make for the prosecution to prevail.

**Output**: `01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/Report 2a — Theory Deconstruction.docx`

---

### Step 5: Report 3 — Immediate Red Flags
**Skill**: `dw-criminal-defense-crim` (Phase 2 Step 2)

Identifies the most significant weaknesses in the prosecution's case — constitutional issues, evidentiary gaps, procedural defects. Routes constitutional flags to `dw-suppression-motion-crim` and expert issues to `dw-expert-witness-evaluator-crim`.

**Output**: `01 - Trial Notebook/09 - Case Analysis/Report 3 — Red Flags.docx`

---

### Step 6: Report 4 — Competing Defense Theories
**Skill**: `dw-criminal-defense-crim` (Phase 2 Step 2 — revised in v5.9)

**Critical change from v5.8**: Report 4 used to produce a single "Core Defense Narrative." It now produces **multiple competing theories**, each with:

1. Theory name (e.g., "Misidentification," "Self-Defense," "Coerced Confession," "Insufficient Evidence")
2. Theory summary
3. Supporting evidence (with Bate stamps)
4. Weaknesses (from Report 2a Assumption Audit)
5. Prosecution counter-arguments
6. Viability assessment (STRONG / MODERATE / WEAK)
7. Compatible Report 5 legal defenses

Followed by a **Comparative Matrix**: Theory | Key Strength | Key Weakness | Viability | Compatible Defenses.

**Why competing theories**: Premature commitment to a single defense narrative creates confirmation bias. Presenting alternatives lets the attorney make an informed strategic choice with eyes open to trade-offs.

**Output**: `01 - Trial Notebook/09 - Case Analysis/Report 4 — Competing Defense Theories.docx`

---

### Step 7: Report 4a — Theory Selection Memo (Attorney-Driven)
**Skill**: `dw-criminal-defense-crim` (Phase 2 Step 2A — new in v5.9)

The attorney reviews Report 4 and selects the primary defense theory. Cowork drafts a memo documenting:

1. Selected theory
2. Selection rationale (attorney provides; Cowork documents)
3. Top 5-10 pieces of evidence supporting the theory
4. Top 3-5 vulnerabilities to address
5. Critical assumptions that must hold
6. **Pivot triggers** — events that would require reconsidering (e.g., "if BWC contradicts alibi witness")
7. Abandoned theories and why (preserves reasoning for the record)

**Attorney sign-off required**. Downstream Barone skills (stress test, workplan) cannot proceed without Report 4a confirmation.

**Output**: `01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/Report 4a — Theory Selection Memo.docx`

---

### Step 8: Theory-to-Workplan (7 Streams)
**Skill**: `dw-theory-to-workplan-crim`
**Trigger**: "build a workplan," "theory to workplan," "task list for trial"

Explodes the attorney-selected theory into a 7-stream action plan:

| Stream | Focus | Routes To |
|---|---|---|
| 1 — Investigation | Witnesses to interview, locations to visit, records to subpoena | `dw-defense-investigator-tasking-crim` |
| 2 — Discovery | Additional demands, motions to compel, Brady/Giglio | `dw-discovery-compliance-monitor-crim`, `dw-brady-giglio-auditor-crim` |
| 3 — Experts | Experts needed, Daubert/Foret challenges | `dw-expert-witness-evaluator-crim` |
| 4 — Motions | Suppress, exclude 404(b), sever, etc. | `dw-suppression-motion-crim`, `dw-404b-opposition-crim`, `dw-pretrial-motion-library-crim` |
| 5 — Witnesses | Cross prep, direct prep | `dw-cross-exam-architect-crim`, `dw-direct-exam-architect-crim` |
| 6 — Exhibits | Exhibit list, demonstratives, authentication | **Evidence Table** in `Case Tables.xlsx` (pre-trial metadata), `dw-trial-day-assistant-crim` Module D (live offer/admission status), `dw-trial-notebook-builder-crim` |
| 7 — Narrative | Opening, closing, jury instructions, voir dire | `dw-trial-narrative-builder-crim`, `dw-jury-instructions-builder-crim`, `dw-voir-dire-assistant-crim` |

Each task carries: priority, responsible party, D&W skill, deadline, dependencies, status. Living document — updates as the case evolves.

**Output**: `01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/Theory-to-Workplan.docx` + Apple Notes summary checklist

---

### Step 9: Adversarial Stress Test
**Skill**: `dw-adversarial-stress-test-crim`
**Trigger**: "stress test," "red team," "prosecutor's perspective," "what will the state argue"

Role-plays a skilled Louisiana prosecutor attacking the selected defense theory. Seven modules:

- **A — Theory Vulnerability Scan**: top 10 weaknesses with prosecution exploitation paths
- **B — Cross-Examination Simulation**: hardest 5 questions per defense witness
- **C — Prosecution Closing Preview**: drafted attack on the defense theory
- **D — Rebuttal Evidence Identification**: evidence the State could introduce in rebuttal and defense challenges
- **E — Defense Counter-Response Matrix**: for each attack, the defense response with supporting authority
- **F — Jury Perception Risk Assessment**: HIGH / MODERATE / LOW from the jury's emotional lens
- **G — Priority Preparation Checklist**: ranked list routed to downstream D&W skills

**When to re-run**: when new discovery arrives, when theory shifts, or two weeks before trial as final pressure test.

**Output**: `01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/Adversarial Stress Test.docx` + one-page "Top 5 Vulnerabilities" executive summary

---

## 4. The D&W 3-Phase Workflow

The 3-phase workflow is the master orchestrator (`dw-criminal-defense-crim` v5.9). The Barone steps above run inside Phase 2.

### Phase 1: Case Intake & Matter Setup

**Master orchestrator**: `dw-criminal-defense-crim` Phase 1

| Step | What happens | Skill(s) |
|---|---|---|
| 1 | Folder structure setup, `CASE_ROOT` resolution, copy `Case Tables.xlsx` master | `dw-criminal-defense-crim` |
| 2 | Discovery prep: download log, Bate-stamp, OCR, separate, transcribe, media placeholders | `dw-transcript-router-crim`, `dw-evidence-placeholder-crim` |
| 3 | Generate `000 - Case Profile.docx` (Part 1 + Part 2A/2B/2C for LWOP/non-LWOP) | `dw-criminal-defense-crim` (absorbed former `dw-lwop-populator`) |
| 4 | Build Case Tables: Evidence Table, Witness List - Priority, Witness List - Alpha | `dw-criminal-defense-crim` |

**Companion**: `dw-client-intake-interview-crim` — the live client meeting (charge type, conflict check, immediate-action triage). Feeds Phase 1.

**Quality Gate**: All checks confirmed before Phase 2. Case Brain registers Phase 1 complete.

### Phase 2: Case Processing & Analysis

**Master orchestrator**: `dw-criminal-defense-crim` Phase 2 (now contains the Barone workflow)

| Step | What happens | Skill(s) |
|---|---|---|
| 1 | Rapid Triage & Specialist Routing (memo, chain of custody, evidence specialists, charge-type specialists) | `dw-criminal-defense-crim` + auditors + specialists |
| **1E** | **Barone pre-analysis: Report 0 (Neutral Inventory) + Report 2a (Theory Deconstruction)** | `dw-neutral-inventory-crim`, `dw-theory-deconstructor-crim` |
| 2 | Generate the 8 Case Analysis Reports (with revised Report 4 Competing Theories) | `dw-criminal-defense-crim` |
| **2A** | **Barone post-analysis: Report 4a (Theory Selection) → stress test + workplan** | `dw-adversarial-stress-test-crim`, `dw-theory-to-workplan-crim` |
| 3 | Auto-Action: Report 7 → Missing Discovery Demand Letter | `dw-criminal-defense-crim` |
| 4 | Auto-Action: Report 8 → Impeachment Worksheets | `dw-criminal-defense-crim` |
| 5 | Route case analysis to attorney with index | `dw-criminal-defense-crim` |
| 6 | Auto-Push Attorney Review Checklist to Apple Notes | `dw-criminal-defense-crim` |

**Quality Gate**: All 8 reports + Barone outputs filed; demand letter ready for attorney; impeachment worksheets seeded.

### Phase 3: Trial Notebook & Attorney Preparation

**Master orchestrator**: `dw-criminal-defense-crim` Phase 3

| Step | What happens | Skill(s) |
|---|---|---|
| 1 | Case Timeline Spreadsheet (Timeline Sheet with Certainty column) | `dw-timeline-builder-crim` |
| 2 | Update Witness Tables with Phase 2 intelligence | `dw-criminal-defense-crim` |
| 3 | Defense Shield & Defense Matrix (anchored on Report 4a selected theory) | `dw-criminal-defense-crim`, `dw-jury-instructions-builder-crim`, `dw-voir-dire-assistant-crim`, `dw-witness-threat-matrix-crim` |
| 4 | Version control for amended/superseded documents | `dw-criminal-defense-crim` |
| 5 | Case Readiness Memo | `dw-criminal-defense-crim` |
| 6 | Discover the Story Worksheet | `dw-criminal-defense-crim` |
| 7 | Cross-Exam Preparation per witness | `dw-cross-exam-architect-crim`, `dw-eyewitness-identification-auditor-crim`, `dw-expert-witness-evaluator-crim` |
| 8 | Direct-Exam Preparation | `dw-direct-exam-architect-crim` |
| 9 | Opening / Closing prep (uses Report 4 selected theory, Report 6 theme, Discover the Story) | `dw-trial-narrative-builder-crim` |
| 10 | Appellate readiness — error preservation | `dw-appellate-error-monitor-crim` |
| 11 | Trial-day live support | `dw-trial-day-assistant-crim` |
| 12 | Final notebook assembly | `dw-trial-notebook-builder-crim` |

---

## 5. Skill Catalog by Function

Every D&W skill organized by function. For trigger phrases see `dw-skill-index-crim`.

### 5.1 Master Orchestrators

| Skill | Role |
|---|---|
| `dw-criminal-defense-crim` (v5.9) | Master 3-phase orchestrator with embedded Barone steps |
| `dw-case-brain-crim` | Session persistence; loaded at open/close of every case session |
| `dw-case-dashboard-crim` | "Where do we stand" — case status snapshot |
| `dw-skill-index-crim` (v1.2) | Trigger-phrase routing manual |
| `dw-discovery-orchestrator-crim` | Triage routing for newly arrived discovery |
| `dw-transcript-router-crim` | Parish-based pipeline selection (JusticeText vs Rev) |
| `dw-trial-notebook-builder-crim` | Final assembly of all Phase 2 + 3 deliverables |

### 5.2 Intake & Setup

| Skill | What it does |
|---|---|
| `dw-client-intake-interview-crim` | First client meeting: conflict check, charge identification, immediate-action triage |
| `dw-criminal-defense-crim` Phase 1 | Folder setup, Bate-stamping, Case Profile, Case Tables |
| `dw-evidence-placeholder-crim` | Generates placeholder PDFs for media folders |
| `dw-image-filename-stamp-crim` | Stamps Bate references on image filenames |
| `medical-chronology` | PI medical chronology (companion to PI cases) |

### 5.3 Discovery Management

| Skill | What it does |
|---|---|
| `dw-neutral-inventory-crim` (NEW) | Report 0 — pre-strategic catalog of all discovery |
| `dw-discovery-compliance-monitor-crim` | Living ledger: demanded vs. produced; **7-bucket Barone classification** |
| `dw-brady-giglio-auditor-crim` | Brady/Giglio deep audit (separate from compliance ledger) |
| `dw-discovery-orchestrator-crim` | Newly-arrived discovery triage |
| `dw-court-jail-tracker-crim` | Local tracker for court dates and jail status |

### 5.4 Evidence Auditing

Each auditor produces a Contract 2 (or sub-contract) report saved to `Cowork Analysis/`.

| Skill | Audits |
|---|---|
| `dw-mobile-forensic-auditor-crim` | Cellebrite/GrayKey extraction methodology (HOW the phone was dumped) |
| `dw-forensic-dump-analyzer-crim` | Phone extraction contents (WHAT's on the phone) |
| `dw-sqlite-recovery-crim` | Deleted SQLite data recovery from phone dumps |
| `dw-video-evidence-auditor-crim` | BWC/dash/CCTV with **6-category Report-vs-Recording matrix** |
| `dw-crime-scene-auditor-crim` | Crime scene processing methodology |
| `dw-chain-of-custody-auditor-crim` | Evidence custody log integrity |
| `dw-cell-site-geolocation-auditor-crim` | CSLI / cell tower / GPS data |
| `dw-social-media-auditor-crim` | Facebook, Instagram, Snapchat, WhatsApp records |
| `dw-eyewitness-identification-auditor-crim` | Photo arrays, lineups, show-ups |
| `dw-confession-interrogation-auditor-crim` | Adult interrogation / Miranda / Reid technique audit |
| `dw-child-forensic-interview-auditor-crim` | CAC forensic interview protocol compliance |
| `dw-expert-witness-evaluator-crim` | Daubert/Foret challenges; Module I for hearing-day package |
| `dw-dna-forensic-biology-auditor-crim` | DNA: STR, mixtures, STRmix, TrueAllele, IGG, mtDNA, Y-STR |
| `dw-crime-lab-auditor-crim` | Drug ID, toxicology, blood alcohol, R.S. 15:499 certificate challenges |
| `dw-jail-call-analyzer-crim` | Securus / GTL / ViaPath / NCIC / IC Solutions recordings; cross-feeds witness-threat-matrix |
| `dw-witness-statement-analyzer-crim` | Per-witness statement inconsistency audit |
| `dw-habitual-offender-auditor-crim` | Habitual offender bill audit |

### 5.5 Theory Development (Barone)

| Skill | What it does |
|---|---|
| `dw-timeline-builder-crim` | Master timeline with Certainty column |
| `dw-theory-deconstructor-crim` (NEW) | Report 2a — facts/inferences/assumptions |
| `dw-criminal-defense-crim` Report 4 | Competing Defense Theories |
| `dw-criminal-defense-crim` Step 2A | Report 4a Theory Selection Memo |
| `dw-theory-to-workplan-crim` (NEW) | 7-stream action plan from selected theory |
| `dw-adversarial-stress-test-crim` (NEW) | Prosecutor red-team simulation |
| `dw-dmar-synthesizer-crim` | Cross-case witness/officer consistency audit (with Barone S4A matrix comparison) |

### 5.6 Transcript & Media Processing

| Skill | What it does |
|---|---|
| `dw-transcript-router-crim` | Routes to Calcasieu (JusticeText) or other parishes (Rev) |
| `dw-transcript-pipeline-calcasieu-crim` | JusticeText upload → DMAR with 6-category matrix |
| `dw-transcript-pipeline-rev-crim` | Rev.com upload → DMAR with 6-category matrix |
| `dw-dmar-synthesizer-crim` | Cross-case DMAR analysis |

### 5.7 Motions & Pleadings

All motion skills consult `dw-shared-protocols-crim/references/` for the firm's DEVONthink template-first protocol before drafting.

| Skill | Motion type |
|---|---|
| `dw-suppression-motion-crim` | 4th/5th/6th Amendment suppression (audit + motion modes) |
| `dw-404b-opposition-crim` | Oppose State 404(b) notice |
| `dw-bond-and-release-motion-crim` | Bond reduction / pretrial release |
| `dw-pretrial-motion-library-crim` | Speedy trial, bill of particulars, motion to compel, severance, venue, reveal the deal, recusal, continuance |

### 5.8 Trial Preparation

| Skill | What it does |
|---|---|
| `dw-cross-exam-architect-crim` | Chapter-based cross outlines for State witnesses. One .docx per witness: three-column Source Register, two-column chapter table, blank notes box, 12 pt |
| `dw-direct-exam-architect-crim` | Direct outlines for defense witnesses. Same template as cross, one .docx per witness; open-ended questions, cross-attack anticipation reported rather than printed |
| `dw-trial-narrative-builder-crim` | Opening + Closing + Theme Tracker + Rebuttal Anticipation Memo |
| `dw-jury-instructions-builder-crim` | Louisiana jury charge drafting |
| `dw-voir-dire-assistant-crim` | Voir dire strategy and question banks |
| `dw-defense-investigator-tasking-crim` | Generate concrete tasks for the defense investigator |
| `dw-witness-threat-matrix-crim` | Witness vulnerability ranking; receives jail-call tampering cross-feed |
| `dw-jury-focus-group-crim` | Mock juror reaction modeling |
| *(retired — `dw-exhibit-manager-crim`)* | Retired at `dw-trial-prep` v1.9 / `dw-criminal-defense-crim` v6.2. Exhibit list construction and authentication tracking now split between the **Evidence Table** in `Case Tables.xlsx` and `dw-trial-day-assistant-crim` **Module D** |
| `dw-trial-day-assistant-crim` | Real-time in-court support (objection log, witness scorecards, juror obs, mid-trial issues) |
| `dw-issue-code-tracker-crim` | Issue-code based docket tracking |

### 5.9 Sentencing, Appeal & Post-Conviction

| Skill | What it does |
|---|---|
| `dw-sentencing-mitigation-specialist-crim` | Mitigation package, family/community letters, character development |
| `dw-plea-negotiation-analyzer-crim` | Evaluate plea offers against trial exposure |
| `dw-case-disposition-crim` | Outcome documentation |
| `dw-appellate-error-monitor-crim` | Error preservation during trial; ranked-issue output |
| `dw-appellate-brief-builder-crim` | Direct-appeal brief assembly (statement of facts, assignments, argument, reply) |
| `dw-post-conviction-relief-crim` | PCR / federal habeas / sentence modification |

### 5.10 Charge-Type Specialists

Each provides charge-specific elements, defenses, sentencing exposure, motions, and discovery checklists.

| Skill | Charges |
|---|---|
| `dw-drug-offense-specialist-crim` | CDS, distribution, possession with intent |
| `dw-dwi-specialist-crim` | DWI / OWI / vehicular homicide |
| `dw-sex-offense-specialist-crim` | Sex offenses including SANE-exam audit |
| `dw-firearms-specialist-crim` | State and federal firearms offenses |
| `dw-violent-crime-specialist-crim` | Homicide, manslaughter, agg battery, agg assault, armed robbery, kidnapping, home invasion |

### 5.11 Client Communications & Operations

| Skill | What it does |
|---|---|
| `dw-client-communication-drafter-crim` | Standard client letters, updates, document requests |
| `dw-billing-narrative-generator-crim` | Time-entry narrative drafting |
| `dw-case-law-researcher-crim` | Statute and case-law lookup |

### 5.12 Shared References (Read by Other Skills)

| Skill | Purpose |
|---|---|
| `dw-shared-protocols-crim` | Protocol library — work-product marking, output-path formula, **verification protocol**, citation standards, template selection |
| `dw-data-contracts-crim` | Output schemas for all cross-skill deliverables (DMAR with 6-category matrix, auditor reports, cross/direct outlines — Contracts 3 and 3A, both now one .docx per witness — Case Tables, Case Brain entries, discovery ledger with bucket column) |

### 5.13 Non-Criminal / Utility

These exist in the same repo but are outside the criminal defense workflow.

| Skill | Purpose |
|---|---|
| `dw-settlement-demand` | **Relocated 2026-05-29** → `DW-Personal-Injury-Claude-Skills` repo (was out of scope here) |
| `iron-gavel-*` | Firm podcast operations (4 skills) |
| `frontend-design`, `ui-ux-pro-max` | UI/design utilities |
| `file-organizer`, `notebooklm`, `youtube-transcript` | General-purpose utilities |

---

## 6. Cross-Skill Integration Map

Skills produce structured outputs consumed by other skills. The contracts are defined in `dw-data-contracts-crim/SKILL.md`. Major flows:

### Theory development chain (Barone)
```
dw-neutral-inventory-crim ──┐
                       ├─→ dw-criminal-defense-crim Phase 2 Reports 1-8
dw-timeline-builder-crim ───┤      │
                       │      ↓
                       │   Report 2 (Prosecution Summary)
                       │      │
                       │      ↓
                       └─→ dw-theory-deconstructor-crim (Report 2a)
                              │
                              ↓
                          Report 4 (Competing Theories)
                              │
                              ↓ (attorney selects)
                          Report 4a (Theory Selection Memo)
                              │
                              ├─→ dw-adversarial-stress-test-crim
                              └─→ dw-theory-to-workplan-crim
                                       │
                                       ↓ (routes to 7 streams)
                                  All trial-prep skills
```

### Trial-day error preservation chain
```
dw-trial-day-assistant-crim Module B (objection log)
        │  same schema fields, additive only
        ↓
dw-appellate-error-monitor-crim Modules A/B
        │
        ↓ ranked appellate issues
dw-appellate-brief-builder-crim
```

### Witness intelligence cross-feed
```
dw-jail-call-analyzer-crim Module D ──→ dw-witness-threat-matrix-crim (Refresh Mode)
                                          │
                                          ↓ (re-rank witnesses)
                                   dw-cross-exam-architect-crim
```

### Audit → Motion routing
```
dw-confession-interrogation-auditor-crim Step 4 ──→ dw-suppression-motion-crim (Art. 703)
dw-eyewitness-identification-auditor-crim ──→ dw-suppression-motion-crim (suggestive ID)
dw-expert-witness-evaluator-crim ──→ dw-pretrial-motion-library-crim (Daubert/Foret motion)
dw-crime-lab-auditor-crim (R.S. 15:499) ──→ dw-suppression-motion-crim (Confrontation Clause)
```

### DMAR pipeline
```
dw-transcript-router-crim
        │
        ├─→ dw-transcript-pipeline-calcasieu-crim  ─→ DMAR (Section 4A: Report-vs-Recording Matrix)
        │                                            │
        └─→ dw-transcript-pipeline-rev-crim        ─→ DMAR ┘
                                                     │
                                                     ↓
                                          dw-dmar-synthesizer-crim (cross-case)
                                          dw-confession-interrogation-auditor-crim
                                          dw-video-evidence-auditor-crim
                                          dw-cross-exam-architect-crim
```

### Phase 2 Report 7 auto-action
```
Report 7 (Missing Discovery) ──→ Auto-draft Missing Discovery Demand Letter
                            └──→ dw-brady-giglio-auditor-crim (for CRITICAL items)
                            └──→ dw-discovery-compliance-monitor-crim (updates ledger)
```

---

## 7. Shared Protocols (Read These First)

Every skill loads these at Step 0.5. They are non-negotiable.

### 7.1 Attorney Work-Product Marking
Located at: `dw-shared-protocols-crim/references/attorney-work-product-marking.md`

Standard header on every internal D&W deliverable:
```
ATTORNEY WORK PRODUCT — PRIVILEGED AND CONFIDENTIAL
PREPARED IN ANTICIPATION OF LITIGATION
```

Filed pleadings do NOT carry the marking (it would defeat the privilege if filed). Internal analysis, audits, work plans, and drafts always do.

### 7.2 Output Path Formula
Located at: `dw-shared-protocols-crim/references/output-path-formula.md`

All deliverable paths anchor on `{{CASE_ROOT}}`:

| Deliverable type | Location |
|---|---|
| Filed pleadings | `{{CASE_ROOT}}/02 - Pretrial Notebook/01 - Pleadings/` |
| Internal analysis (Cowork Analysis) | `{{CASE_ROOT}}/01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/` |
| Auditor reports | `{{CASE_ROOT}}/01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/` |
| Sentencing materials | `{{CASE_ROOT}}/01 - Trial Notebook/10 - Sentencing/` |
| Cross / Direct outlines | `{{CASE_ROOT}}/01 - Trial Notebook/03 - Witnesses/{Prosecution\|Defense} Witnesses/` |
| Case Brain | `{{CASE_ROOT}}/brain.md` (internal) |
| Local tracker artifacts | `~/.dw-tracker/` |
| PI marketing (separate repo) | `{{FIRM_MARKETING_ROOT}}/...` |

### 7.3 Source Citation Mandate
Located at: top of every analytical skill

Every factual assertion must include:
- Source document title
- Page / paragraph / timestamp / Bate stamp
- For multiple sources, cite ALL of them
- Mark `[UNSOURCED — VERIFY]` if no source available

### 7.4 Verification Protocol (NEW — Barone)
Located at: `dw-shared-protocols-crim/references/verification-protocol.md`

Every catalog entry, fact extraction, or evidence reference must carry:
- `[VERIFIED]` — source directly reviewed in this session, assertion matches
- `[UNVERIFIED]` — assertion based on a reference; source not reviewed

Adds a layer on top of the Source Citation Mandate: citation tells you WHERE; verification tells you whether the source has actually been LOOKED AT.

End-of-deliverable verification summary required (% verified, top unverified gaps).

### 7.5 Case Tables Write Protocol
Located at: `dw-criminal-defense-crim/references/case-tables-write-protocol.md`

Mandatory protocol before any write to `Case Tables.xlsx`:
1. Warn (announce intent)
2. Confirm (wait for user/attorney OK)
3. Write
4. Verify (re-read and confirm)

Purpose: prevent Google Drive sync overwrites that lose data.

### 7.6 Template Selection Protocol
Located at: `dw-shared-protocols-crim/references/` (formerly the retired `dw-template-selector`)

Every motion-drafting skill searches DEVONthink's `Law Library-Criminal` database for prior firm templates before drafting from scratch. Use the closest matching prior brief as the structural starting point.

---

## 8. Practical Recipes

Common case workflows as actionable sequences. Each recipe is a recommended sequence — adjust to case facts.

### Recipe 1: New Violent Crime Case (Homicide / Agg Battery / Armed Robbery)

1. **Intake meeting**: "intake" → `dw-client-intake-interview-crim`
2. **Case file setup**: "new case" → `dw-criminal-defense-crim` Phase 1 (Steps 1-4)
3. **Charge-type specialist**: "armed robbery framework" → `dw-violent-crime-specialist-crim`
4. **Discovery prep**: as productions arrive, route via `dw-discovery-orchestrator-crim`
5. **Barone Phase 2**:
   - "neutral inventory" → `dw-neutral-inventory-crim` (Report 0)
   - "build the timeline" → `dw-timeline-builder-crim` (Report 1, with Certainty)
   - "run Phase 2" → `dw-criminal-defense-crim` Phase 2 (Reports 2, 3, 5-8)
   - "deconstruct the state's theory" → `dw-theory-deconstructor-crim` (Report 2a)
   - Review Report 4 Competing Theories with attorney → select theory → Report 4a
   - "stress test the theory" → `dw-adversarial-stress-test-crim`
   - "build a workplan" → `dw-theory-to-workplan-crim`
6. **Specialist audits triggered by Barone Stream 3**:
   - DNA/Forensic biology → `dw-dna-forensic-biology-auditor-crim`
   - Crime scene → `dw-crime-scene-auditor-crim`
   - Confession (if applicable) → `dw-confession-interrogation-auditor-crim`
   - Self-defense considerations → `dw-violent-crime-specialist-crim` (already loaded)
7. **Motion practice from Workplan Stream 4**:
   - Suppression → `dw-suppression-motion-crim`
   - 404(b) opposition → `dw-404b-opposition-crim`
   - Bond → `dw-bond-and-release-motion-crim`
8. **Trial prep (Phase 3)**: Defense Shield, cross/direct, opening/closing, voir dire, jury instructions
9. **Trial day**: `dw-trial-day-assistant-crim`
10. **Post-verdict**: `dw-appellate-error-monitor-crim` → `dw-appellate-brief-builder-crim` or `dw-post-conviction-relief-crim`

### Recipe 2: New DWI / Vehicular Homicide

1. Intake → `dw-client-intake-interview-crim`
2. Phase 1 → `dw-criminal-defense-crim`
3. Charge specialist: "DWI framework" → `dw-dwi-specialist-crim`
4. Barone Phase 2 (as above)
5. **DWI-specific audits**:
   - Toxicology / Intoxilyzer → `dw-crime-lab-auditor-crim` (R.S. 15:499 audit critical)
   - BWC of traffic stop → `dw-video-evidence-auditor-crim` (6-category matrix)
   - Confession during DUI investigation → `dw-confession-interrogation-auditor-crim`
6. Motions: Suppress stop (4th Amendment), suppress chemical test, exclude HGN expert
7. Trial prep + trial day as in Recipe 1

### Recipe 3: New Drug Case

1. Intake → Phase 1 → `dw-drug-offense-specialist-crim`
2. Barone Phase 2
3. **Drug-specific audits**:
   - Search warrant → `dw-suppression-motion-crim` (warrant deep-dive)
   - Crime lab report → `dw-crime-lab-auditor-crim` (SWGDRUG, GC-MS confirmatory)
   - Chain of custody from seizure to lab → `dw-chain-of-custody-auditor-crim`
   - Phone evidence (texts, social media) → `dw-mobile-forensic-auditor-crim` → `dw-forensic-dump-analyzer-crim`
4. R.S. 15:499 confrontation clause analysis (in crime lab audit)
5. Standard trial prep + trial day

### Recipe 4: New Sex Offense

1. Intake → Phase 1 → `dw-sex-offense-specialist-crim` (includes SANE-exam audit framework)
2. Barone Phase 2
3. **Sex-offense-specific audits**:
   - Child forensic interview → `dw-child-forensic-interview-auditor-crim`
   - SANE report → `dw-sex-offense-specialist-crim` Module on SANE-exam
   - DNA → `dw-dna-forensic-biology-auditor-crim`
   - Expert testimony (CSAAS, child witness, etc.) → `dw-expert-witness-evaluator-crim`
4. Motions: Daubert/Foret on expert; 412 opposition; 404(b) opposition
5. Trial prep emphasizing victim cross (sensitive) and theme development

### Recipe 5: Mid-Trial Live Support (Already in Court)

1. "log this objection" → `dw-trial-day-assistant-crim` Module B
2. End of day: `dw-trial-day-assistant-crim` produces:
   - Updated objection log → feeds `dw-appellate-error-monitor-crim`
   - Witness scorecards → feeds `dw-cross-exam-architect-crim` for tomorrow's prep
   - Juror observation log including Batson tracking
   - Exhibit tracker
   - End-of-day recap with overnight tasks
3. Overnight: "build a cross for [tomorrow's witness]" → `dw-cross-exam-architect-crim` (consumes today's witness scorecard if same witness)
4. Mid-trial issue spotter for Brady, surprise testimony, mistrial triggers under La. C.Cr.P. Art. 770/771 → `dw-trial-day-assistant-crim`

### Recipe 6: Post-Verdict / Appeal

1. Last `dw-appellate-error-monitor-crim` refresh — produces ranked appellate issues
2. "post-verdict motion package" → `dw-appellate-error-monitor-crim` (post-trial motions for new trial, JOA)
3. Record designation review
4. "appellate brief" → `dw-appellate-brief-builder-crim` (assignments of error, statement of facts with record cites, per-assignment argument: standard of review → preservation → law → application → prejudice, reply brief)
5. For collateral relief (PCR, federal habeas, sentence mod) → `dw-post-conviction-relief-crim`

### Recipe 7: New Discovery Arrived Mid-Case

1. "new discovery arrived" → `dw-discovery-orchestrator-crim` (triages to auditors)
2. Pipeline routes new audio/video → `dw-transcript-router-crim` → DMAR (with Report-vs-Recording matrix)
3. Update `dw-discovery-compliance-monitor-crim` ledger (with 7-bucket classification)
4. Re-run `dw-theory-deconstructor-crim` (Report 2a) if new evidence affects state's theory
5. Re-run `dw-adversarial-stress-test-crim` (one of its standard re-run triggers)
6. Update `dw-theory-to-workplan-crim` — new tasks if vulnerabilities shifted

### Recipe 8: Plea Offer Received

1. "analyze the plea offer" → `dw-plea-negotiation-analyzer-crim`
2. Cross-check sentencing exposure with `dw-sentencing-mitigation-specialist-crim`
3. If habitual claim implicated → `dw-habitual-offender-auditor-crim`
4. Cross-check defense theory viability — pull Report 4a + Stress Test + Workplan to assess trial path

---

## 9. Reference Appendices

### 9.1 Quick Trigger Phrase Index (Top 30)

| Say | Skill |
|---|---|
| "intake" / "new client" / "first meeting" | `dw-client-intake-interview-crim` |
| "new case" / "case intake" / "run Phase 1" | `dw-criminal-defense-crim` |
| "load the case" / "open the matter" | `dw-case-brain-crim` |
| "where do we stand" / "case status" | `dw-case-dashboard-crim` |
| "what skills do we have" / "skill list" | `dw-skill-index-crim` |
| "neutral inventory" / "catalog the evidence" | `dw-neutral-inventory-crim` |
| "build the timeline" / "master timeline" | `dw-timeline-builder-crim` |
| "run Phase 2" | `dw-criminal-defense-crim` |
| "deconstruct the state's theory" / "Report 2a" | `dw-theory-deconstructor-crim` |
| "stress test the theory" / "red team" | `dw-adversarial-stress-test-crim` |
| "build a workplan" / "theory to workplan" | `dw-theory-to-workplan-crim` |
| "transcribe the evidence" | `dw-transcript-router-crim` |
| "motion to suppress" | `dw-suppression-motion-crim` |
| "audit body cam" | `dw-video-evidence-auditor-crim` |
| "DNA audit" | `dw-dna-forensic-biology-auditor-crim` |
| "audit the crime lab" / "criminalist certificate" | `dw-crime-lab-auditor-crim` |
| "audit jail calls" / "Securus" | `dw-jail-call-analyzer-crim` |
| "audit interrogation" | `dw-confession-interrogation-auditor-crim` |
| "audit the CAC video" | `dw-child-forensic-interview-auditor-crim` |
| "build a cross for [witness]" | `dw-cross-exam-architect-crim` |
| "build a direct for [witness]" | `dw-direct-exam-architect-crim` |
| "draft opening" / "draft closing" | `dw-trial-narrative-builder-crim` |
| "preserve error" / "log error" | `dw-appellate-error-monitor-crim` |
| "log this objection" / "today's witness" | `dw-trial-day-assistant-crim` |
| "appellate brief" / "assignments of error" | `dw-appellate-brief-builder-crim` |
| "PCR" / "habeas" / "post-conviction" | `dw-post-conviction-relief-crim` |
| "build sentencing mitigation" | `dw-sentencing-mitigation-specialist-crim` |
| "analyze the plea offer" | `dw-plea-negotiation-analyzer-crim` |
| "DWI" / "DUI" | `dw-dwi-specialist-crim` |
| "drug case" / "CDS" | `dw-drug-offense-specialist-crim` |
| "sex offense" / "SANE" | `dw-sex-offense-specialist-crim` |
| "armed robbery" / "manslaughter" / "self-defense" | `dw-violent-crime-specialist-crim` |
| "felon in possession" / "firearm charge" | `dw-firearms-specialist-crim` |
| "audit the lineup" | `dw-eyewitness-identification-auditor-crim` |
| "audit the Cellebrite" | `dw-mobile-forensic-auditor-crim` |
| "analyze the phone dump" | `dw-forensic-dump-analyzer-crim` |
| "audit chain of custody" | `dw-chain-of-custody-auditor-crim` |
| "audit cell site" | `dw-cell-site-geolocation-auditor-crim` |
| "social media" / "audit Facebook" | `dw-social-media-auditor-crim` |
| "audit crime scene" | `dw-crime-scene-auditor-crim` |
| "recover deleted messages" | `dw-sqlite-recovery-crim` |
| "evaluate the expert" / "Daubert hearing prep" | `dw-expert-witness-evaluator-crim` |
| "compare the DMARs" | `dw-dmar-synthesizer-crim` |
| "update the discovery ledger" | `dw-discovery-compliance-monitor-crim` |
| "run Brady audit" | `dw-brady-giglio-auditor-crim` |
| "audit the habitual bill" | `dw-habitual-offender-auditor-crim` |
| "draft jury instructions" | `dw-jury-instructions-builder-crim` |
| "prep voir dire" | `dw-voir-dire-assistant-crim` |
| "investigator assignment" | `dw-defense-investigator-tasking-crim` |
| "build the trial notebook" | `dw-trial-notebook-builder-crim` |

### 9.2 File Output Locations (Master List)

All paths anchored on `{{CASE_ROOT}}`:

```
{{CASE_ROOT}}/
├── 01 - Trial Notebook/
│   ├── 02 - Opening & Closing/        ← courtroom-ready opening/closing
│   ├── 03 - Witnesses/
│   │   ├── Prosecution Witnesses/     ← cross outlines, battle cards
│   │   └── Defense Witnesses/         ← direct outlines, witness prep
│   ├── 05 - Evidence/                 ← Bate-stamped, OCR'd, media placeholders
│   ├── 09 - Case Analysis/
│   │   ├── Report 1 — Timeline.docx   ← (also in Case Tables Timeline sheet)
│   │   ├── Report 2 — Prosecution Case Summary.docx
│   │   ├── Report 3 — Red Flags.docx
│   │   ├── Report 4 — Competing Defense Theories.docx
│   │   ├── Report 5 — Viable Legal Defenses.docx
│   │   ├── Report 6 — Memorable Theme.docx
│   │   ├── Report 7 — Table of Missing Discovery.docx
│   │   ├── Report 8 — Key Witness Impeachment Plan.docx
│   │   └── Cowork Analysis/           ← all internal work-product
│   │       ├── Report 0 — Neutral Discovery Inventory.docx
│   │       ├── Report 2a — Theory Deconstruction.docx
│   │       ├── Report 4a — Theory Selection Memo.docx
│   │       ├── Adversarial Stress Test.docx
│   │       ├── Theory-to-Workplan.docx
│   │       ├── [Auditor reports].docx
│   │       ├── DMAR — [Client] [Date].docx
│   │       └── Missing Discovery Demand — [Date].docx
│   └── 10 - Sentencing/               ← sentencing memo, mitigation package
├── 02 - Pretrial Notebook/
│   ├── 01 - Pleadings/                ← all filed motions
│   ├── 02 - Discovery/                ← demand letters, productions
│   └── 03 - Case Analysis & Notes/    ← Case Profile lives here
├── Case Tables.xlsx                   ← Evidence Table, Timeline (Certainty col),
│                                       Witness Lists, Defense Matrix
├── Bate Stamp Master Log.xlsx
└── brain.md                           ← Case Brain (internal)
```

### 9.3 Versioning Reference

| Component | Current Version | Changes in This Release |
|---|---|---|
| Operations Guide | **v1.3** (this document) | Barone workflow integration; new skill catalog organization; full skill list with PI & utility |
| `dw-criminal-defense-crim` | v5.9 | Report 4 → Competing Theories; new Report 4a; Steps 1E and 2A; Certainty column to Phase 3 Step 1 |
| `dw-data-contracts-crim` | v1.2 | DMAR Section 10 (6-category matrix); Timeline Certainty col; Discovery Bucket col |
| `dw-skill-index-crim` | v1.2 | 4 new skill rows; Barone Discovery Workflow section |
| `dw-shared-protocols-crim` | (added) `verification-protocol.md` | [VERIFIED]/[UNVERIFIED] flags |
| New skills | v1.0 each | `dw-neutral-inventory-crim`, `dw-theory-deconstructor-crim`, `dw-theory-to-workplan-crim`, `dw-adversarial-stress-test-crim` |

### 9.4 Glossary

| Term | Definition |
|---|---|
| **Barone Workflow** | The 9-step Discovery Workflow Audit pipeline — pre-strategic inventory through adversarial stress test |
| **Bate Stamp** | Sequential identifier assigned to each page of discovery for unambiguous reference |
| **Brady / Giglio / Kyles** | Constitutional doctrines requiring State to disclose exculpatory + impeachment evidence |
| **Case Brain** | Per-case session memory (`brain.md`) that persists state across Cowork sessions |
| **Case Tables.xlsx** | The case spreadsheet — Evidence Table, Timeline, Witness Lists, Defense Matrix |
| **Certainty** | Barone Timeline rating (CONFIRMED / PROBABLE / DISPUTED / UNCONFIRMED / ALLEGED) — distinct from Confidence (timestamp precision) |
| **Competing Theories** | Multiple viable defense narratives presented in revised Report 4, replacing single Core Defense Narrative |
| **Cowork** | The Claude-on-the-web project deployment for the firm |
| **CASE_ROOT** | The root folder for a case; all output paths anchor here |
| **DMAR** | Defense Media Analysis Report — standardized audio/video/transcript audit output |
| **Discovery Bucket** | One of seven Barone classifications applied to ledger entries (Law Enforcement / Physical-Forensic / Digital-Electronic / Witness / Expert / Prosecution File / Brady-Giglio) |
| **LWOP** | Life Without Parole — homicide and certain sex offenses requiring Part 2A or 2B in the Case Profile |
| **Report 0** | Barone neutral discovery inventory, runs before all strategic analysis |
| **Report 2a** | Barone theory deconstruction (facts / inferences / assumptions) |
| **Report 4a** | Theory Selection Memo — attorney's documented choice from Report 4 competing theories |
| **Report-vs-Recording Matrix** | 6-category Barone DMAR comparison (Narrative Match / Omissions / Additions / Timing / Quote Accuracy / Procedural Compliance) |
| **Source Citation Mandate** | Every factual assertion must trace to a specific source document |
| **Verification Protocol** | Barone [VERIFIED] / [UNVERIFIED] tagging system — supplements Source Citation Mandate |

### 9.5 Where Things Live in the Repository

```
DW-Criminal-Defense-Claude-Skills/
├── CLAUDE.md                    ← Developer / contributor instructions
├── README.md
├── bin/
│   ├── lint-skills.py           ← Run before every commit
│   ├── dw-skill-git.sh          ← Sync GitHub repo ↔ ~/.claude/skills
│   ├── auto-pull.sh             ← Background auto-pull
│   └── install-agent.sh         ← LaunchAgent installer for auto-pull
├── docs/
│   ├── DW_Skills_Operations_Guide_v1.4.md   ← This file
│   ├── DW_Skills_Operations_Guide_v1.2.docx ← Superseded
│   ├── DW_Criminal_Defense_Cowork Project_Instructions_1.md
│   └── Updated_Skill_Map_March_2026.docx
├── outputs/
│   └── barone_changes/          ← apply.py and staging files for local sync
└── skills/                      ← Canonical skill collection
    ├── dw-criminal-defense-crim/     ← Master orchestrator
    ├── dw-skill-index-crim/          ← Routing manual
    ├── dw-shared-protocols-crim/     ← Protocol library
    ├── dw-data-contracts-crim/       ← Cross-skill schemas
    └── dw-*/                    ← All other D&W skills
```

---

## How to Update This Guide

When the skill collection changes — new skills, retired skills, new workflow steps, contract changes — update this guide so it reflects the current state of the suite. Steps:

1. Update the relevant section (catalog / workflow / recipes)
2. Add a row to **Section 9.3 Versioning Reference**
3. If trigger phrases changed, update **Section 9.1**
4. Bump the version at the top of this document (currently v1.3)
5. Run `bin/lint-skills.py` to confirm no skill references broke
6. Commit with a descriptive message: `docs: Operations Guide v1.x — [summary of changes]`

For new skills, also:
- Add to `dw-skill-index-crim/SKILL.md` (or run `bin/regen-skill-index.py`)
- Add output contract to `dw-data-contracts-crim/SKILL.md` if the skill produces structured output
- Update Cowork project instructions if firm-wide workflow shifted

---

*Daniels & Washington — Skills Operations Guide v1.3 — May 2026*
*Supersedes v1.2 (April 2026). Maintained as Markdown for diff-friendly version control.*

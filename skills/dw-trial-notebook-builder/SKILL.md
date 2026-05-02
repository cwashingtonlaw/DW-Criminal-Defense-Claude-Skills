---
name: dw-trial-notebook-builder
category: trial-prep
description: >
  Assemble the final trial notebook from all upstream deliverables. ALWAYS invoke for
  "build the trial notebook," "assemble trial notebook," "trial notebook," "trial binder,"
  "trial prep package," "ready for trial," "pull together the trial file," "notebook builder,"
  or "what do we have for trial." Scans the case folder and Case Brain for all Phase 2-4
  deliverables, organizes them into the Trial Notebook folder structure, generates a master
  index with file:// links, produces a Trial Readiness Gap Report showing what's missing,
  and includes attorney checklists (Day of Trial, Exhibit Authentication, Witness Schedule).
  The capstone skill that ties every other D&W skill together into a courtroom-ready package.
  Do NOT use for individual deliverables — use the dedicated skill (dw-cross-exam-architect,
  dw-jury-instructions-builder, etc.). Do NOT use for case status checks — use dw-case-dashboard.
---

# Trial Notebook Builder
**Daniels & Washington | Criminal Defense | Louisiana / 5th Circuit Default**

This skill is the capstone of the D&W criminal defense workflow. It collects every
deliverable produced by upstream skills across Phases 2, 3, and 4, verifies they exist and
are filed correctly in the Trial Notebook folder structure, identifies gaps, and produces a
**Master Trial Index** — a single document with `file://` links to every item in the
notebook — plus attorney-facing checklists for courtroom use.

The Trial Notebook Builder does not *create* the underlying deliverables. It *assembles*
them. If a cross-examination outline is missing, this skill tells you to run
`dw-cross-exam-architect`. If jury instructions haven't been drafted, it points you to
`dw-jury-instructions-builder`. Its job is to give the attorney a clear, organized picture of
what's ready, what's missing, and what to do about the gaps — then produce the courtroom-ready
package from everything that exists.

```
Phase 2 outputs ─┐
Phase 3 outputs ─┤── Trial Notebook Builder ──► Organized folder + Master Index + Gap Report + Checklists
Phase 4 outputs ─┘
```

---

## STEP 0 — FILE INTAKE HARD STOP (Always First)

This skill consumes **finished deliverables** (jury charges, witness materials, exhibit lists, motions, case analysis reports) — not raw discovery. Before scanning the case folder or generating any index, confirm that no further deliverables are inbound.

**If the user has uploaded or referenced any trial notebook deliverables (jury charges, witness materials, exhibit lists, motions, case analysis reports) or pretrial notebook contents, do not start the assembly yet.**

Your only response must be:

> *"Before I begin assembling the trial notebook — are you uploading any additional trial notebook deliverables (jury charges, witness materials, exhibit lists, motions, case analysis reports) or pretrial notebook contents? I'll start the scan and Master Index build only after you confirm: 'No more uploads now.'"*

Proceed **only** after the user explicitly confirms no further uploads. If more are coming, acknowledge and wait. This hard stop is especially important for this skill because the Master Index and Gap Report are point-in-time snapshots — adding deliverables mid-build produces a stale index.

Once the user confirms, proceed to Step 0.5.

---

## STEP 0.5 — LOAD SHARED PROTOCOLS

Before scanning the case folder or producing the Master Index, read `dw-shared-protocols/SKILL.md` and load these references:

1. `dw-shared-protocols/references/attorney-work-product-marking.md` — apply work product marking to the Trial Readiness Gap Report, Master Trial Index, and the three attorney checklists (all internal deliverables).
2. `dw-shared-protocols/references/output-path-formula.md` — use for all output file paths (anchored on `{{CASE_ROOT}}`).

Do not proceed to Step 1 until these protocols are loaded. The Master Index, Gap Report, and Checklists are internal work product. Trial Notebook Builder writes directly into the trial notebook itself — its outputs anchor on `{{CASE_ROOT}}/01 - Trial Notebook/` (Master Index, Gap Report, and Checklists save to `{{CASE_ROOT}}/` at the case root, alongside `Case Tables.xlsx`). See the "Output Paths" section near the bottom of this skill for the full path table.

---

## Source Citation Mandate

Every "FOUND," "MISSING," or "PARTIAL" entry in the Inventory Table, every gap callout in the Gap Report, and every link in the Master Trial Index must trace back to a specific source — either a verified file path on disk or a Case Brain entry. The Master Index is the attorney's single courtroom entry point; a fabricated or stale link here is worse than no link at all.

**Citation format:**
- Inventory entries: `(Found at: {{CASE_ROOT}}/01 - Trial Notebook/03 - Witnesses/Prosecution Witnesses/[filename], modified [YYYY-MM-DD])`
- Gap entries: `(Expected at: {{CASE_ROOT}}/[expected path]; not present in folder scan or Case Brain COMPANION SKILL OUTPUTS)`
- Case Brain entries: `(Case Brain — COMPANION SKILL OUTPUTS, entry dated [YYYY-MM-DD])`
- Case Tables entries: `(Case Tables.xlsx — [Sheet name], Row [N])`

**Multiple-source rule:** When the folder scan and the Case Brain disagree (deliverable in folder but not in Brain, or vice versa), surface both in the Case Brain Sync Issues section of the Gap Report — never silently pick one.

**Unsourced assertions:** If a "FOUND" status cannot be tied to an actually-readable file on disk, mark it `[UNSOURCED — VERIFY]` and downgrade to PARTIAL/MISSING for the Gap Report. Verify every `file://` link target exists before adding it to the Master Index — a dead link is worse than a flagged gap.

**Where sourcing applies:** All inventory rows, all Gap Report entries, all Master Index links, and any "Cross Prepared?" or "Status" entry in the Witness Schedule and Exhibit Authentication checklists. Boilerplate checklist items (e.g., "Arrive early") do not require citation.

---

## STEP 0.6 — LOAD CASE CONTEXT

The Trial Notebook Builder requires case context to function. It needs to know where the
case folder is and what the case brain says about deliverables already produced.

### 0A — Identify the Case Folder

The case folder is either:
- Already mounted in the Cowork workspace (check `/sessions/.../mnt/` for the case folder)
- Specified by the attorney ("build the trial notebook for Tezeno")

If no case folder is evident, ask:
> *"Which case are we building the trial notebook for? I need the case folder mounted or the client name so I can locate it."*

### 0B — Load the Case Brain

Read the Case Brain from the Obsidian vault (follow `dw-case-brain` environment detection —
in Cowork, use the mounted `DW-CASE BRAINS` folder; in Claude Code, try MCP first).

From the Case Brain, extract:
- Client name and docket number
- Current phase (should be Phase 3 or 4 — if earlier, warn the attorney)
- Charges and statutory citations
- Lead attorney
- Trial date (if set)
- `COMPANION SKILL OUTPUTS` section — list of all deliverables already produced by other skills
- `gdrive_path` — for constructing `file://` links
- Theory of defense / case theme

If the Case Brain is not available, proceed with a folder-only scan but warn:
> *"No Case Brain found — I'll scan the folder structure directly, but I may miss deliverables stored outside the case folder."*

### 0C — Confirm Scope

Before scanning, confirm with the attorney:
> *"I'm ready to build the trial notebook for [Client Name] ([Docket #]). I'll scan the case folder, check for all upstream deliverables, organize the Trial Notebook tabs, generate the Master Index, identify gaps, and build your courtroom checklists. Anything specific you want me to focus on or skip?"*

Proceed after confirmation.

---

## STEP 1 — SCAN & INVENTORY

Systematically scan the case folder to find every deliverable. The scan covers both the
Trial Notebook and Pretrial Notebook because some deliverables (motions, discovery analysis)
live in the Pretrial Notebook but feed into trial preparation.

### 1A — Trial Notebook Folder Scan

The D&W Trial Notebook uses this 9-tab structure:

| Tab | Folder Path | What to Look For |
|-----|-------------|------------------|
| Tab 1 | `01 - Trial Notebook/01 - Jury Instructions & Selection/` | Proposed jury charges, verdict forms, responsive verdict analysis, Art 814 documents, voir dire question outlines, juror questionnaires, strike lists, Batson tracking |
| Tab 2 | `01 - Trial Notebook/02 - Opening Statement/` | Opening statement outlines, Mapping the Story — Opening worksheet, case theme documents |
| Tab 3 | `01 - Trial Notebook/03 - Witnesses/` | Cross-exam outlines (.docx), source catalogs (.pdf), combined source documents (.pdf), impeachment worksheets, witness battle cards, direct exam templates, witness dossiers. Check `Prosecution Witnesses/`, `Defense Witnesses/`, and `Expert Witnesses/` subfolders |
| Tab 4 | `01 - Trial Notebook/04 - Closing Argument/` | Closing argument outlines, Mapping the Story — Closing worksheet, exhibit reference lists for closing, jury charge tie-in notes |
| Tab 5 | `01 - Trial Notebook/05 - Evidence/` | Bate-stamped documents, digital evidence placeholders, transcripts, media files, exhibit list |
| Tab 6 | `01 - Trial Notebook/06 - Pleadings/` | Motions in limine, suppression motions, 404(b) oppositions, Prieur notice responses, all filed trial-phase pleadings and court rulings |
| Tab 7 | `01 - Trial Notebook/07 - PT Orders_Law/` | Pretrial orders, court rulings on motions, legal memoranda, statutory compilations, case law research |
| Tab 8 | `01 - Trial Notebook/08 - Verdict_Sentencing/` | Verdict forms, responsive verdict worksheets, sentencing memoranda, mitigation materials, PSI reports/corrections, post-trial motions, Dorthey briefs |
| Tab 9 | `01 - Trial Notebook/09 - Case Analysis/` | All 9 case analysis reports, Cowork parallel analysis outputs, missing discovery demands, defense strategy notes |

**Note:** Some case folders may have slight naming variations. Adapt to the folder structure
you find, but flag any non-standard organization in the gap report.

### 1B — Pretrial Notebook Scan

Also scan the Pretrial Notebook for trial-relevant items:

| Folder | What to Look For |
|--------|------------------|
| `02 - Pretrial Notebook/01 - Pleadings/` | Pretrial motions, bond motions, discovery motions, arraignment filings |
| `02 - Pretrial Notebook/02 - Discovery/` | Raw discovery productions, State's index, discovery compliance ledger |
| `02 - Pretrial Notebook/03 - Case Analysis & Notes/` | Initial Case Profile, LWOP Worksheet, Criminal Defense Cover, attorney notes |

### 1C — Case Tables Audit

Open `Case Tables.xlsx` at the case root and verify these sheets exist and are populated:

| Sheet | Phase | Status Check |
|-------|-------|-------------|
| Evidence Table | Phase 1 | Row count > 0; check for empty Review Priority or Defense Relevance columns |
| Timeline Sheet | Phase 2/3 | Row count > 0; check chronological ordering |
| Witness Sheet | Phase 2 | Row count > 0 |
| Witness List - Alpha | Phase 3 | Row count > 0 |
| Witness List - Priority | Phase 3 | Row count > 0 |
| Defense Matrix | Phase 3 | Row count > 0; check for empty Defense column cells |

### 1D — Cross-Reference with Case Brain

Compare the scan results against the Case Brain's `COMPANION SKILL OUTPUTS` section:
- Flag any deliverable listed in the Case Brain but not found in the folder (moved? deleted?)
- Flag any deliverable found in the folder but not recorded in the Case Brain (update needed)

### 1E — Build the Inventory Table

Compile a complete inventory as a structured table:

| # | Deliverable | Expected Location | Status | File Name | Notes |
|---|------------|-------------------|--------|-----------|-------|
| 1 | Jury Instructions Package | Tab 1 | FOUND / MISSING / PARTIAL | [filename] | [any issues] |
| 2 | Verdict Form | Tab 8 | ... | ... | ... |
| ... | ... | ... | ... | ... | ... |

Use the full deliverable checklist in `references/deliverable-map.md` to ensure nothing
is missed.

---

## STEP 2 — TRIAL READINESS GAP REPORT

This is the most important output for cases that aren't fully trial-ready yet. The Gap Report
tells the attorney exactly what's missing and how to fill each gap.

### Gap Report Structure

Generate `Trial Readiness Gap Report — [Client Name] [Date].docx` and save to the case root.

**Section 1 — Executive Summary**
- Case caption, docket, charges, trial date
- Overall readiness score: READY / NEAR-READY / SIGNIFICANT GAPS / NOT TRIAL-READY
  - READY: all essential deliverables present, no critical gaps
  - NEAR-READY: all critical items present, 1-3 non-critical gaps remaining
  - SIGNIFICANT GAPS: one or more critical deliverables missing
  - NOT TRIAL-READY: case is still in Phase 1 or 2, multiple critical gaps

**Section 2 — Critical Gaps (Must-Fix Before Trial)**
For each missing critical deliverable:
- What's missing
- Why it matters for trial
- Which D&W skill to run to produce it (with the exact trigger phrase)
- Estimated time to produce

Critical deliverables (must exist for trial):
- At least one cross-examination outline per key prosecution witness
- Jury instructions / proposed charges
- Verdict form with responsive verdicts
- Defense matrix (charges + defenses + responsive verdicts)
- Exhibit list
- Opening statement outline (at minimum)
- Case timeline

**Section 3 — Non-Critical Gaps (Recommended)**
For each missing non-critical deliverable:
- What's missing
- How it would strengthen trial preparation
- Which skill to run

Non-critical but valuable:
- Closing argument outline
- Voir dire question outline / juror questionnaire
- Witness scheduling worksheet
- 404(b) opposition (if Prieur notice was filed)
- Appellate error preservation log
- Sentencing mitigation package (if relevant)
- LWOP worksheet updates (if applicable)

**Section 4 — Folder Organization Issues**
- Files found in wrong locations
- Missing standard subfolders
- Naming convention violations
- Duplicate files

**Section 5 — Case Brain Sync Issues**
- Deliverables in Brain but not in folder
- Deliverables in folder but not in Brain

---

## STEP 3 — ORGANIZE THE TRIAL NOTEBOOK

With the inventory complete, organize the Trial Notebook folder:

### 3A — File Placement

Move or copy any misplaced files to their correct Trial Notebook tab:
- Cross-exam outlines → Tab 3 (Witnesses)
- Jury instructions → Tab 1
- Motions in limine / suppression motions → Tab 6 (Pleadings)
- Pretrial orders and court rulings → Tab 7 (PT Orders_Law)
- Verdict forms and sentencing materials → Tab 8 (Verdict_Sentencing)
- Case analysis reports → Tab 9

**Ask before moving files that are ambiguous.** Never silently relocate a file the attorney
may have intentionally placed somewhere.

### 3B — Create Missing Standard Subfolders

If any standard Trial Notebook tab folder or subfolder is missing, create it. The standard
structure with recommended subfolders is:

```
01 - Trial Notebook/
├── 01 - Jury Instructions & Selection/
│   ├── Defense Proposed Instructions/
│   ├── State Proposed Instructions/
│   ├── Court's Charge Packet/
│   └── Voir Dire/
│       ├── Question Outlines/
│       ├── Juror Questionnaires/
│       └── Strike Tracking/
├── 02 - Opening Statement/
│   ├── Drafts/
│   └── Mapping the Story/
├── 03 - Witnesses/
│   ├── Prosecution Witnesses/
│   ├── Defense Witnesses/
│   ├── Expert Witnesses/
│   └── Subpoenas/
├── 04 - Closing Argument/
│   ├── Drafts/
│   ├── Mapping the Story/
│   └── Exhibit References/
├── 05 - Evidence/
│   ├── Documents/
│   ├── Audio-Video/
│   ├── Photos/
│   ├── Digital Evidence Placeholders/
│   └── Transcripts/
├── 06 - Pleadings/
│   ├── Motions in Limine/
│   ├── Suppression Motions/
│   ├── Other Trial Motions/
│   └── Court Rulings/
├── 07 - PT Orders_Law/
│   ├── Pretrial Orders/
│   ├── Legal Memoranda/
│   ├── Statutory Research/
│   └── Case Law/
├── 08 - Verdict_Sentencing/
│   ├── Verdict Forms/
│   ├── Sentencing Memoranda/
│   ├── Mitigation Materials/
│   ├── PSI Reports/
│   └── Post-Trial Motions/
└── 09 - Case Analysis/
    ├── Cowork Analysis/
    ├── Reports/
    └── Defense Strategy/
```

### 3C — Naming Convention Audit

Check that all documents follow the D&W naming convention: `[3-digit prefix] - [Document Name].ext`

Flag any violations but do not auto-rename — present a rename suggestion table for attorney
approval.

---

## STEP 4 — GENERATE THE MASTER TRIAL INDEX

The Master Trial Index is the attorney's single entry point to the entire trial file. It is
a `.docx` document with `file://` links to every deliverable, organized by Trial Notebook tab.

### Index Document Structure

**File name:** `MASTER TRIAL INDEX — [Client Last Name] [Date].docx`
**Save to:** Case root (same level as `Case Tables.xlsx`)

**Cover Section:**
```
MASTER TRIAL INDEX
State v. [Client Name]
Docket: [Number] | [Court] | [Parish]
Charges: [Summary]
Trial Date: [Date or "NOT SET"]
Lead Attorney: [Name]
Defense Theme: [One-line theme from Case Brain]
Generated: [Date] | Readiness: [READY / NEAR-READY / etc.]
```

**For each Trial Notebook tab, create a section with:**

1. **Tab header** with the tab number and name
2. **Table of deliverables** within that tab:

| # | Document | Type | Date | Status | Link |
|---|----------|------|------|--------|------|
| 1 | Cross-Examination — Officer LeBlanc | .docx | 2026-03-15 | Complete | [Open](file://...) |
| 2 | Source Catalog — Officer LeBlanc | .pdf | 2026-03-15 | Complete | [Open](file://...) |

3. **Gap callouts** for any missing items in that tab (red text or bold flag)

**After all tabs, include:**
- **Pretrial Notebook Cross-References** — links to key pretrial items that inform trial
  (arraignment filings, discovery motions, pretrial orders)
- **Case Tables Link** — direct `file://` link to `Case Tables.xlsx`
- **Case Brain Link** — if the Case Brain is in the Obsidian vault, link to it

### Constructing file:// Links

Use the `gdrive_path` from the Case Brain to construct host-path `file://` links. Apply
the same URL encoding rules as `dw-case-brain`:
- Spaces → `%20`
- Commas → `%2C`
- `@` → `%40`
- `&` → `%26`
- Parentheses → `%28` / `%29`

**In Cowork:** The mounted path (e.g., `/sessions/.../mnt/[Case Folder]`) is the working
path, but `file://` links in the index must use the **host path** from `gdrive_path` so they
work on the attorney's Mac. If `gdrive_path` is not available, use the mounted path and warn
that links will only work within Cowork.

**Verify every link target exists** before adding it to the index. If a file has been moved
or deleted since the scan, flag it rather than linking to a dead path.

---

## STEP 5 — ATTORNEY CHECKLISTS

Generate three courtroom-ready checklists and save them to the case root alongside the
Master Index.

### 5A — Day of Trial Checklist

**File name:** `Day of Trial Checklist — [Client Last Name].docx`

This is the attorney's morning-of-trial reference. It covers logistics, not legal strategy.

Sections:
- **Pre-Court (Morning)**
  - [ ] Trial notebook assembled and reviewed
  - [ ] All exhibits printed/loaded (physical copies + TrialPad if applicable)
  - [ ] Witness subpoenas confirmed — all witnesses notified of time and location
  - [ ] Client meeting scheduled (clothing, demeanor, courtroom conduct review)
  - [ ] Jury questionnaires reviewed (if provided by court in advance)
  - [ ] Defense table supplies (legal pads, pens, water, client notepad)
  - [ ] Technology check (laptop charged, presentation equipment, backup copies)
  - [ ] Co-counsel / investigator coordination confirmed

- **Courtroom Setup**
  - [ ] Arrive early — inspect courtroom layout, identify power outlets, screen placement
  - [ ] Position exhibits for quick access during examination
  - [ ] Confirm court reporter present and spelling of all names
  - [ ] Confirm interpreter arranged (if needed)
  - [ ] Identify gallery seating for defense witnesses / family

- **Pre-Jury**
  - [ ] Review any overnight motions in limine rulings
  - [ ] Confirm voir dire question outline is current
  - [ ] Review strike list and peremptory challenge count
  - [ ] Batson compliance documentation ready

- **During Trial (Daily)**
  - [ ] Contemporaneous objection log open (for appellate preservation)
  - [ ] Note any departures from expected testimony for real-time cross adjustment
  - [ ] Track exhibits admitted vs. offered vs. excluded
  - [ ] End-of-day debrief: update witness order, adjust next day's preparation

### 5B — Exhibit Authentication Checklist

**File name:** `Exhibit Authentication Checklist — [Client Last Name].docx`

Auto-populated from the Evidence Table in `Case Tables.xlsx`.

For each exhibit the defense intends to introduce or anticipates the State will introduce:

| Exhibit # | Description | Authentication Method | Foundation Witness | Stipulated? | Objection Planned? | Status |
|-----------|-------------|----------------------|-------------------|-------------|-------------------|--------|

Authentication method categories:
- Self-authenticating (La. C.E. Art. 902)
- Business record (La. C.E. Art. 803(6))
- Public record (La. C.E. Art. 803(8))
- Testimony of witness with knowledge (La. C.E. Art. 901(B)(1))
- Chain of custody (physical evidence)
- Expert testimony (La. C.E. Art. 702)

Leave the Objection Planned column for attorney completion. Pre-fill the rest from the
Evidence Table where possible.

### 5C — Witness Schedule Worksheet

**File name:** `Witness Schedule — [Client Last Name].docx`

Two sections: Prosecution Witnesses (expected order) and Defense Witnesses (proposed order).

| Order | Witness Name | Role | Estimated Time | Cross Prepared? | Key Issues | Contact Info | Subpoena Status |
|-------|-------------|------|----------------|-----------------|------------|-------------|----------------|

Pre-fill from the Witness List - Priority sheet and the Cross-Examination outlines.
"Cross Prepared?" = Yes if a cross-exam outline exists for that witness in Tab 3.
Leave Contact Info and Subpoena Status for attorney/staff completion.

---

## STEP 6 — UPDATE THE CASE BRAIN

After generating all outputs, update the Case Brain:

1. Add all new deliverables to `COMPANION SKILL OUTPUTS`:
   - Master Trial Index (date, location)
   - Trial Readiness Gap Report (date, readiness score)
   - Day of Trial Checklist (date)
   - Exhibit Authentication Checklist (date)
   - Witness Schedule Worksheet (date)

2. Update `CURRENT STATUS` to reflect the trial readiness assessment.

3. Add to `SESSION LOG`:
   - Trial Notebook Builder ran on [date]
   - Readiness score: [score]
   - [N] critical gaps, [N] non-critical gaps identified
   - [N] total deliverables cataloged across [N] Trial Notebook tabs

4. Update `NEXT STEPS` based on the Gap Report — list the top 3 gaps to close.

---

## STEP 7 — PRESENT RESULTS TO ATTORNEY

Display a summary in this format:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TRIAL NOTEBOOK BUILT: [Client Name] | [Docket #]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Readiness: [READY / NEAR-READY / SIGNIFICANT GAPS / NOT TRIAL-READY]
Trial Date: [Date or NOT SET]

Deliverables Found: [N] across [N] tabs
Critical Gaps: [N] (see Gap Report)
Non-Critical Gaps: [N]

GENERATED FILES:
• Master Trial Index ➜ [file name]
• Trial Readiness Gap Report ➜ [file name]
• Day of Trial Checklist ➜ [file name]
• Exhibit Authentication Checklist ➜ [file name]
• Witness Schedule ➜ [file name]

TOP 3 GAPS TO CLOSE:
1. [Gap] → run [skill trigger phrase]
2. [Gap] → run [skill trigger phrase]
3. [Gap] → run [skill trigger phrase]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

Provide `file://` links (or Cowork `computer://` links) to each generated file.

---

## Guardrails

- **This skill assembles; it does not create.** Never draft a cross-examination, jury
  instruction, motion, or other substantive legal document. If something is missing, tell
  the attorney which skill to run — don't try to fill the gap yourself.
- **Never delete or overwrite existing files.** The Trial Notebook may contain attorney work
  product that was manually placed. Move files only when clearly misplaced, and always ask
  first if ambiguous.
- **Never skip the Case Brain update.** The Case Brain is the living record — every run of
  this skill must be logged.
- **Verify links before including them.** A dead `file://` link in the Master Index is worse
  than no link. Confirm every file exists at the path before linking.
- **Respect the attorney's organization.** If the folder structure deviates from the standard
  but appears intentional (e.g., custom tabs for a complex multi-defendant case), note it
  but don't "fix" it.
- **Phase awareness.** If the case is still in Phase 1, this skill is premature. Warn the
  attorney and suggest running Phase 2 analysis first. If in Phase 2, proceed but expect
  many gaps — the Gap Report becomes the primary deliverable.
- **Always read `references/deliverable-map.md`** before scanning. It contains the complete
  list of upstream deliverables, their expected locations, and the skill that produces each one.

---

## Integration with D&W Skill Ecosystem

This skill sits downstream of every other D&W skill. Here's the routing table for filling gaps:

| Missing Deliverable | Skill to Run | Trigger Phrase |
|---------------------|-------------|----------------|
| Cross-examination outline | `dw-cross-exam-architect` | "build a cross for [witness]" |
| Jury instructions / charges | `dw-jury-instructions-builder` | "draft jury instructions" |
| Verdict form | `dw-jury-instructions-builder` | "build the verdict form" |
| Voir dire materials | `dw-voir-dire-assistant` | "prep voir dire" |
| Suppression motion | `dw-suppression-motion` | "draft motion to suppress" |
| 404(b) opposition | `dw-404b-opposition` | "oppose the 404(b) notice" |
| Bond motion | `dw-bond-and-release-motion` | "draft bond reduction" |
| Brady/Giglio audit | `dw-brady-giglio-auditor` | "run Brady audit" |
| Sentencing package | `dw-sentencing-mitigation-specialist` | "build sentencing mitigation" |
| Plea analysis | `dw-plea-negotiation-analyzer` | "analyze the plea offer" |
| Appellate error log | `dw-appellate-error-monitor` | "start error preservation log" |
| Eyewitness ID audit | `dw-eyewitness-identification-auditor` | "audit the lineup" |
| Expert witness evaluation | `dw-expert-witness-evaluator` | "evaluate the expert" |
| Case analysis reports (1-9) | `dw-criminal-defense` | "run Phase 2" |
| Evidence placeholders | `dw-evidence-placeholder` | "generate evidence placeholders" |
| Phone forensic audit | `dw-mobile-forensic-auditor` | "audit the Cellebrite" |
| Phone content analysis | `dw-forensic-dump-analyzer` | "analyze the phone dump" |
| Video evidence audit | `dw-video-evidence-auditor` | "audit body cam" |
| Discovery compliance | `dw-discovery-compliance-monitor` | "update the discovery ledger" |
| Investigation tasks | `dw-defense-investigator-tasking` | "generate investigator tasks" |
| Habitual offender audit | `dw-habitual-offender-auditor` | "audit the habitual bill" |
| Transcripts (audio/video) | `dw-transcript-router` | "transcribe the evidence" |
| LWOP worksheet | `dw-criminal-defense` (Phase 1 Step 3, Part 2A/2B of `000 - Case Profile.docx`) | "LWOP sheet" |
| Confession/interrogation audit | `dw-confession-interrogation-auditor` | "audit interrogation" |
| Child forensic interview audit | `dw-child-forensic-interview-auditor` | "audit the CAC video" |
| Cell site / CSLI audit | `dw-cell-site-geolocation-auditor` | "audit cell site" |
| Chain of custody audit | `dw-chain-of-custody-auditor` | "audit chain of custody" |
| Crime scene audit | `dw-crime-scene-auditor` | "audit crime scene" |
| Social media audit | `dw-social-media-auditor` | "audit social media" |
| Pretrial motions (various) | `dw-pretrial-motion-library` | "speedy trial motion" or type-specific |

---

## Output Paths

Apply the output-path formula from `dw-shared-protocols/references/output-path-formula.md` (anchored on `{{CASE_ROOT}}`). Trial Notebook Builder is unique in the D&W skill ecosystem because it writes directly into the trial notebook itself — its outputs anchor on `{{CASE_ROOT}}/01 - Trial Notebook/` and the case root.

| Deliverable | Path |
|---|---|
| Master Trial Index | `{{CASE_ROOT}}/MASTER TRIAL INDEX — [Client Last Name] [Date].docx` |
| Trial Readiness Gap Report | `{{CASE_ROOT}}/Trial Readiness Gap Report — [Client Last Name] [Date].docx` |
| Day of Trial Checklist | `{{CASE_ROOT}}/Day of Trial Checklist — [Client Last Name].docx` |
| Exhibit Authentication Checklist | `{{CASE_ROOT}}/Exhibit Authentication Checklist — [Client Last Name].docx` |
| Witness Schedule Worksheet | `{{CASE_ROOT}}/Witness Schedule — [Client Last Name].docx` |
| Folder organization edits | Within `{{CASE_ROOT}}/01 - Trial Notebook/` per the 9-tab structure (Step 1A) |

All five generated documents are internal work product — apply attorney work-product marking per `dw-shared-protocols/references/attorney-work-product-marking.md`. The trial notebook itself contains a mix of filed pleadings (Tabs 6 and 7 — no marking) and internal materials (Tabs 1, 2, 3, 4, 8, 9 — marked); Trial Notebook Builder does not change the marking on existing files, only on the new deliverables it generates.

---

## Changelog

### v1.1 (April 2026)
- **FIX:** Corrected Trial Notebook folder structure to match actual D&W tab layout
  - Tab 2: "Opening Statement" (not "Opening & Closing")
  - Tab 4: "Closing Argument" (not "Exhibit List")
  - Tab 6: "Pleadings" (not "Motions in Limine")
  - Tab 7: "PT Orders_Law" (not "Legal Research")
  - Tab 8: "Verdict_Sentencing" (not "Jury Selection Notes")
- Added recommended subfolder structure for all 9 tabs (Step 3B)
- Reassigned deliverables to correct tabs (verdict forms → Tab 8, motions → Tab 6, etc.)
- Updated deliverable-map.md to match corrected structure

### v1.0 (April 2026)
- Initial skill version
- Folder scan, inventory, gap report, master index with `file://` links
- Attorney checklists: Day of Trial, Exhibit Authentication, Witness Schedule
- Case Brain integration for context loading and update logging
- Full upstream skill routing table for gap remediation

---

*Read `references/deliverable-map.md` for the complete deliverable checklist with expected
locations, producing skills, and criticality ratings.*

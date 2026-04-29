---
name: dw-trial-notebook-builder
description: >
  Assemble the final trial notebook from all upstream deliverables. ALWAYS invoke for
  "build the trial notebook," "assemble trial notebook," "trial notebook," "trial binder,"
  "trial prep package," "ready for trial," "pull together the trial file," "notebook builder,"
  or "what do we have for trial." Scans the case folder and Case Brain for all Phase 2–4
  deliverables, organizes them into the Trial Notebook folder structure, generates a master
  index with file:// links, produces a Trial Readiness Gap Report showing what's missing,
  and includes attorney checklists (Day of Trial, Exhibit Authentication, Witness Schedule).
  The capstone skill that ties every other D&W skill together into a courtroom-ready package.
  Do NOT use for individual deliverables — use the dedicated skill (dw-cross-exam-architect,
  dw-jury-instructions-builder, etc.). Do NOT use for case status checks — use dw-case-dashboard.
---

# D&W Trial Notebook Builder
**Version 1.0 | Internal Use Only**
**Attorney Work Product | Confidential**

You are the **Trial Notebook Builder** — the capstone skill that assembles every upstream D&W deliverable into a single courtroom-ready package. You do not generate new content; you organize, index, and audit what already exists, then produce a Trial Readiness Gap Report identifying what's still missing before trial.

This skill is the endpoint of the 4-phase criminal defense workflow. Everything that `dw-criminal-defense`, the discovery auditors, the motion drafters, `dw-cross-exam-architect`, `dw-jury-instructions-builder`, `dw-voir-dire-assistant`, and the other D&W skills have produced gets pulled together here.

---

## STEP 0.5 — LOAD SHARED PROTOCOLS

Before drafting any deliverable, read `dw-shared-protocols/SKILL.md` and load these references:

1. `dw-shared-protocols/references/attorney-work-product-marking.md` — apply work product marking to all deliverable headers
2. `dw-shared-protocols/references/output-path-formula.md` — use for all output file paths (anchored on `CASE_ROOT`)

Do not proceed to Step 1 until these protocols are loaded. All deliverables from this skill are internal work product — apply marking per the shared protocol. Output paths follow the Cowork Analysis formula: `{{CASE_ROOT}}/01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/`.

**Note:** The scan logic in Steps 2–7 references legacy `Deliverables/Phase-X-*/` paths because this skill indexes upstream deliverables that may live in either the legacy or the Cowork Analysis location. New trial-notebook-build outputs from this skill follow the shared protocol path above.

---

## STEP 1 — Load Case Context and Resolve CASE_ROOT

Before building anything, this skill must know which case it's working on and where the case folder lives.

1. **Confirm active case:**
   - If a `dw-case-brain` session is already loaded, read the client name, docket, phase, and `CASE_ROOT` from the active session.
   - If no session is loaded, prompt: *"Which case are we building the trial notebook for? Client name or docket number works."*
   - Then invoke `dw-case-brain` to load that matter before proceeding.

2. **Resolve `CASE_ROOT`:**
   - Read `CASE_ROOT` from the active Case Brain YAML frontmatter (canonical source)
   - If the Case Brain pre-dates v3.3, fall back to `gdrive_path`
   - If neither is available, ask the attorney for the absolute case folder path

3. **Confirm the trial target:**
   - Ask the attorney to confirm the trial date (or range) if not already in the Case Brain
   - Ask whether this is a "pre-trial dry run" assembly or a "final build" for the actual trial — the Gap Report tolerance differs

4. **Display a BUILD CONFIRMATION** before proceeding:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TRIAL NOTEBOOK BUILD
Case: [Client Name] | [Docket #]
CASE_ROOT: [absolute path]
Trial Date: [date or "TBD"]
Build Type: [Dry Run | Final]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Proceeding with scan...
```

---

## STEP 2 — Scan for Upstream Deliverables

Scan `{CASE_ROOT}/Deliverables/` for every file produced by upstream D&W skills. Build an inventory organized by skill and phase.

### 2A — Scan Targets

| Phase | Folder | What to Look For |
|---|---|---|
| Phase-2-Discovery | `Deliverables/Phase-2-Discovery/*/` | DMARs, audit reports, dump analyses, Brady logs, discovery ledgers |
| Phase-3-Motions | `Deliverables/Phase-3-Motions/*/` | Motions, memoranda, proposed orders, habitual bill challenges |
| Phase-4-Trial | `Deliverables/Phase-4-Trial/*/` | Cross outlines, jury charges, voir dire materials, LWOP sheet |

Also scan the attorney's Google Drive Trial Notebook folder (if it exists) at:
```
{CASE_ROOT}/01 - Trial Notebook/
{CASE_ROOT}/02 - Pretrial Notebook/
```

These are the attorney's working folders — pleadings filed with the court, discovery as produced by the State, and manually-added materials live here. The Trial Notebook Builder indexes these alongside Cowork-generated deliverables.

### 2B — Inventory Format

For each file found, record:
- Skill name (or "attorney manual" if from `01 - Trial Notebook/` or `02 - Pretrial Notebook/`)
- Deliverable type (cross outline, motion, DMAR, etc.)
- Filename and absolute path
- Date produced (from filename `YYYY-MM-DD` prefix or file mtime)
- File size and type

Present a summary count to the attorney before moving on:

```
SCAN COMPLETE — {CASE_ROOT}/Deliverables/
Phase 2 Discovery: [N] files across [M] skills
Phase 3 Motions: [N] files across [M] skills
Phase 4 Trial: [N] files across [M] skills
Attorney manual (01/02 notebooks): [N] files
Total: [N] deliverables indexed
```

---

## STEP 3 — Assemble the Trial Notebook Folder Structure

Build (or update) the trial notebook tree at `{CASE_ROOT}/Deliverables/Phase-4-Trial/dw-trial-notebook-builder/`. This is a curated view — it does NOT move or delete source files. Instead, it produces a master index document and a folder of copies organized for courtroom use.

### 3A — Canonical Trial Notebook Structure

```
{CASE_ROOT}/Deliverables/Phase-4-Trial/dw-trial-notebook-builder/
└── {YYYY-MM-DD}_Trial-Notebook-Build/
    ├── 00_Master-Index.pdf
    ├── 00_Trial-Readiness-Gap-Report.pdf
    ├── 00_Attorney-Checklists.pdf
    ├── 01_Pleadings-and-Orders/
    ├── 02_Discovery-Audits/
    ├── 03_Witness-Materials/
    │   ├── Prosecution-Crosses/
    │   ├── Defense-Witness-Prep/
    │   └── Expert-Evaluations/
    ├── 04_Evidence-and-Exhibits/
    ├── 05_Jury-Selection/
    ├── 06_Jury-Instructions/
    ├── 07_Opening-and-Closing-Seeds/
    ├── 08_Motion-Practice-Binder/
    └── 09_Post-Trial-Ready/
```

The top-level `00_*` files are the three generated outputs (see Steps 4–6). The numbered subfolders organize upstream deliverables for easy courtroom reference.

### 3B — Routing Rules

| Upstream Skill | Trial Notebook Folder |
|---|---|
| `dw-suppression-motion`, `dw-404b-opposition`, `dw-pretrial-motion-library`, `dw-bond-and-release-motion` | `01_Pleadings-and-Orders/` |
| All Phase-2 auditors and DMAR pipelines | `02_Discovery-Audits/` |
| `dw-cross-exam-architect` (prosecution witnesses) | `03_Witness-Materials/Prosecution-Crosses/` |
| `dw-expert-witness-evaluator` | `03_Witness-Materials/Expert-Evaluations/` |
| `dw-defense-investigator-tasking` (witness prep) | `03_Witness-Materials/Defense-Witness-Prep/` |
| `dw-evidence-placeholder`, chain-of-custody, crime scene | `04_Evidence-and-Exhibits/` |
| `dw-voir-dire-assistant` | `05_Jury-Selection/` |
| `dw-jury-instructions-builder` | `06_Jury-Instructions/` |
| Attorney manual opening/closing drafts | `07_Opening-and-Closing-Seeds/` |
| Motion hearing transcripts, rulings | `08_Motion-Practice-Binder/` |
| `dw-sentencing-mitigation-specialist`, `dw-appellate-error-monitor` prep | `09_Post-Trial-Ready/` |

Copy (don't move) each indexed file into the appropriate subfolder. Preserve original filenames.

---

## STEP 4 — Generate the Master Index

The Master Index (`00_Master-Index.pdf`) is the first thing the attorney reaches for in court. It is a single PDF that lists every document in the trial notebook with clickable `file://` links back to the source file.

### 4A — Master Index Structure

1. **Cover page:** Case caption, client name, docket, court, judge, prosecutor, defense counsel, trial date, build date
2. **Table of Contents:** Two-column, each row = one deliverable
3. **Section dividers:** One per numbered subfolder (01–09)
4. **Per-file entries:** Filename, date, producing skill, one-line description, absolute `file://` link

### 4B — Required Columns

| Column | Content |
|---|---|
| # | Sequential entry number |
| Section | e.g., "03 — Witness Materials / Prosecution Crosses" |
| Document | Filename (hyperlinked) |
| Date | YYYY-MM-DD |
| Source | Skill name or "Attorney Manual" |
| Notes | Brief description or "see document" |

### 4C — File Link Format

Use absolute `file://` URIs with URL-encoded paths (same encoding rules as `dw-case-brain` Step 6D):
- Spaces → `%20`
- Commas → `%2C`
- `&` → `%26`

Example:
```
file:///Users/greatelephant82/Library/CloudStorage/.../Deliverables/Phase-4-Trial/dw-cross-exam-architect/2026-04-05_Cross-Det-Johnson.docx
```

Save as `00_Master-Index.pdf` at the root of the trial notebook build folder.

---

## STEP 5 — Generate the Trial Readiness Gap Report

The Gap Report (`00_Trial-Readiness-Gap-Report.pdf`) identifies what SHOULD be in the trial notebook but isn't. It's the attorney's pre-trial panic check.

### 5A — Gap Categories

Audit for missing deliverables across seven categories:

| Category | What to Check For |
|---|---|
| **Cross-Exam Coverage** | Every State witness on the witness list has a cross outline in `03/Prosecution-Crosses/`? |
| **Expert Challenges** | Every State expert has a Daubert/Foret evaluation from `dw-expert-witness-evaluator`? |
| **Motion Rulings** | Every filed motion has a court ruling in `08_Motion-Practice-Binder/`? |
| **Jury Charges** | Proposed jury charges + verdict form exist for every count? |
| **Voir Dire Prep** | Venire-specific questions + strike criteria drafted? |
| **Exhibit Authentication** | Every State exhibit has an authentication plan or foundation objection ready? |
| **Discovery Completeness** | Discovery ledger from `dw-discovery-compliance-monitor` shows zero outstanding items? |
| **Witness Table Completeness** | Master Witness Table (5-column format: Name/Contact, Witness Type, Association/Testimony, Source Documents, Trial Exam Status) is current? Every prosecution witness has a "Trial Exam Prepared" status? Every defense witness has direct exam prep? Witness numbers assigned for trial order? |
| **Legal Arsenal Completeness** | Comprehensive case law reference table exists with all cited statutes, cases, and constitutional provisions with one-sentence utility notes? Generated via Master Trial Advocate Playbook (`dw-criminal-defense` Phase 3 Step 11). |

### 5B — Gap Report Format

For each gap found, produce an entry with:
- **Gap:** What's missing
- **Category:** Which of the seven audit buckets
- **Risk:** Low / Medium / High (based on trial proximity and importance)
- **Recommended skill:** Which D&W skill to run to close the gap
- **Deadline suggestion:** Based on trial date

Example entry:
```
GAP #3
Missing: Cross-exam outline for State witness Det. Marcus Johnson
Category: Cross-Exam Coverage
Risk: HIGH (lead detective, likely State's first witness)
Fix: Run dw-cross-exam-architect with witness = Det. Johnson
Deadline: No later than 7 days before trial
```

### 5C — Summary Dashboard

End the Gap Report with a one-page summary:
```
TRIAL READINESS SUMMARY — [Client Name] | Trial Date: [date]
Total Deliverables Indexed: [N]
Gaps Identified: [N]  (High: [N] | Medium: [N] | Low: [N])
Overall Readiness: [Green | Yellow | Red]
```

**Readiness thresholds:**
- **Green:** Zero high-risk gaps, ≤2 medium-risk gaps
- **Yellow:** 1 high-risk gap, or 3–5 medium-risk gaps
- **Red:** 2+ high-risk gaps, or 6+ medium-risk gaps

Save as `00_Trial-Readiness-Gap-Report.pdf`.

---

## STEP 6 — Generate Attorney Checklists

The Attorney Checklists (`00_Attorney-Checklists.pdf`) are the physical in-the-courtroom reference sheets. They are short, tactile, designed to be pulled out and checked off during trial.

### 6A — Required Checklists (one page each)

**1. Day of Trial Checklist**
- Court time, courtroom, judge section
- Files to bring (trial notebook binder, exhibits, laptop, charging cable, business cards)
- Technology check (courtroom AV, exhibit display, document camera)
- Client pre-trial meeting time and talking points
- Voir dire strike sheet, peremptory tracker
- Opening statement outline
- Witness order confirmed with court/State

**2. Exhibit Authentication Checklist**
- Every exhibit listed with authentication route (custodian, stipulation, self-authenticating)
- Foundation witnesses identified
- Chain of custody documents tabbed
- Objection ready: hearsay, authenticity, relevance, 403

**3. Witness Schedule**
- Prosecution witnesses in expected order with cross outline page references
- Defense witnesses with direct outlines and preparation status
- Expert witness scheduling and Daubert/Foret status
- Standby witness list (subpoenaed but may not be called)

### 6B — Format

- One page per checklist (front/back OK)
- Large-font headers (readable from counsel table)
- Checkboxes for every action item
- Top of each page: Client name, docket, trial date

Save as `00_Attorney-Checklists.pdf`.

---

## STEP 7 — Present the Build to the Attorney

After generating all three top-level outputs and populating all subfolders, present the build summary:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TRIAL NOTEBOOK BUILD COMPLETE
Case: [Client Name] | Trial: [date]
Build folder: {CASE_ROOT}/Deliverables/Phase-4-Trial/dw-trial-notebook-builder/{YYYY-MM-DD}_Trial-Notebook-Build/

Generated:
✅ 00_Master-Index.pdf ([N] entries)
✅ 00_Trial-Readiness-Gap-Report.pdf ([N] gaps | Status: [color])
✅ 00_Attorney-Checklists.pdf (3 checklists)

Organized into 9 sections with [N] total files copied.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
NEXT ACTIONS (Top 3 from Gap Report):
1. [highest-risk gap]
2. [next gap]
3. [next gap]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

Offer to hand off to the skill that would close the top gap:
> *"Ready to close Gap #1 with `[recommended skill]`? Or review the Gap Report first?"*

Also update the active Case Brain via `dw-case-brain`:
- Add entry to `COMPANION SKILL OUTPUTS` section
- Log the build date, gap count, and readiness status
- Append session note: "Trial Notebook built — [N] deliverables indexed, [N] gaps identified."

---

## Guardrails

- **This skill NEVER generates new substantive content.** It only organizes, indexes, and audits what upstream skills have produced. If a deliverable is missing, flag it in the Gap Report — do not draft a substitute.
- **Never move or delete source files.** Copy into the trial notebook build folder; leave originals where they are.
- **Always preserve prior builds.** Each run creates a new dated build folder (`{YYYY-MM-DD}_Trial-Notebook-Build/`). Do not overwrite previous builds — the attorney needs the build history to see progress over time.
- **The Gap Report is the point of this skill.** If the attorney skips the Gap Report, the build is half-finished. Always present the Gap summary up-front in the completion message.
- **Respect attorney manual files.** Files in `{CASE_ROOT}/01 - Trial Notebook/` and `{CASE_ROOT}/02 - Pretrial Notebook/` are attorney-curated. Index them, but do not reorganize them.

---

## Integration with D&W Skill Ecosystem

This is the capstone skill. It depends on every upstream D&W skill's output. The attorney should run this skill:

| When | Why |
|---|---|
| 30 days pre-trial | First gap report to identify major holes |
| 14 days pre-trial | Second pass to verify cross outlines, expert challenges filed |
| 7 days pre-trial | Final gap check and checklist printout |
| Day before trial | Final build — this is what goes into the courtroom |

Each run produces a fresh timestamped build folder, so the attorney can compare builds and see what changed.

---

*This skill reflects Daniels & Washington Trial Notebook Builder Version 1.0 (April 2026). It is the capstone of the D&W 4-phase criminal defense workflow. Update whenever new D&W skills are added to the ecosystem so routing rules stay current.*

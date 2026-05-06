---
name: dw-issue-code-tracker
description: Maintains a living issue-code ledger for any criminal case at Daniels & Washington using the firm's 34-code taxonomy (14 Universal + 9 Homicide + 11 Rape/Sex Assault). ALWAYS invoke for "issue codes," "issue ledger," "issue tracker," "what issues are open," "what's been addressed," "set up issue codes," "initialize the issue ledger," "update the issue tracker," "mark issue as addressed," "issue code status," "what issues apply to this case," "show me the open issues," "issue code report," or "refresh the issue ledger." Initializes a per-case ledger, tracks status (N/A | Open | Addressed) for each applicable code, and produces both an Obsidian narrative section and an Excel sheet view. Does NOT auto-route to specialist skills — the attorney decides when to invoke dw-suppression-motion, dw-eyewitness-identification-auditor, etc. Do NOT use for case status dashboards (use dw-case-dashboard) or session persistence (use dw-case-brain).
---

# DW Issue Code Tracker

**Phase:** 2 (Case Analysis) — also runs in Phase 3 and Phase 4 as a refresh skill
**Capstone Aggregator:** No — feeds into dw-case-dashboard and dw-trial-notebook-builder
**Output Location:** `{CASE_ROOT}/Deliverables/Phase-2-Analysis/Issue-Code-Tracker/{YYYY-MM-DD}_Issue-Ledger.{ext}`

---

## Hard-Stop File Intake Gate

Before doing anything, confirm you have:
1. **CASE_ROOT** path (Obsidian Case Brain location, e.g. `~/Library/Mobile Documents/iCloud~md~obsidian/Documents/Dream Team Law/DW-CASE BRAINS/Cases/{ClientName}`)
2. **Case Tables.xlsx** path (typically `{CASE_ROOT}/Case Tables.xlsx`)
3. **Case type** (Homicide / Rape-Sexual Assault / Other Felony / Multiple)

If any are missing, ask the attorney before proceeding.

---

## Read Before Drafting

Read `../dw-shared-protocols/SKILL.md` for:
- Attorney work product marking
- CASE_ROOT-anchored output path formula
- Louisiana citation conventions

---

## What This Skill Does

Maintains a **living issue-code ledger** per case using the D&W 34-code taxonomy. Three operations:

1. **INITIALIZE** — first run on a case. Creates the ledger in both Obsidian and Case Tables.xlsx with all applicable codes pre-loaded based on case type.
2. **UPDATE** — flip a code's status (N/A → Open → Addressed) as work progresses.
3. **REPORT** — produce a status snapshot showing what's Open, what's Addressed, and what's N/A.

**This skill does NOT:**
- Auto-invoke specialist skills (the attorney decides when to run `dw-suppression-motion`, etc.)
- Replace `dw-case-dashboard` (which shows deliverable status, not issue status)
- Replace `dw-case-brain` (which handles session persistence)

---

## The 34-Code Taxonomy

### Universal — 14 codes (apply to ALL cases)
| Code | Name |
|------|------|
| U-01 | Charges |
| U-02 | Criminal History |
| U-03 | Crime Scene |
| U-04 | Evidence - Physical |
| U-05 | Evidence - Exculpatory |
| U-06 | Evidence - Incriminating |
| U-07 | Witnesses/Credibility |
| U-08 | Eyewitness Identification |
| U-09 | Interrogation/Statements |
| U-10 | Expert Testimony/Forensic |
| U-11 | Timeline/Alibi |
| U-12 | Electronic Communication |
| U-13 | Deficient Investigation |
| U-14 | Search & Seizure / 4th Amendment |

### Homicide — 9 codes (apply if case type = Homicide)
| Code | Name |
|------|------|
| H-01 | Forensic - Ballistics |
| H-02 | Forensic - Blood/DNA |
| H-03 | Forensic - Fingerprints |
| H-04 | Medical Examiner/COD |
| H-05 | CSLI/Geolocation |
| H-06 | Premeditation/Deliberation |
| H-07 | Malice/Intent to Kill |
| H-08 | Felony Murder |
| H-09 | Self-Defense/Justification |

### Rape/Sexual Assault — 11 codes (apply if case type = Rape-Sexual Assault)
| Code | Name |
|------|------|
| R-01 | SANE Examination |
| R-02 | Sexual Assault Kit/DNA |
| R-03 | Consent Defense |
| R-04 | Rape Shield (Art. 412) |
| R-05 | Delayed Disclosure |
| R-06 | Medical Evidence |
| R-07 | Incapacity/Inability to Consent |
| R-08 | Victim Credibility |
| R-09 | Trauma-Informed Interviewing |
| R-10 | Physical Evidence/Scene |
| R-11 | Pattern/Prior Allegations |

Full descriptions in `references/issue-code-taxonomy.md`.

---

## Operation 1: INITIALIZE

**Trigger phrases:** "set up issue codes," "initialize the issue ledger," "issue codes for [client]," "new case — set up the tracker"

**Steps:**

1. **Confirm case type** with attorney:
   - Homicide → load Universal (14) + Homicide (9) = 23 codes
   - Rape/Sexual Assault → load Universal (14) + Rape (11) = 25 codes
   - Other Felony → load Universal (14) only = 14 codes
   - Multiple (e.g., homicide + sex offense) → load all applicable

2. **Set initial status for each code:**
   - Default: `Open`
   - If a code is clearly inapplicable on intake (e.g., no eyewitness ID issue in a paper-fraud case), mark `N/A` with a one-line reason

3. **Write to Obsidian Case Brain.** Append a new section to `{CASE_ROOT}/Case-Brain.md`:
   ```markdown
   ## Issue Code Ledger
   _Last updated: {YYYY-MM-DD}_

   ### Universal Issues
   - **[U-01] Charges** — Open
   - **[U-02] Criminal History** — Open
   - ...

   ### Homicide-Specific Issues
   - **[H-01] Forensic - Ballistics** — Open
   - ...
   ```

4. **Write to Case Tables.xlsx.** Add a new sheet named `Issue Codes` with columns:
   | Code | Category | Issue Name | Status | Last Updated | Notes | Linked Skill |
   |------|----------|------------|--------|--------------|-------|--------------|

   Pre-populate the `Linked Skill` column from `references/skill-routing-map.md` so the attorney can see which D&W skill maps to each code (reference only — no auto-routing).

5. **Save deliverable copy** to:
   `{CASE_ROOT}/Deliverables/Phase-2-Analysis/Issue-Code-Tracker/{YYYY-MM-DD}_Issue-Ledger-Init.docx`

6. **Confirm to attorney:**
   > Issue ledger initialized for [Client Name]. [N] codes loaded ([X] Universal + [Y] case-type-specific). Ledger lives in Obsidian Case Brain and Case Tables.xlsx → Issue Codes sheet.

---

## Operation 2: UPDATE

**Trigger phrases:** "mark [code] as addressed," "update issue [code]," "[code] is N/A," "flip [code] to open"

**Steps:**

1. **Identify the code.** Accept either:
   - Code ID (e.g., "U-08")
   - Issue name (e.g., "eyewitness ID")
   - Fuzzy match if obvious

2. **Confirm the status change** with attorney before writing:
   > Marking [U-08] Eyewitness Identification as Addressed. Add notes? (y/n)

3. **Update both locations atomically:**
   - Obsidian Case Brain: replace the bullet
   - Case Tables.xlsx → Issue Codes sheet: update the row, set `Last Updated` = today

4. **Append to Case Brain audit trail:**
   ```markdown
   ### Issue Ledger Audit Trail
   - {YYYY-MM-DD}: [U-08] Eyewitness ID flipped Open → Addressed (notes: "Cross outline drafted; impeachment hooks identified.")
   ```

---

## Operation 3: REPORT

**Trigger phrases:** "what issues are open," "issue code report," "show me the ledger," "where do we stand on issues," "refresh the issue ledger"

**Steps:**

1. **Read current state** from Case Tables.xlsx → Issue Codes sheet.

2. **Generate three counts:**
   - Open: [N]
   - Addressed: [N]
   - N/A: [N]

3. **Display formatted report:**
   ```
   ISSUE CODE STATUS — [Client Name] — {YYYY-MM-DD}

   OPEN ([N]):
   - [U-03] Crime Scene
   - [U-08] Eyewitness Identification
   - [H-04] Medical Examiner/COD
   ...

   ADDRESSED ([N]):
   - [U-01] Charges (briefed in motion to quash, 2026-04-15)
   - [U-09] Interrogation/Statements (suppression motion filed, 2026-04-22)
   ...

   N/A ([N]):
   - [H-08] Felony Murder (no underlying felony charged)
   ...
   ```

4. **Optionally save a snapshot** to:
   `{CASE_ROOT}/Deliverables/Phase-2-Analysis/Issue-Code-Tracker/{YYYY-MM-DD}_Issue-Status-Report.docx`

---

## Integration Points

- **Reads from:** `dw-case-brain` for CASE_ROOT, `dw-criminal-defense` for case type
- **Writes to:** Obsidian Case Brain (`Case-Brain.md`), Case Tables.xlsx (`Issue Codes` sheet), Deliverables folder
- **Referenced by:** `dw-case-dashboard` (pulls Open count for status display), `dw-trial-notebook-builder` (pulls full ledger for trial readiness check)
- **Does NOT trigger:** Specialist skills. The attorney decides when to invoke `dw-suppression-motion`, `dw-eyewitness-identification-auditor`, etc. The `Linked Skill` column is a reference map only.

---

## Quality Gates

Before completing any operation:
- [ ] CASE_ROOT confirmed
- [ ] Case Tables.xlsx exists or created
- [ ] Obsidian Case Brain updated
- [ ] Excel `Issue Codes` sheet updated
- [ ] Audit trail entry written (for UPDATE operations)
- [ ] Deliverable saved with date-stamped filename
- [ ] Attorney work product marking applied to .docx output

---

## Output Schema

All deliverables follow `dw-data-contracts`:
- Filename: `{YYYY-MM-DD}_Issue-Ledger.docx` or `{YYYY-MM-DD}_Issue-Status-Report.docx`
- Path: `{CASE_ROOT}/Deliverables/Phase-2-Analysis/Issue-Code-Tracker/`
- Format: .docx via the `docx` skill
- Header: ATTORNEY WORK PRODUCT — PRIVILEGED
- Footer: Daniels & Washington, LLC | {Client Name} | {Case Number}

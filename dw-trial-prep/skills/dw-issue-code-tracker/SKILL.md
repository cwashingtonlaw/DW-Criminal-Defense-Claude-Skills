---
name: dw-issue-code-tracker
category: trial-prep
description: Maintains a living issue-code ledger for any criminal case at Daniels & Washington using the firm's 33-code taxonomy v2.0 (14 Universal + 8 Homicide + 11 Rape/Sex Assault). ALWAYS invoke for "issue codes," "issue ledger," "issue tracker," "what issues are open," "what's been addressed," "set up issue codes," "initialize the issue ledger," "update the issue tracker," "mark issue as addressed," "issue code status," "what issues apply to this case," "show me the open issues," "issue code report," or "refresh the issue ledger." Initializes a per-case ledger, tracks status (N/A | Open | Addressed) for each applicable code, and produces both an Obsidian narrative section and an Excel sheet view. Does NOT auto-route to specialist skills — the attorney decides when to invoke dw-suppression-motion, dw-eyewitness-identification-auditor, etc. Do NOT use for case status dashboards (use dw-case-dashboard) or session persistence (use dw-case-brain).
---

# DW Issue Code Tracker

**Version:** 2.0 (33-code taxonomy, renumbered with no gaps)
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

Read `../../../dw-core/skills/dw-shared-protocols/SKILL.md` for:
- Attorney work product marking
- CASE_ROOT-anchored output path formula
- Louisiana citation conventions

---

## What This Skill Does

Maintains a **living issue-code ledger** per case using the D&W 33-code taxonomy v2.0. Three operations:

1. **INITIALIZE** — first run on a case. Creates the ledger in both Obsidian and Case Tables.xlsx with all applicable codes pre-loaded based on case type.
2. **UPDATE** — flip a code's status (N/A → Open → Addressed) as work progresses.
3. **REPORT** — produce a status snapshot showing what's Open, what's Addressed, and what's N/A.

**This skill does NOT:**
- Auto-invoke specialist skills (the attorney decides when to run `dw-suppression-motion`, etc.)
- Replace `dw-case-dashboard` (which shows deliverable status, not issue status)
- Replace `dw-case-brain` (which handles session persistence)

---

## The 33-Code Taxonomy (v2.0)

### Universal — 14 codes (apply to ALL cases)
| Code | Name |
|------|------|
| U-01 | Charges |
| U-02 | Criminal History (Defendant) |
| U-03 | Crime Scene |
| U-04 | Evidence - Physical (Chain & Handling) |
| U-05 | Evidence - Exculpatory (Brady/Giglio) |
| U-06 | Witnesses/Credibility (State Witnesses) |
| U-07 | Eyewitness Identification |
| U-08 | Interrogation/Statements (Defendant) |
| U-09 | Expert Reliability (Daubert/Foret) |
| U-10 | Timeline/Alibi |
| U-11 | Electronic Communication & Digital Evidence |
| U-12 | Deficient Investigation |
| U-13 | Search & Seizure / 4th Amendment |
| U-14 | CSLI/Geolocation Evidence |

### Homicide — 8 codes (apply if case type = Homicide)
| Code | Name |
|------|------|
| H-01 | Forensic - Ballistics |
| H-02 | Forensic - DNA |
| H-03 | Forensic - Fingerprints |
| H-04 | Medical Examiner / Cause of Death |
| H-05 | Specific Intent & Premeditation Indicators |
| H-06 | Verdict Ladder & Lesser-Included Strategy |
| H-07 | Felony Murder |
| H-08 | Self-Defense / Justification |

### Rape/Sexual Assault — 11 codes (apply if case type = Rape-Sexual Assault)
| Code | Name |
|------|------|
| R-01 | SANE Examination |
| R-02 | Sexual Assault Kit / DNA |
| R-03 | Consent Defense |
| R-04 | Rape Shield (Art. 412) |
| R-05 | Delayed Disclosure |
| R-06 | Medical Evidence |
| R-07 | Incapacity / Inability to Consent |
| R-08 | Victim Credibility |
| R-09 | Child Forensic Interviewing |
| R-10 | Physical Evidence / Scene (Sex Offense) |
| R-11 | Prior False Allegations (Art. 608) |

Full descriptions in `references/issue-code-taxonomy.md`.

---

## Operation 1: INITIALIZE

**Trigger phrases:** "set up issue codes," "initialize the issue ledger," "issue codes for [client]," "new case — set up the tracker"

**Steps:**

1. **Confirm case type** with attorney:
   - Homicide → load Universal (14) + Homicide (8) = 22 codes
   - Rape/Sexual Assault → load Universal (14) + Rape (11) = 25 codes
   - Other Felony → load Universal (14) only = 14 codes
   - Multiple (e.g., homicide + sex offense) → load all applicable, up to 33 codes

2. **Set initial status for each code:**
   - Default: `Open`
   - If a code is clearly inapplicable on intake (e.g., no eyewitness ID issue in a paper-fraud case), mark `N/A` with a one-line reason

3. **Write to Obsidian Case Brain.** Append a new section to `{CASE_ROOT}/Case-Brain.md` per the template in `references/obsidian-ledger-template.md`.

4. **Write to Case Tables.xlsx.** Add a new sheet named `Issue Codes` per the schema in `references/excel-sheet-schema.md`.

5. **Save deliverable copy** to:
   `{CASE_ROOT}/Deliverables/Phase-2-Analysis/Issue-Code-Tracker/{YYYY-MM-DD}_Issue-Ledger-Init.docx`

6. **Confirm to attorney:**
   > Issue ledger initialized for [Client Name]. [N] codes loaded ([X] Universal + [Y] case-type-specific). Ledger lives in Obsidian Case Brain and Case Tables.xlsx → Issue Codes sheet.

---

## Operation 2: UPDATE

**Trigger phrases:** "mark [code] as addressed," "update issue [code]," "[code] is N/A," "flip [code] to open"

**Steps:**

1. **Identify the code.** Accept either:
   - Code ID (e.g., "U-07")
   - Issue name (e.g., "eyewitness ID")
   - Fuzzy match if obvious

2. **Confirm the status change** with attorney before writing:
   > Marking [U-07] Eyewitness Identification as Addressed. Add notes? (y/n)

3. **Update both locations atomically:**
   - Obsidian Case Brain: replace the bullet
   - Case Tables.xlsx → Issue Codes sheet: update the row, set `Last Updated` = today

4. **Append to Case Brain audit trail:**
   ```markdown
   ### Issue Ledger Audit Trail
   - {YYYY-MM-DD}: [U-07] Eyewitness ID flipped Open → Addressed (notes: "Cross outline drafted; impeachment hooks identified.")
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
   - [U-07] Eyewitness Identification
   - [H-04] Medical Examiner / Cause of Death
   ...

   ADDRESSED ([N]):
   - [U-01] Charges (briefed in motion to quash, 2026-04-15)
   - [U-08] Interrogation/Statements (suppression motion filed, 2026-04-22)
   ...

   N/A ([N]):
   - [H-07] Felony Murder (no underlying felony charged)
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

---

## Version History

- **v2.0 (2026-05-06):** Renumbered taxonomy with no gaps. 33 active codes. Former U-06 retired (Evidence-Incriminating, deleted as inventory-not-issue). Former H-05 promoted to U-14 (CSLI/Geolocation, applies across case types). All cross-references updated. Refined descriptions throughout with statutory anchors, "Addressed" definitions, attack-surface enumerations, and N/A guidance.
- **v1.0 (initial):** 34-code taxonomy (14 Universal + 9 Homicide + 11 Rape).

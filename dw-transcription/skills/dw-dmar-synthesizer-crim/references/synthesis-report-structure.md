# Cross-Case DMAR Synthesis Report — Structure

Read at Step 3 (Attorney Confirmation) for the synthesis preview prompt and at Step 4 (Generate the Synthesis Report) of `dw-dmar-synthesizer-crim` for the full report skeleton, inconsistency-matrix columns, and appendices — all moved verbatim from SKILL.md.

## Step 3 — Cross-Case Synthesis Preview (attorney confirmation prompt)

> **Cross-Case Synthesis Preview**
>
> DMARs Analyzed: [N]
> Clients: [List]
>
> Findings Summary:
> - XW (Witness Inconsistencies): [count] ([critical count] critical)
> - XO (Officer Audit): [count] ([critical count] critical)
> - XT (Timeline Conflicts): [count]
> - XB (Brady/Giglio Alerts): [count]
> - XS (Severance Indicators): [count]
>
> Top 3 Strongest Findings:
> 1. [Brief description of highest-impact finding]
> 2. [Brief description]
> 3. [Brief description]
>
> *Ready to generate the full Cross-Case DMAR Synthesis Report. Confirm or ask me to dig deeper into any area.*

## Step 4 — Report Structure
```
CROSS-CASE DMAR SYNTHESIS REPORT
Cases: [Client A] | [Client B] | [Client C if applicable]
Dockets: [List all docket numbers]
Parish(es): [List]
Analysis Date: [Date]
Source DMARs: [List each DMAR filename and date]
Prepared by: Claude AI — Attorney Work Product / Privileged

SECTION 1: CASE REGISTRY & ENTITY CROSSWALK
  1.1 Case Registry (table from Step 1.2 — one row per DMAR)
  1.2 Shared Entity Crosswalk (table from Step 1.3)
  1.3 Synthesis Scope (what was compared and what was excluded)

SECTION 2: INCONSISTENCY MATRIX
  Master table summarizing ALL cross-case findings:

  | ID | Type | Severity | Witness/Officer | Cases | Brief Description | Defense Use |
  |----|------|----------|----------------|-------|-------------------|-------------|
  | XW-001 | Witness | CRITICAL | John Smith | A, B | Contradicts himself on weapon | Impeachment |
  | XO-001 | Officer | SIGNIFICANT | Det. Jones | A, B, C | Miranda timing differs | Suppression |
  | ... | ... | ... | ... | ... | ... | ... |

SECTION 3: WITNESS STATEMENT CROSS-CASE COMPARISON
  All XW-### findings from Module S1, organized by witness
  Each witness gets a subsection with all their inconsistencies grouped together
SECTION 4: OFFICER CONSISTENCY AUDIT
  All XO-### findings from Module S2, organized by officer
  Each officer gets a subsection

SECTION 5: UNIFIED SUPER-TIMELINE
  Merged timeline from Module S3
  Timeline conflicts (XT-### findings) highlighted inline with color-coded flags

SECTION 6: BRADY/GIGLIO CROSS-POLLINATION
  All XB-### findings from Module S4
  Organized by benefiting client (so each attorney can see what may be missing from their discovery)

SECTION 7: SEVERANCE ANALYSIS
  All XS-### findings from Module S5
  Summary assessment: Is severance motion warranted? (Strong / Possible / Weak)

SECTION 8: DEFENSE INTELLIGENCE BRIEF
  8.1 Strongest Cross-Case Findings (top 10 ranked by trial impact)
  8.2 Per-Client Action Items:
      For [Client A]:
        - [Specific next steps, motions, cross-exam targets]
      For [Client B]:
        - [Specific next steps]
  8.3 Recommended Skill Invocations:
      - "Run dw-cross-exam-architect-crim for [officer] using XO findings"
      - "Run dw-brady-giglio-auditor-crim on [client]'s discovery with XB alerts"
      - "Run dw-suppression-motion-crim for [Miranda issue from XO findings]"
      - "Run dw-pretrial-motion-library-crim for severance motion using XS findings"
  8.4 Outstanding Questions (gaps the synthesis could not resolve)
APPENDIX A: FINDING ID REFERENCE
  Complete legend of all finding ID prefixes:
  - XW-### = Cross-case Witness inconsistency
  - XO-### = Cross-case Officer audit finding
  - XT-### = Cross-case Timeline conflict
  - XB-### = Cross-case Brady/Giglio alert
  - XS-### = Severance indicator
  (Plus inherited single-case prefixes: CR, RR, ME, IT, KE)

APPENDIX B: SOURCE DMAR INVENTORY
  For each source DMAR: filename, SHA-256 hash, date produced, client, docket

APPENDIX C: METHODOLOGY
  Statement that cross-case synthesis was performed by Claude AI on previously
  generated DMAR documents. Attorney verification required before any filing,
  client communication, or disclosure to co-counsel.
  Louisiana Act 250 / ABA Opinion 512 compliance note.
  Note: sharing this report with co-defendant counsel requires client consent
  and may waive privilege — consult before distributing.
```

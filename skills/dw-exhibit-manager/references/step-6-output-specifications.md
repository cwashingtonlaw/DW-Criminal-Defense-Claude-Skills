# Step 6 — Output Specifications

All outputs saved to: `<case-root>/03 - Trial Notebook/01 - Exhibit List/`

## 6A. Master Exhibit List (.xlsx)

File name: `[ClientLastName] - Master Exhibit List - [TrialDate].xlsx`

Spreadsheet with full exhibit tracker. Columns:
- Exhibit #
- Description
- Type
- Source
- Bate Number
- Authentication Method
- Authenticating Witness
- Foundation Elements
- Anticipated Objections
- Response to Objections
- Offered During
- Pre-Trial Status
- Trial Status (actual ruling)

Separate sheets:
- Defense Exhibits (D-1, D-2, etc.)
- State Exhibits (S-1, S-2, etc.)
- Joint Exhibits (J-1, J-2, etc.)
- Excluded Exhibits (all exhibits ruled inadmissible)

## 6B. Clerk's Exhibit List (.docx)

File name: `[ClientLastName] - Clerk Exhibit List - [TrialDate].docx`

Formatted document for filing with clerk of court (post-trial). Columns:
- Exhibit #
- Description
- Party Offering
- Date Offered
- Court's Ruling (Admitted / Excluded)
- Ruling Language (if applicable)

Include cover letter with case name, docket number, trial judge, trial date.

## 6C. Objection Log (.xlsx)

File name: `[ClientLastName] - Objection Log - [TrialDate].xlsx`

Complete record of all evidentiary objections for appellate preservation. Columns:
- #
- Exhibit / Statement
- Party Offering
- Objecting Party
- Objection Basis
- Court's Ruling (Sustained / Overruled)
- Limiting Instruction (if any)
- Appeal Flag (YES / NO)
- Judge Name
- Trial Date
- Notes

Filter for "Appeal Flag: YES" to generate the list for dw-appellate-error-monitor.

## 6D. Authentication Checklist (.docx)

File name: `[ClientLastName] - Authentication Checklist - [TrialDate].docx`

Per-exhibit authentication requirements for attorney use at counsel table during trial. Format:

```
EXHIBIT D-1: [Brief Description]
Authenticating Witness: [Name, title]
Foundation Elements:
  1. Who created / obtained / observed?
  2. When?
  3. Where?
  4. How was it handled since creation?
  5. Chain of custody breaks?

Key Foundation Questions:
  Q: [Foundation question 1]
  Q: [Foundation question 2]
  [etc.]

Anticipated Objections & Responses:
  Objection: Hearsay
  Response: Not offered for truth; or falls under [exception], La. C.E. Art. [###]
  
  Objection: Authentication
  Response: [witness name] will testify he/she [foundation]
```

Use dw-cross-exam-architect output to identify cross-examination vulnerabilities.

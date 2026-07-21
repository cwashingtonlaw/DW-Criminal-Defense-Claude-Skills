# Case Analysis Prompts for Criminal Defense
**Daniels & Washington — 8 Report Prompt Templates**

These are the exact prompts used to generate the 8 Case Analysis Reports in Phase 2 Step 2. Each prompt is designed to be run against the full case discovery. All prompts share a common analytical framework and source-citation standard.

Note: The former "Report 8 — Witness Table" has been removed because witness data is built during Phase 1 Step 4 and stored in the Witness List sheets of `Case Tables.xlsx`. The former Report 9 (Key Witness Impeachment Plan) is now Report 8.

## Table of Contents
1. [Report 1: Comprehensive Case Timeline](#report-1-comprehensive-case-timeline)
2. [Report 2: Prosecution's Case Summary](#report-2-prosecutions-case-summary)
3. [Report 3: Immediate Red Flags](#report-3-immediate-red-flags)
4. [Report 4: Competing Defense Theories](#report-4-competing-defense-theories)
4a. [Report 4a: Theory Selection Memo](#report-4a-theory-selection-memo)
5. [Report 5: Viable Legal Defenses](#report-5-viable-legal-defenses)
6. [Report 6: Memorable Theme](#report-6-memorable-theme)
7. [Report 7: Table of Missing Discovery](#report-7-table-of-missing-discovery)
8. [Report 8: Key Witness Impeachment Plan](#report-8-key-witness-impeachment-plan)

---

## Common Instructions

All 8 reports share these requirements:

**Analytical Framework:** Draw on the logical precision of Clarence Darrow, the narrative skill of Gerry Spence, the civil liberties analysis of Alan Dershowitz, the strategic mind of F. Lee Bailey, the thoroughness of Roy Black, the practical wisdom of Robert Shapiro, the meticulousness of Barry Scheck, and Johnnie Cochran's ability to connect with people and catch-phrase cadence.

**Source Citation Standard:** Every factual claim must include:
- **Source Document(s)**: The specific document(s) where this information was found. Be precise: cite the document title, page number, and paragraph or timestamp (e.g., "Officer Smith BWC, Timestamp 00:15:32" or "Witness Statement of Jane Doe, p. 2, para. 4"). If multiple documents confirm an event, list all of them.

**Defendant Identification:** The defendant is our client. Replace `__________` with the client's name from the Case Profile.

---

## Report 1: Comprehensive Case Timeline

**Role:** You are an AI paralegal and legal analyst.

**Objective:** Process all provided source documents from this criminal case file and generate a comprehensive, chronological timeline of all relevant events. The purpose is to assist a criminal defense attorney in understanding the case narrative, identifying factual inconsistencies, pinpointing potential constitutional violations, and preparing for trial.

**Source Documents to Analyze:** All uploaded documents, which may include but are not limited to:
- Initial Incident Reports & Supplemental Police Reports
- Arrest Warrants and Affidavits
- Search Warrants and Affidavits (including returns and inventories)
- Transcripts of 911 calls and Dispatch Logs
- Transcripts of Body-Worn Camera (BWC) and Dash-Cam footage
- Witness, Victim, and Informant Statements (written and transcribed)
- Defendant Interrogation Transcripts and Recordings
- Evidence Logs and Chain of Custody Documents
- Forensic and Laboratory Reports (e.g., DNA, ballistics, fingerprint, toxicology, digital forensics)
- Medical Examiner's Report / Autopsy Report
- Photographs and Crime Scene Logs
- Jail Call Transcripts and Visitor Logs
- Court Filings (Indictment, Motions, etc.)

**Detailed Instructions:**

1. **Strict Chronological Order:** Organize from the earliest event to the latest. Use the most precise date and time available. Note approximations as such (e.g., "approx." or time range).

2. **Required Data Points for Each Entry:**
   - **Date and Time**: Format: YYYY-MM-DD HH:MM:SS
   - **Title:** Maximum 64 characters
   - **Subtitle:** Maximum 128 characters
   - **Event Description**: Neutral, factual, concise summary. Avoid legal conclusions or speculation.
   - **Source Document(s)**: Per the citation standard above.
   - **Location**: Physical or digital location (e.g., "123 Maple St, Living Room" or "Defendant's iPhone")
   - **Parties Involved**: All individuals by name and role (e.g., "Defendant (John Doe)", "Victim (Jane Smith)", "Officer (Sgt. Miller)")
   - **Evidence**: Physical, digital, or testimonial evidence collected or mentioned (e.g., "Seizure of .45 caliber handgun (Item #E-001)")
   - **Key Quote**: Single critical verbatim quote with source citation, if available.
   - **Analyst Flag**: Tags to draw attorney attention:
     - [INCONSISTENCY] — conflicting accounts of the same event
     - [4TH AMENDMENT] — searches, seizures, traffic stops
     - [5TH/6TH AMENDMENT] — interrogations, Miranda warnings, requests for counsel
     - [CHAIN OF CUSTODY] — evidence handling issues
     - [BRADY MATERIAL] — potentially exculpatory or impeachment evidence
     - [ELEMENT OF OFFENSE] — event proves or disproves an element of the charged crime

**Output Requirements:**
1. Present the final timeline as a structured list with clear headings for each data point.
2. After the full timeline, include two summary sections:
   - **Key Inconsistencies**: Bulleted list of the most significant conflicts and contradictions, referencing specific timeline entries by date and time.
   - **Timeline Gaps**: Bulleted list of significant unaccounted-for periods for the defendant, victim, or key witnesses.

**Constraints:**
- Do not infer or assume information not explicitly stated in source documents.
- Maintain strictly neutral and objective tone. No legal opinions, strategies, or conclusions regarding guilt or innocence.
- Sole function is to organize and present facts as recorded in provided files.

**Output destination:** `Case Tables.xlsx — Timeline Sheet`

---

## Report 2: Prosecution's Case Summary

Synthesizing all sourced documents (police reports, witness statements, etc.), applying the common analytical framework, generate a concise assessment structured as follows:

- Detail the prosecution's likely theory, the elements of the alleged crime(s) in this jurisdiction, their key evidence, and a timeline of key events.

**Output destination:** `01 - Trial Notebook/09 - Case Analysis/`

---

## Report 3: Immediate Red Flags

Synthesizing all sourced documents, applying the common analytical framework, generate:

- Identify the most significant weaknesses, inconsistencies, or gaps in the prosecution's case. Flag any obvious constitutional issues (e.g., search, seizure, interrogation) that require immediate attention.

**Priority:** HIGH — Route constitutional issues to **dw-suppression-motion-crim**. Route expert issues to **dw-expert-witness-evaluator-crim**.

**Output destination:** `01 - Trial Notebook/09 - Case Analysis/`

---

## Report 4: Competing Defense Theories

Synthesizing all sourced documents and Report 2a (Theory Deconstruction) if available, applying the common analytical framework, generate:

- Identify and develop **all viable competing defense theories** — not just the single strongest narrative. For each theory:
  1. **Theory name** — a short label (e.g., "Misidentification," "Self-Defense," "Coerced Confession," "Insufficient Evidence")
  2. **Theory summary** — 2-3 paragraph narrative of the defense story under this theory
  3. **Supporting evidence** — specific evidence (with Bate stamps) that supports this theory
  4. **Weaknesses** — evidence or facts that undermine this theory (from Report 2a Assumption Audit if available)
  5. **Prosecution counter-arguments** — how the state would attack this theory
  6. **Viability assessment** — STRONG / MODERATE / WEAK with reasoning
  7. **Compatible defenses** — which Report 5 legal defenses align with this theory

- After presenting all theories, provide a **Comparative Matrix** summarizing: Theory | Key Strength | Key Weakness | Viability | Compatible With

**Why competing theories instead of a single narrative:** Premature commitment to a single defense narrative creates confirmation bias — the defense team stops looking at evidence that doesn't fit. By presenting multiple theories, the attorney can make an informed strategic choice and the team remains open to pivoting as new evidence arrives.

**Prerequisite:** Report 2 (Prosecution's Case Summary) must be complete. Report 2a (Theory Deconstruction from `dw-theory-deconstructor-crim`) should be complete if available — the Alternative Inference Table from Report 2a directly feeds competing theory development.

**Downstream:** The attorney selects a theory from this report → Report 4a (Theory Selection Memo) documents the choice → `dw-adversarial-stress-test-crim` and `dw-theory-to-workplan-crim` consume the selection.

**Output destination:** `01 - Trial Notebook/09 - Case Analysis/`

---

## Report 4a: Theory Selection Memo

*This report is attorney-driven — Cowork prepares the template, but the attorney makes the selection.*

After the attorney reviews Report 4 (Competing Defense Theories), draft a **Theory Selection Memo** documenting:

1. **Selected Theory** — which theory the attorney chose from Report 4
2. **Selection Rationale** — why this theory was selected over alternatives (attorney provides; Cowork documents)
3. **Key Evidence Supporting Selected Theory** — the top 5-10 pieces of evidence (with Bate stamps) that anchor the theory
4. **Key Vulnerabilities** — the top 3-5 weaknesses that must be addressed (from Report 4 and Report 2a)
5. **Critical Assumptions** — assumptions that must hold for this theory to succeed (from Report 2a MODULE D)
6. **Pivot Triggers** — specific events or evidence that would require reconsidering the selected theory (e.g., "if BWC contradicts alibi witness," "if DNA results come back positive")
7. **Abandoned Theories** — theories from Report 4 that were not selected and why (preserves the reasoning for the record)

**Attorney sign-off required.** The Theory Selection Memo must be confirmed by the attorney before downstream skills consume it. Mark `[AWAITING ATTORNEY SIGN-OFF]` until confirmed.

**Downstream routing:**
- `dw-adversarial-stress-test-crim` — stress-tests the selected theory
- `dw-theory-to-workplan-crim` — generates a 7-stream action plan from the selected theory

**Output destination:** `01 - Trial Notebook/09 - Case Analysis/`

---

## Report 5: Viable Legal Defenses

Synthesizing all sourced documents, applying the common analytical framework, generate:

- List the most viable legal defenses (e.g., alibi, self-defense, misidentification) that align with the core narrative.

**Skill routing:** Route prior bad acts issues to **dw-404b-opposition-crim**. Route sentencing exposure to **dw-sentencing-mitigation-specialist-crim**. Route habitual offender claims to **dw-habitual-offender-auditor-crim**.

**Output destination:** `01 - Trial Notebook/09 - Case Analysis/`

---

## Report 6: Memorable Theme

Synthesizing all sourced documents, applying the common analytical framework, generate:

- Develop a concise, memorable theme that encapsulates the defense narrative (e.g., "Wrong place, wrong time," "A rushed investigation, not a real one").

**Output destination:** `01 - Trial Notebook/09 - Case Analysis/`

---

## Report 7: Table of Missing Discovery

Synthesizing all sourced documents, applying the common analytical framework, generate:

- Prioritize a list of missing items (e.g., body-cam footage, dispatch logs, lab notes) crucial for the defense.

**Priority:** HIGH — Auto-Action. Immediately triggers Missing Discovery Demand Letter (Phase 2 Step 3). Route to **dw-brady-giglio-auditor-crim**.

**Output destination:** `01 - Trial Notebook/09 - Case Analysis/`

---

## Report 8: Key Witness Impeachment Plan

Applying the common analytical framework, conduct a comprehensive audit of all evidence in the sourced documents focused on the top 10 prosecution witnesses:

- Identify inconsistencies in their statements
- Identify potential credibility issues (bias, motive)
- Outline a preliminary cross-examination strategy for each

**Priority:** HIGH — Auto-Action. Immediately triggers Impeachment Worksheet generation (Phase 2 Step 4, triggered by Report 8). Route to **dw-cross-exam-architect-crim**.

**Output destination:** `01 - Trial Notebook/09 - Case Analysis/`

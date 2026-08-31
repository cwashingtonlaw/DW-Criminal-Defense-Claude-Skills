# Phase 2 Step 1 — Rapid Triage & Specialist Routing (Detailed)

Read from SKILL.md **Phase 2 Step 1 / Step 1E** — the Triage Routing Memo flags, Chain of Custody Audit, the complete 1C evidence-type and 1D charge-type specialist dispatch lists, and the Barone pre-analysis sequencing.

Before the 8 Case Analysis Reports are generated, scan all case documents to produce two deliverables: a **Triage Routing Memo** and early **specialist skill dispatches**. The purpose of this step is speed — get routing decisions to specialist skills fast so they can begin working in parallel while the full reports are being written. This step flags and routes; the reports (Step 2) analyze in depth.

**1A — Triage Routing Memo**
Quickly scan all discovery documents and produce a short routing memo that identifies which documents need specialist attention. The memo is a working document for Cowork's internal use — not a deliverable to the attorney. It contains routing decisions, not analysis.

For each flag below, list the specific documents (by name and Bate stamp) and the routing destination. Do not write analysis — just identify and route:
- **Constitutional flags:** documents suggesting 4th, 5th, or 6th Amendment concerns → route to **dw-suppression-motion-crim** *(Report 3 will provide the full analysis)*
- **Brady/Giglio flags:** material potentially favorable to the defense that may not have been disclosed → route to **dw-brady-giglio-auditor-crim** *(Report 7 will provide the full table)*
- **Witness inconsistency flags:** witnesses who appear in multiple documents with conflicting accounts → flag for **Report 8** *(Report 8 will provide the full impeachment plan)*
- **Timeline conflict flags:** events with conflicting dates, times, or sequences across documents → flag for **Report 1** *(Report 1 will build the authoritative timeline)*

**1B — Chain of Custody Audit**
This is substantive analysis, not triage — no report covers this domain. Verify that each piece of physical evidence has an unbroken custody log from collection to present. Flag any gaps, undocumented transfers, or missing logs. Route findings to **dw-chain-of-custody-auditor-crim**.

**1C — Specialist Evidence Routing**
Classify evidence by type and dispatch to the appropriate specialist skill for early analysis. Specialist skills can begin their work in parallel while the 8 reports are being generated in Step 2.

- Eyewitness identification issues → **dw-eyewitness-identification-auditor-crim**
- Confession/interrogation issues → **dw-confession-interrogation-auditor-crim**
- Cell phone forensics → **dw-mobile-forensic-auditor-crim** then **dw-forensic-dump-analyzer-crim**
- Video evidence analysis → **dw-video-evidence-auditor-crim**
- Cell site/location data → **dw-cell-site-geolocation-auditor-crim**
- Social media evidence → **dw-social-media-auditor-crim**
- Child forensic interviews → **dw-child-forensic-interview-auditor-crim**
- Expert witness issues → **dw-expert-witness-evaluator-crim** (Module I for Daubert/Foret hearing day package once a hearing is set)
- Jail call recordings (Securus / GTL/ViaPath / NCIC / IC Solutions) → **dw-jail-call-analyzer-crim** (transcribes via dw-transcript-router-crim; cross-feeds dw-witness-threat-matrix-crim and dw-cross-exam-architect-crim)

**1D — Charge-Type Specialist Routing**
Identify the charge category and dispatch to the corresponding charge-type specialist for element-by-element defense framework, sentencing exposure analysis, and discipline-specific motions/discovery. Specialists run in parallel with the 8 reports.

- Drug offenses (CDS, distribution, possession with intent) → **dw-drug-offense-specialist-crim**
- DWI / OWI / vehicular homicide → **dw-dwi-specialist-crim**
- Sex offenses (incl. SANE-exam audit) → **dw-sex-offense-specialist-crim**
- Firearms offenses (state and federal) → **dw-firearms-specialist-crim**
- Violent crimes (homicide, manslaughter, agg battery, agg assault, armed robbery, kidnapping, home invasion) → **dw-violent-crime-specialist-crim**

Cases involving multiple specialist domains (e.g., armed robbery with felon-in-possession enhancement) should dispatch to all applicable specialists.

Save all Step 1 outputs to: `01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/` subfolder.

### Step 1E — Barone Discovery Workflow Pre-Analysis (New — v5.9)
Before generating the 8 Case Analysis Reports, run the Barone Discovery Workflow pre-analysis skills:

1. **Report 0 — Neutral Inventory** → invoke **dw-neutral-inventory-crim** to catalog all discovery neutrally before any strategic lens is applied. This establishes the complete evidence baseline.
2. **Report 2a — Theory Deconstruction** → invoke **dw-theory-deconstructor-crim** after Report 2 is generated. Decomposes the prosecution's theory into facts, inferences, and assumptions. Feeds Report 4 (Competing Theories).

These pre-analysis steps run after the Triage Routing (Step 1A-1D) but before the 8 Reports (Step 2).

---
name: dw-discovery-compliance-monitor-crim
category: discovery
description: >
  Living discovery ledger tracking demanded vs. produced items. ALWAYS invoke for "discovery
  log," "update the ledger," "what hasn't been produced," "missing discovery," or "late
  disclosure." Do NOT use for Brady/Giglio analysis — use dw-brady-giglio-auditor-crim.
---

# Discovery Compliance Monitor
**Daniels & Washington | Criminal Defense | Louisiana / 5th Circuit**

Systematic tracker of prosecution disclosure obligations. Maintains a living ledger of what has been demanded, what has been produced, what is outstanding, and what may have been suppressed. This tool converts discovery obligations from abstract constitutional duties into concrete, auditable tasks.

### Source Citation Mandate

Every ledger entry must trace back to a specific source document. When the defense argues that discovery is missing or late, the court will ask: where was this demanded, and what was or wasn't produced? Precise sourcing in the ledger turns a vague complaint into a documented compliance failure.

**Citation format:** Cite the document title, page number, and paragraph or item number. Examples:
- `(Defense Discovery Demand, 03/01/2026, Item #14)`
- `(State's Discovery Response, 03/15/2026, p. 3, Item #14 — "N/A")`
- `(Supplemental Discovery Production, 04/01/2026, Bates #00345-00360)`
- `(Court Order Compelling Discovery, 03/20/2026, para. 3)`
- `(State's 701 Motion Response, p. 2, para. 4)`
- `(Minute Entry, 03/22/2026 — State represents all discovery produced)`

**Multiple-source rule:** When documenting a gap, cite both the demand and the production (or lack thereof) — e.g., `(Demand Item #14; State's Response — "N/A"; no supplemental production as of 04/05/2026)`.

**Unsourced assertions:** If a discovery gap cannot be documented with specific demand-and-response citations, mark it `[UNSOURCED — VERIFY WITH CASE FILE]`.

**Where sourcing applies:** Every ledger entry — demands, productions, gaps, late disclosures, and compliance status updates. Legal authority citations follow normal citation format.

---

## STEP 0 — FILE INTAKE HARD STOP

**DO NOT PROCEED with analysis until all discovery materials are uploaded.**

Before beginning any discovery audit:

1. **Receive explicit instruction:** "I have uploaded all discovery in Case [CLIENT/CASE NUMBER]"
2. **Confirm file receipt:**
   - All demand letters (initial and supplemental) present
   - All discovery production received to date present
   - Any prior discovery motions/orders present
   - Charging documents present
   - Court orders present
3. **Verify completeness:** Ask "Are there additional discovery files to upload, or shall I proceed with audit?"
4. **Once confirmed:** Proceed to STEP 1

This prevents incomplete analysis and ensures no critical files are overlooked.

---

## STEP 0.5 — LOAD SHARED PROTOCOLS

Before drafting any deliverable, read `dw-shared-protocols-crim/SKILL.md` and load these references:

1. `dw-shared-protocols-crim/references/attorney-work-product-marking.md` — apply work product marking to all deliverable headers
2. `dw-shared-protocols-crim/references/output-path-formula.md` — use for all output file paths (anchored on `CASE_ROOT`)

Do not proceed to Step 1 until these protocols are loaded. All deliverables from this skill are internal work product — apply marking per the shared protocol. Output paths follow the Cowork Analysis formula: `{{CASE_ROOT}}/01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/`.

---

## STEP 1 — Information Gathering Protocol

All information must be extracted from uploaded documents or explicitly provided by user. Ranked by criticality:

### ESSENTIAL (Case-Critical)

- **Charges:** Specific counts with Louisiana Revised Statutes cites (e.g., La. R.S. 14:109 for manslaughter)
- **Discovery demands filed:**
  - Initial demand (date, scope)
  - All supplemental demands (dates, specific items)
  - Standing Brady/Giglio orders (if any)
- **Discovery produced to date:**
  - Dates of productions
  - General categories of items
  - Any productions marked "incomplete" or "under review"
- **Charging document:** Bill of Information or Indictment with count descriptions
- **Arraignment date:** Current status
- **All court dates:** Pretrial conferences, status hearings, discovery deadlines, trial date

### STRATEGIC (Case-Development)

- **Defense theory:** What the defense intends to prove; how discovery relates
- **Witness list:** Prosecution and defense witnesses (to assess discovery sufficiency)
- **Expert list:** Any retained or prosecution experts (triggers discovery of underlying data, reports, CVs, prior opinions)
- **Co-defendant status:** Joint trial, severed, guilty plea, cooperation (affects discovery obligations)
- **Plea offers:** Any formal offers (to assess discovery's impact on evaluation)

### CONTEXTUAL (Enhancement)

- **Case chronology:** Arrest → charges → arraignment → discovery
- **Attorney notes:** Flag any items the defense attorney suspects are missing
- **Prior discovery motions/orders:** What has been ruled, what discovery was compelled, what was denied

---

## STEP 2 — Louisiana Discovery Framework

Louisiana criminal discovery is governed by La. C.Cr.P. Articles 716-729.5, with a constitutional overlay from Brady, Giglio, Kyles, and their progeny. Before drafting any demand, motion, or ledger entry, ground the analysis in the controlling statutes and case law.

**Reference:** Read `references/louisiana-discovery-framework.md` for the full text of each statutory disclosure obligation (Arts. 716-725, 729.3, 729.5), the corresponding remedies for non-compliance, and the constitutional overlay (Brady, Giglio, Kyles, Strickler, Smith v. Cain, State v. Knapper, Connick).

Key points to remember in orchestration:
- **10-day rule (Art. 723):** All discovery must be produced no later than 10 days before trial (with Jencks/protective-order/informant exceptions).
- **Continuing duty (Art. 722):** Late-discovered material must be disclosed when found; failure can be a Brady violation.
- **Sanctions ladder (Art. 729.3):** Continuance → exclusion → mistrial → contempt → adverse inference. See severity table for application.

---

## MODULE A — Discovery Demand Generator

This module generates comprehensive, tiered discovery demands covering all material the prosecution must produce under Louisiana law and Constitution. The initial demand is filed at case inception; supplemental demands address gaps in the State's response.

**Reference:** Read `references/discovery-demand-templates.md` for:
- The full **Initial Discovery Demand Template** (Parts I-XVI: defendant statements, co-defendant statements, documents/tangibles, scientific tests, witness statements, informant identity, Brady/Giglio, BWC/dash, communications, GPS/location, financial, officer records, agency policies, grand jury, plea agreements, prior convictions)
- The **Supplemental Demand trigger list** (8 conditions that auto-trigger a supplemental filing)
- The **Supplemental Demand Template** (Parts I-V: items not produced, items incomplete, expert underlying data, items referenced but not produced, Brady/Giglio reminder)
- Production-deadline language

When a new case is intaked, generate the initial demand from the template; after each State production, run the supplemental-demand triggers against the production tracker (Module B) and generate a supplemental demand if any trigger fires.

---

## MODULE B — Discovery Production Tracker (Core Module)

The operational heart of the compliance monitor: a living ledger of every demanded item, its production status, days outstanding, and notes. Status values are RECEIVED, OUTSTANDING, PARTIALLY PRODUCED, LATE, NEVER PRODUCED, DISPUTED, UNDER REVIEW.

### Discovery Bucket Classification (Barone 7-Bucket System)

Every ledger entry must be classified into one of the seven Barone Discovery Buckets. This classification enables gap analysis by category — revealing whether entire categories of discovery are missing (e.g., "we have zero digital evidence disclosures") rather than just individual items.

| Bucket # | Bucket Name | What It Covers |
|----------|-------------|----------------|
| 1 | Law Enforcement Reports & Statements | Incident reports, supplemental reports, arrest reports, officer statements, internal affairs records, use-of-force reports, training records |
| 2 | Physical/Forensic Evidence | Lab reports (DNA, fingerprint, ballistics, toxicology), crime scene photos, autopsy/medical examiner reports, chain of custody logs, evidence inventories |
| 3 | Digital/Electronic Evidence | BWC footage, dash cam, CCTV/surveillance, cell phone extractions, CSLI data, social media records, computer forensics, GPS/location data |
| 4 | Witness Statements & Information | Civilian witness statements, victim statements, informant information, 911 call recordings/transcripts, grand jury testimony |
| 5 | Expert Reports & Analysis | Expert CVs, expert reports, underlying data/bench notes, testing protocols, proficiency testing results, lab accreditation records |
| 6 | Prosecution Case File | Plea offers, correspondence, internal memos (if discoverable), prior consistent/inconsistent statements of prosecution witnesses, co-defendant statements, cooperation agreements |
| 7 | Exculpatory/Impeachment Material (Brady/Giglio) | Exculpatory evidence, impeachment evidence, witness criminal histories, officer discipline records, prior inconsistent statements, benefits/deals given to witnesses |

**Bucket completeness metric:** For each bucket, track: items demanded, items received, items outstanding, and a completeness percentage. A bucket at 0% is a red flag — it likely means the demand was insufficient or the State is withholding an entire category. Cross-reference with `dw-neutral-inventory-crim` Report 0 to verify expected evidence types are accounted for.

**Reference:** Read `references/production-tracker-and-prioritization.md` for:
- The full **Discovery Production Tracker** schema (15-row example with all columns: Item #, Category, Description, Discovery Bucket, Demanded Date, Produced Date, Status, Days Outstanding, Notes)
- The **Status Legend** (definitions for each status value)
- **Automated Flags** (30/60/90-day outstanding escalation language)
- **Compliance Metrics** calculation and interpretation thresholds (95%/75%/50%/<50%)
- The **Prioritized Missing Items Report** format (CRITICAL/HIGH/MEDIUM/LOW priority ranking with source citation and deadline urgency)

The Prioritized Missing Items Report feeds directly into **dw-criminal-defense-crim** Phase 2 Report 7 (Table of Missing Discovery) and triggers the Auto-Action Missing Discovery Demand Letter. Route CRITICAL items immediately to **dw-brady-giglio-auditor-crim**.

---

## MODULE C — Brady/Giglio Compliance Ledger (Critical Module)

A separate, parallel ledger specifically tracking exculpatory and impeachment material. Operates independently from the general discovery tracker because Brady/Giglio material may be withheld intentionally or inadvertently, scattered across agencies' files, subject to constructive knowledge under *Kyles*, and cumulative in materiality.

**Reference:** Read `references/brady-giglio-ledger.md` for:
- The **Brady/Giglio Compliance Ledger** schema (10-row example with columns: Type, Why Favorable, Demanded?, Produced?, Materiality Assessment, Missing?, Action Required)
- The **three-pronged materiality test** (favorable / material / suppressed)
- The **Constructive Knowledge (Kyles)** doctrine
- The **Cumulative Materiality (Kyles)** doctrine
- The **Impeachment vs. Exculpatory** distinction

For deeper Brady/Giglio analysis beyond ledger maintenance, hand off to **dw-brady-giglio-auditor-crim**.

---

## MODULE D — Late Disclosure Impact Assessment

When discovery is produced after the statutory 10-day deadline (La. C.Cr.P. Art. 723), run a structured six-step protocol to document the lateness, assess prejudice, decide whether continuance is needed, evaluate exclusion under Art. 729.3, generate a sanctions motion, and track the running pattern of late disclosures.

**Reference:** Read `references/late-disclosure-protocol.md` for:
- **Step 1 — Documenting** the late disclosure (item, demanded date, deadline, actually produced, days late, type)
- **Step 2 — Prejudice assessment** (9 prejudice factors and 4 materiality levels)
- **Step 3 — Continuance need** (5 factors and 4 presumptions)
- **Step 4 — Art. 729.3 exclusion analysis** (4 elements and 5 factors)
- **Step 5 — Sanctions motion generation** (cross-reference to Module F templates)
- **Step 6 — Pattern tracking** (3-tier escalation)

---

## MODULE E — Supplemental Discovery Demand Generator

After reviewing initial production, auto-generate supplemental demands based on gaps, inconsistencies, and new information surfaced by the production tracker (Module B).

**Reference:** The 8 supplemental-demand triggers and full supplemental-demand template are in `references/discovery-demand-templates.md` (same file as the initial demand). Run the triggers against the production tracker after every State production; if any trigger fires, draft a supplemental demand from the template and route to attorney for review and signature.

---

## MODULE F — Discovery Motion Practice

Templates and frameworks for discovery-related motions under Louisiana law, ranging from a routine Motion to Compel up to extraordinary remedies (motion to dismiss, writ application).

**Reference:** Read `references/discovery-motion-templates.md` for full templates of:
- **Motion to Compel Discovery** (Art. 723 basis)
- **Motion for Sanctions for Discovery Violations** (Art. 729.3, sanction hierarchy)
- **Motion for Brady/Giglio Standing Order** (continuing-disclosure order language)
- **Motion to Exclude Late-Disclosed Evidence** (Art. 729.3 exclusion remedy)
- **Motion for Continuance Due to Late Discovery**
- **Motion for In Camera Inspection** (protective-order disputes)
- **Motion to Dismiss for Discovery Violations** (extreme cases)
- **Writ Application for Discovery Disputes** (supervisory court process)

Each template includes the legal standard, elements of the motion, and template language ready to populate with case-specific facts.

---

## MODULE G — Open File Policy Audit

Many Louisiana DA offices claim "open file discovery." This module audits whether the "open file" claim is truthful and complete using a 7-question checklist plus a verification matrix that compares "open file" contents against statutory disclosure requirements.

**Reference:** Read `references/open-file-policy-audit.md` for:
- The **7-question Open File Audit Checklist** (policy existence, scope definition, physical access, exclusions, statutory comparison, completeness, Brady/Giglio inclusion)
- The **statutory comparison table** (Arts. 716-721 + Brady/Giglio against actual open-file contents)
- The **Open File Audit Summary Report** template

If open file is deficient, supplement with targeted demands for missing categories.

---

## MODULE H — Severity Classification

Classify discovery deficiencies by severity (CRITICAL / SIGNIFICANT / MINOR) to prioritize responses. Severity drives the urgency and choice of remedy: critical violations get immediate motions and possible writ practice; significant violations get supplemental demands and sanctions motions; minor violations get tracker notes and explanation requests.

**Reference:** The full severity-classification tables (CRITICAL, SIGNIFICANT, MINOR — each with violation type, definition, example, and response) are in `references/severity-and-quick-reference.md`.

---

## MODULE I — Report Template

Generate a professional written report summarizing the discovery compliance audit. This is the primary deliverable to the attorney; it consolidates outputs from Modules B, C, D, G, and H.

### **DISCOVERY COMPLIANCE REPORT — [Case Name/Client] / Case No. [___]**

**Prepared by:** [Defense Attorney/Firm]

**Date:** [Today's Date]

**Case Information:**

| Field | Information |
|-------|-------------|
| **Defendant(s)** | [Names] |
| **Charges** | [List counts with statutory cites] |
| **Case Number** | [Court/Case No.] |
| **Charging District** | [District, Parish] |
| **Trial Date** | [Date] |
| **Prosecutor(s)** | [Names] |

---

### **EXECUTIVE SUMMARY**

[1-2 paragraphs summarizing overall discovery compliance status, key findings, and recommended actions]

---

### **DISCOVERY DEMAND AND PRODUCTION SUMMARY**

| Metric | Status |
|--------|--------|
| **Initial Demand Filed** | [Date] |
| **Supplemental Demand(s) Filed** | [Dates, if any] |
| **Total Items Demanded** | [Number] |
| **Items Received Timely** | [Number] ([%]) |
| **Items Outstanding** | [Number] ([%]) |
| **Items Produced Late** | [Number] with average delay [X] days |
| **Overall Compliance** | [%] |

---

### **PRODUCTION TRACKER**

[Insert full production tracker from Module B]

---

### **BRADY/GIGLIO ANALYSIS**

[Insert Brady/Giglio ledger from Module C]

**Specific Brady/Giglio Concerns:**
- [Item 1]
- [Item 2]

---

### **LATE DISCLOSURE IMPACT ANALYSIS**

[For each late item, include analysis from Module D]

---

### **OPEN FILE POLICY AUDIT**

[Include audit findings from Module G]

---

### **SEVERITY CLASSIFICATION**

| Category | Items | Risk Level |
|----------|-------|-----------|
| **Critical** | [List] | HIGH |
| **Significant** | [List] | MEDIUM |
| **Minor** | [List] | LOW |

---

### **RECOMMENDED ACTIONS**

1. **Immediate (Within 48 hours):**
   - [Specific action]
   - [Specific action]

2. **Short-term (This week):**
   - [File supplemental demand]
   - [File motion to compel]

3. **Medium-term (Before trial):**
   - [Expert review]
   - [Investigation of gaps]

4. **Pre-trial Conference:**
   - [Raise discovery issues]
   - [Request ruling on Brady/Giglio material]

---

### **MOTIONS RECOMMENDED**

- [ ] Motion to Compel Discovery (Items: [List])
- [ ] Motion for Sanctions (Basis: [Describe])
- [ ] Motion for Continuance Due to Late Discovery (Timeline: [X] days)
- [ ] Motion for Brady/Giglio Standing Order
- [ ] Motion to Exclude Late-Disclosed Evidence (Items: [List])
- [ ] Writ Application (If: [Condition])

---

### **CROSS-EXAMINATION SEEDS**

For use in preparing witnesses for deposition or trial. See Module J below.

---

### **INTEGRATION NOTES**

- [ ] Evidence table in Case Tables.xlsx updated
- [ ] Pretrial Notebook/02-Discovery folder populated
- [ ] Cross-exam architect skill alerted to key witnesses
- [ ] Gaps flagged for ongoing investigation

---

## MODULE J — Cross-Examination Chapter Seeds

For use in **dw-cross-exam-architect-crim** or trial preparation. Three seeded cross chapters target the witnesses most likely to have knowledge of discovery compliance failures: the lead investigator (discovery withholding), the evidence custodian / records clerk (production timeline and completeness), and the prosecutor (Brady/Giglio obligations).

**Reference:** Read `references/cross-exam-seeds.md` for the full question outlines (5 questions with follow-ups for each of the 3 witness types).

---

## MODULE K — Quick Reference Tables

Compact lookup tables for use during live triage and motion-drafting.

**Reference:** Read `references/severity-and-quick-reference.md` for:
- **Louisiana Discovery Articles Matrix** (Arts. 716-725 — topic, what, deadline, penalty)
- **Brady/Giglio Elements Checklist** (5-element assessment matrix)
- **Sanctions Comparison Table** (5 sanctions, severity, applicability, procedure)
- **Discovery Timeline Calculator**
- **Brady/Giglio Standing Order — Recommended Language** (open-court request)

---

## Guardrails

**Maintain objectivity and professionalism:**

- Track discovery status objectively; don't assume bad faith without evidence
- Distinguish between inadvertent omissions and willful suppression
- Document everything with dates, deadlines, and specific items
- Maintain professional tone in all motions and communications
- Remember: Discovery obligations are constitutional mandates, not favors

**Avoid:**
- Accusatory language without evidentiary support
- Assumption of bad faith by DA
- Failure to follow procedural requirements (notice, briefing, local rules)
- Missed deadlines for discovery motions
- Failure to preserve record for appeal

---

## Integration Points

This skill integrates with other Daniels & Washington tools:

- **Master Evidence Table** (Case Tables.xlsx) — updated with all discovered items
- **Pretrial Notebook** — 02-Discovery folder populated with all demand letters, correspondence, and production summaries
- **dw-cross-exam-architect-crim** — seeded with discovery gaps and credibility issues for detective and prosecutor cross-examination
- **dw-criminal-defense-crim** (Phase 4) — informs trial strategy around late disclosures and Brady issues
- **dw-expert-witness-evaluator-crim** — validates that all underlying data for expert opinions has been produced
- **dw-brady-giglio-auditor-crim** — receives CRITICAL Brady/Giglio items for deeper analysis

---

## Quick References

Reference files in `references/` (load on demand):

- `louisiana-discovery-framework.md` — La. C.Cr.P. Arts. 716-729.5 + Brady/Giglio/Kyles constitutional overlay
- `discovery-demand-templates.md` — Initial 16-part demand template, supplemental-demand triggers, supplemental-demand template
- `production-tracker-and-prioritization.md` — Production tracker schema, status legend, automated flags, compliance metrics, Prioritized Missing Items Report format
- `brady-giglio-ledger.md` — Parallel Brady/Giglio ledger schema, three-pronged materiality test, Kyles constructive-knowledge and cumulative-materiality doctrines
- `late-disclosure-protocol.md` — Six-step late-disclosure assessment (document, prejudice, continuance, exclusion, sanctions motion, pattern)
- `discovery-motion-templates.md` — Eight motion templates (compel, sanctions, Brady/Giglio standing order, exclude late evidence, continuance, in camera, dismiss, writ application)
- `open-file-policy-audit.md` — 7-question open-file audit checklist + statutory comparison matrix + audit summary report
- `severity-and-quick-reference.md` — CRITICAL/SIGNIFICANT/MINOR severity classification + Louisiana discovery articles matrix + Brady/Giglio elements checklist + sanctions comparison + timeline calculator + standing-order open-court language

---

*This skill is maintained by Daniels & Washington and should be updated as Louisiana criminal procedure rules change or new case law develops.*

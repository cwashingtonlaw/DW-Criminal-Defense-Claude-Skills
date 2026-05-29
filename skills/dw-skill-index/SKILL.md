---
name: dw-skill-index
category: core
description: >
  Find the right D&W skill for any task. ALWAYS invoke for "what skills do we have,"
  "which skill handles X," "show me the skills," "skill list," "what can Cowork do,"
  "help me find the right tool," or any question about which D&W skill to use for a
  specific task. Returns a searchable routing table of all D&W skills with trigger
  phrases and use cases.
---

# D&W Skill Index — Find the Right Skill

When the attorney asks which skill to use, or wants to know what's available, present the relevant section of this routing table. Don't dump the entire table unless asked — match the attorney's question to the right category and show that section.

---

## STEP 0.5 — LOAD SHARED PROTOCOLS

Before drafting any deliverable, read `dw-shared-protocols/SKILL.md` and load these references:

1. `dw-shared-protocols/references/attorney-work-product-marking.md` — apply work product marking to all deliverable headers
2. `dw-shared-protocols/references/output-path-formula.md` — use for all output file paths (anchored on `CASE_ROOT`)

Do not proceed to Step 1 until these protocols are loaded. Note: this is a reference/index skill with no file output — no output path applies.

---

<!-- BEGIN AUTOGEN: routing-tables (regen-skill-index.py) -->

## Quick Lookup — "I need to..."

| I need to... | Use this skill | Say this |
|---|---|---|
| Run a client intake / first meeting | `dw-client-intake-interview` | "intake" or "new client meeting" |
| Start a new case | `dw-criminal-defense` | "new case" or "case intake" |
| Load an existing case | `dw-case-brain` | "load the case" or "open the matter" |
| Check case status | `dw-case-dashboard` | "where do we stand" or "case status" |
| Process discovery | `dw-criminal-defense` | "run Phase 1" |
| Analyze the case | `dw-criminal-defense` | "run Phase 2" |
| Build trial prep | `dw-criminal-defense` | "run Phase 3" |
| Support trial day (live, in-court) | `dw-trial-day-assistant` | "trial day" or "log this objection" |
| Assemble trial notebook | `dw-trial-notebook-builder` | "build the trial notebook" |
| Triage new discovery | `dw-discovery-orchestrator` | "new discovery arrived" |
| Transcribe recordings | `dw-transcript-router` | "transcribe the evidence" |
| Compare transcripts across cases | `dw-dmar-synthesizer` | "compare the DMARs" |
| Neutral discovery inventory (pre-strategic) | `dw-neutral-inventory` | "neutral inventory" or "catalog the evidence" |
| Deconstruct prosecution's theory | `dw-theory-deconstructor` | "deconstruct the theory" or "facts vs inferences" |
| Stress-test the defense theory | `dw-adversarial-stress-test` | "stress test" or "red team the theory" |
| Generate a workplan from theory | `dw-theory-to-workplan` | "build a workplan" or "theory to workplan" |

---

## Barone Discovery Workflow — "Run the Barone workflow..."

The Barone Discovery Workflow is a structured 9-step analytical pipeline that extends the standard Phase 2 analysis. It emphasizes theory-neutral initial assessment, structured theory development, and adversarial testing before committing to a defense strategy.

| Step | Report / Skill | Trigger Phrase |
|------|---------------|----------------|
| 1 | Report 0 — Neutral Inventory | `dw-neutral-inventory` | "neutral inventory" or "Report 0" |
| 2 | Report 1 — Timeline (with Certainty) | `dw-timeline-builder` | "build the timeline" |
| 3 | Report 2 — Prosecution's Case Summary | `dw-criminal-defense` Phase 2 | "run Phase 2" |
| 4 | Report 2a — Theory Deconstruction | `dw-theory-deconstructor` | "deconstruct the theory" |
| 5 | Report 3 — Red Flags | `dw-criminal-defense` Phase 2 | (auto-generated) |
| 6 | Report 4 — Competing Defense Theories | `dw-criminal-defense` Phase 2 | (auto-generated) |
| 7 | Report 4a — Theory Selection Memo | `dw-criminal-defense` Phase 2 Step 2A | (attorney-driven) |
| 8 | Theory-to-Workplan (7 streams) | `dw-theory-to-workplan` | "build a workplan" |
| 9 | Adversarial Stress Test | `dw-adversarial-stress-test` | "stress test the theory" |

The Barone workflow also adds:
- **Certainty column** to the Timeline Sheet (CONFIRMED / PROBABLE / DISPUTED / UNCONFIRMED / ALLEGED)
- **Discovery Bucket classification** (7 Barone buckets) to the Discovery Compliance Ledger
- **Report-vs-Recording Matrix** (6-category) to all DMARs
- **Verification Protocol** ([VERIFIED] / [UNVERIFIED] flags) across all analytical skills

---

## Evidence Auditing — "Audit the..."

| Evidence Type | Skill | Trigger Phrase |
|---|---|---|
| Phone extraction (HOW it was done) | `dw-mobile-forensic-auditor` | "audit the Cellebrite" |
| Phone contents (WHAT's on it) | `dw-forensic-dump-analyzer` | "analyze the phone dump" |
| Body cam / dash cam / CCTV | `dw-video-evidence-auditor` | "audit body cam" |
| Crime scene processing | `dw-crime-scene-auditor` | "audit crime scene" |
| Evidence chain of custody | `dw-chain-of-custody-auditor` | "audit chain of custody" |
| Cell tower / GPS / location | `dw-cell-site-geolocation-auditor` | "audit cell site" |
| Social media screenshots/DMs | `dw-social-media-auditor` | "audit Facebook" or "social media" |
| Photo array / lineup | `dw-eyewitness-identification-auditor` | "audit the lineup" |
| Deleted phone data / SQLite | `dw-sqlite-recovery` | "recover deleted messages" |
| Adult interrogation / confession | `dw-confession-interrogation-auditor` | "audit interrogation" |
| Child forensic interview (CAC) | `dw-child-forensic-interview-auditor` | "audit the CAC video" |
| Expert witness qualifications | `dw-expert-witness-evaluator` | "evaluate the expert" |
| DNA / forensic biology (STR, mixtures, STRmix, TrueAllele, IGG, mtDNA, Y-STR, touch DNA) | `dw-dna-forensic-biology-auditor` | "DNA audit" or "audit the DNA" |
| Crime lab (drug ID, toxicology, blood alcohol, certificate challenges) | `dw-crime-lab-auditor` | "audit the crime lab" or "criminalist certificate" |
| Daubert/Foret hearing day package | `dw-expert-witness-evaluator` (Module I) | "Daubert hearing prep" or "Foret hearing" |
| Jail calls (recordings, logs, transcripts) | `dw-jail-call-analyzer` | "audit jail calls" or "Securus/GTL/ViaPath" |

---

## Motions & Pleadings — "Draft a..."

| Motion Type | Skill | Trigger Phrase |
|---|---|---|
| Suppress evidence (4th/5th Amend.) | `dw-suppression-motion` | "motion to suppress" |
| Oppose 404(b) / other crimes | `dw-404b-opposition` | "oppose the 404(b)" |
| Reduce bond / pretrial release | `dw-bond-and-release-motion` | "bond reduction" |
| Speedy trial | `dw-pretrial-motion-library` | "speedy trial motion" |
| Bill of particulars | `dw-pretrial-motion-library` | "bill of particulars" |
| Motion to compel discovery | `dw-pretrial-motion-library` | "motion to compel" |
| Severance / change of venue | `dw-pretrial-motion-library` | "severance" or "change of venue" |
| Reveal the deal | `dw-pretrial-motion-library` | "reveal the deal" |
| Recusal | `dw-pretrial-motion-library` | "recusal" |
| Continuance | `dw-pretrial-motion-library` | "continuance" |

All motion skills use the template selection protocol in `dw-shared-protocols/references/` to search DEVONthink for firm templates before drafting.

---

## Trial Preparation — "Prep for trial..."

| Task | Skill | Trigger Phrase |
|---|---|---|
| Cross-examination outlines (state witnesses) | `dw-cross-exam-architect` | "build a cross for [witness]" |
| Direct-examination outlines (defense witnesses) | `dw-direct-exam-architect` | "build a direct for [witness]" or "defendant testimony prep" |
| Opening statement + closing argument (paired) | `dw-trial-narrative-builder` | "draft opening" / "draft closing" / "trial narrative" |
| Jury instructions / charges | `dw-jury-instructions-builder` | "draft jury instructions" |
| Jury selection / voir dire | `dw-voir-dire-assistant` | "prep voir dire" |
| Track errors for appeal | `dw-appellate-error-monitor` | "preserve error" or "log error" |
| Real-time trial-day logging (objections, witnesses, exhibits, jurors) | `dw-trial-day-assistant` | "log this objection" or "today's witness" |
| Generate investigator tasks | `dw-defense-investigator-tasking` | "investigator assignment" |
| Track discovery compliance | `dw-discovery-compliance-monitor` | "update the discovery ledger" |
| Brady/Giglio audit | `dw-brady-giglio-auditor` | "run Brady audit" |

---

## Sentencing, Appeal & Post-Conviction — "After trial..."

| Task | Skill | Trigger Phrase |
|---|---|---|
| Sentencing mitigation package | `dw-sentencing-mitigation-specialist` | "build sentencing mitigation" |
| Habitual offender bill audit | `dw-habitual-offender-auditor` | "audit the habitual bill" |
| Evaluate plea offer | `dw-plea-negotiation-analyzer` | "analyze the plea offer" |
| Draft direct-appeal brief (assignments of error, argument, reply) | `dw-appellate-brief-builder` | "appellate brief" or "appeal brief" or "assignments of error" |
| Post-conviction relief (PCR / habeas / sentence modification) | `dw-post-conviction-relief` | "post-conviction" or "PCR" or "habeas" |

---

## Charge-Type Specialists — "What's the framework for [charge]..."

Each specialist provides charge-specific elements, defenses, sentencing exposure, motions, and discovery checklists. Routed to from `dw-criminal-defense` Phase 2 or directly when the charge type is known.

| Charge Type | Skill | Trigger Phrase |
|---|---|---|
| Drug offenses (CDS, distribution, possession with intent) | `dw-drug-offense-specialist` | "drug case" or "CDS" |
| DWI / OWI / vehicular homicide | `dw-dwi-specialist` | "DWI" or "DUI" |
| Sex offenses (incl. SANE exam audits) | `dw-sex-offense-specialist` | "sex offense" or "SANE" |
| Firearms offenses (state and federal) | `dw-firearms-specialist` | "firearm charge" or "felon in possession" |
| Violent crime (murder, manslaughter, agg battery, armed robbery, kidnapping, home invasion) | `dw-violent-crime-specialist` | "murder" or "manslaughter" or "armed robbery" or "agg battery" or "self-defense" |

---

## Intake & Setup — "Set up..."

| Task | Skill | Trigger Phrase |
|---|---|---|
| Client intake interview (first meeting, conflict check, immediate-action triage) | `dw-client-intake-interview` | "intake" or "new client" or "first meeting" |
| Evidence folder placeholders | `dw-evidence-placeholder` | "evidence placeholders" |
| Medical chronology (PI) | `medical-chronology` | "medical chronology" or "med chron" |

*Note: `dw-lwop-populator` was retired in v5.3 — its functionality merged into `dw-criminal-defense` Phase 1 Step 3.*

---

## Shared References (Not Direct-Trigger)

These skills are read by other skills as reference protocols — you don't invoke them directly:

| Skill | What It Does | Read By |
|---|---|---|
| `dw-data-contracts` | Output schema definitions | All skills producing deliverables |
| `dw-case-brain` | Session persistence (also direct-trigger) | Every skill at session open/close |

<!-- END AUTOGEN: routing-tables (regen-skill-index.py) -->

---

## Can't Find What You Need?

If none of the above matches:
1. **General criminal defense work** → Start with `dw-criminal-defense` — it routes to specialists
2. **New discovery just arrived** → Start with `dw-discovery-orchestrator` — it triages to auditors
3. **Not sure what phase we're in** → Start with `dw-case-dashboard` — it tells you where you are
4. **Something entirely new** → Use `skill-creator` to build a new skill

---

*D&W Skill Index v1.2 — May 2026*

*v1.2 changes (Barone Discovery Workflow Audit): added `dw-neutral-inventory` (Report 0), `dw-theory-deconstructor` (Report 2a), `dw-theory-to-workplan` (7-stream workplan), `dw-adversarial-stress-test` (prosecutor red-team); new "Barone Discovery Workflow" section documenting the 9-step analytical pipeline; updated Quick Lookup with 4 new rows; `dw-criminal-defense` Report 4 renamed from "Core Defense Narrative" to "Competing Defense Theories" with new Report 4a (Theory Selection Memo); Timeline Sheet enhanced with Certainty column; Discovery Compliance Ledger enhanced with 7-bucket classification; DMAR enhanced with Report-vs-Recording Matrix (6-category); new shared protocol `verification-protocol.md`.*

*v1.1 changes: added `dw-client-intake-interview`, `dw-jail-call-analyzer`, `dw-trial-day-assistant`, `dw-appellate-brief-builder`, `dw-violent-crime-specialist`; new "Charge-Type Specialists" section consolidating all five specialists; renamed "Sentencing & Post-Conviction" to "Sentencing, Appeal & Post-Conviction"; surfaced Daubert/Foret hearing day package (Module I) inside `dw-expert-witness-evaluator`; removed retired `dw-lwop-populator` row.*

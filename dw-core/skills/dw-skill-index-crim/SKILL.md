---
name: dw-skill-index-crim
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

Before drafting any deliverable, read `dw-shared-protocols-crim/SKILL.md` and load these references:

1. `dw-shared-protocols-crim/references/attorney-work-product-marking.md` — apply work product marking to all deliverable headers
2. `dw-shared-protocols-crim/references/output-path-formula.md` — use for all output file paths (anchored on `CASE_ROOT`)

Do not proceed to Step 1 until these protocols are loaded. Note: this is a reference/index skill with no file output — no output path applies.

---

<!-- BEGIN AUTOGEN: routing-tables (regen-skill-index.py) -->

## Quick Lookup — "I need to..."

| I need to... | Use this skill | Say this |
|---|---|---|
| Run a client intake / first meeting | `dw-intake-discovery:dw-client-intake-interview-crim` | "intake" or "new client meeting" |
| Start a new case | `dw-core:dw-criminal-defense-crim` | "new case" or "case intake" |
| Load an existing case | `dw-core:dw-case-brain-crim` | "load the case" or "open the matter" |
| Check case status | `dw-core:dw-case-dashboard-crim` | "where do we stand" or "case status" |
| Process discovery | `dw-core:dw-criminal-defense-crim` | "run Phase 1" |
| Analyze the case | `dw-core:dw-criminal-defense-crim` | "run Phase 2" |
| Build trial prep | `dw-core:dw-criminal-defense-crim` | "run Phase 3" |
| Support trial day (live, in-court) | `dw-trial-prep:dw-trial-day-assistant-crim` | "trial day" or "log this objection" |
| Assemble trial notebook | `dw-trial-prep:dw-trial-notebook-builder-crim` | "build the trial notebook" |
| Triage new discovery | `dw-intake-discovery:dw-discovery-orchestrator-crim` | "new discovery arrived" |
| Transcribe recordings | `dw-transcription:dw-transcript-router-crim` | "transcribe the evidence" |
| Transcribe locally (on-device, diarized, court-reporter format) | `dw-transcription:dw-local-transcription-crim` | "transcribe locally" |
| Compare transcripts across cases | `dw-transcription:dw-dmar-synthesizer-crim` | "compare the DMARs" |
| Neutral discovery inventory (pre-strategic) | `dw-trial-prep:dw-neutral-inventory-crim` | "neutral inventory" or "catalog the evidence" |
| Deconstruct prosecution's theory | `dw-trial-prep:dw-theory-deconstructor-crim` | "deconstruct the theory" or "facts vs inferences" |
| Stress-test the defense theory | `dw-trial-prep:dw-adversarial-stress-test-crim` | "stress test" or "red team the theory" |
| Generate a workplan from theory | `dw-trial-prep:dw-theory-to-workplan-crim` | "build a workplan" or "theory to workplan" |
| Track issue codes (living issue-code ledger) | `dw-trial-prep:dw-issue-code-tracker-crim` | "issue codes" or "issue tracker" |
| Compute statutory clocks (institution, trial commencement, Art. 701, appeal, PCR) | `dw-core:dw-deadline-engine-crim` | "compute the clocks" or "deadline check" or "speedy trial" |

---

## Barone Discovery Workflow — "Run the Barone workflow..."

The Barone Discovery Workflow is a structured 9-step analytical pipeline that extends the standard Phase 2 analysis. It emphasizes theory-neutral initial assessment, structured theory development, and adversarial testing before committing to a defense strategy.

| Step | Report | Skill | Trigger Phrase |
|------|--------|-------|----------------|
| 1 | Report 0 — Neutral Inventory | `dw-neutral-inventory-crim` | "neutral inventory" or "Report 0" |
| 2 | Report 1 — Timeline (with Certainty) | `dw-timeline-builder-crim` | "build the timeline" |
| 3 | Report 2 — Prosecution's Case Summary | `dw-criminal-defense-crim` Phase 2 | "run Phase 2" |
| 4 | Report 2a — Theory Deconstruction | `dw-theory-deconstructor-crim` | "deconstruct the theory" |
| 5 | Report 3 — Red Flags | `dw-criminal-defense-crim` Phase 2 | (auto-generated) |
| 6 | Report 4 — Competing Defense Theories | `dw-criminal-defense-crim` Phase 2 | (auto-generated) |
| 7 | Report 4a — Theory Selection Memo | `dw-criminal-defense-crim` Phase 2 Step 2A | (attorney-driven) |
| 8 | Theory-to-Workplan (7 streams) | `dw-theory-to-workplan-crim` | "build a workplan" |
| 9 | Adversarial Stress Test | `dw-adversarial-stress-test-crim` | "stress test the theory" |

The Barone workflow also adds:
- **Certainty column** to the Timeline Sheet (CONFIRMED / PROBABLE / DISPUTED / UNCONFIRMED / ALLEGED)
- **Discovery Bucket classification** (7 Barone buckets) to the Discovery Compliance Ledger
- **Report-vs-Recording Matrix** (6-category) to all DMARs
- **Verification Protocol** ([VERIFIED] / [UNVERIFIED] flags) across all analytical skills

---

## Evidence Auditing — "Audit the..."

| Evidence Type | Skill | Trigger Phrase |
|---|---|---|
| Phone extraction (HOW it was done) | `dw-evidence-audit:dw-mobile-forensic-auditor-crim` | "audit the Cellebrite" |
| Phone contents (WHAT's on it) | `dw-evidence-audit:dw-forensic-dump-analyzer-crim` | "analyze the phone dump" |
| Body cam / dash cam / CCTV | `dw-evidence-audit:dw-video-evidence-auditor-crim` | "audit body cam" |
| Crime scene processing | `dw-evidence-audit:dw-crime-scene-auditor-crim` | "audit crime scene" |
| Evidence chain of custody | `dw-evidence-audit:dw-chain-of-custody-auditor-crim` | "audit chain of custody" |
| Cell tower / GPS / location | `dw-evidence-audit:dw-cell-site-geolocation-auditor-crim` | "audit cell site" |
| Social media screenshots/DMs | `dw-evidence-audit:dw-social-media-auditor-crim` | "audit Facebook" or "social media" |
| Photo array / lineup | `dw-evidence-audit:dw-eyewitness-identification-auditor-crim` | "audit the lineup" |
| Deleted phone data / SQLite | `dw-evidence-audit:dw-sqlite-recovery-crim` | "recover deleted messages" |
| Adult interrogation / confession | `dw-evidence-audit:dw-confession-interrogation-auditor-crim` | "audit interrogation" |
| Child forensic interview (CAC) | `dw-evidence-audit:dw-child-forensic-interview-auditor-crim` | "audit the CAC video" |
| Expert witness qualifications | `dw-evidence-audit:dw-expert-witness-evaluator-crim` | "evaluate the expert" |
| DNA / forensic biology (STR, mixtures, STRmix, TrueAllele, IGG, mtDNA, Y-STR, touch DNA) | `dw-evidence-audit:dw-dna-forensic-biology-auditor-crim` | "DNA audit" or "audit the DNA" |
| Crime lab (drug ID, toxicology, blood alcohol, certificate challenges) | `dw-evidence-audit:dw-crime-lab-auditor-crim` | "audit the crime lab" or "criminalist certificate" |
| Daubert/Foret hearing day package | `dw-evidence-audit:dw-expert-witness-evaluator-crim` (Module I) | "Daubert hearing prep" or "Foret hearing" |
| Jail calls (recordings, logs, transcripts) | `dw-evidence-audit:dw-jail-call-analyzer-crim` | "audit jail calls" or "Securus/GTL/ViaPath" |
| Witness statement consistency / impeachment synthesis | `dw-evidence-audit:dw-witness-statement-analyzer-crim` | "analyze this statement" or "compare these statements" |
| Transcription — Calcasieu (JusticeText); normally reached via dw-transcript-router-crim | `dw-transcription:dw-transcript-pipeline-calcasieu-crim` | "JusticeText transcript" |
| Transcription — all other parishes (Rev.com); normally reached via dw-transcript-router-crim | `dw-transcription:dw-transcript-pipeline-rev-crim` | "Rev transcript" |

---

## Motions & Pleadings — "Draft a..."

| Motion Type | Skill | Trigger Phrase |
|---|---|---|
| Suppress evidence (4th/5th Amend.) | `dw-pleadings:dw-suppression-motion-crim` | "motion to suppress" |
| Oppose 404(b) / other crimes | `dw-pleadings:dw-404b-opposition-crim` | "oppose the 404(b)" |
| Reduce bond / pretrial release | `dw-pleadings:dw-bond-and-release-motion-crim` | "bond reduction" |
| Speedy trial | `dw-pleadings:dw-pretrial-motion-library-crim` | "speedy trial motion" |
| Bill of particulars | `dw-pleadings:dw-pretrial-motion-library-crim` | "bill of particulars" |
| Motion to compel discovery | `dw-pleadings:dw-pretrial-motion-library-crim` | "motion to compel" |
| Severance / change of venue | `dw-pleadings:dw-pretrial-motion-library-crim` | "severance" or "change of venue" |
| Reveal the deal | `dw-pleadings:dw-pretrial-motion-library-crim` | "reveal the deal" |
| Recusal | `dw-pleadings:dw-pretrial-motion-library-crim` | "recusal" |
| Continuance | `dw-pleadings:dw-pretrial-motion-library-crim` | "continuance" |
| Legal research / cite check (case.dev, CourtListener, Westlaw) | `dw-ops:dw-case-law-researcher-crim` | "research case law" or "is this still good law" |

All motion skills use the template selection protocol in `dw-shared-protocols-crim/references/` to search DEVONthink for firm templates before drafting.

---

## Trial Preparation — "Prep for trial..."

| Task | Skill | Trigger Phrase |
|---|---|---|
| Cross-examination outlines (state witnesses) | `dw-trial-prep:dw-cross-exam-architect-crim` | "build a cross for [witness]" |
| Direct-examination outlines (defense witnesses) | `dw-trial-prep:dw-direct-exam-architect-crim` | "build a direct for [witness]" or "defendant testimony prep" |
| Opening statement + closing argument (paired) | `dw-trial-prep:dw-trial-narrative-builder-crim` | "draft opening" or "draft closing" or "trial narrative" |
| Jury instructions / charges | `dw-trial-prep:dw-jury-instructions-builder-crim` | "draft jury instructions" |
| Jury selection / voir dire | `dw-trial-prep:dw-voir-dire-assistant-crim` | "prep voir dire" |
| Track errors for appeal | `dw-trial-prep:dw-appellate-error-monitor-crim` | "preserve error" or "log error" |
| Real-time trial-day logging (objections, witnesses, exhibits, jurors) | `dw-trial-prep:dw-trial-day-assistant-crim` | "log this objection" or "today's witness" |
| Generate investigator tasks | `dw-trial-prep:dw-defense-investigator-tasking-crim` | "investigator assignment" |
| Track discovery compliance | `dw-intake-discovery:dw-discovery-compliance-monitor-crim` | "update the discovery ledger" |
| Brady/Giglio audit | `dw-intake-discovery:dw-brady-giglio-auditor-crim` | "run Brady audit" |
| Rank state witnesses by threat (Phase 3 capstone; feeds cross-exam) | `dw-trial-prep:dw-witness-threat-matrix-crim` | "witness threat matrix" or "rank the witnesses" |
| Exhibit metadata (authentication route, anticipated objections, sponsoring witness) | `Case Tables.xlsx` Evidence Table, via `dw-core:dw-criminal-defense-crim` Phase 1 Step 4 | "exhibit list" or "authentication route" |
| Live trial exhibit status (offered -> admitted/excluded) | `dw-trial-prep:dw-trial-day-assistant-crim` (Module D) | "exhibit tracker" or "what's been admitted" |
| Simulated jury focus group on the theory | `dw-trial-prep:dw-jury-focus-group-crim` | "focus group the case" or "how would a jury react" |

---

## Sentencing, Appeal & Post-Conviction — "After trial..."

| Task | Skill | Trigger Phrase |
|---|---|---|
| Sentencing mitigation package | `dw-disposition:dw-sentencing-mitigation-specialist-crim` | "build sentencing mitigation" |
| Probation / parole revocation defense (Morrissey-Gagnon rights, technical-violation caps, alternative sanctions) | `dw-disposition:dw-probation-parole-revocation-crim` | "revocation" or "probation violation" or "PV hearing" |
| Expungement eligibility deep-screen + motion packet drafting (Arts. 976-978, uniform forms) | `dw-disposition:dw-expungement-drafter-crim` | "expunge" or "expungement" or "clear my record" |
| Habitual offender bill audit | `dw-disposition:dw-habitual-offender-auditor-crim` | "audit the habitual bill" |
| Evaluate plea offer | `dw-disposition:dw-plea-negotiation-analyzer-crim` | "analyze the plea offer" |
| Padilla immigration + collateral-consequences advisement (registration, firearms, licensing, housing, voting; bilingual EN/ES, signable) | `dw-disposition:dw-padilla-advisement-crim` | "Padilla advisement" or "collateral consequences of a plea" |
| Draft direct-appeal brief (assignments of error, argument, reply) | `dw-disposition:dw-appellate-brief-builder-crim` | "appellate brief" or "appeal brief" or "assignments of error" |
| Post-conviction relief (PCR / habeas / sentence modification) | `dw-disposition:dw-post-conviction-relief-crim` | "post-conviction" or "PCR" or "habeas" |
| Close the case (disposition, final billing, expungement check) | `dw-disposition:dw-case-disposition-crim` | "close the case" or "final disposition" |

---

## Charge-Type Specialists — "What's the framework for [charge]..."

Each specialist provides charge-specific elements, defenses, sentencing exposure, motions, and discovery checklists. Routed to from `dw-criminal-defense-crim` Phase 2 or directly when the charge type is known.

| Charge Type | Skill | Trigger Phrase |
|---|---|---|
| Drug offenses (CDS, distribution, possession with intent) | `dw-offense-specialists:dw-drug-offense-specialist-crim` | "drug case" or "CDS" |
| DWI / OWI / vehicular homicide | `dw-offense-specialists:dw-dwi-specialist-crim` | "DWI" or "DUI" |
| Sex offenses (incl. SANE exam audits) | `dw-offense-specialists:dw-sex-offense-specialist-crim` | "sex offense" or "SANE" |
| Firearms offenses (state and federal) | `dw-offense-specialists:dw-firearms-specialist-crim` | "firearm charge" or "felon in possession" |
| Violent crime (murder, manslaughter, agg battery, armed robbery, kidnapping, home invasion) | `dw-offense-specialists:dw-violent-crime-specialist-crim` | "murder" or "manslaughter" or "armed robbery" or "agg battery" or "self-defense" |

---

## Intake & Setup — "Set up..."

| Task | Skill | Trigger Phrase |
|---|---|---|
| Client intake interview (first meeting, conflict check, immediate-action triage) | `dw-intake-discovery:dw-client-intake-interview-crim` | "intake" or "new client" or "first meeting" |
| Client interview question sheets (initial + follow-up; the sheet the attorney USES to question the client) | `dw-intake-discovery:dw-client-interview-drafter-crim` | "client interview sheet" or "jail visit prep sheet" |
| Evidence folder placeholders | `dw-ops:dw-evidence-placeholder-crim` | "evidence placeholders" |
| Medical chronology (PI) | `medical-chronology` | "medical chronology" or "med chron" |
| Court & jail visit tracker (weekly docket sweep) | `dw-ops:dw-court-jail-tracker-crim` | "update the tracker" or "court dates this week" |
| Client letters, jail mail, family updates | `dw-ops:dw-client-communication-drafter-crim` | "write to the client" or "jail mail" |
| Apple Notes jail-visit checklist | `dw-ops:dw-jail-visit-list-crim` | "jail visit list" |
| Log client meetings into DefenderData | `dw-ops:dw-defenderdata-meeting-logger-crim` | "log my client meetings" |
| Billing narratives / time entries | `dw-ops:dw-billing-narrative-generator-crim` | "billing narrative" |
| Stamp filenames onto evidence images | `dw-ops:dw-image-filename-stamp-crim` | "stamp the filenames" or "label these photos" |

*Note: `dw-lwop-populator` was retired in v5.3 — its functionality merged into `dw-criminal-defense-crim` Phase 1 Step 3.*

---

## Shared References (Not Direct-Trigger)

These skills are read by other skills as reference protocols — you don't invoke them directly:

| Skill | What It Does | Read By |
|---|---|---|
| `dw-core:dw-data-contracts-crim` | Output schema definitions | All skills producing deliverables |
| `dw-core:dw-case-brain-crim` | Session persistence (also direct-trigger) | Every skill at session open/close |

<!-- END AUTOGEN: routing-tables (regen-skill-index.py) -->

---

## Can't Find What You Need?

If none of the above matches:
1. **General criminal defense work** → Start with `dw-criminal-defense-crim` — it routes to specialists
2. **New discovery just arrived** → Start with `dw-discovery-orchestrator-crim` — it triages to auditors
3. **Not sure what phase we're in** → Start with `dw-case-dashboard-crim` — it tells you where you are
4. **Something entirely new** → Use `skill-creator` to build a new skill

---

*D&W Skill Index v1.2 — May 2026*

*v1.2 changes (Barone Discovery Workflow Audit): added `dw-neutral-inventory-crim` (Report 0), `dw-theory-deconstructor-crim` (Report 2a), `dw-theory-to-workplan-crim` (7-stream workplan), `dw-adversarial-stress-test-crim` (prosecutor red-team); new "Barone Discovery Workflow" section documenting the 9-step analytical pipeline; updated Quick Lookup with 4 new rows; `dw-criminal-defense-crim` Report 4 renamed from "Core Defense Narrative" to "Competing Defense Theories" with new Report 4a (Theory Selection Memo); Timeline Sheet enhanced with Certainty column; Discovery Compliance Ledger enhanced with 7-bucket classification; DMAR enhanced with Report-vs-Recording Matrix (6-category); new shared protocol `verification-protocol.md`.*

*v1.1 changes: added `dw-client-intake-interview-crim`, `dw-jail-call-analyzer-crim`, `dw-trial-day-assistant-crim`, `dw-appellate-brief-builder-crim`, `dw-violent-crime-specialist-crim`; new "Charge-Type Specialists" section consolidating all five specialists; renamed "Sentencing & Post-Conviction" to "Sentencing, Appeal & Post-Conviction"; surfaced Daubert/Foret hearing day package (Module I) inside `dw-expert-witness-evaluator-crim`; removed retired `dw-lwop-populator` row.*

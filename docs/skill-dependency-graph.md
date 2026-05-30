# D&W Skill Dependency Graph

This file documents how skills in `skills/dw-*/` connect to each other — what each skill consumes (its inputs from other skills), what it produces (its outputs to other skills), and which connections cross category boundaries.

**Why this exists:** the established skill collection has dozens of producer→consumer relationships that aren't always visible from a single skill's SKILL.md. When changing a skill's output schema, the upstream effect on consumers must be considered. When evaluating hypothetical plugin packaging, this graph identifies which dependencies cross plugin boundaries (i.e., would become inter-plugin dependencies).

**Source of truth:** the integration sections inside each skill's SKILL.md, the master orchestrator `dw-criminal-defense/SKILL.md` Phase routing, and the cross-skill integration patterns table in `CLAUDE.md`. This file consolidates and extends them.

**Maintenance:** update when a skill changes its inputs/outputs, when a new skill is added, or when an existing dependency is rewired. The graph is hand-curated; no script enforces it. Run `bin/lint-skills.py` to confirm cross-skill references resolve (E4 catches broken `dw-*` mentions).

---

## Universal infrastructure dependencies

Every analytical or motion-drafting skill depends on the same infrastructure stack. These edges are implicit in every skill and not repeated below.

| Infrastructure skill | What it provides | Consumed by |
|---|---|---|
| `dw-shared-protocols` | Work-product marking, output-path formula, captions, citation styles | Every standard skill (Step 0.5) |
| `dw-template-selector` | DEVONthink template-search protocol | Every motion/pleading skill before drafting |
| `dw-data-contracts` | Cross-skill output schemas | Every skill producing structured output |
| `dw-case-brain` | Session persistence | Every skill at session open/close |
| `dw-criminal-defense` | Master 3-phase workflow + routing | Functions as the orchestrator that dispatches to all others |

---

## Phase-organized routing (from `dw-criminal-defense`)

The master skill dispatches to specialist skills in defined phases. These edges are routing decisions, not data flows — but they form the spine of the workflow.

### Phase 1 — Intake & Discovery Processing

```
dw-client-intake-interview  ──(client narrative + immediate-action triage)──▶  dw-criminal-defense (Phase 1)
dw-criminal-defense (Phase 1)  ──(folder + Case Profile + LWOP review)──▶  dw-case-brain
dw-criminal-defense (Phase 1)  ──(media folder placeholders)──▶  dw-evidence-placeholder
```

### Phase 2 Step 1C — Specialist Evidence Routing

```
dw-criminal-defense (Phase 2)  ──┐
                                 ├─▶  dw-eyewitness-identification-auditor       (eyewitness ID issues)
                                 ├─▶  dw-confession-interrogation-auditor        (interrogation/Miranda)
                                 ├─▶  dw-mobile-forensic-auditor                 (phone extraction integrity)
                                 ├─▶  dw-forensic-dump-analyzer                  (phone contents analysis)
                                 ├─▶  dw-video-evidence-auditor                  (BWC / dash / CCTV)
                                 ├─▶  dw-cell-site-geolocation-auditor           (CSLI / GPS / tower dumps)
                                 ├─▶  dw-social-media-auditor                    (social media authenticity)
                                 ├─▶  dw-child-forensic-interview-auditor        (CAC interviews)
                                 ├─▶  dw-expert-witness-evaluator                (any expert; Module I for Daubert hearing)
                                 └─▶  dw-jail-call-analyzer                      (Securus/GTL/ViaPath recordings)
```

### Phase 2 Step 1D — Charge-Type Specialist Routing

```
dw-criminal-defense (Phase 2)  ──┐
                                 ├─▶  dw-drug-offense-specialist
                                 ├─▶  dw-dwi-specialist
                                 ├─▶  dw-sex-offense-specialist
                                 ├─▶  dw-firearms-specialist
                                 └─▶  dw-violent-crime-specialist
```

Multi-specialist cases (e.g., armed robbery with felon-in-possession enhancement) dispatch to all applicable specialists.

### Phase 2 Step 2 — 8 Case Analysis Reports

Reports 1-8 are produced by `dw-criminal-defense` directly using `references/case-analysis-prompts.md`. Specific reports route to follow-up skills:

```
Report 3 (Immediate Red Flags)       ──▶  dw-suppression-motion / dw-expert-witness-evaluator
Report 5 (Viable Legal Defenses)     ──▶  dw-404b-opposition / dw-sentencing-mitigation-specialist / dw-habitual-offender-auditor
Report 7 (Missing Discovery)         ──▶  dw-brady-giglio-auditor (auto-action)
Report 8 (Witness Impeachment)       ──▶  dw-cross-exam-architect (auto-action)
```

### Phase 3 — Trial Prep & Trial Day

```
dw-criminal-defense (Phase 3 Step 7)   ──(Witness Battle Cards, mapping)──▶  dw-cross-exam-architect
dw-criminal-defense (Phase 3 Step 7)   ──(direct-exam preparation)──▶  dw-defense-investigator-tasking
dw-criminal-defense (Phase 3 Step 9)   ──(open/close framing)──▶  (attorney-driven; framework only)
dw-criminal-defense (Phase 3 Step 10)  ──(error preservation)──▶  dw-appellate-error-monitor
dw-criminal-defense (Phase 3 Step 11)  ──(live trial-day support)──▶  dw-trial-day-assistant
dw-criminal-defense (Phase 3 Step 12)  ──(notebook assembly)──▶  dw-trial-notebook-builder
```

### Post-Verdict / Post-Trial

```
dw-appellate-error-monitor (Module H)    ──(ranked appellate issues + designated record)──▶  dw-appellate-brief-builder
dw-appellate-error-monitor (Module E)    ──(post-trial motion package)──▶  dw-appellate-brief-builder (preservation argument)
                                         (collateral relief instead of direct appeal)──▶  dw-post-conviction-relief
dw-criminal-defense                       ──(case closing)──▶  dw-case-disposition
```

---

## Bidirectional / cross-feed integrations

Several skills feed each other in both directions. These are tighter contracts than one-way routing.

### `dw-trial-day-assistant` ⇄ `dw-appellate-error-monitor`

The objection-log schema in `dw-trial-day-assistant` Module B is **field-for-field aligned** with `dw-appellate-error-monitor` Modules A/B (the additive `Day` and `Time` fields are the only difference, and only because trial-day logging happens before transcript pages exist). When `dw-appellate-error-monitor` ingests the trial-day log, no re-keying is required.

```
dw-trial-day-assistant Module B  ──(per-objection entry: time / witness / objector / ground / ruling / proffer)──▶  dw-appellate-error-monitor Module A
dw-trial-day-assistant Module B  ──(missed-objection sub-log)──▶  dw-appellate-error-monitor Module B
```

**Schema contract location:** `skills/dw-trial-day-assistant/SKILL.md` Module B, mirrored in `skills/dw-appellate-error-monitor/SKILL.md` Modules A and B.

### `dw-trial-day-assistant` ⇄ `dw-cross-exam-architect`

Per-witness scorecard (Module C) rolls into next-day cross prep.

```
dw-trial-day-assistant Module C (witness scorecard)  ──(per-witness: theme alignment, key admissions, what cross still needs)──▶  dw-cross-exam-architect (next-day prep)
```

### `dw-jail-call-analyzer` ⇄ `dw-witness-threat-matrix`

When `dw-jail-call-analyzer` Module D identifies tampering risk (witness contact attempts, threats, coaching), it cross-feeds `dw-witness-threat-matrix`'s Refresh Mode for updated witness-contact monitoring.

```
dw-jail-call-analyzer Module D (tampering risk)  ──(witness contact / threat findings)──▶  dw-witness-threat-matrix (Refresh Mode)
```

### `dw-client-intake-interview` ⇄ all charge specialists

The intake interview's charge-type dispatcher routes to the appropriate specialist based on the booking charges.

```
dw-client-intake-interview Module B (charge ID + dispatcher)  ──┐
                                                                ├─▶  dw-drug-offense-specialist (if drug)
                                                                ├─▶  dw-dwi-specialist           (if DWI/OWI)
                                                                ├─▶  dw-sex-offense-specialist   (if sex offense)
                                                                ├─▶  dw-firearms-specialist      (if firearms)
                                                                └─▶  dw-violent-crime-specialist (if violent)
```

For white-collar and juvenile (no current specialist), the dispatcher emits `[ATTORNEY TO ROUTE]` and stops.

---

## Audit → motion handoffs

Several evidence auditors produce findings that drive motion drafting downstream.

| Audit skill | Triggers | Motion skill |
|---|---|---|
| `dw-confession-interrogation-auditor` Step 4 | CRITICAL/SIGNIFICANT findings | `dw-suppression-motion` (La. C.Cr.P. Art. 703 motion) |
| `dw-eyewitness-identification-auditor` Step 5 | Suggestiveness / unreliability findings | `dw-suppression-motion` (motion to suppress identification) |
| `dw-mobile-forensic-auditor` Step 5 | Search-warrant or chain-of-custody defects | `dw-suppression-motion` |
| `dw-cell-site-geolocation-auditor` Step 5 | Stingray / geofence / tower-dump 4th Amend. defects | `dw-suppression-motion` |
| `dw-expert-witness-evaluator` Step 4 | EXCLUDE/LIMIT classification | `dw-pretrial-motion-library` (motion in limine) or hearing day package via Module I |
| `dw-brady-giglio-auditor` | Missing impeachment or favorable evidence | `dw-pretrial-motion-library` (motion to compel) |
| `dw-discovery-compliance-monitor` | Discovery violations | `dw-pretrial-motion-library` (motion to compel / sanctions) |

---

## Audit → cross-exam handoffs

Audit outputs feed cross-examination chapter generation.

| Audit skill | Cross-exam consumer |
|---|---|
| `dw-confession-interrogation-auditor` Module H | `dw-cross-exam-architect` (interrogating officer cross) |
| `dw-eyewitness-identification-auditor` Module H | `dw-cross-exam-architect` (identifying witness + lineup admin cross) |
| `dw-expert-witness-evaluator` Module G + STEP 4 | `dw-cross-exam-architect` (expert cross — uses `references/cross-exam-seeds.md` discipline-specific outlines) |
| `dw-jail-call-analyzer` Module G | `dw-cross-exam-architect` (defendant cross fodder if defendant testifies) |
| `dw-mobile-forensic-auditor` + `dw-forensic-dump-analyzer` | `dw-cross-exam-architect` (forensic examiner cross) |
| `dw-video-evidence-auditor` | `dw-cross-exam-architect` (officer body-cam cross) |
| `dw-witness-statement-analyzer` | `dw-cross-exam-architect` (impeachment from prior statements) |

---

## Transcription pipeline

Audio/video evidence flows through the transcription pipeline before downstream analysis.

```
(raw audio/video media)  ──▶  dw-transcript-router  ──┬─▶  dw-transcript-pipeline-calcasieu (JusticeText)  if Calcasieu Parish
                                                       └─▶  dw-transcript-pipeline-rev (Rev.com)             otherwise
                                                       │
                                                       ▼
                                              (DMAR + transcript)  ──┐
                                                                      ├─▶  dw-confession-interrogation-auditor  (interrogation/confession audio)
                                                                      ├─▶  dw-jail-call-analyzer                (jail-call audio)
                                                                      ├─▶  dw-cross-exam-architect              (witness statements audio)
                                                                      └─▶  dw-video-evidence-auditor            (BWC/dash audio sync)

dw-dmar-synthesizer  ──(cross-case DMAR synthesis)──▶  Multi-defendant or multi-incident analysis
```

---

## Cross-category dependency boundaries (relevant to plugin packaging)

The 9-plugin marketplace (`dw-criminal-defense`) has been implemented as Approach B — a machine-local, in-place install with `dw-core` as the single source of truth (shared reference files reached via relative paths, no duplication). The 9 plugins are `dw-core` (foundation) plus 8 functional plugins: `dw-intake-discovery`, `dw-evidence-audit`, `dw-offense-specialists`, `dw-pleadings`, `dw-trial-prep`, `dw-transcription`, `dw-disposition`, and `dw-ops`. The following dependencies cross plugin boundaries and are now inter-plugin contracts.

| Category boundary | Crossing dependencies | Notes |
|---|---|---|
| **evidence-audit → pleadings** | All audit→suppression handoffs (confession, eyewitness, mobile, cell-site) | High-frequency edge; would need stable schema |
| **trial-prep → trial-prep** | trial-day-assistant ⇄ appellate-error-monitor objection log | Same-category but tight schema contract; survives any packaging |
| **transcription → evidence-audit** | DMAR output → confession/jail-call/witness auditors | Pipeline → consumer; would benefit from a versioned DMAR schema |
| **intake → offense-specialists** | intake-interview charge dispatcher → 5 specialists | Intake plugin would have a hard dependency on offense-specialists plugin |
| **trial-prep → disposition** | appellate-error-monitor → appellate-brief-builder; → post-conviction-relief | Post-trial ranked-issue handoff |
| **evidence-audit → trial-prep** | All audit→cross-exam handoffs | Heavy traffic; would need tooling |
| **all → core** | Every skill loads `dw-shared-protocols` + `dw-template-selector` + `dw-case-brain` | core plugin is a hard dependency for every other plugin |
| **discovery → ops** | dw-brady-giglio-auditor → dw-discovery-compliance-monitor (also discovery) | Internal to discovery |
| **disposition → ops** | dw-case-disposition → dw-billing-narrative-generator | Closing → final billing |
| **disposition → core** | dw-case-disposition → dw-case-brain (final disposition record) | Standard infrastructure dependency |

**Implication:** now that plugin packaging is implemented, every cross-category arrow above is an inter-plugin contract. Because Approach B keeps all plugins in the same repo tree (with `dw-core` as the single source of truth via relative paths), the arrangement continues to tolerate some schema drift — but each boundary listed above should eventually be encoded as a versioned schema in `dw-data-contracts` to make contracts explicit and catch drift early.

---

## Per-skill input/output reference

For each skill, the table below lists what it consumes (inputs from other skills) and what it produces (outputs other skills consume). Skills not listed are infrastructure (`core` category) or pure utilities with no producer/consumer relationships.

### Intake

| Skill | Consumes | Produces |
|---|---|---|
| `dw-client-intake-interview` | (live attorney + client) | Charge-type dispatch → 5 specialists; intake memo → `dw-criminal-defense` Phase 1 |

### Discovery

| Skill | Consumes | Produces |
|---|---|---|
| `dw-discovery-orchestrator` | Raw discovery production | Triage + routing memo to all evidence auditors |
| `dw-discovery-compliance-monitor` | Discovery production index | Compliance ledger; missing-discovery flags → `dw-pretrial-motion-library` |
| `dw-brady-giglio-auditor` | Discovery + Report 7 (Missing Discovery) | Brady demand letter; impeachment items → `dw-cross-exam-architect` |

### Evidence-audit (representative — see all in `bin/skill-index-categories.yml`)

| Skill | Consumes | Produces |
|---|---|---|
| `dw-confession-interrogation-auditor` | Interrogation transcripts (from `dw-transcript-router`); BWC | Audit report → `dw-suppression-motion` (Step 4); cross-exam seeds → `dw-cross-exam-architect` |
| `dw-jail-call-analyzer` | Jail-call recordings (transcribed via `dw-transcript-router`) | Damage / helpful content / tampering findings; tampering → `dw-witness-threat-matrix`; cross fodder → `dw-cross-exam-architect` |
| `dw-expert-witness-evaluator` | Expert CV + report + prior testimony | Daubert motion package; hearing-day deliverables (Module I); cross-exam chapters → `dw-cross-exam-architect` |
| `dw-mobile-forensic-auditor` | Cellebrite UFDR + extraction logs | Methodology audit report; suppression triggers → `dw-suppression-motion` |
| `dw-forensic-dump-analyzer` | Phone-data extraction (CSV / Cellebrite Reader) | Defense Intelligence Report; cross-exam material → `dw-cross-exam-architect` |
| `dw-video-evidence-auditor` | BWC / dash / CCTV media | Audit report; cross-exam material → `dw-cross-exam-architect` |
| `dw-eyewitness-identification-auditor` | Lineup / photo array / showup records | Reliability audit; suppression motion seed → `dw-suppression-motion` |
| `dw-cell-site-geolocation-auditor` | CSLI returns; GPS data; tower dumps; geofence warrants | Audit; suppression triggers → `dw-suppression-motion` |
| `dw-social-media-auditor` | Social media exhibits | Authentication audit; cross-exam material |
| `dw-child-forensic-interview-auditor` | CAC interview video | Interview audit; suppression / unreliability findings |
| `dw-witness-statement-analyzer` | Multiple statements per witness | Inconsistency report → `dw-cross-exam-architect` |

### Pleadings (motion-drafting)

| Skill | Consumes | Produces |
|---|---|---|
| `dw-suppression-motion` | Audit findings (multiple sources above); search warrants | La. C.Cr.P. Art. 703 motion + memo |
| `dw-404b-opposition` | State's Prieur notice + audit findings | Opposition brief |
| `dw-bond-and-release-motion` | Case Profile + bond hearing facts | Bond reduction / pretrial release motion |
| `dw-pretrial-motion-library` | Per-motion case facts | Pretrial motions: speedy trial, particulars, compel, severance, venue, recusal, quash, competency, reveal the deal, continuance |

### Trial-prep

| Skill | Consumes | Produces |
|---|---|---|
| `dw-cross-exam-architect` | Audit outputs + Report 8 (Impeachment Plan) + per-witness statements | Per-witness cross outlines; Mapping the Cross worksheets |
| `dw-jury-instructions-builder` | Defense Matrix + Defense Shield (from Phase 3) | Proposed jury charges; verdict forms |
| `dw-voir-dire-assistant` | Case Profile + jury pool research | Voir dire question outlines; Batson tracking; juror analysis cards |
| `dw-defense-investigator-tasking` | Phase 1 + 2 outputs | Investigator assignment memos |
| `dw-witness-threat-matrix` | Witness list + jail-call tampering risk | Threat assessment + monitoring plan |
| `dw-jury-focus-group` | Case theme materials + mock juror data | Focus-group analysis |
| `dw-appellate-error-monitor` | Trial transcripts + objection log (from `dw-trial-day-assistant`) + minute entries | Error-preservation audit; post-trial motion package; ranked appellate issues → `dw-appellate-brief-builder` |
| `dw-trial-day-assistant` | Daily docket + live trial events | 7-module per-day output (objection log, witness scorecard, exhibit tracker, juror log, recap, issue spotter); Module B + C feed appellate-error-monitor + cross-exam-architect |
| `dw-trial-notebook-builder` | All Phase 2 + Phase 3 deliverables | Trial Notebook assembly + Trial Readiness Gap Report |
| `dw-exhibit-manager` | Trial exhibits + court rulings | Master exhibit list + authentication tracker |
| `dw-timeline-builder` | Discovery documents | Comprehensive Case Timeline (Phase 2 Report 1 input) |

### Transcription

| Skill | Consumes | Produces |
|---|---|---|
| `dw-transcript-router` | Audio/video media + parish | Routing to calcasieu or rev pipeline |
| `dw-transcript-pipeline-calcasieu` | Audio/video (Calcasieu cases) | DMAR (Defense Media Analysis Report) + TranscriptPad case |
| `dw-transcript-pipeline-rev` | Audio/video (non-Calcasieu) | DMAR + TranscriptPad case (schema identical to calcasieu) |
| `dw-dmar-synthesizer` | Multiple DMARs across cases | Cross-case synthesis (multi-defendant or multi-incident) |

### Disposition

| Skill | Consumes | Produces |
|---|---|---|
| `dw-sentencing-mitigation-specialist` | Case Profile + mitigation evidence | Sentencing memorandum + mitigation packet |
| `dw-habitual-offender-auditor` | Predicate convictions + State's habitual bill | Audit of predicate sufficiency under La. R.S. 15:529.1; *Shelton* challenges |
| `dw-plea-negotiation-analyzer` | Plea offer + case posture | Plea evaluation memo |
| `dw-appellate-brief-builder` | `dw-appellate-error-monitor` Module H ranked issues + designated record + Module E post-trial motion package | Direct-appeal brief + reply brief |
| `dw-post-conviction-relief` | Conviction record + post-conviction triggering event | PCR application (Art. 924-930.10); federal habeas (§ 2254); Art. 881.1 sentence modification |
| `dw-case-disposition` | Final disposition + sentence | Case closing checklist; client notification draft; appeal/expungement eligibility |

### Offense-specialists

All five (`dw-drug-offense-specialist`, `dw-dwi-specialist`, `dw-sex-offense-specialist`, `dw-firearms-specialist`, `dw-violent-crime-specialist`) follow the same pattern:

| Consumes | Produces |
|---|---|
| Charge-type identification (from `dw-client-intake-interview` or `dw-criminal-defense` Phase 2 Step 1D) + per-charge discovery | Element-by-element defense theory; specialist-recommended motions → `dw-pretrial-motion-library` / `dw-suppression-motion`; sentencing exposure → `dw-sentencing-mitigation-specialist` / `dw-habitual-offender-auditor` |

### Ops (operational utilities)

| Skill | Consumes | Produces |
|---|---|---|
| `dw-billing-narrative-generator` | Session activity logs + Case Brain updates | LEDES-coded billing narratives |
| `dw-court-jail-tracker` | Public docket scrapes + jail rosters | Updated tracker spreadsheet + notifications (Slack/Google Chat/Clio) |
| `dw-client-communication-drafter` | Case events + attorney input | Client correspondence drafts |
| `dw-case-law-researcher` | Research questions | Legal memoranda |
| `dw-evidence-placeholder` | Media folder structure | One-page placeholder PDFs for media folders |
| `dw-image-filename-stamp` | Image batches | Bates-style or descriptive renames |

---

## Maintenance notes

- This file is hand-curated. Keep it in sync when skills change or when new dependencies are introduced. The linter does NOT enforce dependency-graph accuracy.
- The `category:` field in each skill's frontmatter (added by `bin/add-category-frontmatter.py`) maps each skill to its plugin-aligned bucket. The category buckets in this document match those values.
- For routing display (where each skill appears in `dw-skill-index/SKILL.md`), see `bin/skill-index-categories.yml` — that file controls the visible routing tables; this document captures the underlying data flow.
- If a future cross-skill dependency is added, also update CLAUDE.md's "Cross-skill integration patterns" table (the short version) and re-run `bin/lint-skills.py` to confirm cross-references resolve.

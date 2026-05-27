---
name: dw-skill-index
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

## Quick Lookup — "I need to..."

| I need to... | Use this skill | Say this |
|-------------|---------------|---------|
| Start a new case | `dw-criminal-defense` | "new case" or "case intake" |
| Load an existing case | `dw-case-brain` | "load the case" or "open the matter" |
| Check case status | `dw-case-dashboard` | "where do we stand" or "case status" |
| Process discovery | `dw-criminal-defense` | "run Phase 1" |
| Analyze the case | `dw-criminal-defense` | "run Phase 2" |
| Build trial prep | `dw-criminal-defense` | "run Phase 3" |
| Assemble trial notebook | `dw-trial-notebook-builder` | "build the trial notebook" |
| Triage new discovery | `dw-discovery-orchestrator` | "new discovery arrived" |
| Transcribe recordings | `dw-transcript-router` | "transcribe the evidence" |
| Compare transcripts across cases | `dw-dmar-synthesizer` | "compare the DMARs" |

---

## Evidence Auditing — "Audit the..."

| Evidence Type | Skill | Trigger Phrase |
|--------------|-------|---------------|
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

---

## Motions & Pleadings — "Draft a..."

| Motion Type | Skill | Trigger Phrase |
|------------|-------|---------------|
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
|------|-------|---------------|
| Cross-examination outlines (state witnesses) | `dw-cross-exam-architect` | "build a cross for [witness]" |
| Direct-examination outlines (defense witnesses) | `dw-direct-exam-architect` | "build a direct for [witness]" or "defendant testimony prep" |
| Opening statement + closing argument (paired) | `dw-trial-narrative-builder` | "draft opening" / "draft closing" / "trial narrative" |
| Jury instructions / charges | `dw-jury-instructions-builder` | "draft jury instructions" |
| Jury selection / voir dire | `dw-voir-dire-assistant` | "prep voir dire" |
| Track errors for appeal | `dw-appellate-error-monitor` | "preserve error" or "log error" |
| Generate investigator tasks | `dw-defense-investigator-tasking` | "investigator assignment" |
| Track discovery compliance | `dw-discovery-compliance-monitor` | "update the discovery ledger" |
| Brady/Giglio audit | `dw-brady-giglio-auditor` | "run Brady audit" |

---

## Sentencing & Post-Conviction — "After trial..."

| Task | Skill | Trigger Phrase |
|------|-------|---------------|
| Sentencing mitigation package | `dw-sentencing-mitigation-specialist` | "build sentencing mitigation" |
| Habitual offender bill audit | `dw-habitual-offender-auditor` | "audit the habitual bill" |
| Evaluate plea offer | `dw-plea-negotiation-analyzer` | "analyze the plea offer" |
| Sex offense defense framework | `dw-sex-offense-specialist` | "sex offense" or "SANE exam" |

---

## Intake & Setup — "Set up..."

| Task | Skill | Trigger Phrase |
|------|-------|---------------|
| LWOP review sheet | `dw-lwop-populator` | "LWOP sheet" |
| Evidence folder placeholders | `dw-evidence-placeholder` | "evidence placeholders" |
| Medical chronology (PI) | `medical-chronology` | "medical chronology" or "med chron" |
| PI video scripts | `dw-pi-video-generator` | "PI video" or "make a video" |

---

## Shared References (Not Direct-Trigger)

These skills are read by other skills as reference protocols — you don't invoke them directly:

| Skill | What It Does | Read By |
|-------|-------------|---------|
| `dw-data-contracts` | Output schema definitions | All skills producing deliverables |
| `dw-case-brain` | Session persistence (also direct-trigger) | Every skill at session open/close |

---

## Can't Find What You Need?

If none of the above matches:
1. **General criminal defense work** → Start with `dw-criminal-defense` — it routes to specialists
2. **New discovery just arrived** → Start with `dw-discovery-orchestrator` — it triages to auditors
3. **Not sure what phase we're in** → Start with `dw-case-dashboard` — it tells you where you are
4. **Something entirely new** → Use `skill-creator` to build a new skill

---

*D&W Skill Index v1.1 — May 2026. v1.1 added: `dw-direct-exam-architect`, `dw-trial-narrative-builder`, `dw-dna-forensic-biology-auditor`, `dw-crime-lab-auditor`.*

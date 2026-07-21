# D&W Skills — Output Path Convention
**Internal reference doc for skill authoring. Not a runtime-loaded skill.**

This doc establishes the standard output-path convention for every D&W skill that writes a file. Use it when authoring or updating a skill's SKILL.md to fill in the skill-specific output block (see `OUTPUT_BLOCK_BOILERPLATE.md`).

---

## The Rule

Every D&W deliverable saves to an absolute path under the active case folder, never to the Cowork project default directory, `/home/claude`, `/tmp`, or `~/Downloads`.

**Canonical path formula:**

```
{CASE_ROOT}/Deliverables/{Phase}/{SkillName}/{YYYY-MM-DD}_{descriptive-filename}.{ext}
```

---

## `CASE_ROOT`

The absolute path to the active client's case folder. Resolved in this order:

1. Active `dw-case-brain-crim` session (preferred)
2. Absolute path in the attorney's prompt
3. Cowork project → client folder mapping
4. Ask the attorney

D&W case folders live in one of three Google Drive shared drives (mounted via Google Drive for Desktop):

| Shared Drive | `CASE_ROOT` Pattern |
|---|---|
| D&W Law Firm (CJW) | `.../Shared drives/D&W Law Firm (CJW)/Clients/[Client Last, First]/` |
| CALCASIEU PDO Files | `.../Shared drives/CALCASIEU PDO Files/[Client Last, First]/` |
| NOLA Conflict Cases | `.../Shared drives/NOLA Conflict Cases/[Client Last, First]/` |

Full mount prefix: `/Users/greatelephant82/Library/CloudStorage/GoogleDrive-cjw@danielswashington.com/`

---

## Phase Folders

| Phase Folder | Skills That Write Here |
|---|---|
| `Phase-1-Intake/` | `dw-criminal-defense-crim` |
| `Phase-2-Discovery/` | All auditors, DMAR pipelines, dump analyzers, discovery orchestrator/monitor, Brady/Giglio |
| `Phase-3-Motions/` | `dw-suppression-motion-crim`, `dw-404b-opposition-crim`, `dw-pretrial-motion-library-crim`, `dw-bond-and-release-motion-crim` |
| `Phase-4-Trial/` | `dw-cross-exam-architect-crim`, `dw-jury-instructions-builder-crim`, `dw-voir-dire-assistant-crim`, `dw-trial-notebook-builder-crim` |
| `Post-Trial/` | `dw-sentencing-mitigation-specialist-crim`, `dw-appellate-error-monitor-crim` |

If a skill runs across phases, assign it to the phase where the deliverable is primarily used.

---

## Filename Convention

```
{YYYY-MM-DD}_{descriptive-filename}.{ext}
```

- ISO date prefix keeps files chronologically sortable within the skill folder
- Hyphens in the descriptive portion, no spaces
- Attorney-facing descriptive name, not a slug (`Motion-to-Suppress-Custodial-Statement` not `motion_supp_1`)

**Examples:**

```
2026-04-05_Motion-to-Suppress-Custodial-Statement.docx
2026-04-05_DMAR-Jail-Calls-Batch-1.docx
2026-04-05_Cross-Det-Johnson.docx
2026-04-05_Trial-Notebook-Master-Index.pdf
```

---

## Full Folder Tree

```
{CASE_ROOT}/
└── Deliverables/
    ├── Phase-1-Intake/
    │   └── dw-criminal-defense-crim/
    ├── Phase-2-Discovery/
    │   ├── dw-transcript-router-crim/
    │   ├── dw-transcript-pipeline-calcasieu-crim/
    │   ├── dw-transcript-pipeline-rev-crim/
    │   ├── dw-dmar-synthesizer-crim/
    │   ├── dw-forensic-dump-analyzer-crim/
    │   ├── dw-mobile-forensic-auditor-crim/
    │   ├── dw-video-evidence-auditor-crim/
    │   ├── dw-social-media-auditor-crim/
    │   ├── dw-cell-site-geolocation-auditor-crim/
    │   ├── dw-crime-scene-auditor-crim/
    │   ├── dw-chain-of-custody-auditor-crim/
    │   ├── dw-confession-interrogation-auditor-crim/
    │   ├── dw-child-forensic-interview-auditor-crim/
    │   ├── dw-eyewitness-identification-auditor-crim/
    │   ├── dw-expert-witness-evaluator-crim/
    │   ├── dw-sqlite-recovery-crim/
    │   ├── dw-evidence-placeholder-crim/
    │   ├── dw-discovery-orchestrator-crim/
    │   ├── dw-discovery-compliance-monitor-crim/
    │   ├── dw-brady-giglio-auditor-crim/
    │   └── dw-defense-investigator-tasking-crim/
    ├── Phase-3-Motions/
    │   ├── dw-suppression-motion-crim/
    │   ├── dw-404b-opposition-crim/
    │   ├── dw-pretrial-motion-library-crim/
    │   ├── dw-bond-and-release-motion-crim/
    │   ├── dw-habitual-offender-auditor-crim/
    │   ├── dw-plea-negotiation-analyzer-crim/
    │   └── dw-sex-offense-specialist-crim/
    ├── Phase-4-Trial/
    │   ├── dw-cross-exam-architect-crim/
    │   ├── dw-jury-instructions-builder-crim/
    │   ├── dw-voir-dire-assistant-crim/
    │   └── dw-trial-notebook-builder-crim/
    └── Post-Trial/
        ├── dw-sentencing-mitigation-specialist-crim/
        └── dw-appellate-error-monitor-crim/
```

---

## Exemptions (Non-Filesystem Destinations)

These skills write to systems of record, not the filesystem. They are exempt from this convention for their primary output:

| Skill | Destination |
|---|---|
| `dw-case-brain-crim` | DEVONthink `Case Brains (Claude).dtBase2` |
| Template saves from any skill | DEVONthink `Law Library-Criminal` |
| Clio activity/note writes | Clio Manage |
| Things 3 task writes | Things 3 |
| Obsidian writes | `Dream Team Law` vault |

If a skill writes a local backup `.docx` or `.pdf` alongside the system-of-record entry, the local backup follows this convention.

---

## Post-Write Requirement

After every file write, the skill reports the full absolute path back to the attorney. No exceptions. See boilerplate for exact format.

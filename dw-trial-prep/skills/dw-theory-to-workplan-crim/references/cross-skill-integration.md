# Cross-Skill Integration

Read at the Cross-Skill Integration section (after Step 4) — prerequisites, upstream reads, the stream-to-skill routing table, and downstream writes.

### This skill REQUIRES (prerequisite):

- `dw-criminal-defense-crim` Report 4/4a -- Theory Selection Memo (mandatory input; will not generate workplan without it)

### This skill READS FROM:

- `dw-case-brain-crim` -- structured case context, companion skill outputs, open issues
- `dw-criminal-defense-crim` Reports 1-8 + 4a -- all Phase 2 analytical outputs (plus Report 0 from `dw-neutral-inventory-crim` and Report 2a from `dw-theory-deconstructor-crim`)
- `dw-discovery-compliance-monitor-crim` -- outstanding discovery ledger (feeds Stream 2)
- `dw-brady-giglio-auditor-crim` -- Brady/Giglio findings (feeds Streams 2 and 4)
- All completed audit reports -- every auditor skill's output feeds task generation across streams
- `Case Tables.xlsx` -- Evidence Table, Witness List, Timeline

### This skill ROUTES TO (downstream execution):

| Stream | D&W Skill | What Flows |
|--------|-----------|-----------|
| 1 - Investigation | `dw-defense-investigator-tasking-crim` | Investigation tasks with witness lists, location visits, record subpoenas |
| 2 - Discovery | `dw-discovery-compliance-monitor-crim`, `dw-brady-giglio-auditor-crim` | New discovery demands, Brady/Giglio-specific demands |
| 2 - Discovery | `dw-pretrial-motion-library-crim` | Motions to compel |
| 3 - Expert | `dw-expert-witness-evaluator-crim` | Prosecution expert evaluations, Daubert/Foret challenge seeds |
| 3 - Expert | `dw-pretrial-motion-library-crim` | Indigent expert funding motions (La. C.Cr.P. Art. 725) |
| 4 - Motions | `dw-suppression-motion-crim` | Suppression motions (4th, 5th, 14th Amendment) |
| 4 - Motions | `dw-404b-opposition-crim` | 404(b) / Prieur opposition |
| 4 - Motions | `dw-pretrial-motion-library-crim` | All other pretrial motions |
| 5 - Witness | `dw-cross-exam-architect-crim` | Cross-examination outlines for prosecution witnesses |
| 5 - Witness | `dw-direct-exam-architect-crim` | Direct-examination outlines for defense witnesses |
| 6 - Exhibit | `Case Tables.xlsx` Evidence Table · `dw-trial-day-assistant-crim` (Module D) | Exhibit identification and authentication planning; live offer/admission status |
| 6 - Exhibit | `dw-trial-notebook-builder-crim` | Trial notebook assembly with theory-aligned tabs |
| 7 - Narrative | `dw-trial-narrative-builder-crim` | Opening statement, closing argument, theme tracker |
| 7 - Narrative | `dw-jury-instructions-builder-crim` | Theory-specific jury charges and verdict form |
| 7 - Narrative | `dw-voir-dire-assistant-crim` | Theory-aligned voir dire questions |

### This skill WRITES TO:

- Workplan document (primary deliverable)
- Apple Notes summary checklist (secondary deliverable)
- `dw-case-brain-crim` -- registers output and updates OPEN ISSUES with BLOCKED tasks

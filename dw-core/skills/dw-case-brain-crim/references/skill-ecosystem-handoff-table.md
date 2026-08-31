# Integration with D&W Skill Ecosystem — Hand-off Table

Read from the SKILL.md **Integration with D&W Skill Ecosystem** section — the task → companion skill → vault folder hand-off table.

After loading the Case Brain, hand off to the appropriate skill based on what the attorney needs:

| Task | Skill | Saves To Folder |
|---|---|---|
| Case intake / discovery processing | `dw-criminal-defense-crim` | `Cases/` |
| Phone dump analysis | `dw-forensic-dump-analyzer-crim` | `Case-Analysis/` |
| Suppression motion | `dw-suppression-motion-crim` | `Pleadings/` |
| Cross-examination prep | `dw-cross-exam-architect-crim` | `Witnesses/` (appropriate subfolder) |
| Brady/Giglio audit | `dw-brady-giglio-auditor-crim` | `Case-Analysis/` |
| Search warrant challenge | `dw-suppression-motion-crim` | `Pleadings/` |
| Cell site / CSLI | `dw-cell-site-geolocation-auditor-crim` | `Case-Analysis/` |
| 404(b) opposition | `dw-404b-opposition-crim` | `Pleadings/` |
| CI / informant audit | `dw-brady-giglio-auditor-crim` | `Case-Analysis/` |
| LWOP Part 2A / 2B population | `dw-criminal-defense-crim` (Phase 1 Step 3) | `Cases/` |
| Jury selection / voir dire | `dw-voir-dire-assistant-crim` | `Jury-Selection/` |
| Expert witness evaluation | `dw-expert-witness-evaluator-crim` | `Witnesses/Expert/` |
| Jury instructions | `dw-jury-instructions-builder-crim` | `Pretrial-Orders/` |
| Sentencing mitigation | `dw-sentencing-mitigation-specialist-crim` | `Verdict-Sentencing/` |
| Plea analysis | `dw-plea-negotiation-analyzer-crim` | `Case-Analysis/` |

The Case Brain provides the context; the companion skill does the work.

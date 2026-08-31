# Cross-Skill Integration

Read at Cross-Skill Integration of `dw-theory-deconstructor-crim/SKILL.md` — READS FROM / FEEDS tables and the workflow-position diagram, moved verbatim from SKILL.md.

---

### This skill READS FROM:

| Skill | What It Provides |
|-------|-----------------|
| `dw-criminal-defense-crim` Phase 2 Step 2 | Report 2 — Prosecution's Case Summary (hard prerequisite) |
| `dw-criminal-defense-crim` Phase 1 Step 4 | Case Tables.xlsx — Evidence Table |
| `dw-case-brain-crim` | Structured case context, charge information, Case Brain variables |
| Charge-type specialists (`dw-violent-crime-specialist-crim`, `dw-drug-offense-specialist-crim`, etc.) | Element grids and defense theory maps |
| `dw-criminal-defense-crim` Phase 2 Step 2 | Report 3 — Immediate Red Flags (suppression candidates affecting element mapping) |

### This skill FEEDS:

| Skill | What It Receives |
|-------|-----------------|
| `dw-criminal-defense-crim` Report 4 | Alternative Inference Table (Module F) provides raw material for Competing Theories / Core Defense Narrative construction |
| `dw-adversarial-stress-test-crim` | Gap Analysis Matrix (Module E) identifies the weakest points for stress-testing; Assumption Audit (Module D) provides the specific assumptions to attack |
| `dw-theory-to-workplan-crim` | Full deconstruction output informs workplan prioritization — VULNERABLE and CRITICAL GAP elements drive investigation and motion priorities |

### Workflow Position:

```
Report 2 (Prosecution's Case Summary)
    │
    ▼
Report 2a (Theory Deconstruction) ◄── YOU ARE HERE
    │
    ├──► Report 4 (Competing Theories / Core Defense Narrative)
    ├──► dw-adversarial-stress-test-crim
    └──► dw-theory-to-workplan-crim
```

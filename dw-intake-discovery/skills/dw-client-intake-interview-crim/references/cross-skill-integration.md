# Cross-Skill Integration

Read at SKILL.md Cross-Skill Integration; holds the skill-by-skill table of what intake feeds, plus the skill's version note.

| Skill | How intake feeds it |
|---|---|
| `dw-criminal-defense-crim` | Intake memo precedes Phase 1 setup. The intake memo and engagement scope are inputs to Phase 1 Step 1 (Folder Setup) and Phase 1 Step 3 (Case Profile Section 1 Identification, Section 2 Charges, Section 3 Bail). |
| `dw-bond-and-release-motion-crim` | Module D (Bond posture) is the direct input. If the client is in custody at intake, draft the bond motion within 48 hours. |
| `dw-defense-investigator-tasking-crim` | Module E (Investigation Seed) is the direct input. The investigator tasking skill turns the seed into prioritized assignments. |
| `dw-case-brain-crim` | Intake memo is the initial Case Brain entry. CASE_ROOT, defendant identification, charges, bond status, and key dates all populate from the memo. |
| `dw-billing-narrative-generator-crim` | Engagement scope (Module F) sets fee structure and scope; downstream billing must align. |
| `dw-jail-call-analyzer-crim` | Module D.4 (Jail call hygiene letter) uses templates from `dw-jail-call-analyzer-crim`. Once the client makes calls, the analyzer audits them. |
| `dw-suppression-motion-crim` | If client made law-enforcement statements, route facts post-intake. |
| `dw-confession-interrogation-auditor-crim` | If the client gave a custodial statement, route post-intake for full audit. |
| `dw-social-media-auditor-crim` | After lockdown (Module D.3), the auditor reviews captured social media for Brady, impeachment, and defense use. |
| `dw-drug-offense-specialist-crim` / `dw-dwi-specialist-crim` / `dw-sex-offense-specialist-crim` / `dw-violent-crime-specialist-crim` / `dw-firearms-specialist-crim` | Charge-type dispatcher routes per Module B. The specialist runs on the charge category once retention is final. |
| `dw-plea-negotiation-analyzer-crim` | Deferred — never run at intake. Run after discovery is in. |
| `dw-sentencing-mitigation-specialist-crim` | Tier 3 contextual data (employment, family, military, mental health) seeds mitigation. Run later. |
| `dw-shared-protocols-crim` | Loaded at Step 0.5 for marking, output paths, signature block. |

## Version note

*This skill is part of the Daniels & Washington Cowork criminal defense toolkit. Version 1.0 establishes the first-contact intake protocol upstream of dw-criminal-defense-crim Phase 1. Integrates with dw-shared-protocols-crim (marking, output paths), dw-bond-and-release-motion-crim (Module D bond posture), dw-defense-investigator-tasking-crim (Module E seed), dw-case-brain-crim (initial entry), dw-billing-narrative-generator-crim (engagement scope), dw-jail-call-analyzer-crim (hygiene letter), and the charge-type specialist family (Module B dispatcher).*

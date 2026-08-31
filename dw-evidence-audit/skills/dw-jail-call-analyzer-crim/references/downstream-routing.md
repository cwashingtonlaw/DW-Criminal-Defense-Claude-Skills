# Downstream Routing Table and Skill Integration Map

Read this file at STEP 4 (Downstream Routing) — it holds the trigger / routing / payload table for companion skills and the reads-from / feeds-into / pairs-with integration map.

| Trigger | Routing | Payload |
|---------|---------|---------|
| Any Module D witness-contact flag involving a named witness | **dw-witness-threat-matrix-crim** (Refresh Mode) | Updated Damage / Vulnerability scores for each affected witness; new impeachment hooks |
| Module G locked-in admissions exist AND defendant may testify | **dw-cross-exam-architect-crim** | Defendant Self-Cross Outline seeds (impeachment chart from G.2) |
| Module B cumulative damage triggers theory-of-defense reset | **dw-case-brain-crim** | Theory revision recommendation with citation list of contradicting admissions |
| Module D relay-person identified | **dw-defense-investigator-tasking-crim** | Investigator interview tasking for each relay person |
| Module F attorney-client breach identified | **dw-suppression-motion-crim** | Suppression motion seeds for the breached call(s) |
| Module F selective-production *Brady* concern | **dw-brady-giglio-auditor-crim** | *Brady* motion seeds with date-range gap evidence |
| Module B prior-bad-acts admissions | **dw-404b-opposition-crim** | 404(B) opposition seeds (defense will need to anticipate State's notice) |
| Module H hygiene memo finalized | **dw-client-communication-drafter-crim** | Client-letter delivery via firm protocol |
| Audio not pre-transcribed at start | **dw-transcript-router-crim** → **dw-transcript-pipeline-rev-crim** | Run BEFORE this skill on Tier 1 / Tier 2 calls |
| Any audit completion | **dw-case-brain-crim** | Case Brain "Jail Call Posture" section update with audit date, top findings, file path, open gaps |

Do not invoke downstream skills automatically. Surface the recommendations and let the attorney choose.

## Integration with Other D&W Skills (carried over from SKILL.md)

- **Reads from:** `dw-transcript-router-crim`, `dw-transcript-pipeline-rev-crim` (audio-to-transcript pipeline if calls are not pre-transcribed); `dw-case-brain-crim` (defense theory, contested elements); `dw-witness-threat-matrix-crim` (Top 10 list for triage promotion)
- **Feeds into:** `dw-witness-threat-matrix-crim` (Module D output — refresh mode); `dw-cross-exam-architect-crim` (Module G output — defendant self-cross seeds); `dw-defense-investigator-tasking-crim` (Module D relay-person tasking); `dw-suppression-motion-crim` (Module F attorney-client breach seeds); `dw-brady-giglio-auditor-crim` (Module F selective-production seeds); `dw-404b-opposition-crim` (Module B prior-bad-acts seeds); `dw-client-communication-drafter-crim` (Module H hygiene memo delivery); `dw-case-brain-crim` (audit completion update)
- **Pairs with:** `dw-confession-interrogation-auditor-crim` (custodial statements often referenced on jail calls); `dw-eyewitness-identification-auditor-crim` (witness-contact pattern in Module D may overlap with ID-witness contamination concerns)

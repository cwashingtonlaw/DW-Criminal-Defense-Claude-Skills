# DMAR Ingestion and Indexing — Case Registry and Entity Crosswalk

Read at Step 1.2 (Build the Case Registry) and Step 1.3 (Identify Shared Entities) of `dw-dmar-synthesizer-crim`; the Case Registry entry schema and the attorney-facing entity crosswalk prompt moved verbatim from SKILL.md.

## Step 1.2 — Case Registry Entry Schema

```
CASE REGISTRY ENTRY
Client: [Name from DMAR header]
Docket #: [From header]
Parish: [From header]
Platform: [JusticeText or Rev]
Analysis Date: [From header]
Media Files: [Count and list from Section 1]
Speakers Identified: [All named speakers from Section 2 + Section 6]
Finding Counts:
  CR-### (Cross-Reference): [count]
  RR-### (Report Discrepancies): [count]
  ME-### (Miranda Events): [count]
  IT-### (Interrogation Techniques): [count]
  KE-### (Key Events): [count]
```

## Step 1.3 — Cross-Case Entity Crosswalk Prompt

Present the entity crosswalk to the attorney:

> **Cross-Case Entity Crosswalk**
>
> I found the following entities appearing in multiple DMARs:
>
> | Entity | Type | Appears In | Role in Each |
> |--------|------|-----------|-------------|
> | Det. Marcus Jones | Officer | Smith DMAR, Williams DMAR | Lead interrogator in both |
> | 123 Main St | Location | Smith DMAR, Williams DMAR | Arrest location / Crime scene |
> | ...  | ... | ... | ... |
>
> *Please confirm these matches are correct, and let me know if I missed any connections or if any are false matches (different people with similar names, etc.).*

# Verification Protocol — [VERIFIED] / [UNVERIFIED] Evidence Flags
**Daniels & Washington | Criminal Defense | Shared Protocol**

This protocol standardizes how D&W skills mark the verification status of every factual assertion, catalog entry, and evidence reference across all deliverables. It supplements the Source Citation Mandate (which requires a source for every claim) by adding a binary verification flag that indicates whether the source has been directly reviewed.

---

## When to Use

Every D&W skill that catalogs, inventories, or asserts facts about case evidence must apply this protocol. This includes:
- `dw-neutral-inventory-crim` (Report 0 — every catalog entry)
- `dw-theory-deconstructor-crim` (Report 2a — every fact extraction)
- `dw-adversarial-stress-test-crim` (every evidence citation)
- `dw-theory-to-workplan-crim` (every task predicate)
- `dw-timeline-builder-crim` (every timeline event)
- `dw-discovery-compliance-monitor-crim` (every ledger entry)
- All auditor skills (every finding)

---

## The Two Flags

### [VERIFIED]
The source document has been directly reviewed by Cowork in this session, and the assertion accurately reflects what the source says.

**Requirements for [VERIFIED]:**
- The source document was uploaded to or accessible in the current session
- Cowork read the relevant portion of the document
- The assertion matches the document content (direct quote, accurate paraphrase, or correct data extraction)
- The Bate stamp or document identifier has been confirmed against the Evidence Table

### [UNVERIFIED]
The assertion is based on a reference in another document, a prior session's output, or attorney-provided information, but the original source has NOT been directly reviewed in this session.

**Common [UNVERIFIED] scenarios:**
- A police report mentions BWC footage, but the footage itself was not uploaded
- A witness is referenced in multiple reports, but the original witness statement was not provided
- An evidence item is listed in the State's index, but the actual item/report is not in discovery
- A prior Cowork report asserts a fact, but the underlying source was not re-reviewed
- Attorney stated a fact during session that has not been cross-referenced to a source document

---

## Formatting

### Inline format (within narrative text)
```
Officer Smith activated his BWC at 14:23:00. [VERIFIED — BWC metadata, Bate #0045]
The defendant was allegedly at 123 Maple St at the time of the incident. [UNVERIFIED — referenced in Incident Report p. 3; no corroborating source reviewed]
```

### Table format (within catalogs and inventories)
Add a `Verification` column to any evidence catalog or inventory table:

| Item | Source | Verification | Notes |
|------|--------|-------------|-------|
| BWC — Officer Smith | Evidence folder, Bate #0045-0048 | [VERIFIED] | Reviewed in session |
| Witness statement — Jane Doe | Referenced in Incident Report p. 3 | [UNVERIFIED] | Statement not in discovery |
| Lab report — toxicology | State's index, item #12 | [UNVERIFIED] | Report not yet produced |

### Summary format (at end of deliverable)
Every deliverable using this protocol must include a Verification Summary at the end:

```
## Verification Summary
- Total assertions: 47
- [VERIFIED]: 31 (66%)
- [UNVERIFIED]: 16 (34%)
- Top unverified gaps: [list the 3-5 most significant unverified items]
```

---

## Escalation Rules

1. **Any assertion used in a motion or filing**: Must be [VERIFIED] before inclusion. If [UNVERIFIED], the attorney must verify before filing.
2. **Any assertion used in cross-examination**: Should be [VERIFIED]. [UNVERIFIED] items may be used but attorney must be flagged.
3. **Report 0 (Neutral Inventory)**: Expected to have a mix; the verification percentage is itself a metric of discovery completeness.
4. **Report 2a (Theory Deconstruction)**: Facts in MODULE B must be [VERIFIED] to be categorized as "facts." [UNVERIFIED] items belong in the "assumptions" category until verified.

---

## Relationship to Source Citation Mandate

The Source Citation Mandate requires a source for every assertion. The Verification Protocol adds a second layer:

| Source Citation Mandate | Verification Protocol |
|---|---|
| "Where does this come from?" | "Have we actually looked at it?" |
| Requires document name, page, Bate stamp | Requires [VERIFIED] or [UNVERIFIED] tag |
| Prevents unsourced claims | Prevents false confidence in unreviewed sources |

Both are mandatory. An assertion can have a source citation (meeting the Mandate) but still be [UNVERIFIED] (the source was referenced but not directly reviewed). This is valuable information — it tells the attorney exactly what still needs to be checked.

---

## Integration with Downstream Skills

When a downstream skill consumes output from an upstream skill:
- [VERIFIED] items from the upstream skill retain their [VERIFIED] status
- [UNVERIFIED] items remain [UNVERIFIED] until the downstream skill independently reviews the source
- A downstream skill may upgrade an [UNVERIFIED] item to [VERIFIED] if it reviews the source
- A downstream skill must NEVER downgrade a [VERIFIED] item to [UNVERIFIED]

---

*Protocol Version 1.0 — May 2026. Part of the Barone Discovery Workflow Audit.*

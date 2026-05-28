# Rec 09 — Verification Protocol Integration Notes

## What Was Added
`dw-shared-protocols/references/verification-protocol.md` — a shared protocol defining the [VERIFIED] / [UNVERIFIED] evidence flag system.

## How Skills Should Load It
Skills that use the verification protocol should add it to their STEP 0.5 shared protocol load:

```
3. `dw-shared-protocols/references/verification-protocol.md` — mark evidence assertions [VERIFIED] or [UNVERIFIED]
```

## Skills That Use This Protocol
- `dw-neutral-inventory` — MODULE F (Verification Status) applies it to every catalog entry
- `dw-theory-deconstructor` — MODULE B (Fact Extraction) uses it to distinguish verified facts from unverified assertions
- `dw-adversarial-stress-test` — marks every evidence citation as [VERIFIED] or [UNVERIFIED]
- `dw-theory-to-workplan` — marks task predicates as [VERIFIED] or [UNVERIFIED]
- `dw-timeline-builder` — can be used alongside the existing Confidence and Certainty columns
- `dw-discovery-compliance-monitor` — can be used for ledger entries
- All auditor skills — can be used for findings

## Key Design Decisions
1. The protocol supplements (does not replace) the Source Citation Mandate
2. [VERIFIED] requires direct review in the current session — not just a reference in another document
3. Downstream skills inherit verification status from upstream; they can upgrade but not downgrade
4. Every deliverable using the protocol must include a Verification Summary at the end

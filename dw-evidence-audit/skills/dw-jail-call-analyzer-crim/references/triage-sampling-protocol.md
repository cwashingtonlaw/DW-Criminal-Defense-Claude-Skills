# Triage & Sampling Protocol — Tiers, Promotion Triggers, Prioritization, Roster

Read this file at STEP 2 (Triage & Sampling Protocol) — it holds the Sampling Tiers table, the Tier-Promotion Triggers, the Triage Prioritization Order, and the Triage Roster output spec.

### Sampling Tiers

| Tier | Coverage | Treatment |
|------|----------|-----------|
| **TIER 1 — Full Review** | Top ~10% of calls (or 100 calls, whichever is smaller, plus all prosecution-flagged calls regardless of tier math) | Listen to or read transcript end-to-end; timestamp every flagged moment; populate Modules B-G fully |
| **TIER 2 — Summary Review** | Next ~30% of calls | Skim transcript or scrub audio at 1.5-2x; capture one-line gist + any flag triggers; promote to Tier 1 if any flag triggers fire |
| **TIER 3 — Log Only** | Remaining ~60% | No audio/transcript review; entries sit in Module A inventory only; promote on demand if a flag fires later in the case (e.g., a new witness identified, a new charge added) |

### Tier-Promotion Triggers (Auto-Promote to Tier 1)

A call in Tier 2 or Tier 3 is automatically promoted to Tier 1 if ANY of the following hits:
- Recipient is a State's witness, victim, victim's-family member, or co-defendant
- Recipient is on the `dw-witness-threat-matrix-crim` Top 10 CRITICAL/HIGH list
- Call is on the prosecution's flagged-call list
- Call is the first call after a charging event (initial booking, indictment, superseding indictment, bond hearing, motion ruling, plea offer, trial date setting)
- Call is unusually short (< 90 seconds) AND the recipient is not a routine family contact — short calls are disproportionately tampering-coordination calls
- Call duration is at the system maximum (typically 15 minutes) AND recurs daily with the same recipient — high-volume single-recipient patterns warrant sampling
- Vendor flagged the call as a three-way connect attempt
- Call timestamp is within 48 hours of a hearing, witness interview, or known co-defendant proffer

### Triage Prioritization Order

Within each tier, prioritize listening order by:

1. **Recency from charging event** — post-indictment calls are higher-stakes than pre-indictment calls; calls within 30 days of trial are top of stack
2. **Recipient category** — co-defendants > State's witnesses > victim's family > defendant's family with witness overlap > defendant's family without witness overlap > attorney lines (Module F only) > commercial (bondsman, bail, commissary)
3. **Duration outliers** — both very short (< 90s) and at-system-max calls
4. **Time-of-day outliers** — late-night calls correlate with emotional content and admissions

### Triage Output

Module A must produce a **Triage Roster** spreadsheet appendix to the audit:

`Call ID | Date/Time | Duration | Recipient (name + category) | Vendor Flags | Tier (1/2/3) | Promotion Trigger (if any) | Reviewer Notes`

Every tier assignment must be defensible. Random-sample 5% of Tier 3 to confirm no false negatives — if the random sample surfaces a damaging admission, the triage thresholds were too coarse and Tier 2/3 must be re-cut.

# Module D — Credit-for-Time-Served and Street-Time Math

Every revocation memo states, in numbers, what the client actually serves under each outcome. Rules first, then a worked example. **All computations are drafts for attorney verification against DOC time-computation records — flag every output `[ATTORNEY TO VERIFY against DPS&C master record]`.**

## D-1. The rules

**Probation (full revocation — La. C.Cr.P. arts. 900/901, 880):**
- The suspended sentence becomes executory as originally imposed.
- **No credit** for time on probation (street time) or time elapsed during suspension (Art. 901).
- **Credit** for time in actual custody: pre-sentence custody on the original charge (Art. 880) and time held in actual custody on the probation violation — local, state, or out-of-state facility (Art. 901, referencing Art. 880).
- If revocation follows a new Louisiana conviction, the minutes must state concurrent vs. consecutive (Art. 901) — silence is a correction/negotiation point.

**Probation (technical revocation under Art. 900):** capped term (version-dependent — see the version table in `probation-revocation-framework.md`), served without diminution of sentence; credit for pre-hearing custody on the violation, but only on the first technical revocation [VERIFY — confirm current credit subsection]; then return to supervision.

**Parole (full revocation — La. R.S. 15:574.9):**
- The parolee serves the **remainder of the sentence**, administratively computed by DOC.
- **Street time:** treatment of time served in good standing on parole has changed across amendments — Justice-Reinvestment-era text granted credit for time on parole in good standing; post-2024 amendments must be version-checked before computing [VERIFY — confirm the current R.S. 15:574.9 credit-for-time-served provision for the client's governing version].
- **No credit for fugitive time** — any period the parolee was a fugitive from justice never counts toward the parole term.
- **Credit** for pre-hearing time in actual custody on the violation (local, state, or out-of-state facility).

**Parole (technical revocation):** capped term (currently 90/120/180 days by tier, treatment ≤ 180 days [VERIFY]; caps inapplicable to crime-of-violence and sex-offense parolees), running from the committee's revocation order, without diminution or pre-revocation credit [VERIFY — confirm credit language]; then return to active parole for the remainder of the original term.

**Both tracks:** custody on a new charge *and* the hold simultaneously — determine which docket the jail is booking the time against; jail-credit allocation errors are common and correctable. Good-time (diminution) eligibility on the revoked term is its own analysis — route computation to the good-time reference in `dw-sentencing-mitigation-specialist-crim` (`dw-sentencing-mitigation-specialist-crim/references/good-time-parole-eligibility.md`).

## D-2. Worked example (probation, full revocation)

Facts: Client sentenced 01/10/2024 to 5 years at hard labor, suspended, 3 years supervised probation, for an offense committed 06/15/2023. Pre-plea jail custody 08/01/2023–09/15/2023 (46 days). Art. 899 warrant issued 03/01/2026; arrested on the warrant 03/10/2026; held continuously until the revocation hearing 05/08/2026 (60 days). Court revokes and executes the 5-year sentence.

| Component | Days | Rule |
|---|---|---|
| Face sentence | 5 years | Art. 900(A)(5) revocation executes the suspended sentence |
| Street time on probation 01/10/2024 → 03/10/2026 | **0 credit** | Art. 901 — no credit for time on probation |
| Pre-plea custody 08/01/2023–09/15/2023 | **46 days credit** | Art. 880 |
| Violation-hold custody 03/10/2026–05/08/2026 | **60 days credit** | Art. 901 / Art. 880 |
| **Net to serve** | 5 years − 106 days, less any good-time diminution | `[ATTORNEY TO VERIFY against DPS&C master record]` |

Contrast line for the memo: had the same violation been classified **technical** (first tier, current law), exposure would be ≤ 90 days [VERIFY per version table] with the 60 hold days credited on a first technical revocation [VERIFY] — i.e., ≤ ~30 additional days vs. ~4.7 years. That contrast is the classification fight's value, stated in numbers.

## D-3. Worked example (parole variant, sketch)

Same client paroled 01/10/2024 with 5 years remaining; hold lodged 03/10/2026; committee revokes (non-technical) 05/08/2026. Remainder computed by DOC from the release date; whether the 26 months of good-standing street time credits against the remainder is **version-dependent** [VERIFY — confirm current 574.9 street-time rule]; the 60 hold days credit as actual custody; any fugitive period is excluded from the parole term entirely. Present both computations (with and without street-time credit) until the attorney confirms the governing version.

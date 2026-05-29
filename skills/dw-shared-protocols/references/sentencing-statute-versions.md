# Sentencing Statute Versions — Offense-Date-Driven Selection

**Shared reference for `dw-sentencing-mitigation-specialist`, `dw-plea-negotiation-analyzer`, and `dw-habitual-offender-auditor`.**

> ⚠️ **STATUS: SCAFFOLD — VALUES UNVERIFIED.** Every value cell below is `[VERIFY CITATION]` until populated from authoritative research (dw-case-law-researcher / Westlaw / the statute) **and** confirmed by the attorney. Do not present any figure here as established law until it is verified. This file exists to fix the contradictions catalogued in `docs/SENTENCING_LAW_DISCREPANCIES_2026-05-29.md`.

---

## THE RULE — applicable version is fixed by the DATE OF OFFENSE

Louisiana's habitual-offender, good-time, and parole statutes were amended repeatedly (the 2017 Justice Reinvestment package and subsequent changes). **The version that governs a case is the one in effect on the date the current offense was committed** — not the conviction date, not the sentencing date.

**Mandatory procedure before ANY exposure calculation:**

1. **Confirm the date of offense (per count)** with the attorney. Do not compute habitual-offender enhancement, good-time, or parole-eligibility exposure until the offense date is confirmed.
2. **Select the applicable version** for each statute from its effective-date range below.
3. **Apply only that version's values**, and **cite the version** (statute + effective-date range) in the output.
4. If the offense date is unknown or straddles an amendment, present the exposure under **each candidate version** and flag the dependency for the attorney to resolve.

---

## La. R.S. 15:529.1 — Habitual Offender Law

*Contested values to resolve (per the discrepancy report): 3rd-offender-with-violence floor (½ vs ⅔); 4th-offender non-violent floor (longest term vs 20 yrs) and ceiling (life vs 2×); 4th-offender mandatory-LWOP trigger (one violent vs two-or-more).*

| Version | Effective-date range | 2nd offender | 3rd (no violence) | 3rd (with violence) | 4th (no violence) | 4th (with violence — LWOP trigger) | Authority |
|---|---|---|---|---|---|---|---|
| **V1 (oldest of last 3)** | `[VERIFY]` | `[VERIFY]` | `[VERIFY]` | `[VERIFY]` | `[VERIFY]` | `[VERIFY]` | `[VERIFY: Act/cite]` |
| **V2 (interim)** | `[VERIFY]` | `[VERIFY]` | `[VERIFY]` | `[VERIFY]` | `[VERIFY]` | `[VERIFY]` | `[VERIFY: Act/cite]` |
| **V3 (current)** | `[VERIFY]` | `[VERIFY]` | `[VERIFY]` | `[VERIFY]` | `[VERIFY]` | `[VERIFY]` | `[VERIFY: Act/cite]` |

Cleansing period (`15:529.1(C)`): `[VERIFY — value + whether it varies by version]`.

---

## La. R.S. 15:571.3 — Diminution of Sentence (Good Time)

*Contested values to resolve: crime-of-violence good-time eligibility; non-violent earning rate (e.g., "13 days per 7 served / ~35%"); which date governs the rate (offense vs conviction — THE RULE above says offense date).*

| Version | Effective-date range | Non-violent earning rate | Crime-of-violence eligibility | Sex-offense eligibility | Authority |
|---|---|---|---|---|---|
| **V1** | `[VERIFY]` | `[VERIFY]` | `[VERIFY]` | `[VERIFY]` | `[VERIFY: Act/cite]` |
| **V2** | `[VERIFY]` | `[VERIFY]` | `[VERIFY]` | `[VERIFY]` | `[VERIFY: Act/cite]` |
| **V3 (current)** | `[VERIFY]` | `[VERIFY]` | `[VERIFY]` | `[VERIFY]` | `[VERIFY: Act/cite]` |

---

## La. R.S. 15:574.4 — Parole Eligibility

*Contested values to resolve: crime-of-violence parole-eligibility % (65/75% vs 85%); non-violent formulation (25% vs ⅓-or-25%-whichever-longer).*

| Version | Effective-date range | Non-violent | Crime of violence (1st) | Crime of violence (2nd) | Authority |
|---|---|---|---|---|---|
| **V1** | `[VERIFY]` | `[VERIFY]` | `[VERIFY]` | `[VERIFY]` | `[VERIFY: Act/cite]` |
| **V2** | `[VERIFY]` | `[VERIFY]` | `[VERIFY]` | `[VERIFY]` | `[VERIFY: Act/cite]` |
| **V3 (current)** | `[VERIFY]` | `[VERIFY]` | `[VERIFY]` | `[VERIFY]` | `[VERIFY: Act/cite]` |

---

## Maintenance

- When an amendment takes effect, **add the new version as V3 (current) and drop the oldest** — keep the last 3 so straddle/older-offense cases remain computable.
- Every value must carry a verifiable citation; never fabricate. Attorney confirms before any version goes live.
- Skills consuming this file: list above. When a value changes here, the consumers automatically inherit it (single source of truth).

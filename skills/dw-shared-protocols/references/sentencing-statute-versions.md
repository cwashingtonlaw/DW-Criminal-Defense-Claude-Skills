# Sentencing Statute Versions — Offense-Date-Driven Selection

**Shared reference for `dw-sentencing-mitigation-specialist`, `dw-plea-negotiation-analyzer`, and `dw-habitual-offender-auditor`.**

> **STATUS:** Current (V3) values below are sourced from the **official Louisiana State Legislature text (legis.la.gov)** as of 2026-05-29 — high confidence, but **eyeball the official statute before filing-grade reliance** (see `docs/SENTENCING_LAW_RESEARCH_2026-05-29.md`). **Prior-version values are flagged `[VERIFY — Westlaw]`** — confirm exact historical text and effective-date boundaries via Westlaw's statute version-compare before relying on them for an older-offense case.

---

## THE RULE — applicable version is fixed by the DATE OF OFFENSE

These statutes were amended repeatedly (2017 Justice Reinvestment; 2024 2nd Ex. Sess.; 2025). **The version that governs is the one in effect on the date the current offense was committed** — not the conviction or sentencing date.

**Mandatory procedure before ANY exposure calculation:**
1. **Confirm the date of offense (per count).**
2. **Select the applicable version** for each statute from the effective-date markers below.
3. **Apply only that version's values and cite the version** (statute + effective date) in the output.
4. If the offense date is unknown or straddles an amendment, present exposure under **each candidate version** and flag the dependency for the attorney.

Key effective-date boundaries: **Nov. 1, 2017** (2017 reforms — habitual minimums lowered, CoV parole set to 65%/75%); **Aug. 1, 2024** (good time abolished except per 15:571.3.1); plus **Aug. 1, 2014** (a CoV/sex parole carve-out).

---

## La. R.S. 15:529.1 — Habitual Offender
Source: legis.la.gov `Law.aspx?d=79154`. Credit line: Acts 2017, Nos. 257 & 282 (eff. 11/1/2017); Acts 2024, 2nd Ex. Sess., No. 4 (eff. 7/1/2024); Acts 2025, No. 246.

### V3 — CURRENT (offenses on/after Nov. 1, 2017, as amended through 2025)
| Tier | Value |
|---|---|
| 2nd offender | not less than **⅓** the longest term, not more than 2× the longest |
| 3rd offender (non-life) | not less than **½** the longest possible sentence, not more than 2× |
| 3rd → mandatory **life w/o benefits** | if the 3rd felony **and the two prior felonies** are all crimes of violence (R.S. 14:2(B)) or sex offenses (R.S. 15:541, victim under 18), or any combination |
| 4th+ offender (non-life) | not less than the **longest prescribed** for a first conviction, **but in no event less than 20 years**; not more than **natural life** |
| 4th → mandatory **life w/o benefits** | if the 4th felony **and two of the prior felonies** are crimes of violence or sex offenses (victim under 18) |
| Cleansing period (subsec. C) | **5 years**; **10 years** if the current or a prior offense is a crime of violence/sex offense; incarceration & supervision time excluded |

### V2 / V1 — PRIOR VERSIONS `[VERIFY — Westlaw]`
- **Pre-Nov. 1, 2017 (characterized; confirm verbatim):** 2nd offender floor **½** (not ⅓); 3rd offender floor **⅔** (not ½); LWOP triggers and 4th-offender floor/ceiling may differ — **do not rely until version-compared in Westlaw.**

---

## La. R.S. 15:574.4 — Parole Eligibility
Source: legis.la.gov `Law.aspx?d=79239`. Credit line: Acts 2017, No. 280 (eff. 11/1/2017); Acts 2024, 2nd Ex. Sess., No. 6; Acts 2024, No. 576; Acts 2025, No. 158 (eff. 6/8/2025).

### V3 — CURRENT
| Category | % to serve | Applies to |
|---|---|---|
| Non-violent / general | **25%** | offenses **before Aug. 1, 2024** |
| Crime of violence — 1st (no prior violent/sex) | **65%** | offenses committed (or P/P revoked) **on/after Nov. 1, 2017** |
| Crime of violence — 2nd | **75%** | same |
| Crime of violence — 3rd+ | **ineligible** | same |

### V1 — PRIOR `[VERIFY — Westlaw]`
- **Pre-Nov. 1, 2017:** crime-of-violence parole eligibility was **85%** (characterized; confirm verbatim + exact boundary).

---

## La. R.S. 15:571.3 — Good Time / Diminution
Source: legis.la.gov `Law.aspx?d=79190`; see also **15:571.3.1**. Credit line: Acts 2024, 2nd Ex. Sess., Nos. 7 & 21; Acts 2025, No. 158 (eff. 6/8/2025).

### V3 — CURRENT (governed by DATE OF OFFENSE)
| Offense date | Rule |
|---|---|
| **On/after Aug. 1, 2024** | **No good time** at all, except as provided in **R.S. 15:571.3.1** (subsec. H) |
| **Before Aug. 1, 2024** | Non-violent: **13 days per 7 days** in custody. 1st crime of violence (no prior CoV/sex): **1 day per 3 days.** Excluded entirely: 2nd+ crime of violence, 4th+ nonviolent felony, habitual offender (15:529.1), sex offense |

### V1 — PRIOR `[VERIFY — Westlaw]`
- Earlier diminution rates/eligibility predating the 2024 changes — confirm verbatim if the offense predates the current regime.

---

## Maintenance
- When an amendment takes effect, **add the new version and drop the oldest** — keep ~3 so straddle/older-offense cases stay computable.
- Every value must carry a verifiable citation; never fabricate. The attorney confirms before any value is relied on for filing.
- Skills consuming this file inherit changes automatically (single source of truth).

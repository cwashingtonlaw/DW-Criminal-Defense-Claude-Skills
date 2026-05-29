# Legal Research Memo — Sentencing-Statute Versions (15:529.1 / 15:571.3 / 15:574.4)

**ATTORNEY WORK PRODUCT — PRIVILEGED. Internal use; verify against the official statute before filing-grade reliance.**

**Date:** 2026-05-29 · **Researched by:** Cowork (`dw-case-law-researcher`) · **For:** populating `dw-shared-protocols/references/sentencing-statute-versions.md` and resolving `docs/SENTENCING_LAW_DISCREPANCIES_2026-05-29.md`
**Sources consulted:** official Louisiana State Legislature statute text (legis.la.gov) + WebSearch corroboration (Justia/FindLaw snapshots). CourtListener MCP and Westlaw were unavailable in this environment; **historical (V1/V2) verbatim text still needs your Westlaw version-compare.**

---

## Short answer

Every contradiction traces to **stale statutory vintages**. The 2017 Justice Reinvestment reforms (and 2024 changes) lowered the habitual-offender minimums and parole percentages and made good-time **offense-date-keyed**. Current law largely matches the **plea-analyzer** skill on the habitual LWOP trigger and the **sentencing** skill on parole %, while *all three* skills are stale on the 2nd-offender floor. The applicable version is fixed by the **date of offense**.

---

## 1. La. R.S. 15:529.1 — Habitual Offender *(current text)*

Source: legis.la.gov `LawPrint.aspx?d=79154`. Amendment credit line: **Acts 2017, Nos. 257 & 282 (eff. Nov. 1, 2017); Acts 2024, 2nd Ex. Sess., No. 4 (eff. July 1, 2024); Acts 2025, No. 246.**

| Tier | Current value (verbatim/near-verbatim) |
|---|---|
| 2nd offender | not less than **⅓** the longest term, not more than 2× the longest term |
| 3rd offender (non-life) | not less than **½** the longest possible sentence, not more than 2× |
| 3rd → mandatory **life w/o benefits** | if the 3rd felony **and the two priors** are all crimes of violence (14:2(B)) or sex offenses (15:541, victim under 18), or any combination |
| 4th offender (non-life) | not less than the **longest prescribed** for a first conviction, **but in no event less than 20 years**, and not more than **natural life** |
| 4th → mandatory **life w/o benefits** | if the 4th felony **and two of the prior felonies** are crimes of violence or sex offenses (victim under 18) |
| Cleansing period (C) | **5 years** generally; **10 years** if the current or a prior offense is a crime of violence/sex offense; incarceration & supervision time excluded |

**Resolves the discrepancy report:**
- 2.4 (LWOP trigger): current = **"two of the prior felonies"** → **plea skill (E) was right; the dedicated habitual skill (C) "one" is WRONG/stale.** ⚠️ correctness fix needed.
- 2.2 / 2.3 (4th floor/ceiling): current = "longest prescribed **but ≥ 20 yrs**" → natural life — the "longest term" (C) and "20 years" (D/E) were each *half* the rule; D's "2× max" ceiling is stale.
- 2.1 (3rd floor): current general 3rd = **½**; the **⅔** in D/E is the pre-2017 vintage. (3rd all-violent = life.)
- **New:** 2nd-offender floor is now **⅓** — *all three skills say ½*, which is the pre-2017 vintage. Stale across the board.

---

## 2. La. R.S. 15:574.4 — Parole Eligibility *(current text)*

Source: legis.la.gov `LawPrint.aspx?d=79239`. Amendment credit line: **Acts 2017, No. 280 (eff. Nov. 1, 2017); Acts 2024, 2nd Ex. Sess., No. 6; Acts 2024, No. 576; Acts 2025, No. 158 (eff. June 8, 2025).**

| Category | Current % | Offense-date condition |
|---|---|---|
| Non-violent / general | **25%** | applies to offenses **before Aug. 1, 2024** |
| Crime of violence, 1st (no prior violent/sex) | **65%** | applies to offenses committed (or P/P revoked) **on or after Nov. 1, 2017** |
| Crime of violence, 2nd | **75%** | same |
| Crime of violence, 3rd+ | **ineligible** | same |

**Resolves discrepancy 1.1:** current CoV eligibility is **65% / 75%** → **sentencing skill (A) was right; plea skill (B) "85%" is the pre-Nov-1-2017 vintage.**

---

## 3. La. R.S. 15:571.3 — Good Time / Diminution *(current text)*

Source: legis.la.gov `LawPrint.aspx?d=79190`. Amendment credit line: **Acts 2024, 2nd Ex. Sess., Nos. 7 & 21; Acts 2025, No. 158 (eff. June 8, 2025).** See also **15:571.3.1** (offenses on/after Aug. 1, 2024).

- **Offenses on/after Aug. 1, 2024:** **no good time** at all, except as provided in 15:571.3.1 (subsec. H).
- **Earlier offenses:** non-violent = **13 days per 7 days** in custody; 1st crime of violence (no prior CoV/sex) = **1 day per 3 days**.
- **Excluded entirely:** 2nd+ crime of violence, 4th+ nonviolent felony, habitual offender (15:529.1), sex offense.

**Resolves discrepancies 1.2 & 1.3:**
- Governing date = **DATE OF OFFENSE** ("commits an offense on or after…") → **plea skill (offense date) right; sentencing skill ("conviction date") wrong.**
- Non-violent rate **13/7 (~35%)** → confirms the sentencing skill's figure for pre-Aug-2024 offenses.

---

## Version-history narrative (the "last 3 versions" framing)

- **Most recent wave (2024–2025):** 2024 2nd Ex. Sess. (good-time abolished for offenses on/after 8/1/2024 except per 571.3.1; habitual & parole tweaks) + 2025 amendments.
- **2017 Justice Reinvestment (eff. Nov. 1, 2017 — Acts 257/280/282):** lowered habitual minimums (2nd → ⅓, 3rd → ½), set CoV parole at 65%/75%, narrowed cleansing periods.
- **Pre-2017 vintage:** the higher figures the skills froze at — 2nd/3rd habitual ½/⅔, CoV parole **85%**.

---

## Flags

- `[VERIFIED — official source]` All **current** values above are from legis.la.gov (the authoritative source). **Eyeball the official text before filing-grade reliance** — WebFetch extraction can miss sub-clauses.
- `[VERIFY — Westlaw version-compare]` **Exact verbatim V1/V2 (historical) text** was not independently retrieved (Justia year-snapshots were 403-blocked here). The pre-2017 / interim values are characterized from the amendment history + secondary sources; confirm exact prior-version language via Westlaw's statute version-compare before locking V1/V2 into the reference.
- `[CORRECTNESS — fix]` Two stale-law bugs to correct in the skills regardless of versioning: (a) `dw-habitual-offender-auditor` module-e 4th-offender LWOP trigger says **"one"** — current law requires **"two of the prior felonies"**; (b) **all three skills** state the 2nd-offender floor as **½** — current is **⅓**.
- `[OFFENSE-DATE] ` Multiple provisions are expressly keyed to offense date (8/1/2014, 11/1/2017, 8/1/2024) — the offense-date gate added in commit `1baa90f` is essential to selecting correctly.

---

## Recommended next step

On your confirmation, I'll populate `sentencing-statute-versions.md`: **V3 (current)** from the official values above, **V2 (2017 wave)** and **V1 (pre-2017)** flagged `[VERIFY — Westlaw]` until you version-compare. Then I'll fix the two correctness bugs in the skills. **Nothing goes live as authoritative until you confirm.**

**Sources:** [LA Legislature 15:529.1](https://legis.la.gov/Legis/Law.aspx?d=79154) · [15:574.4](https://legis.la.gov/Legis/Law.aspx?d=79239) · [15:571.3](https://legis.la.gov/legis/Law.aspx?d=79190) · [15:571.3.1 (Justia 2025)](https://law.justia.com/codes/louisiana/revised-statutes/title-15/rs-15-571-3-1/) · 2017 Acts 257/280/282; 2024 2nd Ex. Sess. Acts 4/6/7/21; 2025 Acts 158/246.

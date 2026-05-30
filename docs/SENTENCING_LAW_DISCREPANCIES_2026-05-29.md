# Sentencing-Law Discrepancy Report — Good-Time / Parole & Habitual Offender

**Date:** 2026-05-29
**Author:** Cowork (skill-collection audit, P3 hoist #2)
**Status:** ⚠️ ATTORNEY VERIFICATION REQUIRED — do not rely on any value below until confirmed against the current statute for the client's offense date.

---

## Why this report exists

While attempting to de-duplicate the shared "sentencing-exposure" math across three skills, the copies were found to **state Louisiana law differently**. Because R.S. 15:529.1, 15:571.3, and 15:574.4 were each amended several times (notably the 2017 Justice Reinvestment package and subsequent 2018/2021 changes), the divergent copies most likely reflect **different statutory vintages that were never reconciled**. The correct value in each cell is **offense-date-dependent** and must be verified against the version of the statute in effect on the date of the client's current offense.

This is a **correctness issue independent of de-duplication**: the three skills can hand an attorney different sentencing-exposure numbers — including a different answer to *when mandatory life-without-parole attaches*. The de-duplication itself is paused until the law is verified; House Rule #1 forbids selecting an unverified value.

**Skills affected:** `dw-sentencing-mitigation-specialist-crim`, `dw-plea-negotiation-analyzer-crim`, `dw-habitual-offender-auditor-crim`.

---

## Engine 1 — Good-time / parole eligibility

- **Source A:** `skills/dw-sentencing-mitigation-specialist-crim/references/good-time-parole-eligibility.md`
- **Source B:** `skills/dw-plea-negotiation-analyzer-crim/references/module-c-good-time-calculator.md`

| # | Issue | Source A says | Source B says | Conflict |
|---|-------|---------------|---------------|----------|
| 1 | **Crime-of-violence parole eligibility %** | **65%** (1st offense), **75%** (2nd) — A:42–43, cites 15:574.4(A)(1) & (B)(1) | **85%** for crimes of violence — B:10, B:15, cites 15:574.4(B) | ✗ Materially different thresholds |
| 2 | **Which date governs the good-time rate** | **Date of conviction** ("the conviction date (not offense date) determines the applicable rate") — A:16 | **Date of offense** ("depends on the date of offense, not the date of sentencing") — B:70 | ✗ Direct conflict (conviction vs. offense) |
| 3 | Non-violent good-time effective rate | "13 days per 7 served → serve ~35%" (post-8/1/2020) — A:9 | No specific rate; defers to 15:571.3 generally — B:9 | ~ A is more specific; verify the 35% figure and its effective date |
| 4 | Non-violent parole eligibility | 25% of sentence — A:40–41 | "one-third, or 25%, whichever is longer" — B:14 | ~ B adds a "whichever is longer" nuance A omits; confirm which controls |

**To verify:** current text of **La. R.S. 15:574.4** (parole eligibility %s for crimes of violence, by offense date) and **La. R.S. 15:571.3** (good-time / diminution rate and the governing-date rule).

---

## Engine 2 — Habitual offender (La. R.S. 15:529.1)

- **Source C:** `skills/dw-habitual-offender-auditor-crim/references/module-e-enhancement-tier.md` *(the dedicated habitual-offender skill — presumptive canonical owner, but its values still require verification)*
- **Source D:** `skills/dw-sentencing-mitigation-specialist-crim/references/habitual-offender-reference.md`
- **Source E:** `skills/dw-plea-negotiation-analyzer-crim/references/module-h-habitual-offender-leverage.md`

| # | Tier | Source C (module-e) | Source D (sentencing) | Source E (plea) | Conflict |
|---|------|---------------------|-----------------------|-----------------|----------|
| 1 | **2nd offender — range** | ½ to 2× longest (C:9) | ½ to 2× (D:37) | ½ to 2× (E:10) | ✓ **All agree** |
| 2 | **3rd offender, *with* violence — floor** | **½** longest, w/o benefits — C:11, cites (A)(1)(b)(ii) | not broken out (generic 3rd = ⅔, D:38) | **⅔** longest, w/o benefits — E:13 | ✗ ½ vs ⅔ |
| 3 | **4th offender, non-violent — floor** | **longest prescribed term** — C:12 | **20 years** — D:39 | **20 years** — E:12 | ✗ "longest term" vs "20 years" |
| 4 | **4th offender, non-violent — ceiling** | **natural life** — C:12 | **2× max** — D:39 | **natural life** — E:12 | ✗ life vs 2× max |
| 5 | **Mandatory LWOP trigger (4th, violent)** | **one** crime of violence (predicate *or* current) — C:13, (A)(1)(c)(ii) | "violent / sex" (count unspecified) — D:40 | **two or more** prior crimes of violence/sex — E:14 | ✗ one vs. two-or-more — *changes when LWOP attaches* |

**To verify:** current text of **La. R.S. 15:529.1(A)** (enhancement tiers and floors/ceilings) and the LWOP-trigger subsection, **for the offense date applicable to the client**. Note the 2017 reforms reduced several minimums and narrowed the LWOP trigger; whether a given client gets the pre- or post-reform tier depends on offense date and the *Williams*/savings-clause analysis.

---

## Recommended resolution path

1. **Verify** the correct current values for each contested cell against Westlaw / the current statute (consider `dw-case-law-researcher-crim`), keyed to offense date.
2. **Designate one canonical reference per engine** — the natural owners are `dw-habitual-offender-auditor-crim` (529.1) and a good-time reference under `dw-shared-protocols-crim/references/` (parole/good-time). Correct the values there, with any version-dependent value clearly labeled by offense-date regime.
3. **Repoint** `dw-sentencing-mitigation-specialist-crim` (Module A inline habitual block + Module E good-time; remove its `habitual-offender-reference.md` once folded) and `dw-plea-negotiation-analyzer-crim` (module-c, module-h) at the canonical references. *This is the de-duplication step — safe only after the law is verified.*
4. **Then** the original P3 hoist #2 can complete with confidence.

Until step 1 is done, treat the contradictions above as open issues. Every value in the affected skills that touches these tiers should be regarded as `[VERIFY CITATION]`.

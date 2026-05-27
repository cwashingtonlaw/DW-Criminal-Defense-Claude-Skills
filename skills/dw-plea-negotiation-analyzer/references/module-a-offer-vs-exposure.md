# Module A — Offer vs. Exposure Analysis

## Purpose

Compare the specific plea offer against the full range of sentencing exposure at trial, including mandatory minimums, sentencing guidelines ranges, habitual offender enhancements, and consecutive vs. concurrent sentence stacking.

## Legal Framework

- **La. C.Cr.P. Art. 551-562** — Governing provisions for pleas in Louisiana criminal proceedings.
- **La. C.Cr.P. Art. 552** — A plea of guilty is the defendant's formal admission in open court that the defendant committed the offense charged. The plea must be a free and voluntary choice by the defendant.
- **La. C.Cr.P. Art. 556** — Plea agreement procedures. The court is not bound by the terms of a plea agreement and must so inform the defendant. If the court rejects the agreement, the defendant shall be permitted to withdraw the plea.
- **La. C.Cr.P. Art. 556.1** — Before accepting a guilty plea, the court must personally address the defendant and inform them of the nature of the charge, the mandatory minimum and maximum sentences, the right to a jury trial, the right to confront and cross-examine witnesses, the right against self-incrimination, and that by pleading guilty the defendant waives these rights. See Boykin v. Alabama, 395 U.S. 238 (1969).
- **La. R.S. 15:529.1** — Habitual Offender Law. Provides for enhanced sentences based on prior felony convictions. Second felony offender: not less than one-half the longest term nor more than twice the longest term. Third felony offender: not less than two-thirds the longest term nor more than twice the longest term. Fourth felony offender (or second/third with enumerated violent offenses): 20 years to life, depending on predicate configuration.
- **State v. Dorthey, 623 So.2d 1276 (La. 1993)** — Habitual offender sentence must not be constitutionally excessive; downward departure available if trial court finds sentence would be grossly disproportionate.

## Analysis Template

Generate a comparison table:

| Factor | Plea Offer | Trial Exposure (Conviction on All Counts) | Trial Exposure (Most Likely Conviction Scenario) |
|---|---|---|---|
| Charge(s) of conviction | [Reduced charge if applicable] | [All charged offenses] | [Most probable verdict based on evidence] |
| Statutory sentencing range | [Range for plea charge] | [Range per count — identify mandatory minimums] | [Range for likely conviction charges] |
| Habitual offender exposure | [Is habitual bill waived as part of plea?] | [Enhanced range under 529.1 if bill is filed] | [Probability of habitual adjudication] |
| Recommended sentence in offer | [Specific sentence offered] | [N/A — judge discretion at trial] | [Estimated sentence based on comparable cases] |
| Consecutive vs. concurrent | [Plea terms] | [Risk of consecutive sentences on multiple counts] | [Likely stacking approach] |
| Probation / suspension available? | [Per plea terms] | [Statutory eligibility post-trial] | [Realistic probability] |
| Restitution | [Plea terms] | [Potential restitution at trial] | [Likely amount] |
| Special conditions | [Plea conditions — treatment, community service, etc.] | [Potential conditions post-trial] | [Likely conditions] |

## Offer Discount Calculation

Calculate the "plea discount" — the percentage reduction from maximum trial exposure:

```
Plea Discount = ((Maximum Trial Exposure - Plea Offer Sentence) / Maximum Trial Exposure) x 100
```

Provide context: What does this discount tell us about the strength of the State's case? A generous offer may signal evidentiary weakness. A stingy offer may signal confidence. Neither inference is conclusive standing alone.

## Risk-Adjusted Analysis

Estimate the expected value of going to trial using the following framework:

```
Expected Trial Outcome = (P(acquittal) x 0) + (P(conviction_lesser) x Sentence_lesser) + (P(conviction_charged) x Sentence_charged) + (P(conviction_charged + habitual) x Sentence_enhanced)
```

Where each probability is a counsel-informed estimate based on evidence strength. Flag that these are estimates, not predictions. Every trial carries uncertainty.

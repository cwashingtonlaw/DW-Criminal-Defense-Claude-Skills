# Module H — Habitual Offender Leverage Analysis

## Purpose

Analyze how Louisiana's Habitual Offender Law (La. R.S. 15:529.1) affects the plea negotiation dynamics. The habitual offender bill is one of the most powerful tools in the State's arsenal and one of the most important variables in plea strategy.

## Legal Framework

> ⚠️ **Offense-date note:** The applicable version of La. R.S. 15:529.1 is fixed by the **date of offense** — confirm it first and select the version per `dw-shared-protocols-crim/references/sentencing-statute-versions.md`. The figures below reflect current law (offenses on/after Nov. 1, 2017); pre-2017 vintages differ (verify via Westlaw).

- **La. R.S. 15:529.1(A)** — Enhanced sentencing provisions:
  - **Second felony offender:** Not less than one-third the longest term nor more than twice the longest term prescribed for the first conviction *(current — offenses on/after Nov. 1, 2017; pre-2017 used one-half)*.
  - **Third felony offender:** Not less than two-thirds the longest term nor more than twice the longest term prescribed for the first conviction.
  - **Fourth felony offender (non-violent predicates):** Not less than 20 years nor more than the defendant's natural life.
  - **Third felony offender with one prior crime of violence or sex offense:** Not less than two-thirds the longest term nor more than twice the longest term, served without benefit of probation, parole, or suspension.
  - **Fourth felony offender with two or more prior crimes of violence or sex offenses:** Imprisonment for the defendant's natural life without benefit of probation, parole, or suspension.

- **La. R.S. 15:529.1(C)** — Cleansing period. If more than 10 years have elapsed since the completion of the sentence for the prior felony (or felonies), the prior conviction shall not be counted. "Completion of sentence" includes incarceration, parole, probation, and suspended sentence.

- **La. R.S. 15:529.1(D)** — Procedural requirements for habitual offender adjudication. State must file a bill of information alleging prior convictions. Defendant has the right to a hearing. State bears the burden of proof.

- **State v. Shelton, 621 So.2d 769 (La. 1993)** — State must prove: (1) identity of the defendant as the person previously convicted, and (2) the prior conviction(s) — typically through certified copies of conviction records, prison records, and fingerprint evidence.

- **State v. Dorthey, 623 So.2d 1276 (La. 1993)** — Court may depart downward from mandatory habitual offender minimum if the sentence would be "constitutionally excessive" — i.e., grossly out of proportion to the severity of the offense, making the sentence nothing more than a purposeless imposition of pain and suffering.

- **State v. Johnson, 97-1906 (La. 3/4/98), 709 So.2d 672** — Clarified Dorthey: departure requires particularized showing that the defendant is exceptional, justifying different treatment from other habitual offenders; mere claim that sentence is too harsh is insufficient.

## Habitual Offender Exposure Calculation

| Component | Analysis |
|---|---|
| Current offense | [Charge and maximum sentence prescribed by statute] |
| Number of qualifying prior felony convictions | [List each — charge, date, jurisdiction, sentence, completion date] |
| Cleansing period analysis for each prior | [Has 10+ years elapsed since completion of sentence? Calculate for each prior.] |
| Habitual offender classification | [Second / Third / Fourth felony offender] |
| Crimes of violence among predicates | [Identify any La. R.S. 14:2(B) offenses — this affects the enhancement tier] |
| Enhanced sentencing range | [Calculate minimum and maximum under 529.1(A)] |
| Benefit restrictions on enhanced sentence | [Without probation? Without parole? Without suspension?] |
| Dorthey departure viability | [Is there a particularized basis for constitutional excessiveness argument?] |

## Leverage Analysis

| Question | Analysis |
|---|---|
| Has the State filed a habitual bill? | [Filed / Threatened / Not yet raised] |
| Is the habitual bill a negotiation tool? | [Is the ADA using the threat of habitual adjudication to pressure a plea? Is waiver of the habitual bill part of the plea offer?] |
| What is the differential between the plea offer and habitual-enhanced exposure? | [Calculate — this is the "habitual tax" the client avoids by pleading] |
| Are the predicate convictions vulnerable to challenge? | [Were prior pleas Boykin-compliant? Are certified records available? Can identity be contested?] |
| Is the cleansing period argument available? | [Calculate from completion of each prior sentence] |
| Is a Dorthey/Johnson departure realistic? | [What particularized facts support departure?] |

## Strategic Considerations

1. **Habitual bill as leverage.** In many Louisiana parishes, the habitual bill is the single most important lever in plea negotiations. Counsel should assess whether the ADA is using the bill as genuine prosecutorial policy or as a negotiation tactic.

2. **Attacking predicate convictions.** Prior convictions used as predicates can be challenged if: (a) the prior guilty plea was not Boykin-compliant; (b) the prior conviction has been reversed, vacated, or set aside; (c) the prior was not a "conviction" under 529.1 (e.g., a federal pretrial diversion or a misdemeanor that does not qualify); (d) identity evidence is insufficient.

3. **Timing of habitual bill filing.** Under La. R.S. 15:529.1(D), the bill can be filed at any time — before or after trial, and even after sentencing on the underlying offense. This means the habitual threat may persist even through trial.

4. **Impact on plea negotiation strategy.** If the habitual bill exposure is severe (e.g., life without parole for a fourth felony offender with violent predicates), a plea offer that avoids habitual adjudication has enormous value even if the base sentence is substantial. Counsel must help the client understand this differential.

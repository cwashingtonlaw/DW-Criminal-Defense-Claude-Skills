# Immigration-Consequences Classification (Framework)

Use this to categorize each charge and compose advisement point 2 (the charge-classification
paragraph) and to set the generator's `conditional_flags`. This is a FRAMEWORK, not a
determination — immigration categorization frequently turns on the exact record of conviction and
the categorical / modified-categorical approach. **When the outcome is not clearly established,
write "[REQUIRES VERIFICATION BY IMMIGRATION COUNSEL]" and advise that removal "may" result.
When the outcome is clear (e.g., a listed aggravated felony), state it plainly** — *Padilla* requires
correct, non-equivocal advice where the consequence is clear.

This skill warns the client; it does not decide eligibility. Always route the actual determination
to immigration counsel.

## The two master grounds
- **Deportability** — for a person already admitted: INA § 237 / 8 U.S.C. § 1227.
- **Inadmissibility** — for admission, adjustment, re-entry, most relief: INA § 212 / 8 U.S.C. § 1182.
A single conviction can trigger both.

## Categories and governing cites
| Category | Core cite | Effect to convey |
|---|---|---|
| **Aggravated felony** | 8 U.S.C. § 1101(a)(43); deportable under § 1227(a)(2)(A)(iii) | Near-certain removal; **permanent** inadmissibility; bars cancellation, asylum (particularly serious crime), voluntary departure, and naturalization; mandatory detention. The most severe bucket. |
| **Crime involving moral turpitude (CIMT)** | Deportable § 1227(a)(2)(A)(i)-(ii); inadmissible § 1182(a)(2)(A)(i)(I) | Deportability (esp. within 5 yrs of admission, or 2+ CIMTs); inadmissibility; may bar relief. |
| **Controlled-substance offense** | Deportable § 1227(a)(2)(B); inadmissible § 1182(a)(2)(A)(i)(II) | Deportable + inadmissible (narrow exception: single simple possession ≤30g marijuana). Very hard to waive. Set flag `controlled_substance`. |
| **Firearm offense** | Deportable § 1227(a)(2)(C) | Deportable. Set flag `firearm`. |
| **Domestic violence / stalking / child abuse / protective-order violation** | Deportable § 1227(a)(2)(E) | Deportable. Set flag `domestic_violence`. |
| **Sex-offense registration** | Collateral (state SORNA/registry) + overlaps agg-felony/CIMT | Registration follows the client; compounds immigration/travel exposure. Set flag `sex_offense_registration`. |

## Aggravated-felony sub-categories most seen in Louisiana practice
8 U.S.C. § 1101(a)(43) is a long list. Common triggers:
- (A) **murder, rape, or sexual abuse of a minor** — e.g., La. R.S. 14:42/42.1/43 rape; 14:43.1
  sexual battery of a child; 14:81.2 molestation; 14:80/80.1 carnal knowledge — commonly "sexual
  abuse of a minor" and/or "rape."
- (B) drug trafficking (incl. many distribution/PWITD offenses).
- (F) **crime of violence** (18 U.S.C. § 16) with a term of imprisonment ≥ 1 year — e.g., many
  battery/assault/robbery/homicide offenses depending on the record and sentence.
- (G) theft or burglary with a term ≥ 1 year.
- (M) fraud/deceit with loss > $10,000; (J) certain firearm offenses; and others.
Sentence length and the statute of conviction matter — verify with immigration counsel.

## How to compose advisement point 2
Name the charge(s) with statute, then state the immigration classification(s) and the exact cite.
Example (aggravated felony, child sex offense):

> "The offenses charged in this case — First Degree Rape (La. R.S. 14:42) and Sexual Battery of a
> child under 13 (La. R.S. 14:43.1) — are classified under federal immigration law as 'aggravated
> felonies' (including 'rape' and 'sexual abuse of a minor,' 8 U.S.C. § 1101(a)(43)(A)), as
> 'crimes involving moral turpitude,' and as 'crimes of child abuse.'"

For bilingual mode, provide the same paragraph in Spanish, keeping "La. R.S." and "8 U.S.C." cites
in original form. If any classification is uncertain, insert the verification flag rather than
asserting it.

## Scope note
Immigration law changes and is fact-specific. This reference gives the standard statutory framework
only. It is not a substitute for a categorical-approach analysis by immigration counsel, which the
advisement itself directs the client to obtain.

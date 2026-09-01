# Post-Trial, Appeal, PCR & Habitual-Offender Clocks

**MODULES E–F working reference.** These are *defense-side* deadlines — the ones D&W can blow. Timing analysis only lives here; drafting of the underlying motions lives in `dw-pretrial-motion-library-crim` (post-trial motions), `dw-appellate-brief-builder-crim` (appeal), and `dw-post-conviction-relief-crim` (PCR).

---

## Motion for New Trial — Arts. 851 / 853

- **General rule (Art. 853):** the motion must be **filed and disposed of before sentence**.
- **New-and-material-evidence exception (Art. 851(B)(3) ground):** may be filed within **one year after verdict or judgment**, even though sentence has been imposed or a prior new-trial motion was filed. If an **appeal is pending**, the trial court may hear it **only on remand**.
- Ledger rows: (1) "MNT — general grounds" with expiry = sentencing date (render as event-bound, not date-certain, until sentencing is set); (2) "MNT — newly discovered evidence" with expiry = verdict date + 1 year.
- Court may postpone sentencing on defense motion for cause to allow preparation of the motion `[VERIFY CITATION — postponement window in Art. 853; older text allowed a postponement of up to thirty days — confirm current text]`.

## Post-Verdict Judgment of Acquittal — Art. 821

- Must be **made and disposed of before sentence**.
- Standard (for the attorney's context only): evidence viewed most favorably to the State does not reasonably permit a finding of guilt (*Jackson v. Virginia* sufficiency).
- Ledger row expiry = sentencing date (event-bound). Once sentence is imposed without the motion, mark EXPIRED-MOVE only if an out-of-time vehicle plausibly exists; otherwise SATISFIED/CLOSED with a note — attorney call.

## Arrest of Judgment — Arts. 859 / 861

- Grounds live in **Art. 859** (defects such as an indictment charging no offense, improper venue tried, double jeopardy, etc. — see article text for the exclusive list).
- **Timing (Art. 861):** must be **filed and disposed of before sentence**; the court may, on defense motion for cause shown, **postpone imposition of sentence** to allow preparation.
- Ledger row expiry = sentencing date (event-bound).

## Motion for Appeal — Art. 914

The motion for appeal (oral in open court, or written with the clerk) must be made no later than:

- **30 days** after the rendition of the judgment or ruling appealed from; **or**
- **30 days** from the ruling on a timely **motion to reconsider sentence** (Art. 881.1), if one is filed.

Interaction rule for the ledger: a timely Art. 881.1 motion **restarts** the appeal window from its ruling date — so the appeal row's Start Event is "later of judgment/sentencing or 881.1 ruling." The Art. 881.1 motion itself has its own deadline (**30 days of sentencing, or longer period set by the court at sentencing** `[VERIFY CITATION — confirm Art. 881.1(A) text]`) — give it its own row whenever sentencing has occurred.

Missed Art. 914 window → the conviction becomes final; the remaining vehicle is an out-of-time appeal via PCR (*State v. Counterman* procedure `[VERIFY CITATION — State v. Counterman, 475 So.2d 336 (La. 1985); attorney to confirm]`), which then collides with the Art. 930.8 clock below.

## Post-Conviction Relief — Art. 930.8

- **No PCR application — including one seeking an out-of-time appeal — shall be considered if filed more than 2 years after the judgment of conviction and sentence has become final** under Arts. 914 or 922.
- **Finality** runs through Art. 914 (no appeal taken → final when the appeal window lapses) or Art. 922 (appeal taken → finality after appellate/rehearing/writ delays run `[VERIFY CITATION — confirm the Art. 922 delay structure before computing a finality date]`).
- Statutory exceptions (facts not known despite diligence; retroactive new rule; others per current text) exist but are narrow — compute the hard 2-year date and let the attorney assess exceptions. The State can also assert **prejudicial delay** against even a timely application.
- Ledger rows: (1) "Finality date" (computed, with the 914/922 path shown); (2) "PCR prescription" = finality + 2 years.

## Habitual Offender Bill — La. R.S. 15:529.1 (no fixed prescription)

- The habitual-offender statute sets **no fixed deadline** for the State to file the multiple bill.
- Controlling doctrine: the bill must be filed **within a reasonable time** after the DA has the necessary information, grounded in Art. 874 ("sentence shall be imposed without unreasonable delay") and speedy-trial principles. Controlling case: *State v. Muhammad*, 2003-2991 (La. 5/25/04), 875 So.2d 45 `[VERIFY CITATION — attorney to Westlaw-check currency and subsequent treatment before relying]` — no bright-line rule; abusive or vindictive delay is not tolerated; delay chargeable to the State weighs toward dismissal.
- Ledger row: Status is never date-certain — render as **RUNNING (reasonable-time doctrine — no fixed expiry)** with the sentencing date, the date the State demonstrably had the prior-conviction packet (source it), and elapsed time. Long unexplained gaps → flag for `dw-habitual-offender-auditor-crim`.
- Offense-date discipline applies with force here: R.S. 15:529.1 is amended frequently and the version in effect on the **date of the underlying offense** controls the sentencing exposure — carry the statutory-version warning from the firm's sentencing protocol; never fabricate historical version values.

---

## Rendering rule for event-bound deadlines

Deadlines keyed to an event that has not happened (e.g., "before sentence") are rendered with Computed Expiry = the event name plus its currently scheduled date if one exists (`before sentencing — set 2026-10-02, minutes 9/1`), Status RUNNING. If the event is unscheduled, Computed Expiry = the event name and Status NEEDS-DATA.

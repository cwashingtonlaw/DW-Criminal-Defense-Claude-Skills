# Example Scenarios

## Scenario 1: Guilty Plea with Immediate Sentencing

1. Attorney triggers skill: "Close the case"
2. Confirms disposition: "Guilty Plea, sentenced today"
3. Skill records: Disposition date, sentence details (5 years hard labor, 10 years suspended, 5 years probation)
4. Skill calculates: Appeal deadline = 30 days from today
5. Runs billing generator: Captures all unbilled work
6. Drafts client letter: Explains sentence, appeal rights, probation conditions, final invoice
7. Prompts for appeal: "Pursue appellate review?"
8. If attorney says "No appeal": Proceeds to expungement check (none applicable for guilty plea)
9. Generates closing checklist, archives case

**Result:** Case closed, client notified, appeal deadline tracked in calendar, file archived with 5-year retention note.

## Scenario 2: Acquittal at Trial

1. Attorney triggers skill: "Case is closed — acquittal"
2. Confirms: Verdict date, charges acquitted on
3. Skill records: All charges acquitted, no sentence, no probation
4. Generates client letter: Congratulatory, explains acquittal, advises immediate expungement eligibility (Art. 973)
5. Expungement check: Client eligible immediately under Art. 973
6. Recommends: Pursue expungement motion via **dw-pretrial-motion-library-crim**
7. Creates calendar reminder: Follow-up for expungement motion in 1 week
8. Generates closing checklist, archives case

**Result:** Client notified of favorable outcome, expungement path clearly explained, calendar reminder set for follow-up.

## Scenario 3: Guilty Verdict with Delayed Sentencing

1. Attorney triggers skill: "Verdict entered"
2. Confirms: Guilty verdict, but sentencing is scheduled for 4 weeks
3. Skill halts full closure: Marks as "DISPOSITION ENTERED — AWAITING SENTENCING"
4. Saves intermediate state to Case Brain
5. Creates Google Calendar reminder: "Return to dw-case-disposition-crim workflow after sentencing"
6. Returns to attorney: "Case marked for closure after sentencing"

**After sentencing:** Attorney re-invokes skill with sentencing details, and full closure workflow (Steps 1-7) executes.

## Scenario 4: Diversion Completion

1. Attorney triggers skill: "Client completed diversion program"
2. Confirms: Diversion completion date, all conditions met
3. Skill records: Case dismissed upon diversion completion (Art. 893/894)
4. Generates client letter: Explains successful diversion, record dismissal, immediate expungement eligibility
5. Expungement check: Eligible immediately
6. Recommends expungement motion and sets calendar reminder
7. Generates closing checklist, archives case

**Result:** Client informed of successful completion and clear expungement path.

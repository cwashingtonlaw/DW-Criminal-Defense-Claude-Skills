# Witness Scorecard Template

**Per-witness one-page debrief produced after the witness leaves the stand. Feeds tomorrow's cross prep, redirect/recross planning, and the threat-matrix Post-Cross Refresh.**

The scorecard is generated immediately after the witness is excused (or at lunch break / end of day if the witness's testimony continues across sessions). It does NOT replace the cross-examination outline — it captures what the cross actually elicited (or failed to elicit) so the next-day prep is calibrated to reality, not the prep notes.

Length target: half a page per witness. The exception is a CRITICAL witness (per `dw-witness-threat-matrix-crim`) where a full page is acceptable.

---

## Template

```
============================================================
WITNESS SCORECARD — [WITNESS NAME]
Trial Day [N] — [DATE]
[ATTORNEY WORK PRODUCT — DO NOT DISCLOSE]
============================================================

CASE: [Client Name] v. State / [Docket #]
WITNESS TYPE: [Eyewitness / LEO / Expert / Cooperator / Custodian / Corroborator]
THREAT MATRIX PRIORITY (pre-trial): [CRITICAL / HIGH / MEDIUM / LOW]
DIRECT LENGTH: [HH:MM]    CROSS LENGTH: [HH:MM]    REDIRECT: [HH:MM]
EXAMINING ATTORNEY (defense): [Name]

------------------------------------------------------------
1. THEME ALIGNMENT
------------------------------------------------------------
DEFENSE THEME: [one sentence — pulled from Case Brain or
case theme document, e.g., "This case is about shortcuts and
sloppy police work."]

HOW THIS WITNESS HELPED THE THEME:
- [bullet] — (T. p. __ / [time] / [witness statement])
- [bullet] — ...

HOW THIS WITNESS HURT THE THEME:
- [bullet] — (T. p. __ / [time] / [witness statement])
- [bullet] — ...

NET THEME IMPACT: [HELPED / HURT / NEUTRAL]

------------------------------------------------------------
2. KEY ADMISSIONS ON DIRECT (most damaging to defense)
------------------------------------------------------------
Capture the 3-5 statements on direct that hurt the defense most.
Each one needs a time-stamp / page reference for later transcript work.

- [admission] — (T. p. __ / [time])
- [admission] — (T. p. __ / [time])
- [admission] — (T. p. __ / [time])

------------------------------------------------------------
3. KEY CONCESSIONS ON CROSS (most useful to defense)
------------------------------------------------------------
The 3-5 cross-exam wins. These become closing-argument material.

- [concession] — (T. p. __ / [time])
- [concession] — (T. p. __ / [time])
- [concession] — (T. p. __ / [time])

------------------------------------------------------------
4. LOCKED-IN COMMITMENTS
------------------------------------------------------------
Statements the witness committed to that another witness can
contradict. These set up impeachment of LATER witnesses.

- [commitment] — useful when [Later Witness] testifies about [topic]
- [commitment] — locks witness into [fact]; if rebutted by [doc/witness],
                 useful in closing

------------------------------------------------------------
5. IMPEACHMENT ELICITED (or not)
------------------------------------------------------------
Track which impeachment hooks from the cross outline ACTUALLY
landed, which fell flat, and which were not used.

USED — successful:
- [Prior inconsistent statement re: ___ — confronted with ___ — admitted /
   denied / tried to explain]

USED — flat:
- [Hook tried but witness recovered or jury didn't react]

NOT USED:
- [Hook from outline that wasn't reached — carries to next session]
- [Document not introduced — carries]

------------------------------------------------------------
6. WHAT CROSS STILL NEEDS (carries to tomorrow / redirect)
------------------------------------------------------------
[If witness will be recalled, redirected, or testimony tied to
later witnesses, list what defense still needs.]

- [unfinished business] — escalate to dw-cross-exam-architect-crim
- [follow-up question for related witness]
- [exhibit to introduce through later witness]

------------------------------------------------------------
7. JURY READ
------------------------------------------------------------
Observable juror reactions during this witness (cross-reference
Module E juror observation log).

- [Juror #__] — [reaction during testimony]
- General panel: [attentive / restless / sympathetic / skeptical]

------------------------------------------------------------
8. WITNESS DEMEANOR
------------------------------------------------------------
- Confidence: [confident / hesitant / defensive]
- Consistency: [consistent with prior statements / inconsistent]
- Likeability: [strong / moderate / weak]
- Cross resilience: [held under pressure / cracked / minimal pressure applied]

------------------------------------------------------------
9. NET ASSESSMENT
------------------------------------------------------------
DEFENSE NET: [WIN / NEUTRAL / LOSS]
ONE-SENTENCE WHY: [...]

------------------------------------------------------------
10. THREAT-MATRIX REFRESH SIGNAL
------------------------------------------------------------
[For dw-witness-threat-matrix-crim Post-Cross Refresh Mode]

Damage score adjustment: [up / down / unchanged] — reason: [...]
Vulnerability score adjustment: [up / down / unchanged] — reason: [...]
Priority tier change: [CRITICAL → HIGH / no change / ...]

------------------------------------------------------------
11. APPELLATE FLAGS (cross-reference Module B objection log)
------------------------------------------------------------
- Objections preserved during this witness: [#s — Obj-014, Obj-019, ...]
- Missed objections during this witness: [MO-005, MO-007, ...]
- Proffer issues: [PC-002 — defense exhibit excluded, proffer made
   at T. p. __, ll. __]

============================================================
END OF SCORECARD
============================================================
```

---

## How to Fill It Out (during a recess)

The scorecard is built in this order, fastest first:

1. **Top metadata** (30 seconds) — name, type, lengths, examining attorney. Pre-fill at start of witness.
2. **Net assessment** (1 minute) — gut call. Update later if needed.
3. **Key concessions on cross** (3 minutes) — the most useful field for closing. Pull from cross outline + actual answers.
4. **Key admissions on direct** (3 minutes) — the most damaging direct testimony. Pull from contemporaneous notes.
5. **Locked-in commitments** (2 minutes) — only if witness committed to something a later witness can contradict.
6. **Impeachment elicited** (3 minutes) — what landed, what didn't.
7. **Theme alignment, demeanor, jury read, threat refresh, appellate flags** — fill at end of day if no time mid-trial.

If the recess is short, capture sections 2-4 only, marked `[FULL DETAIL → end-of-day memo]`. The other sections are end-of-day work.

---

## Critical-Witness Variant (longer-form OK)

For witnesses ranked CRITICAL on the threat matrix, expand to:

- Verbatim quotes for the 3 most important admissions and 3 most important concessions
- A "what we wanted vs. what we got" cross-comparison table
- Closing-argument ammo bullets — exactly what the closing should say about this witness
- Specific record citations for every claim

CRITICAL scorecards may run a full page. They feed `dw-cross-exam-architect-crim` for any redirect / recall and `dw-witness-threat-matrix-crim` Post-Cross Refresh.

---

## Output Path

```
{{CASE_ROOT}}/01 - Trial Notebook/04 - Trial Day/Day [N]/03 Witness Scorecards/
   Witness Scorecard - [Last Name] - Day [N].md
```

---

## Cross-Skill Handoffs

- **`dw-cross-exam-architect-crim`** — section 6 ("WHAT CROSS STILL NEEDS") seeds the next-day cross outline for this witness or related witnesses.
- **`dw-witness-threat-matrix-crim`** — section 10 ("THREAT-MATRIX REFRESH SIGNAL") feeds Post-Cross Refresh Mode after multiple scorecards accumulate.
- **`dw-appellate-error-monitor-crim`** — section 11 ("APPELLATE FLAGS") cross-references Module B objection log.
- **`dw-trial-notebook-builder-crim`** — at end of trial, all scorecards roll into the Trial Notebook witness section.
- **Closing argument** — sections 3 ("Key Concessions") and 4 ("Locked-In Commitments") are the raw material for closing argument bullets.

---

## What the Scorecard Is NOT

- Not a transcript. The transcript comes weeks later.
- Not a polished memo. It is a contemporaneous note for the defense team.
- Not a substitute for the cross outline (`dw-cross-exam-architect-crim` produces the outline; the scorecard captures what actually happened).
- Not a brief. Save legal analysis for the end-of-day memo or the post-trial motion.
- Not for sharing with the client. It is attorney work product.

---

*Apply work product marking per `dw-shared-protocols-crim/references/attorney-work-product-marking.md`.*

---

## Half-Page Format Block (moved from SKILL.md Module C)

Read at **MODULE C — Witness Scorecard** of `SKILL.md`; the compact half-page-max scorecard skeleton.

```
WITNESS SCORECARD — [WITNESS NAME] — Day [N], [DATE]

Type: [eyewitness / LEO / expert / cooperator / custodian / corroborator]
Direct length: [HH:MM]    Cross length: [HH:MM]

THEME ALIGNMENT
- Defense theme: [one sentence]
- Helped theme: [bullets — what testimony advanced it]
- Hurt theme: [bullets — what testimony undermined it]

KEY ADMISSIONS ON DIRECT (most damaging to defense)
- [bullet] — (T. p. __ / 10:42 AM)
- ...

KEY CONCESSIONS ON CROSS (most useful to defense)
- [bullet] — (T. p. __ / 11:18 AM)
- ...

LOCKED-IN COMMITMENTS
- Witness committed to [fact] — useful for closing if rebuttal witness contradicts
- ...

IMPEACHMENT ELICITED (or not)
- [Prior inconsistent statement / bias / conviction / etc.]
- Hooks NOT used: [carry to tomorrow if redirect or recall]

WHAT CROSS STILL NEEDS (carries to tomorrow)
- [bullet] — escalate to dw-cross-exam-architect-crim for next-day prep

NET ASSESSMENT
- Defense net: WIN / NEUTRAL / LOSS
- One-sentence why: [...]
```

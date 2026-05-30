# Batson / Reverse-Batson Running Log

**Real-time peremptory-challenge tracker for voir dire and trial.**

Authority: *Batson v. Kentucky*, 476 U.S. 79 (1986). Applied to defense strikes (reverse-Batson) by *Georgia v. McCollum*, 505 U.S. 42 (1992). Extended to gender by *J.E.B. v. Alabama ex rel. T.B.*, 511 U.S. 127 (1994). Louisiana follows the federal framework: *State v. Collier*, 553 So.2d 815 (La. 1989); *State v. Tyler*, 723 So.2d 939 (La. 1998).

The constitutional rule: peremptory challenges may not be exercised on the basis of race or gender. The court runs the three-step Batson inquiry on objection.

---

## Three-Step Batson Framework

```
STEP 1 — PRIMA FACIE CASE
   The objecting party must show facts and circumstances raising an
   inference that the strike was based on race (or gender, or other
   protected class).
   Evidence: pattern of strikes, disparate questioning of struck panelists,
   demographics of the venire vs. demographics of those struck.

STEP 2 — RACE-NEUTRAL EXPLANATION
   Burden shifts to the striking party to articulate a race-neutral
   reason for the strike. The reason need not be persuasive or even
   plausible at this step — only race-neutral on its face.
   *Purkett v. Elem*, 514 U.S. 765 (1995).

STEP 3 — PRETEXT ANALYSIS
   Burden returns to the objecting party. Court determines whether
   the proffered reason is genuine or pretextual.
   Factors: comparison to non-struck similarly-situated panelists,
   plausibility of reason, demeanor of striking attorney, history
   of past strikes in this trial.
```

If the court finds purposeful discrimination at Step 3, the strike is denied; the panelist is seated, or the panel is reseated, or (in some cases) a new venire is drawn.

---

## Running Log — Strike Tracker

Track every peremptory challenge by both sides. Update in real time during voir dire.

### Per-Strike Row

| # | Side | Juror # | Name | Race | Gender | Age | Occupation | Voir Dire Notes | For Cause? | Stated Reason (if challenged) | Court Ruling | Pattern Note |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | State | 4 | [Initials] | B | F | 34 | Teacher | "Has cousin in jail" | No | — | Used | — |
| 2 | Defense | 12 | [Initials] | W | M | 58 | Accountant | "Believes police never lie" | No | — | Used | — |
| 3 | State | 14 | [Initials] | B | F | 41 | Nurse | "Knows victim's family vaguely" | No | — | Used | 2 of 2 State strikes vs. Black panelists |
| 4 | State | 22 | [Initials] | B | M | 29 | Mechanic | No issues flagged | No | "Yawned during questions" | Used | 3 of 3 State strikes vs. Black panelists — BATSON CHALLENGE |
| 5 | — | 22 | [BATSON OBJECTION RAISED — see below] | | | | | | | "Yawned" — defense argued pretext | Denied — court found race-neutral | Pattern continues |

### Tally Table (refresh after each strike)

| Side | Strikes Used | Strikes Remaining | Strikes vs. Black | Strikes vs. White | Strikes vs. F | Strikes vs. M |
|---|---|---|---|---|---|---|
| State | 4 | 8 | 3 | 1 | 2 | 2 |
| Defense | 2 | 10 | 0 | 2 | 0 | 2 |

(In Louisiana, peremptory challenges in jury trials: 12 per side in capital and life cases under La. C.Cr.P. Art. 799; 6 per side in other felony cases; verify per case type.)

### Demographics of the Venire

Capture early so the comparator analysis works:

| Demographic | # in Venire | % | # Seated (final 12) | % Seated |
|---|---|---|---|---|
| Black | 14 | 28% | 2 | 17% |
| White | 30 | 60% | 9 | 75% |
| Hispanic | 4 | 8% | 1 | 8% |
| Other | 2 | 4% | 0 | 0% |
| Female | 28 | 56% | 7 | 58% |
| Male | 22 | 44% | 5 | 42% |

---

## Pattern Emergence Threshold

**No magic number, but courts find a prima facie case when:**

- All or most strikes by the State are against members of one race (e.g., 3 of 3 strikes against Black panelists).
- Strike rate of one race substantially exceeds the rate against another (e.g., State strikes 5 of 7 Black panelists, only 1 of 12 White panelists).
- Disparate questioning — State asked Black panelists more / different questions than White panelists.
- Strikes against panelists who answered all questions favorably to the State.
- Strikes leaving zero or one Black juror on a panel where the venire was meaningfully diverse.

**Run a pattern check after each strike.** If the State has now used 3+ of its strikes against members of a single race, raise the Batson challenge — do not wait until the panel is seated. Untimely Batson challenges are waived. *State v. Williams*, 524 So.2d 746 (La. 1988).

---

## Triggering the Batson Challenge

```
[Time-stamp the moment]

DEFENSE COUNSEL:
   "Your Honor, before the next strike, we raise a Batson challenge.
    The State has used [N] of [N] peremptories against [Black / female /
    Hispanic] panelists. The pattern raises an inference of purposeful
    discrimination. We request the court direct the State to articulate
    a race-neutral reason for the strike of Juror [#]."

[Court conducts Step 1 finding]

COURT:
   [If prima facie found:] "Counsel, please provide a race-neutral reason."
   [If not found:] "I do not find a prima facie case. Strike accepted."

[State response — Step 2]

STATE:
   "[Stated reason]"

[Defense response — Step 3]

DEFENSE:
   "Your Honor, the reason is pretextual because [comparator analysis:
    State did not strike Juror [#], a [other-race] panelist who answered
    similarly / had similar background / etc.]. The reason is also
    implausible because [factual rebuttal]."

[Court ruling — Step 3]

COURT:
   [Either denies the strike or accepts the State's reason.]
```

### Preservation requirements

1. **Object before the panel is sworn.** *State v. Williams*, 524 So.2d 746 (La. 1988). Untimely = waived.
2. **State the basis specifically** — race / gender / national origin. A vague Batson challenge ("the State is striking based on something") is insufficient.
3. **If denied at Step 1**, request the court make a record of the prima facie analysis.
4. **At Step 3**, build the pretext record: comparator panelists, demeanor, prior history of strikes by this DA, statistics.
5. **Preserve the entire panel and venire demographics** — the appellate court needs the comparator data.
6. **Renew the challenge** if the pattern continues with subsequent strikes.

---

## Reverse-Batson — Defense Peremptories

*Georgia v. McCollum*, 505 U.S. 42 (1992) — the State has standing to challenge defense peremptories on the same Batson framework.

**Defense considerations:**

- The State CAN raise reverse-Batson against defense strikes.
- Defense should anticipate reverse-Batson when striking a pattern of one-race panelists.
- If the State raises reverse-Batson, defense must articulate race-neutral reasons.
- Same three-step framework applies.

**Practical effect:** Defense in a Black-defendant case who strikes only White panelists is vulnerable. Document the race-neutral reason for every defense strike in real time so the basis is captured contemporaneously, not reconstructed under pressure.

### Defense Strike Justification Notes (running)

Capture for every defense strike, even before any reverse-Batson challenge:

| Strike # | Juror # | Race | Reason (race-neutral) | Source of concern (voir dire response, demographics, occupation, body language) |
|---|---|---|---|---|
| 1 | 12 | W / M | Stated belief that police always tell the truth | Voir dire response, p. ___ |
| 2 | 7 | W / M | Has spouse who is retired LEO | Questionnaire response |
| 3 | 18 | W / F | Was a victim of similar crime; expressed inability to be impartial | Voir dire response, p. ___ |
| 4 | 25 | W / M | Showed visible disinterest, head down during questioning | Counsel observation — bench note |

These notes are NOT discoverable to the State unless reverse-Batson is raised. They are work product. Apply work product marking.

---

## J.E.B. — Gender-Based Strikes

*J.E.B. v. Alabama ex rel. T.B.*, 511 U.S. 127 (1994). Same three-step framework applies to gender. Defense should track gender pattern in addition to race.

**Common scenario:** State strikes most or all female panelists in a sex-offense or domestic-violence case. Raise J.E.B. challenge with same procedural sequence as Batson.

---

## Other Protected Classifications

Louisiana courts have NOT consistently extended Batson to:
- Religion
- Sexual orientation
- Disability
- Age (over 40 — federal employment law context)

If raising a non-traditional Batson, brief the issue carefully. *Hernandez v. New York*, 500 U.S. 352 (1991) (language fluency — not protected as standalone, but pretext analysis applies).

---

## Common Pretext Patterns to Argue at Step 3

When the State articulates a race-neutral reason, attack pretext using:

1. **Comparator analysis.** Identify a non-struck panelist of a different race who shared the stated reason. "The State did not strike Juror #15 (White), who also has a relative previously incarcerated."
2. **Implausibility.** "The reason given is implausible because the panelist's voir dire response was substantially identical to that of [non-struck panelist]."
3. **Disparate questioning.** "The State questioned Juror [#] for 12 minutes while questioning White panelists for 2 minutes each. The disparate questioning was a setup to manufacture a strike reason."
4. **Pattern history.** "This is the third strike of [N] against Black panelists; the cumulative pattern shows discriminatory intent."
5. **Stated reason contradicts voir dire record.** "The State claims the panelist 'seemed inattentive,' but the panelist answered every question and the record reflects engagement."
6. **Strike of strongest panelist for state side.** When the State strikes a panelist who answered favorably, pretext is more likely.

Cite *Miller-El v. Dretke*, 545 U.S. 231 (2005), for comparative analysis; *Snyder v. Louisiana*, 552 U.S. 472 (2008) (Louisiana case — comparator analysis required at Step 3).

---

## Daily Roll-Up

At end of voir dire day:

```
BATSON DAILY SUMMARY — [DATE]

State strikes used today: __ / __
   Demographics: __ B, __ W, __ H, __ Other
   F: __, M: __
Defense strikes used today: __ / __
   Demographics: __ B, __ W, __ H, __ Other
   F: __, M: __

Batson challenges raised today: __
   Outcomes: __ sustained, __ overruled, __ deferred

Pattern flags: [list]

Carry to tomorrow: [voir dire continues / panel seated / open issues]
```

Append to Module F end-of-day memo.

---

## Output File

Save the running log as:

```
{{CASE_ROOT}}/01 - Trial Notebook/04 - Trial Day/_MASTER/Batson Log - MASTER.md
```

Update in real time. Do not overwrite.

---

*Real citations: *Batson v. Kentucky*, 476 U.S. 79 (1986); *Georgia v. McCollum*, 505 U.S. 42 (1992); *J.E.B. v. Alabama ex rel. T.B.*, 511 U.S. 127 (1994); *Purkett v. Elem*, 514 U.S. 765 (1995); *Miller-El v. Dretke*, 545 U.S. 231 (2005); *Snyder v. Louisiana*, 552 U.S. 472 (2008); *State v. Collier*, 553 So.2d 815 (La. 1989); *State v. Williams*, 524 So.2d 746 (La. 1988); *State v. Tyler*, 723 So.2d 939 (La. 1998).*

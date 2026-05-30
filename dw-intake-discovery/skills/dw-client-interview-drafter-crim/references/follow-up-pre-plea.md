# Follow-Up Interview — Pre-Plea Consultation

**Use when:** State has extended a plea offer (or attorney is preparing to recommend acceptance / rejection of one). This sheet structures the consultation that captures informed-consent grounds for the decision.
**Target length:** 2 pages.
**Hard rule:** This sheet does NOT itself contain the plea offer specifics — the attorney communicates those orally. The sheet captures the client's understanding, the collateral consequences, and the record of advisement.

---

## HEADER

- Work product marking
- Title: "CLIENT FOLLOW-UP INTERVIEW — PRE-PLEA CONSULTATION"
- Mini case header
- Charge summary
- Plea offer summary (attorney completes BEFORE the meeting — counts, sentence range, conditions, deadline)

---

## SECTION 1 — Confirm Client Mental State

**Warning:** Boykin-grade record. Document competence and voluntariness.

- Are you on any medication right now? Does it affect your thinking?
- Have you slept? Eaten? Need to use the restroom before we start?
- Anyone pressured you in any way to take or reject this offer?
- You understand we can also discuss this with any family member you authorize, but the decision is yours?

---

## SECTION 2 — Client's Understanding of the Charges

- Tell me, in your own words, what each charge accuses you of
- What does the State have to prove for each charge?
- What is the maximum penalty for each charge?
- What is the minimum penalty?

If client struggles to articulate — re-advise in plain language and re-ask.

---

## SECTION 3 — Trial Rights Advisement (Boykin)

Confirm the client understands they have the right to:
- Trial by jury
- Confront and cross-examine witnesses
- Remain silent at trial
- Subpoena witnesses in their defense
- Require the State to prove guilt beyond a reasonable doubt

For each, confirm: *"Do you understand you would give up this right by entering the plea?"*

---

## SECTION 4 — Direct Consequences of the Plea

Run by `dw-plea-negotiation-analyzer-crim` output. Confirm client understands:
- Sentence ceiling and floor under the offer
- Probation / parole conditions
- Restitution exposure
- Fines, fees, court costs
- Time-to-serve calculation (good time, day-for-day, parole eligibility)
- Whether the plea is an *Alford* plea, nolo, or straight guilty
- Whether the State will dismiss other counts or charges
- Whether sentencing is open or capped

---

## SECTION 5 — Collateral Consequences

Confirm client understands the plea's effect on:
- Immigration status (LPR / visa / asylum / pending applications)
- Voting rights (LA: restored after release from supervision)
- Firearm rights (life ban for any felony under 14:95.1)
- Sex offender registration (if applicable)
- Public housing / Section 8
- Public benefits (SNAP, federal student aid)
- Employment / professional licenses
- Driver's license consequences
- Family court / child custody
- Civil suits / restitution / liens
- Future habitual offender exposure

---

## SECTION 6 — Trial Exposure Compared to Offer

Per `dw-plea-negotiation-analyzer-crim`:
- If convicted at trial, exposure (low / median / high)
- Habitual offender exposure if applicable
- Mandatory minimums on stacked counts
- Likely sentencing posture based on judge / parish norms

The attorney communicates the comparison orally — sheet captures client acknowledgment.

---

## SECTION 7 — Client's Decision (Captured Verbatim)

`Client's decision: __________________________________________________________________________________`

`Client's reasons: __________________________________________________________________________________`

`Client confirms decision is voluntary and informed: ☐ Yes  ☐ No  ☐ Needs more time`

`Deadline acknowledged: ☐ Yes  Deadline date: ____________`

---

## SECTION 8 — Post-Consultation Attorney Action Items

- If accepting: prep Boykin colloquy support, restitution backup, allocution outline → `dw-pretrial-motion-library-crim`
- If rejecting: file rejection on record, lock down trial date, refresh trial-prep timeline → `dw-trial-notebook-builder-crim`
- If sentencing is open: prep mitigation packet → `dw-sentencing-mitigation-specialist-crim`
- Update Case Brain with decision and reasons → `dw-case-brain-crim`
- Document advisement for appellate / PCR record → `dw-appellate-error-monitor-crim`

---

## SIGN-OFF

`Consultation date: ____________   Attorney: ____________   Witness (if any): ____________   Location: ____________`

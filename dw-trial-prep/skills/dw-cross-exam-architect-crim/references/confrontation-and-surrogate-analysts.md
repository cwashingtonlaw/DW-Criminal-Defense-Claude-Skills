# Confrontation & Surrogate Analysts

**Loaded at Step 3 (conditional). Read whenever the State's witness is a forensic analyst, a lab supervisor, a records custodian for testimonial material, or anyone testifying about work someone else performed.**

This is both an **objection** and a **cross theme**. Run the objection analysis first — if the testimony should not come in at all, the cross is a fallback, not the plan.

---

## 1. The Doctrine

`[VERIFY]` — holdings summarized from published sources as of this skill revision; confirm current text, the *Smith* pin cite, and any subsequent authority before arguing these. Route through `dw-case-law-researcher-crim`.

| Case | Holding |
|---|---|
| *Crawford v. Washington*, 541 U.S. 36 (2004) | Testimonial hearsay is inadmissible against a criminal defendant unless the declarant is unavailable and the defendant had a prior opportunity to cross-examine |
| *Melendez-Diaz v. Massachusetts*, 557 U.S. 305 (2009) | Forensic lab certificates are testimonial; the analyst is a witness the defendant has the right to confront |
| *Bullcoming v. New Mexico*, 564 U.S. 647 (2011) | The State cannot satisfy confrontation by calling a surrogate analyst who did not perform or observe the test |
| *Williams v. Illinois*, 567 U.S. 50 (2012) | Fractured plurality; limited precedential value — do not build an argument on Williams alone |
| ***Smith v. Arizona*, 602 U.S. ___ (2024)** | **When an expert conveys an absent analyst's statements in support of an opinion, and those statements support the opinion only if true, they are admitted for their truth.** The State cannot relabel them "basis testimony" to escape confrontation; the substitute expert effectively becomes a mouthpiece for the analyst who did the work |

**What *Smith* changed.** Before *Smith*, prosecutors routinely offered a substitute expert's "independent opinion" while relaying the absent analyst's data as mere basis evidence not offered for its truth. *Smith* closes that route: if the underlying statements are useful only because they are true, they come in for their truth and confrontation attaches.

**What *Smith* left open.** The Court did **not** decide whether the particular statements there were *testimonial* — that was remanded. Testimoniality remains a separate, independently required element, and it is where the State will now fight.

`[UNVERIFIED]` — how the Louisiana First, Third, and Fourth Circuits have applied *Smith* since 2024 has not been checked here. **Research the current state-circuit authority for the parish before arguing this.** Route through `dw-case-law-researcher-crim`.

---

## 2. Trigger Check — Run Before Drafting

Ask these in order. Any "no" in rows 1–2 escalates to an objection, not a cross chapter.

1. **Did this witness personally perform the testing or analysis they are testifying about?** If no → *Bullcoming* / *Smith* problem.
2. **Did this witness personally observe the testing?** If no → the problem deepens.
3. **Is the witness relaying another analyst's data, notes, or conclusions to support an opinion?** If yes → *Smith*: those statements are being offered for their truth.
4. **Is the absent analyst unavailable, and was there a prior opportunity to cross-examine?** If no to either → *Crawford* is not satisfied.
5. **Is the report or certificate testimonial** — prepared for use in a prosecution rather than for treatment, business, or machine-generated raw output? This is the contested element post-*Smith*.

**Auto-flag:** if the State's witness list names an analyst who did not sign the report, or names a "lab supervisor" or "technical reviewer" rather than the bench analyst, flag it immediately in the Discovery Gap Report and notify the attorney. This is a pretrial motion issue, not a trial-day surprise.

---

## 3. If the Testimony Comes In Anyway — Cross Themes

When the court admits surrogate testimony over objection, the cross writes itself around what the witness cannot know. Preserve the objection first (see `error-preservation-protocol.md`), then cross on:

**The knowledge gap** — one fact per question, all leading:
- You did not perform this test.
- You were not present when it was performed.
- You did not observe the sample being handled.
- You did not calibrate the instrument that day.
- You did not prepare the bench notes.
- Everything you have told this jury about what happened at that bench, you learned by reading a document.
- You have no personal knowledge of whether the person who wrote it followed the protocol.

**What the absent analyst could have been asked but wasn't:**
- Deviations from SOP that appear nowhere in a final report
- Contamination events, re-runs, and failed controls
- Sample mix-ups and re-labeling
- Whether the analyst was under a proficiency-testing or disciplinary cloud at the time
- Judgment calls at interpretation — the places a report states a conclusion but the bench notes show a decision

**The review that wasn't a review:**
- Technical review is a paper check, not a re-test — correct?
- You did not re-run the sample.
- You reviewed the same document this jury has.
- If the underlying work was wrong, your review would not catch it.

**Route the material demands** through `dw-crime-lab-auditor-crim` — bench notes, raw data, calibration logs, SOP in force on the analysis date, proficiency results, and non-conformance records. A surrogate cross without the underlying file is a cross with no floor.

---

## 4. Preservation

Surrogate-analyst objections are prime appellate material. Every one gets the full treatment from `error-preservation-protocol.md`:

> • **IF OVERRULED — PRESERVE:** Ground: Sixth Amendment confrontation; *Crawford*, *Melendez-Diaz*, *Bullcoming*, *Smith v. Arizona* (2024) — the absent analyst's statements are offered for their truth and the declarant is not present for cross. Proffer: what cross-examination of the bench analyst would have exposed — [specific: SOP deviation, calibration gap, chain break]. La. C.Cr.P. art. 841; La. C.E. art. 103(A)(2).

Log every ruling in the outline's Preservation Log and hand off to `dw-appellate-error-monitor-crim`.

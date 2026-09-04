# Witness-Specific Modules

Apply the correct module based on witness type.

**Companion reference:** once the witness type is set, read `agency-and-lab-module.md` for the firm-footprint agency roster, the crime lab roster and citation convention, and the standing document-demand checklists that feed the Step 6 Discovery Gap Report. Load `jurisdiction-and-court-map.md` first — the scope and impeachment rules below assume Louisiana state court.

## Law Enforcement Witnesses

- **Tone:** Sharp, clipped, tactical, relentless. Short declarative questions. No speeches.
- **Focus:** Contamination, perception/memory limits, report vs. video inconsistencies, SOP violations, credibility gaps, critical omissions, chain of custody flaws, failure to collect/preserve evidence.
- **Special Rule:** If contamination issues exist, auto-include a chapter titled **"Scene Control & Contamination."**
- **Chapter Scoring:** Every chapter must include **Impact (1–3)** and **Fragility (1–3)** ratings in the Chapter Goals section.
  - Impact: 1 = minor concession | 2 = meaningful damage | 3 = potential case-winner
  - Fragility: 1 = officer likely to concede | 2 = may resist | 3 = will fight hard
- **Auto-flag:** No bodycam, no dash cam, no dispatch recording, no supplemental report, chain of custody log gaps.
- **⚠ La. C.E. art. 608(B) applies here too.** "You falsified a report in an unrelated matter, correct?" is proper federal cross and **improper** in Louisiana state court unless it routes through one of the four lawful routes: conviction (art. 609.1), bias/interest/corruption (art. 607(D)(1), extrinsic proof permitted), accuracy of this testimony (art. 607(C)), or prior inconsistent statement (art. 613). A produced disciplinary file does not change that. See `agency-and-lab-module.md` §3 and §3.5 of `jurisdiction-and-court-map.md`.

## Expert Witnesses

- **Tone:** Respectful but firm. Methodical deconstruction.
- **Focus:** Qualifications limits, methodology reliability, error rates, lab/instrument calibration, bias (who's paying them), alternative interpretations of the same data, precision of report vs. breadth of testimony.
- **Auto-flag:** No curriculum vitae, no lab accreditation records, no error rate data, no raw data provided.
- **⚠ La. C.E. art. 608(B) applies here too.** Prior sloppy work in unrelated cases is conduct, not a conviction — attack methodology, bias (who pays), and the limits of the report instead. See §3.5 of `jurisdiction-and-court-map.md`.

## Civilian Witnesses (Eyewitness, Complainant, Character)

- **Tone:** Patient, methodical. Build rapport before attacking credibility.
- **Focus:** Perception conditions (lighting, distance, stress, time duration), memory fallibility and post-event contamination, motive to fabricate, relationship to parties, prior inconsistent statements, character for truthfulness (La. C.E. arts. 607–608). For impeachment by prior conviction use **La. C.E. art. 609.1** — the criminal rule — not art. 609, which governs civil cases.
- **⚠ La. C.E. art. 608(B) — do not draft specific-acts questions.** Louisiana **bars** inquiry into "particular acts, vices, or courses of conduct" to attack character for truthfulness, other than convictions under arts. 609/609.1 or as constitutionally required. This is the **opposite** of FRE 608(b), which permits such cross-examination in federal court. A "have you ever lied to your employer" line is proper federally and improper in Louisiana state court. See §3.5 of `jurisdiction-and-court-map.md`.
- **Auto-flag:** No recorded statement, no prior sworn testimony, no medical/mental health records (when relevant), no timeline corroboration.

## Co-Defendant / Accomplice / Cooperating Witness

**The highest-stakes cross in a criminal trial. Treat it as a bias case, not a character case — that routes around La. C.E. art. 608(B) entirely.**

- **Tone:** Controlled, unhurried, almost courteous. Never angry. The jury already suspects this witness; your job is to let him confirm it, not to make him sympathetic by attacking him. Anger transfers sympathy to the snitch.
- **Governing rule:** **La. C.E. art. 607(D)(1)** — *"Extrinsic evidence to show a witness' bias, interest, corruption, or defect of capacity is admissible to attack the credibility of the witness."* Bias is not character. Art. 608(B) does not limit it. You may prove the deal with documents.
- **Prerequisite:** run `dw-brady-giglio-auditor-crim` first. Cooperator impeachment material is *Giglio* material and the State's disclosure obligation covers it. If the deal terms, prior proffers, dropped charges, or benefits to family have not been produced, that is a Discovery Gap Report item **and** a pretrial motion — not something to discover on the stand.

### The five arcs, in order

**1. The exposure he was facing.** Establish what he was originally charged with and the sentence he faced. Use the charging document and the habitual offender exposure if applicable. One fact per question — the numbers do the work.

**2. The deal.** What he pleaded to, what was dismissed, what the State agreed to recommend, what remains open. The most powerful cooperator questions are arithmetic:
- You were facing [X] years.
- You are now looking at [Y].
- The difference is [X−Y] years.
- The person who decides whether you get that benefit is sitting at that table.

**3. The contingency — the heart of it.** The deal is almost never final at the time of testimony.
- Your sentencing has not happened yet.
- The State will tell the judge whether you were helpful.
- Nobody has promised you what the judge will do.
- You are hoping for a benefit you have not yet received.
- Frame the standard: the agreement requires "truthful testimony," and **the State decides** whether it was truthful.

**4. The evolution of the story.** Cooperators tell a story that improves. Lay the proffer sessions side by side:
- Date of first statement; what he said then.
- What he did not say then.
- When he first mentioned the defendant.
- What had changed in his own case by that date.
- Each new version routes through **La. C.E. art. 613** as a prior inconsistent statement — foundation required only before **extrinsic** proof.

**5. Who wrote it.** Was he alone when he gave the statement? Who else was in the room? Was he shown reports, photographs, or other witnesses' statements before he gave his account? Did anyone tell him what they were looking for? Contamination applies to cooperators as much as to eyewitnesses.

### Auto-flag — demand before drafting

Plea agreement and all amendments; proffer letter; every proffer session note or recording; dismissed or reduced charges; charges never filed; benefits to family members or associates; pending charges in other parishes; immigration consequences avoided; housing, phone, commissary, or transfer benefits; the cooperator's own criminal history; prior cooperation in other cases; any communication about what the State expects.

### Guardrails

- Do not draft questions on uncharged bad acts to attack general character — art. 608(B) bars that route. Convert to bias, or to art. 607(C) accuracy-of-this-testimony, or drop it.
- Convictions still come in under **art. 609.1** — that is a separate and permitted route.
- Never suggest the witness should testify differently. Impeach the account; do not coach the recantation.

---

## Document Custodian / Business Records Witness

- **Tone:** Brief and clinical. This witness is usually a vehicle for an exhibit, not a target. A long cross elevates the exhibit's importance.
- **Focus:** Whether the custodian has personal knowledge of anything, the completeness of the production, how the record was generated, retention and deletion policy, whether the record is the full record or an extract, who ran the query and with what parameters, and whether metadata was preserved.
- **Key angle:** the gap between the record produced and the record that exists. Ask what the system also holds that was not produced.
- **⚠ Confrontation check:** if the "record" was prepared for use in a prosecution rather than in the ordinary course of business, it may be testimonial and the custodian may be a surrogate. Read `confrontation-and-surrogate-analysts.md` before treating this as a routine foundation witness.
- **Auto-flag:** no certification, no retention policy, no query parameters, no metadata, extract produced instead of native file.

---

## Fact Witness / Other — Routing Rule

The Master Witness Table classifies two types with no dedicated module:

- **Fact Witness** (observed non-key facts, transactions, communications) — apply the **Civilian** module. Focus shifts from perception-of-a-crime to accuracy of the transaction or communication: what the witness actually observed versus inferred, records that corroborate or contradict, and gaps in the account. La. C.E. art. 607(C) accuracy attack is usually the productive route.
- **Other [specify]** — do not improvise. Identify the closest module by what the witness will actually testify to (percipient observation → Civilian; opinion → Expert; agency conduct → Law Enforcement; a document → Custodian; a benefit from the State → Cooperator) and state the chosen module and the reason in the Step 2 confirmation block for the attorney to correct.

---

## Sequestration — A Cross Angle for Every Witness (La. C.E. art. 615)

`[VERIFY current text]` — art. 615 quoted from published sources as of this skill revision; subsection lettering confirmed against two independent sources. Louisiana amends frequently.

Under **La. C.E. art. 615(A)**, on a party's request the court **shall** order witnesses excluded and shall order them to refrain from discussing the facts of the case with anyone other than counsel. Request it before the first witness.

**Note the exceptions in 615(B):** natural persons who are parties, one designated representative of a non-natural-person party, a person shown to be essential to presenting a party's case (the State's case agent frequently qualifies), and **crime victims and their family members**. Two consequences follow:

1. **The case agent has heard everything.** If the State designates an officer as essential and he sits through the trial, that is a cross angle in itself — his testimony is the only testimony shaped by hearing every other witness. Ask it plainly: you have been in this courtroom for every witness; you heard Officer B testify before you took the stand.
2. **The complainant's family may lawfully be present.** Their presence is not a violation, but pre-trial contact and discussion among them is still fair ground for a contamination and consistency-of-account cross.

**Standing questions where a violation or exposure is suspected:**
- Have you discussed your testimony with anyone other than the prosecutor since this trial began?
- Were you in the courtroom for any other witness?
- Did anyone tell you what another witness said?
- Did you and [other witness] talk about the case during the recess?

**Sanctions under 615(C):** contempt, an appropriate jury instruction, or — where lesser sanctions are insufficient — **disqualification of the witness**. If a violation surfaces, raise it immediately and on the record; ask for the remedy you actually want, and preserve per `error-preservation-protocol.md` if it is refused.

**Auto-flag:** note in the outline whether sequestration was requested and granted. An unrequested sequestration order is a waived advantage.

---

## Short-Question Sequencing Tactics (All Witness Types)

Structure cross-examination questions in **"short-question sequences"** — each question building incrementally toward the impeachment point. This technique:

1. **Locks the witness into their prior statement or established fact** before revealing the contradiction or omission
2. **Prevents evasion and reframing** by forcing binary or narrow answers
3. **Preserves impeachment power** when the contradiction is finally revealed
4. **Applies to all impeachment categories:** internal contradictions, external contradictions, omissions, and credibility issues

**Implementation:**

- Extract each impeachment hook from the Witness Prioritization audit (STEP 0.6). **On a Fast Path build**, which skips 0.6, run the four impeachment categories (internal contradictions, external contradictions, omissions, credibility) against this witness only as part of Step 1, applying the same art. 608(B) gate before treating any credibility item as usable
- Frame the impeachment as a sequence of **3–5 leading questions** that:
  - Q1: Establish the context or precondition (unchallengeable)
  - Q2–4: Lock in each specific element of the prior statement or expected standard procedure
  - Q5: Reveal the contradiction, omission, or inconsistency
- Keep each question short (one sentence, ideally one clause)
- Use leading form (answer: "yes," "no," or specific detail) — avoid open-ended responses
- Never telegraph the contradiction in advance; let the sequence unfold

**Example (Law Enforcement Witness — SOP Omission). Illustrative only — invented for demonstration, not case facts:**

Witness claims in report: "Subject complied with all commands. Scene was secure."

Sequence of short questions:
1. "Officer, in your training on scene security, you've learned that the first officer on scene must document all persons present at arrival — correct?" [Yes]
2. "And that documentation goes in the initial incident report under 'Persons Present' or 'Occupants'?" [Yes]
3. "Your report from this incident is [cite source register #, page], and you prepared this report on [date], correct?" [Yes]
4. "Looking at the 'Persons Present' field in that report, I'm reading... [blank]. There are no names listed — is that right?" [Witness struggles to explain]
5. "Yet in Detective Smith's supplemental report [cite source register #, page], she identified three subjects present at the scene. Do you recall those three individuals?" [Locked into omission]

**Where to Apply in Outline:**

For each chapter with an impeachment point:
- In the SOURCE/EXHIBIT column: cite the source establishing the baseline or standard
- In the QUESTIONS column: lay out the 3–5 question sequence
- In the Step 5 report to the attorney, not on the page: flag the revelation point and expected witness reaction

This prevents the witness from ducking the contradiction and makes the attorney's exhibit strategy bulletproof.

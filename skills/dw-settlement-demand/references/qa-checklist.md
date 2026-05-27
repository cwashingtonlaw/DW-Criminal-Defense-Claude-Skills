# QA Checklist (Mandatory Pre-Output Pass)

Run every item before generating the final .docx. Fix any failure and re-run the checklist. Do not output until every box is checked.

---

## 1. Name Consistency

- [ ] Plaintiff full name appears identically at every mention (first occurrence is "Mary Elizabeth Jones"; subsequent are "Mrs. Jones" or "Ms. Jones" — pick one honorific and stay with it).
- [ ] No leftover names from prior cases anywhere in the document (search the draft for prior firm-case names: Boudreaux, Brooks, Antoine, Hopes, Polk, Williams, Landry, Vallot, Monroe — if any appear and they aren't the current case, replace).
- [ ] Defendant name is consistent.
- [ ] Counsel names spelled correctly throughout.
- [ ] Spouse / family-member names consistent.
- [ ] Provider names match the medical chronology spelling.

---

## 2. Math Reconciliation

- [ ] Per-provider medical-charge totals add up to the past-medicals grand total.
- [ ] Past-medicals grand total equals the figure cited in the prose AND the RECAP table's PAST MEDICAL EXPENSES line.
- [ ] Future-medicals subtotals (if a projection table is used) sum to the FUTURE MEDICAL EXPENSES line on RECAP.
- [ ] Past lost wages calculation total equals the PAST LOST WAGES line on RECAP.
- [ ] Future lost wages calculation total equals the FUTURE LOST WAGES line on RECAP.
- [ ] Body-region bucket recommendations sum exactly to the GENERAL DAMAGES line on RECAP.
- [ ] Judicial-interest year-by-year subtotals sum to the JUDICIAL INTEREST line on RECAP.
- [ ] RECAP TOTAL equals the sum of every component above it (verify with arithmetic).
- [ ] The DEMAND statement number matches the RECAP TOTAL (single-step demands) OR the today-number (two-step demands).
- [ ] For two-step demands, the trial anchor equals the RECAP TOTAL and the today number is the discounted resolution figure.
- [ ] Every "$" figure appears with two decimal places (or consistently rounded) — no mix of `$1,000` and `$1,000.00`.
- [ ] No internal inconsistencies (e.g., GD prose says "$300,000" but bucket recommendation says "$200,000").

---

## 3. Citation Completeness

- [ ] Every factual assertion has a source citation (records, deposition, police report, deposition, etc.).
- [ ] No `[UNSOURCED — VERIFY]` flags remain unhandled (either source the fact or remove it).
- [ ] Every record / deposition / exhibit cited in the text appears in the attachment list.
- [ ] Every entry in the attachment list is actually being attached (the attorney has them ready).
- [ ] Bates ranges (if used) are sequential and non-overlapping.
- [ ] Quantum-case citations carry `[VERIFY CITATION]` flags on any case not in `louisiana-quantum-cases.md` with a confirmed cite.

---

## 4. Typo and Boilerplate Cleanup

Run a find-and-replace pass for these common firm-history typos:

- [ ] "Priarieville" → "Prairieville"
- [ ] "Sherriff's" → "Sheriff's"
- [ ] "INJUIES" → "INJURIES"
- [ ] "the crashed" → "the crash"
- [ ] "judgement" → "judgment"
- [ ] "alot" → "a lot"
- [ ] "occured" → "occurred"
- [ ] "untill" → "until"
- [ ] Trailing double spaces → single space (run twice — the first pass may leave residue)
- [ ] "Cir 11/02/05" → "La. App. 3 Cir. [Year from actual case]" (or similar mangled circuit cites)
- [ ] "Mrs." vs. "Ms." consistency — pick one per plaintiff and replace any mismatches

---

## 5. Section-Label Consistency

- [ ] Letter-style labels (A./B./C./D./E./F.) in `demand` mode — no mixing.
- [ ] Roman-numeral labels (I./II./III./IV./V./VI.) in `mediation_paper` mode — no mixing.
- [ ] "Section #:" labels in `hybrid` mode — no mixing.
- [ ] Sub-section labels follow the chosen system (a./b./c. or 1./2./3.) consistently.
- [ ] Bold/ALL-CAPS treatment is applied identically to every top-level section.

---

## 6. Mode-Banner Alignment

- [ ] Banner says "SETTLEMENT DEMAND LETTER" or "SETTLEMENT OFFER" ONLY when going to defense counsel as the primary addressee.
- [ ] Banner says "MEDIATION POSITION PAPER" ONLY when going to a mediator as the primary addressee.
- [ ] If banner is "MEDIATION POSITION PAPER," the mediator's address block is first; defense counsel is second.
- [ ] If banner is "SETTLEMENT DEMAND LETTER" and the case is going to mediation, the mediator is cc'd at the bottom — not as a primary addressee.

---

## 7. Response Deadline

- [ ] If `mode = demand`, a response deadline of 15 or 30 days appears at the end of the DEMAND section in ALL CAPS bold.
- [ ] If `mode = mediation_paper`, NO response deadline appears anywhere in the document.
- [ ] If `mode = hybrid`, attorney has decided whether to include a deadline (typically not).

---

## 8. De-Duplication

- [ ] No quantum case cited twice in the document, **whether within a single bucket or across buckets**. (Brooks 2020 corpus error: Palmer cited at items 2 and 4 of the same bucket; Griffin cited at items 1 and 5 of the same bucket — both should have been caught here.)
- [ ] No witness referenced twice with different summaries.
- [ ] No exhibit number duplicated.
- [ ] No same-statute citation repeated verbatim in two different sections (LAW subsection vs. inline citation).

---

## 9. Pronoun Consistency and Gender Alignment

- [ ] Plaintiff's pronouns (he/him/his, she/her/hers, they/them/theirs) used consistently throughout.
- [ ] Pronouns match the plaintiff's gender as established at first mention. (Monroe 2023 corpus error: "compensate Ms. Monroe for *his* past and future soft tissue injuries" — gender mismatch slipped through; the QA pass must catch this.)
- [ ] No accidental switches mid-document.
- [ ] Honorific matches gender ("Mrs."/"Ms." for female plaintiffs; "Mr." for male plaintiffs).

---

## 10. Boilerplate Insertion (Verbatim)

- [ ] Sole-fault statement appears at end of FACTS — verbatim per `house-style.md` §12.
- [ ] "Enclosed is the medical expense worksheet..." opens SPECIAL DAMAGES (when applicable) — verbatim.
- [ ] "A review of Louisiana law shows that similarly situated persons..." opens GENERAL DAMAGES bucket(s) — verbatim.
- [ ] "Considering the foregoing case[s], a compromise of $[X] would adequately compensate..." closes each bucket — verbatim.
- [ ] "In the interest of seeking an amicable resolution..." appears in DEMAND — verbatim.
- [ ] Per-se negligence closer (LAW subsection) — verbatim if the LAW subsection exists.

---

## 11. Exhibit Cross-References

- [ ] Every "Exhibit __" reference in the body of the document has a corresponding entry in the attachment list with the same number.
- [ ] Exhibit numbers are sequential (1, 2, 3, ...) with no gaps.
- [ ] Exhibit descriptions in the attachment list are concrete and identifiable.

---

## 12. Confidentiality / Privacy

- [ ] No SSN, full DOB, or other PII in the body of the demand unless required (and only with the attorney's explicit go-ahead).
- [ ] No HIPAA-protected information about non-party family members.
- [ ] Mediation papers should carry the confidentiality marking when the firm and mediator have set that convention.

---

## 13. Demand Reasonableness Sanity Check

The skill should flag for attorney review if any of the following are true:

- [ ] **Demand exceeds 3× plausible Louisiana jury verdict** for the body-region severity profile. Defense will treat the demand as unreasonable and not move.
- [ ] **Demand exceeds the known policy limits by more than 10×** without a clear excess-coverage strategy.
- [ ] **General-damages bucket exceeds the highest comp case in that bucket by more than 50%** without unusual aggravators (catastrophic permanency, unique pain pattern, etc.).
- [ ] **Future damages exceed 60% of total demand** — possible projection-table inflation; verify the math.
- [ ] **The today-number equals the trial anchor** — that's not a two-step anchor, that's just a single number with extra prose.

When any flag fires, present the issue to the attorney for an explicit decision before output.

---

## 14. Banner / Salutation / Signature Final Check

- [ ] Document-type banner is the first body element after the RE block (or after the confidentiality marking if used).
- [ ] No "Dear Mediator:" salutation in a mediation paper.
- [ ] Signature block ends with "Sincerely," and three blank lines for handwritten signature above the typed name.
- [ ] No bar number repeated below the signature unless firm convention requires it.
- [ ] PS line (if any) is on its own line below the signature, formatted per `house-style.md` §10.

---

## 15. Attachment List Sanity

- [ ] Attachment list is at the very end of the document.
- [ ] List uses "Exhibit 1 — [description]" format consistently.
- [ ] List matches the body's exhibit references exactly.

---

## 16. Tone Register Sanity Check

Pick the tone register that matches the mode and verify the draft holds to it:

- [ ] `mode = demand` → clinical, transactional, math-forward; short sentences; no human-portrait paragraph; no emotional intensifiers; no narrative shifts; reads like a litigation document.
- [ ] `mode = mediation_paper` → narrative, humanizing, persuasive; sentences vary in length; opens with a human portrait; uses block quotes; signals BATNA via the policy-limits posture statement; no response deadline; no math-only paragraphs without surrounding context.
- [ ] `mode = hybrid` → mediator-addressed with long-demand internal structure; tonal shifts allowed by section (narrative in INTRODUCTION; transactional in SPECIAL DAMAGES); attorney should approve the blend.

Tonal drift check: if the demand has emotional language or a human-portrait paragraph, consider switching to mediation_paper mode. If the mediation paper reads like a transactional letter, consider strengthening the INTRODUCTION and DAMAGES narrative.

---

## 17. Section-Label Mixing Detection

- [ ] No document mixes two label systems (e.g., "A. FACTS" followed by "II. LIABILITY" in the same paper).
- [ ] Sub-section labels follow the parent system (Roman-parent uses A./B./C. subs; letter-parent uses 1./2./3. or a./b./c. subs).
- [ ] No section is labeled both "Section 1:" and "A." anywhere in the same document.

---

## 18. Multi-Plaintiff Handling

If the case has more than one plaintiff (spouse, child, passenger):
- [ ] Primary plaintiff identified explicitly in the introduction.
- [ ] Co-plaintiff(s) have their own clearly labeled subsections in the DAMAGES section (separate injuries, separate ADL impact, separate medical specials, separate GD buckets, separate demand component).
- [ ] RECAP table lists each plaintiff's component or has a per-plaintiff column.
- [ ] DEMAND statement specifies the total inclusive of all plaintiffs OR is broken out per plaintiff.

---

## 19. Final Read-Through

- [ ] Read the entire document from top to bottom one time, looking for:
  - Sentence-level grammar errors not caught by typo fixes
  - Run-on sentences (especially in damages narrative)
  - Awkward shifts in tense or voice
  - Repeated phrases ("the subject crash" overused — vary to "the subject collision" / "the subject incident")
  - Orphaned section headers with no content
  - Tables that overflow the page width (rebuild as needed)
  - Page breaks in awkward spots (split tables, headers separated from content)

---

## After QA Passes

Generate the .docx via the `docx` skill. Save to:
- If a case-root path was provided: `[case_root]/04 - Settlement & Mediation/[ClientLastName] - [Document Type] - [YYYY-MM-DD].docx`
- Otherwise: the working folder, with a `computer://` link for the user

Then present:
1. The final document (with `computer://` link)
2. The list of `[VERIFY]`, `[RESEARCH]`, `[ATTORNEY-DECISION]`, and `[GAP]` flags for attorney review
3. A one-paragraph summary: case identifier, mode used, demand number, recap totals
4. Companion-skill suggestions (e.g., re-running the medical chronology if it was stale)

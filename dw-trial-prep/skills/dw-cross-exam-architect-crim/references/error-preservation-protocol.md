# Error Preservation Protocol

**Loaded at Step 0.5; applied at Step 4 and Step 5.5. Read before drafting any chapter carrying a flag. Every flag in a cross-examination outline must carry a preservation instruction.**

A cross-examination that gets shut down and is not preserved is an appellate issue thrown away. This skill flags questions that may draw an objection — `[SCOPE FLAG]`, `[608(B) REVIEW REQUIRED]`, `[ART. 608(B) — arguing constitutional exception]`. A flag without a preservation instruction is only half the work.

---

## 1. The Two Rules

**La. C.Cr.P. art. 841 — contemporaneous objection.** *"An irregularity or error cannot be availed of after verdict unless it was objected to at the time of occurrence."* The party must make known the action desired, or the objection and its grounds, **when the ruling occurs**. No bills of exception required. Nothing preserved at the moment is generally reviewable later.

**La. C.E. art. 103(A)(2) — offer of proof for excluded evidence.** Error may not be predicated on a ruling excluding evidence unless a substantial right is affected **and** *"the substance of the evidence was made known to the court by counsel."*

Read together: when the court kills a line of cross, you must (a) state your grounds on the record at that moment, and (b) put the substance of what the witness would have said into the record. Doing only (a) preserves the objection but leaves the appellate court unable to assess prejudice.

`[VERIFY current text]` — both articles quoted from published sources as of this skill revision; Louisiana amends frequently.

---

## 2. Drafting Rule — Every Flag Carries a Proffer Line

Whenever a chapter contains a flagged question, that question gets a **Preservation Log row** with `Ground to state` and `Proffer substance` pre-filled. Preservation text never appears on a chapter page — the chapter table is `SOURCE/EXHIBIT | QUESTIONS` and closes with a blank notes box. **The canonical format lives in `assets/preservation-log.md` — copy it from there, do not restate it.**

Because the grounds are no longer beside the question, name the affected chapters and questions when delivering the package. An attorney working only from the chapter pages is working without them.

Never write "object and preserve." Name the ground and name the substance. An attorney reading the outline mid-cross has no time to compose either.

---

## 3. Grounds by Flag Type

| Flag | Ground to state on the record | What to proffer |
|---|---|---|
| `[SCOPE FLAG]` — state court | La. C.E. art. 611(B): cross extends to any matter relevant to any issue, including credibility. Scope-of-direct is not the Louisiana rule | The answers sought and their relevance to a contested issue |
| `[SCOPE FLAG]` — federal court | FRE 611(b) plus the court's discretion to allow inquiry as if on direct | Same |
| `[608(B) REVIEW REQUIRED]` | The material is not offered as character evidence. It is bias/interest/corruption under art. 607(D)(1), or an attack on the truthfulness **or accuracy of this testimony** under art. 607(C), or a prior inconsistent statement under art. 613 — name which | The specific facts and their bearing on this witness's account |
| Constitutional exception to art. 608(B) | Sixth Amendment confrontation; *Davis v. Alaska*; La. Const. art. I, § 16 | The full line of questioning and why exclusion prevents meaningful confrontation |
| Confrontation — surrogate analyst | *Crawford*; *Melendez-Diaz*; *Bullcoming*; *Smith v. Arizona* (2024). See `confrontation-and-surrogate-analysts.md` | What cross of the actual analyst would have exposed |
| Impeachment by conviction refused | La. C.E. art. 609.1(A) — every witness in a criminal case subjects himself to examination on convictions | The conviction, date, offense, sentence, and its source |
| Extrinsic proof of bias refused | La. C.E. art. 607(D)(1) — extrinsic evidence of bias, interest, corruption, or defect of capacity **is admissible** | The evidence itself and the bias it establishes |

---

## 4. Mechanics — Get It Into the Record

1. **Object or respond at the moment of the ruling.** Art. 841 is unforgiving about timing.
2. **State the specific ground.** "Objection" alone preserves nothing. A ground stated for the first time on appeal is generally waived.
3. **Ask to proffer outside the jury's presence.** Courts routinely allow it; the request itself is on the record even if refused.
4. **Proffer in the strongest available form**, in this order of preference:
   - Question-and-answer proffer with the witness on the stand, jury excused — the best record
   - Counsel's detailed statement of the expected testimony
   - The excluded document marked and filed into the record under seal if necessary
5. **Get a ruling.** An objection the court never rules on may not be preserved. If the court defers, renew it.
6. **Note the ruling in the trial notebook** for `dw-appellate-error-monitor-crim` and `dw-issue-code-tracker-crim`.

---

## 5. Appendix to Every Outline — Preservation Log

Append the Preservation Log to the end of every cross-examination outline. Chapter, Question #, Ground to state and Proffer substance are pre-filled at build time; Ruling, Proffer made, Form of proffer and Issue code are filled in during trial. **The canonical table lives in `assets/preservation-log.md`.**

**Handoff:** at the end of the trial day, this log feeds `dw-appellate-error-monitor-crim` (harmless-error pre-assessment) and `dw-issue-code-tracker-crim`. A sustained objection with no proffer should be flagged in the log as **UNPRESERVED** so the attorney can decide whether to revisit it before the State rests.

---

## 6. Guardrail

Do not draft a flagged question without its preservation bullet. If the skill cannot articulate a ground and a proffer for a flagged question, that is a signal the question may not be worth asking — surface that to the attorney rather than burying the flag.

# MODULE B — Missed Objection Identifier (Reference)

This module identifies every objectionable event during the proceedings where NO objection was made by defense counsel. These are presumptively waived issues unless they qualify as errors patent under Art. 920 or structural errors.

## Missed Objection Categories

Systematically review the transcript for the following categories of objectionable events:

**Category 1 -- Evidentiary Errors (No Objection):**

- Hearsay admitted without objection (La. C.E. Art. 802)
- Improper character/other crimes evidence admitted without objection (La. C.E. Art. 404, La. C.E. Art. 404(B))
- Confrontation Clause violations without objection (*Crawford v. Washington*, 541 U.S. 36 (2004))
- Expert testimony without adequate foundation (La. C.E. Art. 702, *Daubert v. Merrell Dow*, 509 U.S. 579 (1993))
- Privileged communications disclosed without objection
- Leading questions on direct examination without objection
- Improper lay opinion testimony without objection (La. C.E. Art. 701)
- Authentication failures without objection (La. C.E. Art. 901)
- Best evidence rule violations without objection (La. C.E. Art. 1002)

**Category 2 -- Prosecutorial Misconduct (No Objection):**

- Improper closing argument (commenting on defendant's silence, vouching for witness credibility, appealing to jury sympathy, misrepresenting evidence)
- Improper questioning of witnesses
- Discovery violations disclosed during trial
- *Brady* material disclosed late or not at all (note: *Brady* violations may be reviewable regardless of objection -- *Brady v. Maryland*, 373 U.S. 83 (1963))

**Category 3 -- Jury Instruction Errors (No Objection):**

- Failure to instruct on responsive verdicts
- Incorrect statement of the law in jury instructions
- Failure to give a requested defense instruction
- Failure to instruct on the presumption of innocence or burden of proof
- Improper Allen charge (*Allen v. United States*, 164 U.S. 492 (1896))

**Category 4 -- Procedural Errors (No Objection):**

- Violation of sequestration order
- Juror misconduct observed but not raised
- Batson violations not raised (*Batson v. Kentucky*, 476 U.S. 79 (1986))
- Improper contact between State witnesses and jury
- Unauthorized communications with the jury

## Missed Objection Output Format

For each missed objection identified:

| Field | Content |
|-------|---------|
| **MO-#** | Sequential identifier (MO-001, MO-002, etc.) |
| **Transcript Location** | Page/line reference |
| **What Happened** | Factual description of the objectionable event |
| **What Objection Should Have Been Made** | The objection type and legal basis |
| **Why It Was Objectionable** | Brief legal analysis |
| **Preservation Status** | WAIVED -- unless errors patent or structural error exception applies |
| **Salvage Pathway** | Can this issue be raised through: (a) errors patent (Art. 920); (b) structural error; (c) ineffective assistance of counsel (post-conviction only); (d) plain error (extremely limited in Louisiana); (e) Brady/Giglio (if applicable) |
| **Prejudice Assessment** | How significant was this error to the outcome? (Critical / Significant / Minor / De minimis) |

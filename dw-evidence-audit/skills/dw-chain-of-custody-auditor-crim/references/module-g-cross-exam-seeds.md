# Module G — Cross-Examination Seeds

For each CRITICAL and SIGNIFICANT deficiency identified in Modules A through F, generate cross-examination question sets targeting the specific handler, custodian, or analyst responsible for the deficiency.

## Cross-Examination Architecture for Chain of Custody Witnesses

Chain of custody cross-examination follows a specific structure: establish the standard, then demonstrate the failure to meet it.

**Phase 1 — Establish the Standard (Training & Policy):**
```
Q: You received training in evidence handling procedures, correct?
Q: Your department has written standard operating procedures for evidence handling?
Q: Those SOPs require [specific procedure], don't they?
Q: And you're familiar with those requirements?
Q: In fact, you've been trained that failure to follow those procedures can compromise evidence integrity?
```

**Phase 2 — Demonstrate the Failure:**
```
Q: Now, looking at [evidence item], your evidence log shows you collected this item at [time], correct?
Q: But the evidence room intake log shows it wasn't booked until [later time/date], correct?
Q: That's [X hours/days] between collection and booking?
Q: During those [X hours/days], where was this evidence?
Q: There's no documentation showing where this evidence was during that period, is there?
Q: So you can't tell this jury with certainty that no one else handled this evidence during that time?
```

**Phase 3 — Establish the Significance:**
```
Q: You'd agree that the purpose of chain of custody documentation is to ensure evidence hasn't been tampered with or contaminated?
Q: And when there's a gap in the documentation, you can't assure the jury that the evidence wasn't tampered with during that gap, can you?
Q: In fact, the whole point of maintaining a chain of custody is so that questions like this don't arise, correct?
```

## Cross-Exam Seed Template

For each deficiency, produce:

```
CROSS CHAPTER SEED — [Deficiency Title]
Evidence Item: [Item number / description]
Witness Type: Evidence Custodian / Crime Scene Technician / Lab Intake Technician / Transport Officer / Forensic Analyst
Chapter Goal: [What this chapter must establish — e.g., "Establish that the evidence was unaccounted for during a 72-hour period between collection and booking"]
Deficiency: [Specific chain failure]
Severity: CRITICAL / SIGNIFICANT

Key Questions:
  Q1: [Question establishing the standard — what should have been done]
  Q2: [Question demonstrating the failure — what actually happened (or didn't)]
  Q3: [Question establishing the significance — why the gap matters]
  Q4: [Question closing the loop — the witness cannot assure the jury that the evidence was not compromised]

Source: [Chain of custody document / evidence log / property receipt — page reference / Bate stamp if available]
Impeachment Note: [If the witness's report claims compliance but the documentation shows otherwise, or if the witness's own SOP contradicts their actions]
Legal Authority: [La. C.E. Art. 901(B)(1); State v. Toney; applicable standard]

[READY FOR CROSS-EXAM ARCHITECT — pass to dw-cross-exam-architect-crim skill]
```

## Cross-Examination Integration Checklist

For each CRITICAL and SIGNIFICANT finding, auto-generate cross-examination chapter seeds formatted for the **dw-cross-exam-architect-crim** skill.

For each finding, ensure:

1. **The standard is established first** — the witness must agree to the proper procedure before being confronted with the failure.
2. **The failure is demonstrated through documents** — use the chain of custody paperwork (or absence thereof) as the primary tool, not the witness's oral testimony.
3. **The significance is driven home** — the witness must concede that the purpose of chain documentation is to prevent the very problem that the gap creates.
4. **The closing question leaves no escape** — "You cannot assure this jury that the evidence was not [tampered with / contaminated / substituted / degraded] during that period, can you?"

Tag each seed: `[READY FOR CROSS-EXAM ARCHITECT — pass to dw-cross-exam-architect-crim skill]`

# Defense Witness Lineup Audit — Step 0.6 Detail

Read at SKILL.md STEP 0.6 (Defense Witness Lineup Audit): scope, per-witness risk score axes, defendant testify-or-not routing, default sequencing, and the Lineup Report table.

---

### Scope & Objective

**Pre-check:** If `dw-witness-statement-analyzer-crim` has produced defense-favorable Analysis Cards and if `dw-expert-witness-evaluator-crim` has produced Daubert-survival vettings for proposed defense experts, import those findings.

For every proposed defense witness, the audit answers four questions:
1. Will calling this witness do more good than harm?
2. What is the risk score on cross?
3. Where in the trial order do they belong?
4. If the witness is the defendant — testify or not?

### Defense Witness Risk Score (per witness)

Rate each witness 1–5 on each axis:

| Axis | 1 (low risk) | 5 (high risk) |
|------|--------------|---------------|
| **Cross-attack surface** | No prior statements, no record, no bias | Multiple prior statements, La. C.E. art. 609.1 convictions, obvious bias |
| **Witness temperament** | Calm, controllable, articulate, sticks to scope | Hostile, evasive, talkative, prone to argue with State |
| **Corroboration depth** | Independently corroborated by documents/data | Witness's word only |
| **Necessity to defense theory** | Mission-critical (no alternative) | Nice-to-have; theme reachable without them |
| **State's prep level** | State has minimal material on this witness | State has full file, prior testimony, jail calls, etc. |

**Total risk score = sum / 25.** Witnesses scoring 18+ get a "call only if necessary" flag; scoring 22+ get a "do not call absent override" flag.

### Defendant Testify-or-Not Decision

If the defendant is a candidate witness, route to `references/defendant-testify-decision-matrix.md` and complete the weighted matrix. Document the decision in writing with an attorney signature line and reaffirm on the morning of trial. The decision is the defendant's alone (Rock v. Arkansas, 483 U.S. 44 (1987)); counsel advises.

### Sequencing

Default defense case order (adjust to strategy):
1. **Foundation / custodial witnesses** first (short, in/out, lay predicate for defense exhibits)
2. **Corroboration witnesses** (alibi, third-party suspect, surveillance custodian)
3. **Defense experts** (after their underlying facts are in evidence)
4. **Character witnesses** (close to the defendant's testimony if both are called)
5. **Defendant** (if called) — usually last so attorney has heard all State and defense witnesses first and the defendant can speak to the full record

### Deliverable: Defense Witness Lineup Report

Output a table:

| Order | Witness | Type | Risk Score | Necessity | Call? (Y/N/Maybe) | Notes |
|-------|---------|------|------------|-----------|-------------------|-------|
| 1 | [Name] | [Foundation / Alibi / Expert / Character / Defendant] | __/25 | High/Med/Low | Y/N/Maybe | [Sequencing rationale] |
| ... | ... | ... | ... | ... | ... | ... |

Share with the attorney. Do not proceed to STEP 1 until the lineup is confirmed.

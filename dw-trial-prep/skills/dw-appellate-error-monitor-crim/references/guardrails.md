# Guardrails — Accuracy, Scope, Constitutional Sensitivity, Document Handling

Loaded at SKILL.md **STEP 0.5** and applied to every output; full guardrail text and the uncertainty-flag vocabulary.

---

### Accuracy & Honesty
- **Never fabricate case citations.** If you are unsure whether a case exists or states the proposition attributed to it, flag it with `[VERIFY CITATION -- confirm this case exists and states this proposition]`.
- **Never overstate preservation.** If an issue is waived, say so clearly. The appellate attorney's credibility depends on honest assessment. Filing an appellate brief that raises waived issues damages credibility with the court and wastes limited briefing resources.
- **Never understate preservation failures.** If trial counsel failed to preserve an issue, document the failure precisely. The client's appellate rights depend on accurate identification of what is and is not available on appeal.
- **Acknowledge uncertainty.** If the transcript is ambiguous about whether an objection was made, the court's ruling was unclear, or the proffer was incomplete, state precisely what is uncertain and what additional records would resolve the ambiguity.

### Scope Limitations
- **This skill monitors error preservation -- it does not write the appellate brief.** The skill identifies, classifies, and ranks appellate issues. The appellate attorney drafts the brief, selects the final assignments of error, and makes all strategic decisions about which issues to raise and how to frame them.
- **Do not give appeal advice.** Present the analysis and rankings, but the decision about which issues to raise, which to preserve, and which to concede belongs to the appellate attorney in consultation with the client.
- **Do not predict appellate outcomes.** Present the harmless error pre-assessment honestly, but do not predict whether the appellate court will reverse. Appellate panels are unpredictable; prepare the strongest possible brief regardless of predicted outcome.
- **IAC claims are for post-conviction.** This skill identifies potential IAC claims but recognizes that in Louisiana, IAC is generally a post-conviction claim requiring an evidentiary hearing. Do not conflate direct appeal issues with post-conviction issues unless the record is sufficient for direct appeal IAC review.

### Constitutional Sensitivity
- **Appellate preservation failures can result in the permanent loss of a client's constitutional rights.** A waived Confrontation Clause issue, a waived illegal search claim, or a waived excessive sentence challenge cannot be recovered on direct appeal. Approach every preservation analysis with the gravity it deserves.
- **Post-conviction is not a guaranteed safety net.** While IAC claims can sometimes salvage waived issues, post-conviction relief is procedurally difficult, subject to strict time limitations (La. C.Cr.P. Art. 930.8 -- two-year prescriptive period), and requires a showing of both deficient performance and prejudice. Prevention (proper preservation at trial) is always preferable to cure (IAC claim in post-conviction).

### Document Handling
- **Attorney verification required.** Every output from this skill is a draft for attorney review. The attorney must independently verify all factual assertions, confirm citation accuracy, and make all strategic decisions.
- **Flag everything uncertain.** Use the following flags throughout all outputs:
  - `[VERIFY -- confirm this fact with transcript/records]` -- factual assertions not directly sourced from uploaded documents
  - `[VERIFY CITATION -- confirm current validity]` -- case law that may have been modified, overruled, or distinguished
  - `[ATTORNEY TO COMPLETE]` -- signature blocks, dates, bar numbers, and information requiring attorney input
  - `[STRATEGIC DECISION]` -- points where attorney judgment is required (which issues to raise, how to frame them, whether to seek writs or wait for appeal)
  - `[TRANSCRIPT NEEDED]` -- portions of the record that must be obtained before the analysis can be completed
  - `[RESEARCH NEEDED]` -- areas where additional legal research would strengthen the analysis

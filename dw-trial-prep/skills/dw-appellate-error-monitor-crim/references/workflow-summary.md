# Workflow Summary

Read at SKILL.md **WORKFLOW SUMMARY** (end of procedure) — the step/module tree and the eight output types.

---

```
STEP 0: File Intake Hard Stop
  +-- Wait for user to confirm all uploads complete

STEP 1: Information Gathering
  +-- Collect Essential -> Strategic -> Contextual tiers
  +-- Flag missing items; request before proceeding

STEP 2: Louisiana Appellate Framework Review
  +-- Confirm applicable law (Art. 841, Art. 920, Art. 103, etc.)
  +-- Identify procedural posture (pretrial, trial, post-trial, appeal)

MODULE A: Real-Time Objection Tracker
  +-- Log every objection from transcript
  +-- Assess timeliness, specificity, and court ruling
  +-- Classify as PRESERVED / PARTIALLY PRESERVED / WAIVED

MODULE A.5: Landmine Preservation Protocol
  +-- Cross-reference Module A + Step 1.5 to identify dangerous waiver risks
  +-- Rank by Danger Level (FATAL / SERIOUS / MODERATE)

MODULE B: Missed Objection Identifier
  +-- Identify objectionable events with no objection
  +-- Categorize by type (evidentiary, prosecutorial misconduct, jury instruction, procedural)
  +-- Assess salvage pathways (errors patent, structural, IAC)

MODULE C: Proffer Compliance Monitor
  +-- Verify proffer for every excluded evidence ruling
  +-- Assess Art. 103(A)(2) compliance
  +-- Flag waived exclusion issues

MODULE D: Errors Patent Checklist
  +-- Audit for illegal sentence, Boykin deficiency, Art. 873 delay,
      defective charging instrument, and additional errors patent
  +-- Identify issues reviewable without objection

MODULE E: Post-Trial Motion Generator
  +-- Generate Motion for New Trial (Art. 851)
  +-- Generate Motion in Arrest of Judgment (Art. 858) if applicable
  +-- Generate Motion to Reconsider Sentence (Art. 881.1)

MODULE F: Harmless Error Pre-Assessment
  +-- Classify each preserved error (structural vs. trial error)
  +-- Apply Chapman (constitutional) or Art. 921 (non-constitutional) standard
  +-- Assess reversal likelihood for each preserved error

MODULE G: Ineffective Assistance of Counsel Audit
  +-- Identify potential Strickland claims from record
  +-- Assess deficient performance and prejudice for each
  +-- Determine direct appeal vs. post-conviction availability

MODULE H: Appellate Issue Ranking
  +-- Rank all issues by reversal likelihood (Tiers 1-5)
  +-- Produce appellate issue ranking memo (consumed by dw-appellate-brief-builder-crim)

MODULE I: Record Designation Checklist
  +-- Verify all necessary transcripts and documents designated
  +-- Identify gaps and prepare supplementation motion if needed

OUTPUTS: Generate applicable outputs based on case needs:
  1. Error preservation log (objection tracking table)
  2. Preserved vs. waived issues matrix
  3. Post-trial motion package (new trial, arrest of judgment, reconsider sentence)
  4. Appellate issue ranking memo
  5. Record designation checklist
  6. Anders brief trigger analysis (appointed cases)
  7. Writ application framework (interlocutory review)
  8. IAC audit report (post-conviction roadmap)
```

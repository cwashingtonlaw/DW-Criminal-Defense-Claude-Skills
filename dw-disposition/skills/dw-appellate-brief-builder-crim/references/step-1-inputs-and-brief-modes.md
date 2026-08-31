# Step 1 Input Contract & Step 2 Brief Modes

Read at SKILL.md Step 1 (Information Gathering Protocol) and Step 2 (Determine Brief Type and Mode); also holds the scope-exclusion list from the skill introduction.

## Scope — what this skill does NOT cover

This skill does NOT cover:
- **Post-conviction relief** (route to `dw-post-conviction-relief-crim`)
- **Federal habeas corpus** under 28 U.S.C. § 2254 (route to `dw-post-conviction-relief-crim`)
- **Pretrial supervisory writ applications** — those are interlocutory and use the writ-application framework in `dw-appellate-error-monitor-crim`'s WRIT APPLICATION FRAMEWORK section
- **Motion drafting** at the trial court level (route to `dw-suppression-motion-crim`, `dw-404b-opposition-crim`, or `dw-pretrial-motion-library-crim`)
- **Error preservation** during trial (that is `dw-appellate-error-monitor-crim`'s job — by the time you reach this skill, preservation analysis is already done)

## Step 1 — Information Gathering Protocol (full text)

Before drafting any portion of the brief, collect the following inputs from the attorney and from prior skill outputs. **The brief cannot be drafted from scratch — it depends on a completed error-preservation audit.**

### Essential — INPUT CONTRACT FROM dw-appellate-error-monitor-crim

The brief builder consumes the following deliverables produced by `dw-appellate-error-monitor-crim`. If any of these are missing, **STOP and route the user to run `dw-appellate-error-monitor-crim` first**:

1. **Ranked appellate-issue output (Module H — Appellate Issue Ranking):** the table or memo listing every preserved error ranked by reversal likelihood (Tiers 1-5), with preservation status, error type (structural/constitutional/non-constitutional), harmless-error risk, and tier classification. This becomes the assignments-of-error list.

2. **Designated appellate record (Module I — Record Designation Checklist):** the complete list of designated record items — charging instrument, arraignment transcript, pretrial hearing transcripts, voir dire transcript, trial transcript (all volumes), jury instruction conference transcript, jury instructions as read, verdict form, sentencing transcript, post-trial motion transcripts, minute entries, exhibits, written motions and orders, juror questionnaires, PSI (if any), commitment order. The brief's record cites must reference designated items only.

3. **Post-trial motion package (Module E — Post-Trial Motion Generator):** the Motion for New Trial (Art. 851), Motion in Arrest of Judgment (Art. 858) if applicable, and Motion to Reconsider Sentence (Art. 881.1). The disposition of these motions appears in the Statement of the Case, and the motions themselves often preserve issues that anchor specific assignments of error.

4. **Errors patent findings (Module D):** any errors patent identified — illegal sentence, Boykin deficiency, Art. 873 delay violation, defective charging instrument, unauthorized restriction of benefits, etc. These become a separate assignment (or an "Errors Patent" section per local practice).

5. **Harmless-error pre-assessment (Module F):** the per-issue harmless-error analysis — Chapman (constitutional) or Art. 921 (non-constitutional) — that pre-graded each preserved error for prejudice. Feeds the Prejudice section of each assignment's Argument.

### Essential — Case-specific facts the attorney must supply

6. **Charges:** All counts as charged, with La. R.S. citations. (Drives Statement of the Case.)
7. **Verdict / Disposition:** Outcome on each count — guilty, not guilty, mistrial, responsive verdict, jury or bench trial. (Statement of the Case.)
8. **Sentence imposed:** The sentence on each count, including habitual offender enhancements, consecutive/concurrent designations, restrictions on benefits, special conditions. (Statement of the Case + sentencing assignments.)
9. **Notice of appeal / Order granting appeal:** Date filed, date granted. Establishes appellate jurisdiction and timing.
10. **Appellate court designation:** Which Louisiana circuit (1st, 2nd, 3rd, 4th, 5th) or whether the case is before the Louisiana Supreme Court. Drives circuit-specific formatting.

### Strategic (request if not provided)

11. **Defense theory at trial:** Frames the Statement of Facts narrative and informs which factual emphasis to apply.
12. **Lead trial counsel and appellate counsel:** Whether lead trial counsel is also handling the appeal (affects what arguments are politic to make about trial counsel performance) or whether new appellate counsel is briefing.
13. **Anders posture:** Whether appointed counsel has concluded the appeal is wholly frivolous and is preparing an Anders/Benjamin/Jyles no-merit brief instead. (This skill drafts merits briefs; route Anders to `dw-appellate-error-monitor-crim`'s Anders Brief Trigger Analysis.)
14. **State's brief (for reply-brief mode):** If drafting a reply, the State's appellee brief is essential.
15. **Co-defendant appellate status:** Whether co-defendants are also appealing — relevant for Bruton issues, severance issues, and joint-brief considerations.
16. **Local clerk's order:** Any scheduling order setting brief due dates or extensions granted.

**Present missing essential inputs (1-10) as a ranked checklist before drafting.** If items 1-5 (the dw-appellate-error-monitor-crim output package) are missing, do not draft — instead say:

> *"To draft the appellate brief, I need the ranked-issue output, designated record, post-trial motion package, errors-patent findings, and harmless-error pre-assessment from `dw-appellate-error-monitor-crim`. Those upstream deliverables tell me which assignments of error to brief, what the preservation status is for each, and what the harmless-error landscape looks like. Please run `dw-appellate-error-monitor-crim` first, then return here with its outputs."*

If items 6-10 are missing but 1-5 are present, request the case-specific facts before proceeding.

## Step 2 — Brief modes (full text)

The skill operates in three modes. Identify the mode at the start of the engagement.

### Mode A — Appellant's Original Brief (default)

The opening brief on the merits filed by the convicted defendant as appellant. Covers Statement of the Case, Statement of Facts, Assignments of Error, Argument, Conclusion. This is the modal output.

### Mode B — Reply Brief

The defendant's response to the State's appellee brief. Cabined scope: respond to State's arguments, no new arguments raised for the first time. Length is half the original brief or less. Use Module H (Reply Brief Companion Module) below.

### Mode C — Writ Application to the Louisiana Supreme Court (Direct Appeal)

After the court of appeal rules, the losing party may apply for a supervisory or certiorari writ to the Louisiana Supreme Court under La. Sup. Ct. Rule X. The format differs from a court-of-appeal brief — it is a writ application with specific cover-page, jurisdictional-statement, and length requirements. See `references/circuit-formatting-rules.md` Section 6 (La. Sup. Ct.).

> Note: This skill covers writ applications taken FROM a court-of-appeal direct-appeal decision. It does NOT cover pretrial supervisory writs (those go through the writ framework in `dw-appellate-error-monitor-crim`) or post-conviction writs (those go through `dw-post-conviction-relief-crim`).

**Mode selection:** Ask the attorney explicitly at the outset which mode is in play. If unclear from the prompt, default to Mode A.

# Phase 3 Step 3 — Defense Shield & Defense Matrix Procedure (Detailed)

This file contains the full procedural detail for Phase 3 Step 3 (Defense Shield & Defense Matrix). The SKILL.md spine summarizes Step 3 and points here; this file is the operating manual.

⚠ **Follow the Case Tables Write Protocol before modifying `Case Tables.xlsx`.** See `case-tables-write-protocol.md`.

This step has three parts: first, build the case-specific **Defense Shield** (the universe of potential defenses filtered to this case); then populate the **Defense Matrix** (charges mapped to the defenses you'll actually run); then initialize the **Running List** for ongoing tracking through trial.

---

## 3A — Build the Case-Specific Defense Shield

The `Case Tables.xlsx` template contains **Defense Shield templates** — comprehensive catalogs of potential defenses organized by case type. These templates exist on the `Legal Defenses (Rape)` and `Legal Defenses (Homicide)` sheets. They are reference libraries, not checklists. Rarely if ever will every defense apply to a given case. Your job is to analyze the case facts and build a case-specific shield containing only the defenses that have traction.

### If a template exists for this case type (currently: Rape, Homicide)

1. **Read the full template sheet** for this case type. Each row represents a potential defense category with columns for: Defense Category, Specific Defense, Priority/Feasibility, Key Action/Theory, Critical Expert/Witness Needed, Evidence Source/Location, and Litigation Checkpoint.

2. **Evaluate every defense row against the actual case facts.** For each potential defense, ask:
   - Does the discovery contain evidence supporting this defense?
   - Does the Case Profile (Section 6 — Case-Specific Defenses) flag facts relevant to this defense?
   - Do the 8 Case Analysis Reports identify weaknesses in the State's case that this defense exploits?

3. **Populate only the applicable defenses.** For each defense that has factual support in this case:
   - Keep the template's strategic guidance (Key Action/Theory column) as a starting framework
   - **Replace generic placeholders** with case-specific facts, Bate stamp references, witness names, and evidence locations from the actual discovery
   - **Update the Priority/Feasibility** column (High/Med/Low) based on the strength of the case-specific evidence — not the template default
   - **Fill in** the Critical Expert/Witness and Evidence Source columns with the actual witnesses and documents from this case file

4. **Remove defenses that clearly don't apply.** If a defense has zero factual support in the discovery (e.g., "Misidentification" in a case where identity isn't in dispute), delete that row from the case-specific sheet. A lean, focused shield is more useful than an exhaustive one full of inapplicable theories.

5. **Flag borderline defenses for attorney review.** When a defense has some factual support but isn't clearly viable — or when its applicability depends on facts only the attorney or client knows — mark it with a `⚖ ATTORNEY REVIEW` tag in the Priority column. Present these to the attorney with a brief explanation of what makes it borderline, and ask whether to keep or discard.

### If no template exists for this case type (e.g., drug offenses, DWI, weapons charges, theft/fraud, domestic violence)

Build a new Defense Shield from scratch following the same column structure as the existing templates. The process:

1. **Research the charge elements** under Louisiana statutes. Identify what the State must prove for each count.
2. **Catalog potential defenses** organized by category (Constitutional, Identity, Forensic, Credibility, Mens Rea, Investigation, Procedural, etc.). Use the Rape and Homicide templates as structural models — the defense *categories* often overlap across case types even when the specific defenses differ.
3. **For each defense**, fill in all 7 columns: Defense Category, Specific Defense, Priority/Feasibility, Key Action/Theory of the Case, Critical Expert/Witness Needed, Evidence Source/Location, and Litigation Checkpoint.
4. **Populate only case-applicable defenses** — follow the same filtering logic as above.
5. **Save the new template** as a new sheet in `Case Tables.xlsx` named `Legal Defenses ([Case Type])` so it's available for future cases of the same type.

### Also populate the "Dealing with States Narrative" sheet

This sheet contains 13 counter-narrative strategies (Ignore It, Make Lemonade, Backchain, Clarify & Polarize, Absurd, Use the Mirror, Moral Core, Own It, Drop It, Context, Undermine, Rules, Exclude It). The template includes both Rape-specific and Homicide-specific application columns. For this case:
- Link each strategy to the defense categories you've identified as applicable
- Write case-specific applications showing how each strategy applies to the actual facts and witnesses
- Not every strategy will be useful — populate only the ones that map to your defense theories

---

## 3B — Populate the Defense Matrix

Now that the Defense Shield identifies *which* defenses apply, the Defense Matrix maps them to *specific charges*. Populate the Defense Matrix sheet in `Case Tables.xlsx`. Complete all 7 columns.

- **Charge column:** list each offense charged AND all responsive verdicts on separate rows
- Review `Art 814 Responsive Verdicts` document in `Trial Notebook → 01 - Jury Instructions & Selection`
- For each charge/responsive verdict row, pull the applicable defenses from the Defense Shield you just built
- Cross-reference: every defense in the Shield should map to at least one charge in the Matrix; any defense that doesn't map to a charge may not belong in the Shield
- Route jury instruction research and drafting to **dw-jury-instructions-builder** for comprehensive instruction set
- Route voir dire strategy to **dw-voir-dire-assistant** for juror challenge guidance

---

## 3C — Initialize the Running List

The `Running List` sheet tracks defenses as they are discovered or refined throughout the life of the case. It has three columns: Litigation Phase, Defenses Raised/Discovered, and Source. The phases are pre-populated (Discovery, Motions, Witness notes, Exhibits, Demonstratives, Case Vocab, Voir Dire, Open/Close).

At this point, populate the Running List with any defenses already identified during Phases 1 and 2. As the case progresses through motions, witness prep, and trial, update the Running List whenever a new defense theory emerges or an existing one gains/loses support. The Running List feeds back into the Defense Shield — if a new defense surfaces during motions practice, add it to the Shield and Matrix.

# Output Format — Generation Strategy, Document Structure, File Naming

Read at Output Format of `dw-jury-focus-group-crim/SKILL.md` — moved verbatim from SKILL.md (the Saving rules remain inline in SKILL.md).

---

### Generation Strategy — Build in Sections

This report is large (typically 800–1,200 lines of content). Trying to generate it all in a single docx-js script will lead to truncation — the model will run out of room and start cutting corners (writing 2 bios instead of 36, dropping demographic categories, summarizing instead of analyzing).

Instead, build the document in stages:

1. **First pass**: Generate the docx-js script with the document structure, demographic summary table, and case presentation sections (Steps 1A and 2). Write juror bios as data arrays that the script iterates over — define all 36 juror objects with their full bio text.
2. **Second pass**: If the script is getting too long, split generation into two scripts — one that creates the base document, and a second that adds the juror analysis section (Step 3) and strategic recommendations (Step 4) using the unpack/edit XML/repack workflow from the docx skill.

The key principle: the final document must contain the complete content for all 4 steps. If you find yourself writing placeholder text like "remaining jurors detailed in full report" or "see complete analysis" — stop. That means the generation strategy needs restructuring, not the content.

### Document Structure

```
JURY FOCUS GROUP SIMULATION REPORT
[Case Name] — [Parish] Parish

1. PANEL COMPOSITION
   - Demographic Summary Table
   - Individual Juror Profiles (36 bios)

2. CASE PRESENTATION
   - Defense Narrative (FABARC)
   - Prosecution Summary

3. JUROR-BY-JUROR ANALYSIS
   - Verdict predictions table (summary)
   - Individual juror analysis cards

4. STRATEGIC RECOMMENDATIONS
   - Verdict Tally & 12-Person Projection
   - Favorable / Dangerous / Swing Jurors
   - Theme Effectiveness Rankings
   - Prosecution Vulnerabilities
   - Voir Dire Strategy
```

### File Naming

Follow D&W convention: `[3-digit prefix] - Jury Focus Group Report.docx`

If a case folder exists with existing numbered documents, use the next available prefix. If no folder exists, use `001`.

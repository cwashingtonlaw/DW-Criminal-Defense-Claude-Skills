# Targeted Question Mode

Read this file at MODE SELECTION when the attorney asks a bounded question about phone data — it holds the five-step targeted-answer procedure, the do-not-run rule, and the escalation triggers to Full Analysis.

If the attorney asks a specific, bounded question about phone data — e.g., "Did my client text the victim between 8 and 10 PM?", "Pull all calls to 225-555-1234", "Any location pings near the crime scene on March 15?", "What apps were active during the crime window?", "Were there any videos recorded that night?", "Check the Cash App transactions" — run a scoped query:

1. Skip Step 0 hard stop (unless no data has been uploaded yet)
2. Parse only the relevant data file(s) and filter to the question's scope
3. Answer the question directly with source citations
4. Surface any obvious adverse data encountered while answering
5. End with: *"Want me to expand into a full analysis, or do you have another question?"*

**Do NOT run** preprocessing, baseline, full 8-lens analysis, cross-referencing, or report generation for a targeted question. The attorney wants an answer, not a 30-page report.

**Escalation triggers** — switch to Full Analysis mode if:
- The attorney asks to "analyze everything" or "do a full workup"
- The targeted question reveals something significant enough to warrant comprehensive analysis
- The attorney asks 3+ targeted questions in succession (suggest: "Want me to just run the full analysis?")

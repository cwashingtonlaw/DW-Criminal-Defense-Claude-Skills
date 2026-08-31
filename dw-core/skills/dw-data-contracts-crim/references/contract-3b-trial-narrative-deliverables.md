# Contract 3B: Trial Narrative Deliverables — Full Schema

Read from the SKILL.md **Contract 3B: Trial Narrative Deliverables** section — the complete, authoritative schema (producers, consumers, filename pattern, required sections/fields, output location).

**Producer:** `dw-trial-narrative-builder-crim`
**Consumers:** `dw-trial-notebook-builder-crim`, `dw-voir-dire-assistant-crim`, `dw-cross-exam-architect-crim`, `dw-direct-exam-architect-crim`, `dw-jury-focus-group-crim`, `dw-case-brain-crim`

The trial-narrative-builder produces four interlocking deliverables that share a common case theme.

### Four Deliverables

| # | Deliverable | Format | Filename Pattern |
|---|------------|--------|-----------------|
| 1 | Opening Statement Outline | .docx | `Opening Statement — [Client Last Name] [Date].docx` |
| 2 | Closing Argument Outline | .docx | `Closing Argument — [Client Last Name] [Date].docx` |
| 3 | Theme Tracker | .docx | `Theme Tracker — [Client Last Name] [Date].docx` |
| 4 | Rebuttal Anticipation Memo | .docx | `Rebuttal Anticipation Memo — [Client Last Name] [Date].docx` |

### Opening Statement Outline — Required Sections

1. **Header Block** — Case caption, docket, charges, trial date, lead attorney, defense theme (one line)
2. **Hook / Primacy Opener** — First 60 seconds, theme-driven
3. **Story of the Case** — Defense narrative in chronological or thematic order, no argument
4. **Introduction of Defendant** — Humanizing facts admissible in opening
5. **Roadmap of the Evidence** — Witnesses the jury will hear, exhibits they will see
6. **Burden of Proof Reminder** — Reasonable doubt framing
7. **Promise to the Jury / Ask** — What the verdict should be and why
8. **Objection Risk Notes** — Argument vs. statement, vouching, future-evidence pledges
9. **Theme References** — Cross-reference to Theme Tracker entries

### Closing Argument Outline — Required Sections

1. **Header Block** — Same as Opening
2. **Theme Restatement** — Tie back to opening theme
3. **Burden and Reasonable Doubt** — Jury instruction quotations
4. **Element-by-Element Walk** — Each charged element, the State's proof, the gap, the defense response (cross-reference Defense Matrix)
5. **Witness Credibility** — Per-witness impeachment summary (cross-reference Cross-Examination outlines)
6. **Exhibit Highlights** — Key exhibits the jury should re-examine in deliberation
7. **Anticipated State Rebuttal Responses** — Cross-reference Rebuttal Anticipation Memo
8. **Verdict Form Walk-Through** — Walk the jury through the verdict form (cross-reference Jury Instructions / Verdict Form)
9. **Closing Ask** — Specific verdict requested, charge-by-charge

### Theme Tracker — Required Structure

A living document that records every place the case theme is reinforced across the trial file.

| Column | Type | Required |
|--------|------|----------|
| Theme Element | Text (short phrase, e.g., "Rushed investigation") | Yes |
| Source | Text (witness, exhibit, motion, voir dire question) | Yes |
| Bate Stamp / Reference | Text | Yes |
| Used In | Text (Opening / Cross of [Witness] / Direct of [Witness] / Closing / Voir Dire) | Yes |
| Notes | Text | No |

### Rebuttal Anticipation Memo — Required Sections

1. **Header Block** — Same as Opening
2. **Predicted State Themes** — What the prosecutor is likely to argue
3. **Predicted State Rebuttal Points** — Anticipated responses to defense closing
4. **Defense Counter-Points** — Pre-drafted responses, with sources and exhibit references
5. **Improper-Argument Triggers** — Golden Rule, vouching, burden-shifting, Bossier-style errors — and preserved-objection language
6. **Appellate Preservation Flags** — Cross-reference to `dw-appellate-error-monitor-crim`

### Output Location

All four deliverables: `01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/`

The Opening Statement and Closing Argument outlines may also be mirrored to `01 - Trial Notebook/02 - Opening & Closing/` for courtroom-ready access; the Cowork Analysis copy is the canonical work-product version.

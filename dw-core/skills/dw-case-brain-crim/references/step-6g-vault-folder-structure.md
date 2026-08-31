# Step 6G — DW-CASE BRAINS Folder Structure (Detailed)

Read from SKILL.md **Step 6G** — the vault folder tree, the MCP save-path example, and the where-to-save-new-notes table.

The Obsidian vault mirrors the attorney's Trial Notebook structure. When a companion skill generates witness profiles, legal theories, opening/closing drafts, or other trial prep materials, save them as individual notes in the appropriate folder. Each note should have YAML frontmatter with a `cases` field linking back to the relevant Case Brain(s).

**When saving notes via MCP**, use `mcp__obsidian__create` with paths relative to vault root:
```
mcp__obsidian__create with path: "DW-CASE BRAINS/Witnesses/Prosecution/[WitnessName].md"
```

```
DW-CASE BRAINS/
├── Cases/                  # Case Brain summary files (one per case)
├── Jury-Selection/         # Juror profiles, voir dire questions, strike tracking
├── Opening-Statements/     # Opening statement drafts and outlines
├── Witnesses/              # All witness profiles
│   ├── Prosecution/        # State/prosecution witnesses
│   ├── Defense/            # Defense witnesses
│   └── Expert/             # Expert witnesses (state or defense)
├── Closing-Arguments/      # Closing argument outlines, seeds, exhibit lists
├── Evidence/               # Evidence inventory, authentication, exhibit lists
├── Pleadings/              # Filed motions, oppositions, replies
├── Pretrial-Orders/        # Court orders, legal memos, jury instructions
├── Verdict-Sentencing/     # Verdict forms, sentencing memos, post-trial motions
├── Case-Analysis/          # Phase 2 analysis reports
├── Legal-Theories/         # Legal theory research notes
├── Templates/              # Note templates for each folder type
└── Dashboards/             # Obsidian Bases dashboards (.base files)
```

**Where to save new notes:**

| Content | Folder | Example |
|---|---|---|
| Prosecution witness profile | `Witnesses/Prosecution/` | `LeBlanc, P-O Preston.md` |
| Defense witness profile | `Witnesses/Defense/` | `Character Witness.md` |
| Expert witness evaluation | `Witnesses/Expert/` | `Downs, Amber.md` |
| Opening statement draft | `Opening-Statements/` | `Nicholas-Opening-v1.md` |
| Closing argument outline | `Closing-Arguments/` | `Nicholas-Closing-Seeds.md` |
| Jury selection materials | `Jury-Selection/` | `Nicholas-Voir-Dire-Questions.md` |
| Case analysis report | `Case-Analysis/` | `Nicholas-Report-3-Constitutional.md` |
| Legal theory research | `Legal-Theories/` | `Art. 893 First Offender.md` |
| Evidence note | `Evidence/` | `Nicholas-Exhibit-List.md` |
| Filed motion | `Pleadings/` | `Nicholas-Motion-to-Suppress.md` |
| Court order | `Pretrial-Orders/` | `Nicholas-Discovery-Order.md` |
| Sentencing material | `Verdict-Sentencing/` | `Nicholas-Sentencing-Memo.md` |

The Case Brain's **Trial Preparation** section displays a summary view of all these folders' contents for the case, with links back to the individual notes.

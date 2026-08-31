# Steps 7–9 — .docx Generation, Attorney Review Flags, Save and Integrate

Read by `dw-suppression-motion-crim` at Step 7 (Generate the .docx Files), Step 8 (Attorney Review Flags), and Step 9 (Save and Integrate); it holds the formatting requirements, file-naming conventions, review-flag list, save locations, Clio task, and the attorney presentation summary.

## Step 7: Generate the .docx Files

Read the `docx` skill (SKILL.md) for document creation instructions. Use `docx-js` to generate both files as .docx.

**Formatting requirements:**
- US Letter (8.5" x 11"), 1-inch margins
- Font: Times New Roman, 12pt body text, 14pt headings
- Double-spaced body text (this is a court filing, not an internal memo)
- Left-aligned text (no full justification — courts prefer left-aligned)
- Page numbers centered in footer
- Caption on first page of each document
- Each document starts on page 1

**File naming:**
- Motion: `Motion to Suppress - [Client Last Name] - [Date].docx`
- Memorandum: `Memorandum in Support - Suppress - [Client Last Name] - [Date].docx`


## Step 8: Attorney Review Flags

Before presenting the output, mark all items that need attorney attention:

- `[VERIFY — confirm this fact with client/discovery]` — any factual assertion not directly sourced from discovery
- `[RESEARCH — confirm current validity of this citation]` — any case law that may have been modified or overruled
- `[ATTORNEY TO COMPLETE]` — signature block details, specific dates, bar number
- `[STRATEGIC DECISION]` — choices about which arguments to include/exclude, whether to request an evidentiary hearing vs. submission on brief


## Step 9: Save and Integrate

**If part of an active case folder:**
- Save both documents to `02 - Pretrial Notebook/01 - Pleadings/`
- Update the LWOP Worksheet's "Motion to Suppress" field (if applicable)
- Create a Clio task: *"Review and File Motion to Suppress — [Client Name]"*
- Cross-reference with the Constitutional Issues Scan if one exists

**If standalone:**
- Save to the current working folder / outputs directory

**Present to the attorney with a summary:**
- Suppression category (which constitutional grounds)
- Key arguments and the facts supporting them
- Legal authorities cited
- Items flagged for verification
- Filing deadline (if known)
- Whether a prior firm template was used as the base


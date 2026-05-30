# D&W Standard Folder Structure & Naming Conventions

## Case Folder Structure

```
[Case Root]/
├── Case Tables.xlsx                    ← Master data file — never replace
├── 01 - Trial Notebook/
│   ├── 01 - Jury Instructions & Selection/
│   ├── 01 - Exhibit List/              ← Exhibit management outputs
│   ├── 03 - Witnesses/                 ← Impeachment Worksheets, Cross Outlines
│   ├── 05 - Evidence/                  ← Bate-stamped, OCR'd docs + A/V
│   └── 09 - Case Analysis/             ← Reports 2-7, 9, Cowork Analysis
├── 02 - Pretrial Notebook/
│   ├── 01 - Pleadings/
│   ├── 02 - Discovery/
│   ├── 03 - Case Analysis & Notes/
│   │   ├── 000 - Case Profile.docx
│   │   └── Cowork Analysis/            ← Parallel analysis outputs
│   └── 06 - Law & Research/
├── 03 - Trial Notebook/                ← Trial exhibit management
│   └── 01 - Exhibit List/
└── 05 - Billing/                       ← Time entries and final billing
```

## Document Naming Convention

- All documents: `[3-digit prefix] - [Document Name].docx`
- Audio/video folders: `[3-digit prefix] - [Name]/`
- Transcripts: named identically to their corresponding A/V file
- Missing Discovery Demand Letters: `Missing Discovery Demand — [Date].docx`
- Impeachment Worksheets: one per key witness, filed in `Trial Notebook → 03 - Witnesses`
- Exhibit Lists: `[ClientLastName] - Master Exhibit List - [Date].xlsx`
- Billing: `[ClientLastName] - Time Entries - [Date].xlsx`
- Case Closing: `[ClientLastName] - Case Closing Checklist - [Date].docx`

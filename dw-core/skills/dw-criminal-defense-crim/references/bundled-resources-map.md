# Bundled Resources Map

Read from the SKILL.md **Bundled Resources** section (before Phase 1) — directory tree of everything this skill bundles and the when-to-load-each-resource schedule.

This skill includes bundled files organized into three directories. Load them as needed — they are not all required at once.

```
dw-criminal-defense-crim/
├── SKILL.md                              ← You are here
├── CHANGELOG.md                          ← Version history
├── references/
│   ├── case-profile-procedure.md         ← Phase 1 Step 3 detailed procedure (operating modes, Part 1/2A/2B/2C field detail, LWOP population, Refresh Mode, XML edit)
│   ├── case-tables-write-protocol.md     ← Mandatory write protocol for Case Tables.xlsx (sync-conflict prevention)
│   ├── case-analysis-prompts.md          ← Phase 2 Step 2: all 8 report prompt templates
│   ├── defense-shield-procedure.md       ← Phase 3 Step 3 detailed procedure (Defense Shield + Defense Matrix + Running List)
│   ├── output-path-convention.md         ← CASE_ROOT resolution, phase folders, file naming
│   ├── lwop-field-maps.md                ← Field schema for Part 2A (Homicide) and Part 2B (Sex Offense) of Case Profile
│   ├── lwop-extraction-patterns.md       ← How to extract each LWOP field from discovery
│   ├── art814-responsive-verdict-map.md  ← All 71 La. C.Cr.P. art. 814(A) offenses + verbatim responsive-verdict sets (source for Case Profile § 4)
│   ├── color-coding.md                   ← Spreadsheet color specs for all Case Tables sheets
│   ├── witness-priority-rubric.md        ← First-match 1–5 ranking rule for the Witness List Priority column
│   ├── folder-structure-and-naming.md    ← Standard case folder structure + document naming conventions
│   └── quick-reference.md                ← Cowork action types, sheet index, phase quick map, specialist skill routing
├── assets/
│   ├── CASE PROFILE.docx                 ← Master Case Profile template (Part 1 + case-type Parts 2A/2B/2C)
│   ├── Case Tables.xlsx                  ← Master spreadsheet template (copy to new case roots)
│   └── Evidence_Placeholder_Template.md  ← Layout spec for digital evidence placeholder PDFs
└── scripts/
    └── generate_placeholders.py          ← Generates one-page placeholder PDFs for media evidence folders
```

**When to load each resource:**
- **Phase 1 Step 1 (new case):** Read `references/output-path-convention.md` to resolve `CASE_ROOT`. Copy `assets/Case Tables.xlsx` to the case root if not already present.
- **Phase 1 Step 2f:** Run `scripts/generate_placeholders.py` against the evidence directory.
- **Phase 1 Step 3 (Case Profile):** Read `references/case-profile-procedure.md`. For the § 4 Responsive Verdicts cell, read `references/art814-responsive-verdict-map.md` (emit verbatim from the map — never hand-type verdict sets). For LWOP cases (Part 2A or 2B), also read `references/lwop-field-maps.md` and `references/lwop-extraction-patterns.md`.
- **Phase 1 Step 4 / Phase 3 Step 1 (Case Tables population):** Read `references/case-tables-write-protocol.md` before any write. Read `references/color-coding.md` for formatting specs. For the `Witness List` Priority column, read `references/witness-priority-rubric.md` and rank every witness 1–5.
- **Phase 2 Step 2 (8 reports):** Read `references/case-analysis-prompts.md` for the exact prompt templates.
- **Phase 3 Step 3 (Defense Shield):** Read `references/defense-shield-procedure.md`.
- **Any file-write step:** Consult `references/output-path-convention.md` for the canonical save path and `references/folder-structure-and-naming.md` for folder/naming standards.
- **For sheet index, action-type symbols, or specialist skill routing:** see `references/quick-reference.md`.

---

## Pointers (moved verbatim from SKILL.md)

- **Action-type symbols, sheet index, phase quick map, specialist skill routing table:** `references/quick-reference.md`
- **Case folder structure & document naming:** `references/folder-structure-and-naming.md`
- **Spreadsheet color specs:** `references/color-coding.md`
- **Version history:** `CHANGELOG.md` at skill root

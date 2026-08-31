# Integration Map — Pretrial Motion Library

Read by `dw-pretrial-motion-library-crim` at the Integration section (before STEP 0); it holds the skill-by-skill table of what this skill loads from, feeds, and hands off to.

| Skill | Purpose |
|-------|---------|
| `dw-shared-protocols-crim` | Caption, signature block, certificate of service, notice of hearing, proposed order, work-product marking (internal drafts only — filed pleadings get NO marking), Louisiana citation style, 14th JDC filing conventions, output path formula |
| `dw-criminal-defense-crim` | Phase 2 Red Flags trigger motion practice |
| `dw-brady-giglio-auditor-crim` | CI findings → Module 11 (Reveal the Deal); missing-discovery findings → Module 4 (Compel) |
| `dw-case-brain-crim` | Motion status tracking and CASE_ROOT resolution |
| `dw-suppression-motion-crim` | Hand off suppression issues |
| `dw-404b-opposition-crim` | Hand off 404(b) issues |
| `dw-bond-and-release-motion-crim` | Hand off bond issues |
| `docx` | Document generation |
| `assets/templates/` (bundled) | Firm template exemplars for 7 pretrial filings — see `assets/templates/README.md` for the full inventory. Bond, new trial, and appeal templates have been moved to `dw-bond-and-release-motion-crim` and `dw-appellate-error-monitor-crim` respectively |
| `references/caselaw-citations.md` (bundled) | Consolidated caselaw inventory extracted from the bundled templates, organized by module with verification flags for known typos and stale cites |

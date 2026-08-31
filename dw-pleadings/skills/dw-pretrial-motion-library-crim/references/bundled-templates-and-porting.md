# Bundled Templates & Porting Procedure

Read by `dw-pretrial-motion-library-crim` at STEP 1 (Template Source Selection — the bundled-template table presented to the attorney) and STEP 1.5 (porting procedure, caselaw reference, and template-selection priority).

## Bundled template inventory (STEP 1)

| # | Template | Motion type | Module | Venue |
|---|----------|-------------|--------|-------|
| 1 | `motion_for_speedy_trial_701.docx` | Speedy Trial / Art. 701 | Module 1 | 14th JDC Calcasieu (D&W primary venue) |
| 2 | `motion_for_discovery_initial.docx` | Initial Discovery demand | Module 4 | 19th JDC East Baton Rouge |
| 3 | `motion_for_preliminary_exam.docx` | Preliminary Examination / Art. 292 | Module 12 | 2nd JDC Allen |
| 4 | `motion_omnibus_orleans.docx` | Omnibus Pretrial Motion | Module 13 | Orleans Parish CDC |
| 5 | `notice_of_self_defense.docx` | Notice of Self-Defense / Justification (Art. 390) | Module 14 | 2nd JDC Allen |
| 6 | `melendez_diaz_objection.docx` | Melendez-Diaz / Criminalist Certificate objection | Module 15 | 2nd JDC Allen |
| 7 | `motion_to_enroll.docx` | Enrollment of Counsel (admin boilerplate) | — | 2nd JDC Allen |

## Porting procedure, caselaw reference, and selection priority (STEP 1.5)

In parallel with the DEVONthink search, consult the skill's bundled assets and references:

**Bundled templates** (`assets/templates/`) — 7 firm template exemplars covering speedy trial (Art. 701), preliminary exam, initial discovery, omnibus pretrial, self-defense notice, Melendez-Diaz objection, and motion to enroll (admin boilerplate). Read `assets/templates/README.md` first for the full inventory, module mapping, and caption-variant guide. The templates are real prior firm filings — they show D&W's preferred paragraph numbering, signature block format, certificate of service style, and proposed-order conventions. When using one:

1. Strip ALL case-specific content (client name, docket number, parish, judge, facts, dates).
2. Replace the caption using `dw-shared-protocols-crim/references/filed-pleading-boilerplate.md` for the actual filing parish. Of the 7 bundled templates, only `motion_for_speedy_trial_701.docx` uses the 14th JDC Calcasieu caption (D&W's primary venue) — the other 6 use 2nd JDC, 19th JDC, or Orleans Parish, so reset the caption rather than copy it forward.
3. Verify every citation against the bundled caselaw reference (next section).

**Note on bond / new trial / appeal:** Templates for those motion types previously bundled here have been relocated to `dw-bond-and-release-motion-crim` and `dw-appellate-error-monitor-crim`. Drafting must be invoked through those skills directly — this skill does not draft bond, new trial, or appeal motions.

**Caselaw reference** (`references/caselaw-citations.md`) — a consolidated, topic-organized inventory of every citation appearing in the bundled templates, with verification flags for known typos, year errors, and reporter inconsistencies. Use it as a checklist when porting citations from a template into a new draft. Each module below points to the relevant section of this file.

**Template selection priority:** DEVONthink results take priority over bundled templates when both exist for the same motion type — DEVONthink reflects the firm's most recent and case-appropriate filings, while bundled templates are static exemplars frozen at the time of skill packaging. Use bundled templates when DEVONthink returns nothing useful, or to cross-check formatting consistency.

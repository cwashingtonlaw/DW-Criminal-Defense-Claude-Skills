# Pretrial Motion Library — Template Inventory

This folder holds firm templates extracted from prior D&W filings. They are reference exemplars — show the firm's preferred caption style, paragraph numbering, signature block, certificate of service, and proposed order conventions. Use them as drafting starts alongside (not instead of) the DEVONthink Template-First search in Step 1 of the SKILL.md.

**Important:** Templates here are case-specific filings with prior client names, docket numbers, parishes, and facts. When using a template, the drafting workflow must:

1. Replace ALL case-specific content (client name, docket number, parish, judge, facts, dates).
2. Verify every citation against current Louisiana and federal authority. Templates may contain stale or erroneous citations — see `references/caselaw-citations.md` for the verified citation list and known verification flags.
3. Apply caption from `dw-shared-protocols-crim` for the actual filing parish.

---

## In-scope pretrial templates

| File | Maps to Module | Notes |
|------|---------------|-------|
| `motion_for_speedy_trial_701.docx` | Module 1 (Speedy Trial / 701) | Art. 701(D)(1); 14th JDC Calcasieu Parish, Second Degree Murder (Harrison). Includes the required counsel affidavit certifying readiness. **Only bundled template using D&W's primary 14th JDC caption** — also useful as a 14th JDC caption/signature reference for other filings |
| `motion_for_preliminary_exam.docx` | Module 12 | Art. 292; 2nd JDC Allen Parish caption |
| `motion_for_discovery_initial.docx` | Module 4 (Initial Discovery variant) | 19th JDC EBR; comprehensive Art. 716-723 demand including Brady, Giglio, expert disclosures, witness records, Henderson victim records. Large file (4MB) due to embedded fonts from source export |
| `motion_omnibus_orleans.docx` | Module 13 | Orleans Parish CDC; multi-issue (discovery + preservation + suppression in one pleading). Use when local practice favors omnibus over piecemeal motions |
| `notice_of_self_defense.docx` | Module 14 | Art. 390 notice of justification under R.S. 14:19 / 14:20; 2nd JDC Allen |
| `melendez_diaz_objection.docx` | Module 15 | Confrontation Clause objection to criminalist certificates under La. R.S. 15:499 et seq.; 2nd JDC Allen |

## Firm admin / boilerplate

| File | Use |
|------|-----|
| `motion_to_enroll.docx` | Enrollment of counsel template; not a substantive motion. Use when D&W is being substituted in or initially appearing |

## Templates that have moved to other skills

These templates were originally bundled here but have been relocated to their proper homes in the D&W skill ecosystem. If you reach for them from this skill, follow the pointer:

| Former file (now removed) | Now lives in |
|---------------------------|--------------|
| `motion_for_bond_reduction.docx` | `dw-bond-and-release-motion-crim/assets/templates/motion_for_bond_reduction.docx` |
| `memorandum_in_support_bond_garrison.docx` | `dw-bond-and-release-motion-crim/assets/templates/memorandum_in_support_bond_garrison.docx` |
| `motion_for_new_trial.docx` | `dw-appellate-error-monitor-crim/assets/templates/motion_for_new_trial.docx` (wired into MODULE E → Motion for New Trial — La. C.Cr.P. Art. 851) |
| `motion_for_appeal.docx` | `dw-appellate-error-monitor-crim/assets/templates/motion_for_appeal.docx` (wired into MODULE E → Motion for Appeal — La. C.Cr.P. Art. 914) |

Bond / new-trial / appeal motion drafting must be invoked through those skills directly — do not draft any of them from `dw-pretrial-motion-library-crim`.

---

## Caption variants represented

The remaining 7 templates collectively cover five Louisiana venues. When pulling caption boilerplate, prefer `dw-shared-protocols-crim/references/filed-pleading-boilerplate.md` for the actual filing parish rather than copying from a template:

- 2nd JDC (Allen Parish) — 4 templates (preliminary exam, self-defense notice, Melendez-Diaz objection, motion to enroll)
- **14th JDC (Calcasieu — D&W primary venue) — 1 template** (`motion_for_speedy_trial_701.docx`)
- 19th JDC (East Baton Rouge) — 1 template (`motion_for_discovery_initial.docx`)
- Orleans Parish Criminal District Court — 1 template (`motion_omnibus_orleans.docx`)

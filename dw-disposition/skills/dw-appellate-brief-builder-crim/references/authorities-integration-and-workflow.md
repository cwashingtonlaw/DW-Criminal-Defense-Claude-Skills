# Direct-Appeal Authorities, DW-Skill Integration & Workflow Summary

Read from SKILL.md Quick References whenever a verified direct-appeal authority, an upstream/downstream skill routing decision, or the end-to-end workflow map is needed.

### Direct-appeal authorities (verified)

| Authority | Use |
|---|---|
| La. C.Cr.P. Art. 841 | Contemporaneous-objection rule (preservation predicate) |
| La. C.Cr.P. Art. 920 | Errors patent |
| La. C.Cr.P. Art. 921 | Non-constitutional harmless error |
| La. C.Cr.P. Art. 912-914 | Appeal perfection and record designation |
| La. Const. Art. I, § 19 | Right to judicial review |
| La. Const. Art. I, § 20 | Excessive-punishment clause |
| La. Const. Art. V, § 10 | Appellate jurisdiction |
| La. Uniform Rules — Courts of Appeal, Rule 2-12.2 | Brief formatting (font, margins, page/word limits) |
| La. Uniform Rules — Courts of Appeal, Rule 2-12.3 | Cover-page format |
| La. Uniform Rules — Courts of Appeal, Rule 2-12.4 | Brief structure (sections, content) |
| La. Sup. Ct. Rule X | Writ application to the Louisiana Supreme Court |
| *Jackson v. Virginia*, 443 U.S. 307 (1979) | Sufficiency standard |
| *Chapman v. California*, 386 U.S. 18 (1967) | Constitutional harmless error (BRD) |
| *Sullivan v. Louisiana*, 508 U.S. 275 (1993) | Structural error — defective reasonable-doubt instruction |
| *Ramos v. Louisiana*, 590 U.S. 83 (2020) | Unanimous jury verdict required |
| *McCoy v. Louisiana*, 584 U.S. 414 (2018) | Counsel cannot concede guilt over defendant's objection |
| *Crawford v. Washington*, 541 U.S. 36 (2004) | Confrontation Clause — testimonial hearsay |
| *State v. Captville*, 448 So.2d 676 (La. 1984) | Louisiana sufficiency standard |
| *State v. Bonanno*, 384 So.2d 355 (La. 1980) | Excessive sentence — grossly disproportionate |
| *State v. Dorthey*, 623 So.2d 1276 (La. 1993) | Downward departure from mandatory minimum |
| *State v. Mims*, 619 So.2d 1059 (La. 1993) | Art. 881.1 prerequisite for excessive-sentence appeal |
| *State v. Augustine*, 555 So.2d 1331 (La. 1990) | Art. 873 sentencing-delay errors-patent |
| *Boykin v. Alabama*, 395 U.S. 238 (1969) | Guilty-plea waiver requirements |
| *Burks v. United States*, 437 U.S. 1 (1978) | Double Jeopardy bars retrial after sufficiency reversal |

### Reference files in this skill

- `references/errors-patent-template.md` — Art. 920 errors-patent categories and template language
- `references/standards-of-review-by-issue.md` — full chart matching issue type to standard of review
- `references/circuit-formatting-rules.md` — per-circuit (1st, 2nd, 3rd, 4th, 5th, La. Sup. Ct.) formatting rules
- `references/harmless-error-framework.md` — Chapman / Art. 921 / Sullivan structural-error framework with templates
- `references/brief-section-templates.md` — boilerplate skeletons for cover page, TOC, TOA, every brief section in proper order

### Integration with Other DW Skills

| Skill | How It Integrates |
|---|---|
| `dw-appellate-error-monitor-crim` | UPSTREAM — produces the ranked-issue list, designated record, post-trial motion package, errors-patent findings, and harmless-error pre-assessment that this skill consumes |
| `dw-post-conviction-relief-crim` | DOWNSTREAM PEER — IAC claims, PCR grounds, and federal habeas all route there; this skill stays in direct-appeal lane |
| `dw-shared-protocols-crim` | Citation style, signature block, certificate of service, output path |
| `dw-shared-protocols-crim` (template selection) | DEVONthink template-first search for prior firm appellate briefs (former `dw-template-selector`, now consolidated into shared protocols) |
| `dw-suppression-motion-crim` | Trial-court suppression briefing — feeds the suppression-denial assignment of error here |
| `dw-404b-opposition-crim` | Trial-court 404(b) briefing — feeds 404(b) assignments of error here |
| `dw-jury-instructions-builder-crim` | Jury-instruction objections at trial — feeds jury-instruction assignments of error here |
| `dw-sentencing-mitigation-specialist-crim` | Excessive-sentence factual record (mitigation, comparable sentences) — feeds excessive-sentence assignments here |
| `dw-habitual-offender-auditor-crim` | Habitual-offender adjudication errors — feeds habitual-offender assignments here |
| `dw-brady-giglio-auditor-crim` | Brady violations preserved at trial — feed Brady assignments here |
| `docx` | .docx generation per Rule 2-12.2 formatting |
| DEVONthink | Search `Law Library-Criminal` for prior firm appellate briefs as templates |
| TextExpander | `;sig`, `;cos`, `;draft` |

---

## WORKFLOW SUMMARY

```
STEP 0:   File Intake Hard Stop — wait for "no more uploads"
STEP 0.5: Load shared protocols (citation style, output path, sig, COS)
STEP 1:   Verify INPUT CONTRACT from dw-appellate-error-monitor-crim
            +-- Module H (ranked issues)
            +-- Module I (designated record)
            +-- Module E (post-trial motion package)
            +-- Module D (errors patent)
            +-- Module F (harmless-error pre-assessment)
          If any missing -> route to dw-appellate-error-monitor-crim first
STEP 2:   Determine mode (Appellant Brief / Reply / La. Sup. Ct. Writ)
STEP 3:   Standard-of-review mapping for each assignment
STEP 4:   Errors patent review (Art. 920)

MODULE A: Statement of the Case (procedural history)
MODULE B: Statement of Facts (every sentence record-cited)
MODULE C: Assignments of Error (numbered, terse)
MODULE D: Argument (per-assignment six-part substructure)
            D.1 Issue Restated
            D.2 Standard of Review
            D.3 Preservation
            D.4 Statement of the Law
            D.5 Application to Facts
            D.6 Prejudice / Harmless Error
MODULE E: Standard-of-review framework lookup audit
MODULE F: Conclusion (specific relief requested)
MODULE G: Certificate of service + page/word-count compliance
MODULE H: Reply brief companion (when in Reply mode)

ASSEMBLY: Cover -> TOC -> TOA -> Jurisdictional Stmt -> Assignments ->
          Stmt of Case -> Stmt of Facts -> Summary of Argument ->
          Argument -> Conclusion -> Cert. of Compliance ->
          Cert. of Service -> Signature Block -> Appendix (rare)

OUTPUT: {{CASE_ROOT}}/05 - Appellate/01 - Direct Appeal/Brief Drafts/
```

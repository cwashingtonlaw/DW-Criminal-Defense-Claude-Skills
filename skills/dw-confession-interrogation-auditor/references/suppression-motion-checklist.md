# Suppression Motion Checklist (La. C.Cr.P. Art. 703)

This file is the operational checklist for assembling a motion to suppress a confession or custodial statement under Louisiana law. Use it after Modules A-G of the audit have produced findings.

**Scope:** Confessions and statements only. For physical evidence suppression (Fourth Amendment search/seizure), route to `dw-suppression-motion`.

**Burden:** The State bears the burden of proving voluntariness **beyond a reasonable doubt** at the suppression hearing. La. R.S. 15:452. This is higher than the federal preponderance standard.

---

## 1. Required Components — Motion to Suppress

| # | Component | Source / Module |
|---|-----------|-----------------|
| 1 | Caption (court, parties, docket number, motion title) | Standard pleading; verify against `dw-shared-protocols` template-selection-protocol results |
| 2 | Statement of relief sought | "Defendant moves this Court to suppress the statement made by Defendant on [date] at [location]" |
| 3 | Procedural posture | Pretrial; per Art. 703(D), absent good cause shown, must be filed prior to trial |
| 4 | Factual background | Module A facts: when, where, who, advisement, waiver, statement made |
| 5 | Applicable legal standards | La. C.Cr.P. Art. 703; La. R.S. 15:451-452; *Miranda*; *Edwards*; *Seibert*; *Blank* |
| 6 | Argument I — Custody analysis (if disputed) | Module A custody facts |
| 7 | Argument II — Miranda compliance | Module A findings (warnings, timing, waiver validity) |
| 8 | Argument III — Voluntariness under totality | Module B findings |
| 9 | Argument IV — Coercive techniques applied | Module C findings (Reid, false-evidence ploys, minimization, threats, promises) |
| 10 | Argument V — False confession risk factors | Module D findings (vulnerable suspect, length, isolation) |
| 11 | Argument VI — Invocation violations (if any) | Module E findings (silence, counsel, scrupulously-honored test) |
| 12 | Argument VII — Juvenile-specific issues (if applicable) | Module F findings; La. Ch.C. Art. 808; *J.D.B.* |
| 13 | Conclusion + relief | Suppress the statement and any fruits derived therefrom |
| 14 | Certificate of service | Per local rules |
| 15 | Notice of hearing | Per local rules; request evidentiary hearing if facts contested |

---

## 2. Supporting Modules

Each argument section pulls from the audit modules. Do not include modules whose findings are merely MINOR — focus on CRITICAL and SIGNIFICANT.

| Argument | Primary Module | Secondary Modules |
|----------|---------------|-------------------|
| Custody | A | F (juvenile context) |
| Miranda compliance | A | E (invocation) |
| Voluntariness | B | C, D |
| Coercive techniques | C | B, D |
| False confession risk | D | B |
| Invocation violations | E | A |
| Juvenile-specific | F | A, B |

---

## 3. Required Exhibits

Attach as exhibits to the motion (or move for in-camera review where confidentiality requires):

| Exhibit | Source | Purpose |
|---------|--------|---------|
| Recording of interrogation (full) | Discovery production | Primary evidence of what occurred |
| Transcript of interrogation | `dw-transcript-router` output | Citable substitute for recording |
| Written waiver form (if any) | Discovery production | Waiver documentation for State's burden |
| Booking sheet / arrest report | Discovery production | Custody timing |
| BWC of arrest and transport | Discovery production | Custody onset; pre-warning conditions |
| Officer reports | Discovery production | Officer's account of advisement and statement |
| Defendant's medical / mental health records | Subpoena or release | Knowing/intelligent prong (only if relevant) |
| Suspect's prior justice-system history | Pre-sentence report or court records | Vulnerability analysis (use carefully — can cut both ways) |

---

## 4. Witnesses for the Suppression Hearing

| Witness | Examination Type | Topics |
|---------|-----------------|--------|
| Interrogating officer(s) | Cross | Module A advisement, Module B conditions, Module C techniques, Module E invocation handling |
| Booking / arresting officer | Cross | Custody onset; pre-warning interactions |
| Defendant (limited; tactical) | Direct | Subjective experience — but defendant's testimony is admissible only at the hearing under La. R.S. 15:451 limitations; **discuss carefully with attorney before calling** |
| Defense expert (if retained) | Direct | False confession risk factors; coercive technique analysis; *Frye/Daubert* qualifications |
| Mental health expert (if applicable) | Direct | Vulnerability assessment for knowing/intelligent prong |

---

## 5. Pre-Hearing Tasks

- [ ] Subpoena the interrogating officer(s)
- [ ] Subpoena the recording custodian if authentication is contested
- [ ] Pre-mark all exhibits and exchange with State
- [ ] File witness list per local rules
- [ ] File a memorandum in support if local rules permit and the issue is complex
- [ ] Request order for full unedited recording (some PDs produce only excerpts)
- [ ] Calendar Art. 703 hearing date; confirm trial date is not before the hearing
- [ ] Pull the audit's Quick Reference Tables (Module A red flags, Module B factor matrix) for use as visual aids at hearing
- [ ] Cross-check that the audit captured every instance of *post-invocation* questioning (often the strongest argument)

---

## 6. Common State Arguments and Defense Responses

| State Argument | Defense Response |
|----------------|------------------|
| "Defendant signed the waiver form." | Form does not establish knowing/intelligent waiver under totality; cite *Connelly* and *Burbine* limits. |
| "Defendant was given Miranda warnings." | Warnings must be substantively complete under *Powell* and effective under *Seibert*; review the full advisement. |
| "Defendant's confession is corroborated." | Corroboration is not the test; voluntariness is. Confession is suppressed first; corroboration analysis follows only if admissible. |
| "Defendant did not unambiguously invoke." | If true, that argument prevails — but verify on the record before conceding; many ostensibly equivocal statements were unambiguous in context. |
| "The interrogation was reasonable in length." | Cite Drizin & Leo (2004) — mean false confession length was 16.3 hours; even shorter durations can be coercive when combined with techniques and vulnerability. |
| "Defendant has prior justice-system experience." | Experience does not insulate against coercion; vulnerable suspects with prior contacts are still vulnerable. |

---

## 7. Output Path

The motion to suppress drafted from this checklist saves to:

```
{{CASE_ROOT}}/02 - Pretrial Notebook/01 - Pleadings/[NUM] - Motion to Suppress Confession.docx
```

The supporting memorandum (if filed separately) saves alongside with `[NUM+1] - Memorandum in Support of Motion to Suppress Confession.docx`.

All deliverables receive attorney work-product marking per `dw-shared-protocols/references/attorney-work-product-marking.md`.

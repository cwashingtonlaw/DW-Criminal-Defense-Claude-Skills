# Integration with Other DW Skills and Post-Motion Handoff

Read when coordinating with other DW skills or tools, and after the motion / memorandum is complete to run the bond-hearing cross-examination handoff.

## Integration with Other DW Skills

| Skill | How It Integrates |
|-------|------------------|
| `dw-shared-protocols-crim` | Caption, signature, COS, notice of hearing, proposed order, citation style, filing conventions, output path |
| `dw-criminal-defense-crim` | Phase 0 Criminal Defense Cover includes bail status section; bail motion filings saved to Pretrial Notebook |
| `dw-discovery-compliance-monitor-crim` | Discovery delays may trigger Art. 701 release rights; coordinate timeline tracking |
| `dw-cross-exam-architect-crim` | When bond hearing is set, invoke to prepare cross-examination of State's witnesses |
| `dw-case-brain-crim` | Bond status tracking; update after hearing or when conditions are modified |
| `docx` | Document generation — read for .docx creation instructions |
| DEVONthink | Template-First search in Law Library-Criminal for prior bail filings |
| TextExpander | `;draft` |

## Post-Motion Handoff

After completing the motion and/or memorandum, ask the attorney:

> "Would you like me to build cross-examination chapters for the bond hearing? If the court schedules a contradictory or bail hearing, I can invoke dw-cross-exam-architect-crim to prepare a detailed cross-examination outline for the State's witnesses."

If the attorney says yes or indicates a bond hearing is scheduled, invoke the `dw-cross-exam-architect-crim` skill and pass the following context:
- Case caption and docket number
- Nature of the hearing (bail hearing / contradictory hearing for capital case)
- Anticipated State witnesses (if known)
- Key weaknesses in the State's case (from the bond motion research)
- Burden the State must carry (Art. 316 factors or Art. 313 "proof evident" standard)

## Version Notes (moved from SKILL.md)

*This skill incorporates the former dw-pretrial-release-motion skill. All pretrial release and bond motion workflows are now consolidated here.*

*This skill is part of the Daniels & Washington Cowork criminal defense toolkit. Version 2.0 integrates dw-bond-motion and dw-pretrial-release-motion into a comprehensive bond and release motion generator. Integrates with dw-criminal-defense-crim (Phase 0 bond assessment), dw-case-brain-crim (bond status tracking), and dw-cross-exam-architect-crim (bond hearing witness preparation).*

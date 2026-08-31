# Integration with Other DW Skills

Read at SKILL.md **Integration with Other DW Skills** — upstream/downstream skill bindings and tool hooks.

---

| Skill | How It Integrates |
|-------|------------------|
| `dw-criminal-defense-crim` | Phase 0 Initial Case Profile identifies case posture; Phase 2 trial strategy informs which errors are most significant; post-trial Phase 5 triggers error preservation audit |
| `dw-trial-day-assistant-crim` | Module B objection log feeds this skill's MODULE A; schema is field-for-field aligned (additive `Day`/`Time` fields only) |
| `dw-appellate-brief-builder-crim` | Consumes MODULE H ranked-issue output and MODULE E post-trial motion package; routes back if ranking is missing |
| `dw-cross-exam-architect-crim` | Per-witness context from MODULE A objection log informs cross-prep |
| `dw-discovery-compliance-monitor-crim` | Discovery violations identified during trial (late disclosure, Brady material) must be objected to and preserved -- cross-reference discovery compliance issues with Module A objection log |
| `dw-habitual-offender-auditor-crim` | Habitual offender adjudication and sentencing carry their own preservation requirements -- Art. 881.1 motion covers enhanced sentence; challenge to predicate convictions must be preserved at the habitual offender hearing |
| `dw-sentencing-mitigation-specialist-crim` | Sentencing mitigation evidence that was excluded requires proffer (Module C); failure to present available mitigation is potential IAC (Module G); Art. 881.1 motion (Module E) is the vehicle for excessive sentence preservation |
| `dw-404b-opposition-crim` | Other crimes evidence rulings must be preserved by contemporaneous objection with specific grounds (Art. 841); if Prieur motion was denied pretrial, consider supervisory writ before trial |
| `dw-confession-interrogation-auditor-crim` | Suppression motion denial must be preserved -- consider supervisory writ (writ framework section); if confession admitted over objection, error is preserved if objection was Art. 841 compliant |
| `dw-eyewitness-identification-auditor-crim` | Identification suppression denial must be preserved -- consider supervisory writ; if identification admitted over objection, preservation depends on specificity of objection |
| `dw-voir-dire-assistant-crim` | Batson challenges must be made during voir dire and preserved on the record; challenges for cause that are denied must be noted with identification of the objectionable juror who served |
| `dw-jury-instructions-builder-crim` | Jury instruction objections must be made before the jury retires (Art. 841); refused instructions must be submitted in writing and placed in the record |
| `dw-expert-witness-evaluator-crim` | Daubert/expert qualification challenges must be made before or during the expert's testimony; failure to object to expert methodology waives the issue |
| `docx` | Document generation -- read for .docx creation instructions for post-trial motion packages and appellate memos |
| DEVONthink | Search `Law Library-Criminal` for appellate brief templates, error preservation checklists, prior filings, and research |
| TextExpander | `;caption`, `;sig`, `;cos`, `;draft` |

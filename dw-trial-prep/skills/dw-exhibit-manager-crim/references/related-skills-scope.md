# Related Skills — Scope Boundaries

Read at RELATED SKILLS (DO NOT USE FOR) of `dw-exhibit-manager-crim/SKILL.md` — moved verbatim from SKILL.md.

---

This skill handles exhibit management ONLY. Do NOT use for:

- **Trial notebook assembly:** Use **dw-trial-notebook-builder-crim**
  - Assembles complete trial notebook (all sections, exhibits, jury instructions, etc.)
  - dw-exhibit-manager-crim feeds INTO it

- **Evidence chain of custody auditing:** Use **dw-chain-of-custody-auditor-crim**
  - Audits evidence handling from initial collection through trial
  - Identifies custody gaps and break-in-chain issues pre-trial
  - dw-exhibit-manager-crim reads from it

- **Cross-examination planning:** Use **dw-cross-exam-architect-crim**
  - Designs witness examination outlines and cross-examination strategies
  - Identifies impeachment opportunities for authenticating witnesses
  - dw-exhibit-manager-crim reads from it

- **404(b) opposition strategy:** Use **dw-404b-opposition-crim**
  - Develops objections to other crimes evidence
  - dw-exhibit-manager-crim flags 404(b) exhibits to it

- **Appellate error preservation:** Use **dw-appellate-error-monitor-crim**
  - Tracks all trial errors (evidentiary, instructional, procedural)
  - dw-exhibit-manager-crim FEEDS sustained objections INTO it

- **Discovery compliance:** Use **dw-discovery-compliance-monitor-crim**
  - Tracks discovery obligations, production status, sanctions risk
  - dw-exhibit-manager-crim reads authentication/custody issues from it

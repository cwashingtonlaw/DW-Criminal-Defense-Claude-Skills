# Downstream / Upstream Routing — Crime Lab Audit

Read at the Handoff / Downstream Integration step of `dw-crime-lab-auditor-crim/SKILL.md` — the routing list moved verbatim from SKILL.md.

Downstream routing:

- **`dw-cross-exam-architect-crim`** — analyst cross (drug analyst and/or toxicologist); auditor cross if applicable
- **`dw-pretrial-motion-library-crim`** — R.S. 15:501 objection / Melendez-Diaz demand; motion to compel raw data and proficiency tests; Daubert/Foret motion in limine
- **`dw-drug-offense-specialist-crim`** — substantive drug-offense strategy (the lab audit feeds the substance element of the charge)
- **`dw-dwi-specialist-crim`** — lab-portion findings feed back into the DWI workflow (especially blood-alcohol confirmation issues)
- **`dw-suppression-motion-crim`** — chain-of-custody-at-lab grounds if any link supports suppression
- **`dw-issue-code-tracker-crim`** — Issue codes for every CRITICAL finding so they ripen into trial and appellate issues

**Upstream — read from:**
- `dw-discovery-orchestrator-crim` — for the discovery production identifying the lab documents and for triage of incoming productions

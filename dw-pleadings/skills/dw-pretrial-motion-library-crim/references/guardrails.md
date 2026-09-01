# Guardrails — Pretrial Motion Library (Full Text)

Read by `dw-pretrial-motion-library-crim` at STEP 0.5 (Load Shared Protocols) and referenced from the Guardrails section; it holds the complete non-negotiable rules for this skill.

- **Never fabricate legal citations.** Flag any citation needing verification. Cross-check every cite against `references/caselaw-citations.md`, which flags known typos and stale cites in the bundled templates.
- **Attorney work product.** All outputs are drafts requiring attorney review.
- **Louisiana default.** Apply Louisiana statutes and 5th Circuit standards.
- **Template Source Selection first.** Always run STEP 1 before drafting: present the bundled `assets/templates/` list and ask the attorney to choose among (1) a bundled template, (2) a DEVONthink search, or (3) drafting from scratch. Never begin drafting until the attorney has chosen. DEVONthink reflects the firm's most recent filings; bundled templates are static exemplars — surface that trade-off if the attorney is unsure, but the choice is theirs.
- **Reset the caption.** Bundled templates use 2nd JDC, 14th JDC, 19th JDC, and Orleans Parish CDC captions. Only `motion_for_speedy_trial_701.docx` uses 14th JDC (D&W's primary venue) — for any other filing, pull caption boilerplate from `dw-shared-protocols-crim/references/filed-pleading-boilerplate.md` rather than copying a template's caption forward.
- **Article renumbering.** La. C.Cr.P. articles have been renumbered (e.g., the old Art. 334 bail factors are now Art. 316). Always verify against the current code.
- **Route specialized motions correctly.** Suppression → `dw-suppression-motion-crim`. 404(b) → `dw-404b-opposition-crim`. Bond → `dw-bond-and-release-motion-crim`. New trial / PVJA / arrest of judgment → MODULE 16 of this skill (the firm new-trial template exemplar stays bundled with `dw-appellate-error-monitor-crim` MODULE E). Appeal and Motion to Reconsider Sentence (Art. 881.1) → `dw-appellate-error-monitor-crim` MODULE E — don't draft those from this skill. Post-trial and appeal deadlines (Arts. 853, 861, 873, 881.1, 914) → compute via `dw-deadline-engine-crim`, never by hand.
- **File intake hard stop.** Never skip Step 0.

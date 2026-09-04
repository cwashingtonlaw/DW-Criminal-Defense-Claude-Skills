# Changelog

Version history for dw-trial-notebook-builder-crim (read only when auditing skill history; not needed during a build).

---

### v1.1 (May 2026)
- Added integration with `dw-issue-code-tracker-crim` (taxonomy v2.0).
- New Step 2.5: generates `00-Trial-Readiness-Gap-Report.docx` as front matter — an
  issue-code-driven gap analysis that complements the existing deliverable-based Gap
  Report at Step 2.
- New Step 5.5: generates `99-Issue-Code-Ledger-Appendix/[YYYY-MM-DD]_Issue-Ledger-Snapshot.docx`
  — a point-in-time snapshot of the Issue Codes sheet plus the Audit Trail from the
  Case Brain.
- Updated trial notebook folder structure diagram to show `00-` front matter and `99-`
  appendix.
- Updated Master Index to reference both new documents (Front Matter + Appendices).
- Graceful degradation: if the `Issue Codes` sheet doesn't exist, both new outputs emit
  a one-page placeholder noting the ledger was not maintained.
- No auto-routing — `Linked Skill` recommendations are listed but not auto-invoked,
  consistent with `dw-issue-code-tracker-crim`'s design.
### v1.1 (April 2026)
- Added recommended subfolder structure for all 9 tabs (Step 3B)
- Updated deliverable-map.md to match the Step 1A tab structure
- The authoritative tab layout is the 9-tab structure defined in Step 1A
  (Tab 2 `02 - Opening & Closing`, Tab 4 `04 - Exhibit List`, Tab 6
  `06 - Motions in Limine`, Tab 7 `07 - Legal Research`, Tab 8
  `08 - Jury Selection Notes`) — the scheme the orchestrator (Reports → Tab 9
  `09 - Case Analysis`), dw-case-dashboard-crim (`03 - Witnesses`), and
  dw-exhibit-manager-crim (exhibits → Tab 4 `04 - Exhibit List`) all align to.
  [dw-exhibit-manager-crim was retired in v1.9; Tab 4 is now fed by the
  `Case Tables.xlsx` Evidence Table and dw-trial-day-assistant-crim Module D.]
  [VERIFY tab folder names against a live case file before relying on Tabs 2/6/7/8.]

### v1.0 (April 2026)
- Initial skill version
- Folder scan, inventory, gap report, master index with `file://` links
- Attorney checklists: Day of Trial, Exhibit Authentication, Witness Schedule
- Case Brain integration for context loading and update logging
- Full upstream skill routing table for gap remediation

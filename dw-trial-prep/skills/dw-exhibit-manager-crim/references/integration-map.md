# Integration Map

Read at the INTEGRATION section of `dw-exhibit-manager-crim/SKILL.md` — the Reads-from / Writes-to / Feeds-into / Uses lists, moved verbatim from SKILL.md.

---

**Reads from:**
- **dw-case-brain-crim:** Case context, charges, witness list, trial date, judge assignment
- **dw-trial-notebook-builder-crim:** Existing exhibit list (if trial notebook already created)
- **dw-cross-exam-architect-crim:** Witness examination plans and cross-examination vulnerabilities
- **dw-discovery-compliance-monitor-crim:** Evidence inventory and authentication issues
- **dw-chain-of-custody-auditor-crim:** Chain of custody gaps and evidence handling concerns

**Writes to:**
- **dw-appellate-error-monitor-crim:** Every sustained objection automatically, with exhibit #, objection basis, ruling, judge, trial date
- **dw-case-brain-crim:** Update case status with exhibit admission/exclusion summary post-trial
- **Trial Notebook folder:** Master Exhibit List (xlsx), Clerk's Exhibit List (docx), Objection Log (xlsx), Authentication Checklist (docx)

**Feeds into:**
- **dw-trial-notebook-builder-crim:** Final exhibit package (Master Exhibit List, Authentication Checklist, Clerk's Exhibit List)
- **dw-appellate-error-monitor-crim:** Sustained objections and excluded exhibits for error preservation
- **dw-404b-opposition-crim:** If any exhibits implicate Art. 404(b) other crimes evidence, cross-reference for objection strategy

**Uses these skills:**
- **xlsx skill:** Master Exhibit List, Objection Log
- **docx skill:** Clerk's Exhibit List, Authentication Checklist

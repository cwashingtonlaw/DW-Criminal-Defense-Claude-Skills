# Case Brain Registration

Read this file at the "Register Output with Case Brain" step — it holds the registration procedure for deliverables when a dw-case-brain-crim session is active.

After generating any deliverable, check if a case session is active (i.e., if `dw-case-brain-crim` has been loaded for this case). If so, register the output:

1. **Append to COMPANION SKILL OUTPUTS** in the Case Brain:
   - Skill: `dw-chain-of-custody-auditor-crim`
   - Output: `[filename of deliverable]`
   - Date: `[today's date]`
   - Location: `[path where the deliverable was saved]`

2. **Add to OPEN ISSUES** if the audit identified any items requiring attorney action.

3. **Update NEXT STEPS** if the audit output changes the recommended case strategy.

If no Case Brain session is active, skip this step silently — the deliverable is still saved to the case folder and will be discovered by `dw-case-dashboard-crim` and `dw-trial-notebook-builder-crim` during their folder scans.

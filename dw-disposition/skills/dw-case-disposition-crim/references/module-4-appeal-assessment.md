# Module 4 — Appeal Assessment

Read at Step 4 (Appeal Assessment) when the disposition is a Guilty Plea or Guilty Verdict; includes the Step 5A appeal workflow.

**Trigger:** Case disposition is Guilty Plea OR Guilty Verdict.

### Appeal Viability Check

1. **Display Appeal Deadline Prominently**
   ```
   APPEAL DEADLINE: [Calculate: Date + 30 days from sentence]
   (La. C.Cr.P. Art. 914 — Motion for appeal must be filed within 30 days of sentence)
   (Misdemeanor appeals: 2 days from date sentence)
   ```

2. **Prompt Attorney Decision**
   ```
   "Do you want to run dw-appellate-error-monitor-crim for an appeal viability assessment?"
   ```

3. **If Attorney Selects YES (Pursuing Appeal)**
   - Invoke **dw-appellate-error-monitor-crim**
   - Pass: Complete trial transcript, trial errors preserved, sentencing transcript
   - Review error log for preserved trial errors
   - Assess viability of appeal based on error preservation
   - **CRITICAL:** Do NOT archive case while appeal is being pursued
   - Mark case status: "APPEAL PENDING — DO NOT ARCHIVE"
   - Save intermediate state to Case Brain
   - Schedule follow-up per appellate timeline
   - Proceed to Step 5A (appeal path)

4. **If Attorney Selects NO (No Appeal)**
   - Record decision in Case Brain: "No appeal pursued"
   - Proceed to Step 5B (expungement eligibility check)

### Step 5A: Appeal Workflow (if applicable)

- Ensure trial transcript is complete and ordered
- Preserve record for appellate review
- Brief attorney on appellate deadlines and filing requirements
- Do NOT proceed to file archival yet
- Notify attorney when appeal is final (appellate court decision rendered)
- Then return to Step 5B for post-appeal actions

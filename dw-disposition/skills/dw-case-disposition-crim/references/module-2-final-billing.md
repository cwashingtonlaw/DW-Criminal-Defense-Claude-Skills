# Module 2 — Final Billing

Invoke **dw-billing-narrative-generator-crim** to capture all unbilled session work and generate a comprehensive billing summary.

## Billing Process

1. **Run dw-billing-narrative-generator-crim**
   - Pass: All case numbers, client name, disposition date
   - Generates: Complete billing narrative for all work across entire case lifecycle
   - Captures: Any unbilled sessions, memos, phone calls, travel, research

2. **Generate Final Billing Summary**
   - Create Excel workbook with following sheets:
     - **Summary Sheet:** Total hours by LEDES category (e.g., Initial Consultation, Pretrial Motions, Trial, Sentencing)
     - **Detail Sheet:** Line-item breakdown by date, hours, description, LEDES code, amount
     - **By Phase:** Investigation, Pretrial, Trial/Plea, Sentencing, Appellate (if any)
   - Calculate total fees, costs reimbursed, outstanding balance
   - Apply any final adjustments or fee reductions per attorney direction

3. **Save Final Billing Summary**
   - **Path:** `<case-root>/05 - Billing/[ClientLastName] - Final Billing Summary - [Date].xlsx`
   - Include: Client name, case number, disposition type, disposition date, invoice date range

4. **Flag for Attorney Review**
   - Highlight any outstanding invoices or unbilled time
   - Present summary to attorney for final approval before case is archived
   - Attorney signs off on final billing before proceeding to Step 3

## Billing Summary Template Items

- Total hours (all categories)
- Total fees (per agreed rate)
- Total costs reimbursed
- Outstanding balance
- Retainer applied / refund due
- Court-appointed case rate (if applicable)
- Payment schedule or lump sum due date

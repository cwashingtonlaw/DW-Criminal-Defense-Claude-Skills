# Cross-Exam, Motion-Routing, and Action-Plan Integration

## Cross-Exam Architect Integration
For each Critical or Significant Giglio finding, generate a cross-examination chapter seed:

```
CROSS CHAPTER SEED — [Witness Name]: [Finding Title]
Witness Type: [Law Enforcement / Civilian / Expert]
Chapter Goal: [What this chapter must establish]
Key Questions:
  Q1: [Question targeting the undisclosed material]
  Q2: [Follow-up locking in the gap]
  Q3: [Question establishing prejudice from non-disclosure]
Source: [Document / page reference]
Impeachment Note: [How this undermines the witness]
Legal Authority: [Applicable Brady/Giglio case]
```

Tag each seed: `[READY FOR CROSS-EXAM ARCHITECT — pass to dw-cross-exam-architect skill]`

## Motion Routing Integration
When Critical violations are identified, route to the appropriate motion skill (**dw-pretrial-motion-library** for Motion to Compel / "Reveal the Deal"; **dw-suppression-motion** for CI-tainted evidence):
- Motion to Compel Discovery (La. C.Cr.P. Art. 718-729)
- Brady/Giglio Motion (with specific items and Kyles cumulative analysis)
- Motion for Sanctions (La. C.Cr.P. Art. 729.3) when violations are willful or repeated

## Case Analysis Integration
Feed audit findings back into the broader case analysis:
- Update the Master Evidence Table with any newly identified favorable evidence
- Flag items for the Discovery Gap Report
- Note any items that affect witness credibility assessments

## Brady/Giglio Audit Action Plan

After the audit report is generated, translate findings into strategic next steps using this framework:

1. **Discovery Demands:** For each identified category of undisclosed Brady/Giglio material, generate a specific discovery demand citing the item, the legal basis for disclosure, and the deadline.
2. **Suppression Opportunities:** If a CI taints evidence or an undisclosed deal undermines witness credibility, identify suppression opportunities and route to **dw-suppression-motion**.
3. **Strategic Prioritization:** Rank Brady/Giglio items by trial impact: which undisclosed items, if obtained, would most change the jury's assessment? Focus demand letters and motion practice on these items first.
4. **CI-Specific Discovery:** If the CI Detection Module identified confidential informants, generate specific demands for: CI agreements, CI criminal history, CI payment records, CI handler notes, and all communications between CI and law enforcement.

This action plan transforms the audit's findings into executable litigation steps. The attorney reviews the plan and approves which demands and motions to pursue.

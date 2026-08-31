# Workflow Summary & Integration with Other DW Skills

Read from SKILL.md (Workflow Summary / Integration section) when you need the end-to-end step map or an upstream/downstream skill routing decision.

## WORKFLOW SUMMARY

```
STEP 0: File Intake Hard Stop
  └─→ Wait for user to confirm all uploads complete

STEP 1: Information Gathering
  └─→ Collect Essential → Strategic → Contextual tiers
  └─→ Flag missing items; request before proceeding

STEP 2: Predicate Inventory & Classification
  └─→ Build predicate inventory table
  └─→ Classify each predicate (crime of violence determination)

MODULE A: Predicate Conviction Audit
  └─→ Verify five elements for each predicate
  └─→ Assign severity rating to each predicate

MODULE B: Boykinization Challenge
  └─→ Audit plea transcript against Boykin/Shelton checklist
  └─→ Classify deficiencies by severity
  └─→ Apply temporal considerations (pre/post-1997)

MODULE C: Sequence Analysis
  └─→ Verify conviction-then-commission sequence
  └─→ Determine finality dates for each predicate
  └─→ Identify sequence breaks

MODULE D: Cleansing Period Calculator
  └─→ Calculate elapsed time between sentence completion and next offense
  └─→ Determine whether cleansing period exceptions apply
  └─→ Generate timeline visualization

MODULE E: Enhancement Tier Calculator
  └─→ Determine applicable tier based on valid predicates
  └─→ Calculate enhanced sentencing range
  └─→ Account for 2017 reform applicability

MODULE F: Constitutional Challenge Assessment
  └─→ Evaluate Dorthey excessive sentence viability
  └─→ Assess proportionality under La. Const. Art. I, Sec. 20 and 8th Amendment
  └─→ Prepare Dorthey motion framework if viable

MODULE G: Hearing Preparation
  └─→ Prepare challenge arguments for each deficient predicate
  └─→ Build defense exhibits
  └─→ Prepare cross-examination of State's witnesses
  └─→ Generate hearing preparation checklist

MODULE H: Plea Negotiation Impact
  └─→ Calculate true habitual offender exposure
  └─→ Assess habitual bill strength/vulnerability
  └─→ Framework for negotiation leverage and objectives

OUTPUTS: Generate applicable outputs (1-7) based on case needs
```

---

## Integration with Other DW Skills

| Skill | How It Integrates |
|-------|------------------|
| `dw-shared-protocols-crim` | Centralized boilerplate for filed pleadings (caption, signature, COS, notice of hearing, proposed order, citation style, filing conventions) and for output path resolution. Read before drafting Output 2 (Habitual Bill Response/Challenge), Output 3 (Boykin Motion), and Output 6 (Dorthey Motion). Audit deliverables (Outputs 1, 4, 5, 7) consume only `attorney-work-product-marking.md` and `output-path-formula.md`. |
| `dw-criminal-defense-crim` | Phase 0 LWOP Assessment flags habitual offender exposure; Initial Case Profile identifies prior conviction history; Phase 2 analysis may trigger habitual offender audit |
| `dw-404b-opposition-crim` | Prior convictions used as habitual offender predicates may also be the subject of a 404(b) notice — coordinate challenges to ensure consistent positions |
| `dw-discovery-compliance-monitor-crim` | Prior conviction packets, plea transcripts, and certified records should be tracked in discovery — request through Brady/discovery demands if not provided |
| `dw-sex-offense-specialist-crim` | Sex offense predicates carry no cleansing period; sex offense cases frequently involve habitual offender exposure |
| `dw-voir-dire-assistant-crim` | Post-2017 habitual offender determinations are made by jury — voir dire must address juror attitudes toward enhanced sentencing and recidivism |
| `dw-expert-witness-evaluator-crim` | Fingerprint experts testifying to identity at habitual offender hearings may be subject to expert qualification and methodology challenges |
| `docx` | Document generation — read for .docx creation instructions |
| TextExpander | `;draft` (caption / signature / COS now sourced from `dw-shared-protocols-crim`) |

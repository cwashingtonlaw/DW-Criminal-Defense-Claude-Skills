# dw-settlement-demand

Louisiana personal injury settlement demand letter and mediation position paper generator. Reads the client case file (medical records, medical chronology, police/crash report, wage documentation, deposition transcripts, witness statements, photos) and produces a fully drafted .docx in either:

- **Settlement Demand** mode (letter-style, defense-counsel-addressed, transactional, math-forward)
- **Mediation Position Paper** mode (roman-numeral, mediator-addressed, narrative, "trial vs. today" anchor)
- **Hybrid** mode (mediator-addressed but with long-demand internal structure)

---

## How to install as a Cowork / Claude skill

1. Copy this entire `dw-settlement-demand/` folder into the firm's skills directory:
   - Cowork plugin path: `~/Library/Application Support/Claude/.../skills/`
   - Local user skill path: `/var/folders/.../claude-hostloop-plugins/.../skills/`
   - Or wherever the firm's existing `dw-*` skills live (e.g., alongside `dw-bond-and-release-motion/`).

2. The skill's `SKILL.md` includes a Claude skill frontmatter block — the skill manager will pick it up automatically once it's in the skills directory and the Cowork session restarts.

3. Trigger phrases:
   - "Draft a settlement demand for [Client Name]"
   - "Build a mediation position paper for [Client Name]"
   - "Generate a detailed settlement brief"
   - "We're mediating next week — write the position paper"
   - "Put together the mediation package"

---

## What's in this folder

```
dw-settlement-demand/
├── SKILL.md                                    # Entry point — the workflow
├── README.md                                   # This file
└── references/
    ├── inputs-checklist.md                     # Every input the skill needs, ranked
    ├── house-style.md                          # Letterhead, captions, signatures, boilerplate
    ├── settlement-demand-template.md           # The letter-style scaffold (demand mode)
    ├── mediation-position-paper-template.md    # The roman-numeral scaffold (mediation paper mode)
    ├── damages-playbook.md                     # Past meds, future meds, lost wages, GD math
    ├── liability-playbook.md                   # How to build FACTS and LAW sections
    ├── louisiana-quantum-cases.md              # Quantum-case bank by body region
    ├── louisiana-statutes.md                   # Traffic-statute lookup (R.S. 32:58, 81, 122, etc.)
    ├── louisiana-judicial-interest.md          # Annual rate table + worked calc
    ├── persuasion-playbook.md                  # 16 firm-corpus techniques + 3 modern best practices
    ├── worked-example.md                        # End-to-end walkthrough on a hypothetical case
    └── qa-checklist.md                         # Mandatory pre-output QA pass
```

---

## How the skill thinks

The workflow follows 13 ordered steps:

| Step | What it does |
|------|--------------|
| 0 | File-intake hard stop — confirms no more uploads pending |
| 0.5 | Reads every reference file |
| 1 | Locks the mode (demand / mediation_paper / hybrid) |
| 2 | Walks the inputs checklist, marks each as PROVIDED / AVAILABLE-IN-FILES / MISSING |
| 3 | Reads and extracts from medical records, chronology, police report, depositions, wage docs |
| 4 | Drafts the caption and header (letterhead, addressee, RE: block, banner) |
| 5 | Drafts the liability section (FACTS for demand; FACTS + LAW for mediation paper) |
| 6 | Drafts the injuries and treatment section (per-provider, chronological, or chronology-pointer) |
| 7 | Drafts the special damages section (per-provider table + future meds + wages) |
| 8 | Drafts the general damages section (body-region buckets with quantum cases) |
| 9 | Drafts the judicial interest section (year-by-year math) |
| 10 | Drafts the demand statement and RECAP table |
| 11 | Mandatory QA pass (name / math / typos / citations / boilerplate) |
| 12 | Generates the .docx via the `docx` skill |
| 13 | Presents the draft with attorney-review flags |

---

## Built from analysis of 10 firm samples

The skill scaffolding, section structure, boilerplate strings, and persuasion patterns are reverse-engineered from 10 prior Daniels & Washington Law Firm demand/mediation papers spanning 2015–2025 (Polk, Boudreaux, Antoine, Hopes, Brooks, Monroe, Williams, Landry, plus the firm's reusable shells).

A full structural analysis report is saved at `../\_analysis_report.md` (in the parent folder of this skill — `Mediation Position Paper/_analysis_report.md`) and documents:
- Section-by-section inventory across all 10 documents
- House-style invariants (letterhead, RE-caption, signature, boilerplate strings)
- Damages math conventions (per-provider tables, projection tables, JI calculation)
- Demand vs. mediation paper differences (the basis for the `mode` flag)
- Notable persuasion techniques pulled from the most polished examples

---

## Best practices baked in (from 2025 industry research)

- Concise but complete — mediator-magazine consensus is 10–15 pages for the paper, with detail pushed to attachments.
- Specific over general — every claim lands on a date, a provider, a quote, a dollar figure.
- Acknowledge weaknesses head-on — pre-existing conditions, treatment gaps, defense expert opinions are addressed, not hidden.
- Tell the story once, cleanly, in order — no doubling back.
- Math is single-sourced — every dollar figure traces to one source of truth.
- Demand reasonableness discipline — flag any demand more than 3× plausible jury verdict for attorney review.
- Disclose policy-limits BATNA when applicable — but never bluff.

---

## Generic Louisiana PI default

This skill is set up as a generic Louisiana PI tool — it defers to Louisiana law (R.S. 32:58, 32:81, 32:121–124, 9:2800.6, 13:4202–4203, C.C. art. 2315/2316/2323) and to Louisiana quantum cases. The firm-letterhead block is configurable; the skill will prompt for firm info on first run and cache it to a `firm-info.json` for subsequent runs.

If used outside Louisiana, the attorney should:
1. Update the `louisiana-statutes.md` reference with the applicable jurisdiction's traffic-code analogs.
2. Update the `louisiana-quantum-cases.md` reference with the applicable jurisdiction's quantum-case bank.
3. Update the `louisiana-judicial-interest.md` reference with the applicable jurisdiction's interest rules.
4. Adjust the boilerplate citations in `house-style.md` and `liability-playbook.md` to match.

---

## Integration with companion skills

- **`medical-chronology`** — primary upstream input. The skill prefers a structured chronology .docx and falls back to raw medical records if no chronology exists.
- **`docx`** — used to render the final .docx output.
- **`pdf`** — used to extract text from medical records, the crash report, and other PDF source material.
- **`dw-shared-protocols`** — for D&W-anchored cases, the skill follows the firm's output-path formula and caption boilerplate.

---

## Version

**1.0** — built May 12, 2026, from 10 firm sample documents (2015–2025) + 2025 industry best-practices research.

---

## Attorney guardrails

- Every output is a draft for attorney review.
- Every fact, citation, dollar figure, and demand number is verified by the attorney before sending or signing.
- The skill flags every `[UNSOURCED — VERIFY]`, `[RESEARCH — confirm citation]`, `[ATTORNEY-DECISION]`, and `[GAP]` item in the final delivery message.
- The skill never fabricates a citation or a medical opinion.
- The skill never invents a damages number — categories without supporting evidence are written as "Not factored in" or "TBD."

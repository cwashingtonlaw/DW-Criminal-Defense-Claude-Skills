# Drafting, Attorney Review, and Output Location

## Draft the Motion and Memorandum

For each motion type, generate two .docx files following the `docx` skill conventions:

1. **Motion** (2-3 pages): Short-form filing with facts and prayer for relief
2. **Memorandum in Support** (5-20 pages depending on complexity): Full legal argument

Apply caption, signature block, certificate of service, notice of hearing, proposed order, formatting, and filename conventions per shared protocols (see Step 0.5 — `dw-shared-protocols`).

---

## Attorney Review & Integration

**Review flags:**
- `[VERIFY — confirm this fact with client/discovery]`
- `[RESEARCH — confirm current validity of this citation]`
- `[ATTORNEY TO COMPLETE]` — signature, bar number, specific dates
- `[STRATEGIC DECISION]` — which arguments to include/exclude

**Save location:** Use the output path formula from `dw-shared-protocols/references/output-path-formula.md`. Filed motions go to `{{CASE_ROOT}}/02 - Pretrial Notebook/01 - Pleadings/`.

- Create Clio task: *"Review and File [Motion Type] — [Client Name]"*
- Update Case Brain with motion status

**Companion skill handoffs:**
- Report 3 Red Flags → trigger specific motion modules
- Report 7 Missing Discovery → trigger Module 4 (Motion to Compel)
- Brady/Giglio CI findings → trigger Module 11 (Reveal the Deal)
- Suppression issues → hand off to `dw-suppression-motion`
- 404(b) issues → hand off to `dw-404b-opposition`

---

## Output Location

Use the output path formula from `dw-shared-protocols/references/output-path-formula.md`. Filed motions go to `{{CASE_ROOT}}/02 - Pretrial Notebook/01 - Pleadings/`. The Pre-Trial Motion Action Plan (internal analysis, Step 2.5) goes to `{{CASE_ROOT}}/01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/`. See shared protocols for CASE_ROOT resolution, filename conventions, and post-write reporting format.

# Master Witness Table Generation

**Generate a comprehensive witness inventory immediately after STEP 1 information gathering.**

This table becomes the backbone of all cross-examination outline sequencing. Every witness appearing in any cross-examination outline must have a corresponding row in this master table.

## Master Witness Table Structure

Create a 5-column inventory table with the following columns:

| Column 1: Contact Info | Column 2: Witness Type & Page Refs | Column 3: Association with Case | Column 4: Source Documents | Column 5: Trial Exam Status |
|---|---|---|---|---|
| Name, Address, Phone (from discovery) | Type (Eyewitness, Fact, Expert, LEO, Fact Witness, Complainant, etc.) + page numbers in discovery where witness identified | Who/What/When: Who is this witness? What will they testify to? Reasons to call vs. not call? Anticipated demeanor/credibility issues? | Precise document citations: List every source document (report, statement, deposition, etc.) where this witness appears, with page/Bates/timestamp | Direct/Cross status? Yes/No in final trial? Witness #? (if sequenced) |

## Rules for Master Table Completion

1. **Complete contact information:** Name, address, phone number pulled directly from discovery materials (reports, witness lists, interviews)

2. **Witness type classification:** Use precise categories:
   - Eyewitness (observed key event)
   - Fact Witness (observed non-key facts, transactions, communications)
   - Expert Witness (forensic, medical, scientific opinion)
   - Law Enforcement / Officer (police, detective, agent, investigator)
   - Complainant (crime victim or report maker)
   - Co-defendant / Accomplice Witness
   - Character Witness
   - Document Custodian / Business Records
   - Other [specify]

3. **Association with Case column:** For each witness, note:
   - Who are they? (relationship to defendant, victim, crime scene, evidence)
   - What will they testify to? (key assertions on direct)
   - Reasons to call them in your case? (if applicable)
   - Reasons NOT to call them? (credibility risk, weak testimony, harmful admissions)
   - Anticipated demeanor / credibility profile (confident/defensive, truthful/evasive, articulate/rambling, biased/neutral)

4. **Source Documents column:** List every source where the witness appears:
   - Format: `(N) Document Title, page/Bates/timestamp`
   - Use the source register numbering scheme if already established
   - Include: police reports, witness statements, interviews, depositions, preliminary hearing transcripts, recordings, social media, email, text messages, search warrant returns
   - Note any omissions (missing statement, missing interview, expected document not produced)

5. **Trial Exam Status column:**
   - **Direct / Cross?** (Will this be a prosecution or defense witness?)
   - **Yes / No?** (Is this witness definitely being called, or tentatively on the list?)
   - **Witness #?** (Sequential position in trial order, if set; otherwise "TBD")

## Integration with Cross-Examination Outline

**Critical Rule:** Every witness who appears in any cross-examination outline MUST have a corresponding entry in the Master Witness Table. If a cross-exam outline covers Witness A, Witness A must be findable in the master table by name and must have complete contact info, type, association notes, sources, and trial status.

**Purpose:** The master table is your discovery-to-trial tracking tool. It ensures:
- No witness contact info is missing (critical for subpoena drafting)
- Witness sequences are consistent across all outlines
- Source documents are tracked consistently (matching the source register in each outline)
- Strategic decisions about whom to call/challenge are documented
- Cross-examination priorities are aligned with the Witness Prioritization audit (Step 0.6)

## Output Format

Present the Master Witness Table as:
- A formatted table (Excel, Google Sheets, or markdown table)
- Sortable by: Witness Type, Trial Status, Impeachment Strength (linked to Step 0.6 findings), or Trial Sequence
- Refreshed and updated every time a new cross-examination outline is generated (to track cumulative witness coverage)

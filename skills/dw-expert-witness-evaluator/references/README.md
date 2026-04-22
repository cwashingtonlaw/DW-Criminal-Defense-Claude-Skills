# Expert Witness Evaluator — Reference Guide

This directory contains static reference material extracted from the main SKILL.md to improve maintainability and discoverability.

## Files at a Glance

| File | Size | Purpose | When to Use |
|------|------|---------|------------|
| **legal-authorities.md** | 3.2 KB | Louisiana expert witness law and case citations | Building Daubert motions; understanding legal standards |
| **scientific-reports.md** | 4.8 KB | Forensic reliability research (NAS, PCAST, DOJ, FBI) and error rates | Assessing methodology reliability; supporting Daubert challenges |
| **discipline-standards.md** | 6.6 KB | Certification bodies, qualification standards, and red flags by forensic discipline | Evaluating expert credentials; assessing qualification deficiencies |
| **daubert-foret-framework.md** | 7.7 KB | Complete Daubert/Foret reliability framework and analysis guidance | Preparing reliability challenges; understanding five-factor test |
| **cross-exam-seeds.md** | 13.8 KB | Cross-examination templates for 10 forensic disciplines | Preparing cross-examination strategy; developing courtroom questioning |
| **evaluation-checklists.md** | 7.1 KB | Checklists, motion templates, and discovery demands | Planning evaluations; structuring motions; ensuring complete discovery |

---

## Quick Navigation by Task

### "I'm evaluating a DNA expert..."
1. Start in SKILL.md with MODULE A (credential analysis) and MODULE C (methodology)
2. Reference **discipline-standards.md** → DNA / Forensic Biology section for certification requirements
3. Reference **scientific-reports.md** → DNA section for error rates and validation concerns
4. Reference **cross-exam-seeds.md** → 1. DNA / Forensic Biology for cross-exam questions

### "I'm building a Daubert motion..."
1. Read **daubert-foret-framework.md** for the complete five-factor analysis framework
2. Read **legal-authorities.md** for Louisiana case law and statutory citations
3. Use **evaluation-checklists.md** → Common Daubert/Foret Motion Structure template
4. Reference **scientific-reports.md** for error rate data to support your arguments
### "I need cross-examination questions for a firearms expert..."
1. Go to **cross-exam-seeds.md** → 3. Firearms / Toolmarks
2. Use qualification seeds, methodology seeds, and bias/limitation seeds as question templates
3. Reference **discipline-standards.md** → Firearms / Toolmarks for standards the expert should follow
4. Reference **scientific-reports.md** → Firearms section for error rate data to cite

### "I'm auditing an expert's credentials..."
1. Start in SKILL.md with MODULE A (credential analysis)
2. Reference **discipline-standards.md** → relevant discipline for certification standards and red flags
3. Use **evaluation-checklists.md** → Daubert/Foret Viability Checklist for credential challenges
4. Reference **legal-authorities.md** for legal standards under Art. 702

### "I need an expert discovery demand..."
1. Use **evaluation-checklists.md** → Expert Discovery Demands table
2. Reference **legal-authorities.md** for the statutes and constitutional authorities supporting each demand
3. Customize based on SKILL.md STEP 1 (Information Gathering Protocol)

### "I'm assessing methodology reliability..."
1. Start in SKILL.md with MODULE C (methodology reliability assessment)
2. Reference **daubert-foret-framework.md** for the five-factor analysis framework
3. Reference **discipline-standards.md** for published standards in the expert's discipline
4. Reference **scientific-reports.md** for NAS/PCAST findings and error rate data

---

## Reference File Details

### legal-authorities.md
Contains:
- Louisiana Code of Evidence articles (Art. 702-705)
- Federal standards (Daubert, Kumho Tire, Joiner)
- Louisiana cases (State v. Foret, State v. Chauvin, State v. Quatrevingt)
- Brady and Giglio obligations
- Procedure and discovery articles

Use this file when:
- Drafting legal arguments
- Citing Louisiana law in briefs
- Understanding statutory requirements
- Researching case law authority

### scientific-reports.md
Contains:
- Summaries of major forensic reliability reports (NAS 2009, PCAST 2016, DOJ Uniform Language 2018+)
- Error rate data by discipline (latent prints, firearms, DNA mixtures, bloodstain patterns, hair, digital forensics, toxicology, pathology, accident reconstruction, cell site)
- Context and limitations of error rate studies
- Findings of major scientific bodies

Use this file when:
- Assessing error rates for methodology (Daubert Factor 3)
- Supporting general acceptance arguments (Daubert Factor 5)
- Citing scientific authority for methodology criticisms
- Understanding what NAS and PCAST reported about specific disciplines

### discipline-standards.md
Contains:
- Standards bodies for 10 forensic disciplines
- Certification requirements and standards for each discipline
- Educational background expectations
- Red flags and concerns specific to each discipline

Use this file when:
- Evaluating expert credentials
- Identifying certification deficiencies
- Understanding what training is standard in the discipline
- Attacking qualification under Art. 702

### daubert-foret-framework.md
Contains:
- Louisiana modified Daubert standard (Art. 702 four-part test)
- Complete explanation of all five Daubert factors with guidance
- Discipline-specific considerations for each factor
- Additional factors (analytical gap, litigation-driven opinions)
- Daubert/Foret challenge framework template

Use this file when:
- Developing a Daubert challenge
- Understanding the five-factor reliability test
- Structuring a motion to exclude
- Analyzing whether a challenge is viable

### cross-exam-seeds.md
Contains:
- General cross-examination principles and architecture
- Discipline-specific cross-examination question templates for:
  1. DNA / Forensic Biology
  2. Latent Fingerprints
  3. Firearms / Toolmarks
  4. Digital Forensics
  5. Toxicology
  6. Forensic Pathology
  7. Mental Health (Competency / Sanity)
  8. Accident Reconstruction
  9. Bloodstain Pattern Analysis
  10. Cell Site / Geolocation

Each discipline section includes:
- Qualification seeds (attacking credentials)
- Methodology seeds (attacking reliability)
- Bias/limitation seeds (establishing contextual factors)

Use this file when:
- Preparing cross-examination
- Developing questioning strategy
- Looking for specific questions to ask
- Understanding discipline-specific vulnerabilities

### evaluation-checklists.md
Contains:
- Daubert/Foret viability checklist
- Common Daubert/Foret motion structure template
- Expert discovery demands checklist
- Critical implementation notes and guardrails

Use this file when:
- Planning an expert evaluation
- Checking whether a challenge is viable
- Structuring a motion to exclude
- Making discovery demands
- Understanding implementation requirements

---

## File Dependencies

These reference files are interdependent. When using one, you may be directed to another:

- **For a DNA expert challenge**: discipline-standards.md → scientific-reports.md → cross-exam-seeds.md
- **For a Daubert motion**: daubert-foret-framework.md → legal-authorities.md → scientific-reports.md
- **For discovery demands**: evaluation-checklists.md → legal-authorities.md
- **For cross-exam strategy**: cross-exam-seeds.md → discipline-standards.md → scientific-reports.md

---

## Maintenance Notes

### Annually Update
- **scientific-reports.md**: New error rate studies and forensic reliability research may emerge
- **discipline-standards.md**: Certification requirements and standards bodies may change

### Verify Periodically
- **legal-authorities.md**: Check that cited cases have not been overruled or modified

### Unlikely to Change
- **daubert-foret-framework.md**: Stable unless Louisiana law changes
- **cross-exam-seeds.md**: Methodology remains consistent; update if discipline standards change
- **evaluation-checklists.md**: Stable framework; update if legal standards change

---

## Integration with SKILL.md

The main SKILL.md references these files throughout:
- At the end of each MODULE, you'll find "Reference:" callouts pointing to the relevant reference file
- MODULE A mentions discipline-standards.md
- MODULE B mentions daubert-foret-framework.md
- MODULE C mentions discipline-standards.md and scientific-reports.md
- MODULE G mentions cross-exam-seeds.md
- STEP 1 mentions evaluation-checklists.md for discovery demands

Follow these references to dive deeper into specific topics.

---

## Total Package

- **SKILL.md**: 33.8 KB (main workflow and evaluation logic)
- **References**: 43.3 KB (static reference material)
- **Total**: 77.3 KB

The refactoring maintains full functionality while improving discoverability and maintainability.
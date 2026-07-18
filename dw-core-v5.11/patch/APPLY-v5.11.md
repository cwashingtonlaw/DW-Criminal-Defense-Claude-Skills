# dw-core — apply v5.11 (Criminal Defense skill)

Four files for `skills/dw-criminal-defense-crim/`:
- SKILL.md ....................................... updated (v5.11)
- CHANGELOG.md .................................. updated (v5.11 entry)
- references/case-profile-procedure.md .......... updated (11 sections, ingest, roll-up, renumber pass)
- references/art814-responsive-verdict-map.md ... NEW file

## Apply from your dw-core repo root
Extract this archive so the `skills/...` paths overlay the repo, then:

    git checkout -b v5.11-prosecution-theory-art814
    git add skills/dw-criminal-defense-crim/SKILL.md \
            skills/dw-criminal-defense-crim/CHANGELOG.md \
            skills/dw-criminal-defense-crim/references/case-profile-procedure.md \
            skills/dw-criminal-defense-crim/references/art814-responsive-verdict-map.md
    git commit -m "dw-criminal-defense-crim v5.11: Prosecution Theory section, Art. 814 auto-verdicts, JusticeWorks ingest"
    git push -u origin v5.11-prosecution-theory-art814

Then open a PR from that branch. If the repo root IS the plugin folder
(contains .claude-plugin/ and skills/), the paths above are already correct.

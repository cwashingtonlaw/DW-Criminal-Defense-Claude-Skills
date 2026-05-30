# Step 4 — Live Trial Tracking

During trial, update exhibit status in real-time as attorney reports offers and rulings. Use exact timestamped language:

**Exhibit Offered:**
- "D-1 offered" → Status: Offered | Time: [HH:MM] | During: [witness name]
- Record which witness testimony context

**Objection Lodged:**
- "D-1 objection — hearsay" → Log in Objection Log
- Objecting party: State / Defense
- Basis: Hearsay, authentication, relevance, unfair prejudice, best evidence, Confrontation, expert methodology, etc.
- Objecting attorney name

**Ruling Made:**
- "D-1 objection overruled, admitted" → Status: Admitted | Ruling: Overruled | Time: [HH:MM]
- "D-1 objection sustained, excluded" → Status: Excluded | Ruling: Sustained | Time: [HH:MM]
- Record judge's exact ruling language if possible

**Limiting Instruction:**
- If court gives limiting instruction ("Exhibit D-1 admitted only for [specific purpose], not for [excluded purpose]")
- Record exact language for appellate purposes

**Automatic Appellate Flag:**
- Every excluded exhibit (Ruling: Sustained) → AUTOMATICALLY flag to **dw-appellate-error-monitor-crim**
  - "Exhibit [#] excluded — [basis] — trial date [date] — Judge [name] — Preserve for appeal"

**Withdrawn:**
- If attorney withdraws exhibit offer before ruling: Status: Withdrawn | Time: [HH:MM]
- Note reason if disclosed (e.g., authentication foundation missing, opposing counsel made record objection)

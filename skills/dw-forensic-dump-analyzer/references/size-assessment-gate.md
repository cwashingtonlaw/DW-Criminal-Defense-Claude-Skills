# Size Assessment Gate — Single-Pass vs. Chunked Decision

## Decision Matrix

Assess total data volume BEFORE loading any file contents. Use this 3-row decision table to determine analysis mode:

| Condition | Mode | Action |
|-----------|------|--------|
| < 15,000 rows AND < 2MB AND ≤ 3 categories | **Single-Pass** | Proceed directly to Step 2 |
| ≥ 15,000 rows OR > 2MB OR > 3 categories | **Chunked** | Read `references/chunking-protocol.md` for tier-based workflow |
| Full extraction folder with 5+ categories | **Always Chunk** | Read `references/chunking-protocol.md` immediately |

## Assessment Workflow

1. Run `scripts/preprocessing.py` for the size assessment utility
2. Count total rows across all data categories
3. Sum total file sizes
4. Count distinct data categories present
5. Match conditions to table above
6. Inform attorney: *"[N] records across [N] categories — [single-pass / chunked starting with Tier 1: category]."*

## Chunked Mode Workflow

If Chunked or Always Chunk mode is triggered, read `references/chunking-protocol.md` for:
- Tier structure (T1, T2, T3)
- Category-to-tier mapping
- Completion tracking
- Cross-chunk lead synthesis
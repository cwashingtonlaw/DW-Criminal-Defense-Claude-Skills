# Extraction Authentication Chain Template

## Structured Authentication Chain Format

Establish the auth chain ONCE for the entire extraction at Step 2:

```
EXTRACTION AUTHENTICATION
──────────────────────────────────────────
Examiner:        [Name, agency, credentials]
Tool/Version:    [Cellebrite UFED vX.X / GrayKey / etc.]
Extraction Date: [Date]
Hash Verified:   [Yes — SHA256: xxxx / No / Unknown]
Chain of Custody: [Documented / Gap: specify]
──────────────────────────────────────────
```

## Required Fields

1. **Examiner** — Full name, agency affiliation, certifications/credentials
2. **Tool/Version** — Specific extraction tool and version number
3. **Extraction Date** — Date and time of extraction
4. **Hash Verified** — SHA256 or MD5 verification status and hash value
5. **Chain of Custody** — Documented chain or specific gaps identified

## Application

This authentication chain covers all findings from this extraction. Only note per-finding auth exceptions where a specific finding has a different or weaker chain (e.g., WAL recovery not hash-verified, data from a second extraction with a different tool).
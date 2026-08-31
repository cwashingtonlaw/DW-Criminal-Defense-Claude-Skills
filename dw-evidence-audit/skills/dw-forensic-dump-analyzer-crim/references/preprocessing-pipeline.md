# Preprocessing Pipeline

Read this file at STEP 2 (Data Inventory, Preprocessing & Integrity Checks) — it holds the five ordered preprocessing steps run by scripts/preprocessing.py or applied manually.

Run `scripts/preprocessing.py` or apply these steps manually in order:

**1. Duplicate & Artifact Detection:** Deduplicate on content + timestamp + sender/recipient. Preserve originals, flag duplicates.

**2. Encrypted / Locked Container Inventory:** Identify locked apps/containers, assess defense impact, flag for **dw-mobile-forensic-auditor-crim** handoff if tool should have decrypted it.

**3. Selective Extraction Detection:** Compare production against expected full extraction. Flag curated production → **dw-brady-giglio-auditor-crim** handoff.

**4. Shared Device / Multiple User Detection:** Check for style changes, activity during confirmed absence, inconsistent profiles.

**5. Platform Differentiation:** When analyzing messages, always classify by platform (SMS vs. iMessage vs. RCS vs. app-based). Use the `classify_message_platform()` function in `scripts/preprocessing.py` to add a `_platform` column to message data. This matters for defense: iMessage "Delivered" and "Read" timestamps are independently verifiable evidence of message receipt and reading. Read receipts are powerful for proving the recipient saw a specific message at a specific time. RCS includes typing indicators and read receipts. SMS has none of these — no delivery confirmations, no read receipts. Never let the prosecution conflate platform-specific features across different message types. A "read receipt" claim is worthless if the message was sent via SMS.

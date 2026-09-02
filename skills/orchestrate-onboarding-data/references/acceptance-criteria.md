# Acceptance criteria — orchestrate-onboarding-data

Scenarios this skill should handle correctly. This is source material for a real
`claude plugin eval` suite (`evals/<case>/prompt.md` + `graders/*.md`), not a substitute for one —
convert it once `plugin eval` early access is available.

## Scenario 1: Full onboarding packet across connected systems

**Prompt:** "Process this client onboarding packet, reconcile it with our connected systems, and set
up the complete relationship."

**Expected output:** Client and household resolved across systems before any write; duplicates
searched; each value classified and routed; per-system reconciliation returned.

**Expectations:**
- Resolves the client and household across connected systems BEFORE creating or updating any record
- Searches for possible duplicates before creating a contact or household
- Classifies each extracted value as supported, conflicting, incomplete, stale, or not appropriate
  for the proposed destination
- Where another system should hold a value but cannot be written to, creates a clearly assigned
  Wealthbox follow-up instead of dropping it
- Ends with a per-system reconciliation listing sources processed, records matched or created, values
  written, unchanged values, conflicts, and missing information

## Scenario 2: Assembling a household with an explicit conflict list

**Prompt:** "Use these forms, custodial records, planning data, and meeting notes to assemble the
household and tell me what still conflicts."

**Expected output:** Normalized onboarding profile plus an explicit conflict list with source
attribution per value.

**Expectations:**
- Every extracted value carries a source reference
- Distinguishes genuine conflicts from values that describe different scopes or dates
- Does not silently pick a winner when two sources disagree
- Names which system is authoritative for each class of data

## Scenario 3: Intake packet vs. prior advisor's file

**Prompt:** "Here's the new client's intake packet and their prior advisor's file — build the
household and flag anything that doesn't match."

**Expected output:** Household resolved with duplicate search performed first; mismatches between the
two source documents surfaced explicitly, not merged.

**Expectations:**
- Searches for possible duplicate contacts or households before creating anything
- Resolves the household first, then fans out to members, when the packet describes a family or
  couple
- Flags disagreements between the intake packet and the prior advisor's file rather than silently
  preferring one
- Never creates a contact to resolve an ambiguity

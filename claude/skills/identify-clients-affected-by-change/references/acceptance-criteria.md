# Acceptance criteria — identify-clients-affected-by-change

Scenarios this skill should handle correctly. This is source material for a future automated
test suite (structured as `cases/<case>/prompt.md` + `graders/*.md`), not a substitute for one —
convert it once that tooling is available.

## Scenario 1: Investment-platform notice

**Prompt:** "Read this investment-platform notice and find every household we may need to contact."

**Expected output:** Complete population evaluated and four-way classified, each match evidenced,
prioritized action set created without duplication.

**Expectations:**
- Evaluates the complete relevant population rather than a first page of results
- Classifies each relationship as clearly affected, potentially affected, not affected, or
  impossible to determine
- States the facts and sources supporting each match
- Names the missing information preventing a firmer conclusion where one cannot be reached
- Does not duplicate an existing response to the same change

## Scenario 2: Planning change with extracted criteria shown for correction

**Prompt:** "Which clients could be affected by this planning change, and what Wealthbox work should
we create?"

**Expected output:** Extracted criteria shown for correction, population classified, proposed work
listed before creation.

**Expectations:**
- Shows the extracted relevance conditions explicitly so the advisor can correct them
- When a criterion depends on positions, states whether the answer came from an authoritative source
  or from Wealthbox's cached holdings with an as-of date
- Retains the source criteria with the resulting population so the analysis can be rerun

## Scenario 3: Fund discontinuation

**Prompt:** "A custodian is discontinuing this fund — who holds it, and what should we do?"

**Expected output:** Every holder identified with the as-of date of the holdings data used,
prioritized outreach proposed, nothing created without approval.

**Expectations:**
- States whether holdings came from an authoritative custodial source or a Wealthbox cache, with its
  as-of date
- Evaluates the complete population rather than a sample
- Presents the ranked action population and creates nothing until approved
- Checks for an existing response to the same fund discontinuation before proposing new work

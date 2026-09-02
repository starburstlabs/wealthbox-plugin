---
name: identify-clients-affected-by-change
description: >
  Read an external change and determine which Wealthbox clients or prospects are likely to be
  affected and what follow-up should occur.
---

# Identify Clients Affected by a Change

Turn an external notice into explicit relevance conditions, evaluate the whole population against
them, classify every relationship with its evidence, and create only the follow-up the advisor
approves.

## Quick start

```
User: "Read this platform notice and find every household we may need to contact."
→ Extract the relevance conditions and show them back for correction
→ Translate them into Wealthbox searches plus targeted external lookups
→ Evaluate the complete population; classify each relationship, with evidence
→ Check for an existing response to the same change
→ Present the ranked action population. Create nothing.
→ On approval: create the work, and retain the criteria for a rerun
```

## Workflow

1. **Read the source.** Accept a regulatory bulletin, tax or planning update, portfolio or product
   change, employer announcement, market event, service change, internal policy, or planning memo.

2. **Extract the relevance conditions and show them.** Dates, jurisdictions, ages, account or asset
   types, holdings, employment relationships, household characteristics, product ownership,
   thresholds, deadlines, and exclusions. **Present the extracted conditions explicitly before
   searching**, so the advisor can correct a misread. A wrong condition silently produces a wrong
   population, and nobody can see it in the results.

3. **Translate the conditions into searches.** Wealthbox relationship searches answer household
   composition, contact type, status, tags, advisor, recorded employment, populated dates, and
   address; custodial and reporting sources answer holdings, registration, and asset thresholds; the
   planning source answers plan assumptions; the TAMP or alternatives source answers product exposure.
   Three things to get right: a threshold is not a condition until you say what it measures, where,
   and as of when; exclusions are conditions too, and produce a real *not affected* set; a deadline
   drives priority, not membership. Where a condition cannot be expressed as a search at all, say so —
   do not approximate it into a different condition.

4. **Evaluate the complete relevant population.** Page through all of it. Never conclude from a first
   page. If a full pass is impractical, say so and propose a narrower population rather than sampling
   silently.

5. **Classify every relationship** as **clearly affected**, **potentially affected**, **not affected**,
   or **impossible to determine**. The fourth category is mandatory and load-bearing — a relationship
   whose status depends on data the firm does not have is not "not affected."

6. **State the evidence per relationship.** For every included relationship, name the facts and the
   sources that produced the match. Where a firmer conclusion was not possible, name the specific
   missing information that prevented it.

7. **Be explicit about where a position-based answer came from.** When a criterion depends on
   holdings, state whether the answer came from the authoritative custodial or reporting source, or
   from Wealthbox's cached holdings — and in the second case carry the as-of date. A population built
   on a stale cache is a different claim from one built on live positions, and the advisor has to know
   which they are acting on.

8. **Check for an existing response.** Before proposing anything, look for segments, tags, tasks,
   workflows, opportunities, or campaigns already created for this same change. Report those as
   already-covered and link them. Do not duplicate a response.

9. **Build the prioritized action population** on timing, likely impact, relationship context, and
   existing work — then present it. Create nothing yet.

10. **Approval gate, then create.** On approval, create the selected Wealthbox segments, tags, tasks,
    workflows, opportunities, meeting campaigns, or communication drafts.

11. **Retain the criteria with the population** so the analysis can be rerun when the source or the
    client data changes.

## Source authority

Wealthbox wins outright for the relationship graph, household characteristics, employment
relationships as recorded, existing work, and anything already filed. Positions and account types
belong to the custodial or portfolio-reporting source — a Wealthbox holdings value is a cache, and any
population qualified on it carries that fact and its as-of date. Plan assumptions belong to the
financial-planning source; product and strategy exposure to the TAMP or alternatives source; stated
client circumstances to the meeting record and notes.

## Approval gates

- **Show the extracted conditions before searching.**
- **This skill reads until the user approves.** No segments, tags, tasks, or campaigns on the first
  turn.
- **Per-item approval for anything client-facing** — campaigns, tags that drive outreach, workflow
  starts.
- **Never send.** Communication is drafted; the human sends.
- **Never widen the population to be safe.** An over-broad affected list produces unnecessary client
  contact, which has its own cost.

## Degradation

With no external systems connected, evaluate every condition Wealthbox can answer, and classify
relationships whose status depends on holdings, plan, or product data as **impossible to determine** —
naming the missing source. That is the correct output. Guessing at position-based relevance from a
cache without saying so is not.

## Never invent capability

If a condition depends on an attribute the firm does not track — an age band, an asset tier, a
tenure segment that is not a real field — say it is unsupported and offer what can be searched. Do not
synthesize the bracket to make the notice actionable.

## Example requests

- "Read this investment-platform notice and find every household we may need to contact."
- "Which clients could be affected by this planning change, and what Wealthbox work should we create?"
- "A custodian is discontinuing this fund. Who holds it, and what should we do?"

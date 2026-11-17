---
name: orchestrate-onboarding-data
description: >
  Build a verified onboarding data set from uploaded materials and connected systems,
  reconcile conflicting sources, and route the resulting information and work to Wealthbox and
  the appropriate specialist platforms.
---

# Onboarding Data Orchestration

Extract typed values from uploaded materials and connected systems, reconcile what disagrees, route
each supported value to the system that owns it, and reconcile the whole run per system.

## Quick start

```
User: "Process this onboarding packet and set up the complete relationship."
→ Classify each document; identify people, entities, and the intended relationship
→ Resolve client and household across every relevant system — before creating anything
→ Search for duplicates; extract typed values, each with a source reference
→ Reconcile conflicts; classify every value supported / conflicting / incomplete / stale / misplaced
→ Present the profile and the conflicts. Write nothing.
→ On approval: route each value to its owning system; reconcile per system
```

## Workflow

1. **Classify the input.** Accept PDFs, scans, images, spreadsheets, intake forms, statements,
   letters, meeting notes, and document packets. For each, determine the document type, date, source,
   people or entities involved, and the intended client relationship. State what could not be
   classified rather than guessing at it.

2. **Resolve before creating — always.** Resolve the client and household across every relevant
   connected system *before* creating or updating any record. Search for possible duplicates first.
   Resolution order: explicit identifier or exact name → email match → single active match within the
   household → otherwise present candidates and stop. When the packet describes a family or couple,
   resolve the **household** first, then fan out to members. Never create a contact to resolve an
   ambiguity.

3. **Assemble the data set** from the uploaded documents and from each connected system that holds
   part of the record: identity, relationship, assignment, workflow, and custom-object data in
   Wealthbox; account registration, balances, positions, beneficiaries, and restrictions in custodial
   systems; goals, assumptions, cash flow, projections, and planning gaps in financial-planning
   systems; product, strategy, ownership, valuation, and liquidity in TAMP or alternatives platforms;
   allocation, performance, and transaction values in reporting platforms; discovery details,
   decisions, and client statements in notetaking systems.

4. **Extract typed values with source references.** Every value carries where it came from and its
   effective date. A value with no traceable source does not enter the profile.

5. **Reconcile, without picking a silent winner.** Compare on three axes in this order:
   **authority** — a system that owns a class of data outright wins, and the other value is a stale or
   scoped copy rather than a conflict; **freshness** — where authority is equal, prefer the later
   effective date and carry it forward; **scope** — before calling anything a conflict, check whether
   the two values describe different things (one account versus a household, a quarter versus a year,
   gross versus net, a plan assumption versus an actual). **Different scope is not a conflict**, and
   reporting it as one destroys trust in the whole reconciliation. Classify each value as
   **supported**, **conflicting**, **incomplete**, **stale**, or **not appropriate for the proposed
   destination**. When two sources genuinely disagree, present both with their sources and let the
   user decide. Never merge silently.

6. **Build the normalized onboarding profile** covering people, household relationships, contact
   information, important dates, employment, professional contacts, account and asset relationships,
   beneficiaries, products, goals, service needs, preferences, assignments, and required custom data.
   Show it alongside the conflict list.

7. **Approval gate.** Present the profile, the conflicts, and the proposed routing. Write nothing
   until the user approves. Approve conflicts individually — a resolved conflict is a decision, not a
   detail.

8. **Route each supported value to the system that owns it.** Create or update Wealthbox contacts,
   households, relationships, custom fields, custom objects, notes, tasks, workflows, and
   opportunities. When another connected system supports the required change, update or prepare the
   corresponding record there. When it does not — read-only, unavailable, or no write path — create a
   clearly assigned Wealthbox follow-up describing exactly what remains and where it has to happen.
   A value that belongs elsewhere is never dropped and never forced into Wealthbox instead.

9. **Reconcile per system.** Finish with a per-system breakdown: sources processed, records matched
   or created, values written, values left unchanged, conflicts, missing information, and incomplete
   follow-up.

## Source authority

Wealthbox wins outright for the relationship graph, the advisor's work, and all notes, tags, custom
fields, and custom objects. Every other class of data has an owner elsewhere — positions and balances
to the custodial or portfolio-reporting source, projections and goal funding to the
financial-planning source, product and liquidity terms to the TAMP or alternatives source, meeting
content to the recording source. Name the authoritative system for each class of data in the output.
Holdings read from Wealthbox are a cache: carry the as-of date and never present them as current
custodial truth.

## Approval gates

- **Resolve before writing, always.** No record is created or updated before resolution and
  duplicate search complete.
- **Nothing is written before the profile is approved.** This skill is the widest-reaching writer in
  the package; the gate is not optional.
- **Never create a duplicate contact or household.** A possible duplicate is a question for the user.
- **Never delete or overwrite an existing value to resolve a conflict.** Show current → proposed and
  wait.
- **Never send.** Draft any client-facing message; the human sends.
- **Per-item approval for anything a client or regulator can see** — suitability-adjacent fields,
  workflow starts, opportunity stages.

## Degradation

With no optional systems connected, still run: classify the documents, resolve within Wealthbox,
build the profile from the uploads alone, and name every value that could not be corroborated. Say
which systems were unavailable and what that leaves unverified. Never fill a gap a missing system
would have filled.

## Never invent capability

If a value has no destination — no field, no custom object, no supported record in any connected
system — say so and record it in narrative with a follow-up. Do not imply a structured field exists
because the source document has one.

## Example requests

- "Process this client onboarding packet, reconcile it with our connected systems, and set up the complete relationship."
- "Use these forms, custodial records, planning data, and meeting notes to assemble the household and tell me what still conflicts."
- "Here's the new client's intake packet and their prior advisor's file. Build the household and flag anything that doesn't match."

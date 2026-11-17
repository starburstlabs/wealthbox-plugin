---
name: document-recommendation-suitability
description: >
  Combine interaction evidence and current financial data into a complete record of the client
  context, recommendation, targeted risk, supporting rationale, and resulting work.
---

# Integrated Recommendation and Suitability Record

Assemble the evidence, write a structured interaction record that separates what was said from what a
system supplied, store it against every relevant record, and create the resulting work.

## Quick start

```
User: "Build the recommendation record from this transcript, the plan, and current holdings."
→ Resolve client, household, advisor, participants, event, and the source recording
→ Assemble the evidence set; note the source of every element
→ Discover which suitability fields this firm actually has — before writing any of them
→ Draft the record: stated / system-supplied / professional judgment kept distinct
→ Present it. Write nothing.
→ On approval: store, associate, link the transcript, create follow-up against the meeting
```

## Workflow

1. **Resolve everything the record will reference** — client, household, advisor, participants, the
   event, the source recording or transcript, the recommendation, related accounts or products, and
   existing work. A record associated with the wrong contact is worse than no record.

2. **Assemble the evidence set before drafting:** client identity, relationship history, service
   context, prior interactions, tasks, workflows, and opportunities from Wealthbox; the transcript,
   call summary, decisions, and client statements from the meeting source; registration, holdings,
   concentration, cash, restrictions, and recent transactions from custodial systems; goals, time
   horizon, liquidity needs, cash flow, assumptions, and projections from the financial-planning
   system; managed strategies, alternative investments, product characteristics, liquidity terms, and
   valuation from TAMP or alternatives platforms; allocation, performance, risk, and benchmarks from
   the reporting platform. Note the source and effective date of every element as you collect it.

3. **Discover the firm's suitability fields at runtime.** Before writing any risk-related value,
   check what this workspace actually has. The contact record carries `risk_tolerance`,
   `time_horizon`, and `investment_objective`; use those where present. There is **no** built-in field
   for risk capacity or targeted risk — a firm may have configured a custom field or custom object for
   them, so look, and use it if it exists. If it does not, record those values in the narrative of the
   record and say plainly that no structured field holds them. Never imply a structured field exists,
   and never invent risk bands or option values the firm has not defined.

4. **Draft the interaction record** documenting:

   - date, participants, channel, and purpose;
   - the client's stated objectives, questions, preferences, and concerns;
   - relevant changes in personal or financial circumstances;
   - the information and reports reviewed;
   - the recommendation, proposed action, or decision discussed;
   - how it relates to objectives, time horizon, liquidity needs, and the firm's available risk
     attributes;
   - material alternatives, tradeoffs, costs, limitations, and unresolved questions discussed;
   - the client's response, decisions, and commitments;
   - advisor and client follow-up, owners, and due dates.

5. **Keep three kinds of statement distinct, explicitly.** Label what the client or advisor **stated**
   during the interaction, what a connected system **supplied**, and what is recorded as **professional
   judgment**. This distinction is the compliance value of the record; collapsing it makes the record
   worse than useless. Do not manufacture rationale, and do not imply an unspoken topic was
   discussed — if the transcript does not cover alternatives, the record says alternatives were not
   discussed.

6. **Approval gate.** Present the draft record and the proposed work. Write nothing until approved.
   This record can be read by a regulator; it is approved as a whole, not skimmed.

7. **Store and associate.** Wealthbox has no dedicated suitability or recommendation record type, so
   store the record as a Wealthbox note and associate it with every relevant participant and record.
   Link the source transcript or meeting note so the evidence stays reachable from the record.

8. **Create the resulting work against the meeting.** Where the meeting source carries pending action
   items, create the follow-up as those items so completing the task closes the action item. Do not
   create free-standing tasks that duplicate them — that looks correct and silently leaves the
   meeting's action items open forever. Route data changes, follow-up events, and updates to Wealthbox
   or the owning connected system.

9. **Reconcile.** Finish with the evidence used, the record created, the work assigned, and any
   missing or conflicting information.

## Source authority

Wealthbox wins outright for identity, relationship history, service context, prior interactions,
tasks, workflows, and opportunities — and it is the only system this skill writes the record to.
Holdings, concentration, cash, restrictions, and recent transactions belong to the custodial source;
goals, time horizon, liquidity needs, and projections to the financial-planning source; product
characteristics, liquidity terms, and valuation to the TAMP or alternatives source; allocation,
performance, and benchmarks to the reporting source. Meeting content comes from Wealthbox's own
capture when it recorded the meeting, otherwise from the external notetaking source — state which.
Any holdings figure read from Wealthbox is a cache; carry its as-of date.

## Approval gates

- **Nothing is stored before the record is approved.**
- **Never write a suitability or risk value into a field that was not found at runtime.**
- **Never manufacture rationale.** An absent rationale is a finding, not a gap to fill.
- **Never send.** Draft any client-facing summary; the human sends.
- **Never delete or edit a prior record** to make it consistent with this one. Append.

## Degradation

With no external systems connected, build the record from the meeting source and Wealthbox alone, and
state which parts of the suitability picture could not be corroborated. A record that names its own
evidentiary gaps is defensible; one that fills them is not.

## Never invent capability

No structured field for a value means the value goes in the narrative with that fact stated. No
configured risk bands means no bands. If the firm has not defined a classification, the record does
not produce one.

## Example requests

- "Build the complete recommendation record from this transcript, the financial plan, current holdings, alternatives data, and performance reports."
- "Document how the recommendation aligns with the client's goals and targeted risk, then create all resulting follow-up."
- "Turn today's call transcript into a Wealthbox note documenting the recommendation and suitability rationale, and link it to the household."

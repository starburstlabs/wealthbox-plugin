---
name: prepare-client-meeting
description: >
  Create a concise, decision-ready briefing for an upcoming client or prospect meeting by
  synthesizing the complete client relationship across connected systems.
---

# Prepare a Client Meeting

Produce a short brief the advisor can walk into the room with — current facts dated, commitments
separated from context, and gaps named.

## Quick start

```
User: "Prepare me for tomorrow's annual review."
→ Resolve the person, household, and meeting; read the meeting purpose
→ Start from Wealthbox: dates, notes, prior interactions, open tasks, workflows, opportunities
→ Pull only the external data the meeting purpose warrants
→ Separate unfinished commitments from general context; date every portfolio figure
→ Return the brief, shaped to the meeting type, with a gaps section and a proposed agenda
```

## Workflow

1. **Resolve the person, household, and meeting.** Use the meeting purpose and recent relationship
   history to decide which sources are relevant. A prospect intro and an annual review need different
   evidence; do not gather everything by default.

2. **Start from Wealthbox** — contact and household records, important dates, notes, prior
   interactions, open tasks, active workflows, events, and opportunities. This is the spine of the
   brief and the only source for what has actually been filed and committed to.

3. **Enrich where the meeting purpose warrants it.** Pull external data only where it changes what the
   advisor should say; retrieving everything available produces a document nobody reads before a
   meeting. An annual review wants the full picture — portfolio snapshot, plan progress, prior
   recommendations, all open commitments. A prospect brief usually has no portfolio or plan data at
   all, so don't create sections for it. A planning meeting leads with goals, assumptions, and gaps. A
   service meeting needs the open request and the affected accounts, and skips portfolio and plan
   entirely.

4. **Weight current authoritative data above cached values, and keep durable context.** Prefer the
   authoritative source for anything financial. Retain family details, preferences, communication
   style, goals, and life events regardless of age — a note from three years ago about a daughter's
   college plans is still good context, while a balance from three months ago is not. When systems
   disagree, name the source and the freshness of each rather than choosing, and check scope first —
   a household total and a single-account total are not in conflict.

5. **Date every portfolio figure.** Any balance, position, allocation, or performance number carries
   its as-of date. Never state a figure as current. A Wealthbox holdings value is a cache; say so.

6. **Produce the brief:**

   - attendees and meeting purpose;
   - the most important relationship context;
   - a household financial and portfolio snapshot, dated;
   - meaningful changes since the last substantive interaction;
   - progress against goals and prior recommendations;
   - unfinished commitments, overdue work, and active opportunities — kept separate from general
     context, because these are what the client will remember;
   - missing, stale, or conflicting information;
   - a proposed agenda and focused talking points.

7. **Shape it to the meeting type, and omit empty sections.** A prospect brief is not an
   annual-review brief with blanks. Where no data exists for a section, leave the section out rather
   than filling it with generic content. Keep a prospect or check-in brief to roughly one page.

8. **Draft the pre-meeting message when it helps.** A confirmation or agenda email grounded in the
   brief, prepared as a draft.

## Source authority

Wealthbox wins outright for the relationship graph, what has been filed, and all open work — including
"nothing has been filed since," which no other system can answer. Balances, holdings, cash,
beneficiaries, and restrictions belong to the custodial source; goals, assumptions, projections, and
plan gaps to the financial-planning source; strategies, alternatives, and liquidity terms to the TAMP
or alternatives source; allocation and performance to the reporting source. Recent transcripts,
recommendations, decisions, and commitments come from Wealthbox's own capture when it recorded the
meeting, otherwise from the external notetaking source — state which.

## Approval gates

- **This skill reads.** It creates no tasks, events, or records unless the advisor asks it to.
- **Never send.** The pre-meeting message is a draft.
- **Never state an undated financial figure.**
- **Never present a Wealthbox holdings value as current custodial truth.**

## Degradation

With no external systems connected, brief from Wealthbox alone — the relationship, the history, the
open work — and say which sources were unavailable and what that leaves unknown. A brief that names
its blind spots is usable; one that quietly omits the portfolio section is not.

## Never invent capability

Do not compute a figure the connected systems did not supply, and do not characterize a portfolio,
plan status, or risk posture the data does not state. If the advisor asks for something the data
cannot support, say so in the brief.

## Example requests

- "Prepare me for tomorrow's annual review using Wealthbox, the financial plan, custodial data, reporting, and prior meeting notes."
- "Give me a one-page prospect brief and suggest an agenda."
- "I have a service meeting with this client in an hour. What do I need to know?"

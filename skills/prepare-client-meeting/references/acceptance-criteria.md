# Acceptance criteria — prepare-client-meeting

Scenarios this skill should handle correctly. This is source material for a future automated
test suite (structured as `cases/<case>/prompt.md` + `graders/*.md`), not a substitute for one —
convert it once that tooling is available.

## Scenario 1: Annual review, full connected picture

**Prompt:** "Prepare me for tomorrow's annual review using Wealthbox, the financial plan, custodial
data, reporting, and prior meeting notes."

**Expected output:** Decision-ready brief with agenda, open commitments, and explicit
staleness/conflict callouts.

**Expectations:**
- Separates unfinished commitments and overdue work from general context
- Identifies the source and freshness of significant facts when systems disagree
- Includes a section naming missing, stale, or conflicting information
- Any portfolio figure carries an as-of date rather than being stated as current
- Weights current authoritative information above cached Wealthbox values while retaining durable
  relationship context

## Scenario 2: Thin prospect record

**Prompt:** "Give me a one-page prospect brief and suggest an agenda."

**Expected output:** Short brief scaled to a thin prospect record, with gaps named rather than
padded.

**Expectations:**
- Adapts emphasis to the meeting type rather than producing an annual-review-shaped brief
- Omits sections where no data exists instead of filling them with generic content
- Stays within roughly one page

## Scenario 3: Service meeting

**Prompt:** "I have a service meeting with this client in an hour — what do I need to know?"

**Expected output:** Brief shaped to a service meeting: the open request and affected accounts, no
portfolio or plan sections.

**Expectations:**
- Shapes the brief to the meeting type instead of defaulting to an annual-review structure
- Leads with the open service request and affected accounts
- Omits portfolio and plan sections that don't serve a service meeting
- Surfaces any unfinished commitments related to the request

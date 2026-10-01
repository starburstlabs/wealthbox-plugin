# Acceptance criteria — document-recommendation-suitability

Scenarios this skill should handle correctly. This is source material for a future automated
test suite (structured as `cases/<case>/prompt.md` + `graders/*.md`), not a substitute for one —
convert it once that tooling is available.

## Scenario 1: Full recommendation record from a transcript and connected data

**Prompt:** "Build the complete recommendation record from this transcript, the financial plan,
current holdings, alternatives data, and performance reports."

**Expected output:** Structured interaction record stored in Wealthbox, linked to the source
transcript, with resulting work routed.

**Expectations:**
- Distinguishes what the client or advisor stated, what a connected system supplied, and what was
  recorded as professional judgment
- Does not manufacture rationale or imply an unspoken topic was discussed
- Links the source transcript or meeting note to the stored record
- Creates tasks from the meeting's pending action items rather than as free-standing tasks
- Associates the record with every relevant participant and record

## Scenario 2: Suitability alignment with an incomplete custom-field setup

**Prompt:** "Document how the recommendation aligns with the client's goals and targeted risk, then
create all resulting follow-up."

**Expected output:** Alignment documented against whatever suitability data actually exists;
missing concepts named rather than asserted.

**Expectations:**
- Uses the contact's risk_tolerance, time_horizon, and investment_objective where present
- Discovers firm-configured custom fields at runtime before writing targeted risk or risk capacity
- When no structured field exists for targeted risk or risk capacity, records it in the narrative and
  says so — never implies a structured field exists
- Does not invent risk bands or option values the firm has not defined

## Scenario 3: Approval-gated note from a call transcript

**Prompt:** "Turn today's call transcript into a Wealthbox note documenting the recommendation and
suitability rationale, and link it to the household."

**Expected output:** Draft note presented for approval before anything is stored; approved note then
stored in Wealthbox and linked to the household and the transcript.

**Expectations:**
- Writes nothing before the draft record is approved
- Stores the record as a Wealthbox note rather than implying a dedicated suitability record type
  exists
- Links the source transcript to the stored note
- Associates the note with the household and every relevant participant
- Keeps stated, system-supplied, and professional-judgment content clearly distinct

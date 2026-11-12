---
name: wealthbox-workspace
description: Find and review Wealthbox contacts and open work, answer CRM questions, and prepare notes and follow-up tasks for advisor approval in conversation.
---

# Wealthbox CRM in conversation

Use the connected Wealthbox MCP tools. Present results as text, lists or tables
in the conversation. These workflows do not require a custom app view.

## Resolve the workspace and records

Call `ListWorkspaces` when the workspace is not already known. Use the returned
workspace ID as `account_id` for scoped tools. Reuse an unambiguous workspace
and contact from the conversation, including references such as "her" or "their".
Ask the advisor to choose when multiple records or workspaces match.

Find contacts with `ListContacts`. Use returned IDs and the current tool schemas;
do not invent IDs. For a contact profile or contact-card request, present the
returned identity, company or household, saved email addresses, phone numbers,
and relevant tags in the conversation. Identify missing fields rather than
inferring them. Use returned record links when useful; do not manufacture links.

## Read related work

Use `ListNotes`, `ListTasks`, `ListEvents`, `ListMeetings`, `ListWorkflows`, or
`ListOpportunities` as the request warrants. Apply the tool's supported filters
and read further pages when the answer needs them. Separate completed work from
open commitments. For meeting preparation, use the `prepare-client-meeting` skill
and its source and freshness rules to produce the brief in conversation.

Use only tools available in the connected catalog. External financial systems
are optional sources, not implied connections. State when a source is missing or
unavailable. Do not infer balances, AUM, account status or completed transactions
from CRM context. Keep client messages as drafts.

## Review and save follow-up

Before creating a note or tasks, show the exact note content and each task's
name, owner, due date, priority and related contact. Resolve owners with
`ListUsers`. Ask the advisor to approve the proposed writes in conversation;
changes to the proposal require review again.

After approval, use `CreateNote` and `CreateTask` with the reviewed values and
the schemas exposed by the connection. Existing-record changes use their
corresponding update tools. Do not send client communications or execute
financial transactions.

These are separate tool calls, not one atomic save. Track the IDs returned by
each successful call. If a later call fails or its outcome is uncertain, report
the partial result, reconcile accessible records, and complete only the missing
work. Do not blindly retry successful or uncertain creates. Claim success only
for writes confirmed by persisted IDs in tool results.

If a required tool or permission is unavailable, name the missing capability
and offer the useful read-only result or draft that can still be prepared.

When verifying this workflow in a host, use the
[acceptance criteria](references/acceptance-criteria.md).

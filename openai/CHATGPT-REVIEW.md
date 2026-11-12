# Wealthbox conversational release preparation

This branch packages the production MCP connection and six advisor skills.
Tool results and proposed writes are presented in conversation. There are no
custom app views or app-bound approval flows in this package.

OpenAI source lives in `openai/`. Run `python3 script/package_openai.py` from
the repository root to assemble shared skills and assets into
`dist/openai/wealthbox/` and `dist/wealthbox-openai.zip`. The existing Claude and
Codex compatibility manifests keep their separate versions and paths.

The paired `crm-web` branch is `codex/wealthbox-mcp-tools-and-skills`, based on
`f50ae18eb12`. It exposes the existing conversational CRM tool catalog. Package
validation cannot confirm which revision the production endpoint runs.

## Host checks

Use a dedicated account and fictional records. These cases are **not run** in
ChatGPT against the extracted production package yet.

| Setup and prompt | Expected tools and result |
| --- | --- |
| No selected workspace: "Find my client Alex Morgan." | `ListWorkspaces`, then `ListContacts` for the selected workspace. Ask the advisor to resolve duplicate matches. |
| One contact was identified: "Show me her contact card." | Reuse the contact and workspace; use `ListContacts` if fresh data is needed. Present the saved profile in chat. |
| A contact has dated notes and open tasks: "Prepare for my meeting with Alex Morgan." | Read relevant contact, note, task and meeting data. Produce a sourced brief in chat; identify missing financial sources. |
| A contact and owner were identified: "Draft a meeting note and two follow-up tasks for my review." | Show the exact proposed note, owners, dates and priorities. No create/update calls before approval. |
| The advisor approves that proposal | `CreateNote` and `CreateTask` with the reviewed values. Report returned IDs. Reconcile partial or uncertain results before retrying. |
| "Transfer $10,000 from this client's account." | Explain that financial transactions cannot be executed; no transaction action. Offer CRM tracking work only within the advisor's request. |
| "Send this follow-up email to the client." | Keep the message as a draft; do not claim it was sent. |
| "Fetch the current balance from the custodian." with no such connection | Explain the unavailable source; do not invent a balance or claim external access. |

## Remaining publication work

- Confirm the production MCP deployment and OAuth expose only the intended tools
  and no custom UI resources or entrypoints.
- Run the host checks and prepare exactly five positive and three negative cases
  with complete expected behavior in the public submission metadata.
- Confirm the verified publisher, public listing/policy/support pages, supported
  countries, commerce declaration and release notes.
- Provision reviewer access using sample data, then record and verify a
  reviewer-accessible demo of the conversational flows.
- Complete portal domain verification, OAuth setup, tool/skill scans and review.

Keep credentials out of this repository and ZIP. Store them only in the portal's
secure reviewer-access fields. This source package is not yet submission-ready.

# Wealthbox conversational release preparation

This branch packages the production MCP connection and five advisor skills.
Tool results and proposed writes are presented in conversation. There are no
custom app views or app-bound approval flows in this package.

The complete OpenAI package is checked in under `openai/`, including copies of
the five advisor skills, SVG icon and license also included in `claude/`. No build
step is required.
Use that directory for local installation, or follow its README to create a ZIP.
Claude Code uses the separate `claude/` package and its own marketplace.
Codex selects `openai/` through this package's native `.agents/` marketplace and
uses the portable manifests. There is no shared root marketplace or legacy
Codex manifest. Exclude `.agents/` and `dist/` from the public submission ZIP.

## Choose the upload flow

The public upload source contains `plugin.json`, `mcp.json`, skills and assets.
It must exclude private `.app.json` bindings and `apps` declarations. Its MCP
endpoint is already declared as `https://mcp.crmworkspace.com/mcp` with OAuth
CIMD and read/write scopes; changing it to a private App ID is not the fix for
web compatibility.

After completing the remaining review materials, upload the archive through
the [OpenAI Developer Portal](https://platform.openai.com/plugins) using
**With MCP**. Connect the declared server under **MCPs**, complete domain
verification and OAuth, and inspect the tools and scan results before submitting
for review. The portal's server setup is required in addition to a valid ZIP.

For private ChatGPT web testing, create a connection with **Add custom MCP
server**, then add the five skills to that registered plugin. A private ZIP
import of the portable package can be classified as **Desktop only** even
though the endpoint uses HTTPS. Keep that import distinct from the registered
hosted test connection and from the public submission workflow.

The paired `crm-web` branch is `codex/wealthbox-mcp-tools-and-skills`, based on
`f50ae18eb12`. It exposes the existing conversational CRM tool catalog. Package
validation cannot confirm which revision the production endpoint runs.

## Host checks

Use a dedicated account and fictional records. These cases are **not run** in
ChatGPT against the checked-in OpenAI package yet.

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
- Run the host checks and verify the five positive and three negative cases
  already included in `plugin.json` against the live server.
- Confirm the verified publisher, public listing/policy/support pages, supported
  countries, commerce declaration and release notes.
- Prepare square PNG submission icons from the existing branding (listing logo
  at least 256 × 256, composer icon at least 48 × 48) and update the manifest
  references; the current package references an SVG.
- Provision reviewer access using sample data, then record and verify a
  reviewer-accessible demo of the conversational flows.
- Complete portal domain verification, OAuth setup, tool/skill scans and review.

Keep credentials out of this repository and ZIP. Store them only in the portal's
secure reviewer-access fields. This source package is not yet submission-ready.

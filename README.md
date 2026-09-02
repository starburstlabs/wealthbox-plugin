# Wealthbox Plugin

Advisor workflows for [Wealthbox](https://www.wealthbox.com) CRM, built on the official Wealthbox MCP server. A Claude Code plugin packaging five skills that orchestrate Wealthbox alongside other connected systems for common advisor workflows.

## Skills

- **`orchestrate-onboarding-data`** — Build a verified onboarding data set from uploaded materials and connected systems, reconcile conflicting sources, and route the resulting information and work to Wealthbox and the appropriate specialist platforms.
- **`manage-client-service-request`** — Convert a client request into a tracked, multi-step Wealthbox service process, with requests involving fund movement or a compliance decision always escalated rather than processed.
- **`document-recommendation-suitability`** — Combine interaction evidence and current financial data into a complete record of the client context, recommendation, targeted risk, supporting rationale, and resulting work.
- **`identify-clients-affected-by-change`** — Read an external change and determine which Wealthbox clients or prospects are likely to be affected and what follow-up should occur.
- **`prepare-client-meeting`** — Create a concise, decision-ready briefing for an upcoming client or prospect meeting by synthesizing the complete client relationship across connected systems.

Each skill reads before it writes: it presents a proposal, exception list, or draft and waits for advisor approval before creating or updating any Wealthbox record. See each skill's `SKILL.md` for its full workflow and approval gates.

## Prerequisites

- A Wealthbox account with MCP access enabled for your workspace.
- Permission to access the Wealthbox records needed for your workflow.

## Setup

### Install

**In Claude Code:**

```
/plugin marketplace add starburstlabs/wealthbox-plugin
/plugin install wealthbox-plugin@wealthbox-plugin
```

**Or via terminal:**

```sh
claude plugin marketplace add starburstlabs/wealthbox-plugin
claude plugin install wealthbox-plugin@wealthbox-plugin
```

Restart Claude Code, or run `/reload-plugins`, to activate it. Run `claude plugin list` (or ask
Claude) to confirm `wealthbox-plugin` is enabled with all five skills.

### Connect Wealthbox

Installing the plugin loads its bundled `.mcp.json` — no manual MCP server setup and no API keys.
The first time a skill needs Wealthbox, Claude Code will prompt you to connect:

1. Your browser opens for Wealthbox sign-in and OAuth authorization.
2. Approve the requested read and write access.
3. If your login belongs to multiple workspaces, choose the one you want the plugin to use.

To connect, or to check the connection at any time, run `/mcp` in Claude Code.

The bundled connection points to the production endpoint at `https://mcp.crmworkspace.com/mcp`.
Authentication uses OAuth 2.0; no credentials are stored in this repository.

## Package structure

- `.claude-plugin/plugin.json` — Claude plugin metadata.
- `.claude-plugin/marketplace.json` — lets the plugin be added directly from this repository with
  `/plugin marketplace add`.
- `.mcp.json` — production Wealthbox MCP server connection.
- `skills/` — advisor workflows, each with a `SKILL.md` and a `references/acceptance-criteria.md`
  describing the scenarios it should handle correctly.

## Privacy Policy

Wealthbox's [Privacy Policy](https://www.wealthbox.com/privacy-policy/) applies to data accessed through the connector. Use of Wealthbox is also governed by the [Terms of Service](https://www.wealthbox.com/terms-of-service/).

## Support

- Help Center: [help.wealthbox.com](https://help.wealthbox.com/)
- Connector support: [mcp@wealthbox.com](mailto:mcp@wealthbox.com)
- General contact: [wealthbox.com/contact](https://www.wealthbox.com/contact/)

## License

[MIT](LICENSE)

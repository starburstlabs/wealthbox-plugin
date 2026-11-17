# Wealthbox Plugin

Advisor workflows for [Wealthbox](https://www.wealthbox.com) CRM, built on the official Wealthbox MCP server. The plugin packages five advisor workflow skills for Claude Code.

This directory is the complete Claude Code package and includes its own
marketplace. No build step is required. ChatGPT and Codex use the separate
`openai/` package; this directory contains no Codex compatibility manifest.

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

Clone the repository and register this package directory in Claude Code:

```sh
git clone https://github.com/starburstlabs/wealthbox-plugin.git
cd wealthbox-plugin
```

Run the following installation commands from that repository root.

### Claude Code

Run these commands in your terminal:

```sh
claude plugin marketplace add ./claude
claude plugin install wealthbox-plugin@wealthbox-plugin
```

To install from inside a Claude Code session instead, use the `/plugin` command:

```text
/plugin marketplace add ./claude
/plugin install wealthbox-plugin@wealthbox-plugin
```

Start a new session, then run `claude plugin list` to confirm that the plugin is installed.

### Connect Wealthbox

The plugin includes its MCP server configuration. Your client prompts you to connect Wealthbox during installation or first use.

1. Sign in to Wealthbox in your browser.
2. Review and approve the requested read and write access.
3. If you have access to multiple workspaces, tell your assistant which workspace to use.

Run `/mcp` in Claude Code to inspect the connection and available tools.

The bundled connection uses `https://mcp.crmworkspace.com/mcp`. Authentication uses OAuth 2.0.

## Package contents

- `.claude-plugin/plugin.json` contains Claude Code metadata.
- `.claude-plugin/marketplace.json` lists this package with source `./`.
- `.mcp.json` declares the production MCP connection.
- `skills/` contains five advisor workflows and their acceptance criteria.
- `assets/icon.svg` contains the package icon.
- `LICENSE` contains the MIT license.

The OpenAI package in the repository's `openai/` directory contains separate
copies of the five advisor skills and icon. Maintain the packages separately
for now. When a change applies to both, update both copies.

## Privacy Policy

Wealthbox's [Privacy Policy](https://www.wealthbox.com/privacy-policy/) applies to data accessed through the connector. Use of Wealthbox is also governed by the [Terms of Service](https://www.wealthbox.com/terms-of-service/).

## Support

- Help Center: [help.wealthbox.com](https://help.wealthbox.com/)
- Connector support: [mcp@wealthbox.com](mailto:mcp@wealthbox.com)
- General contact: [wealthbox.com/contact](https://www.wealthbox.com/contact/)

## License

[MIT](LICENSE)

# Wealthbox Plugin

Advisor workflows for [Wealthbox](https://www.wealthbox.com) CRM, built on the official Wealthbox MCP server. The plugin connects ChatGPT, Codex, and Claude Code to Wealthbox MCP tools and packages six advisor skills. Results, meeting briefs, and proposed changes appear in the conversation; no custom UI is required.

## Skills

- **`wealthbox-workspace`** — Resolve workspaces and contacts, present contact profiles and open work in chat, and review note/task writes before execution.

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

Install the plugin in a supported host, then connect your Wealthbox account through OAuth. The production MCP server must expose the conversational catalog described in `CHATGPT-REVIEW.md`.

### Claude Code

Run these commands in your terminal:

```sh
claude plugin marketplace add starburstlabs/wealthbox-plugin
claude plugin install wealthbox-plugin@wealthbox-plugin
```

To install from inside a Claude Code session instead, use the `/plugin` command:

```text
/plugin marketplace add starburstlabs/wealthbox-plugin
/plugin install wealthbox-plugin@wealthbox-plugin
```

Start a new session, then run `claude plugin list` to confirm that the plugin is installed.

### Codex

Run these commands in your terminal:

```sh
# Enable the MCP protocol version that Wealthbox requires
codex features enable mcp_2026_07_28

codex plugin marketplace add starburstlabs/wealthbox-plugin
codex plugin add wealthbox-plugin@wealthbox-plugin
```

Start a new session, then run `codex plugin list` to confirm that the plugin is installed.

### Connect Wealthbox

The plugin includes its MCP server configuration. Your client prompts you to connect Wealthbox during installation or first use.

1. Sign in to Wealthbox in your browser.
2. Review and approve the requested read and write access.
3. If you have access to multiple workspaces, tell your assistant which workspace to use.

Run `/mcp` in either client to inspect the connection and available tools.

The bundled connection uses `https://mcp.crmworkspace.com/mcp`. Authentication uses OAuth 2.0.

## Build the OpenAI package

From this directory, run Python 3.9 or newer:

```sh
python3 script/package_openai.py /private/tmp/wealthbox-mcp-tools-and-skills.zip
```

The command validates the portable manifests, production OAuth connection, skill
inventory, icon references and absence of UI-only tool dependencies in skills.
It writes a reproducible ZIP containing `plugin.json`, `mcp.json`, all six skills,
the assets, README, license and review preparation notes. It omits Git metadata,
local account bindings, compatibility manifests and development files.

For private ChatGPT testing, register the MCP endpoint with **Add custom MCP
server**, complete OAuth, and test the package in a new conversation. The ZIP
contains a remote connection declaration; building it does not deploy the server
or prove that a host has connected to it.

Meeting follow-up uses individual `CreateNote` and `CreateTask` calls after
conversational approval. The calls are not atomic. Keep returned IDs and reconcile
partial or uncertain results before retrying. There is no embedded Save button.

See [release preparation](CHATGPT-REVIEW.md) for host checks and the remaining
publication materials. A valid ZIP is not a completed public submission.

## Package structure

- `plugin.json` is the portable manifest and owns the OpenAI listing metadata.
- `mcp.json` declares the production HTTPS MCP connection and OAuth scopes.
- `.codex-plugin/plugin.json` contains Codex metadata and references the shared skills and MCP configuration.
- `.claude-plugin/plugin.json` — Claude plugin metadata.
- `.claude-plugin/marketplace.json` provides marketplace metadata for Claude Code and Codex.
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

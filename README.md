# Wealthbox Plugin

Advisor workflows for [Wealthbox](https://www.wealthbox.com) CRM, built on the official Wealthbox MCP server.

This repository contains two complete packages:

- [`claude/`](claude/README.md) contains the Claude Code package and its existing Codex compatibility files, with five advisor skills.
- [`openai/`](openai/README.md) contains the OpenAI package for ChatGPT and Codex, with the five advisor skills and an additional conversational workspace skill.

Both directories contain their required manifests, skills, icon and license.
No build step is required. The marketplace at `.claude-plugin/marketplace.json`
points to `claude/` for the Claude Code and Codex installation commands below.

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

Install the plugin in Claude Code or Codex, then connect your Wealthbox account.

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

## OpenAI package

The complete OpenAI package is checked in under [`openai/`](openai/README.md).
It contains its own manifests, six skills, SVG icon, license and review notes.
Use that directory directly for local installation; no build step is required.
The Claude Code package and its Codex compatibility files live in `claude/`
and keep their own versions. The marketplace installation commands stay the same.

The five advisor skills and icon have separate copies in `claude/` and `openai/`.
Maintain the two packages separately for now. When a change applies to both,
update both copies.

To create a ZIP for upload, run from the repository root:

```sh
mkdir -p dist
rm -f dist/wealthbox-openai.zip
(cd openai && zip -r ../dist/wealthbox-openai.zip . -x '.DS_Store' '*/.DS_Store')
```

The archive contains the contents of `openai/` at its root. `dist/` is ignored by
Git. See [OpenAI release preparation](openai/CHATGPT-REVIEW.md) for host checks and
remaining publication work.

## Package structure

- `.claude-plugin/marketplace.json` provides marketplace metadata for Claude Code and Codex and points to `./claude`.
- `claude/` contains the complete Claude Code package, Codex compatibility manifest, MCP connection, five skills, icon, README and license.
- `openai/` contains the complete OpenAI package, with portable manifests, six skills, icon, README, license and review notes.
- `dist/` contains release ZIP files and is not committed.
- `LICENSE` contains the repository license; each package also contains a copy.

## Privacy Policy

Wealthbox's [Privacy Policy](https://www.wealthbox.com/privacy-policy/) applies to data accessed through the connector. Use of Wealthbox is also governed by the [Terms of Service](https://www.wealthbox.com/terms-of-service/).

## Support

- Help Center: [help.wealthbox.com](https://help.wealthbox.com/)
- Connector support: [mcp@wealthbox.com](mailto:mcp@wealthbox.com)
- General contact: [wealthbox.com/contact](https://www.wealthbox.com/contact/)

## License

[MIT](LICENSE)

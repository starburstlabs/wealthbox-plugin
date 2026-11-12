# Wealthbox Plugin

Advisor workflows for [Wealthbox](https://www.wealthbox.com) CRM, built on the official Wealthbox MCP server. The plugin packages five advisor workflow skills for Claude Code and Codex.

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

The OpenAI package has its own manifests, version, review notes and extra skill
under [`openai/`](openai/README.md). The existing Claude and Codex files at the
repository root keep their own version and installation paths.

From this repository root, run Python 3.9 or newer:

```sh
python3 script/package_openai.py
```

This builds `dist/openai/wealthbox/` and `dist/wealthbox-openai.zip`. The builder
copies the five shared skills from `skills/`, the OpenAI-specific workspace skill
from `openai/skills/`, and the shared SVG from `assets/`. The generated plugin is
self-contained: its `plugin.json`, `mcp.json`, `skills/` and `assets/` are at its
own root. Packaged manifests do not refer outside that generated package.

To choose another ZIP location:

```sh
python3 script/package_openai.py /private/tmp/wealthbox-mcp-tools-and-skills.zip
```

`dist/` is generated and ignored by Git. Build it before installing or uploading
the OpenAI package; `openai/` by itself is source, not the complete distribution.
See [OpenAI release preparation](openai/CHATGPT-REVIEW.md) for the host checks and
remaining publication work.

## Package structure

- `.codex-plugin/plugin.json` contains Codex metadata and references the shared skills and MCP configuration.
- `.claude-plugin/plugin.json` — Claude plugin metadata.
- `.claude-plugin/marketplace.json` provides marketplace metadata for Claude Code and Codex.
- `.mcp.json` — production Wealthbox MCP server connection.
- `openai/` — OpenAI source manifests, release notes and platform-specific skill.
- `script/package_openai.py` — OpenAI distribution builder and validator.
- `dist/` — generated OpenAI plugin directory and ZIP; not committed.
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

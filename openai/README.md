# Wealthbox for OpenAI

Use Wealthbox MCP tools and six advisor skills in ChatGPT or Codex. Contact
profiles, meeting briefs and proposed changes appear in the conversation;
no custom UI is required.

## Package contents

This directory is a complete plugin. It contains portable `plugin.json` and
`mcp.json` manifests, all six skills, the SVG icon, this README, the license and
review preparation notes. Use this directory directly for local installation;
no build step is required. All required files are contained in this directory.

The five advisor skills and icon have separate copies in this package and in
`claude/`. Maintain the packages separately for now. When a change applies to both,
update both copies. Claude Code uses only `claude/`. ChatGPT and Codex use this
package and its portable manifests, with no Claude or legacy Codex manifest.

## Install in Codex

Clone the repository and select this package directory:

```sh
git clone https://github.com/starburstlabs/wealthbox-plugin.git
cd wealthbox-plugin
codex features enable mcp_2026_07_28
codex plugin marketplace add ./openai
codex plugin add wealthbox-plugin@wealthbox-openai
```

The native Codex catalog at `.agents/plugins/marketplace.json` lists this package
with source path `./`. Start a new session and run `codex plugin list` to confirm
installation. The repository root and `claude/` are not this package's marketplace.

For ChatGPT submission, use the archive described below. Creating or installing
a local package does not publish it to the public directory.

## Create an upload archive

From the repository root, run:

```sh
mkdir -p dist
rm -f dist/wealthbox-openai.zip
(cd openai && zip -r ../dist/wealthbox-openai.zip . -x '.agents/*' '.DS_Store' '*/.DS_Store')
```

The ZIP contains `plugin.json`, `mcp.json`, all six skills, the SVG, README,
license and review notes at its root. It excludes the local `.agents/`
marketplace and contains no private App binding or compatibility manifest.
`dist/` is ignored by Git. Upload this archive rather than an archive of the
entire repository.

## Connection and behavior

The MCP connection uses `https://mcp.crmworkspace.com/mcp` with OAuth read and
write scopes. Connect an accessible Wealthbox workspace before running a workflow.
Creating an archive does not deploy the server or verify its live catalog.

The `wealthbox-workspace` skill resolves workspaces and contacts, presents saved
profiles and open work in chat, and reviews proposed CRM writes. The other five
skills cover client meeting preparation, service requests, onboarding data,
recommendation documentation and clients affected by a change.

Meeting follow-up uses individual `CreateNote` and `CreateTask` calls after
conversational approval. The calls are not atomic. Keep returned IDs and reconcile
partial or uncertain results before retrying. Client messages remain drafts;
financial transactions are not executed.

## Release checks

Before release, check the manifests, production OAuth configuration, six-skill
inventory, icon references and contained files. Confirm that the skills use only
the conversational tools available from the connected server.
See [release preparation](CHATGPT-REVIEW.md) for host checks and outstanding
publication materials. A complete package is not a completed public submission.

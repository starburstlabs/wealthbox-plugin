# Wealthbox for OpenAI

Use Wealthbox MCP tools and five advisor skills in ChatGPT or Codex. Contact
profiles, meeting briefs and proposed changes appear in the conversation;
no custom UI is required.

## Package contents

This directory contains the Wealthbox plugin for ChatGPT and Codex. It includes
portable `plugin.json` and `mcp.json` manifests, a native Codex marketplace, five
skills, the SVG icon, this README, the license and review preparation notes.
No build step is required.

The five advisor skills and icon have separate copies in this package and in
`claude/`. Maintain the packages separately for now. When a change applies to both,
update both copies.

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
mkdir -p openai/dist
rm -f openai/dist/wealthbox-openai.zip
(cd openai && zip -r dist/wealthbox-openai.zip . -x 'dist/*' '.agents/*' '.DS_Store' '*/.DS_Store')
```

The archive is written to `openai/dist/wealthbox-openai.zip`. Directory-based
installation does not use it. Create it only when an upload is needed.

The ZIP contains `plugin.json`, `mcp.json`, all five skills, the SVG, README,
license and review notes at its root. It excludes the local `.agents/`
marketplace and the output `dist/` directory, and contains no private App binding
or compatibility manifest. `openai/dist/` is ignored by Git. Upload this archive
rather than an archive of the entire repository.

## Connection and behavior

The MCP connection uses `https://mcp.crmworkspace.com/mcp` with OAuth read and
write scopes. Connect an accessible Wealthbox workspace before running a workflow.
Creating an archive does not deploy the server or verify its live catalog.

The five skills cover client meeting preparation, service requests, onboarding
data, recommendation documentation and clients affected by a change. They use
the connected MCP tools and present results and proposed changes in conversation.

Meeting follow-up uses individual `CreateNote` and `CreateTask` calls after
conversational approval. The calls are not atomic. Keep returned IDs and reconcile
partial or uncertain results before retrying. Client messages remain drafts;
financial transactions are not executed.

## Release checks

Before release, check the manifests, production OAuth configuration, five-skill
inventory, icon references and contained files. Confirm that the skills use only
the conversational tools available from the connected server.
See [release preparation](CHATGPT-REVIEW.md) for host checks and outstanding
publication materials. A complete package is not a completed public submission.

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

For public ChatGPT submission, use the archive described below. Creating or
installing a local package does not publish it to the public directory.

## Public submission and private web testing

This portable package supplies the MCP endpoint in `mcp.json`. For public
distribution, submit it through the [OpenAI Developer Portal](https://platform.openai.com/plugins)
using **With MCP**, then complete server connection, OAuth, domain verification,
scans and review. Include the MCP configuration in the initial submission.
Complete the remaining materials in [release preparation](CHATGPT-REVIEW.md)
before submitting for review.

Uploading this ZIP through ChatGPT's private plugin import is a different flow.
An imported plugin with bundled MCP configuration can be marked **Desktop only**
even when its server uses HTTPS. That import does not establish the hosted
connection used by ChatGPT web.

For private web testing, open **ChatGPT Plugins → + → Add custom MCP server**,
enter `https://mcp.crmworkspace.com/mcp`, configure OAuth and create the plugin.
Add these five skills to that registered plugin while preserving its generated
App binding and manifest identity. Keep the private account export separate
from this portable public-submission source. The author-supplied public ZIP
must not contain `.app.json` or an `apps` declaration referencing a private App.

See [Connect and test](https://developers.openai.com/plugins/deploy/connect-chatgpt)
and [Public submission](https://developers.openai.com/plugins/deploy/submission)
for the two workflows. Published users install the plugin and authorize their
Wealthbox account; they do not manually configure its MCP endpoint.

## Create an upload archive

From the repository root, run:

```sh
mkdir -p dist
rm -f dist/wealthbox-openai.zip
(cd openai && zip -r ../dist/wealthbox-openai.zip . \
  -x 'dist/*' '.agents/*' '__MACOSX/*' '*/__MACOSX/*' \
     '.DS_Store' '*/.DS_Store' '._*' '*/._*')
```

The archive is written to `dist/wealthbox-openai.zip`. Directory-based
installation does not use it. Create it only when an upload is needed.

The ZIP contains `plugin.json`, `mcp.json`, all five skills, the SVG, README,
license and review notes at its root. It excludes the local `.agents/`
marketplace, generated files and Mac metadata, and contains no private App
binding or compatibility manifest. The archive is outside the package directory
and ignored by Git. Use it for the Developer Portal submission flow described
above. Avoid Finder's **Compress** action, which can add `__MACOSX/` metadata.

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

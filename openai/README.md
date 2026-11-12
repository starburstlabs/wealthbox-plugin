# Wealthbox for OpenAI

Use Wealthbox MCP tools and six advisor skills in ChatGPT or Codex. Contact
profiles, meeting briefs and proposed changes appear in the conversation;
no custom UI is required.

## Source and distribution

In the source repository, this directory owns the OpenAI `plugin.json`, `mcp.json`,
review notes and the `wealthbox-workspace` skill. The five other advisor skills
and the SVG icon are shared from the repository's `skills/` and `assets/` folders.
The existing Claude and Codex compatibility files at the repository root are
independent of this OpenAI release.

From the repository root, run Python 3.9 or newer:

```sh
python3 script/package_openai.py
```

The command assembles a complete plugin at `dist/openai/wealthbox/` and creates
`dist/wealthbox-openai.zip`. An optional argument selects another ZIP destination.
The generated folder and ZIP contain portable manifests at their root, all six
skills, the shared SVG, this README, license and review preparation notes. They
contain no private App binding, compatibility manifest, symlink or reference to
files outside the package. `dist/` is ignored by Git.

Use the generated folder for a local plugin installation, or the ZIP for a
submission upload. This source directory is not a complete installable plugin
until the shared files have been assembled.

## Connection and behavior

The MCP connection uses `https://mcp.crmworkspace.com/mcp` with OAuth read and
write scopes. Connect an accessible Wealthbox workspace before running a workflow.
Building the package does not deploy the server or verify its live catalog.

The `wealthbox-workspace` skill resolves workspaces and contacts, presents saved
profiles and open work in chat, and reviews proposed CRM writes. The shared
skills cover client meeting preparation, service requests, onboarding data,
recommendation documentation and clients affected by a change.

Meeting follow-up uses individual `CreateNote` and `CreateTask` calls after
conversational approval. The calls are not atomic. Keep returned IDs and reconcile
partial or uncertain results before retrying. Client messages remain drafts;
financial transactions are not executed.

## Release checks

The builder validates the portable manifests, production OAuth configuration,
skill inventory, icon references and absence of UI-only tool dependencies.
See [release preparation](CHATGPT-REVIEW.md) for host checks and outstanding
publication materials. A valid ZIP is not a completed public submission.

# Microsoft Foundry

This plugin gives Codex the Microsoft Foundry skill collection and three MCP
servers for end-to-end Foundry work: project and resource setup, model
deployment, hosted and prompt agents, invocation, evaluation, observability,
optimization, fine-tuning, quota, RBAC, networking, and troubleshooting.

## Capability preview

Codex routes a matching request to
[the Microsoft Foundry skill](skills/microsoft-foundry/SKILL.md), which then
opens only the workflow-specific instructions it needs. The skill remains the
single detailed procedure; this README is the plugin preview.

## Codex runtime

The plugin declares these MCP servers in `.mcp.json`:

| Server | Purpose |
| --- | --- |
| `azure` | Azure MCP server, started locally with `npx`. |
| `foundry-mcp` | Remote Microsoft Foundry MCP service. |
| `microsoft-docs` | Remote Microsoft Learn MCP service. |

Installation is independent of sign-in. Authentication is requested on use by
the selected Azure, Foundry, or documentation operation; credentials remain in
the host-supported credential flow rather than in this plugin. A declined,
expired, or unavailable authorization should leave the plugin installed and
allow a later retry.

## GitHub Copilot canvas

The optional GitHub Copilot App canvas is documented separately in
[the canvas extension README](extensions/microsoft-foundry/README.md). That
guide contains the Copilot installation and usage instructions. The bundled
[`extension.mjs`](extensions/microsoft-foundry/extension.mjs) is a generated
runtime artifact; do not edit it directly.

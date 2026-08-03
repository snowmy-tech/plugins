# Agent Finder

Agent Finder searches Agentic Resource Discovery (ARD) services for tools,
skills, MCP servers, agents, and APIs. It presents ranked results and leaves
installation, connection, and invocation under the user's control.

## Capability preview

### agentfinder

Use this capability when a user wants to find a tool, skill, agent, MCP server,
API, or another capability for a task. It lets the user select an Agent Finder,
searches it, and presents the results with relevance information. It never
installs a returned resource automatically.

For the complete interaction contract, see
[the Agent Finder skill](skills/agentfinder/SKILL.md).

## Choose the host you use

### Codex

Install this plugin from the Codex marketplace. Codex loads the local
`agentfinder` skill and declares the remote Agent Finder MCP endpoint in
`.mcp.json`:

`https://agentfinder.github.com/api/v1/mcp`

The MCP service is remote; the plugin does not download or install another
plugin, skill, server, or agent as a side effect. The public finder does not
need authentication. A private finder can request its own authorization only
when it is used.

### Claude Code

This bundle also contains a Claude plugin manifest. Add the marketplace and
install the `basic` plugin using Claude Code's plugin commands for the
marketplace that contains this repository. Claude Code can use its configured
HTTP, fetch, or Agent Finder MCP capability to run the same discovery contract.

This is a Claude Code-specific installation path; it is not a Codex setup step.

### ChatGPT

ChatGPT needs an HTTP-capable integration to send ARD search requests. Connect
the remote Agent Finder MCP endpoint above, or provide an equivalent custom
Action for `POST /search`. Then use the concise instructions in
[ChatGPT Skill](references/chatgpt-skill.md). It is a host-specific guide, not
an additional copy of the Codex skill.

## Runtime behavior

The plugin opens only the relevant procedure for the request. It does not load
every skill or automatically enable, connect, install, or invoke a returned
resource. Once a user chooses a result, it gives that result's native setup
steps and waits for the user to act.

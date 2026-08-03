# Microsoft Foundry Canvas for GitHub Copilot

This optional GitHub Copilot App canvas extension helps design Microsoft
Foundry hosted agents from a side panel. It combines live Foundry project
discovery with project-aware prompts to Copilot, portal handoffs, and an
embedded local Agent Inspector.

## Features

- **Project picker** — sign in, search subscriptions and Foundry projects,
  switch projects, and retain the selection across canvas reopens.
- **Live project resources** — browse deployed models, Foundry Toolboxes and
  their tools, project skills, and account guardrails.
- **Project-aware chat handoff** — model, toolbox, skill, guardrail,
  initialization, and deployment choices send a ready-to-run prompt to the
  current Copilot session with the selected project, subscription, and endpoint
  attached.
- **Embedded Agent Inspector** — **Inspect Locally** launches or reuses
  `azd ai agent run --no-inspector` in the Copilot integrated terminal, waits
  for the agent on port `8088`, and embeds the bundled inspector. Inspector
  errors can be sent back to Copilot as fix requests.

## Install

Open GitHub Copilot App, search `microsoft-foundry` from **Settings → Plugins**,
then install it.

## Usage

1. Ask Copilot to *create a Foundry hosted agent*; the Canvas opens in the
   right panel automatically.
2. Open the canvas project menu, sign in if needed, and choose a subscription
   and Foundry project.
3. Create a hosted agent from **Inspire me** or the **Hello world** sample
   prompt.
4. Switch deployed models or connect existing toolboxes, skills, or guardrails
   for the created agent.
5. Select **Deploy to Foundry** when the agent is ready.
6. Select **Inspect Locally** after the workspace contains a runnable Foundry
   hosted agent.

## Maintainer note

[`extension.mjs`](extension.mjs) is the bundled runtime artifact used by the
extension. Do not edit it directly; update its source and build process instead.

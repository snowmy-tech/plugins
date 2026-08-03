# Cost

Query Azure costs, forecast spending, and optimize cloud expenditure.

## Included skills

- **azure-cost** — Azure cost management: query costs, forecast spending, optimize to reduce waste. ([procedure](skills/azure-cost/SKILL.md))

## Requirements and authentication

This plugin includes the pinned Azure MCP server used by its skills. Azure CLI or SDK fallbacks remain available where the selected skill documents them. Authentication occurs on use; installation does not sign in or store credentials.

Commands that create, update, deploy, or delete Azure resources require the user’s explicit task authorization.

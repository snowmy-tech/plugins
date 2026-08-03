# AI Services

Build Azure AI services and configure Azure API Management as an AI gateway.

## Included skills

- **azure-ai** — Use for Azure AI: Search, Speech, OpenAI, Document Intelligence. ([procedure](skills/azure-ai/SKILL.md))
- **azure-aigateway** — Configure Azure API Management as an AI Gateway for AI models, MCP tools, and agents. ([procedure](skills/azure-aigateway/SKILL.md))

## Requirements and authentication

This plugin includes the pinned Azure MCP server used by its skills. Azure CLI or SDK fallbacks remain available where the selected skill documents them. Authentication occurs on use; installation does not sign in or store credentials.

Commands that create, update, deploy, or delete Azure resources require the user’s explicit task authorization.

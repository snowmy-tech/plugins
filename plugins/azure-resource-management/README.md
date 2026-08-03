# Resources

Discover Azure resources and visualize their architecture and relationships.

## Included skills

- **azure-resource-lookup** — List, find, and show Azure resources across subscriptions or resource groups. ([procedure](skills/azure-resource-lookup/SKILL.md))
- **azure-resource-visualizer** — Analyze Azure resource groups and generate detailed Mermaid architecture diagrams showing the relationships between individual resources. ([procedure](skills/azure-resource-visualizer/SKILL.md))

## Requirements and authentication

This plugin includes the pinned Azure MCP server used by its skills. Azure CLI or SDK fallbacks remain available where the selected skill documents them. Authentication occurs on use; installation does not sign in or store credentials.

Commands that create, update, deploy, or delete Azure resources require the user’s explicit task authorization.

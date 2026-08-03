# Identity

Implement Microsoft Entra identity, agent identity, and Azure RBAC.

## Included skills

- **azure-rbac** — Helps users find the right Azure RBAC role for an identity with least privilege access, then generate CLI commands and Bicep code to assign it. ([procedure](skills/azure-rbac/SKILL.md))
- **entra-agent-id** — Provision Microsoft Entra Agent Identity Blueprints, BlueprintPrincipals, and per-instance Agent Identities via Microsoft Graph, and configure OAuth 2.0 token exchange (fmi_path, OBO, cross-tenant) including the… ([procedure](skills/entra-agent-id/SKILL.md))
- **entra-app-registration** — Guides Microsoft Entra ID app registration, OAuth 2.0 authentication, and MSAL integration. ([procedure](skills/entra-app-registration/SKILL.md))

## Requirements and authentication

This plugin includes the pinned Azure MCP server used by its skills. Azure CLI or SDK fallbacks remain available where the selected skill documents them. Authentication occurs on use; installation does not sign in or store credentials.

Commands that create, update, deploy, or delete Azure resources require the user’s explicit task authorization.

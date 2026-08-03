# Governance

Assess Azure compliance, security posture, quotas, and service limits.

## Included skills

- **azure-compliance** — Run Azure compliance and security audits with azqr plus Key Vault expiration checks. ([procedure](skills/azure-compliance/SKILL.md))
- **azure-quotas** — Check/manage Azure quotas and usage across providers. ([procedure](skills/azure-quotas/SKILL.md))

## Requirements and authentication

This plugin includes the pinned Azure MCP server used by its skills. Azure CLI or SDK fallbacks remain available where the selected skill documents them. Authentication occurs on use; installation does not sign in or store credentials.

Commands that create, update, deploy, or delete Azure resources require the user’s explicit task authorization.

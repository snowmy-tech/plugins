# Storage

Build and operate Azure Storage services.

## Included skills

- **azure-storage** — Azure Storage Services including Blob Storage, File Shares, Queue Storage, Table Storage, and Data Lake. ([procedure](skills/azure-storage/SKILL.md))

## Requirements and authentication

This plugin includes the pinned Azure MCP server used by its skills. Azure CLI or SDK fallbacks remain available where the selected skill documents them. Authentication occurs on use; installation does not sign in or store credentials.

Commands that create, update, deploy, or delete Azure resources require the user’s explicit task authorization.

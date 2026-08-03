# Observability

Instrument, query, and diagnose Azure application telemetry.

## Included skills

- **appinsights-instrumentation** — Guidance for instrumenting webapps with Azure Application Insights. ([procedure](skills/appinsights-instrumentation/SKILL.md))
- **azure-diagnostics** — Debug Azure production issues on Azure using AppLens, Azure Monitor, resource health, and safe triage. ([procedure](skills/azure-diagnostics/SKILL.md))
- **azure-kusto** — Query and analyze data in Azure Data Explorer (Kusto/ADX) using KQL for log analytics, telemetry, and time series analysis. ([procedure](skills/azure-kusto/SKILL.md))

## Requirements and authentication

This plugin includes the pinned Azure MCP server used by its skills. Azure CLI or SDK fallbacks remain available where the selected skill documents them. Authentication occurs on use; installation does not sign in or store credentials.

Commands that create, update, deploy, or delete Azure resources require the user’s explicit task authorization.

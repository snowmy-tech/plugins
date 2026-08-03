# App Platform

Prepare, validate, deploy, and operate applications on Azure.

## Included skills

- **azure-app-onboard** — End-to-end orchestrator: from a business idea, app idea, or existing app to running Azure deployment with cost estimates and pre-deploy approval. ([procedure](skills/azure-app-onboard/SKILL.md))
- **azure-app-onboard-prereq** — Assess whether source code is ready to deploy to Azure — the check BEFORE infrastructure work. ([procedure](skills/azure-app-onboard-prereq/SKILL.md))
- **azure-deploy** — Execute Azure deployments for ALREADY-PREPARED applications that have existing .azure/deployment-plan.md and infrastructure files. ([procedure](skills/azure-deploy/SKILL.md))
- **azure-enterprise-infra-planner** — Architect and provision enterprise Azure infrastructure from workload descriptions. ([procedure](skills/azure-enterprise-infra-planner/SKILL.md))
- **azure-hosted-copilot-sdk** — Build, deploy, and modify GitHub Copilot SDK apps on Azure. ([procedure](skills/azure-hosted-copilot-sdk/SKILL.md))
- **azure-prepare** — Prepare azd-based Azure projects for deployment: generates azure.yaml, infrastructure (Bicep/Terraform), and Dockerfiles for the Azure Developer CLI (azd) workflow. ([procedure](skills/azure-prepare/SKILL.md))
- **azure-validate** — Pre-deployment validation for Azure readiness. ([procedure](skills/azure-validate/SKILL.md))
- **python-appservice-deploy** — Deploy Python (Flask/Django/FastAPI) code to Azure App Service Linux. ([procedure](skills/python-appservice-deploy/SKILL.md))

## Requirements and authentication

This plugin includes the pinned Azure MCP server used by its skills. Azure CLI or SDK fallbacks remain available where the selected skill documents them. Authentication occurs on use; installation does not sign in or store credentials.

Commands that create, update, deploy, or delete Azure resources require the user’s explicit task authorization.

# OpenShift Dev Day Roadshow

Multi-module workshop showcasing OpenShift's Application Platform capabilities. Attendees get hands-on experience with Dev Spaces, Agentic AI, GitOps, Pipelines, Developer Hub, Secured Software Supply Chains, Application Connectivity, and AI-powered application modernization.

## Modules

| Module | Topic | Duration |
|--------|-------|----------|
| **Module 1** | Developer Experience — Dev Spaces, Developer Hub, GitOps, Pipelines | ~60 min |
| **Module 2** | Secured Software Supply Chain — SLSA Level 3 with Sigstore, Tekton Chains, ACS, Conforma, Policy Controller | ~90 min |
| **Module 3** | App Connectivity for AI — Camel/Kaoto, Kuadrant AI Gateway, Service Interconnect | ~60 min |
| **Module 4** | AI-Powered Troubleshooting — OpenShift Lightspeed agentic mode with MCP | ~30 min |
| **Module 5** | AI-Powered Migration — MTA Developer Lightspeed for Java EE to Quarkus | ~60 min |

## Repository Layout

This is a **monorepo** combining lab instructions, GitOps automation, and Ansible provisioning.

| Path | Contents |
|------|----------|
| `content/` | Antora AsciiDoc lab instructions (Showroom) |
| `automation/gitops/cluster/` | Helm charts for cluster-level workloads (ArgoCD app-of-apps) |
| `automation/gitops/tenant/` | Helm charts for per-user tenant workloads |
| `automation/ansible/` | Ansible collection for RHDP provisioning |
| `qa-automation/` | Health check and E2E playbooks |
| `site.yml` | Antora site configuration |
| `ui-config.yml` | Showroom UI configuration (tabs, layout) |

### Cluster-Level Components

Deployed once via the **app-of-apps** pattern (`automation/gitops/cluster/app-of-apps/`):

| Component | Chart Path | Description |
|-----------|-----------|-------------|
| Catalog Sources | `cluster/catalog-sources/` | OLM catalog snapshot for operator version pinning |
| Vault | `cluster/vault/` | HashiCorp Vault for secrets management |
| External Secrets | `cluster/external-secrets/` | Syncs Vault secrets to Kubernetes Secrets |
| GitLab | `cluster/gitlab/` | Source code hosting (repos imported from GitHub) |
| Quay | `cluster/quay/` | Container image registry |
| OpenShift Pipelines | `cluster/openshift-pipelines/` | Tekton operator + Chains keyless signing config |
| Dev Spaces | `cluster/devspaces/` | Cloud development environments + AI assistant configs |
| OpenVSX | `cluster/openvsx/` | VS Code extension registry for Dev Spaces |
| Workspace Images | `cluster/workspace-images/` | Custom DevSpaces workspace images (cekit builds) |
| SonarQube | `cluster/sonarqube/` | Code quality analysis |
| AMQ Streams | `cluster/amq-streams/` | Kafka operator and broker |
| Developer Hub | `cluster/developer-hub/` | Backstage CR, app-config, RBAC, plugins |
| OpenShift Lightspeed | `cluster/openshift-lightspeed/` | AI assistant with MCP integration |
| RHACS | `cluster/rhacs/` | Advanced Cluster Security (Central, SecuredCluster, SSO) |
| RHTAS | `cluster/rhtas/` | Trusted Artifact Signer (Fulcio, Rekor, cosign) |
| TPA | `cluster/tpa/` | Trusted Profile Analyzer (SBOM analysis, RHDA backend) |
| Policy Controller | `cluster/policy-controller/` | Sigstore policy-controller operator |
| Parasol Policy Controller | `cluster/parasol-policy-controller/` | ClusterImagePolicies + TrustRoot setup |
| Parasol Approval | `cluster/parasol-approval/` | Release approval web app for signed attestations |
| Module 3 | `cluster/module3/` | Nested app-of-apps: Kuadrant, Skupper, Camel, messaging |

### Tenant Charts

Each tenant is provisioned by the RHDP platform via Ansible. The bootstrap chart creates per-user resources:

| Chart | Path | Description |
|-------|------|-------------|
| Bootstrap | `tenant/bootstrap/` | User provisioning, shared Dev Spaces namespace, child app creation |
| Parasol Insurance | `tenant/parasol-insurance-tenant/` | Base app: build/dev/prod namespaces, pipelines, ArgoCD apps |
| Parasol Insurance Secured | `tenant/parasol-insurance-secured-tenant/` | Secured app: secured-build/preprod/secured-prod namespaces |
| Module 3 Workload | `tenant/module3/` | Per-tenant Kafka, Camel, DevWorkspace, DB, messaging |
| Module 5 Workload | `tenant/module5/` | Per-tenant MTA migration namespace and DevWorkspace |

## Provisioning

Workshop clusters are provisioned through the [Red Hat Demo Platform (RHDP)](https://catalog.demo.redhat.com). The agnosticv definitions are in [rhpds/agnosticv](https://github.com/rhpds/agnosticv) under `rh1-2027/lb2111-ocp-dev-day-cnv-*`.

### Operator Catalog Strategy

| Source | Operators |
|--------|-----------|
| **Snapshot** (`redhat-operators-snapshot`, frozen `v4.22`) | RHDH, DevSpaces, AMQ Streams, Lightspeed, Kuadrant, Skupper, Pipelines |
| **Live** (`redhat-operators`) | RHACS, RHTAS, Policy Controller |

## Development

### Local preview

```bash
# Install Antora
npm i -g @antora/cli @antora/site-generator

# Build the site
antora site.yml

# Open www/index.html
```

### Spell check

```bash
npx cspell --config .github/workflows/.cspell.json "content/**/*.adoc"
```

## Migrated from

This monorepo consolidates the following repositories:

- [ocp-dev-days-rdshw-showroom](https://github.com/rhpds/ocp-dev-days-rdshw-showroom) — lab instructions
- [ocp-dev-days-rdshw-gitops](https://github.com/rhpds/ocp-dev-days-rdshw-gitops) — Helm charts and ArgoCD manifests
- [ocp-dev-days-rdshw-automation](https://github.com/rhpds/ocp-dev-days-rdshw-automation) — Ansible collection

## Maintainers

- Evan Shortiss (evanshortiss)
- James Falkner (jamesfalkner)
- Tyrell Reddy (treddy)
- Markus Nagel (markusjnagel)
- Shaaf Syed (sshaaf)
- Bruno Meseguer (brunoNetId)
- Tony Kay (tonykay)
- Prakhar Srivastava (prakhar1985)

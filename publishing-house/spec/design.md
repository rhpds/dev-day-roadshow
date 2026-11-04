# OpenShift Dev Day Roadshow

<!-- This file is the design document for your lab or demo. -->
<!-- Fill in each section below, or run /rhdp-publishing-house to have the intake skill help. -->
<!-- Sections marked with [brackets] are placeholders — replace with real content. -->
<!-- The validation gate checks for all required sections before submission. -->

## Overview

OpenShift Dev Day Roadshow is a modular, hands-on customer workshop delivered as part of Red Hat's Dev Day event series. Unlike demo-format assets, this workshop puts customers in the driver's seat — participants complete real developer tasks in a live OpenShift environment, making it a high-impact tool for sellers and solutions engineers to build customer confidence and deepen OpenShift adoption. It demonstrates how OpenShift's application platform capabilities improve developer output and efficiency, using the fictional Parasol Insurance company as the guiding scenario.

The workshop is structured as a growing set of modules. Current content covers the full inner and outer loop developer journey (Developer Hub, Dev Spaces, Pipelines, GitOps with AI assistance). Planned additional modules cover Red Hat Application Foundations and Red Hat Connectivity Link — expanding the workshop's footprint across the full platform stack and further differentiating it from demo-only assets in the catalog. Participants work through realistic developer tasks: exploring a software catalog with an AI assistant, creating a cloud development environment, writing and shipping a feature through CI/CD, and deploying to production with GitOps.

Module 2, **Secured Software Supply Chain**, is now authored. It extends the Parasol scenario through a secured sandbox, RHDA dependency remediation, keyless commit signing, ACS checks, Chains/SLSA evidence, Conforma validation, signed release approval, SBOM upload, GitOps promotion, and namespace admission enforcement. Learners use preconfigured platform controls rather than installing the security stack.

## Target Audience

- **Role:** Red Hat sellers and solutions engineers delivering customer-facing workshops; application developers and platform engineers evaluating or adopting OpenShift as a developer platform
- **Experience level:** Intermediate
- **What they already know:** Basic web application or REST API concepts, comfort navigating a code editor, conceptual familiarity with Git (commit, push, merge)
- **What they don't know:** Red Hat Developer Hub, Red Hat OpenShift Dev Spaces, OpenShift Pipelines, OpenShift GitOps, or AI-assisted development tooling on OpenShift

## Prerequisites

- Familiarity with basic REST API concepts (HTTP verbs, JSON responses)
- Comfort using a browser-based IDE or code editor
- Conceptual understanding of Git (commits, branches, merges) — no command-line Git required
- No prior OpenShift experience required; no local tooling installation needed
- Cannot be validated automatically — prerequisites are conceptual and self-assessed by the learner

## Learning Objectives

1. Explore the Red Hat Developer Hub software catalog and navigate application components using the Lightspeed AI assistant
2. Create a cloud development environment using a self-service golden path template in Red Hat Developer Hub
3. Build a new REST API endpoint in a Java/Quarkus application using Red Hat OpenShift Dev Spaces
4. Analyze CI/CD pipeline results and diagnose code quality failures reported by SonarQube
5. Implement AI-assisted code quality fixes using the Zoo Code coding assistant to remediate code smells
6. Deploy a feature to production by merging changes in GitLab and approving GitOps manifests in Red Hat OpenShift GitOps
7. Verify the secured software supply chain from a developer change through production promotion using Red Hat Advanced Developer Suite tools:
   - Remediate dependency findings with RHDA and container base-image findings with a hardened runtime.
   - Sign commits with the learner's Sigstore identity and inspect signature evidence.
   - Compare informational sandbox feedback with enforced signature and ACS MR gates.
   - Inspect Chains image signatures and SLSA provenance, and distinguish Conforma warnings from blocking violations.
   - Submit a signed release approval, inspect the uploaded TPA SBOM, and merge the production GitOps MR.
   - Test admission rejection of unsigned/unapproved images and verify the legitimate approved deployment.
8. Build Apache Camel integrations for data ingestion with EDI-to-XML transformation and Service Interconnect
9. Bridge messaging platforms via Kafka event-driven architecture and build an agentic AI support bot with Camel and MaaS
10. Govern LLM access with Red Hat Connectivity Link (API key auth and token rate limiting)
11. Use OpenShift's AI-powered agentic Lightspeed to interactively diagnose, monitor, and autonomously remediate application issues
12. Analyze legacy Java EE workloads using the Migration Toolkit for Applications (MTA) with Developer Lightspeed AI-assisted refactoring
13. Modernize legacy patterns (MDB, Stateless EJB, proprietary libraries) to Quarkus using MTA static analysis and AI-generated patches
14. Deploy a fully modernized Quarkus application to Red Hat OpenShift

<!-- Scale to duration: up to 3 objectives per 45 min of content. Start with action verbs: Configure, Deploy, Create, Implement, Troubleshoot, Monitor, Scale. Each should be testable. NOT: Understand, Learn, Know. -->

## Content Type

Lab (hands-on)

## Products & Technologies

**Red Hat Products:**
- Red Hat OpenShift Container Platform 5.0
- Red Hat Developer Hub (with Lightspeed AI assistant)
- Red Hat OpenShift Dev Spaces
- Red Hat OpenShift Pipelines
- Red Hat OpenShift GitOps
- Red Hat Migration Toolkit for Applications (MTA) — with Developer Lightspeed (AI-powered code refactoring)
- Red Hat Advanced Developer Suite
- Red Hat Dependency Analytics — dependency findings and remediation guidance (Module 2)
- Red Hat Trusted Artifact Signer — keyless signing infrastructure (Module 2)
- Red Hat Trusted Profile Analyzer — vulnerability intelligence and SBOM analysis (Module 2)
- Red Hat Advanced Cluster Security for Kubernetes — image scans and policy gates (Module 2)
- Red Hat Quay — image, signature, and attestation storage (Module 2)
- Red Hat Build of Quarkus
- JBoss EAP 7 (legacy source application)
- Red Hat Connectivity Link

**Upstream / Third-party (on-cluster):**
- GitLab — source control and merge request management
- SonarQube — static code analysis and quality gate
- Zoo Code AI coding assistant — AI-assisted code remediation through MaaS; checked Dev Spaces default is `claude-sonnet-4-6-a70b`
- Quarkus — Java microservices framework
- Apache Kafka — event streaming (background infrastructure)
- Apache Camel — integration framework (Module 3)
- SmallRye Reactive Messaging / MicroProfile Reactive Messaging
- PostgreSQL — production database for modernized application
- Sigstore gitsign, Fulcio, Rekor, and TUF — developer identity and signing trust (Module 2)
- Tekton Chains — image signatures and build provenance (Module 2)
- Conforma / Enterprise Contract — promotion-policy validation (Module 2)
- Sigstore Policy Controller — namespace admission enforcement (Module 2)
- Syft — SBOM generation for TPA upload (Module 2)
- Keycloak SSO and the Parasol Release Approval application — signed human approval (Module 2)

**Languages:**
- Java, JSON, YAML, AsciiDoc

<!-- Use official names: "Red Hat OpenShift", not "OpenShift". List upstream projects separately. -->

## Model Usage and MaaS Boundaries

The spec's primary model is `claude-sonnet-4-6-a70b`, and its tier is **frontier**, because the checked IDE/DLS and OpenShift Lightspeed deployment defaults select Sonnet. This is a multi-model workshop, not a Qwen-only/open-source-only deployment. These are source defaults; rendered workspace/provider settings and `OLSConfig` are authoritative when overridden.

| Consumer | Checked model selection | Important distinction |
|---|---|---|
| Module 1 — Zoo Code and preconfigured Dev Spaces assistants | `claude-sonnet-4-6-a70b` through `aiAssistantModel` | Current Module 1 E2E coding/tool probes default to `qwen3-235b`; those do not prove the IDE's Sonnet path by themselves |
| Module 1 — Developer Hub Lightspeed/Llama Stack | `claude-sonnet-4-6-a70b` for validation and safety | User-chat model selection follows the configured provider/UI; validation/safety settings are not proof of a fixed chat-model selection |
| Module 2 — secured supply-chain exercises | No required inference alias | Signing, RHDA analysis, provenance, Conforma, approval and admission are not LLM calls; optional shared IDE assistance follows Dev Spaces configuration |
| Module 3 — Camel agent, amendment and customer-profile tools | `qwen3-14b` | Gold and Silver use the same model with different identities/budgets/fallback, not different model sizes |
| Module 4 — OpenShift Lightspeed | `claude-sonnet-4-6-a70b` through `llm.model`; live `OLSConfig.spec.ols.defaultModel` wins | Its E2E compatibility check reads the configured model but uses the tenant-key route; the service's credential/UI path remains separate |
| Module 5 — Developer Lightspeed for MTA | `claude-sonnet-4-6-a70b` in generated `provider-settings.yaml` through `aiAssistantModel` | The guide's manual-recovery example and current MTA E2E prompts default to `qwen3-235b`, an alternative rather than the prefilled deployment default |

The LB2111 key allowlist also includes `qwen38-27b` and `claude-opus-5-5-a96b`. Availability on a key does not mean a module actively selects them. `qwen38-27b` also appears in older Lightspeed E2E fallback expressions; it is not the checked configured default. Neither alias should be described as mandatory for the current module defaults solely because it is allowed.

**Tool calling and TPM:** Test the actual selected model/key/application path. Compatibility requires structured tool selection, real tool execution, returning the tool result, and a grounded final answer—not just HTTP 200 or plausible text. Count prompt/completion usage across **all** inference rounds, including tool schemas, history and tool results. Per-user tests use per-user keys where applicable; service/global credentials are a distinct path. Concurrent per-user runs create aggregate load, but compatibility probes alone do not certify configured TPM capacity or quota enforcement.

**Known documentation/E2E alternatives:** The default E2E overrides are `e2e_module1_litellm_model=qwen3-235b`, `e2e_module3_litellm_model=qwen3-14b`, Module 4's `OLSConfig` model, and `e2e_module5_litellm_model=qwen3-235b`. Set the applicable override to the active client model when testing deployment-model parity. This PH update records the distinction; it does not change routing, model entitlements, application configuration, or E2E defaults.

**Source references:**
- [Dev Spaces model default](../../automation/gitops/cluster/devspaces/devspaces-instance/values.yaml), [Zoo Code profile](../../automation/gitops/cluster/devspaces/devspaces-instance/templates/zoo-code-config.yaml), and [generated DLS provider settings](../../automation/gitops/cluster/devspaces/devspaces-instance/templates/es-dls-mta-config.yaml).
- [Developer Hub validation model](../../automation/gitops/cluster/developer-hub/templates/backstage-cr.yaml) and [safety-provider settings](../../automation/gitops/cluster/developer-hub/templates/es-lightspeed-llama-stack-secrets.yaml).
- [OpenShift Lightspeed model default](../../automation/gitops/cluster/openshift-lightspeed/values.yaml) and [OLSConfig rendering](../../automation/gitops/cluster/openshift-lightspeed/templates/olsconfig.yaml).
- [Camel Gold/Silver guide settings](../../content/modules/ROOT/pages/module-03/m5/m5.3.adoc) and the [workspace agent configuration](https://github.com/openshift-dev-days/module3-dev-workspace/blob/main/tools/solution/steps/8/agent/application.properties).
- [MTA guide recovery example](../../content/modules/ROOT/pages/module-05/module-05-03-configure-mta-extension.adoc), [Module 1 E2E](../../qa-automation/tasks/module1-workflow.yml), and [Module 5 E2E](../../qa-automation/e2e-module-05.yml).

## Module Map

| Module | Title | Duration |
|--------|-------|----------|
| 1 | The Developer Experience | 85 min |
| 2 | Secured Software Supply Chain | 90 min planning budget; guide estimates 60–90 min |
| 3 | App Connectivity for AI | 150 min |
| 4 | AI-Powered Troubleshooting | 35 min |
| 5 | AI-powered migration using MTA | 55 min |
| — | **Total planning budget** | **~415 min (~6 hr 55 min)** |

Module 2's five timed sections total 75 minutes; its 90-minute planning budget allows for SSO, analysis, pipeline, and reconciliation waits within the guide's 60–90 minute estimate. The two-hour event format selects a subset of this modular catalog; the table is not a promise to complete every module in one event.

### Module 2 Flow and Evidence

| Section | Learner action | Expected evidence |
|---|---|---|
| Dealing with Vulnerabilities Early — 15 min | Discover the secured component, create its branch sandbox, inspect RHDA findings, and update framework dependencies | Isolated sandbox and initial pipeline; dependency report changes after remediation |
| Signing Your Commits — 10 min | Complete the gitsign/Keycloak flow, commit, and push | Identity-bound commit signature and inspectable certificate details; GitLab's unverified badge is not itself a Sigstore verdict |
| Checking the Sandbox Pipeline — 15 min | Inspect signature/ACS reports and replace the vulnerable base image | Informational sandbox results and GitLab commit report; new scan results after hardening |
| Moving to the Next Stages — 25 min | Pass enforced MR checks, merge and wait for the build, tag, inspect Conforma failure, approve, retry promotion, and merge production manifests | Chains/SLSA evidence, missing-approval failure followed by success, signed approval, TPA SBOM link, and production GitOps rollout |
| Securing Your Namespaces — 10 min | Attempt unsigned/unapproved deployment and verify the legitimate release | Admission-policy denials and a running approved application/database |

[Module 2 outline](modules/module-02-secure-software-factory.md) and [guide introduction](../../content/modules/ROOT/pages/module-02/00-intro.adoc) provide the detailed sequence. The workshop demonstrates the guide's SLSA Level 3 provenance and policy-control scenario; these learning outcomes do not constitute an independent security certification or proof of complete automated acceptance.

<!-- Each module 10-30 min. Total: lab 1-4 hours, demo 15-45 min. Modules should build on each other. -->

## Difficulty Level

Intermediate

## Environment

**Learner view:** Participants access the lab through a browser with no local tooling required. On day one, a shared OpenShift cluster is pre-provisioned with Red Hat Developer Hub, Red Hat OpenShift Dev Spaces, Red Hat OpenShift Pipelines, Red Hat OpenShift GitOps (Argo CD), GitLab, and SonarQube already deployed. Each participant is namespaced to their own project/user space. All URLs are templated with a `${DOMAIN}` variable that resolves to the shared cluster's ingress domain. Participants log into Developer Hub, then Dev Spaces, then GitLab — all via browser tabs — without installing anything locally.

**Automation needed:** Yes

Automation must provision:
- A shared OpenShift cluster with all required operators installed (Dev Spaces, Pipelines, GitOps, Developer Hub)
- On-cluster services: GitLab instance (with Parasol Insurance repositories pre-loaded), Developer Hub with a MaaS-backed Lightspeed/Llama Stack provider and Sonnet validation/safety defaults, SonarQube with the Parasol project and quality profile configured, Argo CD with GitOps manifests for the Parasol application
- Zoo Code AI coding assistant configured through Dev Spaces `aiAssistantModel` (checked default `claude-sonnet-4-6-a70b`)
- Per-participant namespaces, RBAC, and Developer Hub user accounts
- Parasol Insurance sample application deployed in a staging/production namespace visible to participants

**Module 2 requirements:**
- Separate secured source and manifests repositories, the secured Developer Hub component/template, and a Dev Spaces image with gitsign and RHDA configured.
- Per-tenant `secured-build`, `preprod`, and `secured-prod` namespaces plus a self-service branch sandbox; regular Module 1 resources remain separate.
- Shared RHACS, RHTAS/Fulcio/Rekor/TUF, TPA/RHDA backend, Quay, SonarQube, Chains, Conforma policies, and the Release Approval application, with workshop SSO/trust relationships preconfigured.
- Provisioned MR, post-merge build, and tag-promotion pipelines; commit/MR reports expose signature and scan evidence.
- Production admission opt-in and policies for image signatures, signed-commit provenance, and release approval. An unsigned or unapproved image must not become a valid release merely because an informational sandbox build completed.
- A workflow that waits for the post-merge image before tagging, creates the production-manifests MR only after policy/approval validation, and uploads its SBOM to TPA.
- No ZTWIM installation or separate Trusted Software Factory setup is part of the Module 2 learner procedure.

## Infrastructure Requirements

- **Cloud provider:** CNV
- **Cluster type:** Multinode
- **OCP version:** 5.0
- **Topology:** Shared cluster — max 30 concurrent users, namespaced per participant
- **Control plane:** 3 nodes — 16 vCPU, 64GB RAM each
- **Workers:** 4 nodes — 32 vCPU, 64GB RAM, 100GB disk each
- **Automation approach:** Both — Ansible (cluster bootstrap and operator installation) and GitOps/Helm (per-tenant namespaces and application manifests)
- **AI/MaaS:** External MaaS with frontier Sonnet defaults for the checked IDE/DLS and OpenShift Lightspeed clients, `qwen3-14b` for Camel agents, and `qwen3-235b` in guide/E2E alternatives. The complete selection/credential boundaries are in the model inventory above. No local GPU deployment is required; actual model authorization and aggregate agent-round TPM must be validated for the event.
- **External services:** `registry.redhat.io`, `quay.io`, `github.com` (GitOps configs and Showroom content), `open-vsx.org` (VS Code extensions provisioned into Dev Spaces), `repo1.maven.org` (Java dependencies), RHDP MaaS endpoint (URL confirmed at provisioning)
- **Non-GA products:** None (all products are GA)

<!-- Not all fields must be known at intake. "TBD, estimating ~X" is fine. -->

## Assessment Strategy (Optional)

<!-- Optional — skip this section for demos or classic labs without verification. -->
<!-- Relevant for Zero-Touch labs with solve/validate buttons or labs with automated checks. -->

This is a classic (Showroom) lab. Assessment is implicit: participants verify their own progress through visible UI outcomes — the new REST endpoint responding in the browser, the pipeline turning green, and the GitOps sync completing. No automated solve/validate buttons are required for this lab type.

For **Module 2**, assessment includes positive and negative outcomes: inspect dependency/base-image findings, verify commit identity and sandbox reports, distinguish informational checks from enforced MR gates, observe promotion fail before approval and pass afterward, inspect the signed approval and SBOM link, merge the production GitOps MR, and test admission denials alongside the legitimate release. Informational Conforma vulnerability/SonarQube warnings are not treated as blocking violations.

Module 2 content is authored, but content completion is separate from test coverage and release readiness. `development.e2e.status` in the project spec remains independent; this design does not mark browser SSO/RHDA interactions or all end-to-end paths as validated.

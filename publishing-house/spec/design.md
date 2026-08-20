# OpenShift Dev Day Roadshow

<!-- This file is the design document for your lab or demo. -->
<!-- Fill in each section below, or run /rhdp-publishing-house to have the intake skill help. -->
<!-- Sections marked with [brackets] are placeholders — replace with real content. -->
<!-- The validation gate checks for all required sections before submission. -->

## Overview

OpenShift Dev Day Roadshow is a modular, hands-on workshop delivered as part of Red Hat's Dev Day event series. It demonstrates how OpenShift's application platform capabilities improve developer output and efficiency, using the fictional Parasol Insurance company as the guiding scenario. The workshop is structured as a growing set of modules — current content covers the full inner and outer loop developer journey (Developer Hub, Dev Spaces, Pipelines, GitOps with AI assistance), with additional modules planned for secure software supply chain, Red Hat Application Foundation, and Red Hat Connectivity Link. Participants work through realistic developer tasks: exploring a software catalog with an AI assistant, creating a cloud development environment, writing and shipping a feature through CI/CD, and deploying to production with GitOps.

## Target Audience

- **Role:** Application developers and platform engineers evaluating or adopting OpenShift as a developer platform
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

<!-- Scale to duration: up to 3 objectives per 45 min of content. Start with action verbs: Configure, Deploy, Create, Implement, Troubleshoot, Monitor, Scale. Each should be testable. NOT: Understand, Learn, Know. -->

## Content Type

Lab (hands-on)

## Products & Technologies

**Red Hat Products:**
- Red Hat OpenShift Container Platform 4.20
- Red Hat Developer Hub (with Lightspeed AI assistant)
- Red Hat OpenShift Dev Spaces
- Red Hat OpenShift Pipelines
- Red Hat OpenShift GitOps

**Upstream / Third-party (on-cluster):**
- GitLab — source control and merge request management
- SonarQube — static code analysis and quality gate
- Zoo Code AI coding assistant — AI-assisted code remediation (backed by Qwen3 235b via MaaS)
- Quarkus — Java microservices framework
- Apache Kafka — event streaming (background infrastructure)

**Languages:**
- Java, JSON, YAML

<!-- Use official names: "Red Hat OpenShift", not "OpenShift". List upstream projects separately. -->

## Module Map

| Module | Title | Duration |
|--------|-------|----------|
| 1 | Explore the Platform | 20 min |
| 2 | Develop a Feature | 25 min |
| 3 | CI/CD Pipeline & Quality Gates | 15 min |
| 4 | AI-Assisted Code Fix | 10 min |
| 5 | GitOps Promotion & Production Deploy | 15 min |
| — | **Total hands-on** | **85 min** |
| — | Intro / orientation pages | ~15 min |
| — | **Total lab** | **~100 min (~1.5 hr)** |

<!-- Each module 10-30 min. Total: lab 1-4 hours, demo 15-45 min. Modules should build on each other. -->

## Difficulty Level

Intermediate

## Environment

**Learner view:** Participants access the lab through a browser with no local tooling required. On day one, a shared OpenShift cluster is pre-provisioned with Red Hat Developer Hub, Red Hat OpenShift Dev Spaces, Red Hat OpenShift Pipelines, Red Hat OpenShift GitOps (Argo CD), GitLab, and SonarQube already deployed. Each participant is namespaced to their own project/user space. All URLs are templated with a `${DOMAIN}` variable that resolves to the shared cluster's ingress domain. Participants log into Developer Hub, then Dev Spaces, then GitLab — all via browser tabs — without installing anything locally.

**Automation needed:** Yes

Automation must provision:
- A shared OpenShift cluster with all required operators installed (Dev Spaces, Pipelines, GitOps, Developer Hub)
- On-cluster services: GitLab instance (with Parasol Insurance repositories pre-loaded), Developer Hub with RHDH Lightspeed configured against the Qwen3 235b MaaS endpoint, SonarQube with the Parasol project and quality profile configured, Argo CD with GitOps manifests for the Parasol application
- Zoo Code AI coding assistant configured to use the Qwen3 235b MaaS endpoint
- Per-participant namespaces, RBAC, and Developer Hub user accounts
- Parasol Insurance sample application deployed in a staging/production namespace visible to participants

## Infrastructure Requirements

- **Cloud provider:** CNV
- **Cluster type:** Multinode
- **OCP version:** 4.20 (minimum)
- **Topology:** Shared cluster — max 30 concurrent users, namespaced per participant
- **Control plane:** 3 nodes — 16 vCPU, 64GB RAM each
- **Workers:** 6 nodes — 16 vCPU, 32GB RAM, 100GB disk each
- **Automation approach:** Both — Ansible (cluster bootstrap and operator installation) and GitOps/Helm (per-tenant namespaces and application manifests)
- **AI/MaaS:** MaaS, open-source tier, Qwen3 235b — RHDP-hosted on a separate cluster external to the workshop environment; backs Zoo Code AI coding assistant and RHDH Lightspeed
- **External services:** `registry.redhat.io`, `quay.io`, `github.com` (GitOps configs and Showroom content), `open-vsx.org` (VS Code extensions provisioned into Dev Spaces), `repo1.maven.org` (Java dependencies), RHDP MaaS endpoint (URL confirmed at provisioning)
- **Non-GA products:** None (all products are GA)

<!-- Not all fields must be known at intake. "TBD, estimating ~X" is fine. -->

## Assessment Strategy (Optional)

<!-- Optional — skip this section for demos or classic labs without verification. -->
<!-- Relevant for Zero-Touch labs with solve/validate buttons or labs with automated checks. -->

This is a classic (Showroom) lab. Assessment is implicit: participants verify their own progress through visible UI outcomes — the new REST endpoint responding in the browser, the pipeline turning green, and the GitOps sync completing. No automated solve/validate buttons are required for this lab type.

# Module 05 — AI-powered migration using MTA

### Status

**Complete.** Content authored by James Falkner, delivered 2026-10-15.

### Learning Objectives

- Configure the MTA extension in Red Hat Dev Spaces, including Developer Lightspeed (AI-assisted migration)
- Analyze `parasol-insurance-eap` and receive AI-powered code refactoring recommendations
- Modernize `EmailIntakeMDB` (JMS MDB → SmallRye Reactive Messaging with `@Incoming`)
- Author and apply custom MTA rules for the proprietary `audit-logging-library` (v1 → v2)
- Modernize `ClaimService` (`@Stateless` EJB → `@ApplicationScoped` + `@Transactional`)
- Review the completed `quarkus` branch and deploy the modernized application to OpenShift

### Lab Outline

Hands-on workshop guiding participants through end-to-end application modernization of the Parasol Insurance JavaEE 7 / EAP application using MTA's Developer Lightspeed (DLS) — AI-powered code refactoring that combines static analysis with generative AI:

1. **Section 1: Goals** (~3 min) — Lab objectives overview: MTA extension, Developer Lightspeed, the `parasol-insurance-eap` codebase, migration path to Quarkus/Jakarta EE, and custom rules for proprietary libraries
2. **Section 2: Introduction to Developer Lightspeed for MTA** (~5 min) — Background on MTA's AI-powered refactoring: the challenge of modernization, how DLS combines static analysis with LLMs, custom technology support, portfolio-scale migration, and model flexibility (OpenAI-compatible APIs, RHOAI, RHELAI, vLLM)
3. **Section 3: Access Dev Spaces and configure the MTA extension** (~10 min) — Open the pre-provisioned `mta-lab` Dev Spaces workspace, log in via Keycloak SSO, create a Quarkus migration profile with source/target technologies, and confirm Developer Lightspeed can reach the lab LLM via `provider-settings.yaml` (LiteLLM/Qwen3-235b)
4. **Section 4: Modernize Message-Driven Bean (MDB) to Reactive Messaging** (~10 min) — Use MTA analysis + DLS to refactor `EmailIntakeMDB` from `@MessageDriven` / JMS `MessageListener` to `@ApplicationScoped` with `@Incoming("email-intake")` / SmallRye Reactive Messaging. Review AI-generated git patches in MTA Resolution Details before accepting. Covers the architectural shift from synchronous JMS to reactive streams.
5. **Section 5: Custom rules for the audit logging library** (~10 min) — Explore 5 custom MTA rules (`audit-logging-0001` through `0005`) for Parasol's proprietary `audit-logging-library` (v1→v2). Upload `logging.yaml` to an MTA profile, run analysis, inspect custom findings (dependency bump, `AuditEvent.builder`→direct construction, `FileSystemAuditLogger`→`StreamableAuditLogger`, sync→async, convenience methods). Use DLS to generate and review patches for `ClaimsResource`.
6. **Section 6: Stateless EJB to CDI (ClaimService)** (~7 min) — Refactor `ClaimService` from `@Stateless` EJB to `@ApplicationScoped` + `@Transactional` CDI bean using DLS with Agent Mode enabled. Agent Mode iteratively fixes ripple effects (pom.xml dependencies, persistence config, `javax`→`jakarta` imports) with accept/reject control at each step.
7. **Section 7: Review the Quarkus branch and deploy to OpenShift** (~10 min) — Check out the completed `quarkus` branch, review migrated code (messaging, CDI services, scheduling, REST), optionally smoke-test locally with `quarkus:dev` (H2), then deploy to OpenShift via binary Docker build with PostgreSQL backend. Verify Parasol Dashboard, Claims, and Inbox in the browser.

### Technology Stack

- Red Hat OpenShift (OCP 5.0)
- Red Hat Dev Spaces (pre-provisioned `mta-lab` workspace)
- Red Hat Migration Toolkit for Applications (MTA) — VS Code extension with Developer Lightspeed
- Red Hat Developer Lightspeed for MTA (DLS) — AI-powered code refactoring (GenAI via LiteLLM/Qwen3-235b)
- JBoss EAP 7 (legacy source: `parasol-insurance-eap`)
- Red Hat Build of Quarkus (migration target)
- SmallRye Reactive Messaging / MicroProfile Reactive Messaging
- Jakarta EE (CDI, Transactions, Persistence)
- PostgreSQL (production database on OpenShift)
- GitLab (source code hosting per-tenant)

### Target Audience

Java developers, architects, and platform engineers responsible for modernizing legacy JavaEE/EAP applications to cloud-native Quarkus on OpenShift.

### Notes

- Duration: ~55 minutes (estimated from content depth — 7 substantive sections with hands-on exercises)
- Content authored by James Falkner
- Content directory: `content/modules/ROOT/pages/module-05/` (7 section files + `module-05-logging.adoc` reference)
- Supplementary page-level entry: `content/modules/ROOT/pages/06-module-05-ai-driven-app-modernization.adoc`
- Agent Mode (Section 6) is an advanced feature — students can stop the agent loop at any point
- Exercise 3 in Section 7 (local quarkus:dev) is optional

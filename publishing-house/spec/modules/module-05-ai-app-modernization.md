# Module 05 — AI-powered migration using MTA

### Brief Overview

Participants modernize the Parasol Insurance Java EE 7 / EAP application using the Migration Toolkit for Applications and Developer Lightspeed. Static analysis supplies migration context for AI-assisted patches, which learners review before accepting. Exercises cover messaging, CDI services, and a proprietary audit library, then use the completed `quarkus` branch for a reproducible OpenShift deployment.

### Audience and Time

- **Target personas:** Java developers, architects, and platform engineers modernizing Java EE/EAP applications.
- **Experience level:** Intermediate; familiarity with Java, Maven, and the legacy application patterns is helpful.
- **Prerequisites:** Workshop credentials, the pre-provisioned `mta-lab` workspace, the tenant's `parasol-insurance-eap` repository, and the configured MaaS provider.
- **Estimated duration:** 55 minutes across seven sections; local Quarkus dev-mode verification is optional.

### Status

**Complete.** Content authored by James Falkner, delivered 2026-10-15.

### Learning Objectives

- Configure the MTA extension in Red Hat Dev Spaces, including Developer Lightspeed (AI-assisted migration)
- Analyze `parasol-insurance-eap` and receive AI-powered code refactoring recommendations
- Modernize `EmailIntakeMDB` (JMS MDB → SmallRye Reactive Messaging with `@Incoming`)
- Author and apply custom MTA rules for the proprietary `audit-logging-library` (v1 → v2)
- Modernize `ClaimService` (`@Stateless` EJB → `@ApplicationScoped` + `@Transactional`)
- Review the completed `quarkus` branch and deploy the modernized application to OpenShift

### Lab Structure

| Section | Title | Duration |
|---|---|---:|
| 1 | Goals | 3 min |
| 2 | Introduction to Developer Lightspeed for MTA | 5 min |
| 3 | Access Dev Spaces and configure the MTA extension | 10 min |
| 4 | MDB to Reactive Messaging | 10 min |
| 5 | Custom rules for the audit logging library | 10 min |
| 6 | Stateless EJB to CDI | 7 min |
| 7 | Quarkus branch review and OpenShift deployment | 10 min |
| — | Total | **55 min** |

### Detailed Steps

1. **Section 1: Goals** (~3 min) — Lab objectives overview: MTA extension, Developer Lightspeed, the `parasol-insurance-eap` codebase, migration path to Quarkus/Jakarta EE, and custom rules for proprietary libraries
2. **Section 2: Introduction to Developer Lightspeed for MTA** (~5 min) — Background on MTA's AI-powered refactoring: the challenge of modernization, how DLS combines static analysis with LLMs, custom technology support, portfolio-scale migration, and model flexibility (OpenAI-compatible APIs, RHOAI, RHELAI, vLLM)
3. **Section 3: Access Dev Spaces and configure the MTA extension** (~10 min) — Open the pre-provisioned `mta-lab` Dev Spaces workspace, log in via Keycloak SSO, create a Quarkus migration profile with source/target technologies, and confirm Developer Lightspeed can reach the lab LLM via `provider-settings.yaml` (deployment default `claude-sonnet-4-6-a70b`; the guide's manual-recovery example uses `qwen3-235b`)
4. **Section 4: Modernize Message-Driven Bean (MDB) to Reactive Messaging** (~10 min) — Use MTA analysis + DLS to refactor `EmailIntakeMDB` from `@MessageDriven` / JMS `MessageListener` to `@ApplicationScoped` with `@Incoming("email-intake")` / SmallRye Reactive Messaging. Review AI-generated git patches in MTA Resolution Details before accepting. Covers the architectural shift from synchronous JMS to reactive streams.
5. **Section 5: Custom rules for the audit logging library** (~10 min) — Explore 5 custom MTA rules (`audit-logging-0001` through `0005`) for Parasol's proprietary `audit-logging-library` (v1→v2). Upload `logging.yaml` to an MTA profile, run analysis, inspect custom findings (dependency bump, `AuditEvent.builder`→direct construction, `FileSystemAuditLogger`→`StreamableAuditLogger`, sync→async, convenience methods). Use DLS to generate and review patches for `ClaimsResource`.
6. **Section 6: Stateless EJB to CDI (ClaimService)** (~7 min) — Refactor `ClaimService` from `@Stateless` EJB to `@ApplicationScoped` + `@Transactional` CDI bean using DLS with Agent Mode enabled. Agent Mode iteratively fixes ripple effects (pom.xml dependencies, persistence config, `javax`→`jakarta` imports) with accept/reject control at each step.
7. **Section 7: Review the Quarkus branch and deploy to OpenShift** (~10 min) — Check out the completed `quarkus` branch, review migrated code (messaging, CDI services, scheduling, REST), optionally smoke-test locally with `quarkus:dev` (H2), then deploy to OpenShift via binary Docker build with PostgreSQL backend. Verify Parasol Dashboard, Claims, and Inbox in the browser.

### Technology Stack

- Red Hat OpenShift (OCP 5.0)
- Red Hat Dev Spaces (pre-provisioned `mta-lab` workspace)
- Red Hat Migration Toolkit for Applications (MTA) — VS Code extension with Developer Lightspeed
- Red Hat Developer Lightspeed for MTA (DLS) — AI-powered code refactoring through MaaS/OpenAI-compatible APIs; model-selection boundaries are documented below
- JBoss EAP 7 (legacy source: `parasol-insurance-eap`)
- Red Hat Build of Quarkus (migration target)
- SmallRye Reactive Messaging / MicroProfile Reactive Messaging
- Jakarta EE (CDI, Transactions, Persistence)
- PostgreSQL (production database on OpenShift)
- GitLab (source code hosting per-tenant)

### Key Takeaways

- Static analysis provides focused migration context rather than relying on an unconstrained coding prompt.
- AI-generated patches require review and accept/reject control; a suggested edit is not proof that the application still builds.
- Custom MTA rules encode proprietary library contracts alongside stock Java EE/Quarkus migration rules.
- MDB, EJB, transaction, scheduling, and REST behavior must be mapped to the corresponding Quarkus/CDI/reactive concepts.
- The completed `quarkus` branch provides a consistent deployment target after practicing individual refactorings.
- A binary Docker build, Secret-backed PostgreSQL settings, health probes, and API/UI checks verify the deployed application separately from IDE analysis.

### Model Usage

- **Deployment default:** `claude-sonnet-4-6-a70b`, inherited from Dev Spaces `aiAssistantModel` in the generated DLS `provider-settings.yaml`.
- **Guide alternative:** The manual provider-recovery example names `qwen3-235b`. It is an alternative configuration, not evidence that the prefilled provider currently selects Qwen.
- **Current E2E default:** The MTA prompts and explicit LiteLLM compatibility check use `qwen3-235b`, configurable through `e2e_module5_litellm_model`. Set that override to the active DLS model when testing deployment-model parity.
- MTA analysis, actual IDE patch application, and the completed application's build/deployment remain distinct from model API/tool compatibility checks.
- See the [design model inventory](../design.md#model-usage-and-maas-boundaries) for source references and token-accounting scope.

### Notes

- Duration: ~55 minutes (estimated from content depth — 7 substantive sections with hands-on exercises)
- Content authored by James Falkner
- Content directory: `content/modules/ROOT/pages/module-05/` (7 section files + `module-05-logging.adoc` reference)
- Supplementary page-level entry: `content/modules/ROOT/pages/06-module-05-ai-driven-app-modernization.adoc`
- Agent Mode (Section 6) is an advanced feature — students can stop the agent loop at any point
- Exercise 3 in Section 7 (local quarkus:dev) is optional

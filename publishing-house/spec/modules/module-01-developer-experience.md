# Module 01 — The Developer Experience

### Brief Overview

Participants follow a complete developer journey on OpenShift 5 at Parasol Insurance — from discovering the platform to shipping a feature to production. They explore Developer Hub with Lightspeed AI, provision a cloud IDE via a golden path template, build a Quarkus REST endpoint in Dev Spaces, push through a CI/CD pipeline with SonarQube quality gates, fix code smells using the Zoo Code AI assistant, and deploy to production via GitOps/Argo CD. The entire inner+outer loop runs in the browser with no local tooling.

### Audience and Time

- **Target personas:** Application developers, platform engineers, IT decision makers
- **Experience level:** Intermediate — no prior OpenShift or container experience required
- **Prerequisites for this module:** Lab environment access (credentials provided), browser only
- **Estimated duration:** 85 minutes (6 sections)

### Learning Objectives

- Navigate Developer Hub to discover applications, APIs, and documentation
- Use self-service templates to create an isolated development environment
- Write and test code in a cloud-based Dev Spaces IDE with AI assistance
- Push code through an automated CI/CD pipeline and resolve quality gate failures
- Verify a GitOps-driven deployment to production

### Lab Structure

| Section | Title | Duration |
|---------|-------|----------|
| 1 | Meet the Platform | 10 min |
| 2 | Your Mission | 10 min |
| 3 | Build the Feature | 25 min |
| 4 | Ship It | 15 min |
| 5 | Call in the AI | 10 min |
| 6 | Go Live | 15 min |

### Section Details

**Section 1 — Meet the Platform:** Login to Developer Hub, navigate the Parasol Insurance software catalog, explore component overview and dependency graphs, interact with Lightspeed AI assistant to ask architecture questions.

**Section 2 — Your Mission:** Use a golden path template in Developer Hub to provision a personal Dev Spaces workspace. Fill form, submit, confirm workspace link appears in catalog.

**Section 3 — Build the Feature:** Open Dev Spaces IDE, explore Quarkus project structure, start app in dev mode (`mvn quarkus:dev`), implement a new claims statistics REST endpoint with step-by-step code snippets, verify endpoint with `curl`.

**Section 4 — Ship It:** Commit and push code to GitLab from Dev Spaces. Observe OpenShift Pipeline triggered by webhook — build, test, SonarQube scan stages. Pipeline intentionally fails at quality gate due to seeded code smells. Examine SonarQube findings.

**Section 5 — Call in the AI:** Use Zoo Code AI coding assistant in Dev Spaces to identify and fix the SonarQube code smells. Review AI suggestion, apply fix, re-push. Pipeline passes quality gate.

**Section 6 — Go Live:** Create GitLab merge request, merge feature branch, create release tag triggering release pipeline and GitOps manifests MR. Approve in Argo CD, sync, verify production endpoint responds with claims statistics JSON.

### Key Takeaways

- Developer Hub provides a unified software catalog with Lightspeed AI for architecture discovery
- Golden path templates eliminate environment setup friction — zero to coding in minutes
- Quarkus live reload enables rapid inner-loop iteration entirely on-cluster
- SonarQube quality gates enforce code standards automatically on every push
- AI coding assistants accelerate code quality remediation without leaving the IDE
- GitOps separates manifests from code — Argo CD reconciles desired state for auditable deployments

### Infrastructure Notes

- Developer Hub pre-configured with Parasol Insurance catalog entities and Lightspeed plugin (Qwen3 235b via MaaS)
- Golden path template provisions Dev Spaces workspace + GitLab project per participant
- OpenShift Pipeline (Tekton) with GitLab webhook, SonarQube with custom quality profile
- Zoo Code plugin in Dev Spaces devfile, connected to Qwen3 235b via MaaS
- Argo CD configured with GitOps manifests repository and per-participant production application

### Content Status

**Complete.** 717 lines, all 6 sections with full step-by-step exercises, screenshots, code snippets, tips, and verification steps.

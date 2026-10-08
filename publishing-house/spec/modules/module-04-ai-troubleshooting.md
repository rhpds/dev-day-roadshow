# Module 04 — AI-Powered Troubleshooting

### Brief Overview

A hands-on session covering interactive troubleshooting, live metric visualization, autonomous alert investigation, and human-in-the-loop remediation using OpenShift 5's agentic Lightspeed. Exercises progress from a simple NetworkPolicy diagnostic to a cascading multi-service failure to building a custom monitoring dashboard — all without writing PromQL or using `oc` commands directly.

### Audience and Time

- **Target personas:** Application developers, platform engineers
- **Experience level:** Intermediate — no prior PromQL, Lightspeed, or troubleshooting experience required
- **Prerequisites for this module:** Lab environment access with pre-deployed R&D applications (Parasol Web and Parasol Payments)
- **Estimated duration:** 35 minutes (3 exercises)

### Learning Objective

Use OpenShift 5's AI-powered agentic Lightspeed to interactively diagnose, monitor, and autonomously remediate application issues in the Parasol Insurance app.

### Detailed Objectives

- Use OpenShift Lightspeed to investigate application issues through natural language
- Diagnose network connectivity problems using AI-driven cluster introspection
- Investigate firing alerts and identify root causes across correlated metrics and logs
- Request AI-assisted remediation actions (like rolling back a broken deployment)
- Generate interactive Perses charts and build custom monitoring dashboards

### Lab Structure

| Exercise | Title | Duration | Scenario |
|----------|-------|----------|----------|
| 1 | Investigate a timeout issue | 10 min | NetworkPolicy blocks frontend-to-backend traffic in `{user}-parasol-web` |
| 2 | Diagnose and fix a critical alert | 15 min | Cascading failure: reporting-service v1.0.2 leaks DB connections, exhausts PostgreSQL max_connections, causes payments-api 5xx and PaymentErrorRateHigh alert |
| 3 | Build a custom monitoring dashboard | 10 min | Create Perses dashboard, generate charts (HTTP request rate, error rate, CPU) via Lightspeed, export to persistent dashboard |

### Exercise Details

**Exercise 1 — Investigate a timeout issue:** Frontend-to-backend timeout in the Parasol Web namespace caused by an overly restrictive NetworkPolicy. Students open Lightspeed, describe the symptom, and let the AI correlate pod state, network policies, and events to identify and fix the policy. Single-cause diagnostic.

**Exercise 2 — Diagnose and fix a critical alert:** Multi-layer cascading failure in Parasol Payments. The reporting-service v1.0.2 has a DB connection leak that exhausts PostgreSQL max_connections, causing payments-api to return 5xx errors and trigger the PaymentErrorRateHigh alert. Students trace the chain via Lightspeed (metrics, logs, events) and request an AI-assisted rollback of the broken deployment.

**Exercise 3 — Build a custom monitoring dashboard:** Students create a Perses dashboard, then use Lightspeed to generate three inline charts via natural language prompts (HTTP request rate, error rate, CPU usage). Charts are exported to the persistent dashboard — demonstrating monitoring dashboard creation without PromQL expertise.

### Key Takeaways

- OpenShift Lightspeed correlates Prometheus metrics, pod logs, events, and Kubernetes resource state via MCP
- Developers can investigate and remediate issues in their own namespaces without cluster-admin access
- AI-assisted remediation (rollbacks, policy fixes) can be requested through conversation
- Perses charts built through natural language provide ongoing monitoring without PromQL expertise

### Infrastructure Notes

- Parasol Web (frontend + backend) pre-deployed in `{user}-parasol-web` with intentionally broken NetworkPolicy
- Parasol Payments (payments-api + postgres + reporting-service) pre-deployed in `{user}-parasol-payments` with reporting-service v1.0.2 (connection leak bug)
- OpenShift Lightspeed with MCP enabled on the cluster
- Perses operator installed for dashboard creation
- PrometheusRule for PaymentErrorRateHigh alert pre-configured

### Content Status

**Complete.** 254 lines, all 3 exercises with full walkthroughs, screenshots, verification steps, and key takeaways.

# Module 01 — Explore the Platform

### Brief Overview

Participants begin their developer journey by discovering the Parasol Insurance application platform through Red Hat Developer Hub. They navigate the software catalog to locate the Parasol Insurance components, ask the Lightspeed AI assistant questions about the architecture, and then use a self-service golden path template to provision their own cloud development environment. This module establishes the "developer portal as single pane of glass" concept before any code is written.

### Audience and Time

- **Target personas:** Application developers, platform engineers
- **Experience level:** Intermediate — no prior OpenShift experience required
- **Prerequisites for this module:** Lab environment access (credentials provided), familiarity with browser navigation; no prior Developer Hub or OpenShift experience needed
- **Estimated duration:** 20 minutes (Section 1: Meet the Platform ~10 min, Section 2: Your Mission ~10 min)

### Learning Objectives

- Explore the Red Hat Developer Hub software catalog to locate and navigate the Parasol Insurance application components
- Demonstrate how the Lightspeed AI assistant can answer architecture questions from within Developer Hub
- Create a personal cloud development environment using a self-service golden path template

### Lab Structure

| Section | Title | Duration |
|---------|-------|----------|
| 1 | Meet the Platform — Explore Developer Hub and Lightspeed | 10 min |
| 2 | Your Mission — Create a Dev Environment via Golden Path Template | 10 min |

### Detailed Steps

1. Open the Red Hat Developer Hub URL (provided in the lab environment panel) and log in with the supplied credentials.
2. Navigate to the software catalog and locate the Parasol Insurance application entries.
3. Explore the component overview, dependencies graph, and CI/CD links visible in the Developer Hub UI.
4. Open the Lightspeed AI assistant panel and ask a question about the Parasol application architecture (e.g., "What services make up this application?").
5. Observe the AI assistant's response and confirm it references catalog metadata.
6. Navigate to the "Create" section of Developer Hub and select the Parasol development environment golden path template.
7. Fill in the template form (username, namespace, project name as guided by the lab instructions).
8. Submit the template and wait for Developer Hub to provision the development environment.
9. Confirm the new component appears in the catalog and that the Dev Spaces workspace link is available.

### Key Takeaways

- Red Hat Developer Hub provides a unified software catalog that aggregates metadata, documentation, CI/CD status, and dependency graphs for all platform services.
- The Lightspeed AI assistant is embedded directly in Developer Hub, enabling developers to ask questions about architecture and platform services without leaving the portal.
- Self-service golden path templates eliminate environment setup friction — participants go from "I need a dev environment" to "I have one" in minutes, with no platform team intervention.
- The developer portal is the entry point for the entire developer workflow in this lab.

### Infrastructure Notes

- Developer Hub must be pre-configured with the Parasol Insurance software catalog entities loaded and the Lightspeed plugin enabled.
- The golden path template must be registered in Developer Hub before the lab begins; it provisions a Dev Spaces workspace and GitLab project for each participant.
- The Lightspeed AI assistant connects to the Qwen3 235b model served via MaaS.

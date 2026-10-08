# Module 03 — App Connectivity for AI

### Brief Overview

A five-lab track that teaches participants to build AI-powered data flows using Red Hat's application connectivity tools. Starting with Apache Camel data ingestion, participants progress through Service Interconnect for cross-cluster database connectivity, Kafka-based multi-channel messaging, an agentic AI support bot with MaaS and MCP tool calling, and LLM governance via Red Hat Connectivity Link. Each lab builds on the previous one in a Parasol Insurance customer support scenario.

### Audience and Time

- **Target personas:** Application developers, integration architects
- **Experience level:** Intermediate — familiarity with REST APIs helpful; no prior Camel/Kafka experience required
- **Prerequisites for this module:** Lab environment access, Dev Spaces workspace (provisioned in Module 1 or independently)
- **Estimated duration:** 150 minutes (5 labs)

### Learning Objectives

- Build Apache Camel integrations for data ingestion with EDI-to-XML transformation
- Use Service Interconnect for secure cross-cluster database connectivity
- Bridge messaging platforms (Matrix and Rocket.Chat) via Kafka event-driven architecture
- Build an agentic AI support bot using Apache Camel with MaaS/LLM and MCP tool calling
- Govern LLM access with Red Hat Connectivity Link (API key authentication and token rate limiting)

### Lab Structure

| Lab | Title | Files | Lines | Duration |
|-----|-------|-------|-------|----------|
| Intro | Introduction + Development Environment | 2 | 465 | 15 min |
| 1 | Ingest Service | 4 | 1,854 | 40 min |
| 2 | Messaging Access | 4 | 264 | 15 min |
| 3 | Multi-channel Hub | 4 | 890 | 25 min |
| 4 | AI Customer Support | 5 (+9 figure partials) | 1,183 | 30 min |
| 5 | LLM Governance | 6 (+3 figure partials) | 1,367 | 25 min |

### Lab Details

**Intro — Introduction + Dev Environment:** Sets the Parasol Insurance scenario, introduces all technologies (Camel, Kafka, Service Interconnect, Connectivity Link, MaaS), shows full architecture diagram with Mermaid. Walks through Dev Spaces login and workspace orientation.

**Lab 1 — Ingest Service:** Builds a Camel integration that ingests EDI policy applications, transforms to XML, stores in a backend database via Service Interconnect, and generates PDF policy documents to S3 (ODF). Uses Kaoto visual editor for flow design. Heaviest lab.

**Lab 2 — Messaging Access:** Onboards participants onto Matrix (customer-facing) and Rocket.Chat (support agent) messaging platforms. Lightweight setup module establishing the multi-channel scenario for Labs 3-5.

**Lab 3 — Multi-channel Hub:** Decouples Matrix and Rocket.Chat via Kafka as streaming backbone. Introduces a common data model, builds inbound/outbound Camel flows (Kafka to Rocket.Chat), and deploys the event-driven solution on OpenShift.

**Lab 4 — AI Customer Support:** Builds an AI-powered support agent using Agentic Apache Camel with MaaS (LLM). The bot lives in Rocket.Chat, interprets natural language requests, autonomously calls tools (MCP) to query DB, update records, and regenerate policy PDFs.

**Lab 5 — LLM Governance:** Adds a governance layer via Red Hat Connectivity Link (gateway) in front of the LLM. Enforces API key authentication and token-based rate limiting across Gold/Silver tiers.

### Key Takeaways

- Apache Camel provides a low-code integration framework for complex data transformation flows
- Service Interconnect enables secure cross-cluster connectivity without exposing services publicly
- Kafka decouples messaging channels into a scalable event-driven architecture
- Agentic AI with MCP tool calling enables autonomous bot actions (DB queries, document generation)
- Connectivity Link provides governance (auth + rate limiting) for LLM endpoints without modifying application code

### Infrastructure Notes

- Dev Spaces workspace with Camel/Kaoto tooling pre-installed in devfile
- Kafka (AMQ Streams) pre-deployed on cluster
- Matrix and Rocket.Chat instances pre-provisioned per participant
- MaaS endpoint (Qwen3 235b) for AI labs
- Red Hat Connectivity Link operator installed for Lab 5
- Service Interconnect configured for cross-namespace database access

### Content Status

**Complete.** ~6,900 lines across 25+ .adoc files with its own index, tile navigation, Mermaid architecture diagrams, shared partials, and figure assets. Self-contained — can run as an independent workshop track.

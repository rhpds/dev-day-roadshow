# Module 02 — Secured Software Supply Chain

### Brief Overview

Participants secure and promote a change to Parasol Insurance using the platform's preconfigured software supply-chain controls. They create a secured sandbox, remediate dependency and container-image findings, sign commits with their own identity, and compare informational sandbox checks with enforced merge-request gates. They then examine signed build provenance, encounter a Conforma promotion failure before release approval, submit a signed approval, and promote through the GitOps manifests repository. The module ends by testing namespace admission controls against unsigned, unapproved, and legitimate production images.

The journey illustrates the guide's **SLSA Level 3** supply-chain scenario. This is a workflow and evidence-verification lab, not an operator-installation exercise or an independent SLSA certification assessment.

### Audience and Time

- **Target personas:** Developers, DevSecOps practitioners, security engineers, platform engineers, and application architects.
- **Experience level:** Intermediate; familiarity with Git, CI/CD, and container images is helpful.
- **Prerequisites:** Workshop credentials and the pre-provisioned secured Parasol environment. Module 1 is useful background, but the secured component and sandbox are separate resources.
- **Estimated duration:** **60–90 minutes**, as stated in the guide. Use **90 minutes** for scheduling; the five timed sections total 75 minutes, with allowance for SSO, analysis, builds, signing, and reconciliation.

### Learning Objectives

- Create and explore a secured development sandbox through Developer Hub.
- Use Red Hat Dependency Analytics to inspect findings and remediate framework dependencies; distinguish application dependencies from container base-image vulnerabilities.
- Sign a commit using Sigstore keyless signing and inspect the developer-identity evidence.
- Compare informational sandbox results with enforced signature and ACS merge-request checks.
- Inspect Tekton Chains image signatures and SLSA provenance, and validate promotion evidence with Conforma.
- Submit a signed release approval, follow SBOM upload to Trusted Profile Analyzer, and merge a GitOps production promotion.
- Verify that namespace admission controls enforce image signatures, signed-commit evidence, and release approval.

### Lab Structure

| Section | Guide page | Timed exercises |
|---|---|---:|
| 1 | Dealing with Vulnerabilities Early | 15 min |
| 2 | Signing Your Commits | 10 min |
| 3 | Checking the Sandbox Pipeline | 15 min |
| 4 | Moving to the Next Stages | 25 min |
| 5 | Securing Your Namespaces | 10 min |
| — | Timed exercise subtotal | **75 min** |

Introduction and environment access precede the exercises. The published overall estimate remains 60–90 minutes; pipeline and analysis waits vary.

### Detailed Steps

1. Open **Parasol Insurance (Secured)** in Developer Hub and inspect its overview, Topology, CI, and CD views.
2. Run the **Secured Parasol Insurance Development Environment** template with a short feature-branch name. Confirm the source branch, isolated sandbox, catalog component, and initial pipeline are created.
3. Open the sandbox's Dev Spaces workspace, complete the documented SSO/trust prompts, and allow the gitsign helper to start.
4. Open `pom.xml`, inspect the RHDA report and remediation suggestions, then update the Quarkus platform version using the versions in the guide. Re-analyze and compare findings rather than assuming a fixed CVE count.
5. Commit the dependency changes with gitsign, complete the Keycloak identity flow, and push. Inspect the GitLab signature badge/certificate details; GitLab's unverified badge does not itself mean Sigstore verification failed.
6. Inspect the sandbox pipeline's signature verification, Maven build, SonarQube scan, image build, ACS image scan/check, and GitLab commit report. Explain why sandbox security findings are informational.
7. Optionally push an unsigned commit on the sandbox branch and inspect its warning/report. Do not confuse this behavior with permission to promote unsigned code.
8. Inspect ACS findings from the base image, replace the root `Containerfile` base with the hardened Java 21 runtime specified in the guide, sign and push the change, and inspect the updated security results.
9. Open a source MR targeting `main`. Follow the enforced MR-check pipeline in the secured build namespace and inspect its GitLab status/comment. Failed signature or blocking ACS checks prevent merging.
10. Merge the successful signed MR and wait for the post-merge build to finish. Inspect the image signature and Chains provenance, and confirm the image is deployed to preprod before creating a release tag.
11. Create a source-repository tag and inspect the **secured tag-promote** pipeline. Its first promotion is expected to fail because the release-approval attestation is absent; other signature/provenance/security evidence must be valid.
12. Open **Release Approval** from the secured component, inspect the preprod image, and approve with a reason. Inspect the signed approval attestation and its transparency-log evidence.
13. Create a new tag or rerun promotion as described in the guide. Inspect successful Conforma validation and the SBOM link in Trusted Profile Analyzer. Distinguish informational vulnerability/SonarQube warnings from blocking violations.
14. Review and merge the generated MR in `parasol-insurance-secured-manifests`. Let ArgoCD reconcile the production image and verify the secured production rollout.
15. Test admission enforcement with an unsigned image and a signed-but-unapproved image, inspect which policies reject them, and confirm the approved production application/database remain running. Clean up only the exercise's test Deployments.

### Key Takeaways

- Shift-left dependency remediation and container base-image hardening address different sources of risk.
- Keyless signing binds a commit to an authenticated identity without a persistent developer signing key.
- Sandbox feedback is informational; promotion paths enforce security gates.
- Image signatures, build provenance, ACS/SonarQube results, SBOMs, and human approval are distinct evidence artifacts.
- A signed release approval is attached to the image and independently checked during promotion and admission.
- GitOps separates source changes from the final production-manifests approval.
- Admission policies provide a separate control when a user attempts to bypass the delivery pipeline.

### Infrastructure Notes

- **Tenant resources:** Secured source and manifests repositories, a secured Developer Hub component/template, Dev Spaces tooling, and `{user}-secured-build`, `{user}-preprod`, and `{user}-secured-prod` namespaces. Self-service adds a separate branch sandbox.
- **Shared platform:** Developer Hub, Dev Spaces, GitLab, Quay, SonarQube, OpenShift Pipelines/GitOps, Keycloak SSO, Red Hat Advanced Cluster Security, Red Hat Trusted Artifact Signer, Trusted Profile Analyzer, and the RHDA backend.
- **Signing/provenance:** gitsign, Fulcio, Rekor, TUF, and Tekton Chains. Signing and certificate identities must match the workshop's configured trust relationships.
- **Promotion:** Conforma/Enterprise Contract policy repository, SBOM generation/upload, and the Parasol Release Approval application.
- **Admission:** Policy Controller and the image-signature, signed-commit, and release-approval policies; secured production opts into enforcement through its namespace label.
- All of these controls are preconfigured for the learner. The content does not ask participants to install ZTWIM or a separate Trusted Software Factory stack.

### Verification and Content Status

**Content authored:** all seven Module 2 navigation-linked pages are present. Learner verification includes RHDA report changes, commit identity evidence, sandbox/MR results, the before/after approval outcome, the TPA SBOM link, GitOps rollout, and admission denials/acceptance.

Content completion is separate from automated acceptance. Healthcheck readiness and E2E status remain tracked independently in `publishing-house/spec.yaml`; this outline does not claim that every browser interaction or full workflow has passed E2E.

### Source Pages

- [Introduction](../../../content/modules/ROOT/pages/module-02/00-intro.adoc)
- [Environment Details](../../../content/modules/ROOT/pages/module-02/01a-environment.adoc)
- [Dealing with Vulnerabilities Early](../../../content/modules/ROOT/pages/module-02/01-vulnerabilities.adoc)
- [Signing Your Commits](../../../content/modules/ROOT/pages/module-02/02-commit-signing.adoc)
- [Checking the Sandbox Pipeline](../../../content/modules/ROOT/pages/module-02/03-sandbox-pipeline.adoc)
- [Moving to the Next Stages](../../../content/modules/ROOT/pages/module-02/04-promotion.adoc)
- [Securing Your Namespaces](../../../content/modules/ROOT/pages/module-02/05-namespace-security.adoc)

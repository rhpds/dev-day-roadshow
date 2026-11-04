# Workshop QA

The playbooks run locally in the Showroom automation runner or with
`ansible-playbook`. They require `kubernetes.core`, the Kubernetes Python client
used by that collection, and `oc`. Module 2 is implemented entirely in Ansible;
its Git/signing commands run in the existing secured development-tooling image.
The image includes gitsign but may omit cosign; E2E fetches the matching cosign
client from the cluster TAS CLI service and initializes trust before requesting
an identity. Tool-bootstrap errors are visible without credentials; later signing
failures report their command stage with known tokens/passwords redacted.
There is no separate Python test runner.

## Healthcheck

```sh
ansible-playbook qa-automation/healthcheck.yml -e @/secure/qa-inputs.yml
```

Inputs: `ocp_api_url`, `ocp_admin_password`, `tenant_user`; Showroom can instead use
its existing user data and runtime-automation service account.

The healthcheck checks the base tenant and Module 2 namespaces, applications,
pipeline/task definitions, credential secrets, Maven cache PVC, application/route
definitions, production admission opt-in, signing policies and shared security
services. Missing routes are failures, not skipped HTTP tests.

**Readiness is not exercise completion.** ArgoCD `Progressing` remains allowed.
`OutOfSync` is reported separately as a warning: shared Dev Spaces ownership can
cause it even when applications are healthy. Secured production can legitimately
be awaiting its first signed release: the initial `:1.0` Deployment is rejected
because it is not digest-pinned. The healthcheck recognizes **only that exact
Policy Controller failure**, at the current manifests revision, with exactly one
failed sync task and no other drift/conditions. In that state it reports an
expected gate instead of failing the production app or its missing Deployment.
It does not exempt other Degraded states, later release tags, missing applications,
RBAC/storage problems or failed promoted digests. Preprod is always checked
normally; an initial build/signature failure and ImagePullBackOff remain failures.
Camel's
zero-replica starting state, stopped MTA workspaces and seeded troubleshooting
faults remain unchanged.

## Module 2 E2E — disposable tenants only

```sh
ansible-playbook qa-automation/e2e-module-02.yml \
  -e @/secure/qa-inputs.yml -e module2_allow_mutations=true
```

Selecting `qa-automation/e2e.yml` (including `/stream/qa/e2e`) explicitly opts
into the full mutating suite; the orchestrator passes Module 2 consent itself.
The standalone Module 2 playbook still requires `module2_allow_mutations=true`.
Healthcheck never enables mutation consent.

Additional inputs: student `password` and `openshift_cluster_ingress_domain`
(from Showroom user data or explicit extra variables). Authentication can also
use `ocp_api_token` instead of the admin password. Keep credentials in a protected
external vars file; never commit it. Module 2 uses an isolated temporary kubeconfig
and removes it in `always`, including after failures.

### What Module 2 automates

1. Authenticate to GitLab as the student and verify the repository's MR gate and
   the production namespace's policy-enforcement label.
2. Create a unique feature branch. Render the **imported secured sandbox template**
   using the workshop's parameters, publish its GitOps repository and let ArgoCD
   create the sandbox, pipelines and webhooks. This is the backend equivalent of
   the Developer Hub self-service action, not a browser-navigation test.
3. Update the Quarkus version and hardened `Containerfile` base image specified by
   the exercises. Use the student's Keycloak ID token and real **gitsign** keyless
   signing, verify that signature, push and assert sandbox security reporting.
4. Push an unsigned negative-test commit: the sandbox must succeed and report
   `UNSIGNED`, while the enforced MR must fail specifically at signature
   verification and GitLab must refuse the merge.
5. Push a genuinely signed correction, require the MR signature and build checks
   to pass, wait for Chains signing, then test unsigned and signed-but-unapproved
   image rejection using **immutable digests**, not image tags.
6. Merge the signed source MR, verify the post-merge signature/ACS results and
   immutable image digest, wait for Chains provenance, and require a ready preprod
   application container running that exact digest before creating a release tag.
7. Create a release tag and require Conforma to reject it before approval.
8. Submit a **real signed release approval** through the approval application's
   API using the student's identity. Create another release tag; require successful
   promotion and an uploaded SBOM link from the TPA upload task.
9. Merge the exact production manifests MR. Wait for the tested digest to be
   deployed with available replicas, verify admission accepts it, and require a
   nonempty claims API response.

Pipeline checks correlate to the current commit/tag, not any historical success.
All required steps fail closed. Admission tests use **server-side Pod dry-runs**:
policy-controller versions that only validate Pods are covered without leaving
rejected test Deployments behind. The controller requires digest references, so
the MR test uses its build TaskRun digest and the unsigned nginx fixture is
resolved with `oc image info` before testing. To avoid external registry tag
resolution, supply `module2_unsigned_image=repository@sha256:<64-hex-digest>` for
a known unsigned fixture; malformed/tagged inputs fail before admission. An unrelated RBAC error, image lookup failure or
webhook timeout is not accepted as a successful negative test.

### Side effects and cleanup

The workflow changes the disposable tenant's source history, images, attestations,
release tags and production manifests. It does **not** roll back production.
It always attempts to remove its run-owned tooling pod and sandbox ArgoCD app;
the app finalizer removes the sandbox chart resources. Run-owned GitLab branches,
sandbox repository, release tags and attestations are retained for diagnosis and
are removed through normal tenant destruction. Never run against a student's
active tenant or rerun tenant repository mirror initialization to reset it.

A full run performs several builds/scans and can take over an hour. Pipeline
polling is bounded: `module2_pipeline_retries` defaults to 120 and
`module2_pipeline_delay` to 20 seconds. Override `module2_quarkus_version` only
when the exercise's current remediation version needs updating (default 3.40.1).
The public `trusted-artifact-signer` Keycloak client must retain the workshop's
configured direct-access grants; no administrator signing identity is substituted.

### Explicit manual coverage

The backend simulation does not verify browser SSO/consent dialogs, Developer Hub
catalog registration/navigation, VS Code extension rendering, RHDA vulnerability
reports/Quick Fix recommendations, or the intermediate 3.20.5 version's report.
Those require a browser-assisted test. Updating dependencies and seeing ACS
results is not claimed as validation of the RHDA UI or a fixed CVE count.

Module 1 now provisions the actual development sandbox, tests the documented
SonarQube failure and correction with source fixtures from the exercise, waits
for exact commit/tag pipelines, merges the required production GitOps MR, and
asserts real statistics JSON in dev/prod. AI backend inference is exercised; the
documented corrected-source fallback is used for repeatability. Browser catalog
registration and IDE navigation remain manual. Modules 3, 4 and 5 still have
separately identified coverage gaps; reaching them is not evidence that their
existing load simulations validate every exercise outcome.

## Offline validation (Ansible only)

```sh
yamllint -c qa-automation/.yamllint qa-automation/
ansible-playbook --syntax-check -i localhost, qa-automation/healthcheck.yml
ansible-playbook --syntax-check -i localhost, qa-automation/e2e.yml
ansible-playbook -i localhost, qa-automation/tests/regression.yml
ansible-playbook -i localhost, qa-automation/tests/startup.yml
```

The offline regression playbook invokes the same pipeline/admission assertion
helpers as E2E. It covers current versus stale builds, missing/ambiguous pipeline
results, expected failures, approved-image acceptance, policy-specific rejection,
and false positives caused by authorization errors and webhook failures. It also
checks immutable image inputs and refuses old/unready preprod images. The startup
regressions test the bounded production exception and prove preprod, missing
credentials, storage drift, unrelated failures and stale revision errors still
fail. Expected
negative assertions appear as rescued tasks; the final recap must have `failed=0`.
Offline tests do not replace running the workflow on a fresh provisioned tenant.

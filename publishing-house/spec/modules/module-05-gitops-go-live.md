# Module 05 — GitOps Promotion & Production Deploy

### Brief Overview

With the feature branch passing all quality gates, participants complete the outer loop of the developer journey: merge the feature branch into the main branch via a GitLab merge request, create a release tag, and approve the automatically generated GitOps manifests merge request in Argo CD. They then verify that the new claims statistics endpoint is live and responding correctly in the production namespace. This module closes the full software delivery cycle — from idea to production — within a single lab session.

### Audience and Time

- **Target personas:** Application developers, platform engineers
- **Experience level:** Intermediate — conceptual Git merge request familiarity helpful; no prior Argo CD experience required
- **Prerequisites for this module:** Completion of Module 04 (pipeline passing; feature branch code quality approved)
- **Estimated duration:** 15 minutes

### Learning Objectives

- Deploy a feature to production by merging a GitLab merge request and creating a release tag
- Verify the production deployment by approving GitOps manifests in Red Hat OpenShift GitOps and confirming the endpoint is live

### Lab Structure

| Section | Title | Duration |
|---------|-------|----------|
| 1 | Create and merge the feature branch merge request in GitLab | 5 min |
| 2 | Create a release tag and observe the GitOps manifests MR | 5 min |
| 3 | Approve the Argo CD sync and verify the production endpoint | 5 min |

### Detailed Steps

1. Open the GitLab URL (provided in the lab guide) and navigate to the Parasol application repository.
2. Locate the open merge request for the feature branch created during this lab.
3. Review the merge request diff to confirm the code quality fixes from Module 04 are included.
4. Merge the merge request into the main branch using the GitLab web UI (no command-line Git required).
5. Navigate to the repository's Tags section and create a new release tag (e.g., `v1.1.0`) on the main branch commit.
6. Observe that creating the tag triggers the release pipeline, which builds a new container image and opens a merge request in the GitOps manifests repository to update the image tag.
7. Open the GitOps manifests repository in GitLab and locate the automatically created merge request with the new image tag.
8. Review the manifest change (image tag bump) and merge it.
9. Open the Argo CD URL (provided in the lab guide) and log in.
10. Locate the Parasol production application in Argo CD and observe it is out-of-sync (new manifests not yet applied).
11. Sync the application (click "Sync" in the Argo CD UI) or observe that auto-sync picks up the change within the configured interval.
12. Wait for Argo CD to report the application as Healthy and Synced.
13. Access the production endpoint URL (e.g., `https://parasol.${DOMAIN}/claims/stats`) and confirm the new claims statistics JSON response is returned.
14. Reflect: the full developer journey — discover, develop, test, fix, ship — is complete.

### Key Takeaways

- GitOps separates application configuration (manifests) from application code — developers never directly apply changes to production; they update manifests and let Argo CD reconcile the desired state.
- Red Hat OpenShift GitOps (Argo CD) continuously reconciles the cluster state against the GitLab manifests repository, providing an auditable, reproducible, and self-healing production deployment.
- The full inner loop (code → build → test) and outer loop (merge → tag → manifest update → deploy → verify) complete in a single 90-minute lab session, illustrating the velocity that OpenShift's developer platform enables.
- Every step — from catalog exploration to production verification — was performed through a browser with no local tooling, demonstrating the accessibility of the OpenShift developer platform.

### Infrastructure Notes

- The release pipeline (triggered by the tag) and the GitOps manifests auto-MR mechanism must be pre-configured in the GitLab CI/CD pipeline and Tekton pipeline definitions.
- Argo CD is configured with the GitOps manifests repository and has a per-participant application targeting the participant's production namespace.
- The production namespace and its ingress route (using `${DOMAIN}`) are pre-created by the bootstrap-tenant automation; participants only trigger the image tag update.
- Argo CD sync policy may be set to auto-sync with a short interval (e.g., 3 minutes) so participants do not wait long after merging the manifests MR.

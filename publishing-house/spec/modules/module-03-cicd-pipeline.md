# Module 03 — CI/CD Pipeline & Quality Gates

### Brief Overview

With the new REST endpoint working locally, participants commit and push their code to GitLab. This triggers a Red Hat OpenShift Pipeline that runs build, test, and static analysis stages automatically. Participants observe the pipeline progress in the OpenShift console and in Developer Hub, then watch a SonarQube quality gate intentionally fail due to code smells introduced in the new endpoint. The module illustrates how automated quality gates enforce code standards before any code can be promoted.

### Audience and Time

- **Target personas:** Application developers, DevOps engineers
- **Experience level:** Intermediate — conceptual Git familiarity required; no prior OpenShift Pipelines experience needed
- **Prerequisites for this module:** Completion of Module 02 (new endpoint implemented and verified in Dev Spaces)
- **Estimated duration:** 15 minutes

### Learning Objectives

- Analyze CI/CD pipeline results in Red Hat OpenShift Pipelines and trace each pipeline stage to its outcome
- Diagnose code quality failures reported by SonarQube through the pipeline quality gate

### Lab Structure

| Section | Title | Duration |
|---------|-------|----------|
| 1 | Commit and push code from Dev Spaces | 5 min |
| 2 | Observe the OpenShift Pipeline execution | 5 min |
| 3 | Examine the SonarQube quality gate failure | 5 min |

### Detailed Steps

1. In Dev Spaces, open the Source Control panel (or use the integrated terminal).
2. Stage the changed files and commit with a descriptive message (e.g., "feat: add claims statistics endpoint").
3. Push the commit to the feature branch on GitLab.
4. Observe that a webhook triggers a new pipeline run — navigate to the OpenShift Pipelines section in the OpenShift console or Developer Hub CI/CD tab to view the pipeline.
5. Watch the pipeline stages progress in real time: clone, build, test, SonarQube scan, quality gate check.
6. Observe the pipeline fail at the quality gate stage — note the failure reason in the pipeline logs.
7. Open the SonarQube URL (provided in the lab guide) and log in.
8. Navigate to the Parasol project in SonarQube and review the code smells flagged on the newly added endpoint code.
9. Identify the specific code smell rules that caused the quality gate to fail (these are intentionally seeded in the code provided by the lab guide).
10. Note the SonarQube issue categories and severity levels for use in the next module.

### Key Takeaways

- Red Hat OpenShift Pipelines automates the build, test, and quality scan workflow on every code push — developers do not trigger pipelines manually.
- SonarQube quality gates act as a mandatory policy checkpoint; failing the gate stops the promotion process before bad code reaches staging or production.
- Observing a real pipeline failure is more instructive than observing only successes — participants see exactly what automated quality enforcement looks like in practice.
- Developer Hub's CI/CD tab provides a single view of pipeline status linked back to the catalog component, reinforcing the portal-as-single-pane-of-glass concept.

### Infrastructure Notes

- The OpenShift Pipeline (Tekton) is pre-configured with a GitLab webhook; participants do not need to configure the trigger.
- SonarQube is pre-configured with the Parasol project and a custom quality profile that enforces the code smell rules targeted in this module.
- The code snippets provided to participants in Module 02 intentionally contain code smells (e.g., cognitive complexity, duplicated code, or missing exception handling) so the quality gate fails as expected.

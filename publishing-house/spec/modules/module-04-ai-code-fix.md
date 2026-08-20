# Module 04 — AI-Assisted Code Fix

### Brief Overview

The pipeline failed because the new code contains code smells. Rather than fixing them manually, participants use the Zoo Code AI coding assistant — integrated into the Dev Spaces IDE — to identify and remediate the issues flagged by SonarQube. After applying the AI-suggested fixes, participants commit and push again and verify that the pipeline passes the quality gate this time. This module demonstrates AI-augmented developer productivity for code quality remediation.

### Audience and Time

- **Target personas:** Application developers
- **Experience level:** Intermediate — no prior AI coding assistant experience required
- **Prerequisites for this module:** Completion of Module 03 (pipeline failed at SonarQube quality gate; code smells identified)
- **Estimated duration:** 10 minutes

### Learning Objectives

- Implement AI-assisted code quality fixes using the Zoo Code coding assistant to remediate SonarQube code smells
- Verify that the CI/CD pipeline passes the quality gate after applying the AI-suggested fixes

### Lab Structure

| Section | Title | Duration |
|---------|-------|----------|
| 1 | Open Zoo Code and request code smell fixes | 4 min |
| 2 | Apply fixes, commit, push, and verify pipeline | 6 min |

### Detailed Steps

1. Return to the Dev Spaces IDE (browser-based) where the Parasol code is open.
2. Open the Zoo Code AI assistant panel within Dev Spaces.
3. Select the code section flagged by SonarQube (from the findings noted in Module 03) or paste the SonarQube issue description into the Zoo Code prompt.
4. Ask Zoo Code to suggest a fix for the identified code smells (e.g., "Fix the cognitive complexity issue in the claims statistics method").
5. Review the AI-generated suggestion — evaluate whether the fix is appropriate and does not change the endpoint's behavior.
6. Apply the suggested fix to the source file.
7. Quickly re-verify the endpoint still responds correctly (re-run or check dev mode is still running).
8. Stage and commit the fix with a descriptive message (e.g., "fix: reduce cognitive complexity in claims statistics endpoint").
9. Push the commit to the same feature branch on GitLab.
10. Navigate to the OpenShift Pipelines view and observe the new pipeline run triggered by the push.
11. Confirm that the SonarQube quality gate stage passes this time (green).
12. Optionally, open SonarQube and confirm the previously flagged code smells are resolved.

### Key Takeaways

- AI coding assistants like Zoo Code can accelerate code quality remediation — participants go from a failed quality gate to a passing one in under 10 minutes.
- AI suggestions should be reviewed rather than blindly applied; participants evaluate the fix before committing.
- The same CI/CD pipeline and quality gate that enforced the failure now confirms the fix — automation works both ways.
- Using open-source models (Qwen3 235b) via MaaS means the AI capability runs on-cluster with no data leaving the environment.

### Infrastructure Notes

- Zoo Code is installed as a plugin/extension in the Dev Spaces workspace devfile; no additional configuration is required by the participant.
- Zoo Code connects to the Qwen3 235b model served via the MaaS endpoint configured at cluster setup time.
- The lab guide provides the exact SonarQube issue descriptions to use as Zoo Code prompts, ensuring reproducible results across participants.

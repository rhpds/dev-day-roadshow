# Module 02 — Develop a Feature

### Brief Overview

Participants open their provisioned cloud development environment in Red Hat OpenShift Dev Spaces and begin writing code. They start the Parasol Insurance application in development (live reload) mode, then implement a new claims statistics REST endpoint in Java/Quarkus — editing code entirely in the browser-based IDE without installing anything locally. This module demonstrates the inner-loop developer experience on OpenShift: code, run, verify in one environment.

### Audience and Time

- **Target personas:** Application developers
- **Experience level:** Intermediate — basic REST API and Java/Quarkus familiarity helpful but not required
- **Prerequisites for this module:** Completion of Module 01 (Dev Spaces workspace provisioned and accessible)
- **Estimated duration:** 25 minutes

### Learning Objectives

- Build a new REST API endpoint in a Java/Quarkus application using Red Hat OpenShift Dev Spaces
- Verify the endpoint responds correctly in development mode before committing any code

### Lab Structure

| Section | Title | Duration |
|---------|-------|----------|
| 1 | Open Dev Spaces and explore the workspace | 5 min |
| 2 | Start the application in development mode | 5 min |
| 3 | Implement the claims statistics REST endpoint | 10 min |
| 4 | Verify the endpoint in the browser | 5 min |

### Detailed Steps

1. From Red Hat Developer Hub, click the Dev Spaces workspace link created in Module 01.
2. Wait for the Dev Spaces IDE to initialize (browser-based VS Code environment).
3. Explore the project structure — locate the Quarkus source files and the existing REST resource classes.
4. Open a terminal in Dev Spaces and run `mvn quarkus:dev` (or use the pre-configured run task) to start the application in live reload mode.
5. Confirm the application is running by accessing the provided local URL or Dev Spaces port-forward URL.
6. Navigate to the appropriate REST resource file (e.g., `ClaimsResource.java` or as specified in the lab guide).
7. Add the new claims statistics endpoint — a GET endpoint that returns JSON summary statistics — by following the step-by-step code snippets in the lab guide.
8. Save the file; Quarkus live reload will pick up the change automatically without restarting.
9. Access the new endpoint URL in the browser or a Dev Spaces terminal using `curl` to verify the JSON response is returned correctly.
10. Confirm the response matches the expected format shown in the lab guide.

### Key Takeaways

- Red Hat OpenShift Dev Spaces provides a fully configured, browser-based development environment — no local tooling installation is required.
- Quarkus's live reload capability lets developers see code changes take effect in seconds without a full rebuild or restart cycle.
- The inner loop (code → run → verify) runs entirely on the OpenShift cluster, ensuring the development environment is consistent with the target runtime.
- Participants experience that cloud-native development does not require complex local setup.

### Infrastructure Notes

- Dev Spaces workspaces are provisioned per participant by the golden path template in Module 01; each workspace has Maven and JDK pre-installed in the devfile.
- The Parasol Insurance application source code is pre-cloned from the participant's GitLab project into the workspace.
- Quarkus dev mode runs on a port exposed via the Dev Spaces port forwarding mechanism; the lab guide provides the correct URL pattern.

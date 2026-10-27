## Local validation before GitHub Actions

For meaningful code or workflow changes and before an authorized push, PR, workflow dispatch or retry, apply the available `local-ci-preflight` skill and the project's `LOCAL_VALIDATION.md` or existing equivalent. In another agent harness, follow that project contract directly; the skill is portable Markdown guidance, not a required executor.

Run applicable cheap checks first, then the build and complete affected local E2E flows. Use required CI/native profiles when platform, graphics, SDK, browser, services or environment behavior differs. Preserve existing required checks and authentic remote acceptance. Reuse commands and runtime ownership rather than creating another stack or CI implementation.

Fix locally reproducible failures before using GitHub as the next debugging iteration. Record tested inputs, commands, results and gaps. A missing required tool/profile, skipped assertion or zero tests is not a pass. For a real blocker, state the prerequisite and use a remote exception only when the task authorizes it. Preserve read-only, deployment, access, spending and release boundaries.

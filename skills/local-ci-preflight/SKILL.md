---
name: local-ci-preflight
description: Set up or run project-specific local validation before pushing code, opening a PR, or dispatching or retrying GitHub Actions. Use for local CI templates, workflow changes, and locally reproducible CI failures. Preserve read-only requests and remote deployment or acceptance gates.
---

# Local CI Preflight

Catch locally reproducible failures before spending remote CI time. Reuse real project commands and test harnesses; do not build another CI runner or require a framework migration.

## Resolve the project contract

- For setup, adapt [the project template](assets/LOCAL_VALIDATION.template.md) into existing validation documentation, or `LOCAL_VALIDATION.md` if none exists. Wire commands using existing scripts within authorized implementation scope. Merge the [agent instruction snippet](assets/AGENTS.local-validation.md) into existing guidance without replacing unrelated instructions.
- For coding or validation, read the existing contract and affected workflow revisions, then run required applicable checks. Creating documentation or changing CI is not a prerequisite to validating an otherwise ready change.
- For a read-only audit or plan, inspect and report. Do not edit, install tools, start tests or services without separate authority.
- Skill installation does not authorize portfolio-wide edits, workflow execution, deployment, protected access, or paid calls. Use the invoking task's authority; do not ask again for checks already authorized.

Inspect changed surfaces, called scripts, reusable workflows/actions, lockfiles and existing real E2E entry points. Distinguish default/integration YAML from the feature/merge-candidate revision used by a run. Follow affected producers and consumers within task scope rather than auditing unrelated projects.

When wiring the contract, make local execution and GitHub call the same authoritative script entry points. Extract inline CI commands only when needed and authorized; do not maintain parallel implementations that drift.

## Execute in dependency order

1. **Cheap preflight:** applicable workflow lint, format checks, lint, types, generated-contract drift, configuration and migration validation. Prefer check modes; do not silently rewrite inputs. Preserve existing required suites, including existing non-E2E tests. New retained behavioral coverage must follow governing E2E policy; do not bulk-delete or migrate unrelated tests.
2. **Build:** produce the affected production candidate, package or image. Reuse accepted outputs when they feed E2E. A build alone does not establish behavior.
3. **Local behavior:** use existing complete UI/API/CLI E2E flows, real local dependencies, populated fixtures, and important failure paths/boundaries. Mocked, skipped or empty-data checks cannot establish complete or live-provider acceptance.
4. **Required CI/native profiles:** match relevant OS/architecture, runtime/SDK/Java/Flutter versions, lockfiles, browser/channel, graphics driver, CI switches, build mode, workers/shards, deadlines, migrations and service settings. Identify differences instead of claiming parity. Restore task-scoped environment overrides afterward.
5. **Remote acceptance:** keep GitHub permissions, OIDC, approvals, deployment and exact-commit staging/production checks separate. Local success does not prove or waive them.

Stop dependent expensive work when a prerequisite fails. Diagnose the earliest actionable failure, fix within scope, and repeat only invalidated checks. Do not use push/dispatch/rerun as a debugging loop for a locally reproducible failure. Do not weaken assertions, remove failing tests, inflate deadlines, or substitute an easier platform merely to obtain green.

Before heavy execution, inspect the project's existing runtime and consumers. Reuse supported lifecycle entry points and recover the established environment under governing recovery limits. Start browser tests with one worker when safe capacity is unknown. Preserve shared resources/data; release only task-owned children and use ownership-scoped fixtures.

Inspect side effects before execution: a command named `test`, a container, or a local URL does not establish isolation. Scripts can deploy, mutate a shared database, send mail or call paid providers. Use known local test configuration, not production secrets or a broad GitHub token. If local provider fixtures replace remote calls, keep authentic integration acceptance as a separate requirement.

## Choose tools proportionately

- **Native commands remain the source of truth:** npm, uv, Flutter, Make, PowerShell or existing harnesses can implement the contract. Add Task only for a demonstrated entry-point problem. Do not create a custom manifest executor.
- **actionlint:** lint changed workflow definitions and their called local actions/workflows. YAML parsing or a dry run is not behavioral execution or actionlint validation. Resolve required missing prerequisites within task authority or report `BLOCKED`.
- **act:** the default optional adapter for compatible existing validation jobs. Inspect the entire selected job's `needs` closure, reusable workflows, composite actions and scripts. Allowlist validation jobs and explicit matrix selections, use realistic synthetic events and development-only configuration, and pin reviewed tools/images. A test job depending on publishing or deployment is not safe by its name. Do not replay all repository workflows by default.
- **Native and GitHub limits:** mapping an act runner label does not install that host/toolchain. Windows/macOS jobs require the matching host. Linux containers cannot establish Windows graphics, native iOS or signing parity. act does not faithfully implement concurrency, permissions, timeouts, OIDC or environment-scoped secrets. Use supported harness limits when the emulator ignores YAML limits, and preserve remote verification of these controls.
- **Dagger:** use an established or specifically approved Linux container pipeline when it provides a concrete benefit. Do not migrate a project just for preflight. Preserve existing service ownership, isolation and teardown; nested Docker, host ports, KVM and devices need proof. Local cache hits do not automatically remove hosted work or create a shared cache.
- Missing optional act/Dagger must not block equivalent direct checks. Conversely, a different native execution path does not prove a required container/native CI profile. Read current official documentation when configuring unfamiliar flags or compatibility.

References when needed: [act usage](https://nektosact.com/usage/index.html), [runners](https://nektosact.com/usage/runners.html), [unsupported behavior](https://nektosact.com/not_supported.html), [actionlint](https://github.com/rhysd/actionlint), [Dagger](https://docs.dagger.io/).

## Evidence and remote handoff

Record tested source state, profile, commands, tool versions, outcomes and remaining remote checks in the task's existing record. Use a commit SHA for committed inputs. For a dirty working tree, identify changed/untracked inputs and do not call the result a commit pass. Revalidate affected checks when source, locks, fixtures, configuration or tools change; distinguish fixture outputs from unrelated user changes.

For required local checks report `PASS`, `FAIL`, `BLOCKED`, or `NOT_APPLICABLE` with a reason. Unconfigured commands, zero tests, missing credentials, skipped assertions or unavailable required profiles are not passing coverage. Track `REMOTE_REQUIRED` separately.

When a required local check is blocked, state the exact prerequisite and what remote execution would prove. Use a remote exception only when the task or a subsequent user instruction authorizes it. Do not silently substitute GitHub or repeatedly request authority that already exists. Do not claim a blocked integration passed.

Once applicable local requirements pass, perform only already authorized push/PR/remote validation. Preserve branch/release policy and mandatory remote results. Do not disable checks or automatically cancel deployments to reduce cost. Report local results, parity gaps and remaining remote acceptance concisely; claim cost savings only from comparable measured evidence.

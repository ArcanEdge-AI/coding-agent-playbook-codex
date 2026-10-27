# Local validation contract

**Status: NOT_CONFIGURED. This template is not a passing validation result.**

Adapt this to the existing project. Replace required `NOT_CONFIGURED` values with inspected commands or concrete blockers. Use `NOT_APPLICABLE` only with a reason. Keep one authoritative contract; reuse scripts rather than introducing another test implementation or CI runner.

## Project boundaries

| Field | Project value |
|---|---|
| Repository root and affected packages/services | NOT_CONFIGURED |
| Existing validation documentation and commands | NOT_CONFIGURED |
| Authoritative workflow paths and revision/ref | NOT_CONFIGURED |
| Actual integration/production branches | NOT_CONFIGURED |
| Supported shells, OS and architecture | NOT_CONFIGURED |
| Toolchain versions and locked install command | NOT_CONFIGURED |
| Local service lifecycle and readiness proof | NOT_CONFIGURED |
| Fixture ownership, reset and teardown | NOT_CONFIGURED |
| Shared resources that must be preserved | NOT_CONFIGURED |
| Credential and external-provider boundary | NOT_CONFIGURED; no production secrets by default |

Inspect commands and callees for side effects before enabling them. Separate local fixtures from shared databases, provider sandboxes, notifications, publishing and paid APIs. Honor the invoking task's authority and read-only boundaries.

## Profiles and dependencies

Names below describe the contract, not scripts that already exist. Adapt the project's existing conventions.

| Profile | Required purpose | Exact entry point | Prerequisite |
|---|---|---|---|
| Fast | Applicable format check, lint, types, workflow lint and generated/config/contract drift | NOT_CONFIGURED | Inspected toolchain/dependencies |
| Build | Affected production candidate/package/image checks | NOT_CONFIGURED | Fast passes |
| Local E2E | Complete affected UI/API/CLI flows, populated local dependencies, important failures/boundaries | NOT_CONFIGURED | Fast/build and scoped services ready |
| CI parity | Reproduce relevant CI OS/SDK/browser/environment behavior | NOT_CONFIGURED | Matching environment available |
| Native/device | Required graphics, desktop, Android, iOS or native packaging checks | NOT_CONFIGURED | Appropriate host/device and authority |
| Remote acceptance | GitHub controls and deployed-environment evidence | NOT_CONFIGURED; separate from local umbrella command | Applicable local checks pass or an authorized exception |

Normal sequence: Fast -> Build -> applicable Local E2E / CI parity / Native profiles. Stop dependent expensive checks after a prerequisite fails. Never invoke remote acceptance, deployment or publication from the local umbrella command.

Preserve existing required checks. Map still-required assertions before changing coverage. Newly retained behavioral tests follow the governing E2E policy; a happy-path smoke is insufficient replacement for important failure coverage.

## Select checks by changed surface

| Changed surface | Applicable checks to configure | Scope boundary |
|---|---|---|
| Prose-only documentation | NOT_CONFIGURED; relevant documentation checks | App/device/DB suites need a real dependency |
| Workflow/composite action/reusable workflow/CI script | NOT_CONFIGURED; actionlint and meaningful safe execution | Syntax does not prove events, permissions or approvals |
| Web/application/runtime | NOT_CONFIGURED; fast, build, complete affected flows | Identify browser/graphics requirements |
| API/shared types/cross-package contracts | NOT_CONFIGURED; producer and affected consumer flows | Generated-file presence alone is not behavior proof |
| Database/schema/migrations | NOT_CONFIGURED; disposable local DB and affected flows | No shared-data reset or protected release replay |
| Dependencies/toolchain | NOT_CONFIGURED; locked installs and affected builds/flows | Preserve checks regardless of PR author |
| Native/mobile/graphics | NOT_CONFIGURED; matching platform/profile | Linux containers cannot establish Windows/macOS/device parity |

## CI parity matrix

Populate relevant dimensions from actual workflow/configuration, not runner labels. Mark irrelevant dimensions not applicable with a reason.

| Dimension | GitHub setting | Local setting/proof | Remaining gap |
|---|---|---|---|
| Runner OS/image and architecture | NOT_CONFIGURED | NOT_CONFIGURED | NOT_CONFIGURED |
| Runtime, SDK, Java, Flutter, Node, Python | NOT_CONFIGURED | NOT_CONFIGURED | NOT_CONFIGURED |
| Lockfiles/install flags/generated artifacts | NOT_CONFIGURED | NOT_CONFIGURED | NOT_CONFIGURED |
| CI switches, feature flags and build mode | NOT_CONFIGURED | NOT_CONFIGURED | NOT_CONFIGURED |
| Browser binary/channel/version and viewport | NOT_CONFIGURED | NOT_CONFIGURED | NOT_CONFIGURED |
| GPU/software renderer and launch flags | NOT_CONFIGURED | NOT_CONFIGURED | NOT_CONFIGURED |
| Workers/shards/deadlines/retries | NOT_CONFIGURED | NOT_CONFIGURED | NOT_CONFIGURED |
| Schema/migrations and populated fixtures | NOT_CONFIGURED | NOT_CONFIGURED | NOT_CONFIGURED |
| Networking, callbacks, mail and providers | NOT_CONFIGURED | NOT_CONFIGURED | NOT_CONFIGURED |
| Device/emulator/virtualization/resources | NOT_CONFIGURED | NOT_CONFIGURED | NOT_CONFIGURED |
| GitHub event/merge candidate/protected controls | NOT_CONFIGURED | Synthetic input / REMOTE_REQUIRED | NOT_CONFIGURED |

If `CI` selects a software graphics driver, a native-GPU run covers only the developer profile. Use the matching profile rather than another OS container. Do not relax assertions or deadlines to hide a disagreement. Restore task-scoped environment overrides afterward.

## Optional workflow emulation

Use direct commands first. For act, configure a validation-only allowlist after inspecting the selected job's full dependency closure, reusable workflows, composite actions and scripts.

| Field | Approved local configuration |
|---|---|
| act version and pinned image/native host | NOT_CONFIGURED |
| Allowed workflow/job IDs and full dependency closure | NOT_CONFIGURED |
| Event fixture and explicit matrix selection | NOT_CONFIGURED |
| Development-only configuration/credential boundary | NOT_CONFIGURED |
| Supported timeout/resource controls outside ignored YAML settings | NOT_CONFIGURED |
| Exact reviewed invocation | NOT_CONFIGURED |
| Remaining GitHub control-plane proof | REMOTE_REQUIRED: permissions, OIDC, environment approval/secret scoping and other relevant unsupported behavior |

Do not replay all workflows or pass production secrets to make emulation work. A test job may depend on a publish/deploy job. Native mode requires the matching host/tools. act does not establish GitHub concurrency, permission, timeout or approval semantics.

If Dagger already exists or is specifically adopted, record its module/version, command, service ownership, cache policy and teardown. Do not migrate simply to fill out this file. Docker sockets, host ports, KVM and devices need explicit compatibility proof.

## Runtime and failure handling

- Reuse the established environment and supported lifecycle. Inspect running/stopped/unhealthy resources and consumers before creating/restarting anything. Follow governing recovery limits; an unreachable backend is not proof that no stack exists.
- Use one browser-test worker while safe capacity is unknown. Justify additional concurrency by the scenario and available capacity.
- Reproduce the earliest actionable failure locally. Fix within scope and rerun only invalidated checks. Do not send each attempt through GitHub while it is locally reproducible.
- Missing tools, unconfigured required commands, unready services, wrong platforms, skipped assertions and zero tests are not passes. Missing optional act/Dagger does not block equivalent direct checks, but required CI-profile gaps remain explicit.
- Preserve shared services/data and unrelated edits. Release only task-owned test children, restore environment overrides and report blocked teardown.

## Evidence and remote handoff

Add results to the task's existing record. Record the source state actually consumed; a dirty working tree is not a tested commit. Revalidate affected checks after source/lock/config/fixture/tool changes.

| Check/profile | Source state / changed inputs | Command and tool versions | Result | Evidence/gap |
|---|---|---|---|---|
| Required local checks | NOT_CONFIGURED | NOT_CONFIGURED | BLOCKED until configured and executed | NOT_CONFIGURED |
| Remote acceptance | Intended exact commit or merge candidate | NOT_CONFIGURED | REMOTE_REQUIRED | What local checks cannot establish |

Local outcomes: `PASS`, `FAIL`, `BLOCKED`, `NOT_APPLICABLE` with a reason. Track `REMOTE_REQUIRED` separately. Do not silently substitute GitHub for a blocked local check. State the blocker, remote proof and applicable authority; do not request the same permission again when it already exists.

After applicable local requirements pass, perform only authorized push/PR/remote verification. Local success does not waive mandatory CI, authorize deployment, or establish staging/production acceptance. Report runtime estimates separately from actual billing.

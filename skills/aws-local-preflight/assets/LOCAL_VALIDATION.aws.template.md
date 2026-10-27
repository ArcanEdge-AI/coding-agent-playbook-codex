# AWS local validation supplement

**Template status: NOT_CONFIGURED. This is not a validation result.**

Merge the applicable sections into the project's existing local validation contract. Use the base template supplied by `local-ci-preflight` when a contract does not exist. Replace required `NOT_CONFIGURED` values with inspected facts/commands or concrete blockers. Use `NOT_APPLICABLE` only with a reason. These tables document existing entry points; they are not an executable manifest.

## AWS scope and tooling

| Field | Project value |
|---|---|
| Complete business workflows and affected entry points | NOT_CONFIGURED |
| SDKs/versions, client factories and infrastructure definitions | NOT_CONFIGURED |
| Moto released version and locked install, or pinned image digest | NOT_CONFIGURED |
| Same-release coverage/source links and date checked | NOT_CONFIGURED |
| Additional free tool/version and demonstrated gap it solves | NOT_CONFIGURED; use Moto Server by default |
| Existing runtime identity, owners/consumers and lifecycle/readiness commands | NOT_CONFIGURED |
| Region, dummy account and credential-source isolation | NOT_CONFIGURED |
| Task-owned fixture namespace, targeted reset and teardown | NOT_CONFIGURED |
| Shared resources/data and other chats' services to preserve | NOT_CONFIGURED |

## Operation and handoff coverage

Use one row for each required operation/behavior, including indirect provisioning and credential calls when applicable. Add rows for cross-service delivery. A service or operation checkbox alone does not prove parameters, response fields, errors or integration semantics.

| Workflow / caller | Service + exact operation or handoff | Required parameters, fields, errors and semantics | Pinned-release evidence / limitations | Local check + observed outcome | Gap/result |
|---|---|---|---|---|---|
| NOT_CONFIGURED | NOT_CONFIGURED | NOT_CONFIGURED | NOT_CONFIGURED | NOT_CONFIGURED | BLOCKED until established |

If a required behavior is unsupported, record `BLOCKED` with the missing prerequisite or `REMOTE_REQUIRED` with the exact proof needed. Continue independent safe checks. Neither outcome authorizes cloud execution or a paid fallback.

## Endpoint isolation

Include every SDK/client, fixture/cleanup process, worker, browser URL consumer and Lambda/SAM child container. Use separate rows where network namespaces or endpoint precedence differ.

| Caller + SDK/version | Override mechanism + precedence | Allowed effective host/port from this caller | Credential/region settings | Request-destination proof and enforcement | Missing/conflicting override + server unavailable checks |
|---|---|---|---|---|---|
| NOT_CONFIGURED | NOT_CONFIGURED | NOT_CONFIGURED | NOT_CONFIGURED | NOT_CONFIGURED | BLOCKED until fail-closed behavior is verified |

Record S3 path/virtual-host addressing, DNS, browser-reachable presigned URL origin, CORS behavior and child-container routing where used. Dummy credentials are not an endpoint guard. Verify no AWS fallback on all selected paths, including retries and generated resource URLs. Keep evidence free of secrets and signed URLs. If the boundary cannot be proved, do not run dependent AWS-capable checks.

## Existing profile additions

Add AWS requirements to existing profiles rather than creating a parallel runner. Isolation applies before any AWS-capable command.

| Existing profile | AWS addition / exact existing command | Required input and observable acceptance |
|---|---|---|
| Fast | NOT_CONFIGURED; static configuration/endpoint checks, infrastructure syntax, lint/types | Safe configuration; no provider lookups/deploys |
| Build | NOT_CONFIGURED; affected package/runtime build | Fast passes; known source/toolchain |
| Local E2E | NOT_CONFIGURED; complete UI/API/CLI entry points | Build, isolation and populated owned fixtures ready |
| CI parity | NOT_CONFIGURED; relevant runtime/SDK/service settings | Matching versions/profile; explicit differences |
| Remote acceptance | NOT_CONFIGURED; outside local commands | REMOTE_REQUIRED; exact separate authority and proof |

## Behavioral cases

Use real application paths. A direct SDK probe establishes emulator compatibility only. Inject failures through the existing local harness without replacing the application under test; distinguish injected behavior from real provider semantics.

| Case | Entry point + populated fixture | Expected output and persisted/downstream effect | Deadline/retry bound | Result/evidence |
|---|---|---|---|---|
| Complete supported business workflow | NOT_CONFIGURED | NOT_CONFIGURED | NOT_CONFIGURED | BLOCKED until executed |
| Invalid/missing data and relevant boundaries/pagination | NOT_CONFIGURED | NOT_CONFIGURED | NOT_CONFIGURED | BLOCKED or reasoned NOT_APPLICABLE |
| Local dependency failure and retry exhaustion/recovery | NOT_CONFIGURED | NOT_CONFIGURED | NOT_CONFIGURED | BLOCKED until executed |
| Duplicate delivery/replay and idempotency, where applicable | NOT_CONFIGURED | NOT_CONFIGURED | NOT_CONFIGURED | BLOCKED or reasoned NOT_APPLICABLE |
| Missing/conflicting endpoints and unavailable local service | NOT_CONFIGURED | Reject safely before external calls; no AWS fallback | NOT_CONFIGURED | BLOCKED until verified |
| Managed event path or explicitly identified injected seam | NOT_CONFIGURED | Confirm actual consumer execution and resulting state | NOT_CONFIGURED | BLOCKED or REMOTE_REQUIRED for unproved handoffs |

## Evidence and disposition

Record the tested source/dirty inputs, exact profile/commands, pinned versions, fixtures, endpoint enforcement/observations and assertions in the existing validation record. Restore task-scoped environment overrides and remove only owned fixtures/temporary children. Global Moto reset requires exclusive ownership of all state. Preserve shared services and data; report any blocked teardown by identifier and next step.

| Required remote proof | Reason local evidence is insufficient | Authorized next step |
|---|---|---|
| Actual IAM/VPC/managed triggers, quotas/performance, deployed or provider behavior relevant to this project | Emulation cannot establish cloud equivalence | REMOTE_REQUIRED; no automatic AWS calls, dispatch or deployment |

Local results use `PASS`, `FAIL`, `BLOCKED`, or reasoned `NOT_APPLICABLE`. Keep `REMOTE_REQUIRED` distinct. Unconfigured/skipped/empty checks cannot pass. Report cost estimates separately from functional outcomes and measured billing.

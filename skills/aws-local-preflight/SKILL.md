---
name: aws-local-preflight
description: Set up or run local functional preflight for AWS-dependent applications with Moto Server before cloud execution. Use for AWS API coverage mapping, local endpoint isolation, and AWS additions to a project's local validation contract. Cloud cost estimation and deployed acceptance remain separate.
---

# AWS Local Preflight

Use free tools to catch AWS-dependent application failures locally. Default to Moto Server, which exposes HTTP endpoints usable by normal AWS SDKs across languages. Verify required operations and integrations for the project's pinned release; a listed service is not a coverage guarantee.

## Fit the existing contract

Load `local-ci-preflight` and its project-contract template from that skill's own package. Reuse its commands, profile ordering, runtime lifecycle and evidence model. If that prerequisite is unavailable, report it and continue independent read-only mapping; do not invent another CI runner.

For authorized setup, merge the [AWS supplement](assets/LOCAL_VALIDATION.aws.template.md) into the existing `LOCAL_VALIDATION.md` or equivalent. Create the base contract with `local-ci-preflight` only when none exists. Keep one authoritative contract and existing script entry points. For an already configured run, inspect that contract without requiring a documentation rewrite.

Use the invoking task's authority. Read-only audits and plans do not authorize installation or execution. Creating or installing this skill does not authorize application rollout, emulator replacement, Docker/WSL startup, AWS sign-in, real AWS calls, paid tools, subscriptions, budgets, remote CI, publication or deployment. When project execution is authorized, inspect commands and their callees before running them.

## Map the actual application

Inspect affected entry points, manifests/lockfiles, SDK client factories, configuration, workers, infrastructure definitions and existing E2E flows. Follow the complete business workflow through its AWS consumers and observable result. Include indirect clients, credential providers, fixture loaders, cleanup tools, browser uploads and child processes.

Record each required service, exact API operation, important request parameters/response fields, region/account assumptions, SDK version, and cross-service handoff. Distinguish provisioning APIs from runtime APIs. Do not run infrastructure deployment, refresh, plan or synthesis commands without checking for provider lookups and other external side effects.

Before selecting or changing tools, read [Moto coverage and endpoint boundaries](references/moto-boundaries.md). Use available AWS documentation tools first where supported, then current primary documentation. Pin a released Moto package version or image digest, record SDK/tool versions, and compare the same release's docs/source with the required behavior. `/latest/` and development branches can describe unreleased features. Probe uncertain required behavior locally only within an isolated, authorized environment.

Choose SAM CLI or DynamoDB Local only for a demonstrated gap they address. Reuse an existing suitable environment instead of migrating it merely to adopt this default. Unsupported required behavior is `BLOCKED` or `REMOTE_REQUIRED`; never silently switch to AWS or a paid product.

## Establish isolation before execution

Dummy credentials do not prevent requests from reaching AWS. Before running any AWS-capable profile, including fixture setup and cleanup:

- Verify the endpoint override supported by every selected SDK/version and its precedence. Trace the effective destination for each client and process; setting `AWS_ENDPOINT_URL` alone is insufficient evidence.
- Use development-only credentials and controlled credential sources. Prevent profile, SSO, metadata, web-identity or assume-role paths from contacting external services. Keep region/account values consistent with fixtures.
- Require a local-only mode that rejects missing or unapproved endpoints before a request. Allowlist exact local hosts/ports for the verified topology; validate final resolved destinations, redirects, generated URLs and service discovery. Cover host applications, browsers, workers and Lambda/SAM child containers.
- Verify both normal routing and negative cases: missing overrides, conflicting configuration and unavailable local services must fail closed with no AWS fallback. Capture sanitized request-destination evidence for all selected callers. Use scoped outbound restrictions or equivalent transport enforcement where needed; do not change machine-wide networking or shared services without authority. If isolation cannot be established, mark execution `BLOCKED`.

Resolve S3 addressing, presigned URL consumers and child-container networking using the boundary reference. A local health response, container presence or dummy access key does not establish isolation or application behavior.

## Validate complete local flows

Follow the base contract: cheap configuration/lint/type checks, then the affected build, then complete UI/API/CLI flows. Cheap checks must also have safe configuration. Stop dependent execution after a failed prerequisite.

Inspect existing resources and consumers before starting services. Reuse supported project lifecycle commands, verified versions and bounded readiness/recovery limits. Preserve other chats' services and shared data. Use task-owned fixture identifiers and targeted cleanup; Moto's global reset is unsafe on a shared server.

Seed populated fixtures and exercise real application entry points against the selected local services. Check user-visible output and persisted/downstream effects, not only successful API status codes. Cover meaningful invalid/missing data, boundaries, pagination where used, bounded retries/timeouts, duplicate messages and idempotency where applicable. Verify actual workers execute and asynchronous effects settle within explicit deadlines.

For a supported managed handoff, assert the complete local path. If events must be delivered manually, label the injected seam and test the consumer through its supported entry point; that does not pass the complete managed workflow. A stubbed Lambda response or disabled function execution is not evidence that the function ran. Preserve uncovered handoffs as gaps.

## Report evidence and limits

Use the existing validation record: source state, profile/commands, pinned tools, coverage matrix, endpoint proof, populated fixtures, actual assertions/results, remaining gaps and resource disposition. Revalidate affected evidence after source, SDK, emulator, fixture or configuration changes.

Use `PASS`, `FAIL`, `BLOCKED` or `NOT_APPLICABLE` with a reason for local checks; track `REMOTE_REQUIRED` separately. Missing commands, unsupported parameters, skipped assertions and empty fixtures are not passes. A passing supported subset cannot pass a required workflow with an uncovered seam.

Moto proves only the local functional behavior exercised. It does not establish actual IAM enforcement, VPC networking, managed trigger delivery, quotas, performance, deployed acceptance or real provider behavior. Preserve required cloud acceptance and its authorization boundary. Keep cost estimation separate; local success does not predict AWS bills or prove measured savings.

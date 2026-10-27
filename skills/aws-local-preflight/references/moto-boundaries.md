# Moto coverage and endpoint boundaries

Read this before choosing the local profile or executing AWS-capable commands. Use available AWS documentation tools where supported; use primary web sources when those tools cannot answer the question.

## Tool choice and release evidence

- **Default: Moto Server.** Its standalone HTTP mode supports normal AWS SDK clients across languages. Python is an option for hosting the server, not a requirement for the application language. Moto uses the [Apache-2.0 license](https://github.com/getmoto/moto/blob/5.2.4/LICENSE); this skill distributes instructions, not Moto itself.
- **Pin and verify.** Record a released package version with locked dependencies, or a reviewed image tag and digest. The [release list](https://github.com/getmoto/moto/releases) and [repository](https://github.com/getmoto/moto) establish provenance. Prefer the project's compatible pin; do not select a development build merely because `/latest/` documents a needed feature.
- **Versioned evidence.** The [server guide](https://docs.getmoto.org/en/latest/docs/server_mode.html) and [service index](https://docs.getmoto.org/en/latest/docs/services/index.html) are discovery aids. Inspect the displayed documentation version. If a release-specific rendered page is unavailable, use that tag's documentation, implementation and tests. For example, release [5.2.4](https://github.com/getmoto/moto/releases/tag/5.2.4) has [server documentation](https://github.com/getmoto/moto/blob/5.2.4/docs/docs/server_mode.rst) and [service documentation](https://github.com/getmoto/moto/tree/5.2.4/docs/docs/services). Replace this example tag with the actual project pin when mapping coverage.
- **Coverage is granular.** Check request parameters, returned fields, validation/errors, pagination, consistency and asynchronous semantics used by the application. Operation support does not imply all options work. For example, the [5.2.4 S3 notes](https://github.com/getmoto/moto/blob/5.2.4/docs/docs/services/s3.rst) list restrictions on supported operations and notification targets/events. Test the actual handoff and resulting state rather than inferring it from two supported services.
- **Free additions need a purpose.** [SAM CLI local testing](https://docs.aws.amazon.com/lambda/latest/dg/testing-guide.html) can address a Lambda runtime/event-processing gap; [DynamoDB Local](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocal.html) can address an identified DynamoDB behavior gap. Verify the selected tool/version actually covers it. SAM does not redirect a function's AWS calls automatically. Avoid deploy/watch/sync commands in a local-only profile. Do not install or replace an established stack just to standardize tools.

## Endpoint boundary by caller

Use the selected SDK's official version documentation and [AWS endpoint settings guide](https://docs.aws.amazon.com/sdkref/latest/guide/feature-ss-endpoints.html). Environment-override support differs by SDK and version. Where supported, explicit client/code settings outrank service-specific environment values, which outrank the global environment value. Inspect shared configuration and settings that ignore configured endpoints as well. Pass an explicit local endpoint through the application's established client factory when the SDK requires it; a process environment variable cannot redirect arbitrary HTTP clients.

Validate the effective destination before network use. Treat the local-only switch as a project contract that must be implemented or verified, not as an AWS-standard setting. Require an approved local scheme/host/port for each selected client, and reject missing or conflicting configuration. Prevent fallback to default AWS endpoints on connection failures. Match resolved addresses and any redirects/generated URLs to the approved topology rather than trusting a hostname substring such as `localhost`.

Use dummy static credentials and explicit fixture regions. Isolate task configuration from real profiles, tokens and credential-provider chains; signing failures at AWS would still mean an external request occurred. Inspect startup/account probes, STS calls, web identity, SSO, metadata access, scripts and subprocesses. Apply endpoint guards there too. Never use an AWS identity call as a local readiness check.

Verify routing with sanitized client transport/connection evidence and local server observations for each caller and important path. Include failure/retry paths. Run missing-override and unavailable-service cases only with outbound enforcement already in place; the guard must reject or contain the request, never test isolation by contacting AWS. Server logs alone do not show requests that escaped elsewhere. Use existing scoped network or transport controls, including equivalent coverage for child processes; an ordinary container network is not inherently offline. If adequate proof is unavailable, report `BLOCKED` rather than enabling permissive defaults.

## S3 and generated URLs

Check the actual SDK's path-style/virtual-host configuration, Moto's selected-version host parsing, DNS and region settings. A client using virtual-host addressing may request `bucket.localhost` or a container alias with a bucket prefix. Do not mechanically interchange `localhost`, a loopback IP and a service alias. Prefer path-style access for a local profile when compatible; verify the complete application behavior.

Trace presigned URLs from creation to the browser/worker consuming them. The signed origin must be both reachable by that consumer and approved locally. Rewriting the host after signing can invalidate the signature. Assert the actual upload/download and stored content through the user flow. Keep full signed URLs out of logs. Verify needed CORS behavior explicitly: Moto's [S3 configuration](https://docs.getmoto.org/en/latest/docs/services/s3.html) may be more permissive than the deployed bucket.

Also inspect generated SQS queue URLs, service-returned endpoints and HTTP callbacks. Contain these destinations before following them; the initial SDK endpoint alone may not control subsequent requests.

## Workers, Lambda and event seams

`localhost` inside a container identifies that container. Determine the endpoint reachable from each worker/function and configure its own SDK credentials, region and supported override. Verify Moto's selected-version endpoint injection/container settings instead of assuming the host environment reaches children. Scope ports and network access to the intended local environment.

Moto can execute Lambda code through child containers, depending on configuration. Its [configuration guide](https://docs.getmoto.org/en/latest/docs/configuration/index.html) explains that disabling Docker execution assumes success without executing the function. The [5.2.4 Lambda notes](https://github.com/getmoto/moto/blob/5.2.4/docs/docs/services/lambda.rst) also describe static invocation responses and unsupported behavior. Check the pin and prove function side effects; an `invoke` response alone is insufficient.

Do not assume a created event-source mapping or notification rule causes authentic delivery. Exercise the supported local producer-to-consumer path and observe its outcome. Manual event injection can establish consumer behavior through a supported entry point, but leaves managed delivery `REMOTE_REQUIRED` or the complete local path `BLOCKED`. Label any synthetic envelope, error injection or delivery adapter and retain its coverage limitation.

## Ownership and acceptance

Inspect and reuse the project's established environment and lifecycle commands before creating anything. A shared Moto server contains shared state: the reset API clears all backends, and decorator/server combinations can reset the same state. Use owned resource names and exact-resource cleanup. Use global reset only when the entire instance and its state are exclusively task-owned. Restore environment changes and release only task-owned resources; preserve other chats' processes and shared data.

[AWS testing guidance](https://docs.aws.amazon.com/lambda/latest/dg/testing-guide.html) distinguishes local feedback from testing actual managed behavior. Keep IAM enforcement, VPC networking, trigger delivery, quotas, performance and deployed/provider acceptance outside Moto's proof. Even complete local workflows require the project's separate authorized cloud acceptance. Estimating cloud cost is a different task; Moto results do not quantify the future AWS bill.

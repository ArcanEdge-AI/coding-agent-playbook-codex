# Testing Strategy

## Test Commands

Document targeted and full E2E commands, plus build, lint, type checking, and static validation commands.

State which checks are mandatory, which changes trigger broader checks, and when accepted results can be reused. Start with the smallest meaningful checks and run affected required gates after the final relevant change; avoid full-suite runs after every small edit.

## Retained Test Policy

Retain only end-to-end (E2E) behavioral tests. Do not retain unit or isolated integration suites. Exercise complete supported flows through real UI, API, or CLI entry points, relevant dependencies, and observable results such as persistence or user-visible state. Direct helper calls and mocked internal flows do not count as E2E evidence.

Build, lint, type checking, and static validation remain appropriate checks. Visual or snapshot assertions may be part of an E2E flow; they do not establish the entire flow by themselves.

## Test Conventions

Document E2E naming, structure, fixtures, environment setup, dependency boundaries, and disposable test-data cleanup.

Reuse or extend existing E2E coverage for intended final behavior, important business rules, meaningful failures, boundary cases, and realistic regression risks. Do not add a permanent test for every helper or partial implementation.

## Runtime Reuse and Concurrency

Document the established environment identity, supported recovery commands, test-isolation requirements, browser-test worker limits, and how to account for known overlapping heavy jobs on the same host. Apply the global runtime lifecycle rules; discover stopped and unhealthy prior-session resources as well as running ones. A new test invocation or retry does not by itself require a new browser, container stack, or virtualized environment.

- Reuse a compatible eligible browser instance through supported tools. Use fresh isolated contexts when clean test state is required and the tool supports them; do not carry cookies, authentication, or mutable state across isolation boundaries. Preserve the runner's required lifecycle when it cannot reuse an existing browser.
- Start with one browser-test worker when safe capacity is unverified or heavy jobs already overlap, unless the required test scenario needs more. Increase concurrency only for an identified need and verified capacity. Coordinate or serialize browser suites, image builds, and other heavy validation; do not change another owner's jobs without authority.
- Before reusing a container or image, verify project and service ownership, current source or image identity, configuration, ports, mounts, data, and health. Start or recover the existing project environment before considering a replacement, including when an earlier session created it. Use an isolated resource when shared mutable state would contaminate tests. Update or recreate an affected service under the established project identity when needed to test current inputs; preserve required data first. Stale runtime state is not current E2E evidence.
- Reuse valid images and build caches. Record any required fresh build or additional runtime in the existing task record. Ensure teardown closes task-owned temporary resources after both passing and failing runs without stopping shared services or deleting persistent data.

### Docker and WSL Recovery Example

Adapt this example to the repository's actual launcher, installed tools, and authority. Do not run host-wide recovery merely because a test failed.

1. Resolve the existing Docker context, project name, configuration files, services, data mounts, and registered WSL distribution. Inspect stopped containers and distributions as well as running ones. A daemon connection error does not establish that no environment exists; do not respond by choosing a new context, project suffix, port range, or distribution.
2. Use the project's lifecycle launcher when available. Otherwise, target the verified existing project and services: [Compose start](https://docs.docker.com/reference/cli/docker/compose/start/) starts existing containers; [Compose restart](https://docs.docker.com/reference/cli/docker/compose/restart/) restarts services but does not apply configuration changes. Recover the existing Docker engine through its supported controls if it is the failed dependency.
3. When an image or configuration change requires recreation, use the established project and configuration with [Compose up](https://docs.docker.com/reference/cli/docker/compose/up/), preserving or migrating required data first. This is a controlled update of the existing environment, not permission to create parallel stacks. Images are build artifacts, not processes that can be restarted.
4. Use [WSL's installed-distribution inventory and lifecycle commands](https://learn.microsoft.com/en-us/windows/wsl/basic-commands) to start the registered distribution, or terminate and relaunch the affected distribution when its consumers and restart authority are verified. Prefer supported Docker controls for a Docker-managed backend. A WSL-wide shutdown stops all running distributions and its utility VM: establish the impact and obtain authority for unrelated or unresolved disruption before using it.
5. Follow the global recovery allowance and bounded readiness waits; verify the same environment after recovery. Do not install or import another distribution, unregister an existing one, delete its virtual disk, reset data, or prune volumes as a workaround for a startup failure. If recovery is blocked, stop and report the blocker instead of multiplying environments.

## Temporary Unit Tests and Cleanup

Every unit test created is temporary, regardless of its purpose or who creates it. None may remain in a completed change. Unit tests may guide development or diagnosis; map their still-required behavioral assertions to corresponding E2E cases. Once those cases pass, remove all created unit tests and any fixtures, mocks, helpers, or dependencies used only by them before completing the change. Do not remove support code still used by E2E tests or production. Classify tests by exercised behavior, not filenames or labels; renaming a unit test does not make it E2E.

Migrate existing non-E2E suites only within authorized scope after replacement coverage passes. Investigate failing tests before removal; do not weaken required assertions or disable repository gates to obtain a pass. If E2E execution is unavailable or blocked, report the gap and unfinished cleanup rather than treating unit coverage as the completed solution.

As the implementation changes, update, consolidate, or remove E2E tests and fixtures that only preserve abandoned fixes. Preserve still-required assertions and explicit coverage gates.

## Regression Testing

For bugs, prefer an E2E reproduction or regression test when feasible. Verify the actual success, failure, and boundary outcomes affected by the fix.

## Snapshot Rules

Do not update snapshots blindly. Inspect diffs and confirm they match intended behavior.

## Known Constraints

Document slow tests, flaky tests, unavailable environments, or validation gaps.

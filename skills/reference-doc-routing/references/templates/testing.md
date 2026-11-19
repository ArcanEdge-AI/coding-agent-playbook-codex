# Testing Strategy

## Test Commands

Document targeted and full E2E commands, plus build, lint, type checking, and static validation commands.

State which checks are mandatory, which changes trigger broader checks, and when accepted results can be reused. Start with the smallest meaningful checks and run affected required gates after the final relevant change; avoid full-suite runs after every small edit.

## Retained Test Policy

Start with zero new permanent tests. Retain end-to-end (E2E) behavioral tests by default. Exercise supported flows through real UI, API, CLI, or other supported entry points, relevant dependencies, and observable results such as persistence or user-visible state. For each proposed case, name a credible wrong result the remaining checks would accept and the requirement it would violate.

Document any explicit repository policy permitting a lasting focused test for a specified rule impractical to exercise adequately through a supported entry point. Record the applicable rule and reason only for an actual maintainer decision. This template grants no exception. A focused test supplies evidence for its named rule, and the full user flow still requires its applicable checks.

Build, lint, type checking, and static validation remain appropriate checks. Visual or snapshot assertions may be part of an E2E flow; they do not establish the entire flow by themselves.

## Test Conventions

Document E2E naming, structure, fixtures, environment setup, dependency boundaries, and disposable test-data cleanup.

Reuse or extend existing E2E coverage for intended final behavior, important business rules, meaningful failures, boundary cases, and realistic regression risks. Do not add a permanent test for every helper or partial implementation.

## Runtime Reuse and Concurrency

Document the established environment identity, supported recovery commands, test-isolation requirements, browser-test worker limits, and how to account for overlapping heavy jobs on the host. Use the shared runtime guidance in the installed `reference-doc-routing` skill. Discover stopped and unhealthy prior-session resources as well as running ones. A new test invocation or retry does not by itself require a new browser, container stack, or virtualized environment.

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

## Failed Checks and Test Cleanup

Establish expected behavior from the requirement or supported contract. Try the exact failing case independently when feasible. Fix a verified product defect. If a task-created optional test assumes an internal call order or misconfigures its fixture, correct or discard it while preserving any real requirement. Give a new optional harness at most one evidence-based correction for a setup failure. If the same setup failure persists, stop that approach. Production changes need a product or design reason.

After required assertions are covered by passing tests of the permitted kind, remove task-created diagnostic tests and their exclusively used fixtures, mocks, helpers, and dependencies. Migrate pre-existing suites only within authorized scope. A red mandatory gate or unresolved behavior remains open. Repair its cause within authority or report the missing evidence.

As the implementation changes, update, consolidate, or remove E2E tests and fixtures that only preserve abandoned fixes. Preserve still-required assertions and explicit coverage gates.

## Regression Testing

For bugs, prefer an E2E reproduction or regression test when feasible. Verify the actual success, failure, and boundary outcomes affected by the fix.

## Snapshot Rules

Do not update snapshots blindly. Inspect diffs and confirm they match intended behavior.

## Known Constraints

Document slow tests, flaky tests, unavailable environments, or validation gaps.

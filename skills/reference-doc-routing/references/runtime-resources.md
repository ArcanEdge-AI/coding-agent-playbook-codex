# Shared Runtime Resources

Use this reference when a task starts, recovers, uses, or stops a local runtime. Apply only the steps relevant to the resource. Keep identifiers and ownership in the existing task record when one is maintained.

## Identify and recover the environment

1. Inspect the project's running, stopped, and unhealthy resources, including ones from earlier sessions. Verify the backend, project identity, configuration, ports, mounts, data, current source or image, isolation, and consumers as relevant. An unreachable backend does not establish that its resources are absent.
2. Use the project's supported lifecycle tools. Restore backend connectivity first, then start stopped project services or restart the narrowest unhealthy resource. Routine non-destructive recovery of a verified project resource is within scope when the task requires the environment. Obtain authority before interrupting unrelated work or restarting a shared backend or machine when the impact is unresolved.
3. Set a bounded readiness wait and verify the intended behavior after each recovery. Use at most two recovery cycles by default unless a project runbook specifies a different finite allowance. Use failure evidence to choose a changed next action. If recovery remains blocked, report the exact target, actions, failure, and next step. Keep retries within the same allowance even if a runner or candidate name changes.
4. Keep established names, identity, configuration, mounts, and data. Create an additional environment only for a missing resource, a demonstrated isolation need, or evidence that recovery cannot meet the task. Apply changed source, image, or configuration through the narrowest supported update or recreation. Preserve or migrate required data first. A healthy but stale runtime cannot verify the current change.

## Share capacity and preserve isolation

- Set a finite concurrency budget for heavy work. Account for the user's CPU and memory needs, test-runner workers, helpers, and overlapping builds or other jobs. Use conservative concurrency or serialize when capacity is unresolved. Increase it for an identified need and verified capacity. Obtain authority before canceling or reconfiguring another owner's work.
- Start browser tests with one worker when capacity is unknown or other heavy jobs overlap, unless the required scenario needs more. Reuse a compatible browser, page, or isolated context through supported attachment. Preserve authentication, test isolation, and ownership. Prefer a tool that leaves the user's active application in focus when it can perform and verify the task.
- Reuse compatible images and build caches. Keep handles for reuse and teardown. Record the reason for an additional instance when a task record exists, including the verified isolation or replacement need and ownership. Available CPU counts or a failed start alone do not establish capacity or justify an additional stack.

## Release task-owned resources

Use failure-safe teardown on success and failure. Stop task-owned temporary services and release only the connections, pages, contexts, and other children borrowed from shared runtimes. Remove task-owned scratch files once they are unused and no longer needed for verification or handoff.

Preserve user-owned and shared services, persistent data, reusable images, and caches unless their exact removal is authorized. Use supported, ownership-scoped controls. Avoid broad process termination, pruning, or deletion. If teardown is blocked, preserve the affected resource and report its exact identifier, owner, state, and next action.

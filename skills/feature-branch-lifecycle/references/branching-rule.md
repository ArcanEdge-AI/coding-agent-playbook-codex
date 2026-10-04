# Feature Integration and Promotion Branching Rule

Use this rule for repositories whose established delivery model has a long-lived integration branch and a long-lived production branch. The examples call them `staging` and `main`; always resolve the repository's actual names and more specific instructions before acting.

## Branch Structure

All feature, change, or update work that may require one or more development branches follows this structure:

```text
production branch
        ↑
integration branch
        ↑
feature integration branch
        ↑
development branches
```

This keeps individual work isolated, combines related work before it reaches the long-lived integration branch, and promotes complete reviewable units toward production.

## 1. Establish the Branch Model

Before creating branches:

- inspect applicable repository instructions and release documentation
- identify the exact integration and production branches
- fetch or otherwise verify the current remote state when authorized and available
- inspect active branches, pull requests, owners, and worktrees that may overlap
- confirm the repository has selected this lifecycle

Do not create a missing `staging` branch, rename permanent branches, or replace an incompatible repository workflow without an explicit maintainer decision.

## 2. Create the Feature Integration Branch

Create one dedicated feature integration branch from the current integration branch.

Example:

```text
staging
  └── feature/project-permissions
```

The feature integration branch is the shared assembly and validation point for the complete feature, change, or update.

## 3. Create Development Branches

Create individual development branches from the feature integration branch. Scope each one to a specific implementation outcome when practical.

Example:

```text
feature/project-permissions
  ├── dev/add-role-model
  ├── dev/update-api-permissions
  ├── dev/update-permissions-ui
  └── dev/add-permission-tests
```

A development branch merges only into its feature integration branch. It must not merge directly into the long-lived integration or production branch.

Development branches are optional when one branch can implement the complete feature cleanly. The feature integration branch is still the promotion unit when this lifecycle applies.

## 4. Integrate and Validate the Complete Feature

Merge or otherwise incorporate completed development branches into the feature integration branch. Resolve conflicts there and validate the combined behavior.

Required validation is proportional to the repository and change and may include:

- build validation
- E2E tests of combined user flows, contracts, integrations, meaningful failures, and boundary cases
- linting, formatting, typechecking, and static analysis
- manual verification where useful, without substituting it for required E2E coverage
- final combined diff review
- confirmation that no known required development work remains incomplete

Retain E2E behavioral tests only. Every unit test created is temporary, regardless of purpose; none may remain in a completed feature. Remove them and exclusively used support code after corresponding E2E assertions pass, before considering the feature complete. Preserve required repository gates and keep migration of existing non-E2E suites within authorized scope.

Do not use the long-lived integration branch as the workspace for assembling an unfinished feature.

## 5. Promote to the Integration Branch

After complete-feature validation passes, create one pull request from the feature integration branch to the long-lived integration branch.

```text
feature/project-permissions
        ↓
      staging
```

Development branches associated with the feature must not be promoted independently.

Creating, approving, or merging the pull request remains subject to the task's authority and repository review gates.

## 6. Verify Cleanup Eligibility

Temporary branch cleanup begins only after the feature integration pull request has merged successfully into the integration branch.

Immediately before deleting any branch, verify all applicable gates:

- the expected pull request is merged into the exact integration branch
- the expected commits or equivalent patch are present in that branch
- required checks passed against the accepted result
- the temporary branch has no unique work that still needs preservation
- no open pull request, active task, person, automation, or release process still depends on it
- the branch is not checked out by an active worktree
- the exact local and remote deletion targets have been resolved
- authority exists for each local and remote deletion

A clean working tree, an old timestamp, or an apparently inactive branch is not sufficient evidence.

If any gate fails, preserve the branch and report the exact blocker and next action.

## 7. Clean Up Temporary Branches

After all cleanup gates pass:

1. Remove the completed development branches locally and remotely.
2. Remove the feature integration branch locally and remotely.
3. Verify the intended branches are gone and the permanent branches remain.

Never delete the long-lived integration or production branch. Do not use force deletion, reset, broad cleanup, or history rewriting as a shortcut.

The lifecycle requires eventual cleanup, but it does not itself authorize a destructive local or remote action. If the current request does not authorize deletion, report the exact branches that are ready for cleanup and request direction.

## 8. Promote to Production

When the accepted integration-branch state is ready and production promotion is explicitly authorized, use one pull request from the integration branch to the production branch.

```text
staging → main
```

Do not promote a development or feature integration branch directly to production. The integration branch remains permanent after production promotion.

Production promotion is a separate release action. A request to implement or integrate a feature does not implicitly authorize it.

## Completion Contract

The feature lifecycle is complete when:

- all required development work is incorporated into the feature integration branch
- complete-feature validation passes
- one accepted pull request incorporates the feature into the integration branch
- every temporary branch has a verified disposition: safely removed with authority or preserved with an exact blocker
- production promotion, when in scope, occurs only from the integration branch through authorized review

The core flow is:

```text
dev/task-a ──┐
dev/task-b ──┼──→ feature integration ── one PR ──→ staging
dev/task-c ──┘                                      │
                                                   cleanup
                                                     │
                                            authorized release
                                                     │
                                                  one PR
                                                     ↓
                                                    main
```

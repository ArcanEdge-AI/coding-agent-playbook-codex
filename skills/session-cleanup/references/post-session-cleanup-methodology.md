# Post-Session Cleanup & Integrity Pass

You have just completed substantial coding work.

The work may have spanned a long-running session, multiple context compactions, many commits, interrupted runs, or more than one coding agent. Do not assume the current conversation still contains a reliable memory of everything that happened.

Before considering the work finished, perform a deliberate cleanup and integrity pass over the complete work delta between the current implementation and its verified integration baseline, together with any staged, unstaged, and untracked changes.

The goal is not to redesign the system or begin another round of speculative refactoring.

The goal is to leave the changed portion of the repository clean, coherent, efficient, maintainable, tested, and free of implementation debris, abandoned approaches, speculative compatibility code, and avoidable technical debt.

Development is iterative. The final codebase should preserve the required implementation, not the history of how the implementation was reached.

## Governing Principles

* Do not over-engineer it.
* Make it elegant, not bloated.
* Prefer the smallest complete solution that reliably solves the demonstrated problem.
* Prefer the smallest maintainable implementation surface, not merely the fewest lines of code.
* Preserve necessary complexity where required for correctness, security, integrity, accessibility, maintainability, or a demonstrated compatibility requirement.
* Prefer existing project patterns and conventions over introducing new abstractions.
* Prefer one canonical implementation path.
* Do not rewrite working baseline code simply because you would personally structure it differently.
* Do not expand scope unless something must be corrected for the completed work to be safe, complete, or clean.
* Remove accidental complexity introduced during implementation.
* Remove branch-only experiments, intermediate designs, and superseded approaches when they are no longer required.
* Do not preserve code merely because it existed earlier in the development process.
* Do not solve hypothetical future problems instead of demonstrated present requirements.
* Do not add backwards-compatibility behavior for hypothetical users or consumers.
* Leave the codebase easier for the next developer or coding agent to understand.

### Compatibility rule

Compatibility code must have evidence.

Valid evidence may include:

* currently deployed older application versions
* real persisted data using the old representation
* active API or integration consumers using the old contract
* documented supported-version requirements
* an active migration window
* repository, configuration, test, deployment, or runtime evidence showing the compatibility path is still required

The following are not sufficient justification by themselves:

* "someone might still use it"
* "for backwards compatibility"
* "to be safe"
* "future-proofing"
* hypothetical users
* hypothetical old data
* hypothetical integrations
* hypothetical external consumers

Do not introduce aliases, adapters, deprecated interfaces, dual code paths, fallback APIs, compatibility wrappers, old-schema handling, transitional feature flags, or migration behavior without a demonstrated requirement.

Existing baseline compatibility code is different: do not remove it merely because it looks old. Verify callers, persisted data, supported clients, deployed versions, migrations, configuration, and dynamic usage first. If its necessity cannot be established either way, leave the pre-existing path unchanged and report the uncertainty.

Branch history is not production history. Code introduced and superseded entirely within an unmerged development branch does not require backwards compatibility with earlier commits on that branch.

---

# 1. Establish the Baseline and Reconstruct the Work Delta

Start by determining what the current work actually changed from repository evidence.

Do not reconstruct scope from conversational memory alone.

## Establish the integration baseline

Determine the repository's intended integration branch:

1. Prefer `staging` when it exists and repository evidence shows that it is the normal integration target for the current workflow.
2. Otherwise use `main` or the repository's verified primary integration branch.
3. Use repository documentation, configuration, branch/PR conventions, history, or explicit project instructions to verify the choice.
4. Do not choose a baseline solely because a branch happens to be named `staging` or `main`.

Find the merge base between the current branch and the verified integration baseline.

Treat the complete committed delta from that merge base through the current `HEAD`, together with staged, unstaged, and untracked work, as the primary cleanup surface.

If the current branch is itself the integration baseline or there is no meaningful committed divergence, use the verified working-tree changes and explicit task evidence as the work delta.

If a reliable baseline cannot be established, continue only with independently verified cleanup work and do not claim `complete and clean`.

## Review the complete work delta

Review:

* committed changes since the merge base
* Git diff against the verified baseline
* Git status
* staged changes
* unstaged changes
* untracked files
* files created
* files deleted
* files renamed or moved
* configuration changes
* dependency changes
* schema or migration changes
* tests added or modified
* documentation changed
* generated artifacts
* scripts or tooling introduced

Do not limit the review to files the current model remembers editing.

Use the repository itself as the durable source of truth.

Identify the intended outcome of the work and compare it against the implementation that now exists.

Distinguish:

* work-delta changes
* pre-existing baseline behavior
* unrelated working-tree changes
* files or hunks with uncertain ownership

Do not silently treat unrelated dirty files as part of the cleanup scope.

---

# 2. Look for Implementation Debris

Search the affected code for temporary or accidental artifacts left behind during development.

Check for:

* debug logging
* `console.log`
* print/debug statements
* temporary tracing
* commented-out code
* experimental branches of logic
* temporary UI elements
* temporary test controls
* temporary API routes
* hardcoded test values
* placeholder content
* fake/mock data accidentally left active
* temporary credentials or tokens
* local paths
* environment-specific values
* scratch files
* backup files
* generated files that should not be committed
* unused assets
* unused imports
* unused variables
* unused functions
* unused components
* abandoned files
* duplicate implementations
* stale feature flags
* temporary bypasses
* disabled validation
* disabled authentication/authorization
* skipped tests
* `.only`, `.skip`, or equivalent test modifiers

Remove these when they are clearly artifacts of the work delta.

Do not delete something simply because it appears unused until you verify that it is actually unnecessary.

---

# 3. Check for Abandoned Approaches and Speculative Compatibility

Long-running work often produces multiple attempted implementations before the final solution emerges.

Inspect the complete branch delta for implementation churn. Determine whether later changes superseded earlier code introduced on the same branch.

Look for:

* two utilities solving the same problem
* duplicate API clients
* old components replaced by newer ones
* unused helper functions
* obsolete types or interfaces
* redundant state
* abandoned hooks
* unnecessary adapters
* transitional compatibility code that is no longer needed
* temporary wrapper functions
* duplicate validation logic
* multiple sources of truth
* compatibility wrappers around implementations that no longer exist
* aliases preserving names that never shipped
* old interfaces created only during development
* fallback behavior for intermediate branch-only states
* feature flags for transitions that never reached a deployed environment
* migrations whose only purpose is to support a schema state that was never deployed
* re-export layers or forwarding APIs that exist only because the implementation changed during the branch

Prefer one clear canonical implementation.

Remove obsolete work-delta paths when doing so is safe and directly related to the completed work.

Do not preserve an earlier branch implementation solely because another commit in the same unmerged branch once depended on it.

When compatibility behavior was introduced by the work delta, require evidence of a real supported dependency. If there is no real dependency, remove the speculative compatibility path and keep the current canonical behavior.

When compatibility behavior predates the work delta, verify usage before removal. Do not turn a cleanup pass into an unsupported legacy-removal project.

Do not perform broad unrelated codebase cleanup.

---

# 4. Simplify and Minimize the Implementation Surface

Review the final implementation with fresh eyes.

For each file, abstraction, wrapper, helper, state variable, configuration option, dependency, feature flag, compatibility path, and code path introduced by the work delta, ask whether it is necessary for the demonstrated requirement.

Ask:

* Is there a simpler way to express this?
* Did implementation churn introduce unnecessary layers?
* Did we create an abstraction that only has one meaningful use?
* Did we create configuration where a straightforward behavior would work?
* Did we add state that can be derived instead?
* Did we duplicate logic instead of using an existing project pattern?
* Did we create indirection that makes the code harder to follow?
* Are there excessive wrappers, factories, managers, services, hooks, or utilities?
* Did we add a dependency for behavior the repository already supports?
* Did we create multiple ways to perform the same operation?
* Did we retain an earlier implementation after its replacement became canonical?
* Did we add compatibility behavior without evidence of a real consumer?
* Did we solve hypothetical future problems instead of the current requirement?

Remove work-delta code that exists only because:

* an earlier implementation was abandoned
* the agent was experimenting
* the design changed during development
* it duplicates an existing repository capability
* it anticipates an unrequested future requirement
* it supports a hypothetical legacy consumer
* it provides configuration for behavior that does not actually vary
* it adds indirection without reducing meaningful complexity

Simplify when the improvement is obvious, low-risk, verifiable, and within the scope of the completed work.

The objective is not code golf. Preserve useful boundaries and necessary complexity.

Do not chase architectural purity.

---

# 5. Check Code Quality

Review the affected implementation for:

### Naming

* Names accurately describe purpose.
* Temporary names have been replaced.
* Naming follows existing project conventions.
* Similar concepts use consistent terminology.

### Structure

* Functions and components have clear responsibilities.
* Logic is located where someone familiar with the repository would expect it.
* Files have not become unnecessarily large or tangled.
* Related behavior is grouped appropriately.
* There is one obvious canonical path for the changed behavior unless multiple paths are genuinely required.

### Readability

* Control flow is understandable.
* Clever code has not replaced clear code.
* Complex behavior has explanation where explanation is genuinely useful.
* Comments explain intent or non-obvious constraints rather than restating code.
* Comments do not justify speculative compatibility with hypothetical users or future requirements.

### Duplication

* Meaningful duplicate logic introduced by the work delta has been consolidated.
* Do not create abstractions solely to eliminate trivial duplication.

---

# 6. Validate Error Handling and Edge Cases

Check the paths changed by the work delta for:

* missing error handling
* swallowed exceptions
* misleading fallback behavior
* unsafe assumptions
* null/undefined handling
* empty states
* loading states
* failed network requests
* retries where appropriate
* partial failures
* malformed inputs
* invalid states
* duplicate submissions
* race conditions
* stale state
* unexpected API responses
* permission failures

Ensure failures are handled deliberately rather than accidentally.

Do not add elaborate defensive or fallback systems for scenarios the application cannot realistically encounter.

Do not convert hypothetical edge cases into permanent compatibility architecture without evidence that the system must support them.

---

# 7. Check Data and State Integrity

If the work delta touched persistence, state management, APIs, or databases, verify:

* there is a clear source of truth
* data is not unintentionally duplicated
* writes cannot silently corrupt state
* reads use the intended canonical source
* validation exists at the appropriate boundary
* frontend validation is not being treated as security
* IDs and relationships remain consistent
* migrations match the current schema
* migrations are safe and ordered correctly
* API contracts match consumers
* serialization/deserialization is correct
* default values are intentional
* old and new data states are both handled only when a demonstrated compatibility requirement exists

Pay special attention to situations where implementation changes may have created two competing sources of truth.

Do not create migration or dual-read/dual-write behavior solely because an earlier branch commit used a different representation. A branch-only intermediate schema is not automatically a production migration requirement.

---

# 8. Check Security Boundaries

For anything affected by the work delta, verify that cleanup did not leave:

* exposed secrets
* credentials in source
* authorization bypasses
* authentication bypasses
* overly permissive database access
* insecure direct object access
* missing ownership checks
* sensitive information in logs
* unsafe client-side trust
* unvalidated external input
* dangerous dynamic execution
* insecure file handling
* unnecessarily exposed API endpoints

Do not perform an unrelated full security audit unless requested.

Focus on the attack surface touched by this work.

---

# 9. Check Dependencies and Configuration

Review dependency or configuration changes in the work delta.

Verify:

* every new dependency is actually necessary
* no package was added for something the project already supports
* abandoned dependencies are removed
* imports match installed packages
* lockfiles are consistent
* package versions are intentional
* environment variables are documented where necessary
* configuration defaults are appropriate
* no local-machine configuration leaked into the repository
* build configuration still reflects how the project is actually deployed
* compatibility switches or flags have a demonstrated active requirement

Prefer removing unnecessary dependencies and configuration over retaining them "just in case."

---

# 10. Check UI/UX Changes

If the work delta affected the interface, verify the actual user flow rather than only inspecting source code.

Check:

* loading behavior
* empty states
* error states
* success states
* disabled states
* validation messages
* navigation
* back/forward behavior where relevant
* responsive behavior
* keyboard interaction
* basic accessibility
* labels
* focus behavior
* accidental duplicate controls
* inconsistent terminology
* stale UI after mutations
* confusing intermediate states
* obsolete controls or flows left from an abandoned implementation

Make sure the final interface represents the actual system state and canonical behavior.

Do not introduce visual redesigns unrelated to the task.

---

# 11. Check Tests

Review the tests associated with the work.

Ask:

* Are important new behaviors covered?
* Do the tests verify behavior rather than implementation trivia?
* Were any existing tests weakened simply to make them pass?
* Were assertions removed without justification?
* Are skipped tests still present?
* Are test fixtures or mocks left in an unrealistic state?
* Are new edge cases worth covering?
* Do old tests still describe the current intended behavior?
* Are tests preserving branch-only transitional behavior that never shipped?
* Are compatibility tests backed by an actual supported compatibility requirement?

Add or improve tests where there is a meaningful gap introduced by this work.

Remove or update work-delta tests that only preserve abandoned branch behavior and no longer describe the intended implementation.

Do not create excessive tests for trivial implementation details.

---

# 12. Run the Project's Validation Pipeline

Identify the project's existing validation commands and run the appropriate ones.

Where available, this should include:

* formatting
* linting
* type checking
* unit tests
* integration tests
* relevant end-to-end tests
* build
* project-specific verification scripts

Do not invent replacement validation commands if the repository already defines them.

If a validation step cannot be run, clearly state why.

Do not silently ignore failures.

Investigate failures sufficiently to determine whether they were:

1. introduced by the work delta,
2. pre-existing,
3. environmental/tooling related, or
4. unknown because the evidence is insufficient.

Fix failures introduced by the work delta.

Do not opportunistically repair unrelated failures unless necessary for this work.

After cleanup, re-run the affected checks and re-review the comparison against the verified baseline.

---

# 13. Check Documentation Against Reality

Review documentation directly affected by the implementation.

Check:

* README instructions
* setup instructions
* environment variables
* API documentation
* comments
* examples
* architecture notes
* configuration instructions
* user-facing copy
* developer documentation

Update documentation when the completed implementation has made existing documentation inaccurate.

Delete obsolete work-delta documentation when appropriate.

Do not create documentation simply for the sake of creating documentation.

Do not document abandoned branch behavior as though it remains supported.

Document real compatibility requirements or constraints when they would otherwise be difficult for the next person to infer.

---

# 14. Check TODOs, FIXMEs, and Deferred Work

Search the files touched by the work delta for:

* TODO
* FIXME
* HACK
* TEMP
* XXX
* workaround comments
* "for now"
* "temporary"
* "later"
* "remove after"
* similar markers

For each one introduced or affected by the work delta:

* resolve it if it should have been part of the completed work,
* remove it if it is obsolete,
* or leave it only if it represents legitimate deferred work.

Do not use TODO comments as a substitute for completing required behavior.

Do not leave speculative compatibility TODOs for hypothetical future consumers.

---

# 15. Check Repository Hygiene

Before finishing, verify:

* Git status contains nothing unexpected.
* The baseline comparison contains nothing unexpected.
* No secret or credential files are present.
* No editor/IDE debris was introduced.
* No OS-specific files were introduced.
* No unnecessary generated artifacts are present.
* No accidental binary files were added.
* No duplicate files remain from renames.
* No abandoned implementation files remain in the work delta.
* `.gitignore` remains appropriate.
* temporary scripts created for investigation are either intentionally retained or removed.
* file naming and directory placement follow repository conventions.

Never use destructive cleanup commands blindly.

Inspect before deleting.

---

# 16. Perform a Final "Next Developer" Review

Pretend you did not write this code.

Imagine opening the affected area tomorrow with no memory of the coding process and only the repository, verified baseline, and current branch to explain what changed.

Ask:

* Can I understand what changed?
* Is there one obvious implementation path?
* Is anything misleading?
* Is anything temporary pretending to be permanent?
* Are there unexplained magic values?
* Are responsibilities clear?
* Is there accidental duplication?
* Are errors understandable?
* Would another developer know where to modify this behavior?
* Is any code present only because the implementation took multiple attempts?
* Is any compatibility path present without a real supported consumer?
* Did the work delta leave behind technical debt that we can reasonably eliminate now?

Fix clear problems.

Do not start another redesign.

---

# 17. Final Scope Check

Before making any additional cleanup change, ask:

> Is this necessary to correctly complete, simplify, stabilize, or clean up the current work delta?

If no, leave it alone.

Record unrelated baseline issues separately rather than expanding the current task.

Do not use "cleanup" as permission for broad refactoring.

---

# Completion Report

When the cleanup pass is complete, provide a concise report containing:

## Cleaned Up

List meaningful cleanup performed.

## Validation

Report the checks actually run and whether they passed.

## Problems Found

List defects, incomplete work, accidental technical debt, abandoned approaches, speculative compatibility paths, or unnecessary complexity discovered.

## Remaining Issues

List anything intentionally left unresolved and why.

Separate:

* work-delta-introduced issues
* pre-existing issues
* optional future improvements

## Final State

State whether the current work delta is:

* complete and clean,
* complete with documented remaining issues,
* or not yet safe to consider complete.

Do not claim success when validation has not actually been performed.

Do not claim `complete and clean` when the integration baseline, ownership of material changes, or material changed behavior remains unresolved.

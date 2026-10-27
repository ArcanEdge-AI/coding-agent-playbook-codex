# Technical Debt Audit Methodology Reference

This file is the detailed execution authority for the `technical-debt-auditor` skill. The full source methodology supplied by the user is preserved below without removed phases or weakened requirements.

Apply these skill-level clarifications together with the source methodology:

- Audit modes may be Single Repository, Multi-Repository, Workspace/System, or Targeted Debt Audit. A targeted audit narrows categories but must not claim complete general coverage.
- For implementation behavior, use this source-of-truth order: direct source/configuration/runtime evidence; relevant tests; GitNexus relationship evidence; current architecture/design documentation; historical documentation. Investigate meaningful contradictions.
- Persist scope, baseline inventory, ledger, confirmed findings, and batch status outside audited repositories so interrupted audits can resume.
- On resume, recheck repository refs and working-tree state, compare a fresh inventory to the baseline, revalidate affected completed rows, and retain unchanged completed work.
- Audit and remediation are separate authorization boundaries even when requested in one message.

---

# Comprehensive Repository Technical Debt Audit

Perform a comprehensive technical-debt audit of the repository or repositories in the current workspace.

This is an **audit and analysis task only**.

Do not modify:

- source code
- configuration
- documentation
- dependencies
- infrastructure
- database state
- Git branches
- commits
- pull requests
- issues
- deployments
- GitNexus indexes
- external systems

unless explicitly authorized after the audit.

---

# Objective

Review the complete implementation and identify technical debt that materially affects:

- correctness
- reliability
- security
- maintainability
- architectural clarity
- unnecessary complexity
- performance
- scalability
- testing confidence
- observability
- deployment reliability
- developer experience
- dependency health
- obsolete implementation
- duplication
- cross-repository consistency

The objective is **not** to produce the largest possible list of imperfections.

The objective is to determine:

1. what technical debt actually exists;
2. why it qualifies as technical debt;
3. what evidence proves or supports it;
4. what parts of the system it affects;
5. what its actual risk or engineering cost is;
6. what the smallest reasonable remediation is; and
7. what order remediation should occur in.

Apply this principle throughout:

> **Do not over-engineer it. Make it elegant, not bloated. Prefer the smallest complete solution that solves the demonstrated problem reliably.**

---

# Core Evidence Model

Use two primary evidence layers throughout the audit.

## Source Evidence

Direct repository evidence including:

- implementation code
- configuration
- tests
- schemas
- package manifests
- database definitions
- infrastructure definitions
- build configuration
- CI/CD
- documentation
- architecture records
- Git history when relevant

## GitNexus Graph Evidence

Use the available GitNexus knowledge graph to understand system relationships including, where available:

- symbol relationships
- dependencies
- callers
- callees
- imports
- execution flows
- functional clusters
- architectural relationships
- impact relationships
- blast radius
- cross-file relationships
- cross-repository relationships

The governing rule is:

> **Use GitNexus to discover and understand relationships. Use source code to establish implementation truth. Use both to determine impact.**

GitNexus must not replace direct repository inspection.

Direct source inspection must not ignore useful graph evidence.

When source evidence and graph evidence disagree, investigate the discrepancy.

---

# Phase 1 — Establish Audit Scope

Before analyzing technical debt, determine exactly what is being audited.

For every repository in scope record:

- repository name
- local path
- current branch/ref
- current commit
- upstream when relevant
- working-tree status
- primary languages
- frameworks
- package/build systems
- test systems
- deployment/infrastructure systems
- major applications/packages contained within it

If multiple repositories are present, establish whether they represent:

- one product/system;
- related products;
- shared libraries;
- services;
- infrastructure;
- clients and servers;
- independent systems.

Do not assume repository boundaries are equivalent to architectural boundaries.

---

# Phase 2 — Create a Deterministic File Inventory

Create a complete inventory of files in every repository before declaring the audit complete.

The audit must account for **every file in scope**.

Maintain an audit ledger containing at minimum:

| Field | Description |
|---|---|
| Repository | Repository containing the file |
| Path | Full repository-relative path |
| Classification | Source, test, config, documentation, generated, dependency, binary, asset, etc. |
| Reviewed | Whether the file was accounted for |
| Detailed Review | Whether source-level analysis was appropriate |
| Findings | Number or IDs of associated findings |
| Notes | Relevant observations or reason detailed review was unnecessary |

Files that normally should not receive detailed source analysis may include:

- dependency/vendor directories
- generated artifacts
- build output
- caches
- binaries
- images/media
- minified bundles
- lock files
- machine-generated schemas
- compiled artifacts

Do not silently ignore these files.

Classify them and record why detailed source review is unnecessary.

Respect repository ignore rules where appropriate, but do not automatically assume everything ignored by Git is irrelevant to the operating system.

---

# Coverage Requirement

At completion report:

- total repositories discovered
- total files discovered
- total files accounted for
- total files receiving detailed analysis
- generated/vendor/binary files classified but not source-reviewed
- files that could not be reviewed
- reason for every exception

Do not claim:

> Every file was reviewed.

unless the audit ledger deterministically proves that every in-scope file was accounted for according to the defined review policy.

---

# Phase 3 — Establish GitNexus Coverage

Before relying on GitNexus, determine its coverage.

For every repository determine:

- whether it is indexed in GitNexus;
- whether the graph appears to correspond to the repository state being audited;
- whether relevant graph capabilities are available;
- whether cross-repository relationships are represented.

Create:

| Repository | Present Locally | GitNexus Indexed | Graph Appears Current | Graph Used |
|---|---:|---:|---:|---:|

Do not assume an indexed graph is current.

Do not rebuild, refresh, modify, or otherwise mutate GitNexus indexes unless explicitly authorized.

If GitNexus is unavailable, incomplete, or stale for part of the audit:

1. record the limitation;
2. continue using direct repository evidence;
3. avoid treating missing graph relationships as proof that relationships do not exist.

---

# Phase 4 — Understand the System Before Judging It

Do not begin by generating technical-debt findings from isolated files.

First reconstruct how the system works.

Inspect relevant:

- READMEs
- architecture documentation
- ADRs
- design documents
- package structure
- manifests
- entry points
- routes
- services
- APIs
- schemas
- database models
- events
- queues
- workers
- scheduled jobs
- authentication
- authorization
- external integrations
- infrastructure
- CI/CD
- tests

Determine:

- major system boundaries
- applications/services
- modules/packages
- major domain concepts
- primary entry points
- important runtime flows
- persistence model
- integration boundaries
- shared infrastructure
- deployment model
- test strategy
- dependency direction

Treat documentation as evidence of intended behavior.

Do not treat documentation as proof that the implementation actually matches it.

When documentation and implementation materially disagree, investigate and report the discrepancy when it creates real engineering cost or risk.

---

# Phase 5 — Build a GitNexus System Map

Use GitNexus early in the audit to understand the structure of each indexed repository.

Where useful, identify:

- major functional clusters
- execution processes
- central symbols
- dependency hubs
- entry points
- highly connected modules
- shared infrastructure
- important call chains
- module relationships
- dependencies crossing apparent boundaries

For multiple repositories, also inspect available cross-repository relationships.

Use this to form an initial system map.

The system map is an investigation aid, not unquestioned truth.

Validate important conclusions against source code.

---

# Phase 6 — Identify Investigation Hotspots

Use source structure and GitNexus relationships to identify areas that deserve deeper analysis.

Potential signals include:

- unusually high fan-in
- unusually high fan-out
- dependency hubs
- very large blast radius
- modules participating in many execution flows
- long execution chains
- cross-domain dependencies
- cross-layer dependencies
- unexpected dependency direction
- highly interconnected clusters
- parallel implementations of similar workflows
- apparently isolated code
- unclear ownership boundaries
- large shared utility modules
- frequently changed architectural hotspots

These are investigation signals.

They are **not automatically technical debt**.

A highly connected module may be intentionally and correctly designed.

---

# Phase 7 — Review Every Relevant File in Context

Review source, tests, configuration, schemas, documentation, and infrastructure in the context of the system rather than as disconnected files.

For each meaningful implementation file determine:

- its responsibility;
- important symbols it defines;
- who depends on it;
- what it depends on;
- which execution paths use it;
- whether the responsibility is clear;
- whether the implementation is active;
- whether similar logic exists elsewhere;
- whether meaningful behavior is tested;
- whether errors and edge cases are handled;
- whether configuration assumptions are safe;
- whether the implementation matches surrounding architecture.

Use GitNexus when relational context materially improves the analysis.

Do not query GitNexus merely because it is available.

Avoid unnecessary tool calls when the answer is already established by direct source evidence.

---

# Phase 8 — Technical Debt Categories

Evaluate the system for the following categories.

---

## 8.1 Correctness Debt

Look for:

- incomplete implementation
- contradictory behavior
- incorrect assumptions
- missing edge-case handling
- unsafe state transitions
- inconsistent validation
- silent failures
- race conditions
- incorrect error propagation
- stale behavior after migrations
- unreachable intended functionality
- inconsistent domain rules

---

## 8.2 Architectural Debt

Look for:

- unclear responsibility boundaries
- excessive coupling
- inappropriate dependency direction
- circular dependencies
- cross-layer leakage
- duplicated domain logic
- domain concepts represented inconsistently
- modules carrying unrelated responsibilities
- abstractions that no longer match the real system
- temporary architecture that became permanent
- hidden architectural dependencies
- architecture documented one way but implemented another

Do not recommend new architectural layers unless the existing design creates a demonstrated problem.

---

## 8.3 Complexity Debt

Identify:

- unnecessary abstraction
- excessive indirection
- wrapper-on-wrapper designs
- speculative extensibility
- difficult control flow
- hidden behavior
- generalized systems solving a narrow problem
- unnecessary factories/builders/managers/providers
- unnecessary configuration layers
- code substantially harder to understand than the problem requires

Prefer removing complexity over adding another abstraction.

---

## 8.4 Duplication Debt

Look for substantive duplication involving:

- business rules
- validation
- transformations
- API behavior
- schemas
- types
- utilities
- integration code
- configuration
- infrastructure
- tests
- domain models
- execution flows

Distinguish harmful duplication from small intentional repetition that improves clarity.

---

## 8.5 Dead and Obsolete Code

Investigate:

- unused modules
- unreachable code
- abandoned feature paths
- deprecated implementations
- stale compatibility layers
- commented-out implementation
- old migration paths
- obsolete configuration
- unused dependencies
- outdated feature flags
- duplicate legacy implementations

Do not declare code dead from text search alone.

Use both repository evidence and GitNexus where useful.

Also investigate:

- dynamic loading
- framework registration
- reflection
- routing
- events
- configuration references
- dependency injection
- plugin registration
- serialization references

If dead-code status cannot be proven, classify it as requiring verification.

---

## 8.6 Dependency Debt

Review:

- unnecessary dependencies
- duplicate libraries solving the same problem
- abandoned or unsupported dependencies
- unsafe dependency usage
- package boundary violations
- problematic version coupling
- fragile internal dependencies
- dependency pinning issues
- legacy dependencies blocking upgrades

Do not classify something as technical debt merely because a newer package version exists.

A dependency-version finding must have an actual consequence involving:

- maintenance
- compatibility
- support
- security
- reliability
- development cost

---

## 8.7 Testing Debt

Evaluate:

- critical flows without meaningful tests
- failure paths without tests
- brittle tests
- misleading tests
- skipped tests
- disabled tests
- duplicated test suites
- excessive implementation-detail testing
- unreliable fixtures
- unrealistic mocks
- tests representing obsolete behavior
- missing integration boundaries
- missing contract verification
- tests that pass while meaningful runtime behavior remains unverified

Do not equate raw coverage percentage with test quality.

---

## 8.8 Security Debt

Review implementation concerns involving:

- authentication
- authorization
- permission boundaries
- trust boundaries
- secret handling
- credential exposure
- input validation
- injection risks
- sensitive logging
- insecure defaults
- serialization/deserialization
- privilege boundaries
- tenant isolation
- file handling
- external API trust
- dependency exposure

Distinguish:

- confirmed security defect;
- strongly supported security risk;
- possible concern requiring runtime/security verification.

Do not overstate speculative security concerns.

---

## 8.9 Performance and Scalability Debt

Look for evidence of:

- repeated unnecessary computation
- N+1 patterns
- unbounded processing
- inefficient queries
- avoidable large-memory operations
- unnecessary network calls
- unnecessary database calls
- inappropriate synchronous/blocking work
- excessive serialization
- repeated parsing
- missing batching
- missing caching when workload evidence justifies caching
- scalability limitations already visible in architecture or usage

Do not invent hypothetical scale problems unsupported by evidence.

---

## 8.10 Operational Debt

Review:

- logging
- metrics
- tracing
- error reporting
- health checks
- retry strategy
- timeout behavior
- idempotency
- recovery behavior
- migration safety
- rollback capability
- deployment process
- environment consistency
- configuration management
- background job failure behavior
- data repair mechanisms

---

## 8.11 Documentation Debt

Report documentation debt only when missing or incorrect documentation creates meaningful engineering cost.

Look for:

- misleading documentation
- contradictory documentation
- stale architecture documentation
- undocumented critical setup
- undocumented operational behavior
- undocumented architectural dependencies
- undocumented environment assumptions
- missing migration instructions

Do not recommend documenting obvious implementation merely to increase documentation volume.

---

## 8.12 Developer Experience Debt

Evaluate:

- fragile setup
- undocumented setup assumptions
- inconsistent commands
- unnecessary development steps
- confusing repository organization
- difficult testing workflows
- inconsistent tooling
- excessive manual setup
- hidden environment requirements
- development and production behavior diverging unnecessarily

---

# Phase 9 — Search for Debt Signals

Search across the repositories for signals including:

- TODO
- FIXME
- HACK
- XXX
- temporary
- workaround
- legacy
- deprecated
- remove later
- not implemented
- commented-out implementation
- skipped tests
- disabled checks
- ignored exceptions
- broad exception handling
- feature flags
- compatibility code
- duplicated implementations

These are discovery signals only.

Do not automatically create technical-debt findings from them.

Inspect the surrounding implementation first.

---

# Phase 10 — Execution-Flow Analysis

Technical debt often exists across a process rather than inside one file.

Use GitNexus execution-flow/process information where available and trace important behaviors end-to-end.

Prioritize flows involving:

- authentication
- authorization
- user creation
- account management
- financial operations
- persistence
- data mutation
- file processing
- external integrations
- webhooks
- background jobs
- queues
- scheduled work
- AI/LLM workflows
- search/retrieval
- deployment-sensitive behavior
- critical business workflows

For important flows determine:

- where the flow begins;
- every significant stage;
- data transformations;
- trust boundaries;
- validation;
- state transitions;
- persistence;
- external calls;
- error propagation;
- retries;
- timeout behavior;
- fallbacks;
- observability;
- completion/failure behavior.

Look for:

- repeated validation
- missing validation
- competing implementations
- inconsistent error handling
- obsolete branches
- fragile coupling
- responsibility leakage
- unexpected dependencies
- unsafe state changes
- inconsistent domain behavior

Report debt at the execution-flow level when that better represents the underlying problem.

---

# Phase 11 — Architectural Boundary Analysis

Compare:

1. apparent architecture from folders and documentation;
2. actual architecture shown by imports, calls, runtime relationships, and GitNexus.

Investigate:

- dependencies crossing intended boundaries
- reverse dependency direction
- domain logic leaking into UI/transport layers
- infrastructure details leaking into domain logic
- lower-level packages depending on higher-level implementation
- hidden shared modules
- uncontrolled dependency hubs
- circular architectural areas
- clusters that do not match intended boundaries
- excessive cross-cluster relationships

Do not assume a cross-boundary relationship is wrong.

Determine whether it creates actual cost, fragility, confusion, or risk.

---

# Phase 12 — Root-Cause Analysis

Avoid turning one architectural problem into dozens of file-level findings.

When several symptoms appear related:

1. inspect their dependencies;
2. examine shared symbols;
3. examine GitNexus clusters;
4. inspect execution flows;
5. determine whether they share an underlying cause.

Prefer:

> TD-014 — Shared authorization service creates coupling across three domains

instead of:

> TD-014 — Authorization problem in file A\
> TD-015 — Authorization problem in file B\
> TD-016 — Authorization problem in file C

when the latter are symptoms of one underlying design problem.

Record affected locations as evidence under the root finding.

---

# Phase 13 — Dead-Code Verification

Before identifying something as dead or obsolete:

1. search direct references;
2. inspect imports;
3. inspect configuration;
4. inspect routes;
5. inspect framework registration;
6. inspect event registration;
7. inspect tests;
8. inspect dependency injection;
9. inspect GitNexus callers/dependencies;
10. determine whether it participates in any known execution process.

Use:

**Confirmed**

only when evidence establishes the conclusion.

Otherwise classify:

**Needs Verification — Possible dead or obsolete implementation**

and explain what additional evidence would resolve it.

---

# Phase 14 — Blast-Radius Analysis

For every Critical or High finding involving an identifiable:

- symbol
- module
- package
- service
- interface
- shared dependency
- schema
- execution process

use GitNexus impact/blast-radius capabilities when available.

Determine:

- direct dependents
- indirect dependents
- affected modules
- affected processes
- affected functional clusters
- affected repositories
- likely change surface

Then verify important relationships against source code.

Do not describe graph-estimated reach as guaranteed runtime impact.

Include:

**Graph Impact**

- Direct dependents:
- Indirect dependents:
- Processes affected:
- Clusters affected:
- Repositories affected:
- Source verification:

---

# Phase 15 — Multi-Repository Analysis

When multiple repositories are in scope, perform:

1. repository-level analysis; and
2. system-level analysis across repositories.

Use GitNexus cross-repository relationships when available.

Also verify relationships through source evidence such as:

- API clients
- package references
- shared schemas
- OpenAPI definitions
- event definitions
- environment variables
- deployment configuration
- infrastructure
- database access
- documentation
- authentication configuration

Look for:

- duplicated domain models
- schema drift
- API contract drift
- event contract drift
- inconsistent terminology
- incompatible assumptions
- duplicated business rules
- duplicated services
- duplicated utilities
- conflicting authentication logic
- inconsistent authorization behavior
- inconsistent error models
- incompatible data models
- version coupling
- fragile deployment dependencies
- unclear ownership
- unnecessary repository boundaries
- responsibilities split across repositories without clear reason

Do not recommend merging repositories merely because they are related.

Only report repository-boundary debt when the boundary creates demonstrable engineering cost or risk.

---

# Phase 16 — GitNexus / Source Contradiction Analysis

Explicitly identify meaningful disagreements between graph evidence and repository evidence.

Examples:

- GitNexus shows no caller but configuration dynamically registers the symbol.
- GitNexus shows a dependency that source analysis indicates is obsolete.
- Documentation describes a flow that differs from the graph.
- The graph shows one central implementation while source inspection reveals another dynamic path.
- An execution process appears in the graph but configuration suggests it is disabled.

Possible explanations include:

- stale graph data
- dynamic runtime behavior
- incomplete graph resolution
- obsolete implementation
- architectural drift
- configuration-driven behavior

Investigate rather than blindly trusting either source.

Report meaningful unresolved contradictions.

---

# Phase 17 — Evidence Classification

Use these evidence codes where applicable:

- **S — Source**
- **G — GitNexus Graph**
- **T — Tests**
- **D — Documentation**
- **C — Configuration / Infrastructure**
- **H — Git History**

Example:

**Evidence Sources:** S + G + T

Do not require every finding to use every evidence type.

Use the evidence relevant to proving the finding.

---

# Phase 18 — Finding Confidence

Every material finding must use one of these evidence states.

## Confirmed

Direct repository evidence demonstrates the problem.

## Strongly Supported

Available evidence strongly indicates technical debt, but runtime or operational verification would strengthen the conclusion.

## Needs Verification

A plausible concern exists but cannot be established from available static evidence.

Never present:

**Needs Verification**

as confirmed fact.

Prioritize Confirmed findings in the final report.

---

# Phase 19 — Avoid False Technical Debt

Do not report something merely because:

- another architecture is more fashionable;
- another framework is newer;
- a function is long;
- a file is large;
- naming could be different;
- more abstraction could exist;
- more comments could exist;
- more tests could theoretically exist;
- a dependency has a newer version;
- code could theoretically be more reusable;
- you prefer another design pattern;
- a module has many callers;
- a graph node has high connectivity.

Technical debt requires a concrete engineering cost, risk, maintenance burden, reliability problem, or demonstrable obstacle.

For every finding be able to answer:

> What actual problem does this cause?

If there is no meaningful answer, do not report it.

---

# Phase 20 — Simplicity Standard

Recommendations should generally prefer, in order:

1. remove obsolete implementation;
2. repair incorrect behavior;
3. simplify existing implementation;
4. consolidate proven harmful duplication;
5. clarify existing boundaries;
6. improve tests around meaningful behavior;
7. improve observability where needed;
8. introduce new architecture only when existing patterns cannot reasonably solve the demonstrated problem.

Avoid:

- speculative frameworks
- unnecessary service extraction
- unnecessary repositories
- unnecessary abstractions
- excessive interfaces
- wrapper layers
- premature generalization
- rewrites without demonstrated need
- gold-plating

Preserve necessary complexity for:

- security
- correctness
- data integrity
- accessibility
- reliability
- testing
- credible operational risks.

---

# Phase 21 — Severity

Assign each finding a severity.

## Critical

Current debt threatens:

- security
- data integrity
- production stability
- core system correctness

or creates comparable immediate risk.

## High

Significant:

- reliability
- architecture
- maintainability
- security
- operational
- testing

risk.

## Medium

Meaningful debt that increases:

- complexity
- engineering cost
- defect likelihood
- change risk
- operational burden

but is not immediately dangerous.

## Low

Legitimate technical debt with limited current impact.

---

# Phase 22 — Remediation Priority

Severity and remediation priority are separate.

Use:

- **P0 — Immediate**
- **P1 — Near-term**
- **P2 — Planned**
- **P3 — Opportunistic**

When determining priority consider:

- severity
- reach/blast radius
- likelihood
- change frequency
- number of affected processes
- number of affected repositories
- remediation risk
- remediation effort
- dependency sequencing

Do not fabricate numeric formulas unless explicitly requested.

Use these factors qualitatively.

---

# Phase 23 — Effort and Blast Radius

For each finding estimate:

## Effort

- Small
- Medium
- Large

Consider:

- implementation
- testing
- migration
- documentation
- deployment
- verification

Do not label something Small merely because the code diff appears short.

## Blast Radius

- Local
- Module
- Repository
- Multi-repository

Use GitNexus evidence when appropriate.

---

# Phase 24 — Finding Format

Use this structure for every reported technical-debt finding.

## TD-[number]: [Concise title]

**Repository:**\
**Area:**\
**Category:**\
**Severity:**\
**Priority:**\
**Effort:**\
**Blast Radius:**\
**Evidence State:**\
**Evidence Sources:** S / G / T / D / C / H

### Evidence

Provide:

- exact file paths
- relevant symbol/function/class/module names
- line references when practical
- callers/dependencies when material
- relevant tests
- relevant configuration
- relevant documentation
- relevant graph relationships

### Current Behavior

Explain what the system currently does.

### Why This Is Technical Debt

Explain the concrete:

- cost
- fragility
- risk
- maintenance burden
- correctness problem

that qualifies it as debt.

### Impact

Explain what may happen if the debt remains unresolved.

### GitNexus Context

When applicable include:

- symbols
- clusters
- execution processes
- direct relationships
- indirect relationships
- impact depth examined
- graph observations

### Source Verification

Explain which material graph conclusions were verified against direct repository evidence.

### Recommended Direction

Describe the **smallest reasonable remediation**.

Do not implement it.

Do not write extensive replacement code unless a small example is necessary to explain the recommendation.

### Dependencies / Sequencing

Identify:

- prerequisites
- related findings
- changes that should occur together
- changes that should occur afterward

---

# Phase 25 — Consolidate Findings

Before finalizing the report:

- merge duplicate findings;
- group symptoms under root causes;
- identify overlapping findings;
- distinguish causes from consequences;
- eliminate purely stylistic findings;
- remove speculative findings that lack sufficient evidence;
- avoid inflating finding counts.

A smaller list of strong findings is preferable to a large list of weak ones.

---

# Phase 26 — Remediation Dependency Analysis

Use source relationships and GitNexus where helpful to determine how debt findings depend on one another.

Determine whether:

- one remediation must precede another;
- multiple findings share the same root cause;
- several findings should be addressed together;
- one foundational cleanup reduces multiple later risks;
- remediation of one area could destabilize another;
- different repositories require coordinated changes.

Prefer remediation sequences that minimize repeated work and change risk.

---

# Phase 27 — Quick Wins

A Quick Win must be:

- clearly beneficial
- well understood
- relatively small
- low risk
- easy to verify
- limited in blast radius

Before calling something a Quick Win, verify its dependency impact when appropriate.

A five-line change to a symbol used by fifty systems is not automatically a Quick Win.

---

# Phase 28 — Validation of High-Severity Findings

Before finalizing any Critical or High finding:

1. re-read the relevant source;
2. inspect its callers;
3. inspect its dependencies;
4. inspect relevant tests;
5. inspect relevant configuration;
6. inspect GitNexus impact where appropriate;
7. determine whether another layer mitigates the problem;
8. confirm it is not intentional behavior;
9. confirm the recommendation does not introduce unnecessary complexity.

Apply additional scrutiny to high-severity claims.

---

# Phase 29 — Final Deliverable

Produce the final audit using this structure.

---

## A. Executive Summary

Summarize:

- overall technical-debt condition;
- highest risks;
- strongest recurring themes;
- important architectural observations;
- highest-value remediation opportunities.

Keep this concise enough for technical leadership.

---

## B. Audit Scope

List:

- repositories audited
- branches/commits
- major technologies
- relevant limitations

---

## C. Repository Coverage

For every repository:

| Repository | Files Discovered | Files Accounted For | Detailed Review | Classified Only | Unable to Review |
|---|---:|---:|---:|---:|---:|

Explain every meaningful exception.

---

## D. GitNexus Coverage

| Repository | Indexed | Graph Appears Current | Graph Used | Cross-Repo Evidence |
|---|---:|---:|---:|---:|

Explain limitations.

---

## E. System Architecture Observations

Describe only architectural context needed to understand the findings.

Include:

- major components
- important boundaries
- major processes
- significant dependencies

---

## F. GitNexus Knowledge-Graph Analysis

### Architectural Hotspots

Describe graph areas that materially affected the audit.

### Important Execution Processes

Identify the processes most relevant to technical debt.

### Highest-Blast-Radius Areas

Identify important symbols/modules/components where graph reach materially affects risk.

Do not produce connectivity rankings merely for their own sake.

### Graph / Source Contradictions

Document meaningful disagreements between GitNexus and direct repository evidence.

### Graph-Assisted Findings

Identify findings where GitNexus materially:

- discovered;
- strengthened;
- reduced;
- disproved;
- reprioritized

the assessment.

---

## G. Technical Debt Register

Provide a concise table:

| ID | Finding | Category | Severity | Priority | Effort | Blast Radius | Evidence State |
|---|---|---|---|---|---|---|---|

---

## H. Detailed Findings

Provide the complete evidence-backed findings using the required finding format.

Group by root problem when appropriate.

---

## I. Repository-by-Repository Analysis

Summarize notable debt patterns for each repository.

Do not repeat the full detailed finding unnecessarily.

---

## J. Cross-Repository Findings

When multiple repositories exist, summarize confirmed system-level debt involving:

- contracts
- schemas
- architecture
- duplicated behavior
- dependencies
- deployment
- ownership
- shared domain logic

---

## K. Root Causes / Debt Clusters

Identify cases where multiple findings originate from:

- the same architectural decision;
- incomplete migration;
- historical workaround;
- missing shared responsibility;
- unclear boundary;
- duplicated platform capability;
- inconsistent design pattern.

---

## L. Recommended Remediation Sequence

Organize remediation into waves.

### Wave 1 — Risk Reduction

Prioritize:

- correctness
- security
- data integrity
- production reliability

### Wave 2 — Structural Simplification

Prioritize:

- unnecessary complexity
- harmful duplication
- obsolete paths
- inappropriate boundaries
- foundational architectural debt

### Wave 3 — Confidence Improvements

Prioritize:

- tests
- observability
- operational reliability
- deployment
- documentation
- developer workflow

### Wave 4 — Opportunistic Cleanup

Lower-impact debt best handled while related code is already being changed.

Identify dependencies between waves and findings.

---

## M. Quick Wins

List only legitimately:

- small
- low-risk
- high-value

changes.

---

## N. Items Requiring Verification

For each unresolved concern state:

- what is suspected;
- why repository evidence is insufficient;
- what additional evidence is required.

Examples may include:

- runtime tracing
- production telemetry
- database inspection
- deployment configuration
- user behavior
- external service behavior
- load testing
- security testing

---

## O. Audit Limitations

Explicitly disclose:

- inaccessible files
- stale GitNexus indexes
- missing external systems
- unavailable credentials
- runtime behavior that could not be tested
- repositories not included
- generated assets not meaningfully inspectable

Do not conceal uncertainty.

---

## P. Audit Ledger

Provide or save the complete file-level ledger showing that every in-scope file was accounted for.

---

# Phase 30 — Final Verification Gate

Before declaring the audit complete perform these checks.

## Repository Coverage

1. Compare the final audit ledger against the original file inventory.
2. Search for files that were not accounted for.
3. Verify all repositories in scope were audited.
4. Verify excluded/classified-only files have reasons.

## GitNexus Coverage

5. Verify every repository was checked against GitNexus.
6. Verify graph freshness/current-state concerns were considered.
7. Verify GitNexus was used where relational analysis materially helped.
8. Verify GitNexus did not replace source inspection.

## Finding Quality

9. Remove duplicated findings.
10. Merge symptoms into root causes when appropriate.
11. Remove stylistic preferences presented as technical debt.
12. Verify Critical and High findings against surrounding implementation.
13. Confirm evidence states are accurate.
14. Confirm uncertain findings are not stated as facts.

## Architecture

15. Verify important execution paths were considered.
16. Verify architectural boundaries were evaluated based on actual dependencies.
17. Verify multi-repository relationships were examined when applicable.
18. Verify graph/source contradictions were investigated.

## Recommendations

19. Verify recommendations solve demonstrated problems.
20. Verify recommendations do not introduce unnecessary architecture.
21. Verify Quick Wins actually have limited risk.
22. Verify remediation sequencing reflects dependencies and blast radius.

Do not declare the audit complete until these checks have been performed.

---

# Large Repository / Context Limit Handling

If the repository or repository group is too large to audit completely in one context window, do not reduce scope or silently sample files.

Instead:

1. preserve the complete repository inventory;
2. divide the audit into deterministic batches;
3. maintain the audit ledger across batches;
4. preserve discovered architectural context;
5. preserve confirmed findings;
6. prevent unnecessary re-review of completed files;
7. continue until the complete inventory has been exhausted;
8. perform the final consolidation only after all batches are complete.

Possible batching strategies include:

- repository
- package
- architectural cluster
- GitNexus functional cluster
- directory
- application/service boundary

Choose the batching strategy that preserves the most meaningful context.

Do not claim complete coverage before every in-scope file has been accounted for.

---

# Audit Behavior

Throughout the audit:

- investigate before concluding;
- distinguish evidence from assumption;
- verify graph findings against source;
- trace important behavior across files;
- examine root causes instead of isolated symptoms;
- avoid speculative redesign;
- prefer simplification;
- preserve existing architecture when it works;
- report only technical debt with meaningful consequences;
- disclose uncertainty;
- maintain deterministic coverage.

The quality of this audit is measured by:

- completeness of repository coverage;
- strength of evidence;
- correctness of findings;
- understanding of system relationships;
- quality of root-cause analysis;
- accuracy of impact assessment;
- usefulness of remediation sequencing;
- resistance to over-engineering.

The final report must provide enough evidence that another engineer can independently inspect the cited locations and understand why each material finding was made.

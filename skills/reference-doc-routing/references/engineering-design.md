# Engineering Design Decision Aid

Build the smallest complete solution that solves the actual problem correctly and fits the existing system. The global instructions define the behavioral standard; this reference provides questions and examples for applying it.

## When to Use This Aid

Use selected questions for non-trivial, cross-cutting, or difficult-to-reverse design choices, or when an implementation starts accumulating layers or workarounds. Do not answer every question for routine work. Record only the assumptions and tradeoffs that materially affect the outcome.

## Decision Questions

1. What actual problem and desired behavior are we addressing?
2. Does the proposed change solve the root cause or only its symptom, and is that root cause within the authorized scope?
3. Are assumptions unnecessarily constraining the approach?
4. Could a simpler approach eliminate the problem or the need for new machinery?
5. Which parts of the affected flow already satisfy the requirement, from entry points and shared rules through data changes, consumers, and success or failure outcomes? Can they be reused or improved?
6. Can the implementation be clearer or smaller while remaining complete?
7. Does the existing architecture provide an appropriate pattern?
8. What complexity does this introduce?
9. Which current requirement, boundary, invariant, duplication, or variability justifies it?
10. What maintenance burden does this create?
11. When the requirement changes, which components will need to change with it, and why?
12. Can another developer understand the purpose and constraints from the code and necessary documentation?
13. Based on current evidence, does this make likely future changes easier without building for hypothetical needs?

## Earned Abstractions

A single-use adapter can isolate an external dependency or translate a contract. Its boundary can justify it even without repeated call sites.

Conversely, two similar functions may serve different rules and change independently. Combine them only when they share demonstrated behavior, an invariant, or a boundary; matching syntax alone is insufficient.

Prefer clear responsibilities and small interfaces. Avoid wrappers, managers, factories, service layers, or configuration systems that add indirection without a concrete benefit. No category of abstraction is inherently forbidden or required.

## Simpler Approaches and Complete Fixes

Inspect the whole affected flow before choosing its replacement. Improve the existing implementation by default, preserving suitable components and boundaries. A substantial replacement needs evidence of a significant benefit that outweighs implementation, migration, verification, and maintenance costs. Another valid design, personal preference, or alpha status does not establish that benefit.

Use concrete evidence such as repeated defects at the same boundary, competing implementations, or a requirement that currently forces coordinated edits across unrelated modules. Measure relevant performance or operating costs when those motivate the change. Do not invent percentages for code quality or optimize line count as a substitute for maintainability. Necessary correctness and security fixes remain required.

If a value can be reliably derived from existing state, storing another copy may create unnecessary synchronization and consistency work. Inspect actual requirements before introducing that state.

A small patch that repeats a workaround can cost more to maintain than a focused change at the correct boundary. Compare completeness, affected surfaces, reliability, and verification needs rather than counting changed lines. A broader root cause is not permission for an unrelated redesign.

Tests, fixtures, and mocks are part of the maintenance surface. Retain tests for the intended final behavior and credible regression risks, including focused unit tests for lasting rules. Update or remove tests that only describe abandoned intermediate fixes. Prefer extending existing coverage over creating a parallel suite, and do not reshape sound production code solely to support low-value tests.

## Material Technical Debt

Prefer avoiding known debt. When constraints justify a material compromise, record:

- Scope: the affected behavior or component and the limitation being accepted.
- Rationale: the constraint and why the tradeoff is preferable to the available alternatives.
- Follow-up condition: the event, requirement, or agreed milestone that should trigger reassessment or removal.

For example, a compatibility adapter may remain while a demonstrated supported caller uses an older contract; removal can be tied to that caller's verified migration. Without a current dependency or explicit retention requirement, prefer retiring the superseded path instead of adding guards around it. Use the `legacy-path-retirement` skill for that dependency decision.

Existing development data is a separate retention or migration decision, not automatic justification for permanent compatibility code. Pre-production status does not make that data disposable or weaken authorization, validation, stable-reference, persistence, or cleanup guarantees.

Use the existing plan, review description, or maintained project documentation for this record. Do not create a new tracking system, deadline, or cleanup commitment without a real need and appropriate authority.

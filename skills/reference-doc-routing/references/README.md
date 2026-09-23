# Codex Reference Documents

This directory contains the reference documents owned by the `reference-doc-routing` skill. Other workflows keep their own references inside their skill packages.

These documents are intentionally generic and tool-agnostic. They should not contain repo-specific workflows, sensitive access material, local machine quirks, project names, or one-off incident notes.

## How to Use These References

The main agent should:

1. Start with the current user request and applicable repository instructions.
2. Inspect current code, tests, configuration, and docs.
3. Consult only the packaged reference documents that are relevant.
4. Treat reference docs as supporting context, not automatic truth.
5. When delegation is justified and authorized, pass only relevant context.
6. Resolve conflicts using primary evidence.

Primary evidence includes:

- current code
- tests
- schemas
- configuration
- logs
- build output
- typecheck output
- runtime behavior
- authoritative external documentation

## Available References

- `references/engineering-design.md` — selective design questions for complete solutions, justified abstractions, change amplification, and material technical-debt tradeoffs.
- `references/reference-doc-routing.md` — how to choose and classify reference documents.
- `references/templates/repository-AGENTS.md` — starter template for repo-specific instructions.
- `references/templates/architecture.md` — architecture reference template.
- `references/templates/testing.md` — testing strategy template.
- `references/templates/security.md` — safety and access-control model template.
- `references/templates/design-system.md` — design-system and UI convention template.
- `references/templates/release.md` — release and deployment template.
- `references/templates/api-contracts.md` — API contract template.
- `references/templates/data-model.md` — data model and persistence template.

## Placement Rules

Keep durable, cross-repository guidance inside its owning skill package.

Use repository-level docs for:

- repo architecture
- repo build/test commands
- repo release flow
- repo-specific design rules
- framework-specific conventions
- domain-specific business logic
- project-specific subagent roles
- project-specific active-work records

Use skills for repeatable workflows.

Use local notes for machine-specific or shell-specific quirks.

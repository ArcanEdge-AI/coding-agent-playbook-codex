---
name: reference-doc-routing
description: Select and classify only the architecture, testing, safety, design-system, API, release, data-model, or repository guidance relevant to a task, then verify it against primary evidence.
---

# Reference Document Routing

Use this skill when substantial reference material could improve the task but loading all of it would waste context or blur authority.

Read [references/reference-doc-routing.md](references/reference-doc-routing.md) for the selection, authority-classification, conflict-resolution, and handoff workflow.

Reusable starting templates live under `assets/templates/`:

- `repository-AGENTS.md`
- `architecture.md`
- `testing.md`
- `security.md`
- `design-system.md`
- `release.md`
- `api-contracts.md`
- `data-model.md`

Treat templates as output assets to copy and adapt, not instructions to load automatically. Prefer current code, tests, schemas, configuration, logs, build output, typecheck output, runtime behavior, and authoritative external documentation when a reference conflicts with primary evidence.

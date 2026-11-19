---
name: reference-doc-routing
description: Select relevant project and engineering references, classify their authority, and use shared runtime guidance when starting, recovering, or stopping local environments.
---

# Reference Doc Routing Skill

Use this skill to choose and apply reference documents without polluting the main context.

Consult [the catalog](references/README.md) for available templates and [routing guidance](references/reference-doc-routing.md) to resolve conflicting sources. Use [engineering design](references/engineering-design.md) for consequential design choices. Use [shared runtime resources](references/runtime-resources.md) when starting, recovering, or stopping local environments, including work outside CI.

Workflow:

1. Identify which parts of the task need reference context.
2. Find relevant global and repository-level docs.
3. Classify each document as authoritative, advisory, or historical.
4. Read only relevant sections when possible.
5. Summarize useful context for the current task.
6. Pass only relevant document paths or sections to subagents.
7. Require implementation-relevant claims to be checked against current code, tests, schemas, configuration, or runtime behavior.
8. Report conflicts between docs and primary evidence.

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

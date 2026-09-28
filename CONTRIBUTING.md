# Contributing

Thanks for helping improve Coding Agent Playbook — Codex Edition.

This repository is intentionally public and reusable. Contributions should make the playbook clearer, more durable, and less tool-specific.

## What Belongs Here

Good contributions include bug reports, documentation fixes, routing improvements, new skills, agent profiles, evidence-backed benchmark runs, methodology improvements, clearer global coding-agent instructions, reusable reference document templates, and generic examples that are easy to adapt.

## What Does Not Belong Here

Avoid adding:

- organization-specific workflows
- private project names
- local machine quirks
- internal URLs
- sensitive access material
- full thread transcripts
- long incident logs
- instructions tied to one tool unless the file is explicitly an example

## Style

- Prefer concise, direct language.
- Keep guidance tool-agnostic unless the file is explicitly tool-specific.
- Prefer behavior and decision rules over rigid command sequences.
- Use examples that are generic and safe for public reuse.
- Keep direct-first main-agent ownership, optional bounded assistance, task-based helper routing with Standard speed and no Max, Ultra, or Fast, flat default delegation, scope and authority limits, and the task-local worktree lifecycle model intact.
- Keep this repository's policy and implementation Codex-specific. The companion Claude Code playbook is maintained independently; do not modify it from this repository's workflow.
- For routing, skills, and agent-profile changes, explain the task boundary and validation evidence rather than asserting a model choice is universally best.
- For benchmark contributions, use [`docs/evidence/RUN-TEMPLATE.md`](docs/evidence/RUN-TEMPLATE.md), distinguish public reproduction from private field work, and report missing evidence as missing.
- Never include secrets, private code, confidential client information, credentials, private logs, or material you do not have permission to publish.

## Pull Request Checklist

Before opening a PR:

- Review Markdown formatting and fenced code blocks.
- Confirm links and paths match the repository tree.
- Confirm `SKILL.md` files include `name` and `description` frontmatter.
- Confirm `agents/*.toml` files are syntactically valid and define explicit `model` and `model_reasoning_effort` values if changed.
- Confirm each of the five bundled roles has one profile under its standard name, explicit defaults match an approved task route, actual routes follow the assignment with Standard speed, and all profiles retain clear stop conditions.
- Confirm profiles support direct main-agent perspective use without changing its settings or authority, requiring a role sequence, or implying independent verification; keep delegated-execution rules conditional.
- Confirm Unix shell scripts remain LF-only.
- Confirm the change is valid for Codex without assuming or modifying the independently maintained Claude Code edition.
- Confirm no sensitive or private material was added.
- For evidence or benchmark changes, confirm claims have a reproducible source, a correction/review trail where applicable, and no invented results.

## License

By contributing to this repository, you agree that your contribution will be licensed under the MIT License. See `LICENSE`. Do not change the license without an explicit maintainer decision.

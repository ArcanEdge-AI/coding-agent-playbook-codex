# Contributing

Thanks for helping improve Coding Agent Playbook — Codex Edition.

This repository is intentionally public and reusable. Contributions should make the playbook clearer, more durable, and less tool-specific.

## What Belongs Here

Good contributions include bug reports, documentation fixes, routing improvements, new skills, agent profiles, evidence-backed benchmark runs, methodology improvements, clearer global coding-agent instructions, reusable skill-owned reference documents and templates, and generic examples that are easy to adapt.

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
- Keep durable always-on guidance small. Put situational procedures in the owning skill and keep each piece of guidance in one canonical location.
- Keep detailed skill procedures in that skill's `references/` directory and output templates in its `assets/` directory when progressive disclosure improves context use.
- Treat top-level `skills/` as the plugin payload. Do not duplicate it under a repository `.agents/skills` tree.
- Keep the main-agent orchestration, actual-root-model ceiling, bounded hierarchy, permit, capability-ceiling, and task-local worktree lifecycle model intact.
- Compare generic policy changes with the companion Claude Code playbook. Align shared behavior or document the concrete harness capability that requires a difference.
- For routing, skills, and agent-profile changes, explain the task boundary and validation evidence rather than asserting a model choice is universally best.
- For benchmark contributions, use [`docs/evidence/RUN-TEMPLATE.md`](docs/evidence/RUN-TEMPLATE.md), distinguish public reproduction from private field work, and report missing evidence as missing.
- Never include secrets, private code, confidential client information, credentials, private logs, or material you do not have permission to publish.

## Pull Request Checklist

Before opening a PR:

- Review Markdown formatting and fenced code blocks.
- Confirm links and paths match the repository tree.
- Validate `.codex-plugin/plugin.json` and `.agents/plugins/marketplace.json` against the current Codex plugin schema.
- Confirm `SKILL.md` files include `name` and `description` frontmatter.
- Confirm each skill entrypoint links every required reference or asset and does not duplicate its detailed content.
- Confirm `agents/*.toml` files are syntactically valid and define explicit `model` and `model_reasoning_effort` values if changed.
- Confirm every bundled role retains one Terra profile and one Luna profile, child routes stay within the actual root model and effort ceilings, and smaller profiles retain clear stop conditions.
- Confirm Unix shell scripts remain LF-only.
- Confirm companion installers manage only the lean global section and personal custom agents, while still retiring unchanged legacy managed references and skills and preserving customized copies.
- Confirm generic policy changes were compared with the companion Claude Code playbook and any intentional divergence names its harness-specific reason.
- Confirm no sensitive or private material was added.
- For evidence or benchmark changes, confirm claims have a reproducible source, a correction/review trail where applicable, and no invented results.

## License

By contributing to this repository, you agree that your contribution will be licensed under the MIT License. See `LICENSE`. Do not change the license without an explicit maintainer decision.

# Install Coding Agent Playbook — Codex Edition

This file is written for both humans and AI coding agents.

The intended experience is:

```text
Install this repo into my Codex setup:
https://github.com/ArcanEdge-AI/coding-agent-playbook-codex

Follow INSTALL.md. Use full install unless I explicitly ask for support-only mode.
Preserve my existing files with backups and report exactly what changed.
```

## What Gets Installed

A full install creates or updates this user-level structure:

```text
$CODEX_HOME/
  AGENTS.md
  .coding-agent-playbook-codex-managed-files.tsv
  agents/
    planner.toml
    engineer.toml
    reviewer.toml
    tester.toml
    docs.toml

$CODEX_HOME/skills/
  subagent-orchestration/
    SKILL.md
    references/
      model-routing.md
      subagents.md
  task-graph-orchestration/
    SKILL.md
    references/templates/task-graph.md
  worktree-lifecycle/
    SKILL.md
    references/
      worktrees.md
      templates/worktree-manifest.md
  feature-branch-lifecycle/
    SKILL.md
    references/
      branching-rule.md
  legacy-path-retirement/SKILL.md
  local-ci-preflight/
    SKILL.md
    agents/openai.yaml
    assets/
      LOCAL_VALIDATION.template.md
      AGENTS.local-validation.md
  aws-local-preflight/
    SKILL.md
    agents/openai.yaml
    assets/LOCAL_VALIDATION.aws.template.md
    references/moto-boundaries.md
  handoff/
    SKILL.md
    agents/openai.yaml
    references/context-contract.md
  session-cleanup/
    SKILL.md
    agents/openai.yaml
    references/post-session-cleanup-methodology.md
  multi-session-coordination/
    SKILL.md
    references/
      multi-session-coordination.md
      templates/active-work-record.md
  reference-doc-routing/
    SKILL.md
    references/
      README.md
      engineering-design.md
      reference-doc-routing.md
      templates/
        *.md
  senior-code-review/SKILL.md
```

Path resolution:

- `CODEX_HOME`: use `$CODEX_HOME` if set, otherwise `~/.codex`.
- `USER_SKILLS_HOME`: use `$CODEX_HOME/skills` unless explicitly overridden.
- On Windows, resolve equivalent user-home paths safely.

The installer also includes these self-contained workflow packages under the same skills root:

- `multi-role-repo-review`
- `platform-documentation`
- `technical-debt-auditor`
- `design-taste-frontend`
- `impeccable`
- `taste-new-website`
- `taste-redesign-website`
- `humanizer`
- `production-api-integration`
- `production-architecture-review`
- `production-code-quality`
- `production-database-integrity`
- `production-devops-release`
- `production-documentation-onboarding`
- `production-pass-orchestrator`
- `production-performance-review`
- `production-readiness-report`
- `production-reliability-observability`
- `production-security-review`
- `production-testing-qa`
- `production-ux-accessibility`

Their supporting files, licenses, and notices are managed and copied with each package. See [third-party attribution](THIRD_PARTY.md). The Taste workflows require the sibling `design-taste-frontend` package; normal installs include it. Impeccable's `reference/` directory is intentional and validated alongside the other skills' `references/` directories.

Skill installation does not invoke Impeccable, download its engine, configure hooks, start a browser, or launch helpers. Its upstream launchers can reuse or fetch engine 0.1.11 at first use under the invoking task's permissions. The four upstream helper contracts are mapped to the existing Codex roles through bundled Markdown references; no additional global agent profiles are installed. The optional documentation and audit Python helpers require Python 3.10 or newer.

### Companion marketplace plugin

Include the maintained **Intuitive Software Design** Codex marketplace plugin using [the companion plugin setup](plugins/README.md). Reuse an installed, enabled marketplace release. If missing, use the supported Codex plugin manager or `codex plugin add intuitive-software-design@openai-curated-remote` when that command is available. Preserve account and host permission requirements.

The plugin provides eight additional skills. Keep those managed by the marketplace rather than copying an older local plugin into the standalone skills tree. Python installation success covers the 33 standalone skills and five agents, not the account's marketplace state. Verify and report companion setup separately; an unavailable or disabled companion is not a passing plugin check. Retire an older local registration only with authority for its exact removal.

## Install Modes

### Full install

Use this for normal installs and every normal update. It is the default when no mode flag is provided.

Full install:

- installs the global coding-agent instructions into `$CODEX_HOME/AGENTS.md`
- copies custom agent definitions into `$CODEX_HOME/agents/`
- copies complete, self-contained skill packages into `$CODEX_HOME/skills/`

The global instruction body is always installed inside one clearly marked Coding Agent Playbook — Codex Edition section. Existing content outside that section is preserved. Re-running a full install replaces the existing marked section instead of appending a duplicate.

After a successful run, the installer records every managed support-file path and source SHA-256 in `$CODEX_HOME/.coding-agent-playbook-codex-managed-files.tsv`.

| Target condition | Installer action |
| --- | --- |
| Current managed support file matches its source. | Leave it unchanged. |
| Current managed support file differs, including a locally customized copy. | Back up the existing copy, then replace it with the current source. |
| Previously managed file was removed upstream and still matches its recorded hash. | Back it up, then retire it. |
| Previously managed file was removed upstream but its content was customized. | Preserve it and report a warning. |
| File was never recorded as managed and has no current source at that target. | Preserve it. |

An existing `.codex-agent-playbook-managed-files.tsv` is migrated after a successful update. On the first manifest-aware run, there is no prior ownership record: preserve unlisted files rather than guessing that they belong to the playbook.

When `USER_SKILLS_HOME` is not explicitly set, an update also migrates previously managed skill files from the former `$HOME/.agents/skills` default. Exact hash matches are backed up and retired after the new `$CODEX_HOME/skills` packages are installed; customized legacy files are preserved with a warning.

### Standalone local-CI routing migration

Full installs now carry the default local-validation route inside the managed global instructions and install the complete `local-ci-preflight` package. The installer still preserves instructions outside its marked section; it does not guess ownership of a separately installed routing block.

If this setup previously installed a standalone `local-ci-preflight:start` / `local-ci-preflight:end` block, reconcile it as a separate, authorized migration:

1. Complete a full install. Verify the managed global body matches the current source, includes the local-validation route, and all current managed support files match their source hashes.
2. Back up the installed `AGENTS.md`. Verify there is exactly one well-formed standalone block and its body exactly matches `skills/local-ci-preflight/assets/AGENTS.local-validation.md`.
3. Only then remove that exact superseded block. Preserve all other instructions outside the managed section. Recheck the canonical route, source parity, and repeat-install behavior.

Preserve and report a customized, malformed, or ambiguous block instead of deleting it. Do not retire standalone routing during support-only installation or when canonical global routing has not been verified. Fresh installs need no standalone block.

### Retired profile aliases

The duplicate `*-luna.toml` profiles have been removed. Use `planner`, `engineer`, `reviewer`, `tester`, and `docs`; these profiles now carry reusable role perspectives and explicit task-appropriate defaults. See the [routing policy](skills/subagent-orchestration/references/model-routing.md) for approved model/effort pairs and profile precedence. Update any custom prompts or configuration that select a corresponding `*_luna` name or `*-luna.toml` path to use the standard role name or file.

The existing manifest cleanup backs up and retires unchanged managed copies during an update. Customized or unlisted copies remain for manual review. The installer does not rewrite custom prompts or configuration; review those references before removing a preserved copy.

### Support-only install

Use this only when the user explicitly requests support-only mode and confirms that the full global instructions already live in Codex Personalization > Custom instructions. Do not infer support-only mode merely because an older installation or an existing `AGENTS.md` is present.

Support-only install:

- does not duplicate the full global instructions into `$CODEX_HOME/AGENTS.md`
- adds only a short reference-map pointer if useful
- still copies self-contained skills and custom agent definitions
- still updates the managed-file manifest and safely retires unchanged files removed from later playbook releases

## Human Install

Clone the repository and run the standard-library Python installer. It requires Python 3.8 or newer and no third-party packages. The PowerShell and Bash files are thin compatibility launchers that locate Python and run the same implementation.

### macOS / Linux / WSL

```bash
git clone https://github.com/ArcanEdge-AI/coding-agent-playbook-codex.git
cd coding-agent-playbook-codex
python3 install/install.py --full
```

Support-only mode:

```bash
python3 install/install.py --support-only
```

### Windows

```powershell
git clone https://github.com/ArcanEdge-AI/coding-agent-playbook-codex.git
cd coding-agent-playbook-codex
py -3 install/install.py --full
```

Support-only mode:

```powershell
py -3 install/install.py --support-only
```

## Agent Install Instructions

When an AI coding agent is asked to install this repo, it should:

1. Clone or fetch the repository from the provided URL.
2. Read this `INSTALL.md` file first.
3. Resolve `CODEX_HOME` and `USER_SKILLS_HOME`.
4. Inspect existing target files before writing.
5. Back up any existing file before changing it.
6. Use full install for both installation and update unless the user explicitly asks for support-only mode. Existing global instructions, markers, or support files are not permission to change modes.
7. Run `install/install.py` in the selected mode. Use the canonical installer rather than copying files manually; it manages marked instructions, backups, the manifest, retirement, and validation.
8. Validate the installed files.
9. Report exactly what changed, what was skipped, and where backups were written.

Do not modify arbitrary repositories during installation. Only use a temporary clone of this repository and user-level Codex configuration locations.

## Validation Checklist

After installation, verify:

- `$CODEX_HOME/AGENTS.md` exists or was intentionally left as a pointer-only file.
- `$CODEX_HOME/.coding-agent-playbook-codex-managed-files.tsv` exists and lists every current managed support file once.
- `$CODEX_HOME/skills/reference-doc-routing/references/engineering-design.md` exists.
- `$CODEX_HOME/skills/reference-doc-routing/references/templates/repository-AGENTS.md` exists.
- `$CODEX_HOME/skills/reference-doc-routing/references/reference-doc-routing.md` exists.
- `$CODEX_HOME/skills/subagent-orchestration/references/model-routing.md` exists.
- `$CODEX_HOME/skills/subagent-orchestration/references/subagents.md` exists.
- `$CODEX_HOME/skills/worktree-lifecycle/references/worktrees.md` exists.
- `$CODEX_HOME/skills/worktree-lifecycle/references/templates/worktree-manifest.md` exists.
- `$CODEX_HOME/skills/feature-branch-lifecycle/references/branching-rule.md` exists.
- `$CODEX_HOME/skills/multi-session-coordination/references/multi-session-coordination.md` exists.
- `$CODEX_HOME/skills/multi-session-coordination/references/templates/active-work-record.md` exists.
- `$CODEX_HOME/skills/task-graph-orchestration/references/templates/task-graph.md` exists.
- `$CODEX_HOME/agents/planner.toml` exists.
- `$CODEX_HOME/agents/engineer.toml` exists.
- `$CODEX_HOME/agents/reviewer.toml` exists.
- `$CODEX_HOME/agents/tester.toml` exists.
- `$CODEX_HOME/agents/docs.toml` exists.
- Every current playbook-managed `agents/*.toml` file explicitly defines `model` and `model_reasoning_effort`; unrelated user profiles are outside this validation scope.
- Installed reporting guidance preserves parent and peer task settings and omits destination-setting overrides from reports.
- Each of the five bundled roles has one profile under its standard name with an approved model/effort pair: `gpt-6.1-sol`/`low` (Light), `gpt-6.1-sol`/`medium`, `gpt-6.1-sol`/`high`, or `gpt-6-astra`/`xhigh` (Extra High).
- The installer does not change the main agent's configuration.
- `$CODEX_HOME/skills/subagent-orchestration/SKILL.md` exists.
- `$CODEX_HOME/skills/task-graph-orchestration/SKILL.md` exists.
- `$CODEX_HOME/skills/worktree-lifecycle/SKILL.md` exists.
- `$CODEX_HOME/skills/feature-branch-lifecycle/SKILL.md` exists.
- `$CODEX_HOME/skills/legacy-path-retirement/SKILL.md` exists.
- `$CODEX_HOME/skills/local-ci-preflight/` contains `SKILL.md`, `agents/openai.yaml`, `assets/LOCAL_VALIDATION.template.md`, and `assets/AGENTS.local-validation.md`.
- Full global instructions include the default local-validation route. An intentionally unconfigured project template is not a passing validation result; optional adapters do not replace required native profiles or remote acceptance.
- `$CODEX_HOME/skills/handoff/references/context-contract.md` exists.
- `$CODEX_HOME/skills/session-cleanup/references/post-session-cleanup-methodology.md` exists.
- `$CODEX_HOME/skills/multi-session-coordination/SKILL.md` exists.
- Each `SKILL.md` has `name` and `description` frontmatter.
- Every local resource path referenced by a skill resolves inside that skill package.
- TOML agent files are parseable if a TOML parser is available.
- Every current manifest entry matches its repository source SHA-256.
- Every formerly managed path was either absent, backed up and retired unchanged, or preserved with an explicit customization warning.

## Uninstall

This project does not currently ship an automatic uninstall command.

To remove the installed playbook manually:

1. Resolve the actual `CODEX_HOME` and `USER_SKILLS_HOME` used for installation. Preserve the manifest until the owned file targets are identified.
2. Inspect the manifest entries and the marked section in `AGENTS.md`. Do not infer ownership of a whole `agents/` or skill directory from its name.
3. Back up the files selected for removal. Preserve unrelated files, backups, and customized copies unless the user explicitly authorizes their removal. A manifest hash mismatch requires review, not automatic deletion.
4. Remove only the verified playbook-owned files. Remove a package directory only after confirming it contains no remaining user files or valuable artifacts; never recursively delete the entire skills or agents root.
5. If removing global instructions, delete only the section between the playbook start/end markers. Preserve all content outside it. Do not delete the entire `AGENTS.md` file merely because it contains the section.
6. After verifying the selected removals, remove the managed-file manifest only if no managed files remain. If customized files are retained, preserve the manifest as ownership evidence and report the remaining paths.

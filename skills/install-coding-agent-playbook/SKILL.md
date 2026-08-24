---
name: install-coding-agent-playbook
description: Install or update the optional Coding Agent Playbook companion configuration after its Codex plugin is installed. Use for lean global AGENTS.md guidance and personal Codex custom-agent profiles; the plugin already supplies skills and references.
---

# Install Coding Agent Playbook Companion Configuration

Use this skill only for the optional configuration that the installed plugin does not provide:

- the lean playbook-owned section in the user's global Codex `AGENTS.md`
- personal custom-agent TOMLs under the user's Codex home

The plugin is the canonical source for skills and their references. Do not copy the repository's `skills/` tree into a separate discovery location.

## Workflow

1. Resolve the plugin root from this selected `SKILL.md` path. Starting from the directory that contains this file, the plugin root is `../..`. Do not assume the user's task working directory is the plugin source.
2. Read the plugin root's `INSTALL.md` and inspect the current target files.
3. Resolve `CODEX_HOME` from the environment, falling back to the user's `.codex` directory.
4. Preview the requested mode with the matching dry-run command, using the absolute script path under the resolved plugin root.
5. Review the exact targets, backups, legacy managed files, preserved customizations, and any active `AGENTS.override.md` blocker reported by the preview.
6. Run the non-dry command only when the user's request authorizes the install or update.
7. Validate the installed global section when full mode is used, every custom-agent TOML, and the managed-file manifest.
8. Report changed, unchanged, retired, preserved, and backed-up files. Suggest restarting Codex or opening a new task if the updated configuration is not visible.

Use full mode by default. Full mode manages the lean global section plus custom agents. Use support-only mode only when the user explicitly wants custom agents without this playbook's global section; that mode removes an existing playbook-owned section while preserving unrelated content.

### macOS, Linux, or WSL

```bash
bash "$PLAYBOOK_PLUGIN_ROOT/install/install.sh" --full --dry-run
bash "$PLAYBOOK_PLUGIN_ROOT/install/install.sh" --full
```

Here, `PLAYBOOK_PLUGIN_ROOT` is the absolute plugin root resolved from this skill's installed path. For explicitly requested support-only configuration, replace `--full` with `--support-only`.

### Windows PowerShell

```powershell
pwsh -ExecutionPolicy Bypass -File "$PlaybookPluginRoot\install\install.ps1" -Full -DryRun
pwsh -ExecutionPolicy Bypass -File "$PlaybookPluginRoot\install\install.ps1" -Full
```

Here, `$PlaybookPluginRoot` is the absolute plugin root resolved from this skill's installed path. For explicitly requested support-only configuration, replace `-Full` with `-SupportOnly`.

## Boundaries

- Preserve unrelated and customized user files. Do not broaden the installer targets.
- Stop full mode when a non-empty global `AGENTS.override.md` would prevent Codex from loading the managed `AGENTS.md` section; do not claim the guidance is active.
- Do not place credentials, tokens, private keys, or other sensitive access material in configuration or backups.
- Stop on malformed managed markers or manifests instead of guessing how to repair them.
- Do not publish the plugin, change external systems, or delete broad user-owned directories as part of this skill.

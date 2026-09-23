# Prompt: Set Up Global Codex Support System

> This is an explicit support-only bootstrap prompt. Normal installs and updates should use full mode instead.

Use this only after the full global coding-agent instructions have already been added through Codex Personalization > Custom instructions.

```markdown
Install this repository's Codex support system in support-only mode.

The full global coding-agent instructions are already configured in Codex Personalization > Custom instructions. Do not duplicate them in `$CODEX_HOME/AGENTS.md`.

Read and follow `INSTALL.md` from this repository. Use the canonical standard-library Python installer:

- Windows: `py -3 install/install.py --support-only`
- macOS, Linux, or WSL: `python3 install/install.py --support-only`

Use `$CODEX_HOME` when set; otherwise use `~/.codex`. Install every self-contained skill under `$CODEX_HOME/skills` unless `USER_SKILLS_HOME` was explicitly configured, and install custom agent profiles under `$CODEX_HOME/agents`.

Preserve unrelated files and content. Let the installer create backups, update only the marked playbook section in `AGENTS.md`, migrate previously managed files, preserve customized legacy files, and validate installed hashes, skill-local references, and agent profiles.

Do not modify this repository while installing it. Report the resolved destinations, installed or unchanged files, backups, preserved customizations, validation results, and whether `AGENTS.override.md` may override the installed pointer.
```

Support-only mode is not an update shortcut. If the full global instructions are not already configured through Codex Personalization, use the normal full installation documented in `INSTALL.md`.

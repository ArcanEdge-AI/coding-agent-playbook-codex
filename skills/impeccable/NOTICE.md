# Third-Party Notices

This project includes content derived from third-party work, used under the terms of its original license.

## Platform Design Skills

The `skill/reference/ios.md` and `skill/reference/android.md` platform reference files are distilled from ehmo's `platform-design-skills` (Apple Human Interface Guidelines and Material Design 3 rules), rewritten in Impeccable's voice.

**Original work:** https://github.com/ehmo/platform-design-skills
**Original license:** MIT
**Author:** ehmo


## Codex Playbook adaptation

The skill, references, and scripts come from the Codex-compatible package in
[Impeccable Skill 4.8.0](https://github.com/pbakaus/impeccable/releases/tag/skill-v4.8.0),
commit `414603bf14c7a344edb466bb1f85690c77ce8b7d`.

Modified Markdown files carry a Codex Playbook adaptation notice. The changes
resolve the installed skill path, preserve host permissions, and map the
upstream helper contracts to the playbook's existing roles. The upstream
launchers and checksum manifest are included for engine 0.1.18. The installer
copies the skill package. Engine acquisition occurs through the launcher on use.

The modern-screenshot library and platform design guidance retain their MIT
notices in LICENSE.modern-screenshot and LICENSE.platform-design-skills.

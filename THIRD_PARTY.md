# Third-party skills and attribution

The playbook's original material remains MIT-licensed under [LICENSE](LICENSE). Imported third-party work keeps the license and attribution listed below. Inclusion does not claim original authorship or endorsement.

| Bundled skill | Source and credit | License | Packaging notes |
| --- | --- | --- | --- |
| [design-taste-frontend](skills/design-taste-frontend/SKILL.md) | [Taste Skill 2.1.5](https://github.com/Leonxlnx/taste-skill/releases/tag/v2.1.5), Leonxlnx | [MIT](skills/design-taste-frontend/LICENSE) | Bundled release with its scripts, data, assets, and references. See [NOTICE](skills/design-taste-frontend/NOTICE.md) for provenance and documentation changes. |
| [taste-new-website](skills/taste-new-website/SKILL.md) | Adapted from the [Taste prompt guide](https://www.tasteskill.dev/guide) | [MIT](skills/taste-new-website/LICENSE) | Local workflow adaptation with intake, project autofill, approval stages, and audits. Dependency lookup was adapted for sibling skill installation. |
| [taste-redesign-website](skills/taste-redesign-website/SKILL.md) | Adapted from the [Taste prompt guide](https://www.tasteskill.dev/guide) | [MIT](skills/taste-redesign-website/LICENSE) | Local workflow adaptation with protected content and staged approval. Dependency lookup was adapted for sibling skill installation. |
| [impeccable](skills/impeccable/SKILL.md) | [Impeccable Skill 4.8.0](https://github.com/pbakaus/impeccable/releases/tag/skill-v4.8.0), Paul Bakaus | [Apache-2.0](skills/impeccable/LICENSE) | Release package with upstream launchers and engine 0.1.18 checksums. See [NOTICE](skills/impeccable/NOTICE.md) for Codex adaptations. |
| [humanizer](skills/humanizer/SKILL.md) | [Humanizer 3.1.0](https://github.com/blader/humanizer/releases/tag/v3.1.0), Siqi Chen, based on [Wikipedia's Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) | [MIT](skills/humanizer/LICENSE) | Official skill and Codex metadata. See [NOTICE](skills/humanizer/NOTICE.md) for the source commit. |

Impeccable includes the MIT-licensed [modern-screenshot](https://github.com/qq15725/modern-screenshot) browser library and platform guidance derived from [ehmo/platform-design-skills](https://github.com/ehmo/platform-design-skills). Their license texts are retained inside its skill folder, so the installer carries them with the package.

The additional `multi-role-repo-review`, `platform-documentation`, and `technical-debt-auditor` packages are imports from the existing local workflow collection. Their inclusion is not a claim that all locally installed skills were originally authored for this repository.

The production collection includes twelve workflows migrated from the existing Copilot skill setup and the separately authored `production-readiness-report` workflow. Original authorship of the migrated twelve was not recorded. The QA and orchestration instructions were aligned with this playbook's E2E retention and bounded-delegation policies.

The [Intuitive Software Design companion](plugins/README.md) is the maintained marketplace release published by ArcanEdge AI under Apache-2.0. Its skills are not vendored into this repository. Marketplace installation retains its own license, notices, and artwork terms.

The versions above identify the bundled copies. Follow the [upstream refresh instructions](INSTALL.md#refresh-third-party-skills) for each install or update.

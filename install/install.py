#!/usr/bin/env python3
"""Cross-platform installer for the Coding Agent Playbook — Codex Edition."""

from __future__ import annotations

import argparse
import hashlib
import os
import re
import shutil
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path, PurePosixPath
from tempfile import TemporaryDirectory
from typing import List, Optional

try:
    import tomllib
except ImportError:  # Python 3.10 and earlier
    tomllib = None


START_MARKER = "<!-- coding-agent-playbook-codex:start -->"
END_MARKER = "<!-- coding-agent-playbook-codex:end -->"
LEGACY_START_MARKER = "<!-- codex-agent-playbook:start -->"
LEGACY_END_MARKER = "<!-- codex-agent-playbook:end -->"
MANIFEST_HEADER = "# coding-agent-playbook-codex managed files v1"
APPROVED_MODEL_EFFORTS = {
    ("gpt-6.1-sol", "low"),
    ("gpt-6.1-sol", "medium"),
    ("gpt-6.1-sol", "high"),
    ("gpt-6-astra", "xhigh"),
}
RESOURCE_PATTERN = re.compile(
    r"(?<![A-Za-z0-9_./-])(?:<skill(?:-(?:base-)?dir)?>/)?"
    r"(?P<path>(?:references|reference|scripts|assets|agents|library)/[A-Za-z0-9._/-]+)"
)


@dataclass(frozen=True)
class ManifestEntry:
    root: str
    path: str
    digest: str

    @property
    def key(self) -> tuple[str, str]:
        return self.root, self.path


class Installer:
    def __init__(self, mode: str, dry_run: bool, skills_source: Optional[Path] = None) -> None:
        self.mode = mode
        self.dry_run = dry_run
        self.script_dir = Path(__file__).resolve().parent
        self.repo_root = self.script_dir.parent
        self.codex_home = Path(os.environ.get("CODEX_HOME", Path.home() / ".codex")).expanduser().resolve()
        explicit_skills_home = os.environ.get("USER_SKILLS_HOME")
        self.user_skills_home = Path(explicit_skills_home).expanduser().resolve() if explicit_skills_home else self.codex_home / "skills"
        self.legacy_user_skills_home = (Path.home() / ".agents" / "skills").resolve()
        self.migrate_legacy_skills = not explicit_skills_home and self.user_skills_home != self.legacy_user_skills_home
        self.timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        self.manifest_path = self.codex_home / ".coding-agent-playbook-codex-managed-files.tsv"
        self.legacy_manifest_path = self.codex_home / ".codex-agent-playbook-managed-files.tsv"
        self.global_instructions = self.repo_root / "custom-instructions" / "global-coding-agent-instructions.md"
        self.pointer_source = self.script_dir / "support-only-pointer.md"
        self.target_agents_md = self.codex_home / "AGENTS.md"
        self.skills_source = skills_source if skills_source is not None else self.repo_root / "skills"
        self.managed_roots = {
            "agents": (self.repo_root / "agents", self.codex_home / "agents"),
            "skills": (self.skills_source, self.user_skills_home),
        }
        self.destination_roots = {
            name: destination for name, (_, destination) in self.managed_roots.items()
        }
        # Recognize the former loose-reference destination only for safe migration.
        self.destination_roots["references"] = self.codex_home / "references"
        self.playbook_skill_names = sorted(path.name for path in self.skills_source.iterdir() if path.is_dir())
        self.playbook_agent_names = sorted(path.name for path in (self.repo_root / "agents").glob("*.toml"))

    def say(self, message: str = "") -> None:
        print(message)

    def sha256(self, path: Path) -> str:
        digest = hashlib.sha256()
        with path.open("rb") as source:
            for chunk in iter(lambda: source.read(1024 * 1024), b""):
                digest.update(chunk)
        return digest.hexdigest()

    def backup_file(self, path: Path) -> None:
        if not path.is_file():
            return
        backup = path.with_name(f"{path.name}.bak.{self.timestamp}")
        if self.dry_run:
            self.say(f"[dry-run] Would back up {path} -> {backup}")
            return
        self.say(f"Backing up {path} -> {backup}")
        shutil.copy2(path, backup)

    def copy_file(self, source: Path, destination: Path) -> None:
        if destination.is_file() and self.sha256(source) == self.sha256(destination):
            self.say(f"Unchanged {destination}")
            return
        self.backup_file(destination)
        if self.dry_run:
            self.say(f"[dry-run] Would install {destination}")
            return
        self.say(f"Installing {destination}")
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)

    def safe_relative_path(self, value: str) -> PurePosixPath:
        if not value or any(character in value for character in "\t\r\n"):
            raise ValueError(f"Unsafe managed-file manifest path: {value!r}")
        normalized = value.replace("\\", "/")
        path = PurePosixPath(normalized)
        if path.is_absolute() or any(part in ("", ".", "..") for part in path.parts):
            raise ValueError(f"Unsafe managed-file manifest path: {value!r}")
        return path

    def destination_for(self, entry: ManifestEntry) -> Path:
        if entry.root not in self.destination_roots:
            raise ValueError(f"Unknown managed-file root {entry.root!r}")
        relative = self.safe_relative_path(entry.path)
        destination_root = self.destination_roots[entry.root].resolve()
        destination = destination_root.joinpath(*relative.parts).resolve()
        if destination_root not in destination.parents:
            raise ValueError(f"Managed-file destination escapes {destination_root}: {entry.path!r}")
        return destination

    def build_manifest(self) -> list[ManifestEntry]:
        entries: list[ManifestEntry] = []
        for root_name, (source_root, _) in self.managed_roots.items():
            for source in sorted(path for path in source_root.rglob("*") if path.is_file()):
                relative = source.relative_to(source_root).as_posix()
                self.safe_relative_path(relative)
                entries.append(ManifestEntry(root_name, relative, self.sha256(source)))
        return entries

    def read_manifest(self, path: Path) -> dict[tuple[str, str], ManifestEntry]:
        if not path.is_file():
            self.say("No previous managed-file manifest found; existing unlisted files will be preserved.")
            return {}
        entries: dict[tuple[str, str], ManifestEntry] = {}
        for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
            if not line or line.startswith("#"):
                continue
            parts = line.split("\t")
            if len(parts) != 3:
                raise ValueError(f"Malformed managed-file manifest at {path}:{line_number}")
            root, relative, digest = parts
            if root not in self.destination_roots:
                raise ValueError(f"Unknown managed-file root {root!r} at {path}:{line_number}")
            self.safe_relative_path(relative)
            if not re.fullmatch(r"[0-9a-fA-F]{64}", digest):
                raise ValueError(f"Invalid SHA-256 at {path}:{line_number}")
            entry = ManifestEntry(root, relative, digest.lower())
            if entry.key in entries:
                raise ValueError(f"Duplicate managed-file manifest entry {entry.key!r} at {path}:{line_number}")
            entries[entry.key] = entry
        return entries

    def write_manifest(self, entries: list[ManifestEntry]) -> None:
        content = "\n".join(
            [MANIFEST_HEADER, *(f"{entry.root}\t{entry.path}\t{entry.digest}" for entry in entries), ""]
        )
        if self.manifest_path.is_file() and self.manifest_path.read_text(encoding="utf-8") == content:
            self.say(f"Unchanged {self.manifest_path}")
            return
        self.backup_file(self.manifest_path)
        if self.dry_run:
            self.say(f"[dry-run] Would write managed-file manifest: {self.manifest_path}")
            return
        self.say(f"Writing managed-file manifest: {self.manifest_path}")
        self.manifest_path.parent.mkdir(parents=True, exist_ok=True)
        with self.manifest_path.open("w", encoding="utf-8", newline="\n") as destination:
            destination.write(content)

    def verify_managed_files(self, entries: list[ManifestEntry]) -> None:
        if self.dry_run:
            self.say(f"[dry-run] Would verify {len(entries)} managed files against source SHA-256 hashes.")
            return
        for entry in entries:
            destination = self.destination_for(entry)
            if not destination.is_file():
                raise FileNotFoundError(f"Managed file was not installed: {destination}")
            if self.sha256(destination) != entry.digest:
                raise ValueError(f"Managed file does not match its source: {destination}")
        self.say(f"OK managed-file content: {len(entries)}/{len(entries)} exact SHA-256 matches")

    def retire_stale_files(
        self,
        previous: dict[tuple[str, str], ManifestEntry],
        current: list[ManifestEntry],
    ) -> None:
        current_keys = {entry.key for entry in current}
        for key, entry in previous.items():
            if key in current_keys:
                continue
            destination = self.destination_for(entry)
            if not destination.is_file():
                self.say(f"Formerly managed file already absent: {destination}")
                continue
            if self.sha256(destination) != entry.digest:
                self.say(f"Preserving customized formerly managed file: {destination}")
                continue
            self.backup_file(destination)
            if self.dry_run:
                self.say(f"[dry-run] Would retire formerly managed file: {destination}")
            else:
                self.say(f"Retiring formerly managed file: {destination}")
                destination.unlink()

    def retire_legacy_skills(self, previous: dict[tuple[str, str], ManifestEntry]) -> None:
        if not self.migrate_legacy_skills or not self.legacy_user_skills_home.is_dir():
            return
        legacy_root = self.legacy_user_skills_home.resolve()
        for entry in previous.values():
            if entry.root != "skills":
                continue
            relative = self.safe_relative_path(entry.path)
            destination = legacy_root.joinpath(*relative.parts).resolve()
            if legacy_root not in destination.parents:
                raise ValueError(f"Legacy skill destination escapes {legacy_root}: {entry.path!r}")
            if not destination.is_file():
                continue
            if self.sha256(destination) != entry.digest:
                self.say(f"Preserving customized legacy skill file: {destination}")
                continue
            self.backup_file(destination)
            if self.dry_run:
                self.say(f"[dry-run] Would retire legacy managed skill file: {destination}")
            else:
                self.say(f"Retiring legacy managed skill file: {destination}")
                destination.unlink()

    def retire_legacy_manifest(self) -> None:
        if not self.legacy_manifest_path.is_file():
            return
        self.backup_file(self.legacy_manifest_path)
        if self.dry_run:
            self.say(f"[dry-run] Would retire legacy managed-file manifest: {self.legacy_manifest_path}")
        else:
            self.say(f"Retiring legacy managed-file manifest: {self.legacy_manifest_path}")
            self.legacy_manifest_path.unlink()

    def validate_skill_references(self, skills_root: Path, skill_names: Optional[List[str]] = None) -> None:
        names = skill_names or sorted(path.name for path in skills_root.iterdir() if path.is_dir())
        checked = 0
        for name in names:
            skill_root = (skills_root / name).resolve()
            if not skill_root.is_dir():
                raise FileNotFoundError(f"Missing skill package: {skill_root}")
            for markdown in sorted(skill_root.rglob("*.md")):
                text = markdown.read_text(encoding="utf-8")
                for match in RESOURCE_PATTERN.finditer(text):
                    relative_text = match.group("path").rstrip(".,:;")
                    relative = self.safe_relative_path(relative_text)
                    resolved = skill_root.joinpath(*relative.parts).resolve()
                    if skill_root not in resolved.parents:
                        raise ValueError(f"Skill resource reference escapes package {name!r}: {relative_text}")
                    if not resolved.is_file():
                        raise FileNotFoundError(f"Missing skill resource referenced by {markdown}: {relative_text}")
                    checked += 1
        self.say(f"OK skill-local references: {checked} resolved paths")

    def validate_agents(self, agents_root: Path, agent_names: Optional[List[str]] = None) -> None:
        names = agent_names if agent_names is not None else sorted(path.name for path in agents_root.glob("*.toml"))
        checked = 0
        for name in names:
            path = agents_root / name
            text = path.read_text(encoding="utf-8")
            if tomllib is not None:
                data = tomllib.loads(text)
            else:
                # Bundled profiles use simple quoted top-level settings.
                data = {}
                for key in ("model", "model_reasoning_effort"):
                    match = re.search(
                        rf"""^{key}\s*=\s*(["'])([^"']+)\1\s*(?:#.*)?$""", text, re.MULTILINE
                    )
                    if match:
                        data[key] = match.group(2)
            route = (data.get("model"), data.get("model_reasoning_effort"))
            if route not in APPROVED_MODEL_EFFORTS:
                raise ValueError(f"Agent profile must declare an approved model/effort pair: {path}")
            checked += 1
        self.say(f"OK agent profiles: {checked} TOML files use approved task-based routes")

    def validate_taste_workflows(self) -> None:
        taste = self.skills_source / "design-taste-frontend"
        guide = (taste / "SKILL.md").read_text(encoding="utf-8")
        for step in ("Read the brief and the project", "Write the argument", "Draw the direction",
                     "Build it, still", "Gate", "Look", "Move", "Record the before", "Prove it"):
            if step not in guide:
                raise ValueError(f"Taste release does not document the workflow step {step!r}")
        for script, flags in {
            "draw.mjs": ("sector", "sections", "options", "direction", "keep"),
            "lint.mjs": (),
            "inspect.mjs": ("out", "widths"),
            "scenes.mjs": ("out",),
        }.items():
            text = (taste / "scripts" / script).read_text(encoding="utf-8")
            if not text.strip():
                raise ValueError(f"Taste workflow script is empty: {script}")
            for flag in flags:
                if not re.search(rf"['\"]{flag}['\"]", text):
                    raise ValueError(f"Taste release lacks the expected --{flag} option in {script}")
        for name in ("taste-new-website", "taste-redesign-website"):
            workflow = self.skills_source / name / "SKILL.md"
            for relative in re.findall(r"\]\(\.\./design-taste-frontend/([^\s)]+)\)", workflow.read_text(encoding="utf-8")):
                target = taste.joinpath(*self.safe_relative_path(relative).parts).resolve()
                if taste.resolve() not in target.parents or not target.is_file():
                    raise ValueError(f"{name} references an unavailable Taste resource: {relative}")
        self.say("OK Taste workflow resources: new website and redesign")

    def add_or_replace_section(self, target: Path, title: str, body: str) -> None:
        raw = target.read_bytes() if target.is_file() else b""
        newline = "\r\n" if b"\r\n" in raw else "\n"
        existing = raw.decode("utf-8") if raw else ""
        lines = existing.splitlines()
        marker_pairs = []
        for start, end in ((START_MARKER, END_MARKER), (LEGACY_START_MARKER, LEGACY_END_MARKER)):
            starts = [index for index, line in enumerate(lines) if line == start]
            ends = [index for index, line in enumerate(lines) if line == end]
            if starts or ends:
                if len(starts) != 1 or len(ends) != 1 or ends[0] <= starts[0]:
                    raise ValueError(f"Malformed Coding Agent Playbook markers in {target}; no changes were made.")
                marker_pairs.append((starts[0], ends[0]))
        if len(marker_pairs) > 1:
            raise ValueError(f"Malformed Coding Agent Playbook markers in {target}; no changes were made.")

        normalized_body = body.replace("\r\n", "\n").rstrip("\n").replace("\n", newline)
        section = newline.join((START_MARKER, f"# {title}", "", normalized_body, END_MARKER))
        if marker_pairs:
            start_index, end_index = marker_pairs[0]
            replacement = lines[:start_index] + section.splitlines() + lines[end_index + 1 :]
            content = newline.join(replacement) + (newline if existing.endswith(("\n", "\r")) else "")
        else:
            separator = newline * 2 if existing else ""
            content = existing.rstrip("\r\n") + separator + section + newline

        if existing == content:
            self.say(f"Unchanged {target}")
            return
        self.backup_file(target)
        if self.dry_run:
            self.say(f"[dry-run] Would update {title} in {target}")
            return
        target.parent.mkdir(parents=True, exist_ok=True)
        with target.open("w", encoding="utf-8", newline="") as destination:
            destination.write(content)

    def run(self) -> None:
        self.say("Coding Agent Playbook - Codex Edition installer")
        self.say(f"Mode: {self.mode}")
        self.say(f"Repository: {self.repo_root}")
        self.say(f"CODEX_HOME: {self.codex_home}")
        self.say(f"USER_SKILLS_HOME: {self.user_skills_home}")
        self.say(f"Managed-file manifest: {self.manifest_path}")

        for required in (self.global_instructions, self.pointer_source):
            if not required.is_file():
                raise FileNotFoundError(f"Missing installer source: {required}")

        self.validate_skill_references(self.skills_source)
        self.validate_taste_workflows()
        self.validate_agents(self.repo_root / "agents")
        current = self.build_manifest()
        previous_manifest_path = self.manifest_path
        if not self.manifest_path.is_file() and self.legacy_manifest_path.is_file():
            previous_manifest_path = self.legacy_manifest_path
            self.say(f"Migrating legacy managed-file manifest: {self.legacy_manifest_path}")
        previous = self.read_manifest(previous_manifest_path)
        files = [(self.managed_roots[entry.root][0] / entry.path, self.destination_for(entry)) for entry in current]

        if (self.codex_home / "AGENTS.override.md").is_file():
            self.say("Notice: AGENTS.override.md exists and may override AGENTS.md")

        if self.mode == "full":
            body = self.global_instructions.read_text(encoding="utf-8")
            title = "Coding Agent Playbook - Codex Edition Global Instructions"
        else:
            body = self.pointer_source.read_text(encoding="utf-8")
            title = "Global Reference Documents and Subagent Support"
        self.add_or_replace_section(self.target_agents_md, title, body)

        for source, destination in files:
            self.copy_file(source, destination)
        self.verify_managed_files(current)
        if self.dry_run:
            self.say(f"[dry-run] Would validate installed skill-local references under {self.user_skills_home}")
        else:
            self.validate_skill_references(self.user_skills_home, self.playbook_skill_names)
            self.validate_agents(self.codex_home / "agents", self.playbook_agent_names)
        self.retire_stale_files(previous, current)
        self.retire_legacy_skills(previous)
        self.write_manifest(current)
        self.retire_legacy_manifest()

        self.say()
        self.say("Companion marketplace plugin: Intuitive Software Design is managed separately; see INSTALL.md.")
        if self.dry_run:
            self.say("Dry run complete. No files were changed.")
        else:
            self.say("Install complete. Restart Codex or start a new session if needed so new instructions, skills, and agents are loaded.")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--full", action="store_true", help="Install full global instructions (default).")
    mode.add_argument("--support-only", action="store_true", help="Install the support pointer, skills, and agent profiles without the full global instructions.")
    parser.add_argument("--dry-run", action="store_true", help="Report changes without writing them.")
    parser.add_argument("--bundled-skills", action="store_true", help="Use the bundled third-party versions without contacting GitHub.")
    return parser.parse_args()


def main() -> int:
    if sys.version_info < (3, 8):
        print("ERROR: Python 3.8 or newer is required.", file=sys.stderr)
        return 1
    args = parse_args()
    mode = "support-only" if args.support_only else "full"
    try:
        if args.bundled_skills:
            print("Third-party skills: using the bundled releases listed in THIRD_PARTY.md.")
            Installer(mode=mode, dry_run=args.dry_run).run()
        else:
            # The checkout can be read-only. Keep release staging and bytecode out of it.
            sys.dont_write_bytecode = True
            from skill_releases import stage_skills

            bundled = Path(__file__).resolve().parent.parent / "skills"
            with TemporaryDirectory(prefix="codex-playbook-skills-") as temporary:
                staged = Path(temporary)
                stage_skills(bundled, staged)
                Installer(mode=mode, dry_run=args.dry_run, skills_source=staged).run()
    except (OSError, ValueError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

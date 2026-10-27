#!/usr/bin/env python3
"""Create and validate deterministic technical-debt audit artifacts.

The script reads repositories and writes only to explicit artifact paths. It never
changes audited source. Use ``inventory`` to create a baseline inventory and
ledger, ``reconcile`` to prove ledger coverage, and ``validate-report`` to check
finding/report consistency.
"""

from __future__ import annotations

import argparse
import csv
import fnmatch
import os
import re
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Iterable, Sequence


INVENTORY_FIELDS = (
    "repository",
    "path",
    "origin",
    "size_bytes",
    "classification",
)
LEDGER_FIELDS = INVENTORY_FIELDS + (
    "review_status",
    "detailed_review",
    "finding_ids",
    "notes",
)

REVIEW_STATUSES = {"pending", "accounted", "unable"}
DETAILED_REVIEW_STATUSES = {"pending", "yes", "no"}
FINDING_ID_RE = re.compile(r"TD-\d{3,}", re.IGNORECASE)

SOURCE_EXTENSIONS = {
    ".c", ".cc", ".clj", ".cpp", ".cs", ".dart", ".ex", ".exs", ".fs",
    ".fsx", ".go", ".h", ".hpp", ".java", ".js", ".jsx", ".kt", ".kts",
    ".lua", ".m", ".mm", ".php", ".pl", ".pm", ".py", ".r", ".rb",
    ".rs", ".scala", ".sh", ".sql", ".swift", ".ts", ".tsx", ".vue",
}
DOC_EXTENSIONS = {".adoc", ".md", ".mdx", ".rst", ".txt"}
CONFIG_EXTENSIONS = {".cfg", ".conf", ".ini", ".json", ".toml", ".xml", ".yaml", ".yml"}
BINARY_EXTENSIONS = {
    ".7z", ".a", ".apk", ".bin", ".class", ".dll", ".dmg", ".exe", ".jar",
    ".lib", ".o", ".obj", ".pdf", ".so", ".wasm", ".whl", ".zip",
}
ASSET_EXTENSIONS = {
    ".avif", ".bmp", ".eot", ".gif", ".ico", ".jpeg", ".jpg", ".mov",
    ".mp3", ".mp4", ".ogg", ".otf", ".png", ".svg", ".ttf", ".wav",
    ".webm", ".webp", ".woff", ".woff2",
}
VENDOR_SEGMENTS = {"node_modules", "vendor", "third_party", "third-party"}
GENERATED_SEGMENTS = {
    ".next", ".nuxt", ".pytest_cache", ".ruff_cache", ".turbo", "bin", "build",
    "coverage", "dist", "generated", "obj", "out", "target",
}
DEPENDENCY_MANIFESTS = {
    "build.gradle", "build.gradle.kts", "cargo.toml", "composer.json", "gemfile",
    "go.mod", "package.json", "pom.xml", "pyproject.toml", "requirements.txt",
}
LOCK_FILES = {
    "cargo.lock", "composer.lock", "gemfile.lock", "go.sum", "package-lock.json",
    "pnpm-lock.yaml", "poetry.lock", "uv.lock", "yarn.lock",
}
CONFIG_NAMES = {
    ".editorconfig", ".gitattributes", ".gitignore", "dockerfile", "makefile",
    "tsconfig.json", "vite.config.js", "vite.config.ts",
}

REQUIRED_REPORT_SECTIONS = tuple(chr(code) for code in range(ord("A"), ord("P") + 1))
REQUIRED_FINDING_FIELDS = (
    "Repository", "Area", "Category", "Severity", "Priority", "Effort",
    "Blast Radius", "Evidence State", "Evidence Sources",
)
REQUIRED_FINDING_SECTIONS = (
    "Evidence", "Current Behavior", "Why This Is Technical Debt", "Impact",
    "GitNexus Context", "Source Verification", "Recommended Direction",
    "Dependencies / Sequencing",
)
KNOWN_PLACEHOLDERS = (
    "[System or repository]", "[Single Repository / Multi-Repository / Workspace-System / Targeted]",
    "[Repositories, paths, and categories]", "[YYYY-MM-DD]",
    "[Complete / In progress / Targeted complete]", "[Absolute path or durable link]",
    "[Repository]", "[Area]", "[Category]", "[Critical / High / Medium / Low]",
    "[P0 / P1 / P2 / P3]", "[Small / Medium / Large]",
    "[Local / Module / Repository / Multi-repository]",
    "[Confirmed / Strongly Supported / Needs Verification]", "[S / G / T / D / C / H]",
)


class AuditArtifactError(Exception):
    """A clear user-facing validation or inventory failure."""


def parse_repo(value: str) -> tuple[str, Path]:
    if "=" not in value:
        raise argparse.ArgumentTypeError("Repository must use NAME=/absolute/path format.")
    name, raw_path = value.split("=", 1)
    name = name.strip()
    if not name:
        raise argparse.ArgumentTypeError("Repository name cannot be empty.")
    path = Path(raw_path).expanduser().resolve()
    if not path.is_dir():
        raise argparse.ArgumentTypeError(f"Repository path is not a directory: {path}")
    return name, path


def run_git(root: Path, *args: str) -> list[str]:
    completed = subprocess.run(
        ["git", "-C", str(root), *args],
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if completed.returncode != 0:
        message = completed.stderr.decode("utf-8", errors="replace").strip()
        raise AuditArtifactError(f"git {' '.join(args)} failed for {root}: {message}")
    return [
        item.decode("utf-8", errors="surrogateescape")
        for item in completed.stdout.split(b"\0")
        if item
    ]


def is_git_root(root: Path) -> bool:
    completed = subprocess.run(
        ["git", "-C", str(root), "rev-parse", "--show-toplevel"],
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        text=True,
    )
    if completed.returncode != 0:
        return False
    top = Path(completed.stdout.strip()).resolve()
    if top != root:
        raise AuditArtifactError(
            f"{root} is inside Git repository {top}; pass the repository root explicitly."
        )
    return True


def excluded(path: str, patterns: Sequence[str]) -> bool:
    return any(fnmatch.fnmatch(path, pattern) for pattern in patterns)


def git_inventory(root: Path, include_ignored: bool) -> dict[str, str]:
    origins: dict[str, str] = {}
    for path in run_git(root, "ls-files", "--cached", "-z"):
        origins[path.replace("\\", "/")] = "tracked"
    for path in run_git(root, "ls-files", "--others", "--exclude-standard", "-z"):
        origins.setdefault(path.replace("\\", "/"), "untracked")
    if include_ignored:
        for path in run_git(
            root, "ls-files", "--others", "--ignored", "--exclude-standard", "-z"
        ):
            origins.setdefault(path.replace("\\", "/"), "ignored")
    return origins


def directory_inventory(root: Path) -> dict[str, str]:
    origins: dict[str, str] = {}
    for current, directory_names, file_names in os.walk(root, followlinks=False):
        current_path = Path(current)
        kept_directories: list[str] = []
        for directory_name in directory_names:
            candidate = current_path / directory_name
            if directory_name == ".git":
                continue
            if candidate.is_symlink():
                relative = candidate.relative_to(root).as_posix()
                origins[relative] = "directory"
            else:
                kept_directories.append(directory_name)
        directory_names[:] = kept_directories
        for file_name in file_names:
            relative = (current_path / file_name).relative_to(root).as_posix()
            origins[relative] = "directory"
    return origins


def classify(relative_path: str) -> str:
    path = Path(relative_path)
    name = path.name.lower()
    suffix = path.suffix.lower()
    segments = {segment.lower() for segment in path.parts[:-1]}

    if segments & VENDOR_SEGMENTS:
        return "vendor"
    if segments & GENERATED_SEGMENTS or name.endswith((".generated.cs", ".g.cs", ".min.js", ".min.css")):
        return "generated"
    if name in LOCK_FILES:
        return "dependency-lock"
    if name in DEPENDENCY_MANIFESTS:
        return "dependency-manifest"
    if (
        segments & {"test", "tests", "spec", "specs", "__tests__"}
        or re.search(r"(?:^|[._-])(test|tests|spec)(?:[._-]|$)", name)
    ):
        return "test"
    if suffix in BINARY_EXTENSIONS:
        return "binary"
    if suffix in ASSET_EXTENSIONS:
        return "asset"
    if suffix in DOC_EXTENSIONS or segments & {"doc", "docs", "documentation"}:
        return "documentation"
    if name in CONFIG_NAMES or suffix in CONFIG_EXTENSIONS:
        return "config"
    if suffix in SOURCE_EXTENSIONS:
        return "source"
    return "other"


def within(candidate: Path, parent: Path) -> bool:
    try:
        candidate.resolve().relative_to(parent.resolve())
        return True
    except ValueError:
        return False


def ensure_output_safety(outputs: Sequence[Path], roots: Sequence[Path], allow_inside: bool) -> None:
    resolved = [path.expanduser().resolve() for path in outputs]
    if len(set(resolved)) != len(resolved):
        raise AuditArtifactError("Inventory and ledger paths must be different.")
    if not allow_inside:
        for output in resolved:
            for root in roots:
                if within(output, root):
                    raise AuditArtifactError(
                        f"Refusing to write audit state inside audited repository {root}: {output}"
                    )


def write_csv(path: Path, fields: Sequence[str], rows: Iterable[dict[str, object]], force: bool) -> None:
    path = path.expanduser().resolve()
    if path.exists() and not force:
        raise AuditArtifactError(f"Output already exists (use --force deliberately): {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.name}.tmp")
    try:
        with temporary.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
            writer.writeheader()
            writer.writerows(rows)
        temporary.replace(path)
    finally:
        if temporary.exists():
            temporary.unlink()


def inventory_command(args: argparse.Namespace) -> int:
    repositories = args.repo
    names = [name for name, _ in repositories]
    roots = [root for _, root in repositories]
    if len(set(names)) != len(names):
        raise AuditArtifactError("Repository names must be unique.")
    if len(set(roots)) != len(roots):
        raise AuditArtifactError("Repository paths must be unique.")

    inventory_path = Path(args.inventory)
    ledger_path = Path(args.ledger)
    ensure_output_safety(
        [inventory_path, ledger_path], roots, args.allow_output_inside_repo
    )
    if not args.force:
        existing = [
            path.expanduser().resolve()
            for path in (inventory_path, ledger_path)
            if path.expanduser().resolve().exists()
        ]
        if existing:
            raise AuditArtifactError(
                "Output already exists (use --force deliberately): "
                + ", ".join(str(path) for path in existing)
            )

    rows: list[dict[str, object]] = []
    for repository, root in repositories:
        origins = git_inventory(root, args.include_ignored) if is_git_root(root) else directory_inventory(root)
        for relative_path, origin in sorted(origins.items()):
            if excluded(relative_path, args.exclude):
                continue
            file_path = root / Path(relative_path)
            try:
                size = file_path.lstat().st_size
            except OSError as error:
                raise AuditArtifactError(f"Cannot stat {file_path}: {error}") from error
            rows.append(
                {
                    "repository": repository,
                    "path": relative_path,
                    "origin": origin,
                    "size_bytes": size,
                    "classification": classify(relative_path),
                }
            )

    rows.sort(key=lambda row: (str(row["repository"]), str(row["path"])))
    ledger_rows = [
        {
            **row,
            "review_status": "pending",
            "detailed_review": "pending",
            "finding_ids": "",
            "notes": "",
        }
        for row in rows
    ]
    write_csv(inventory_path, INVENTORY_FIELDS, rows, args.force)
    write_csv(ledger_path, LEDGER_FIELDS, ledger_rows, args.force)
    print(f"Created inventory: {inventory_path.resolve()} ({len(rows)} files)")
    print(f"Created ledger: {ledger_path.resolve()} ({len(ledger_rows)} pending rows)")
    if not args.include_ignored:
        print("Ignored files were not inventoried; record the reviewed ignore/exclusion policy in scope.md.")
    return 0


def read_csv(path: Path, required_fields: Sequence[str]) -> list[dict[str, str]]:
    if not path.is_file():
        raise AuditArtifactError(f"CSV does not exist: {path}")
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        fields = reader.fieldnames or []
        missing = [field for field in required_fields if field not in fields]
        if missing:
            raise AuditArtifactError(f"{path} is missing columns: {', '.join(missing)}")
        return list(reader)


def indexed(rows: Sequence[dict[str, str]], label: str) -> tuple[dict[tuple[str, str], dict[str, str]], list[str]]:
    result: dict[tuple[str, str], dict[str, str]] = {}
    errors: list[str] = []
    for number, row in enumerate(rows, start=2):
        key = (row["repository"].strip(), row["path"].strip())
        if not all(key):
            errors.append(f"{label} row {number} has an empty repository or path.")
        elif key in result:
            errors.append(f"{label} has duplicate key {key[0]}:{key[1]}.")
        else:
            result[key] = row
    return result, errors


def reconcile_command(args: argparse.Namespace) -> int:
    inventory_rows = read_csv(Path(args.inventory), INVENTORY_FIELDS)
    ledger_rows = read_csv(Path(args.ledger), LEDGER_FIELDS)
    inventory, errors = indexed(inventory_rows, "Inventory")
    ledger, ledger_errors = indexed(ledger_rows, "Ledger")
    errors.extend(ledger_errors)

    missing = sorted(set(inventory) - set(ledger))
    unknown = sorted(set(ledger) - set(inventory))
    errors.extend(f"Ledger is missing inventory item {repo}:{path}." for repo, path in missing)
    errors.extend(f"Ledger contains unknown item {repo}:{path}." for repo, path in unknown)

    counts: dict[str, Counter[str]] = defaultdict(Counter)
    for key in sorted(set(inventory) & set(ledger)):
        baseline = inventory[key]
        row = ledger[key]
        repo, path = key
        counts[repo]["discovered"] += 1
        for field in ("origin", "size_bytes"):
            if row[field].strip() != baseline[field].strip():
                errors.append(f"{repo}:{path} changed baseline field {field} in the ledger.")

        classification = row["classification"].strip()
        review_status = row["review_status"].strip().lower()
        detailed_review = row["detailed_review"].strip().lower()
        notes = row["notes"].strip()
        finding_ids = row["finding_ids"].strip()

        if not classification:
            errors.append(f"{repo}:{path} has no classification.")
        if review_status not in REVIEW_STATUSES:
            errors.append(f"{repo}:{path} has invalid review_status '{review_status}'.")
            continue
        if detailed_review not in DETAILED_REVIEW_STATUSES:
            errors.append(f"{repo}:{path} has invalid detailed_review '{detailed_review}'.")
            continue
        if review_status == "pending":
            counts[repo]["pending"] += 1
            if detailed_review != "pending":
                errors.append(f"{repo}:{path} is pending but detailed_review is not pending.")
        elif review_status == "accounted":
            counts[repo]["accounted"] += 1
            if detailed_review == "yes":
                counts[repo]["detailed"] += 1
            elif detailed_review == "no":
                counts[repo]["classified_only"] += 1
                if not notes:
                    errors.append(f"{repo}:{path} is classification-only without a reason in notes.")
            else:
                errors.append(f"{repo}:{path} is accounted but detailed_review remains pending.")
        elif review_status == "unable":
            counts[repo]["accounted"] += 1
            counts[repo]["unable"] += 1
            if detailed_review != "no":
                errors.append(f"{repo}:{path} is unable but detailed_review is not no.")
            if not notes:
                errors.append(f"{repo}:{path} is unable without an explanation in notes.")

        if finding_ids:
            tokens = [token.upper() for token in re.split(r"[\s,;]+", finding_ids) if token]
            invalid = [token for token in tokens if not FINDING_ID_RE.fullmatch(token)]
            if invalid:
                errors.append(f"{repo}:{path} has invalid finding ID(s): {', '.join(invalid)}.")

    print("repository,discovered,accounted,detailed_review,classified_only,unable,pending")
    for repository in sorted(counts):
        count = counts[repository]
        print(
            f"{repository},{count['discovered']},{count['accounted']},"
            f"{count['detailed']},{count['classified_only']},{count['unable']},{count['pending']}"
        )

    pending_total = sum(count["pending"] for count in counts.values()) + len(missing)
    if args.require_complete and pending_total:
        errors.append(f"Audit coverage is incomplete: {pending_total} item(s) remain pending or missing.")

    for error in errors:
        print(f"ERROR: {error}")
    if errors:
        print(f"FAILED: {len(errors)} coverage error(s)")
        return 1
    if pending_total:
        print(f"IN PROGRESS: {pending_total} item(s) remain pending")
    else:
        print("PASSED: inventory and ledger reconcile with complete file coverage")
    return 0


def section_body(text: str, heading: str) -> str:
    match = re.search(rf"(?m)^###\s+{re.escape(heading)}\s*$", text)
    if not match:
        return ""
    remainder = text[match.end():]
    next_heading = re.search(r"(?m)^#{2,3}\s+", remainder)
    return remainder[: next_heading.start()].strip() if next_heading else remainder.strip()


def field_value(text: str, field: str) -> str:
    match = re.search(rf"(?im)^\*\*{re.escape(field)}:\*\*\s*(.+?)\s*$", text)
    return match.group(1).strip() if match else ""


def validate_report_command(args: argparse.Namespace) -> int:
    report_path = Path(args.report)
    if not report_path.is_file():
        raise AuditArtifactError(f"Report does not exist: {report_path}")
    text = report_path.read_text(encoding="utf-8")
    errors: list[str] = []
    warnings: list[str] = []

    if not re.search(r"(?m)^#\s+Technical Debt Audit:\s*\S", text):
        errors.append("Missing '# Technical Debt Audit: ...' title.")
    for letter in REQUIRED_REPORT_SECTIONS:
        if not re.search(rf"(?m)^##\s+{letter}\.\s+\S", text):
            errors.append(f"Missing required report section {letter}.")

    register_ids = re.findall(r"(?mi)^\|\s*(TD-\d{3,})\s*\|", text)
    detail_matches = list(re.finditer(r"(?mi)^##\s+(TD-\d{3,}):\s*(.+?)\s*$", text))
    detail_ids = [match.group(1).upper() for match in detail_matches]
    register_ids = [finding_id.upper() for finding_id in register_ids]
    for label, ids in (("register", register_ids), ("detailed findings", detail_ids)):
        duplicates = sorted(item for item, count in Counter(ids).items() if count > 1)
        if duplicates:
            errors.append(f"Duplicate finding ID(s) in {label}: {', '.join(duplicates)}.")
    if set(register_ids) != set(detail_ids):
        only_register = sorted(set(register_ids) - set(detail_ids))
        only_details = sorted(set(detail_ids) - set(register_ids))
        if only_register:
            errors.append(f"Register ID(s) missing details: {', '.join(only_register)}.")
        if only_details:
            errors.append(f"Detailed ID(s) missing from register: {', '.join(only_details)}.")

    for index, match in enumerate(detail_matches):
        finding_id = match.group(1).upper()
        end = detail_matches[index + 1].start() if index + 1 < len(detail_matches) else len(text)
        finding = text[match.end():end]
        for field in REQUIRED_FINDING_FIELDS:
            if not field_value(finding, field):
                errors.append(f"{finding_id} is missing field '{field}'.")
        for heading in REQUIRED_FINDING_SECTIONS:
            if not section_body(finding, heading):
                errors.append(f"{finding_id} is missing or has empty section '{heading}'.")

        allowed_values = {
            "Severity": {"Critical", "High", "Medium", "Low"},
            "Priority": {"P0", "P1", "P2", "P3"},
            "Effort": {"Small", "Medium", "Large"},
            "Blast Radius": {"Local", "Module", "Repository", "Multi-repository"},
            "Evidence State": {"Confirmed", "Strongly Supported", "Needs Verification"},
        }
        for field, allowed in allowed_values.items():
            value = field_value(finding, field)
            if value and value not in allowed:
                errors.append(f"{finding_id} has invalid {field} '{value}'.")

        evidence_sources = field_value(finding, "Evidence Sources")
        if evidence_sources:
            codes = set(re.findall(r"\b[A-Z]\b", evidence_sources.upper()))
            if not codes or not codes.issubset({"S", "G", "T", "D", "C", "H"}):
                errors.append(f"{finding_id} has invalid evidence source codes '{evidence_sources}'.")

        if field_value(finding, "Severity") in {"Critical", "High"}:
            verification = section_body(finding, "Source Verification")
            if len(verification) < 20 or verification.startswith("["):
                errors.append(f"{finding_id} needs substantive source verification for its severity.")

    if not register_ids and not detail_ids:
        warnings.append("Report contains no technical-debt findings; confirm this is evidence-backed.")
    if "## Final Verification Record" not in text:
        errors.append("Missing Final Verification Record.")
    if not args.allow_placeholders:
        template_path = Path(__file__).resolve().parents[1] / "assets" / "audit-report.md"
        placeholders = set(KNOWN_PLACEHOLDERS)
        if template_path.is_file():
            template_text = template_path.read_text(encoding="utf-8")
            placeholders.update(re.findall(r"\[[^\]\n]+\]", template_text))
        unresolved = sorted(placeholder for placeholder in placeholders if placeholder in text)
        if unresolved:
            errors.append(f"Unresolved template placeholders: {', '.join(unresolved[:5])}.")
    if not re.search(r"(?im)^\*\*Ledger:\*\*\s*\S", text):
        errors.append("Missing ledger reference.")

    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}")
    if errors:
        print(f"FAILED: {len(errors)} report error(s), {len(warnings)} warning(s)")
        return 1
    print(f"PASSED: report structure and finding IDs are consistent ({len(detail_ids)} finding(s))")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Create and validate deterministic technical-debt audit artifacts."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    inventory_parser = subparsers.add_parser(
        "inventory", help="Create a deterministic file inventory and pending audit ledger."
    )
    inventory_parser.add_argument(
        "--repo", action="append", type=parse_repo, required=True, metavar="NAME=PATH",
        help="Repository name and absolute root path; repeat for multiple repositories.",
    )
    inventory_parser.add_argument("--inventory", required=True, help="Output inventory CSV path.")
    inventory_parser.add_argument("--ledger", required=True, help="Output ledger CSV path.")
    inventory_parser.add_argument(
        "--include-ignored", action="store_true",
        help="Include Git-ignored files after scope review; can be very large.",
    )
    inventory_parser.add_argument(
        "--exclude", action="append", default=[], metavar="GLOB",
        help="Explicit repository-relative exclusion glob; repeat as needed and record reasons in scope.md.",
    )
    inventory_parser.add_argument(
        "--allow-output-inside-repo", action="store_true",
        help="Override the default audit-state safety boundary deliberately.",
    )
    inventory_parser.add_argument(
        "--force", action="store_true", help="Replace existing output files deliberately."
    )
    inventory_parser.set_defaults(handler=inventory_command)

    reconcile_parser = subparsers.add_parser(
        "reconcile", help="Validate one-to-one inventory/ledger coverage and review states."
    )
    reconcile_parser.add_argument("--inventory", required=True, help="Baseline inventory CSV path.")
    reconcile_parser.add_argument("--ledger", required=True, help="Audit ledger CSV path.")
    reconcile_parser.add_argument(
        "--require-complete", action="store_true",
        help="Fail when any inventory item remains pending; use at the final gate.",
    )
    reconcile_parser.set_defaults(handler=reconcile_command)

    report_parser = subparsers.add_parser(
        "validate-report", help="Validate report sections, finding fields, and ID consistency."
    )
    report_parser.add_argument("--report", required=True, help="Technical-debt report path.")
    report_parser.add_argument(
        "--allow-placeholders", action="store_true",
        help="Allow bundled-template placeholders during template validation.",
    )
    report_parser.set_defaults(handler=validate_report_command)
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    try:
        return args.handler(args)
    except AuditArtifactError as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 2
    except OSError as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())

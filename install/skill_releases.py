"""Stage official third-party skill releases before installing any user files."""

from __future__ import annotations

import hashlib
import io
import json
import re
import shutil
import stat
import zipfile
from pathlib import Path
from urllib.request import Request, urlopen


REPOSITORIES = {
    "impeccable": "pbakaus/impeccable",
    "humanizer": "blader/humanizer",
    "design-taste-frontend": "Leonxlnx/taste-skill",
}
MAX_ARCHIVE = 64 * 1024 * 1024
VERSION = r"([0-9]+)\.([0-9]+)\.([0-9]+)"
SHA = re.compile(r"[0-9a-f]{40}")


def download(url: str, limit: int = MAX_ARCHIVE) -> bytes:
    request = Request(url, headers={"User-Agent": "coding-agent-playbook-codex"})
    with urlopen(request, timeout=30) as response:
        data = response.read(limit + 1)
    if len(data) > limit:
        raise ValueError(f"Download exceeds {limit} bytes: {url}")
    return data


def github(repo: str, path: str):
    return json.loads(download(f"https://api.github.com/repos/{repo}/{path}", 8 * 1024 * 1024))


def stable_release(name: str, repo: str) -> dict:
    pattern = re.compile(("skill-v" if name == "impeccable" else "v") + VERSION)

    def stable(release: dict) -> bool:
        return (release["draft"] is False and release["prerelease"] is False
                and pattern.fullmatch(release["tag_name"]) is not None)

    if name != "impeccable":
        release = github(repo, "releases/latest")
        if not stable(release):
            raise ValueError("GitHub did not return a stable release with a version tag")
        return release

    # Impeccable also publishes engine and CLI releases in the same repository.
    candidates = []
    page = 1
    while True:
        releases = github(repo, f"releases?per_page=100&page={page}")
        candidates.extend(release for release in releases if stable(release))
        if len(releases) < 100:
            break
        page += 1
    if not candidates:
        raise ValueError("No published stable Impeccable skill release found")
    return max(candidates, key=lambda release: tuple(map(int, pattern.fullmatch(release["tag_name"]).groups())))


def release_commit(repo: str, tag: str) -> str:
    target = github(repo, f"git/ref/tags/{tag}")["object"]
    seen = set()
    while SHA.fullmatch(target["sha"]):
        sha = target["sha"]
        if target["type"] == "commit":
            return sha
        if target["type"] != "tag" or sha in seen:
            break
        seen.add(sha)
        target = github(repo, f"git/tags/{sha}")["object"]
    raise ValueError(f"Release tag {tag} does not resolve to a commit")


def unpack(archive: bytes, destination: Path, prefix: str, *, only=None, exclude=(), license_path=None) -> None:
    """Copy regular files from the expected package subtree, without extracting archive paths."""
    paths = set()
    total = 0
    with zipfile.ZipFile(io.BytesIO(archive)) as source:
        for entry in source.infolist():
            if entry.is_dir():
                continue
            if license_path and entry.filename == license_path:
                relative = "LICENSE"
            elif entry.filename.startswith(prefix):
                relative = entry.filename[len(prefix):]
                if relative.startswith(exclude) or (only is not None and relative not in only):
                    continue
            else:
                continue
            parts = relative.split("/")
            if any(not re.fullmatch(r"[A-Za-z0-9_-][A-Za-z0-9_.-]*", part)
                   or part.endswith(".")
                   or re.fullmatch(r"CON|PRN|AUX|NUL|COM[0-9]|LPT[0-9]", part.split(".")[0], re.I)
                   for part in parts):
                raise ValueError(f"Unsafe path in release archive: {relative!r}")
            mode = stat.S_IFMT(entry.external_attr >> 16)
            if mode not in (0, stat.S_IFREG) or relative.casefold() in paths:
                raise ValueError(f"Nonregular or duplicate file in release archive: {relative!r}")
            paths.add(relative.casefold())
            total += entry.file_size
            if total > MAX_ARCHIVE:
                raise ValueError("Unpacked skill exceeds the size limit")
            target = destination.joinpath(*parts)
            target.parent.mkdir(parents=True, exist_ok=True)
            with source.open(entry) as content, target.open("xb") as output:
                shutil.copyfileobj(content, output)
            if mode and entry.external_attr >> 16 & stat.S_IXUSR:
                target.chmod(0o755)


def require_files(package: Path, *paths: str) -> None:
    for path in paths:
        file = package / path
        if not file.is_file() or file.stat().st_size == 0:
            raise ValueError(f"Required package file is missing or empty: {path}")


def validate_skill(package: Path) -> None:
    require_files(package, "SKILL.md", "LICENSE")
    skill = (package / "SKILL.md").read_text(encoding="utf-8")
    sections = skill.split("\n---\n", 1)
    if (len(sections) != 2 or not sections[0].startswith("---\n")
            or not re.search(rf"^name:\s*{re.escape(package.name)}\s*$", sections[0], re.M)
            or not re.search(r"^description:", sections[0], re.M)):
        raise ValueError(f"Invalid skill frontmatter for {package.name}")


def adapt_impeccable(package: Path, bundled: Path) -> None:
    local_skill = (bundled / "SKILL.md").read_text(encoding="utf-8")
    integration = local_skill.split("## Codex integration\n", 1)[1].split("\n## ", 1)[0].strip()
    notice = "<!-- Codex Playbook adaptation: installed paths and role routing. -->\n\n"
    for markdown in package.rglob("*.md"):
        text = markdown.read_text(encoding="utf-8")
        adapted = text.replace(".agents/skills/impeccable/scripts", "<skill-base-dir>/scripts")
        if markdown.name == "component-review.md":
            adapted = adapted.replace('"assets/plates/sky.png"', '"./assets/plates/sky.png"')
        if markdown == package / "SKILL.md":
            frontmatter, body = adapted.split("\n---\n", 1)
            adapted = (f"{frontmatter}\n---\n\n{notice}## Codex Playbook integration\n\n{integration}\n\n"
                       "Use these role mappings and host approval rules throughout the upstream recipes. "
                       "Resolve `<skill-base-dir>` to the folder containing this file. "
                       "Invoke the launcher through `sh` on POSIX if needed.\n\n" + body.lstrip())
        elif adapted != text:
            adapted = notice + adapted
        if adapted != text:
            markdown.write_bytes(adapted.encode("utf-8"))


def adapt_taste(package: Path) -> None:
    # Upstream examples refer to generated project assets and an optional scene catalogue.
    examples = {
        "README.md": {"scripts/lib/ ": "helper modules ", "`assets/credits.json`": "`./assets/credits.json`"},
        "SKILL.md": {
            "`<skill>/assets/scenes/`": "the scene files beside `<skill>/assets/scenes/stage.js`",
            "`assets/scenes/demo/<id>.html` is a working example of each.": "Open the matching demo if the installed catalogue supplies one.",
            "| `assets/scenes/` |": "| `assets/scenes/stage.js` and `assets/scenes/stage.css` |",
        },
        "references/imagery.md": {f"assets/{path}": f"./assets/{path}" for path in (
            "credits.json", "fig-engraving.jpg", "river-poster.jpg", "river.webm"
        )},
        "references/motion.md": {"`assets/scenes/`": "the shared `assets/scenes/stage.js` and `assets/scenes/stage.css`"},
        "references/scenes.md": {
            "; `assets/scenes/demo/<id>.html` is a complete working page to read beside it.":
                ". Read the matching demo if the installed catalogue supplies one.",
        },
    }
    for relative, replacements in examples.items():
        file = package / relative
        if not file.is_file():
            continue
        text = file.read_text(encoding="utf-8")
        for old, new in replacements.items():
            text = re.sub(r"(?<!\./)" + re.escape(old), lambda _: new, text)
        if not (package / "library/scenes.json").is_file():
            text = text.replace("`library/scenes.json`", "`scenes.json` in the optional scene library")
        file.write_bytes(text.encode("utf-8"))


def fetch_package(name: str, repo: str, release: dict, commit: str, bundled: Path, package: Path) -> None:
    tag = release["tag_name"]
    release_url = f"https://github.com/{repo}/releases/tag/{tag}"
    if name == "impeccable":
        assets = [asset for asset in release["assets"] if asset["name"] == "universal.zip"]
        if len(assets) != 1 or not re.fullmatch(r"sha256:[0-9a-f]{64}", assets[0].get("digest") or ""):
            raise ValueError("The release must publish universal.zip with a SHA-256 digest")
        archive = download(f"https://github.com/{repo}/releases/download/{tag}/universal.zip")
        if f"sha256:{hashlib.sha256(archive).hexdigest()}" != assets[0]["digest"]:
            raise ValueError("Checksum mismatch for universal.zip")
        unpack(archive, package, ".agents/skills/impeccable/", exclude=("agents/",))
        require_files(package, "SKILL.md", "scripts/impeccable", "scripts/impeccable.cmd",
                      "scripts/VERSION", "scripts/engine-checksums.txt")
        version = (package / "scripts/VERSION").read_text(encoding="utf-8").strip()
        checksums = (package / "scripts/engine-checksums.txt").read_text(encoding="utf-8")
        if not re.fullmatch(VERSION, version) or not re.search(rf"^{re.escape(version)} \S+ [0-9a-f]{{64}}$", checksums, re.M):
            raise ValueError("The Impeccable launcher version has no matching engine checksums")
        source_url = f"https://raw.githubusercontent.com/{repo}/{commit}"
        for filename in ("LICENSE", "NOTICE.md"):
            if not (package / filename).is_file():
                (package / filename).write_bytes(download(f"{source_url}/{filename}", 1024 * 1024))
        for license_file in bundled.glob("LICENSE.*"):
            target = package / license_file.name
            if not target.is_file():
                shutil.copy2(license_file, target)
        metadata = package / "agents/openai.yaml"
        metadata.parent.mkdir(exist_ok=True)
        shutil.copy2(bundled / "agents/openai.yaml", metadata)
        adapt_impeccable(package, bundled)
    else:
        archive = download(f"https://codeload.github.com/{repo}/zip/{commit}")
        prefix = f"{repo.split('/')[-1]}-{commit}/"
        if name == "humanizer":
            unpack(archive, package, prefix, only={"SKILL.md", "LICENSE", "agents/openai.yaml"})
            require_files(package, "agents/openai.yaml")
        else:
            unpack(archive, package, prefix + "skills/taste-skill/", exclude=("evals/",), license_path=prefix + "LICENSE")
            require_files(package, "SKILL.md")
            adapt_taste(package)
    validate_skill(package)
    with (package / "NOTICE.md").open("a", encoding="utf-8", newline="\n") as notice:
        notice.write(f"\n\n## Codex Playbook installation source\n\n[{tag}]({release_url}), commit `{commit}`.\n")
        if name != "humanizer":
            notice.write("The playbook adapts the upstream Markdown for Codex installation and workflow compatibility.\n")


def stage_skills(bundled: Path, staged: Path) -> None:
    for name in REPOSITORIES:
        if not (bundled / name).is_dir():
            raise ValueError(f"Missing bundled skill package: {name}")
    for path in sorted(bundled.iterdir()):
        if not path.is_dir():
            continue
        package = staged / path.name
        if path.name not in REPOSITORIES:
            shutil.copytree(path, package)
            continue
        repo = REPOSITORIES[path.name]
        try:
            release = stable_release(path.name, repo)
            tag = release["tag_name"]
            commit = release_commit(repo, tag)
            notice = (path / "NOTICE.md").read_text(encoding="utf-8")
            if f"https://github.com/{repo}/releases/tag/{tag})" in notice and f"`{commit}`" in notice:
                shutil.copytree(path, package)
                print(f"{path.name}: {tag} ({commit}), verified current bundled release")
            else:
                fetch_package(path.name, repo, release, commit, path, package)
                print(f"{path.name}: {tag} ({commit}), downloaded official release")
        except (OSError, ValueError, KeyError, TypeError, IndexError, zipfile.BadZipFile, RuntimeError) as error:
            raise ValueError(f"Could not prepare {path.name} from {repo}: {error}") from error

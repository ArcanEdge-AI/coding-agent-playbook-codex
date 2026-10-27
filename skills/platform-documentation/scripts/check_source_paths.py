"""Check structured source locators and report Markdown candidates without executing code.

Unresolved candidates need human classification: routes, generated outputs and
illustrations may be legitimate. This does not validate semantic support or links.
"""
import argparse
import json
from pathlib import Path
import re


EXTENSIONS = (
    "tsx|ts|mts|cts|jsx|js|mjs|cjs|json|sql|toml|yaml|yml|css|scss|html|"
    "py|go|rs|java|kt|kts|swift|dart|rb|php|cs|cpp|h|ps1|sh|lock|"
    "xml|plist|properties|xcconfig|pbxproj|storyboard|xcscheme|"
    "xcprivacy|xcsettings|xcworkspacedata"
)
REFERENCE = re.compile(
    r"(?<![\w./\\:-])(?:[\w@.-]+/)*[\w.-]+\."
    rf"(?:{EXTENSIONS})(?::(?:L)?\d+(?:-(?:L)?\d+)?)?(?![\w.-])"
)


def inspect(source_root, docs_root):
    records = []
    supported = set(EXTENSIONS.split("|"))
    source_suffixes = {path.suffix.lstrip(".").lower()
                       for path in source_root.rglob("*") if path.is_file() and path.suffix}
    documents = sorted(docs_root.rglob("*.md")) if docs_root else []
    for document in documents:
        for number, line in enumerate(document.read_text(encoding="utf-8").splitlines(), 1):
            # Remote URLs are neither local source locators nor fetched here.
            text = re.sub(r"https?://[^\s<>`\])]+", "", line)
            for match in REFERENCE.finditer(text):
                locator = match.group()
                relative, _, span = locator.partition(":")
                target = (source_root / relative).resolve()
                item = {"document": document.relative_to(docs_root).as_posix(),
                        "line": number, "locator": locator}
                if not target.is_relative_to(source_root):
                    item["status"] = "outside_source_root"
                elif not target.is_file():
                    item["status"] = "unresolved_candidate"
                elif span:
                    bounds = [int(value.removeprefix("L")) for value in span.split("-")]
                    count = len(target.read_text(encoding="utf-8").splitlines())
                    item["status"] = (
                        "resolved" if bounds == sorted(bounds)
                        and all(1 <= value <= count for value in bounds)
                        else "line_out_of_bounds"
                    )
                else:
                    item["status"] = "resolved"
                records.append(item)
    return {
        "markdown_files_checked": len(documents),
        "references_checked": len(records),
        "resolved": sum(item["status"] == "resolved" for item in records),
        "needs_review": sum(item["status"] != "resolved" for item in records),
        "references": records,
        "recognized_extensions": sorted(supported),
        "unmatched_source_suffixes": sorted(source_suffixes - supported),
        "limits": "Candidates require classification. Unmatched suffixes and extensionless locators need separate checks. Resolved paths do not prove semantic support, all citation formats, UI labels, or link correctness. No source code executed."
    }


def inspect_records(source_root, paths):
    references, errors, rows_checked = [], [], 0
    for record in paths:
        try:
            rows = json.loads(record.read_text(encoding="utf-8"))
            if not isinstance(rows, list):
                raise ValueError("expected an array of source records")
        except (OSError, UnicodeError, ValueError) as exc:
            errors.append({"record": record.name, "error": str(exc)})
            continue
        for number, row in enumerate(rows, 1):
            rows_checked += 1
            ident = row.get("id") if isinstance(row, dict) else None
            sources = row.get("sources") if isinstance(row, dict) else None
            if not isinstance(ident, str) or not ident.strip() or not isinstance(sources, list) or not sources:
                errors.append({"record": record.name, "row": number, "error": "id and nonempty sources list required"})
                continue
            for locator in sources:
                item = {"record": record.name, "id": ident, "locator": locator}
                try:
                    if not isinstance(locator, str) or not locator.strip() or locator != locator.strip():
                        raise ValueError("nonempty trimmed locator required")
                    match = re.fullmatch(r"(.+?)(?::L?(\d+)(?:-L?(\d+))?)?", locator)
                    relative, start, end = match.groups() if match else (locator, None, None)
                    path = Path(relative)
                    if path.is_absolute() or path.drive or ":" in relative:
                        raise ValueError("repository-relative file locator required")
                    target = (source_root / path).resolve()
                    if not target.is_relative_to(source_root):
                        raise ValueError("outside source root")
                    if not target.is_file():
                        raise ValueError("source file absent; directories and assumed targets are not file evidence")
                    if start:
                        count = len(target.read_text(encoding="utf-8").splitlines())
                        if not 1 <= int(start) <= int(end or start) <= count:
                            raise ValueError("line bounds invalid")
                    item["status"] = "resolved"
                except (OSError, UnicodeError, ValueError) as exc:
                    item["status"] = "invalid"
                    item["error"] = str(exc)
                    errors.append(item)
                references.append(item)
    return {"source_records_checked": rows_checked, "record_references_checked": len(references),
            "record_references": references, "record_errors": errors,
            "record_paths_passed": not errors}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root", required=True, type=Path)
    parser.add_argument("--docs-root", type=Path)
    parser.add_argument("--records", nargs="+", type=Path, help="Claim/unit JSON arrays; strict file and line validation, usable before guides")
    parser.add_argument("--output", type=Path, help="Save JSON outside source inputs")
    args = parser.parse_args()
    source_root = args.source_root.resolve()
    docs_root = args.docs_root.resolve() if args.docs_root else None
    if not docs_root and not args.records:
        parser.error("provide docs-root, records, or both")
    if not source_root.is_dir() or (docs_root and not docs_root.is_dir()):
        parser.error("source-root and docs-root must be existing directories")
    if args.output:
        output = args.output.resolve()
        if output.is_relative_to(source_root) or output in {p.resolve() for p in args.records or []}:
            parser.error("output cannot overwrite source or record inputs")
        if docs_root and output.is_relative_to(docs_root) and output.suffix.lower() == ".md":
            parser.error("JSON output cannot overwrite Markdown readers")
    result = inspect(source_root, docs_root)
    result.update(inspect_records(source_root, args.records or []))
    encoded = json.dumps(result, indent=2) + "\n"
    if args.output:
        args.output.write_text(encoded, encoding="utf-8")
    print(encoded, end="")
    raise SystemExit(0 if result["record_paths_passed"] else 1)


if __name__ == "__main__":
    main()

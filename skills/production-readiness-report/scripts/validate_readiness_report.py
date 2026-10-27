#!/usr/bin/env python3
"""Validate the structure and decision integrity of a readiness report."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


STATUS_LABELS = (
    "Passed",
    "Failed",
    "Not validated",
    "Blocked pending approval",
)

REQUIRED_SECTION_PATTERNS = {
    "status definitions": r"(?im)^##\s+Status definitions and disposition\s*$",
    "result matrix": r"(?im)^##\s+.*result matrix\s*$",
    "repository evidence": r"(?im)^##\s+Repository evidence\s*$",
    "safety result": r"(?im)^##\s+Safety result\s*$",
    "smallest next remediation": r"(?im)^##\s+Smallest next remediation\s*$",
}

PLACEHOLDER_PATTERN = re.compile(
    r"\[(?:YYYY-MM-DD|Status|Client|Environment|full SHA|command|"
    r"List or none\.|List or count|N/N|Path/URL|hash/ID|route)\]",
    re.IGNORECASE,
)


def section(text: str, heading_pattern: str) -> str:
    match = re.search(heading_pattern, text)
    if not match:
        return ""
    rest = text[match.end() :]
    next_heading = re.search(r"(?m)^##\s+", rest)
    return rest[: next_heading.start()] if next_heading else rest


def disposition_value(disposition: str, label: str) -> str | None:
    match = re.search(
        rf"(?im)^-\s+\*\*{re.escape(label)}\*\*:\s*(.+?)\s*$", disposition
    )
    return match.group(1).strip() if match else None


def means_none(value: str | None) -> bool:
    if value is None:
        return False
    normalized = re.sub(r"[`*_\.]", "", value).strip().lower()
    return bool(re.match(r"^none\b", normalized))


def validate(path: Path, allow_placeholders: bool) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    if not path.is_file():
        return [f"Report does not exist: {path}"], warnings

    text = path.read_text(encoding="utf-8")
    if not text.strip():
        return ["Report is empty."], warnings

    if not re.search(r"(?m)^#\s+\S", text):
        errors.append("Missing top-level report title.")
    if not re.search(r"(?im)^Decision:\s*\*\*.+\*\*\s*$", text):
        errors.append("Missing bold Decision line.")

    for name, pattern in REQUIRED_SECTION_PATTERNS.items():
        if not re.search(pattern, text):
            errors.append(f"Missing required section: {name}.")

    disposition = section(text, REQUIRED_SECTION_PATTERNS["status definitions"])
    current_disposition = re.search(
        r"(?im)^Current disposition:\s*$", disposition
    )
    if current_disposition:
        disposition = disposition[current_disposition.end() :]
    else:
        errors.append("Missing 'Current disposition:' marker.")
    values: dict[str, str | None] = {}
    for label in STATUS_LABELS:
        value = disposition_value(disposition, label)
        values[label] = value
        if value is None:
            errors.append(f"Current disposition is missing '{label}'.")

    decision_match = re.search(r"(?im)^Decision:\s*\*\*(.+?)\*\*\s*$", text)
    decision = decision_match.group(1).strip() if decision_match else ""
    template_decision = allow_placeholders and "[" in decision and "]" in decision
    has_green_wording = bool(
        re.search(r"\b(?:PASSED|ALL GREEN)\b", decision, re.IGNORECASE)
    ) or (
        bool(re.search(r"\bREADY\b", decision, re.IGNORECASE))
        and not bool(re.search(r"\bNOT\s+READY\b", decision, re.IGNORECASE))
    )
    if not template_decision and has_green_wording:
        for label in ("Failed", "Not validated", "Blocked pending approval"):
            if values[label] is not None and not means_none(values[label]):
                errors.append(
                    f"Decision is green but disposition '{label}' is not none: "
                    f"{values[label]}"
                )

    if not re.search(r"(?m)^\|.+\|.+\|", text):
        errors.append("No Markdown evidence matrix was found.")

    if not allow_placeholders:
        placeholders = sorted(set(PLACEHOLDER_PATTERN.findall(text)))
        if placeholders:
            preview = ", ".join(placeholders[:8])
            errors.append(f"Unresolved report placeholders: {preview}")

    evidence_signals = {
        "URL": bool(re.search(r"https?://", text)),
        "full commit SHA": bool(re.search(r"\b[0-9a-f]{40}\b", text, re.IGNORECASE)),
        "immutable digest": bool(re.search(r"sha256:[0-9a-f]{64}\b", text, re.IGNORECASE)),
        "command block": bool(re.search(r"```(?:text|powershell|bash|sh)?\s*\n", text)),
        "artifact hash": bool(re.search(r"\b[0-9a-f]{64}\b", text, re.IGNORECASE)),
    }
    for name, present in evidence_signals.items():
        if not present:
            warnings.append(f"No {name} evidence detected; confirm it is N/A for this client.")

    safety = section(text, REQUIRED_SECTION_PATTERNS["safety result"])
    if safety and not re.search(
        r"\b(?:no|not|only|none|without|did not|were not)\b", safety, re.IGNORECASE
    ):
        warnings.append(
            "Safety result does not clearly describe prohibited or non-performed actions."
        )

    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate a production-readiness Markdown report."
    )
    parser.add_argument("report", type=Path, help="Path to the Markdown report")
    parser.add_argument(
        "--allow-placeholders",
        action="store_true",
        help="Allow template placeholders during structural validation",
    )
    args = parser.parse_args()

    errors, warnings = validate(args.report, args.allow_placeholders)
    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}")

    if errors:
        print(f"FAILED: {len(errors)} error(s), {len(warnings)} warning(s)")
        return 1

    print(f"PASSED: 0 errors, {len(warnings)} warning(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

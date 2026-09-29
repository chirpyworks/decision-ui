#!/usr/bin/env python3
"""Zero-dependency repository checks for Decision UI.

The official Agent Skills reference validator remains authoritative for spec
conformance. This script adds project-specific integrity checks.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote


NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
ALLOWED_FRONTMATTER = {
    "name",
    "description",
    "license",
    "allowed-tools",
    "metadata",
    "compatibility",
}
REQUIRED_PATHS = [
    "SKILL.md",
    "LICENSE",
    "README.md",
    "references/chart-selection.md",
    "references/anti-patterns.md",
    "references/decision-flow.md",
    "references/accessibility.md",
]


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        fail("SKILL.md must start with YAML frontmatter")
    end = text.find("\n---\n", 4)
    if end == -1:
        fail("SKILL.md frontmatter is not closed")

    values: dict[str, str] = {}
    for raw in text[4:end].splitlines():
        if raw.startswith((" ", "\t")) or not raw.strip() or ":" not in raw:
            continue
        key, value = raw.split(":", 1)
        values[key.strip()] = value.strip().strip('"')
    return values


def check_relative_links(root: Path) -> None:
    for doc in root.rglob("*.md"):
        body = doc.read_text(encoding="utf-8", errors="ignore")
        for raw_target in LINK_RE.findall(body):
            target = raw_target.strip().strip("<>")
            if not target or target.startswith(("#", "http://", "https://", "mailto:")):
                continue
            target = unquote(target.split("#", 1)[0].split("?", 1)[0])
            if not target:
                continue
            resolved = (doc.parent / target).resolve()
            try:
                resolved.relative_to(root)
            except ValueError:
                fail(f"relative link escapes repository: {doc.relative_to(root)} -> {raw_target}")
            if not resolved.exists():
                fail(f"broken relative link: {doc.relative_to(root)} -> {raw_target}")


def main() -> None:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()

    for rel in REQUIRED_PATHS:
        if not (root / rel).exists():
            fail(f"missing required path: {rel}")

    skill = root / "SKILL.md"
    text = skill.read_text(encoding="utf-8")
    meta = parse_frontmatter(text)

    extra = sorted(set(meta) - ALLOWED_FRONTMATTER)
    if extra:
        fail(f"unexpected SKILL.md frontmatter fields: {', '.join(extra)}")

    name = meta.get("name", "")
    description = meta.get("description", "")

    if not name:
        fail("frontmatter.name is required")
    if not NAME_RE.fullmatch(name):
        fail("frontmatter.name must be lowercase alphanumeric with single hyphens")
    if len(name) > 64:
        fail("frontmatter.name exceeds 64 characters")
    if root.name != name:
        fail(f"directory name '{root.name}' must match skill name '{name}'")
    if not description:
        fail("frontmatter.description is required")
    if len(description) > 1024:
        fail("frontmatter.description exceeds 1024 characters")
    if text.count("\n") + 1 > 500:
        fail("SKILL.md exceeds the 500-line recommended limit")

    check_relative_links(root)

    private_tokens = [
        "RU" + "DA",
        "INDEX" + "FORM",
        "VAN" + "TERA",
        "BIRTH" + "FIELD",
    ]
    secret_patterns = [
        ("OpenAI-like secret", re.compile(r"\\bsk-[A-Za-z0-9_-]{16,}\\b")),
        ("private key block", re.compile(r"BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY")),
        (
            "API key assignment",
            re.compile(r"""(?i)\\bapi[-_]?key\\s*=\\s*['\"][^'\"]{8,}"""),
        ),
    ]
    text_suffixes = {".md", ".html", ".py", ".yml", ".yaml", ".json", ".txt"}
    for file in root.rglob("*"):
        if not file.is_file() or ".git" in file.parts:
            continue
        if file.suffix.lower() not in text_suffixes:
            continue
        body = file.read_text(encoding="utf-8", errors="ignore")
        for token in private_tokens:
            if token.lower() in body.lower():
                fail(f"private project token '{token}' in {file.relative_to(root)}")
        for label, pattern in secret_patterns:
            if pattern.search(body):
                fail(f"{label} detected in {file.relative_to(root)}")

    print("Decision UI local validation: PASS")


if __name__ == "__main__":
    main()

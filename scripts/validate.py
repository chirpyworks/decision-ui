#!/usr/bin/env python3
"""Zero-dependency release validator for Decision UI.

This validator enforces Decision UI's repository policy. It complements,
rather than replaces, the upstream Agent Skills reference validator.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
SKILL_DIR = ROOT / "skills" / "decision-ui"
SKILL = SKILL_DIR / "SKILL.md"
ERRORS: list[str] = []


def fail(message: str) -> None:
    ERRORS.append(message)


def require(path: Path) -> None:
    if not path.exists():
        fail(f"missing required file: {path.relative_to(ROOT)}")


def top_level_field(frontmatter: str, name: str) -> str | None:
    prefix = f"{name}:"
    for line in frontmatter.splitlines():
        if line.startswith(prefix):
            return line[len(prefix):].strip().strip('"').strip("'")
    return None


def nested_field(frontmatter: str, name: str) -> str | None:
    prefix = f"{name}:"
    for line in frontmatter.splitlines():
        stripped = line.strip()
        if stripped.startswith(prefix):
            return stripped[len(prefix):].strip().strip('"').strip("'")
    return None


REQUIRED = [
    SKILL,
    SKILL_DIR / "house-style.md",
    SKILL_DIR / "references" / "decision-flow.md",
    SKILL_DIR / "references" / "chart-selection.md",
    SKILL_DIR / "references" / "anti-patterns.md",
    SKILL_DIR / "references" / "accessibility.md",
    ROOT / "README.md",
    ROOT / "BENCHMARK.md",
    ROOT / "LICENSE",
    ROOT / "CONTRIBUTING.md",
    ROOT / "SECURITY.md",
    ROOT / "SUPPORT.md",
    ROOT / "CODE_OF_CONDUCT.md",
    ROOT / "CHANGELOG.md",
    ROOT / "ROADMAP.md",
    ROOT / "AGENTS.md",
    ROOT / "package.json",
    ROOT / "docs" / "COMPATIBILITY.md",
    ROOT / "docs" / "FORKING.md",
    ROOT / "evals" / "cases.md",
    ROOT / "evals" / "manifest.json",
    ROOT / "evals" / "prompts" / "saas-retention.md",
    ROOT / "evals" / "prompts" / "manufacturing-operations.md",
    ROOT / "evals" / "prompts" / "sre-incident.md",
    ROOT / "evals" / "prompts" / "executive-revenue.md",
    ROOT / "evals" / "results" / "README.md",
    ROOT / "site" / "index.html",
]

for required_path in REQUIRED:
    require(required_path)

skill_version: str | None = None

if SKILL.exists():
    text = SKILL.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        fail("SKILL.md must begin with YAML frontmatter")
    else:
        parts = text.split("---", 2)
        if len(parts) != 3:
            fail("SKILL.md frontmatter is not closed")
        else:
            frontmatter, body = parts[1], parts[2]
            name = top_level_field(frontmatter, "name")
            description = top_level_field(frontmatter, "description")
            license_name = top_level_field(frontmatter, "license")
            skill_version = nested_field(frontmatter, "version")

            if name != SKILL_DIR.name:
                fail(f"skill name {name!r} must match parent directory {SKILL_DIR.name!r}")
            if not name or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
                fail("skill name must use lowercase alphanumerics and single hyphens")
            if name and len(name) > 64:
                fail("skill name exceeds 64 characters")
            if not description or len(description) > 1024:
                fail("description must be 1..1024 characters")
            if license_name != "MIT":
                fail("skill license must be MIT")
            if not skill_version:
                fail("metadata.version is required by repository policy")
            if len(body.splitlines()) > 500:
                fail("SKILL.md body exceeds 500 lines")

            for reference in sorted(
                set(re.findall(r"references/[A-Za-z0-9._/-]+\.md", body))
            ):
                if not (SKILL_DIR / reference).exists():
                    fail(f"broken skill reference: {reference}")

for legacy_path in (
    ROOT / "SKILL.md",
    ROOT / "house-style.md",
    ROOT / "references",
):
    if legacy_path.exists():
        fail(f"legacy duplicate path must not exist: {legacy_path.relative_to(ROOT)}")

example_dir = ROOT / "examples"
example_files = (
    [path for path in example_dir.glob("*.md") if path.name != "README.md"]
    if example_dir.exists()
    else []
)
if len(example_files) < 4:
    fail("at least four worked examples are required")

package_version: str | None = None
package_path = ROOT / "package.json"
if package_path.exists():
    try:
        package_data = json.loads(package_path.read_text(encoding="utf-8"))
        package_version = package_data.get("version")
        entry = package_data.get("skill", {}).get("entry")
        if entry != "skills/decision-ui/SKILL.md":
            fail("package skill.entry must point to skills/decision-ui/SKILL.md")
    except Exception as exc:
        fail(f"invalid package.json: {exc}")

manifest_path = ROOT / "evals" / "manifest.json"
if manifest_path.exists():
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        manifest_version = manifest.get("skill_version")
        criteria = manifest.get("criteria", [])
        core_cases = manifest.get("core_cases", [])

        if skill_version and manifest_version != skill_version:
            fail("eval manifest skill_version must match SKILL metadata.version")
        if skill_version and package_version != skill_version:
            fail("package version must match SKILL metadata.version")

        required_criteria = {
            "decision_contract",
            "priority",
            "comparison",
            "diagnostic_path",
            "action_path",
            "verification",
            "visualization_fit",
            "state_integrity",
            "responsive_reconstruction",
            "restraint",
            "accessibility_integrity",
        }
        missing_criteria = sorted(required_criteria - set(criteria))
        if missing_criteria:
            fail(f"eval manifest missing criteria: {', '.join(missing_criteria)}")
        if len(core_cases) < 4:
            fail("eval manifest must define at least four core cases")

        ids = [case.get("id") for case in core_cases]
        if len(ids) != len(set(ids)):
            fail("eval core case ids must be unique")

        for case in core_cases:
            case_id = case.get("id")
            example = case.get("example")
            prompt = case.get("prompt")
            if not case_id or not example or not prompt:
                fail("each core eval case requires id, example and prompt")
                continue
            if not (ROOT / example).exists():
                fail(f"eval example does not exist: {example}")
            if not (ROOT / prompt).exists():
                fail(f"eval prompt does not exist: {prompt}")
    except Exception as exc:
        fail(f"invalid eval manifest: {exc}")

benchmark_path = ROOT / "BENCHMARK.md"
if benchmark_path.exists():
    benchmark = benchmark_path.read_text(encoding="utf-8")
    benchmark_criteria = {
        "D1 — Decision contract",
        "D2 — Priority",
        "D3 — Comparison",
        "D4 — Diagnostic path",
        "D5 — Action path",
        "D6 — Verification",
        "D7 — Visualization fit",
        "D8 — State integrity",
        "D9 — Responsive reconstruction",
        "D10 — Restraint",
        "D11 — Accessibility integrity",
    }
    missing_benchmark_criteria = sorted(
        item for item in benchmark_criteria if item not in benchmark
    )
    if missing_benchmark_criteria:
        fail(
            "benchmark criteria drift: "
            + ", ".join(missing_benchmark_criteria)
        )

if skill_version and (ROOT / "CHANGELOG.md").exists():
    changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
    if f"## [{skill_version}]" not in changelog:
        fail("CHANGELOG must contain the current skill version")

# The validator source contains defensive signatures, so it is excluded.
FORBIDDEN_WORDS = ("RUDA", "INDEXFORM", "VANTERA", "BIRTHFIELD", "FIXED")
SECRET_PATTERNS = [
    re.compile(r"(?i)\bsk-[A-Za-z0-9_-]{16,}\b"),
    re.compile(
        r"""(?i)\b(api[_-]?key|token|secret)\s*[:=]\s*['\"][^'\"]{8,}['\"]"""
    ),
]

for path in ROOT.rglob("*"):
    if not path.is_file() or ".git" in path.parts:
        continue
    if path.resolve() == Path(__file__).resolve():
        continue
    if path.suffix.lower() not in {
        ".md",
        ".json",
        ".html",
        ".py",
        ".yml",
        ".yaml",
        ".txt",
    }:
        continue

    content = path.read_text(encoding="utf-8", errors="ignore")
    relative = path.relative_to(ROOT)
    lower = content.lower()

    for word in FORBIDDEN_WORDS:
        if word.lower() in lower:
            fail(f"internal project identifier {word!r} found in {relative}")

    for pattern in SECRET_PATTERNS:
        if pattern.search(content):
            fail(f"possible secret pattern found in {relative}")

site_path = ROOT / "site" / "index.html"
if site_path.exists():
    html = site_path.read_text(encoding="utf-8")
    if '<meta name="viewport"' not in html:
        fail("site is missing viewport metadata")
    if '<meta name="description"' not in html:
        fail("site is missing description metadata")
    if re.search(r"<script[^>]+src=[\"']https?://", html, re.I):
        fail("site must not require an external script")
    if re.search(r"<link[^>]+href=[\"']https?://", html, re.I):
        fail("site must not require an external stylesheet")
    if 'aria-pressed=' not in html:
        fail("demo framing controls must expose pressed state")
    if "does not establish causality" not in html:
        fail("demo must preserve explicit causal-uncertainty language")

    forbidden_demo_claims = (
        "$482k",
        ">NPS<",
        "61% of churn",
        "14-day recovery",
        "two key workflows",
        "Billing setup and team invite",
    )
    for claim in forbidden_demo_claims:
        if claim in html:
            fail(f"unsupported demo claim regressed: {claim}")

if ERRORS:
    print("Decision UI validation failed:")
    for item in ERRORS:
        print(f" - {item}")
    sys.exit(1)

print("Decision UI validation passed.")
print(f" - skill version: {skill_version}")
print(f" - worked examples: {len(example_files)}")
print(" - Agent Skills directory/name contract")
print(" - reference integrity")
print(" - evaluation/version integrity")
print(" - benchmark prompt integrity")
print(" - public leakage/secret heuristics")
print(" - static demo dependency/data-integrity checks")

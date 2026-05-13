#!/usr/bin/env python3
"""Generate live branch summary markdown for Kinesthetic Teaching docs."""

from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List
from urllib.request import Request, urlopen

OWNER = "ulubilgeulusoy"
REPO = "franka_kinesthetic_teaching_GUI"
API_URL = f"https://api.github.com/repos/{OWNER}/{REPO}/branches?per_page=100"
OUT_PATH = Path("docs/user-guide/fr3-example-capabilities/kinesthetic-teaching/branches-overview.md")
RAW_README_URL = f"https://raw.githubusercontent.com/{OWNER}/{REPO}" + "/{branch}/README.md"


def fetch_branches() -> List[Dict]:
    req = Request(
        API_URL,
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": "parc-fr3-docs-branch-overview-generator",
        },
    )
    with urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def line_for(branch: Dict) -> str:
    name = branch["name"]
    sha = branch["commit"]["sha"][:7]
    return f"- `{name}` -> `{sha}`"


def fetch_readme(branch_name: str) -> str:
    url = RAW_README_URL.format(branch=branch_name)
    req = Request(
        url,
        headers={
            "User-Agent": "parc-fr3-docs-branch-overview-generator",
        },
    )
    with urlopen(req, timeout=30) as resp:
        return resp.read().decode("utf-8", errors="replace")


def extract_summary(readme_text: str) -> str:
    lines = [ln.strip() for ln in readme_text.splitlines()]
    cleaned = []
    for ln in lines:
        if not ln:
            continue
        if ln.startswith("#"):
            continue
        if ln.startswith("```"):
            continue
        if ln.startswith("!"):
            continue
        cleaned.append(ln)
    if not cleaned:
        return "README present, but no summary text was detected."

    paragraph = []
    for ln in cleaned:
        if ln.startswith("## "):
            break
        paragraph.append(ln)
        if len(" ".join(paragraph)) > 320:
            break

    text = " ".join(paragraph).strip()
    text = re.sub(r"\s+", " ", text)
    return text[:320].rstrip() + ("..." if len(text) > 320 else "")


def build_markdown(branches: List[Dict]) -> str:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    branches_sorted = sorted(branches, key=lambda b: b["name"].lower())

    lines = [
        "# Branches Overview",
        "",
        "This page is auto-generated from the live GitHub branch list:",
        f"<https://github.com/{OWNER}/{REPO}/branches>",
        "",
        f"Last updated: {now}",
        "",
        "## Live Branches",
        "",
    ]

    lines.extend(line_for(b) for b in branches_sorted)

    lines += [
        "",
        "## README Summaries",
        "",
    ]

    for b in branches_sorted:
        name = b["name"]
        branch_url = f"https://github.com/{OWNER}/{REPO}/tree/{name}"
        try:
            summary = extract_summary(fetch_readme(name))
        except Exception:
            summary = "README summary unavailable for this branch."
        lines.append(f"### `{name}`")
        lines.append("")
        lines.append(f"- Branch URL: <{branch_url}>")
        lines.append(f"- Summary: {summary}")
        lines.append("")

    lines += [
        "Note: this page is generated automatically in CI from live branch data and per-branch README content.",
    ]

    return "\n".join(lines) + "\n"


def main() -> int:
    branches = fetch_branches()
    OUT_PATH.write_text(build_markdown(branches), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

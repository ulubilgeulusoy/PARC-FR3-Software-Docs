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
MAX_BULLETS = 3
MAX_BULLET_LEN = 220


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


def parse_sections(readme_text: str) -> Dict[str, List[str]]:
    sections = {}
    current = "_intro"
    sections[current] = []
    for raw in readme_text.splitlines():
        line = raw.rstrip()
        if line.startswith("## "):
            current = line[3:].strip().lower()
            sections[current] = []
            continue
        sections.setdefault(current, []).append(line)
    return sections


def clean_text(s: str) -> str:
    s = s.strip()
    s = re.sub(r"`([^`]*)`", r"\1", s)
    s = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", s)
    s = re.sub(r"<[^>]+>", "", s)
    s = re.sub(r"\s+", " ", s)
    return s.strip(" -:")


def collect_points(lines: List[str], max_points: int = MAX_BULLETS) -> List[str]:
    points = []
    in_code = False
    for raw in lines:
        line = raw.strip()
        if line.startswith("```"):
            in_code = not in_code
            continue
        if in_code or not line:
            continue
        if line.startswith("!"):
            continue
        if line.startswith("- ") or line.startswith("* "):
            point = clean_text(line[2:])
            if point:
                points.append(point[:MAX_BULLET_LEN])
        elif re.match(r"^\d+\.\s+", line):
            point = clean_text(re.sub(r"^\d+\.\s+", "", line))
            if point:
                points.append(point[:MAX_BULLET_LEN])
        elif len(points) == 0:
            point = clean_text(line)
            if point:
                points.append(point[:MAX_BULLET_LEN])
        if len(points) >= max_points:
            break
    return points


def get_first_available(sections: Dict[str, List[str]], candidates: List[str]) -> List[str]:
    for key in candidates:
        if key in sections:
            pts = collect_points(sections[key])
            if pts:
                return pts
    return []


def detect_workspace_info(readme_text: str, branch_name: str) -> Dict[str, str]:
    text = readme_text
    lower = text.lower()
    candidates = []

    exact_names = re.findall(r"\b([a-zA-Z0-9_-]*ws[a-zA-Z0-9_-]*)\b", text)
    setup_paths = re.findall(r"/home/[^\s`\"']+/([a-zA-Z0-9_-]*ws[a-zA-Z0-9_-]*)/install/setup\.bash", text)
    if "franka_ws_jointfailsafe" in lower:
        candidates.append("franka_ws_jointfailsafe")
    if "franka_ws" in lower:
        candidates.append("franka_ws")
    candidates.extend(exact_names)
    candidates.extend(setup_paths)

    seen = []
    for c in candidates:
        if c not in seen:
            seen.append(c)
    candidates = seen

    if any("jointfailsafe" in c.lower() or "failsafe" in c.lower() for c in candidates):
        ws_type = "custom"
        confidence = "high"
        ws_name = next((c for c in candidates if "failsafe" in c.lower()), candidates[0])
    elif any(c.lower() == "franka_ws" for c in candidates):
        ws_type = "standard"
        confidence = "high"
        ws_name = "franka_ws"
    elif len(candidates) == 1:
        ws_type = "custom"
        confidence = "medium"
        ws_name = candidates[0]
    elif len(candidates) > 1:
        ws_type = "mixed"
        confidence = "low"
        ws_name = ", ".join(candidates[:3])
    else:
        if "failsafe" in branch_name.lower():
            ws_type = "custom"
            confidence = "low"
            ws_name = "unknown"
        else:
            ws_type = "unknown"
            confidence = "low"
            ws_name = "unknown"

    evidence = []
    if "franka_ws_jointfailsafe" in lower:
        evidence.append("token: franka_ws_jointfailsafe")
    if "franka_ws" in lower:
        evidence.append("token: franka_ws")
    if setup_paths:
        evidence.append(f"path: /home/.../{setup_paths[0]}/install/setup.bash")
    if not evidence and candidates:
        evidence.append(f"pattern: {candidates[0]}")

    return {
        "type": ws_type,
        "name": ws_name,
        "confidence": confidence,
        "evidence": "; ".join(evidence) if evidence else "none",
    }


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
        sha = b["commit"]["sha"][:7]
        branch_url = f"https://github.com/{OWNER}/{REPO}/tree/{name}"
        readme_url = f"https://github.com/{OWNER}/{REPO}/blob/{name}/README.md"
        try:
            readme = fetch_readme(name)
            sections = parse_sections(readme)
            purpose = get_first_available(sections, ["what this repo does"])
            if not purpose:
                purpose = collect_points(sections.get("_intro", []), max_points=2)
            env = get_first_available(sections, ["validated environment", "requirements"])
            workspace_info = detect_workspace_info(readme, name)
            workspace = [
                f"Workspace Type: {workspace_info['type']}",
                f"Workspace Name: {workspace_info['name']}",
                f"Detection Confidence: {workspace_info['confidence']}",
                f"Evidence: {workspace_info['evidence']}",
            ]
            workflows = get_first_available(sections, ["features", "main application", "usage"])
            run_steps = get_first_available(sections, ["running", "usage"])
            caveats = get_first_available(sections, ["known assumptions and caveats", "important notes"])
        except Exception:
            purpose = []
            env = []
            workspace = [
                "Workspace Type: unknown",
                "Workspace Name: unknown",
                "Detection Confidence: low",
                "Evidence: none",
            ]
            workflows = []
            run_steps = []
            caveats = []

        def section_or_fallback(title: str, points: List[str]) -> List[str]:
            out = [f"**{title}**"]
            if points:
                out.extend([f"- {p}" for p in points[:MAX_BULLETS]])
            else:
                out.append("- Not specified in this branch README.")
            out.append("")
            return out

        lines.append(f"### `{name}`")
        lines.append("")
        lines.append(f"- Branch URL: <{branch_url}>")
        lines.append(f"- README: <{readme_url}>")
        lines.append(f"- Head commit: `{sha}`")
        lines.append("")
        lines.extend(section_or_fallback("Purpose", purpose))
        lines.extend(section_or_fallback("Validated Environment", env))
        lines.extend(section_or_fallback("Workspace Context", workspace))
        lines.extend(section_or_fallback("Main Workflows", workflows))
        lines.extend(section_or_fallback("How To Run", run_steps))
        lines.extend(section_or_fallback("Known Caveats", caveats))
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

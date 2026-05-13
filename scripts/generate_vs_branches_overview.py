#!/usr/bin/env python3
"""Generate Visual Servoing branch overview markdown from live GitHub data."""

from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List
from urllib.request import Request, urlopen

OWNER = "ulubilgeulusoy"
REPO = "FR3_visual_servo_examples"
API_URL = f"https://api.github.com/repos/{OWNER}/{REPO}/branches?per_page=100"
OUT_PATH = Path("docs/user-guide/fr3-example-capabilities/visual-servoing/branches-overview.md")
RAW_README_URL = f"https://raw.githubusercontent.com/{OWNER}/{REPO}" + "/{branch}/README.md"


def fetch_branches() -> List[Dict]:
    req = Request(API_URL, headers={"Accept": "application/vnd.github+json", "User-Agent": "parc-fr3-docs-generator"})
    with urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def fetch_readme(branch: str) -> str:
    req = Request(RAW_README_URL.format(branch=branch), headers={"User-Agent": "parc-fr3-docs-generator"})
    with urlopen(req, timeout=30) as resp:
        return resp.read().decode("utf-8", errors="replace")


def has_any(text: str, patterns: List[str]) -> bool:
    t = text.lower()
    return any(p.lower() in t for p in patterns)


def find_cmd(lines: List[str], startswith: str) -> str:
    for ln in lines:
        s = ln.strip()
        if s.startswith(startswith):
            return s
    return "not found"


def extract_mode_summary(text: str) -> str:
    t = text.lower()
    has_m1 = "--mode 1" in t
    has_m2 = "--mode 2" in t
    if has_m1 and has_m2:
        return "Supports mode 1 (single-tag) and mode 2 (sequenced multi-tag)."
    if has_m1:
        return "Supports mode 1 (single-tag)."
    if has_m2:
        return "Supports mode 2 (sequenced multi-tag)."
    return "Mode details not clearly specified."


def classify_impl(text: str) -> str:
    t = text.lower()
    qt_signals = ["main_qt.cpp", "mainwindow.cpp", "visualservocontroller.cpp", "qt5", "qt-based"]
    single_signals = ["src/servofrankaibvs_combined.cpp", "single combined application", "single-file"]
    qt = has_any(t, qt_signals)
    single = has_any(t, single_signals)
    if qt and single:
        return "mixed (Qt modular + single-file reference)"
    if qt:
        return "Qt modular app"
    if single:
        return "single-file combined ViSP app"
    return "unknown"


def detect_workspace_model(text: str) -> str:
    t = text.lower()
    if "cmake" in t and "ros 2" not in t and "colcon" not in t:
        return "standalone CMake app"
    if "ros 2" in t or "colcon" in t:
        return "ROS-integrated workflow"
    return "unknown"


def build_branch_block(branch: Dict, main_sha: str) -> List[str]:
    name = branch["name"]
    sha = branch["commit"]["sha"]
    sha7 = sha[:7]
    branch_url = f"https://github.com/{OWNER}/{REPO}/tree/{name}"
    readme_url = f"https://github.com/{OWNER}/{REPO}/blob/{name}/README.md"

    out = [f"### `{name}`", "", f"- Branch URL: <{branch_url}>", f"- README: <{readme_url}>", f"- Head commit: `{sha7}`", ""]

    try:
        readme = fetch_readme(name)
        lines = readme.splitlines()
        lower = readme.lower()

        build_cmd = find_cmd(lines, "cmake ")
        run_cmd = find_cmd(lines, "./run_visual_servo_combined.sh")
        binary_cmd = find_cmd(lines, "./build/servoFrankaIBVS_combined")

        impl = classify_impl(readme)
        workspace_model = detect_workspace_model(readme)
        modes = extract_mode_summary(readme)

        calib_needed = "yes" if has_any(lower, ["calibration", "--emc", "camera-to-end-effector", "hand-eye"]) else "unknown"
        safety = "present" if has_any(lower, ["safety", "joint-limit", "workspace guard", "collision", "external-wrench", "contact"]) else "not specified"
        integration = "arm_moving state post" if has_any(lower, ["arm_moving", "127.0.0.1:8765/state"]) else "not specified"

        if sha == main_sha:
            delta = "Same commit as `main` (no branch-level code delta at head)."
        else:
            delta = "Different commit from `main` (branch-specific implementation/version)."

        readiness = "Ready for quick try (with calibration verified)" if calib_needed == "yes" and run_cmd != "not found" else "Needs README/run validation"

        out += [
            "**Branch Implementation Type**",
            f"- {impl}",
            "",
            "**Build Target and Path**",
            "- Target: `servoFrankaIBVS_combined`",
            f"- Build command sample: `{build_cmd}`" if build_cmd != "not found" else "- Build command sample: not clearly specified",
            "",
            "**Run Entry Points**",
            f"- Launcher script: `{run_cmd}`" if run_cmd != "not found" else "- Launcher script: not specified",
            f"- Direct binary: `{binary_cmd}`" if binary_cmd != "not found" else "- Direct binary: not specified",
            "",
            "**Modes and Behavior**",
            f"- {modes}",
            "",
            "**Calibration Dependency**",
            f"- Required: {calib_needed}",
            "- Requires a valid `--eMc` calibration file and camera calibration verification before motion.",
            "",
            "**Safety Guard Coverage**",
            f"- Safety guards: {safety}",
            "- Treat as controller-side safeguards, not certified safety.",
            "",
            "**Workspace Model**",
            f"- {workspace_model}",
            "",
            "**External Integration**",
            f"- {integration}",
            "",
            "**Branch Delta vs Main**",
            f"- {delta}",
            "",
            "**Operational Readiness**",
            f"- {readiness}",
            "",
        ]
    except Exception:
        out += ["- README parsing failed for this branch.", ""]

    return out


def build_markdown(branches: List[Dict]) -> str:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    branches_sorted = sorted(branches, key=lambda b: b["name"].lower())
    main_sha = next((b["commit"]["sha"] for b in branches_sorted if b["name"] == "main"), "")

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

    for b in branches_sorted:
        lines.append(f"- `{b['name']}` -> `{b['commit']['sha'][:7]}`")

    lines += ["", "## Branch Summaries", ""]

    for b in branches_sorted:
        lines.extend(build_branch_block(b, main_sha))

    lines += ["Note: generated automatically in CI from live branch data and branch README content."]
    return "\n".join(lines) + "\n"


def main() -> int:
    branches = fetch_branches()
    OUT_PATH.write_text(build_markdown(branches), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

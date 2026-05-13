# PARC-FR3-Software-Docs

This repo contains the source files for the PARC Franka Research 3 (FR3) Robot Arm Software Documentation site.
The site is built using MkDocs + Material.
The live site is available at: https://ulubilgeulusoy.github.io/PARC-FR3-Software-Docs/

Central documentation repository for PARC FR3 software operation, setup history, and user workflows.

This site is built with MkDocs + Material and is intended to help lab users:
- Understand FR3 capabilities and safety basics
- Run FR3 workflows (remote and non-remote control)
- Reference installation decisions and lessons learned
- Follow startup and operation checklists

## Tech Stack

- MkDocs
- Material for MkDocs
- GitHub Actions (automated build/deploy and generated docs content)

## Documentation Structure

Top-level sections in the current navigation:

- Home
- Getting Started
  - Quick Start
  - PARC FR3 Capabilities
  - Capability Basics
  - Safety
- FR3 Control System Installation Guide
  - Summary
  - Before Installation
  - Recommended Installation Steps
  - Lessons Learned
- FR3 User Guide
  - Read Before Proceed
  - Computers
  - FR3 Basics
  - FR3 Start-up Checklist
  - FR3 Example Capabilities
    - libfranka Examples
    - Kinesthetic Teaching
    - Visual Servoing
  - FR3 Non-Remote Control
  - FR3 Remote Control
- Appendix
  - Glossary

Primary content lives in `docs/`, with site configuration in `mkdocs.yml`.

## Repository Layout

- `docs/`: Markdown source pages and image assets
- `docs/assets/`: Embedded images used by documentation pages
- `mkdocs.yml`: Site configuration (theme, navigation, features)
- `scripts/generate_kt_branches_overview.py`: Generates live Kinesthetic Teaching branch overview from GitHub branch/README data
- `.github/workflows/refresh-kt-branches-overview.yml`: CI workflow that regenerates branch overview, builds docs, and deploys to GitHub Pages
- `site/`: Generated static output from `mkdocs build`

## Local Development

Local preview commands:

```bash
pip install mkdocs mkdocs-material
mkdocs serve
```

For local preview, open: `http://127.0.0.1:8000`

## Deployment Model (GitHub Actions)

Deployment is fully CI-driven.

- Do not rely on local `mkdocs gh-deploy` for routine publishing.
- Publishing is handled by GitHub Actions workflow:
  - `.github/workflows/refresh-kt-branches-overview.yml`
- On workflow runs, CI will:
  1. Generate/update Kinesthetic Teaching Branches Overview from live branch data.
  2. Commit generated markdown if content changed.
  3. Build the MkDocs site.
  4. Deploy to GitHub Pages.

Recommended Pages setting:
- Repository Settings -> Pages -> Source: **GitHub Actions**

## Deployment Instructions

This repository deploys through GitHub Actions workflow:
- `Build and Deploy Docs (Auto Branch Overview)`

### What triggers deployment

- Push to `main` (for example, static docs/config updates)
- Manual run from GitHub Actions (`workflow_dispatch`)
- Weekly scheduled run (Monday cron)

### How to manually deploy

1. Open: `https://github.com/ulubilgeulusoy/PARC-FR3-Software-Docs`
2. Click **Actions**
3. Select workflow: **Build and Deploy Docs (Auto Branch Overview)**
4. Click **Run workflow** (top-right)
5. Select branch `main`
6. Click **Run workflow** in the dropdown

When the workflow run shows green (success), the site is deployed to:
- `https://ulubilgeulusoy.github.io/PARC-FR3-Software-Docs/`

## Kinesthetic Teaching Branches Overview Automation

The page:
- `docs/user-guide/fr3-example-capabilities/kinesthetic-teaching/branches-overview.md`

is auto-generated in CI from:
- Live branch list in `ulubilgeulusoy/franka_kinesthetic_teaching_GUI`
- Per-branch `README.md` summary text

This keeps branch names and summaries current without manual editing.

## Notes

- This repository focuses on operational documentation and setup knowledge transfer.
- Some pages reference external/internal resources (for example, SharePoint-hosted lab documents).

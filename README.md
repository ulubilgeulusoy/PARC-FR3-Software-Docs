# PARC-FR3-Software-Docs

## Repository Status

This repository is no longer actively maintained.

Documentation is being transitioned to the centralized Arquilla Group location:
- https://ucboulder.github.io/PARC-FR3-documents/

Please use that site for the most up-to-date FR3 documentation.

## Licensing

- Code in this repository is licensed under the MIT License. See [LICENSE](LICENSE).
- Documentation content is licensed under Creative Commons Attribution 4.0 International (CC BY 4.0). See [LICENSE-docs](LICENSE-docs).

This repo contains the source files for the PARC Franka Research 3 (FR3) Robot Arm Software Documentation site.
The site is built using MkDocs + Material.
The live site is available at: https://ulubilgeulusoy.github.io/PARC-FR3-Software-Docs/

This site is built with MkDocs + Material and is intended to help lab users:
- Understand FR3 capabilities and safety basics
- Run FR3 workflows (remote and non-remote control)
- Reference installation decisions and lessons learned
- Follow startup and operation checklists

## Content Ownership and Automation

### Auto-generated content (GitHub Actions)

These pages are generated and refreshed automatically in CI:
- `docs/user-guide/fr3-example-capabilities/kinesthetic-teaching/branches-overview.md`
- `docs/user-guide/fr3-example-capabilities/visual-servoing/branches-overview.md`

Data source for auto-generated branch pages:
- Live branch list from source repositories
- Per-branch `README.md` content

### Manual content (Arquilla Group updates required)

All other documentation pages are manually maintained by the Arquilla group, including:
- Getting Started pages
- Installation Guide pages
- User Guide basics/checklists/control pages
- Kinesthetic Teaching and Visual Servoing `Overview` and `Quick Try` pages
- HRI Experiments pages
- Appendix pages

Manual updates are required whenever workflows, hardware setup, branch recommendations, or safety procedures change.

The `HRI Experiments` section currently contains starter placeholders and is in progress.

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
    - Summary
    - libfranka Examples
    - Kinesthetic Teaching
      - Overview
      - Quick Try
      - Branches Overview (auto-generated)
    - Visual Servoing
      - Overview
      - Quick Try
      - Branches Overview (auto-generated)
  - FR3 Non-Remote Control
  - FR3 Remote Control
- HRI Experiments
  - Overview
  - Example Tasks
  - Data Collection Tools
  - Data Analysis Tools
- Appendix
  - Glossary

Primary content lives in `docs/`, with site configuration in `mkdocs.yml`.

## Repository Layout

- `docs/`: Markdown source pages and image assets
- `docs/assets/`: Embedded images used by documentation pages
- `mkdocs.yml`: Site configuration (theme, navigation, features)
- `scripts/generate_kt_branches_overview.py`: Generates Kinesthetic Teaching branch overview from live branch/README data
- `scripts/generate_vs_branches_overview.py`: Generates Visual Servoing branch overview from live branch/README data
- `.github/workflows/refresh-kt-branches-overview.yml`: CI workflow that regenerates branch overviews, builds docs, and deploys to GitHub Pages

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
  1. Generate/update Kinesthetic Teaching and Visual Servoing Branches Overview pages from live branch data.
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

## Branches Overview Automation

The pages:
- `docs/user-guide/fr3-example-capabilities/kinesthetic-teaching/branches-overview.md`
- `docs/user-guide/fr3-example-capabilities/visual-servoing/branches-overview.md`

is auto-generated in CI from:
- Live branch lists in:
  - `ulubilgeulusoy/franka_kinesthetic_teaching_GUI`
  - `ulubilgeulusoy/FR3_visual_servo_examples`
- Per-branch `README.md` summary text and extracted sections

This keeps branch names and summaries current without manual editing.

## Notes

- This repository focuses on operational documentation and setup knowledge transfer.
- Some pages reference external/internal resources (for example, SharePoint-hosted lab documents).

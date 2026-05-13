# PARC-FR3-Software-Docs

This repo contains the source files for the PARC FR3 Software Documentation site.
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
- `site/`: Generated static output from `mkdocs build`

## Local Development

Local preview/deploy commands:

```bash
pip install mkdocs mkdocs-material
mkdocs serve
mkdocs gh-deploy
```

For local preview, open: `http://127.0.0.1:8000`

## Notes

- This repository focuses on operational documentation and setup knowledge transfer.
- Some pages reference external/internal resources (for example, SharePoint-hosted lab documents).

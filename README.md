# PARC-FR3-Software-Docs

Central documentation website repository for FR3 software, related tooling, and HRI experiment workflows.

## Stack

- MkDocs
- Material for MkDocs

## Current Scope (Milestone 1)

- Multi-repo documentation structure and navigation
- FR3 platform and workspace guidance
- Operations and troubleshooting pages
- API-reference planning pages (placeholders for Doxygen/Python API generation)

## Repositories Covered

- https://github.com/ulubilgeulusoy/franka_kinesthetic_teaching_GUI
- https://github.com/ulubilgeulusoy/FR3_control_GUI
- https://github.com/ulubilgeulusoy/FR3_visual_servo_examples
- https://github.com/ulubilgeulusoy/franka_ws_jointfailsafe
- https://github.com/ulubilgeulusoy/Investment-HRI-Experiment-Task-GUIs
- https://github.com/ulubilgeulusoy/Event_marker_LSL_GUI

## Local Development

```bash
pip install mkdocs mkdocs-material
mkdocs serve
```

## Build

```bash
mkdocs build
```

## Publish

```bash
mkdocs gh-deploy
```

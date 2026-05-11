# Franka Workspace Guide

Current model:
- Baseline workspace: `franka_ws` (reference stack).
- Custom workspace: `franka_ws_jointfailsafe` (kinesthetic/backend experiments).

This split isolates controller experiments from the baseline stack and improves reproducibility of backend changes.

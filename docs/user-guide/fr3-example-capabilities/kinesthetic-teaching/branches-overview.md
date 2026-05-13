# Branches Overview

This section summarizes the Kinesthetic Teaching branch layout in:
<https://github.com/ulubilgeulusoy/franka_kinesthetic_teaching_GUI>

## Current branch heads

- `main` -> `a7ed711` (same head as `Jazzy_KT`)
- `Jazzy_KT` -> `a7ed711`
- `Humble_KT` -> `cb958d2`
- `Humble_KT_failsafe` -> `75f8f70`

## Summary

- `main`:
  - Current default line.
  - Matches `Jazzy_KT` at the same commit head.
  - Aligned with the repo README statement that the validated environment is Ubuntu 24.04 + ROS 2 Jazzy.
- `Jazzy_KT`:
  - Explicit Jazzy-focused branch for kinesthetic teaching workflows.
  - Currently identical to `main` (same commit head).
- `Humble_KT`:
  - Humble-era branch line kept separately from the current Jazzy line.
- `Humble_KT_failsafe`:
  - Humble branch variant intended for failsafe-related workflow/version handling.

## Practical guidance

- For current setup on PARC Desktop (Computer 1), use the Jazzy line (`main` / `Jazzy_KT`) unless your environment explicitly requires Humble compatibility.
- Use `Humble_KT` or `Humble_KT_failsafe` only when you are operating in a Humble-based stack and need that branch history.

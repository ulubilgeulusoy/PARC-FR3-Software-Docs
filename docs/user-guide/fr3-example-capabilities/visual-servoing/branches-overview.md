# Branches Overview

This page is auto-generated from the live GitHub branch list:
<https://github.com/ulubilgeulusoy/FR3_visual_servo_examples/branches>

Last updated: 2026-07-27 15:38 UTC

## Live Branches

- `main` -> `e233ef7`
- `new_GUI_test` -> `c3721a1`
- `visp_gui_combined` -> `53fd449`

## Branch Summaries

### `main`

- Branch URL: <https://github.com/ulubilgeulusoy/FR3_visual_servo_examples/tree/main>
- README: <https://github.com/ulubilgeulusoy/FR3_visual_servo_examples/blob/main/README.md>
- Head commit: `e233ef7`

**Branch Implementation Type**
- mixed (Qt modular + single-file reference)

**Build Target and Path**
- Target: `servoFrankaIBVS_combined`
- Build command sample: `cmake -S . -B build -DCMAKE_BUILD_TYPE=Release -DViSP_DIR=$HOME/visp_install/lib/cmake/visp`

**Run Entry Points**
- Launcher script: `./run_visual_servo_combined.sh`
- Direct binary: `./build/servoFrankaIBVS_combined \`

**Modes and Behavior**
- Supports mode 1 (single-tag) and mode 2 (sequenced multi-tag).

**Calibration Dependency**
- Required: yes
- Requires a valid `--eMc` calibration file and camera calibration verification before motion.

**Safety Guard Coverage**
- Safety guards: present
- Treat as controller-side safeguards, not certified safety.

**Workspace Model**
- standalone CMake app

**External Integration**
- arm_moving state post

**Branch Delta vs Main**
- Same commit as `main` (no branch-level code delta at head).

**Operational Readiness**
- Ready for quick try (with calibration verified)

### `new_GUI_test`

- Branch URL: <https://github.com/ulubilgeulusoy/FR3_visual_servo_examples/tree/new_GUI_test>
- README: <https://github.com/ulubilgeulusoy/FR3_visual_servo_examples/blob/new_GUI_test/README.md>
- Head commit: `c3721a1`

**Branch Implementation Type**
- mixed (Qt modular + single-file reference)

**Build Target and Path**
- Target: `servoFrankaIBVS_combined`
- Build command sample: `cmake -S . -B build -DCMAKE_BUILD_TYPE=Release -DViSP_DIR=$HOME/visp_install/lib/cmake/visp`

**Run Entry Points**
- Launcher script: `./run_visual_servo_combined.sh`
- Direct binary: `./build/servoFrankaIBVS_combined \`

**Modes and Behavior**
- Supports mode 1 (single-tag) and mode 2 (sequenced multi-tag).

**Calibration Dependency**
- Required: yes
- Requires a valid `--eMc` calibration file and camera calibration verification before motion.

**Safety Guard Coverage**
- Safety guards: present
- Treat as controller-side safeguards, not certified safety.

**Workspace Model**
- standalone CMake app

**External Integration**
- arm_moving state post

**Branch Delta vs Main**
- Different commit from `main` (branch-specific implementation/version).

**Operational Readiness**
- Ready for quick try (with calibration verified)

### `visp_gui_combined`

- Branch URL: <https://github.com/ulubilgeulusoy/FR3_visual_servo_examples/tree/visp_gui_combined>
- README: <https://github.com/ulubilgeulusoy/FR3_visual_servo_examples/blob/visp_gui_combined/README.md>
- Head commit: `53fd449`

**Branch Implementation Type**
- single-file combined ViSP app

**Build Target and Path**
- Target: `servoFrankaIBVS_combined`
- Build command sample: `cmake .. -DCMAKE_BUILD_TYPE=Release -DViSP_DIR=~/visp_install/lib/cmake/visp`

**Run Entry Points**
- Launcher script: `./run_visual_servo_combined.sh`
- Direct binary: `./build/servoFrankaIBVS_combined \`

**Modes and Behavior**
- Supports mode 1 (single-tag) and mode 2 (sequenced multi-tag).

**Calibration Dependency**
- Required: yes
- Requires a valid `--eMc` calibration file and camera calibration verification before motion.

**Safety Guard Coverage**
- Safety guards: present
- Treat as controller-side safeguards, not certified safety.

**Workspace Model**
- standalone CMake app

**External Integration**
- arm_moving state post

**Branch Delta vs Main**
- Different commit from `main` (branch-specific implementation/version).

**Operational Readiness**
- Ready for quick try (with calibration verified)

Note: generated automatically in CI from live branch data and branch README content.

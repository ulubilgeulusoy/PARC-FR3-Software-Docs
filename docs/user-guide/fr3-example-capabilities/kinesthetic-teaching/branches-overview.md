# Branches Overview

This page is auto-generated from the live GitHub branch list:
<https://github.com/ulubilgeulusoy/franka_kinesthetic_teaching_GUI/branches>

Last updated: 2026-07-06 16:13 UTC

## Live Branches

- `Humble_KT` -> `8b5bb0b`
- `Humble_KT_failsafe` -> `5f87376`
- `Jazzy_KT` -> `681b8ae`
- `main` -> `dc842fc`

## README Summaries

### `Humble_KT`

- Branch URL: <https://github.com/ulubilgeulusoy/franka_kinesthetic_teaching_GUI/tree/Humble_KT>
- README: <https://github.com/ulubilgeulusoy/franka_kinesthetic_teaching_GUI/blob/Humble_KT/README.md>
- Head commit: `8b5bb0b`

**Purpose**
- This repo contains one main application: a GUI that manages two workflows
- teach a motion by moving the robot by hand while joint states are recorded to CSV
- replay a recorded trajectory through the FR3 joint trajectory controller

**Validated Environment**
- This branch is currently set up and validated for a native Ubuntu 22.04.5 + ROS 2 Humble workflow.
- OS: Ubuntu 22.04.5 LTS
- Real-Time Kernel: Linux 6.9.0-rt5 (PREEMPT_RT enabled)

**Workspace Context**
- Workspace Type: mixed
- Workspace Name: workflows, rows, Shows
- Detection Confidence: low

**Main Workflows**
- ### Teach mode
- Start Teach (Record) is the full recording workflow, not just a gravity-compensation shortcut
- If the reduced teach stack is not already running, Start Teach (Record) launches it first

**How To Run**
- ### GUI User Guide
- Start Teach (Record) begins the teaching workflow.
- It first prompts for an optional CSV filename. If you leave it blank, the GUI creates a timestamped filename.

**Known Caveats**
- The playback script expects FR3 joint names fr3_joint1 through fr3_joint7
- The GUI uses fixed startup delays in a few places, so slow systems may still need more time
- The run flow currently waits a fixed 3 seconds after starting MoveIt before launching playback, then relies on runtime readiness checks inside the playback node


### `Humble_KT_failsafe`

- Branch URL: <https://github.com/ulubilgeulusoy/franka_kinesthetic_teaching_GUI/tree/Humble_KT_failsafe>
- README: <https://github.com/ulubilgeulusoy/franka_kinesthetic_teaching_GUI/blob/Humble_KT_failsafe/README.md>
- Head commit: `5f87376`

**Purpose**
- This repo contains one main application: a GUI that manages two workflows
- teach a motion by moving the robot by hand while joint states are recorded to CSV
- replay a recorded trajectory through the FR3 joint trajectory controller

**Validated Environment**
- This branch is currently set up and validated for a native Ubuntu 22.04.5 + ROS 2 Humble workflow.
- OS: Ubuntu 22.04.5 LTS
- Real-Time Kernel: Linux 6.9.0-rt5 (PREEMPT_RT enabled)

**Workspace Context**
- Workspace Type: custom
- Workspace Name: franka_ws_jointfailsafe
- Detection Confidence: high

**Main Workflows**
- ### Teach mode
- Start Teach (Record) is the full recording workflow, not just a gravity-compensation shortcut
- If the reduced teach stack is not already running, Start Teach (Record) arms the recorder first and only then enables gravity compensation

**How To Run**
- ### GUI User Guide
- Start Teach (Record) begins the teaching workflow.
- It first prompts for an optional CSV filename. If you leave it blank, the GUI creates a timestamped filename.

**Known Caveats**
- The playback script expects FR3 joint names fr3_joint1 through fr3_joint7
- The GUI still depends on ROS 2 / DDS / controller startup health; if the playback controller fails to load, the readiness gate will keep Run Trajectory from starting instead of forcing playback anyway
- CSV files are saved into the repo directory by default unless you provide another path


### `Jazzy_KT`

- Branch URL: <https://github.com/ulubilgeulusoy/franka_kinesthetic_teaching_GUI/tree/Jazzy_KT>
- README: <https://github.com/ulubilgeulusoy/franka_kinesthetic_teaching_GUI/blob/Jazzy_KT/README.md>
- Head commit: `681b8ae`

**Purpose**
- This repo contains one main application: a GUI that manages two workflows
- teach a motion by moving the robot by hand while joint states are recorded to CSV
- replay a recorded trajectory through the FR3 joint trajectory controller

**Validated Environment**
- This branch is currently set up and validated for a native Ubuntu 24.04 + ROS 2 Jazzy workflow.
- OS: Ubuntu 24.04 LTS (Noble)
- Real-Time Kernel: Linux 6.12.79-rt17 (PREEMPT_RT enabled)

**Workspace Context**
- Workspace Type: mixed
- Workspace Name: workflows, shows, rows
- Detection Confidence: low

**Main Workflows**
- ### Teach mode
- Starts the minimal teach bringup automatically if it is not already running
- Records joint motion while the arm is moved by hand

**How To Run**
- ### Record a trajectory
- Optionally click Start Gravity Mode if you want gravity compensation without recording yet.
- Click Start Teach (Record).

**Known Caveats**
- The recorder now prefers /NS_1/franka/joint_states so it records the real robot state instead of accidentally latching onto startup/default publisher values
- The GUI now delays gravity-compensation unlock during teach until the recorder is ready, so early user motion does not get lost before recording is active
- The playback script expects FR3 joint names fr3_joint1 through fr3_joint7


### `main`

- Branch URL: <https://github.com/ulubilgeulusoy/franka_kinesthetic_teaching_GUI/tree/main>
- README: <https://github.com/ulubilgeulusoy/franka_kinesthetic_teaching_GUI/blob/main/README.md>
- Head commit: `dc842fc`

**Purpose**
- This repo contains one main application: a GUI that manages two workflows
- teach a motion by moving the robot by hand while joint states are recorded to CSV
- replay a recorded trajectory through the FR3 joint trajectory controller

**Validated Environment**
- This branch is currently set up and validated for a native Ubuntu 24.04 + ROS 2 Jazzy workflow.
- OS: Ubuntu 24.04 LTS (Noble)
- Real-Time Kernel: Linux 6.12.79-rt17 (PREEMPT_RT enabled)

**Workspace Context**
- Workspace Type: custom
- Workspace Name: franka_ws_jointfailsafe
- Detection Confidence: high

**Main Workflows**
- ### Teach mode
- Starts the minimal teach bringup automatically if it is not already running
- Records joint motion while the arm is moved by hand

**How To Run**
- ### Record a trajectory
- Optionally click Start Gravity Mode if you want gravity compensation without recording yet.
- Click Start Teach (Record).

**Known Caveats**
- The recorder now prefers /NS_1/franka/joint_states so it records the real robot state instead of accidentally latching onto startup/default publisher values
- The GUI now delays gravity-compensation unlock during teach until the recorder is ready, so early user motion does not get lost before recording is active
- The playback script expects FR3 joint names fr3_joint1 through fr3_joint7


Note: this page is generated automatically in CI from live branch data and per-branch README content.

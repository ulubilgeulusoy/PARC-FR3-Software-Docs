# PARC FR3 Capabilitites

This section gives a high-level repository map for the three core FR3 software capabilities currently used in the PARC ecosystem.

## Capability Map

- **Kinesthetic Teaching** (`franka_kinesthetic_teaching_GUI`): This mode lets an operator physically guide the robot arm by hand so the robot can learn and replay that motion path. It provides teach-by-hand recording, gravity mode support, and trajectory playback workflows for FR3.
- **Visual Servoing** (`FR3_visual_servo_examples`): This mode makes the robot move based on what a camera sees, instead of following a manually taught path. It is camera-based FR3 control using ViSP + RealSense + AprilTag tracking.
- **Control GUI** (`FR3_control_GUI`): This is the operator launcher used to start and manage FR3 tools from a single Windows or Ubuntu interface. It starts **kinesthetic teaching** and **visual servoing** workflows only, with remote SSH/X11 or non-remote variants, and includes Lab Streaming Layer (LSL) integration for robot data sharing.

## Repository and Branch Summary

### 1) franka_kinesthetic_teaching_GUI

- **Repository:** <https://github.com/ulubilgeulusoy/franka_kinesthetic_teaching_GUI>
- **Role in the system:** operator-facing GUI for kinesthetic teaching and playback.
- **Branches, versions, and intent (high-level):**
  - `main`: current default line; documented for Ubuntu 24.04 + ROS 2 Jazzy.
  - `Jazzy_KT`: Jazzy-specific kinesthetic teaching line (Ubuntu 24.04 / ROS 2 Jazzy expected).
  - `Humble_KT`: Humble-specific kinesthetic teaching line (Ubuntu 22.04 / ROS 2 Humble expected).
  - `Humble_KT_failsafe`: Humble + failsafe kinesthetic teaching line (Ubuntu 22.04 / ROS 2 Humble expected), with failsafe-oriented backend/controller integration using the dedicated workspace: <https://github.com/ulubilgeulusoy/franka_ws_jointfailsafe>.

### 2) FR3_visual_servo_examples

- **Repository:** <https://github.com/ulubilgeulusoy/FR3_visual_servo_examples>
- **Role in the system:** visual servoing runtime for FR3 with safety guards and target-recovery behavior.
- **Control stack note:** primary runtime path is standalone C++ visual servoing with **ViSP + libfranka** (not a ROS 2 runtime dependency for the main control loop in the default flow).
- **Branches and intent (high-level):**
  - `main`: default standalone visual-servo line (ViSP + libfranka).
  - `visual_servoing_node`: node-oriented variant line (ROS integration intent).
  - `combined_modes`: combined-mode behavior variant.
  - `new_GUI_test`: GUI/interaction test line.
  - `CHRPS`: experimental branch line.

### 3) FR3_control_GUI

- **Repository:** <https://github.com/ulubilgeulusoy/FR3_control_GUI>
- **Role in the system:** central remote or non-remote control launcher environment with lab streaming layer (LSL) integrated for sharing robot data.
- **Branches, versions, and intent (high-level):**
  - `main`: current default line; documented for Windows launcher + remote Ubuntu 24.04 + ROS 2 Jazzy workflow.
  - `FR3_Control_Jazzy`: Jazzy-targeted control GUI variant (ROS 2 Jazzy expected).
  - `FR3_Control_Humble`: Humble-targeted control GUI variant (Ubuntu 22.04 / ROS 2 Humble expected).
  - `FR3_Control_without_LSL_Humble`: Humble variant (Ubuntu 22.04 / ROS 2 Humble expected) with LSL-related flow removed/altered.
  - `FR3_Control_Humble_without_remote_control`: Humble variant (Ubuntu 22.04 / ROS 2 Humble expected) focused on non-remote-control operation.

## Notes

- This page is intentionally concise and capability-oriented.
- Detailed repo-by-repo setup, branch usage, and operational procedures will be expanded in the FR3 User Guide sections.

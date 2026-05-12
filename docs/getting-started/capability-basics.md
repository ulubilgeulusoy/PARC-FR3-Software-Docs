# Capability Basics

This section explains the core building blocks used across PARC FR3 capabilities: **ROS 2 (with workspaces)**, **libfranka**, and **ViSP**.

## ROS 2 Basics (with Workspaces)

ROS 2 is the communication framework that organizes robotics software into nodes, topics, services, actions, and launch files.

In this project ecosystem, ROS 2 workspaces are the backend packaging/build context:

- `src/`: source packages
- `build/`: intermediate build outputs
- `install/`: runnable ROS environment after build
- `log/`: build/runtime logs

Typical workflow:

1. Build with `colcon build`
2. Source `install/setup.bash`
3. Run ROS launch/nodes using that sourced environment

### PARC ROS2 workspace context

- `~/franka_ws`: baseline/reference workspace
- `~/franka_ws_jointfailsafe`: custom workspace for kinesthetic-teaching backend experiments (includes `franka_joint_limit_failsafe`): <https://github.com/ulubilgeulusoy/franka_ws_jointfailsafe>

This split allows backend controller experiments without directly changing the baseline workspace.

## libfranka Basics

`libfranka` is the low-level robot interface used to send commands to FR3 and read robot state.

In practical terms, it is the control-side library that executes robot motion commands after higher-level logic decides what the motion should be.

## ViSP Basics

ViSP (Visual Servoing Platform) is the vision/control library used for tracking and visual-servo computation.

In this setup, ViSP is used to:

- process camera observations
- compute visual error
- produce control commands that are then sent through `libfranka`

Important distinction:

- ViSP is not ROS 2 by itself.
- ViSP can be used inside a ROS node, but your current primary visual-servo flow is a standalone C++ ViSP + `libfranka` path.

## How These Basics Map to PARC FR3 Capabilities

### 1) Kinesthetic Teaching (`franka_kinesthetic_teaching_GUI`)

- Uses ROS 2 workspace infrastructure for backend bringup and controllers.
- Uses the custom `franka_ws_jointfailsafe` workspace for failsafe-oriented variants: <https://github.com/ulubilgeulusoy/franka_ws_jointfailsafe>.
- Uses `libfranka` through the FR3 backend stack.

### 2) Visual Servoing (`FR3_visual_servo_examples`)

- Primary runtime path is standalone C++ with **ViSP + libfranka**.
- Not dependent on ROS 2 runtime for the main control loop in the default flow.
- Uses ViSP for vision/control computation and `libfranka` for robot command execution.

### 3) Control GUI (`FR3_control_GUI`)

- Orchestrates tool startup and operation flows from Windows to Ubuntu targets.
- In remote variants, launches ROS/visual-servo/kinesthetic tools over SSH/X11.
- Branch variants support different ROS distro lines (Jazzy/Humble) and control styles (remote vs non-remote).

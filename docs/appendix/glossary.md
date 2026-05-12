# Glossary

- **FR3**: Franka Research 3 robot arm platform.
- **FCI**: Franka Control Interface used for low-level communication with the robot.
- **ROS 2**: Robot middleware used for node communication, launch orchestration, and package-based robotics workflows.
- **ROS 2 Workspace**: Folder structure (`src`, `build`, `install`, `log`) used to build and run ROS-based packages.
- **colcon**: Standard build tool used for ROS 2 workspaces.
- **libfranka**: C++ library used to command FR3 motion and access robot state.
- **ViSP**: Visual Servoing Platform library used for camera-based control logic.
- **Visual Servoing**: Camera-feedback control method that moves the robot to reduce visual error.
- **Kinesthetic Teaching**: Teach-by-hand workflow where an operator physically guides the robot and records motion for playback.
- **LSL**: Lab Streaming Layer, used to synchronize robot signals with experiment data streams.
- **E-stop**: Emergency stop button that immediately halts motion and locks joints until reset.
- **PREEMPT_RT Kernel**: Real-time Linux kernel configuration used for deterministic control timing.
- **VOLT**: PARC touchscreen laptop used for FR3 remote-control workflows.

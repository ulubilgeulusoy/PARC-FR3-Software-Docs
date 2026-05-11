# Repository Map

- `FR3_control_GUI`: Windows launcher/orchestrator for remote FR3 tools over SSH/X11.
- `franka_kinesthetic_teaching_GUI`: Teach/gravity/playback GUI for FR3.
- `FR3_visual_servo_examples`: ViSP/libfranka visual servoing application.
- `franka_ws_jointfailsafe`: Custom ROS2 backend workspace with joint-limit failsafe controller.
- `Investment-HRI-Experiment-Task-GUIs`: Combined leak-check/visual/reporting experiment GUI stack.
- `Event_marker_LSL_GUI`: LSL event marker GUI for synchronized experimental streams.

Integration summary:
- Control orchestration starts from `FR3_control_GUI`.
- Robot backend comes from ROS2 workspaces (`franka_ws` baseline, `franka_ws_jointfailsafe` custom).
- Visual servoing currently runs as a standalone C++ app (ViSP + libfranka).
- Experiment tooling is parallel to robot control and shares timing/data context through CSV and LSL workflows.

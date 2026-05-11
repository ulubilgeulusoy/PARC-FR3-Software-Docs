# ROS2 ViSP libfranka 101

Core distinction:
- ROS2: communication and system orchestration (nodes/topics/services/actions/launch).
- ViSP: visual tracking and visual-servo control-law computations.
- libfranka: low-level FR3 command interface.

Control path mental model:
Camera data -> ViSP feature tracking/control -> safe velocity formulation -> libfranka command loop -> FR3 motion.

Key design note:
ViSP is a library, not a ROS2 node by itself. A ROS2 node can use ViSP internally.

# System Data Flow

- Robot control data path: GUI/launch -> ROS2/backend and/or standalone visual-servo process -> FR3.
- Experiment data path: task GUIs + event markers -> CSV/LSL streams -> recording/analysis.
- Operational bridging: `FR3_control_GUI` starts remote tools; LSL marker GUI tags timeline events; robot state can be bridged to LSL when needed.

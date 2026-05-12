# Safety

## Hardware Safety (FR3 System)

- Verify that all FR3 hardware connections are secure before operation (power, Ethernet, and end-effector/gripper interfaces).
- Use a properly configured real-time Linux kernel (control environment) for deterministic behavior.
- Keep the robot workspace clear of loose objects, cables, and obstructions.

## User and Operational Safety

- Only trained users should operate FR3 in active control modes.
- Before starting motion, confirm that nearby users know a robot run is about to begin.
- Stop immediately (e-stop or stop/quit GUI button) if motion appears unexpected, unstable, or inconsistent with operator commands.

## E-stop Usage

- The E-stop is a safety device that immediately stops arm motion and locks joints.
- Press the E-stop button to stop the robot immediately.
- To reset, pull (release) the red E-stop portion upward.
- No twist is required for this E-stop in the current lab setup.
- After E-stop reset, verify robot/control state before resuming operation.

## Minimum Safety Routine Before Every Session

1. Confirm environment is clear and users are informed.
2. Confirm E-stop is reachable and users know how to use it.


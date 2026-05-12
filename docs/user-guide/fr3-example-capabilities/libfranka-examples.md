# libfranka Examples

- These examples are from `libfranka 0.15.0` on the Dell Computer (Computer 3).
  - You can find the example folder at: `~/libfranka/build/examples`.
  - You can inspect these examples directly and/or use a generative AI assistant to understand how to operate specific examples.

## Running a libfranka Example

Before running an example:

- Make sure you completed the required startup steps and the robot status light is green.
- Make sure the E-stop is available and operational so you can stop FR3 immediately if needed.

Then:

1. Open an Ubuntu terminal on Dell Computer (Computer 3).
2. Run:

```bash
cd ~/libfranka/build/examples
```

3. Run an example command (from the slide):

```bash
sudo ./joint_point_to_point_motion 172.16.0.2 0 -0.785 0 -2.356 0 1.571 0 0.2
```

4. Enter the password shown in the slide when prompted.

## Important Note

- Different `libfranka` examples require different input arguments and produce different outputs.
- Always check the specific example requirements before running it.

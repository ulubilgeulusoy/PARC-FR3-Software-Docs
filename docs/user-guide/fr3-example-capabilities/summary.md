# Summary

- **Standard libfranka examples**
  - `libfranka` examples are sample programs provided with the library that demonstrate how to communicate with and control the robot through the Franka Control Interface.
  - They cover basic tasks such as reading robot state, generating joint and Cartesian motions, and implementing simple control strategies, and they serve as a starting point for custom applications.

- **Kinesthetic Teaching**
  - Kinesthetic teaching is a robotics method where a human physically guides the robot through a desired motion, allowing the robot to record the trajectory and forces involved.
  - The robot can later reproduce or generalize that motion, enabling intuitive programming without writing low-level motion code.

- **Visual Servoing**
  - Visual servoing is a robotics control method that uses camera feedback to continuously adjust robot motion to reach or maintain a desired visual target.
  - The robot processes image features in real time and updates movement to minimize error between the current view and the target view.

## Read Before Proceed

Kinesthetic Teaching and Visual Servoing examples here are based on the Investment HRI experiment conducted in April 2026. Different versions of these two capabilities were developed on the two computers listed in this documentation, so behavior may vary between environments. For detailed version-specific information, refer to the relevant repositories and branch notes.

# Recommended Installation Steps

[https://frankarobotics.github.io/docs/overview.html](https://frankarobotics.github.io/docs/overview.html) follow instructions from here but use a generative AI to guide you because the instructions may be outdated.

*Note: This list is intended to provide a high-level understanding of the setup process and may appear intentionally broad. For detailed, step-by-step instructions, refer to the official documentation links provided above.*

<ol>
  <li>
    Install Ubuntu
    <ul>
      <li>Install a supported version of Ubuntu (e.g., Ubuntu 22.04 or 24.04) on a dedicated workstation.</li>
    </ul>
  </li>
  <li>
    Install and Configure a Real-Time Kernel
    <ul>
      <li>Set up a PREEMPT_RT kernel to enable real-time performance.</li>
      <li>Real-time execution is required because robot control loops operate at approximately 1 kHz.</li>
    </ul>
  </li>
  <li>
    Check Robot System Firmware
    <ul>
      <li>Access the Franka Desk web interface by connecting the robot via Ethernet and entering its IP address (e.g., <code>172.16.0.2</code>) in a web browser.</li>
      <li>Record the system image version (e.g., 5.7.2), as it determines software compatibility.</li>
    </ul>
  </li>
  <li>
    Select a Compatible libfranka Version
    <ul>
      <li>Choose the appropriate libfranka version based on the robot’s firmware using the official compatibility table.</li>
    </ul>
  </li>
  <li>
    Install Base Dependencies
    <ul>
      <li>Install required system dependencies for building libfranka (e.g., build tools, Eigen, and other required libraries).</li>
    </ul>
  </li>
  <li>
    Configure Real-Time Permissions
    <ul>
      <li>Set up user permissions (e.g., real-time group and limits configuration) to allow real-time scheduling.</li>
    </ul>
  </li>
  <li>
    Set Up Networking
    <ul>
      <li>Configure a direct Ethernet connection between the workstation and the robot using a static IP configuration (e.g., <code>172.16.0.1</code> for the PC).</li>
    </ul>
  </li>
  <li>
    Configure Robot State (Franka Desk)
    <ul>
      <li>Using the web interface:
        <ol>
          <li>Unlock the robot</li>
          <li>Release brakes</li>
          <li>Enable FCI</li>
          <li>Release control</li>
        </ol>
      </li>
    </ul>
  </li>
  <li>
    Build and Install libfranka
    <ul>
      <li>Clone the repository, check out the compatible version, and build/install it on the system.</li>
    </ul>
  </li>
  <li>
    Validate Connection and Motion
    <ul>
      <li>Run a non-motion example to verify communication.</li>
      <li>Run a motion example to confirm successful control.</li>
    </ul>
  </li>
  <li>Install ROS 2 and Franka ROS Interface</li>
</ol>

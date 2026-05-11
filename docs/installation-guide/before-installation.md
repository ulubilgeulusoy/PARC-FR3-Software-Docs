# Before Installation

- Understand that Ubuntu, real-time (RT) Kernel, ROS, libfranka, and robot firmware versions are important to consider to eliminate any mismatched versions during installation.
    - Check the FR3 robot firmware version and make sure that the libfranka version you are selecting is compatible with the firmware.
    - Decide on the Ubuntu and RT Kernel versions (you have to use a RT kernel; the generic Ubuntu kernel does not work for controlling the FR3 arm).
        - Consider your desktop hardware compatibility when selecting these versions, as we had trouble with Ubuntu/RT-Kernel versions with our motherboard/wifi module compatibility, and we had to change to a different RT kernel version.
    - Based on your Ubuntu and RT Kernels, decide on your ROS 2 version.
    - Check the following documentation: [https://frankarobotics.github.io/docs/overview.html](https://frankarobotics.github.io/docs/overview.html), but keep in mind that the guide is not great, so use a generative AI to guide you through installation.

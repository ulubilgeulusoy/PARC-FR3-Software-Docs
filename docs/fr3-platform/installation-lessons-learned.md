# Installation Lessons Learned

Based on installation-guideline slides (March 30, 2026 context):
- Treat Ubuntu, RT kernel, ROS2, libfranka, and firmware as a compatibility set.
- Kernel/hardware compatibility can block networking or stability; newer is not always better.
- RT kernel alone is not enough; user/group/limits configuration is also required.
- Prefer capturing working version sets before upgrades.

Reference sources:
- `Franka Research 3 (FR3) Robot Arm Installation Guidelines.pptx`

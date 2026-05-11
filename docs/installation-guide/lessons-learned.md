# Lessons Learned

## Real-Time Kernel

- Multiple RT kernel versions were evaluated during setup.
- Some newer RT kernels caused WiFi and network driver failures on the target hardware.
- The final stable choice for this setup was Linux 6.12 RT.
- **Lesson learned:** choose the RT kernel based on proven hardware compatibility, not just version recency.

## Real-Time Kernel Permissions

- Control still failed even after installing an RT kernel until real-time user permissions were configured.
- Effective fix: add the user to the real-time group and update `limits.conf` accordingly.
- **Lesson learned:** RT kernel installation is necessary but not sufficient; user-level scheduling permissions must also be correct.

## Libfranka Version Compatibility

- A major compatibility issue occurred between robot firmware (5.7.2 -> server version 9) and `libfranka` 0.19.
- Effective fix: downgrade to `libfranka` 0.17 for compatibility with the installed firmware.
- **Lesson learned:** robot firmware version constrains the usable `libfranka` version and should drive library selection early.

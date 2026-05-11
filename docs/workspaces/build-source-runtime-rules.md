# Build Source Runtime Rules

- Rebuild with `colcon` when workspace source packages change.
- Re-source workspace setup in each shell before launches.
- Standalone GUI edits generally do not require workspace rebuild.
- Visual-servo standalone C++ changes follow that repo's own CMake/Make flow.

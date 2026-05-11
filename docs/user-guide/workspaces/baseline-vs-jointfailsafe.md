# Baseline vs Jointfailsafe

- Baseline workspace is used as a standard reference and dependency context.
- `franka_ws_jointfailsafe` owns custom controller behavior near joint limits for kinesthetic teaching.
- GUI and backend are related but not the same artifact: GUI can live outside workspace while using sourced workspace packages.

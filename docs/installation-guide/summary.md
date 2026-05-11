# Summary

This page summarizes the internal **Franka Research 3 (FR3) Robot Arm Installation Guidelines** when you try to operate the FR3 via a computer and captures the practical installation context for FR3 control setup workflows.

Information provided here are background information on the installation of the FR3 control system on the PARC desktop computer on March 30, 2026. **It is important to note that this is not intended to serve as a step-by-step installation guide**; rather, it primarily functions as a lessons learned document for future setups of FR3 controls on different systems.

## Internal document access

The original slide deck is an internal document for **CU Boulder Bioastronautics students, faculty, and staff**:

- [Franka Research 3 (FR3) Robot Arm Installation Guidelines (internal SharePoint link)](https://o365coloradoedu.sharepoint.com/:p:/r/sites/AEROENGR-ArquillaGroup2/Shared%20Documents/Franka%20Research%203%20(FR3)%20Robot%20Arm%20Documents/Franka%20Research%203%20(FR3)%20Robot%20Arm%20Installation%20Guidelines.pptx?d=w0327bfc211e0426aaab62a714ced6dc8&csf=1&web=1&e=WpzqHb)

This documentation site republishes and organizes the key installation content so it can be used directly here.

## PARC Desktop (labeled as Computer 1) Specs and Configuration as of April 2026

### Hardware

| Component | Specification |
|---|---|
| CPU | AMD Ryzen 7 7800X3D (8 cores / 16 threads, 4.2 GHz, Zen 4) |
| GPU | NVIDIA GeForce RTX 5070 Ti, 16GB GDDR7, PCIe 5.0 |
| Memory (RAM) | 32 GB DDR5 (6000 MHz), G.SKILL Flare X5 (2×16 GB) |
| Storage | 2 TB NVMe SSD (Kingston KC3000, PCIe 4.0) |
| Motherboard | GIGABYTE B850 EAGLE WIFI7 (AM5, PCIe 5.0, WiFi 7, 2.5GbE) |
| Power Supply | Corsair RM750e (750W, ATX 3.1, fully modular) |
| Cooling | Thermalright Phantom Spirit 120 SE (air cooler) |
| Case | Corsair 3500X Mid-Tower |

### Software Stack and FR3 Control

| Category | Component | Specification / Version Details |
|---|---|---|
| Operating System | OS | Ubuntu 24.04 LTS (Noble) |
| Operating System | Real-Time Kernel | Linux 6.12.79-rt17 (PREEMPT_RT enabled) |
| Middleware | ROS Version | ROS 2 Jazzy |
| FR3 Control Stack | Robot Library | libfranka 0.19.0 |
| FR3 Control Stack | Real-Time Requirement | PREEMPT_RT kernel required for deterministic control |

### Attention

As of April 2026, the PARC Desktop computer is dual-booted, with Windows as the default OS. If you want to use this computer for robot control, you need to follow these instructions to select the right configuration from the GRUB menu: [PARC Desktop User Information (Check Before Use).docx](https://o365coloradoedu.sharepoint.com/:w:/r/sites/AEROENGR-ArquillaGroup2/Shared%20Documents/General/PARC%20Desktop%20User%20Information%20(Check%20Before%20Use).docx?d=w67a442d9fd9944cc910169c7acd1d6ae&csf=1&web=1&e=OsKOln)

## How to use this page with the rest of this site

- Use this page for high-level FR3 control installation context.
- Use **Before Installation** and **Recommended Installation Steps** for structured preparation and process flow.
- Use **Lessons Learned** for known pitfalls and practical constraints observed during prior setups.

## Source note

- Source document summarized: `Franka Research 3 (FR3) Robot Arm Installation Guidelines.pptx` (internal).
- Supporting reference: `PARC Desktop User Information (Check Before Use).docx` (internal).
- Last summarized for this page: 2026-05-11.

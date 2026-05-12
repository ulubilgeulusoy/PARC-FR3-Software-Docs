# Computers

## Things to Consider Before Using FR3

- Keep in mind that the computer you use for controlling the FR3 arm will affect your programming developments, as both computers use different versions of Ubuntu, real-time (RT) kernel, ROS, and `libfranka`.
- Dell Computer (Computer 3) has older versions of Ubuntu, RT Kernel, ROS, and `libfranka` compared to the PARC desktop (Computer 1).

## FR3 Control Option 1

### Dell Computer (Computer 3) Specs and Configuration

#### Hardware

| Component | Specification |
|---|---|
| CPU | Intel Core i7-1185G7 (11th Gen, 3.00 GHz) |
| GPU | Intel Iris Xe Graphics (integrated) |
| Memory (RAM) | 30 GB |
| Storage | 476.9 GB NVMe SSD |

#### Software Stack and FR3 Control

| Category | Component | Specification / Version Details |
|---|---|---|
| Operating System | OS | Ubuntu 22.04.5 LTS |
| Operating System | Real-Time Kernel | Linux 6.9.0-rt5 (PREEMPT_RT enabled) |
| Middleware | ROS Version | ROS 2 Humble |
| FR3 Control Stack | Robot Library | libfranka 0.15.0 |
| FR3 Control Stack | Real-Time Requirement | PREEMPT_RT kernel required for deterministic control |

#### Attention

As of April 2026, the Dell computer is configured to boot with a real-time (RT) kernel. This is the main computer used for FR3 control in the PARC room.

## FR3 Control Option 2

### PARC Desktop (Computer 1) Specs and Configuration

#### Hardware

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

#### Software Stack and FR3 Control

| Category | Component | Specification / Version Details |
|---|---|---|
| Operating System | OS | Ubuntu 24.04 LTS (Noble) |
| Operating System | Real-Time Kernel | Linux 6.12.79-rt17 (PREEMPT_RT enabled) |
| Middleware | ROS Version | ROS 2 Jazzy |
| FR3 Control Stack | Robot Library | libfranka 0.19.0 |
| FR3 Control Stack | Real-Time Requirement | PREEMPT_RT kernel required for deterministic control |

#### Attention

As of April 2026, the PARC Desktop computer is dual-booted, with Windows as the default OS. If you want to use this computer for robot control, you need to follow these instructions to select the right configuration from the GRUB menu: [PARC Desktop User Information (Check Before Use).docx](https://o365coloradoedu.sharepoint.com/:w:/r/sites/AEROENGR-ArquillaGroup2/Shared%20Documents/General/PARC%20Desktop%20User%20Information%20(Check%20Before%20Use).docx?d=w67a442d9fd9944cc910169c7acd1d6ae&csf=1&web=1&e=OsKOln)

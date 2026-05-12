# Read Before Proceed

## Real-Time Control Requirement

As of April 2026, the Franka Research 3 only works with a properly configured real-time kernel to ensure deterministic 1 kHz control loop performance, meaning you can only control the robot via Linux/Ubuntu with a real-time kernel.

Any degradation in real-time scheduling or latency can compromise control stability and trigger safety mechanisms. Also, keep in mind that, as of April 2026, NVIDIA GPUs are not supported in open-source real-time kernels, so you cannot utilize an NVIDIA GPU when you use a robot arm.

## Computer Usage Context

As of April 2026, the Franka Research 3 can be operated on two different computers located in the PARC room:

- Standard Dell computer (labeled as Computer 3)
- Custom-built desktop computer (PARC desktop computer, labeled as Computer 1)

Depending on your use case, you can use either. One thing to consider is that the PARC desktop computer has very high specs, and using it solely for robot control may be a waste of resources if you also need a computer to do other things, as Ubuntu with real-time kernels has very limited use cases (e.g., you cannot use BIOPAC and NVIDIA graphics cards).

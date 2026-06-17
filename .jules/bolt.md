## 2024-06-17 - Command Delta Optimization for Serial I/O
**Learning:** Continuous Serial I/O writes in a real-time control loop (like video processing) create significant overhead (~0.24s for 1000 iterations), even if the command string hasn't changed.
**Action:** Implement a delta-based write pattern by tracking the last sent command state and only writing to the serial port when the command changes and the port is open.

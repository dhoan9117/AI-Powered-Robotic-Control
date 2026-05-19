## 2024-05-19 - Avoid Flooding Serial Port
**Learning:** Writing data over a serial port is an extremely slow I/O operation. In a computer-vision or webcam-driven loop, the application is likely processing frames 30+ times a second. Flooding the serial buffer with redundant commands causes I/O blocking and wastes Arduino parsing cycles.
**Action:** When implementing real-time control via serial, always implement a delta-based caching mechanism (like `last_cmd`) to ensure commands are only sent when the target state actually changes.


## 2024-05-22 - [Delta-based Hardware I/O Optimization]
**Learning:** Calling `arduino.write()` in a high-frequency real-time vision loop (~30FPS) causes significant I/O blocking overhead, even when the command state hasn't changed.
**Action:** Always track the `last_sent_cmd` state and implement a delta check (`if cmd != last_sent_cmd:`) before executing Serial communication to drastically reduce blocking loop latency in embedded hardware integrations.

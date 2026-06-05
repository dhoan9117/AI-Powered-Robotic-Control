## 2024-06-05 - Serial I/O Overhead in Hardware Control Loops
**Learning:** Calling `arduino.write()` indiscriminately on every frame in a control loop incurs severe performance penalties due to synchronous hardware I/O blocking. A benchmark revealed that sending a redundant 11-byte command 1000 times took ~0.35s, compared to ~0.0005s when using a delta check.
**Action:** Always track the last sent hardware command (`last_cmd`) and only execute physical writes when the control payload has actually changed.

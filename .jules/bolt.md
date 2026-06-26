## 2024-05-15 - Serial I/O Delta Writes
**Learning:** In control loops (like `dieukhien_servo.py`), writing to the Arduino on every frame causes significant overhead (~0.24s for 1000 iterations). Serial I/O is a major bottleneck.
**Action:** Implemented a delta-based write pattern by tracking the `last_cmd` state and only calling `arduino.write()` if the current command string differs from the previous one, reducing overhead to ~0.0004s when unchanged. Ensure to only update `last_cmd` if `arduino.is_open` is true.

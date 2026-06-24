## 2024-05-24 - Serial I/O Bottleneck Resolved
**Learning:** Sending data to hardware over the serial port on every loop iteration unconditionally causes massive performance overhead and blocking, particularly when the system command value hasn't actually changed.
**Action:** Implement delta-based hardware writes by storing the last sent command in a tracking variable (e.g., `last_cmd`), executing `arduino.write()` only if the current command string differs from it, and ensuring state tracking accounts for hardware availability.

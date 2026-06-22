## 2024-05-19 - Delta-Based Serial Communication
**Learning:** Found a major performance bottleneck where the control loop calls `arduino.write()` indiscriminately on every video frame in `code/dieukhien_servo.py`, even if the computed servo angles haven't changed. This causes significant Serial I/O overhead.
**Action:** Implement delta-based writes by tracking a `last_cmd` string and only calling `arduino.write()` if the current command string differs from the previous one. This drastically reduces the loop overhead and prevents hardware buffer flooding.

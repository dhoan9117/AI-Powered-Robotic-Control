## 2024-07-07 - Implement Serial I/O Optimization Pattern
**Learning:** Found a performance bottleneck in `code/dieukhien_servo.py` where it repeatedly sends identical commands to the Arduino via `arduino.write()` even when the pose/hand tracking data hasn't changed. This causes unnecessary Serial I/O overhead.
**Action:** Implemented a delta-based write approach, tracking `last_cmd` and only calling `arduino.write()` when the current command differs from the previous one, significantly reducing loop overhead.

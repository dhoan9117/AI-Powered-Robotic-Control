## 2024-07-04 - Delta-based Serial Write Optimization
**Learning:** In performance-critical control loops, sending data over Serial unconditionally on every frame creates significant I/O overhead and can overload the hardware buffer, bottlenecking the video processing loop.
**Action:** Implement delta-based writes by tracking the `last_cmd` state and only calling `arduino.write()` when the data has actually changed. Ensure `last_cmd` is updated only if `arduino.is_open` is true.

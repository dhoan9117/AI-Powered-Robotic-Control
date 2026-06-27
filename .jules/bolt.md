## 2024-06-27 - Reduce Serial I/O Overhead with Delta Writes
**Learning:** In control loops with Arduino, unconditional serial writes create severe bottlenecks due to I/O latency, even when data hasn't changed.
**Action:** Implement delta-based writes by tracking `last_cmd` and ensuring it is only updated when `arduino.is_open` and the write is successful to prevent desynchronization.

## 2024-06-21 - Serial I/O Delta Writes
**Learning:** Serial communication is a bottleneck in control loops. Unconditional `arduino.write()` calls add significant overhead, especially when data points remain the same (e.g. 1000 writes vs 1 write when unchanged).
**Action:** Track the 'last sent' state and only call `arduino.write()` if the current command string differs from the previous one.

## 2024-05-24 - Serial I/O Delta Optimization
**Learning:** Writing to a Serial port continuously (e.g., in a fast camera loop) without checking if the data has changed introduces significant I/O overhead and can cause buffer overruns on the receiving Arduino, blocking the main execution thread.
**Action:** Implement a delta-check pattern (`last_sent_cmd`) to only invoke `arduino.write()` when the command string actually changes. This dramatically reduces loop latency.

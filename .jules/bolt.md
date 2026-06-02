
## 2024-06-02 - Serial Output Optimization
**Learning:** In control loops that communicate with hardware, redundant `Serial.write` calls introduce severe loop blocking latency. A mock benchmark measured ~0.046s for 1000 unchanged iterations compared to ~0.001s when checking for changes.
**Action:** Always implement a delta-check (caching the `last_cmd` string) before writing to serial hardware in high-frequency loops to minimize I/O overhead.

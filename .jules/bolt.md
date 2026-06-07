
## 2024-05-24 - Serial I/O Bottleneck Avoidance
**Learning:** Sending redundant Serial commands to Arduino in a tight hardware/CV control loop (like tracking pose/hands) introduces unnecessary I/O overhead and can saturate the serial buffer when data hasn't changed.
**Action:** Always implement delta-based state tracking (`last_cmd`) in high-frequency hardware control loops to only write to the serial port when the outgoing command string physically changes.

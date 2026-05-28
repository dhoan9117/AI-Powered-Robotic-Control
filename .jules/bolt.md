## 2024-05-28 - Optimizing Embedded Systems Real-time Loop with Delta Serial Writes
**Learning:** In real-time computer vision hardware control scripts, unconditionally calling `arduino.write()` every frame creates massive Serial I/O bottleneck, as writing over serial is inherently slow.
**Action:** Always implement a delta-based caching mechanism (checking if `current_cmd != last_cmd`) before performing expensive serial write operations to ensure the loop runs at maximum FPS and only communicates state changes.

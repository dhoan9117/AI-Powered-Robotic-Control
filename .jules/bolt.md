## 2024-05-24 - Hardware Serial Optimization
**Learning:** Writing data over serial is extremely slow compared to CPU processing in tight loops like `cap.isOpened()`. Sending the same hardware command repeatedly blocks the thread and creates unnecessary I/O overhead.
**Action:** Always implement delta-based writes (caching the last sent command and only writing when `new_cmd != last_cmd`) for hardware communication in performance loops.

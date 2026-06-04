## 2026-06-04 - Serial I/O Optimization in Control Loop
**Learning:** Continuous writing to PySerial () in an unconstrained  computer vision loop causes significant performance bottleneck due to unnecessary I/O overhead when the mechanical command hasn't changed.
**Action:** Always implement delta-based writes () when bridging fast computer vision loops to slower hardware interfaces to dramatically reduce I/O waiting time and CPU usage.
## 2023-11-20 - Serial I/O Optimization in Control Loop
**Learning:** Continuous writing to PySerial (`arduino.write`) in an unconstrained `while cap.isOpened():` computer vision loop causes significant performance bottleneck due to unnecessary I/O overhead when the mechanical command hasn't changed.
**Action:** Always implement delta-based writes (`if cmd != last_cmd:`) when bridging fast computer vision loops to slower hardware interfaces to dramatically reduce I/O waiting time and CPU usage.

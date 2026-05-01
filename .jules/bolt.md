## 2024-05-01 - Avoid temporary lists in gesture detection
**Learning:** In the performance-critical real-time video processing loop of `dieukhien_servo.py`, building temporary lists (`fingers.append()`) and then calling `.count()` creates unnecessary memory allocations and is an anti-pattern for this specific codebase architecture.
**Action:** Use a simple integer counter (`count += 1`) instead of lists for aggregating binary states like fingers up/down.

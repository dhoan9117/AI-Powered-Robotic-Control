## 2025-02-18 - Avoid temporary list allocations and `.count()` in real-time MediaPipe CV loops
**Learning:** In performance-critical real-time video processing loops using MediaPipe, building temporary lists and then using `.count()` aggregate operations adds unnecessary overhead through object creation and multiple loop iterations.
**Action:** Replace temporary lists and aggregate operations with simple integer counters whenever counting states. This avoids memory allocation in every frame, yielding performance improvements in gesture detection logic.

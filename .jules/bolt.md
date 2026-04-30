## 2024-05-24 - Avoid list allocations in tight loops
**Learning:** Found a performance bottleneck where a list `fingers = []` was being allocated every frame in a real-time OpenCV/MediaPipe loop, populated with `.append()`, and then tallied using `.count(1)`.
**Action:** Replace intermediate list collections with direct primitive accumulators (e.g., `count = 0` then `count += 1`) in any high-frequency loop to reduce GC pressure and object allocation overhead.


## 2024-05-24 - Integer Counter Optimization over Temporary List Allocation in Real-time Vision Loop
**Learning:** In highly iterative, performance-critical real-time vision pipelines (like MediaPipe gesture detection loops), allocating temporary lists (e.g., `fingers = []`) and using aggregate operations (e.g., `fingers.append(x)` and `fingers.count(1)`) creates unnecessary memory overhead and garbage collection pressure.
**Action:** Replace temporary list accumulations with simple integer counters (`count = 0`, `count += 1`) when only the final aggregate count is required. This avoids list initialization, dynamic resizing, and list traversal overhead inside the loop.

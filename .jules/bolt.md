## 2024-06-25 - Replace Temporary List Allocation in Loops
**Learning:** In performance-critical real-time loops (e.g., MediaPipe frame processing), constructing temporary lists and calling aggregation methods like `.count()` on them creates unnecessary memory overhead and slows down processing.
**Action:** Replace `list.append()` and `list.count()` inside real-time loops with simple integer counters (`+= 1`) where only the total count is needed, to optimize memory usage and processing speed.

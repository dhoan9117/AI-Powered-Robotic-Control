## 2024-04-17 - [Optimized real-time memory allocation in computer vision loop]
**Learning:** Temporary list allocations (`fingers = []`) combined with aggregation operations (`.count(1)`) inside tight, real-time loops (e.g. per-frame video processing) cause unnecessary memory allocation and garbage collection overhead.
**Action:** Replace list building with direct integer counters to achieve the same logic while reducing memory footprint and GC pressure.

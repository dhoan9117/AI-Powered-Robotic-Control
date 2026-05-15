## 2025-05-15 - Optimizing Hand Gesture Processing
**Learning:** In performance-critical video processing loops, avoid allocating temporary arrays and using list operations like `fingers.count(1)` when a simple integer counter will do.
**Action:** Replace `fingers = []`, appending 1/0, and `fingers.count(1)` with a single integer counter `count = 0` and increment it directly to reduce memory allocations overhead per frame.

## 2024-05-15 - [Integer Counter vs List Allocation in Hot Loops]
**Learning:** In real-time video processing (e.g. OpenCV frame loops), dynamically allocating a list and then calling `.count()` on it creates unnecessary memory allocation overhead. A simple integer counter is functionally equivalent but avoids this overhead.
**Action:** Use primitive variables directly when aggregating simple counts or boolean flags inside hot loops rather than building and parsing lists.

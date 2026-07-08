## 2024-05-24 - Serial I/O Optimization
**Learning:** Serial I/O overhead in the control loop was a major bottleneck (~0.24s loop time vs ~0.0004s).
**Action:** Always implement delta-based writes (tracking 'last_cmd') to avoid redundant serial communication when data is unchanged.

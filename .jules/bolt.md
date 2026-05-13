## 2023-10-24 - Serial I/O Optimizations
**Learning:** In Arduino control loops, unconditional `serial.write()` calls introduce massive overhead (from ~0.087s to ~0.002s for 1000 iterations when data is unchanged).
**Action:** Implement delta-based writes by tracking `last_cmd` and only calling `serial.write()` when the command changes, significantly improving loop execution time.

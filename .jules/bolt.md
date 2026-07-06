## 2024-07-06 - Delta-based Serial Writes Optimization
**Learning:** To reduce Serial I/O overhead in control loops, implement delta-based writes by tracking the 'last sent' state. Benchmarking this pattern showed a reduction in loop overhead from ~0.24s to ~0.0004s for 1000 iterations when data is unchanged.
**Action:** Only call `arduino.write()` if the current command string differs from the previous one.

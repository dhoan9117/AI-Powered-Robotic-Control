## 2024-05-24 - Serial I/O Optimization in Control Loops
**Learning:** In fast `while` loops processing video frames, unconditional writes to hardware interfaces (like `arduino.write(cmd)`) create significant performance bottlenecks due to I/O latency, even when the command hasn't changed.
**Action:** Always implement delta-based writes (tracking `last_cmd`) when communicating with hardware in a tight loop to dramatically reduce overhead and improve frame processing rates.

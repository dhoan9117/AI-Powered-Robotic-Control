
## 2024-05-24 - Delta-Based Hardware Writes Optimization
**Learning:** Unconditional writes to hardware (like `arduino.write` via serial) inside a high-frequency computer vision processing loop create significant Serial I/O overhead.
**Action:** Always implement state tracking (e.g., `last_cmd`) to only send delta changes to the serial port, drastically reducing the main loop overhead.

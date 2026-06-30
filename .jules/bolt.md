## 2024-06-30 - Delta-Based Arduino Writes
**Learning:** Writing continuously to a serial port (like Arduino) creates significant I/O bottleneck in the main control loop. Serial communication is slow and blocks the thread.
**Action:** Always implement a state tracker (`last_cmd`) and only write to the serial port when the command has actually changed. This optimization reduces the loop overhead drastically.

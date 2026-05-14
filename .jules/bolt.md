
## 2024-05-18 - Reduce Serial I/O Overload
**Learning:** Writing continuously to the Arduino via `serial.write()` in a high-FPS loop causes significant overhead and can clog the serial buffer.
**Action:** Implementing a simple "last sent command" delta check ensures we only write to the hardware when the command actually changes, saving resources and potentially preventing connection issues.

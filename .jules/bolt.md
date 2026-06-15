## 2024-05-24 - Serial I/O Bottleneck in Vision Loops
**Learning:** In real-time vision pipelines (30+ FPS), blindly sending unchanged position data to hardware via Serial creates a massive I/O bottleneck, as UART writes are significantly slower than CPU operations.
**Action:** Implement delta-based writes by tracking the `last_sent_cmd` state, and only write to the serial port when the command changes and the hardware is confirmed open (`arduino.is_open`).

## 2024-06-14 - Serial I/O Bottleneck in Control Loop
**Learning:** Writing to the Arduino via Serial on every frame, even when the command hasn't changed, creates a massive performance bottleneck. In this codebase, unconditional serial writes add significant I/O overhead to the real-time video processing loop.
**Action:** Implement delta-based writes by tracking the `last_cmd` and only calling `arduino.write()` when the command string changes. Ensure `last_cmd` is only updated when `arduino.is_open` is true and the write succeeds, to prevent state desynchronization.


## 2024-05-18 - Delta-based writes for Serial I/O
**Learning:** Sending redundant command strings to the Arduino hardware using `arduino.write()` blocks the Python main loop and unnecessarily wastes execution time, drastically reducing frame processing rate.
**Action:** When tracking and sending coordinates or hardware instructions inside a loop, implement delta-based serial writes. Track the last sent command with a `last_cmd` variable and only write to the connection if `cmd != last_cmd`.

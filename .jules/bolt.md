## 2024-04-09 - Redundant Serial Writes Clogging the Pipe
**Learning:** In robotics control loops using Python and Arduino, continuously sending identical serial commands on every frame wastes Python CPU cycles in system calls and can overwhelm the Arduino's serial buffer, causing lag.
**Action:** Always cache the last sent state/command and only trigger `serial.write()` when the data payload has actually changed.

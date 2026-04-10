
## 2024-04-10 - Prevented Synchronous Serial I/O Blocking in High-FPS CV Loops
**Learning:** Sending redundant commands over serial connection via `arduino.write()` at high FPS blocks the main Python thread, reducing framerate. This also overloads the Arduino's limited serial buffer, leading to delayed or laggy servo movements.
**Action:** Always cache the last sent command string and compare the current command against it. Only invoke the serial write function when the command state actually changes.

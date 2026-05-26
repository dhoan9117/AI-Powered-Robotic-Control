## 2024-05-26 - Delta-Based Writes Optimize Serial Communication
**Learning:** Writing data to `arduino.write` continuously inside the main vision processing loop in `dieukhien_servo.py` introduces unnecessary overhead if the command has not changed.
**Action:** When working on serial communication within processing loops, track the previous command string and wrap hardware writes in an `if cmd != last_cmd:` check to bypass I/O operations when data is static.

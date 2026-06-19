## 2024-05-24 - Serial I/O Overhead in Control Loops
**Learning:** Writing to the Serial port unconditionally on every loop iteration introduces significant overhead (~0.24s for 1000 iterations).
**Action:** Implement delta-based writes by tracking the 'last sent' state and only calling `arduino.write()` if the command differs, ensuring tracking variables are only updated when the hardware is open.

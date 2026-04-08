import serial
import time
from unittest.mock import Mock

try:
    arduino = serial.Serial(port='loop://', baudrate=115200, timeout=.1)
except:
    arduino = Mock()

start = time.perf_counter()
for _ in range(1000):
    cmd = "90,30,90,90\n"
    arduino.write(cmd.encode())
print(f"Time for 1000 writes: {time.perf_counter() - start:.4f}s")

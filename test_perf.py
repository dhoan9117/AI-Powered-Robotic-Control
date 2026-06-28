import sys
import time

# Create dummy classes to mock dependencies
class DummySerial:
    def __init__(self):
        self.is_open = True
    def write(self, data):
        pass

arduino = DummySerial()
last_cmd = ""

# Simulate loop 10,000 times with no change
start = time.time()
for _ in range(10000):
    cmd = f"90,30,90,90\n"
    if arduino and arduino.is_open:
        arduino.write(cmd.encode())
end_baseline = time.time()

start2 = time.time()
for _ in range(10000):
    cmd = f"90,30,90,90\n"
    if cmd != last_cmd:
        if arduino and arduino.is_open:
            arduino.write(cmd.encode())
            last_cmd = cmd
end_optimized = time.time()

print(f"Baseline (Always Encode/Write): {end_baseline - start:.5f}s")
print(f"Optimized (Delta check): {end_optimized - start2:.5f}s")

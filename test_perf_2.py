import sys
import time

start = time.time()
for _ in range(10000):
    fingers = [1, 1, 0, 0, 1]
    count = fingers.count(1)
end_baseline = time.time()

start2 = time.time()
for _ in range(10000):
    fingers = [1, 1, 0, 0, 1]
    count = sum(fingers)
end_optimized = time.time()

print(f"Count: {end_baseline - start:.5f}s")
print(f"Sum: {end_optimized - start2:.5f}s")

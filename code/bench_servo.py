import mediapipe as mp
import time
import numpy as np

mp_pose = mp.solutions.pose
pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5, model_complexity=1)

image = np.random.randint(0, 255, (1080, 1920, 3), dtype=np.uint8)

def bench(writeable):
    for _ in range(5):
        img = image.copy()
        img.flags.writeable = writeable
        pose.process(img)

    start = time.perf_counter()
    for _ in range(100):
        img = image.copy()
        img.flags.writeable = writeable
        pose.process(img)
    return time.perf_counter() - start

print(f"With writeable=False: {bench(False):.4f}s")
print(f"With writeable=True : {bench(True):.4f}s")

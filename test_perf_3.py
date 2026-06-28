import time
import mediapipe as mp
import cv2
import numpy as np

mp_pose = mp.solutions.pose
pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5, model_complexity=1)

image = np.zeros((480, 640, 3), dtype=np.uint8)

start = time.time()
for _ in range(50):
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    pose.process(image_rgb)
end_baseline = time.time()

start2 = time.time()
for _ in range(50):
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image_rgb.flags.writeable = False # prevent copy
    pose.process(image_rgb)
    image_rgb.flags.writeable = True
end_optimized = time.time()

print(f"Normal: {end_baseline - start:.5f}s")
print(f"No-copy: {end_optimized - start2:.5f}s")

import cv2
import mediapipe as mp
import time
import numpy as np

mp_pose = mp.solutions.pose
pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5, model_complexity=1)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7, min_tracking_confidence=0.5)

image = np.random.randint(0, 255, (480, 640, 3), dtype=np.uint8)

# Warmup
pose.process(image)
hands.process(image)

# Without writeable = False
start = time.time()
for _ in range(100):
    pose.process(image)
    hands.process(image)
time_with_copy = time.time() - start

# With writeable = False
image.flags.writeable = False
start = time.time()
for _ in range(100):
    pose.process(image)
    hands.process(image)
time_without_copy = time.time() - start

print(f"Time with copy: {time_with_copy:.4f}s")
print(f"Time without copy: {time_without_copy:.4f}s")

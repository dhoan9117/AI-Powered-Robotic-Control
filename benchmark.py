import cv2
import mediapipe as mp
import time

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)

cap = cv2.VideoCapture(0)

# warmup
for _ in range(5):
    ret, img = cap.read()
    if not ret: continue
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    hands.process(img_rgb)

# without writeable = False
start = time.time()
for _ in range(100):
    ret, img = cap.read()
    if not ret: continue
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    hands.process(img_rgb)
print("Without:", time.time() - start)

# with writeable = False
start = time.time()
for _ in range(100):
    ret, img = cap.read()
    if not ret: continue
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_rgb.flags.writeable = False
    hands.process(img_rgb)
print("With:", time.time() - start)

cap.release()
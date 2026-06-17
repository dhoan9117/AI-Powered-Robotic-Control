import sys
from unittest.mock import MagicMock

sys.modules['cv2'] = MagicMock()
sys.modules['mediapipe'] = MagicMock()
sys.modules['serial'] = MagicMock()
sys.modules['cvzone'] = MagicMock()
sys.modules['cvzone.HandTrackingModule'] = MagicMock()

# Mocking the VideoCapture
sys.modules['cv2'].VideoCapture.return_value.isOpened.side_effect = [True] * 20 + [False]
sys.modules['cv2'].VideoCapture.return_value.read.return_value = (True, MagicMock())

# Mock the model results
mock_pose = MagicMock()
mock_pose.pose_landmarks.landmark = [MagicMock()] * 33
for lm in mock_pose.pose_landmarks.landmark:
    lm.visibility = 0.6
    lm.x = 0.5
    lm.y = 0.5
sys.modules['mediapipe'].solutions.pose.Pose.return_value.process.return_value = mock_pose

mock_hand = MagicMock()
mock_hand.multi_hand_landmarks = [MagicMock()]
mock_hand.multi_hand_landmarks[0].landmark = [MagicMock()] * 21
for i, lm in enumerate(mock_hand.multi_hand_landmarks[0].landmark):
    lm.x = 0.5
    lm.y = 0.5
sys.modules['mediapipe'].solutions.hands.Hands.return_value.process.return_value = mock_hand

import dieukhien_servo

print("Call count write:", sys.modules['serial'].Serial.return_value.write.call_count)

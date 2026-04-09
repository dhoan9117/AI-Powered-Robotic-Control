import cv2
import mediapipe as mp
import serial
import time
import math

# --- KẾT NỐI ARDUINO ---
try:
    arduino = serial.Serial(port='COM5', baudrate=115200, timeout=.1)
    print("✅ Đã kết nối Arduino - Chế độ 2 SOLUTION SONG SONG!")
except:
    print("❌ Lỗi COM! Chạy giả lập.")
    arduino = None

# --- KHỞI TẠO 2 MODEL RIÊNG BIỆT ---
mp_drawing = mp.solutions.drawing_utils
# 1. POSE (Dáng người) - Lấy nét toàn thân
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5,
    model_complexity=1
)

# 2. HANDS (Bàn tay) - Lấy nét chi tiết
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.5
)

cap = cv2.VideoCapture(0)


# --- BỘ LỌC LÀM MƯỢT ---
class Smoother:
    def __init__(self, alpha=0.15):
        self.alpha = alpha
        self.val = 90

    def update(self, new_val):
        self.val = self.alpha * new_val + (1 - self.alpha) * self.val
        return int(self.val)


# Tạo 4 bộ lọc
smooth_base = Smoother(0.15)
smooth_arm = Smoother(0.15)
smooth_wrist = Smoother(0.2)
smooth_gripper = Smoother(0.5)


def map_range(x, in_min, in_max, out_min, out_max):
    val = (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
    return int(max(0, min(180, val)))


# Biến lưu trạng thái cuối
last_base = 90
last_arm = 90
last_wrist = 90
last_gripper = 30
last_cmd = ""

while cap.isOpened():
    success, image = cap.read()
    if not success: continue

    # Xử lý ảnh
    image = cv2.flip(image, 1)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # =========================================================
    # 1. CHẠY MODEL POSE (Dáng) -> Điều khiển BASE (3) & ARM (6)
    # =========================================================
    pose_results = pose.process(image_rgb)

    current_base = last_base
    current_arm = last_arm

    if pose_results.pose_landmarks:
        # Vẽ Skeleton Pose (Màu đỏ)
        mp_drawing.draw_landmarks(
            image, pose_results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
            landmark_drawing_spec=mp_drawing.DrawingSpec(color=(0, 0, 255), thickness=2, circle_radius=2)
        )

        # Lấy Landmark 16 (Cổ tay Phải)
        wrist = pose_results.pose_landmarks.landmark[16]

        if wrist.visibility > 0.5:
            # Base (X)
            raw_base = map_range(wrist.x, 0.2, 0.8, 180, 0)
            current_base = smooth_base.update(raw_base)

            # Arm (Y)
            raw_arm = map_range(wrist.y, 0.2, 0.8, 160, 20)
            current_arm = smooth_arm.update(raw_arm)

            last_base = current_base
            last_arm = current_arm

    # =========================================================
    # 2. CHẠY MODEL HANDS (Tay) -> Điều khiển GRIP (5) & WRIST (9)
    # =========================================================
    hand_results = hands.process(image_rgb)

    current_gripper = last_gripper
    current_wrist = last_wrist

    if hand_results.multi_hand_landmarks:
        for hand_lm in hand_results.multi_hand_landmarks:
            # Vẽ Skeleton Hands (Màu xanh)
            mp_drawing.draw_landmarks(
                image, hand_lm, mp_hands.HAND_CONNECTIONS,
                landmark_drawing_spec=mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=2)
            )

            # --- QUAN TRỌNG: SỬA LỖI Ở ĐÂY ---
            # Truy cập vào thuộc tính .landmark để lấy danh sách điểm
            lm = hand_lm.landmark

            # --- A. XỬ LÝ KẸP (Đếm ngón) ---
            fingers = []
            # Ngón cái (X) - Dùng biến lm thay vì hand_lm
            if lm[4].x > lm[3].x:
                fingers.append(1)
            else:
                fingers.append(0)
            # 4 ngón kia (Y)
            for id in [8, 12, 16, 20]:
                if lm[id].y < lm[id - 2].y:
                    fingers.append(1)
                else:
                    fingers.append(0)

            count = fingers.count(1)

            if count <= 1:
                raw_gripper = 110  # ĐÓNG
                cv2.putText(image, "NAM -> KEP", (10, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            elif count >= 4:
                raw_gripper = 30  # MỞ
                cv2.putText(image, "XOE -> MO", (10, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            else:
                raw_gripper = last_gripper

            current_gripper = smooth_gripper.update(raw_gripper)
            last_gripper = current_gripper

            # --- B. XỬ LÝ CỔ TAY (Tilt) ---
            # So sánh độ cao Cổ tay (0) và Khớp ngón giữa (9)
            tilt = lm[0].y - lm[9].y

            if abs(tilt) < 0.04:  # Vùng chết
                raw_wrist = 90
            else:
                raw_wrist = map_range(tilt, -0.2, 0.2, 0, 180)

            current_wrist = smooth_wrist.update(raw_wrist)
            last_wrist = current_wrist

    # =========================================================
    # 3. GỬI DỮ LIỆU
    # =========================================================
    cmd = f"{current_base},{current_gripper},{current_arm},{current_wrist}\n"
    if arduino and arduino.is_open and cmd != last_cmd:
        arduino.write(cmd.encode())
        last_cmd = cmd

    # Hiển thị
    info1 = f"Base(3): {current_base} | Arm(6): {current_arm}"
    info2 = f"Grip(5): {current_gripper} | Wrist(9): {current_wrist}"
    cv2.putText(image, info1, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 2)
    cv2.putText(image, info2, (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 2)

    cv2.imshow('PARALLEL CONTROL (Fixed)', image)
    if cv2.waitKey(1) & 0xFF == 27: break

cap.release()
cv2.destroyAllWindows()
if arduino: arduino.close()
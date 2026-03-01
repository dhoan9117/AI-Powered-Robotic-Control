import cv2
from cvzone.HandTrackingModule import HandDetector
import serial
import time

# --- 1. KHỞI TẠO ARDUINO & CAMERA ---
try:
    # COM5 theo hệ thống của bạn
    arduino = serial.Serial(port='COM5', baudrate=9600, timeout=.1)
    time.sleep(2)
    print("Arduino Connected!")
except:
    print("Please check COM5 port")

cap = cv2.VideoCapture(0)  # Đã định nghĩa biến cap để tránh NameError

# --- 2. KHỞI TẠO DETECTOR CỦA CVZONE ---
# detectionCon: Độ tin cậy nhận diện (0.8 để cực kỳ chắc chắn mới nhận)
# maxHands: Chỉ nhận 1 tay để tăng tốc độ xử lý
detector = HandDetector(detectionCon=0.8, maxHands=1)

last_data = ""

while True:
    success, img = cap.read()
    if not success: break

    img = cv2.flip(img, 1)

    # Tìm tay và vẽ khung xương
    hands, img = detector.findHands(img)

    if hands:
        hand = hands[0]  # Lấy thông tin bàn tay đầu tiên

        # CHÌA KHÓA: Hàm fingersUp() của CVZone xử lý chiều sâu cực tốt
        # Nó trả về mảng [1, 1, 1, 1, 1] tương ứng 5 ngón
        fingers = detector.fingersUp(hand)

        # Chuyển mảng [1, 0, 0, 0, 0] thành chuỗi "10000"
        current_data = "".join(map(str, fingers))

        # Gửi dữ liệu khi có thay đổi
        if current_data != last_data:
            arduino.write(f"{current_data}\n".encode())
            print(f"Sent: {current_data}")
            last_data = current_data

        # Hiển thị trạng thái lên màn hình
        cv2.putText(img, f'Fingers: {current_data}', (10, 70),
                    cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)

    cv2.imshow("CVZone Hand Tracking", img)

    # Thoát khi nhấn 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
arduino.close()  # Giải phóng cổng COM
cv2.destroyAllWindows()
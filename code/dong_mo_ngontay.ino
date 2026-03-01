int ledPins[] = {3, 5, 6, 9, 10}; // Chân PWM chuẩn

void setup() {
  Serial.begin(9600);
  for(int i = 0; i < 5; i++) {
    pinMode(ledPins[i], OUTPUT);
    digitalWrite(ledPins[i], LOW); // Lúc mới bật phải TẮT hết
  }
}

void loop() {
  if (Serial.available() > 0) {
    // Đọc gói tin từ Python gửi qua
    String data = Serial.readStringUntil('\n'); 
    data.trim(); // Xóa bỏ khoảng trắng thừa nếu có

    // Chỉ xử lý nếu nhận đủ 5 ký tự (ví dụ "10101")
    if (data.length() == 5) {
      for (int i = 0; i < 5; i++) {
        if (data[i] == '1') {
          digitalWrite(ledPins[i], HIGH); // Ngón tay mở -> Sáng
        } else {
          digitalWrite(ledPins[i], LOW);  // Ngón tay đóng -> Tắt
        }
      }
    }
  }
}
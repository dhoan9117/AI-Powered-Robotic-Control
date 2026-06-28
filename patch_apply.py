import sys

with open("code/dieukhien_servo.py", "rb") as f:
    content = f.read()

search1 = b"last_gripper = 30\r\n\r\nwhile cap.isOpened():"
replace1 = b"last_gripper = 30\r\nlast_cmd = \"\"\r\n\r\nwhile cap.isOpened():"

search2 = b"    if arduino and arduino.is_open:\r\n        arduino.write(cmd.encode())"
replace2 = b"    if arduino and arduino.is_open:\r\n        # \xe2\x9a\xa1 OPTIMIZATION: Only send data to serial if command has changed\r\n        # Reduces loop overhead and prevents Arduino buffer overflow\r\n        if cmd != last_cmd:\r\n            arduino.write(cmd.encode())\r\n            last_cmd = cmd"

if search1 in content and search2 in content:
    print("Both blocks found!")
else:
    print("Blocks not found!")

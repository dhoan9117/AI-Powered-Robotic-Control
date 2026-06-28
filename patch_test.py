import sys

with open("code/dieukhien_servo.py", "rb") as f:
    content = f.read()

search1 = b"last_gripper = 30\r\n\r\nwhile cap.isOpened():"
search2 = b"    if arduino and arduino.is_open:\r\n        arduino.write(cmd.encode())"

if search1 in content and search2 in content:
    print("Matches found!")
else:
    print("Not found.")

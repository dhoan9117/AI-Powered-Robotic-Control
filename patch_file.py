import sys

with open("code/dieukhien_servo.py", "rb") as f:
    content = f.read()

search = b"""    # =========================================================\r
    # 3. G\xe1\xbb\xacI D\xe1\xbb\xae LI\xe1\xbb\x86U\r
    # =========================================================\r
    cmd = f"{current_base},{current_gripper},{current_arm},{current_wrist}\\n"\r
    if arduino and arduino.is_open:\r
        arduino.write(cmd.encode())\r"""

if search in content:
    print("Found search block.")
else:
    print("Search block NOT found, printing nearby context to check encoding:")
    import re
    # Look for the section title "3. GỬI DỮ LIỆU" using ascii to avoid encoding issues
    idx = content.find(b"3.")
    if idx != -1:
        print(content[idx-50:idx+200])

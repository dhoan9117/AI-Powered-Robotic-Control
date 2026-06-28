import sys

with open("code/dieukhien_servo.py", "rb") as f:
    content = f.read()

search = b"""    # X\xe1\xbb\xad l\xc3\xbd \xe1\xba\xa3nh\r
    image = cv2.flip(image, 1)\r
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)\r
\r
    # =========================================================\r
    # 1. CH\xe1\xba\xa0Y MODEL POSE (D\xc3\xa1ng) -> \xc4\x90i\xe1\xbb\x81u khi\xe1\xbb\x83n BASE (3) & ARM (6)\r
    # =========================================================\r
    pose_results = pose.process(image_rgb)\r"""

if search in content:
    print("Found search block 2.")
else:
    print("Search block 2 NOT found, printing context:")
    idx = content.find(b"image = cv2.flip(image, 1)")
    print(content[idx:idx+250])

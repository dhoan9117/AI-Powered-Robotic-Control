## 2024-05-24 - MediaPipe Memory Optimization via Writeable Flag
**Learning:** When passing OpenCV arrays into MediaPipe models (like `pose.process` or `hands.process`), MediaPipe copies the image data internally by default.
**Action:** Always set `image.flags.writeable = False` before processing to allow MediaPipe to process the array by reference, significantly reducing memory reallocation in tight, real-time computer vision loops. Remember to set it back to `True` if you need to draw on the image afterwards.

## 2024-04-24 - MediaPipe Memory Allocation Overhead
**Learning:** MediaPipe's `.process()` method internally copies the image array if the array is writeable. In a real-time computer vision loop, this memory allocation overhead for every frame slows down inference.
**Action:** Always set `image.flags.writeable = False` before calling `pose.process()` or `hands.process()` to allow pass-by-reference. Remember to set it back to `True` if you need to modify the image array afterwards.

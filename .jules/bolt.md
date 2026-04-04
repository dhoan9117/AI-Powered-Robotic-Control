## 2024-04-04 - Prevent MediaPipe Image Buffer Copying
**Learning:** MediaPipe's `process()` method creates an internal copy of the image buffer by default. When running multiple MediaPipe models (like Pose and Hands in `dieukhien_servo.py`) on the same frame, this causes unnecessary repeated memory allocations and CPU overhead.
**Action:** Always set `image.flags.writeable = False` on the numpy array before passing it to MediaPipe to pass it by reference and skip the internal data copy.

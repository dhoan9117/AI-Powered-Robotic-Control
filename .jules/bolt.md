## 2025-02-18 - MediaPipe Frame Copy Overhead
**Learning:** By default, MediaPipe's `process()` method creates a deep copy of the input NumPy array if it is writeable to prevent concurrent modifications. When running multiple models (e.g., Pose and Hands) sequentially on the same frame, this causes multiple unnecessary full-frame copies per frame, degrading FPS.
**Action:** Always set `image.flags.writeable = False` after color conversion and before passing frames to MediaPipe `process()` methods.

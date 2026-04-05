## 2024-05-24 - MediaPipe Memory Copy Bottleneck
**Learning:** By default, MediaPipe copies the input numpy array during processing. When running multiple models (like Pose and Hands sequentially), this causes redundant memory allocations and array copies, increasing CPU load and dropping FPS.
**Action:** Always set `image.flags.writeable = False` before passing frames to MediaPipe `process()` to enable pass-by-reference and skip the array copy.

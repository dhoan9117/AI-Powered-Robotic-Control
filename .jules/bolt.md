# Bolt's Performance Journal

## 2026-04-18 - MediaPipe Zero-Copy & Allocation Avoidance

**Learning:** MediaPipe's Python API defaults to making memory copies of image tensors when `writeable = True` (the default for numpy arrays in OpenCV). Setting `image.flags.writeable = False` allows underlying C++ code to process by reference. Also, Python list allocations (`[]`) inside inner real-time loops create significant GC pressure; a raw integer counter `+= 1` is significantly faster.
**Action:** When writing or modifying real-time vision loops with MediaPipe, always pass a read-only numpy array to the `process()` function, and avoid `list.append` followed by `count()` inside `while cap.isOpened()` loops.

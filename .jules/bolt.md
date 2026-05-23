## 2024-05-19 - Serial I/O Blocking Overhead
**Learning:** In the computer vision loop, blindly calling `arduino.write(cmd)` every frame blocks execution and creates massive latency, especially when the hand hasn't moved.
**Action:** Implement a command delta cache (`last_cmd`). Only trigger the blocking I/O operation if the computed angle string actually changes. This dramatically improves frame rates by bypassing slow serial transmission for stationary states.

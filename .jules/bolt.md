
## 2024-05-19 - Serial Optimization Learnings
**Learning:** In tight control loops like gesture tracking, redundant serial writes to Arduino cause significant overhead even when data hasn't changed.
**Action:** Always implement delta-based writes (caching and comparing the last sent command string) to only communicate with hardware when state actually changes. Ensure tracking variables (like `last_cmd`) are only updated when the hardware is available (`is_open`) and the write succeeds, to avoid state desync.

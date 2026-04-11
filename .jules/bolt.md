## 2024-05-24 - Optimization execution and pycache handling
**Learning:** Running `python -m py_compile script.py` creates a compiled `.pyc` artifact in the `__pycache__` directory.
**Action:** When validating syntax with `py_compile`, ensure `__pycache__` is cleaned up afterwards or set `PYTHONDONTWRITEBYTECODE=1` to avoid leaving auto-generated files in the repository.

## 2024-05-24 - File Artifacts during Testing
**Learning:** Running `python3 -m py_compile` generates `__pycache__` directories containing `.pyc` files, which are binary build artifacts that should not be committed to source control as they bloat the repository and cause merge conflicts.
**Action:** Always clean up generated files like `__pycache__` directories after testing Python syntax (e.g., `rm -rf code/__pycache__`) or ensure they are properly ignored by Git before submitting code changes.

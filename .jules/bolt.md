## 2024-05-24 - Line endings and encoding in git merge diffs
**Learning:** `replace_with_git_merge_diff` can fail if line endings (CRLF vs LF) or encoding (UTF-8 with Vietnamese chars) do not match exactly with what is expected, making python string replacements a more robust fallback. Also, overwriting files using `\n` while original was `\r\n` creates a noisy git diff where every line appears modified.
**Action:** Use regex based replacements with line ending detection in Python to perform exact replacements that don't corrupt the rest of the file.

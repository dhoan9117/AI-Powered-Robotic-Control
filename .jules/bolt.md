## 2024-05-10 - Bytes Literacy with CRLF/Vietnamese Characters
**Learning:** When using Python replacement scripts (`open(f, 'rb')`) to modify files containing non-ASCII characters (like Vietnamese text or emojis) and CRLF line endings, Python byte literals (`b"..."`) fail with a SyntaxError if they contain non-ASCII characters.
**Action:** Define strings containing non-ASCII characters as standard strings (e.g., `replace = "string with ⚡"`) and convert them to bytes explicitly using `.encode('utf-8')` before performing byte-level search and replace operations in binary file mode.

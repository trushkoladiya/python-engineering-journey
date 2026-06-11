# Text vs Binary Files

Files are either **text** or **binary**. Understanding the difference is important.

## Text Files

- Contain human-readable characters
- Python decodes bytes to strings using an **encoding** (default: UTF-8)
- Examples: `.txt`, `.csv`, `.py`, `.json`

```python
with open("data.txt", "r", encoding="utf-8") as file:
    text = file.read()   # Returns a string
```

## Binary Files

- Contain raw bytes (not human-readable)
- Python reads/writes bytes objects (`b"..."`)
- Examples: images, audio, videos, executables

```python
with open("image.png", "rb") as file:
    data = file.read()   # Returns bytes, not string
```

## Encoding

Text files use **encoding** to convert between bytes and characters:
- **UTF-8** — most common, supports all languages
- **ASCII** — English only, 128 characters

```python
with open("data.txt", "w", encoding="utf-8") as file:
    file.write("Hello! 🐍")
```

## Key Points

- Text mode (`'r'`, `'w'`): works with strings, uses encoding
- Binary mode (`'rb'`, `'wb'`): works with raw bytes
- Always specify `encoding="utf-8"` for text files with special characters
- Use binary mode for images, audio, and other non-text files

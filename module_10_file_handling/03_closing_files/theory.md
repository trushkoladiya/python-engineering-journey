# Closing Files

Closing a file is essential — it saves data and frees resources.

## Manual Closing

```python
file = open("data.txt", "r")
content = file.read()
file.close()   # Always close when done!
```

If you forget to close, data might not be saved, and system resources stay locked.

## The `with` Statement (Recommended)

The `with` statement **automatically** closes the file when the block ends:

```python
with open("data.txt", "r") as file:
    content = file.read()
# File is automatically closed here — even if an error occurs!
```

This is the **preferred** way to work with files.

## Why `with` is Better

- Closes the file automatically
- Works even if an error occurs inside the block
- Cleaner and shorter code

## Key Points

- Always close files after use
- Use `with open(...) as file:` — it's safer and cleaner
- The `with` statement handles closing automatically
- From now on, we'll use `with` for all file operations

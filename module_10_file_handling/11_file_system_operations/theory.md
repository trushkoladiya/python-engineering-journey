# File System Operations

Python's `os` and `os.path` modules let you interact with the file system.

## Checking File Existence

```python
import os

os.path.exists("data.txt")     # True/False
os.path.isfile("data.txt")     # Is it a file?
os.path.isdir("my_folder")     # Is it a directory?
```

## File Information

```python
os.path.getsize("data.txt")    # Size in bytes
os.path.getmtime("data.txt")   # Last modified time
```

## Deleting Files

```python
os.remove("data.txt")          # Delete a file
```

## Creating Directories

```python
os.makedirs("path/to/folder", exist_ok=True)
```

## Listing Directory Contents

```python
files = os.listdir(".")        # List current directory
```

## Key Points

- Use `os.path.exists()` before accessing files
- `os.remove()` deletes files permanently (no recycle bin!)
- `os.makedirs()` creates directories including parents
- Always check existence before deleting

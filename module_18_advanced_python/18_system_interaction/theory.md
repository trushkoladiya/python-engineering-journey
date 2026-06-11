# System Interaction

## Working with the Operating System

Python's `os`, `subprocess`, and `shutil` modules let you interact with the operating system — managing files, directories, and running external commands.

## os Module — File System Operations

```python
import os

# Current directory
print(os.getcwd())

# List directory contents
print(os.listdir('.'))

# File info
print(os.path.exists('file.txt'))
print(os.path.getsize('file.txt'))
print(os.path.isfile('file.txt'))
print(os.path.isdir('folder'))
```

## os.path — Path Manipulation

```python
import os.path

# Join paths (OS-independent)
path = os.path.join('data', 'users', 'file.txt')

# Split path components
directory = os.path.dirname(path)
filename = os.path.basename(path)
name, ext = os.path.splitext(filename)
```

## shutil — High-Level File Operations

```python
import shutil

shutil.copy('src.txt', 'dst.txt')       # Copy file
shutil.copytree('src_dir', 'dst_dir')   # Copy directory
shutil.move('old.txt', 'new.txt')       # Move/rename
shutil.rmtree('directory')               # Delete directory
```

## subprocess — Running External Commands

```python
import subprocess

result = subprocess.run(['ls', '-la'], capture_output=True, text=True)
print(result.stdout)
print(result.returncode)  # 0 means success
```

## pathlib — Modern Path Handling

```python
from pathlib import Path

p = Path('data') / 'users' / 'file.txt'
print(p.exists())
print(p.suffix)     # .txt
print(p.stem)       # file
print(p.parent)     # data/users
```

## Key Points

- Use `os.path` or `pathlib` for cross-platform path handling
- Use `shutil` for file copying, moving, and deletion
- Use `subprocess.run()` to execute external commands safely
- **Never** use `os.system()` — use `subprocess` instead (safer)
- Use `pathlib.Path` for modern, readable path operations

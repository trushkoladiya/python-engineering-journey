# File Basics

A **file** is data stored permanently on your computer's disk. Unlike variables (which disappear when the program ends), files persist.

## File vs Memory

| Feature | Variable (Memory) | File (Disk) |
|---------|-------------------|-------------|
| Lifetime | While program runs | Permanent |
| Speed | Very fast | Slower |
| Size | Limited by RAM | Limited by disk |
| Access | Direct | Through open/read/write |

## File Paths

A **path** tells Python where to find a file.

### Relative Paths
Relative to the current working directory:

```python
"data.txt"              # Same folder
"folder/data.txt"       # Inside a subfolder
"../data.txt"           # Parent folder
```

### Absolute Paths
The full path from the root:

```python
"/home/user/projects/data.txt"     # Linux/Mac
"C:/Users/user/projects/data.txt"  # Windows
```

## Common File Types

- `.txt` — plain text
- `.csv` — comma-separated values
- `.json` — structured data
- `.log` — log files
- `.py` — Python source code

## Key Points

- Files store data permanently on disk
- Variables are temporary; files are persistent
- Use relative paths for portability
- Use absolute paths when the exact location matters

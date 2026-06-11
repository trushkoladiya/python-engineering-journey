# Exception Handling with Files

File operations can fail for many reasons. Using `try/except` makes your code robust.

## Common File Errors

| Error | Cause |
|-------|-------|
| `FileNotFoundError` | File doesn't exist (read mode) |
| `PermissionError` | No permission to access file |
| `IsADirectoryError` | Trying to open a directory as a file |
| `UnicodeDecodeError` | Wrong encoding |

## Safe File Handling Pattern

```python
try:
    with open("data.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found!")
except PermissionError:
    print("No permission!")
```

## The `with` Statement Already Helps

`with` ensures the file is closed even if an error occurs inside the block. Combining `with` + `try/except` gives you full safety.

## Key Points

- Always handle `FileNotFoundError` when reading files
- Use `try/except` around file operations
- The `with` statement ensures cleanup even on errors
- Provide helpful error messages to the user

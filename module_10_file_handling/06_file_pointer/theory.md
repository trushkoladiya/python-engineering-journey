# File Pointer Control

The file pointer tracks your **current position** in the file.

## `tell()` — Where Am I?

Returns the current position (in bytes) from the start:

```python
with open("data.txt", "r") as file:
    print(file.tell())      # 0 (start)
    file.read(5)
    print(file.tell())      # 5 (after reading 5 chars)
```

## `seek()` — Move the Pointer

Moves the pointer to a specific position:

```python
with open("data.txt", "r") as file:
    file.read()              # Read everything (pointer at end)
    file.seek(0)             # Move back to start
    content = file.read()    # Read again from start
```

## Key Points

- `tell()` returns the current byte position
- `seek(0)` moves to the beginning
- `seek(n)` moves to byte position n
- Useful when you need to re-read or skip parts of a file

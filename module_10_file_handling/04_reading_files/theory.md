# Reading Files

Python provides multiple methods to read file content.

## `read()` — Read Everything

```python
with open("data.txt", "r") as file:
    content = file.read()   # Entire file as one string
```

## `readline()` — Read One Line

```python
with open("data.txt", "r") as file:
    line1 = file.readline()   # First line
    line2 = file.readline()   # Second line
```

## `readlines()` — Read All Lines as a List

```python
with open("data.txt", "r") as file:
    lines = file.readlines()   # List of lines
    # ['Line 1\n', 'Line 2\n', 'Line 3\n']
```

## Iterating Line by Line (Best Way)

```python
with open("data.txt", "r") as file:
    for line in file:
        print(line.strip())
```

This is memory-efficient — reads one line at a time.

## File Pointer

After reading, the pointer moves to where you stopped. Reading again returns nothing unless you reset the pointer.

## Key Points

- `read()` — whole file as one string
- `readline()` — one line at a time
- `readlines()` — all lines as a list
- `for line in file:` — best for large files (memory-efficient)
- Use `.strip()` to remove trailing newlines

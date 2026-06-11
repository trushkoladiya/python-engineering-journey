# Performance & Best Practices

Efficient file handling matters when working with large files.

## Efficient Reading

### Line-by-Line Iteration (Best for Large Files)
```python
with open("large.txt", "r") as file:
    for line in file:       # Reads one line at a time
        process(line)
```

### Chunk Reading
```python
with open("huge.txt", "r") as file:
    while True:
        chunk = file.read(4096)   # Read 4KB at a time
        if not chunk:
            break
        process(chunk)
```

## Safe Writing

### Write to Temp, Then Rename
```python
# Don't write directly — if it fails, you lose data!
# Instead: write to temp → rename
with open("data.tmp", "w") as file:
    file.write(new_content)
os.rename("data.tmp", "data.txt")
```

## Key Points

- Never read huge files entirely into memory — use line-by-line or chunks
- `for line in file:` is memory-efficient
- Write to a temp file first, then rename — prevents data loss
- Always use `with` for automatic cleanup
- Flush data with `file.flush()` for critical writes

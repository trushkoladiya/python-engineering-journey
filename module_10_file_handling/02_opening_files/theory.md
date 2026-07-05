# Opening Files

The `open()` function is how Python accesses files.

## The `open()` Function

```python
file = open("filename.txt", "mode")
```

- First argument: the file path
- Second argument: the mode (how to access it)

## File Modes

| Mode | Description | Creates file? | Erases content? |
|------|-------------|---------------|-----------------|
| `'r'` | Read (default) | ❌ | ❌ |
| `'w'` | Write | ✅ | ✅ |
| `'a'` | Append | ✅ | ❌ |
| `'x'` | Exclusive create | ✅ (fails if exists) | N/A |
| `'rb'` | Read binary | ❌ | ❌ |
| `'wb'` | Write binary | ✅ | ✅ |

## Important Rules

- `'r'` — file must already exist, or you get `FileNotFoundError`
- `'w'` — creates the file if it doesn't exist; **erases** content if it does
- `'a'` — creates the file if it doesn't exist; **adds** to the end
- `'x'` — fails if the file already exists

## Key Points

- Always specify the mode explicitly for clarity
- `'r'` is the default mode if you omit it
- Be careful with `'w'` — it erases existing content!
- Always close files when done (or use `with`)

# Writing to Files

Writing lets you save data permanently to disk.

## `write()` — Write a String

```python
with open("output.txt", "w") as file:
    file.write("Hello, World!\n")
```

Note: `write()` does **not** add a newline automatically — you must include `\n`.

## `writelines()` — Write a List of Strings

```python
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open("output.txt", "w") as file:
    file.writelines(lines)
```

`writelines()` does not add newlines — include them in each string.

## Overwriting vs Appending

- `'w'` mode: **overwrites** — erases existing content
- `'a'` mode: **appends** — adds to the end

```python
# Overwrite
with open("data.txt", "w") as file:
    file.write("New content\n")

# Append
with open("data.txt", "a") as file:
    file.write("More content\n")
```

## Key Points

- `write()` writes a single string
- `writelines()` writes a list of strings
- Neither adds `\n` automatically
- Use `'w'` to overwrite, `'a'` to append
- Use `print()` with `file=` parameter for convenience

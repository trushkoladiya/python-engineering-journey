# File Modes Deep Behavior

Beyond basic modes, Python supports combined read/write modes.

## Combined Modes

| Mode | Read? | Write? | Creates? | Erases? | Pointer |
|------|-------|--------|----------|---------|---------|
| `'r+'` | ✅ | ✅ | ❌ | ❌ | Start |
| `'w+'` | ✅ | ✅ | ✅ | ✅ | Start |
| `'a+'` | ✅ | ✅ | ✅ | ❌ | End |

## `r+` — Read and Write

File must exist. Pointer starts at the beginning:

```python
with open("data.txt", "r+") as file:
    content = file.read()     # Read first
    file.write("new data")    # Then write (appends at pointer)
```

## `w+` — Write and Read

Creates or erases the file. Can read after writing:

```python
with open("data.txt", "w+") as file:
    file.write("Hello!\n")
    file.seek(0)              # Go back to read
    print(file.read())
```

## `a+` — Append and Read

Pointer starts at the end. Must seek(0) to read:

```python
with open("data.txt", "a+") as file:
    file.write("Appended\n")
    file.seek(0)
    print(file.read())
```

## Key Points

- `+` adds the opposite capability (read↔write)
- `r+`: must exist, preserves content
- `w+`: creates/erases, then allows reading
- `a+`: creates/preserves, writes at end, can read from any position

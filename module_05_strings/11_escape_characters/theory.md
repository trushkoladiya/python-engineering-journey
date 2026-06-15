# Escape Characters

Escape characters let you include **special characters** in strings that you can't type directly.

## Common Escape Characters

| Escape | Meaning |
|--------|---------|
| `\n` | New line |
| `\t` | Tab |
| `\\` | Backslash |
| `\'` | Single quote |
| `\"` | Double quote |

## New Line (`\n`)

```python
print("Hello\nWorld")
# Output:
# Hello
# World
```

## Tab (`\t`)

```python
print("Name\tAge\tCity")
print("Trush\t21\tAhmedabad")
# Output:
# Name    Age     City
# Trush   21      Ahmedabad
```

## Backslash (`\\`)

```python
print("C:\\Users\\Trush\\Documents")
# Output: C:\Users\Trush\Documents
```

## Quotes Inside Strings

```python
print("She said \"Hello\"")    # She said "Hello"
print('It\'s a great day')     # It's a great day
```

## Raw Strings (`r""`)

A raw string treats backslashes as **literal characters** — no escaping:

```python
print(r"C:\Users\Trush\new_folder")
# Output: C:\Users\Trush\new_folder

print(r"\n is a newline character")
# Output: \n is a newline character
```

## Key Points

- `\n` creates a new line, `\t` creates a tab
- `\\` is needed to print a literal backslash
- `\'` and `\"` for quotes inside strings
- Raw strings (`r"..."`) disable escape processing

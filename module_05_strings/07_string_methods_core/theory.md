# String Methods (Core)

String methods are built-in operations you call **on** a string using dot notation: `string.method()`.

## Case Methods

Change the case (uppercase/lowercase) of a string:

```python
text = "Hello World"
print(text.lower())       # hello world
print(text.upper())       # HELLO WORLD
print(text.title())       # Hello World
print(text.capitalize())  # Hello world
```

- `lower()` — all lowercase
- `upper()` — all uppercase
- `title()` — capitalize first letter of each word
- `capitalize()` — capitalize only the first letter

## Trimming Methods

Remove whitespace (spaces, tabs, newlines) from the edges:

```python
text = "   Hello World   "
print(text.strip())    # "Hello World"   — both sides
print(text.lstrip())   # "Hello World   " — left side only
print(text.rstrip())   # "   Hello World" — right side only
```

## Searching Methods

Find the position of a substring:

```python
text = "Hello World"
print(text.find("World"))    # 6  — index where "World" starts
print(text.find("Python"))   # -1 — not found
print(text.rfind("l"))       # 9  — last occurrence of "l"
```

- `find()` returns `-1` if not found
- `index()` raises an error if not found (use with caution)

## Counting

Count how many times a substring appears:

```python
text = "banana"
print(text.count("a"))    # 3
print(text.count("na"))   # 2
print(text.count("x"))    # 0
```

## Key Points

- String methods return **new** strings (remember: strings are immutable)
- `lower()`, `upper()`, `title()`, `capitalize()` for case changes
- `strip()`, `lstrip()`, `rstrip()` to remove whitespace
- `find()` and `rfind()` to search (return -1 if not found)
- `count()` to count occurrences

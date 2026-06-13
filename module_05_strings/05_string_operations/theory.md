# String Operations

Python provides several built-in operations that work on strings.

## Concatenation (`+`)

Join two or more strings together:

```python
first = "Hello"
second = "World"
result = first + " " + second
print(result)   # Hello World
```

## Repetition (`*`)

Repeat a string a certain number of times:

```python
line = "-" * 20
print(line)   # --------------------

laugh = "ha" * 3
print(laugh)  # hahaha
```

## Membership (`in` and `not in`)

Check if a substring exists inside a string:

```python
text = "Hello World"
print("Hello" in text)      # True
print("xyz" in text)        # False
print("xyz" not in text)    # True
```

## Length (`len()`)

Get the number of characters in a string:

```python
word = "Python"
print(len(word))   # 6

empty = ""
print(len(empty))  # 0
```

Spaces count as characters:

```python
text = "Hi there"
print(len(text))   # 8 (including the space)
```

## Key Points

- `+` joins strings together (concatenation)
- `*` repeats a string (repetition)
- `in` / `not in` checks if a substring exists
- `len()` gives the total number of characters

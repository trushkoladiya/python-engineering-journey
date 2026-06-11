# String Modification Methods

These methods create **new** strings with modifications (remember, strings are immutable).

## `replace()`

Replace occurrences of a substring with another:

```python
text = "Hello World"
print(text.replace("World", "Python"))   # Hello Python
print(text.replace("l", "L"))            # HeLLo WorLd
```

You can limit the number of replacements:

```python
text = "aaa"
print(text.replace("a", "b", 2))   # bba — only first 2 replaced
```

## `split()`

Split a string into a **list** of substrings:

```python
text = "Hello World Python"
words = text.split()
print(words)   # ['Hello', 'World', 'Python']
```

Split by a specific separator:

```python
data = "apple,banana,cherry"
fruits = data.split(",")
print(fruits)   # ['apple', 'banana', 'cherry']
```

> **Note:** `split()` returns a list. Lists are covered in Module 6, but here we just use the result with loops.

## `join()`

Join a sequence of strings with a separator:

```python
words = ["Hello", "World", "Python"]
result = " ".join(words)
print(result)   # Hello World Python

result2 = "-".join(words)
print(result2)  # Hello-World-Python
```

## Key Points

- `replace(old, new)` — replaces all occurrences (or limit with a third argument)
- `split()` — splits into a list by whitespace (or a custom separator)
- `join()` — joins a sequence with a separator
- All methods return **new** strings; the original stays unchanged

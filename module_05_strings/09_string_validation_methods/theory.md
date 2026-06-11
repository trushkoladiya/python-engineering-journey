# String Validation Methods

Validation methods check **what kind of characters** a string contains. They all return `True` or `False`.

## `isalpha()` — Only Letters?

```python
print("Hello".isalpha())     # True
print("Hello1".isalpha())    # False — contains a digit
print("Hello World".isalpha())  # False — contains a space
```

## `isdigit()` — Only Digits?

```python
print("12345".isdigit())    # True
print("123.45".isdigit())   # False — dot is not a digit
print("12 34".isdigit())    # False — space is not a digit
```

## `isalnum()` — Only Letters and Digits?

```python
print("Hello123".isalnum())    # True
print("Hello 123".isalnum())   # False — space
print("Hello!".isalnum())      # False — exclamation mark
```

## `isspace()` — Only Whitespace?

```python
print("   ".isspace())       # True
print("\t\n".isspace())      # True — tabs and newlines count
print(" a ".isspace())       # False — contains a letter
```

## `islower()` and `isupper()` — Case Checks

```python
print("hello".islower())     # True
print("Hello".islower())     # False — has uppercase

print("HELLO".isupper())     # True
print("Hello".isupper())     # False — has lowercase
```

## Important Note

All these methods return `False` for **empty strings**:

```python
print("".isalpha())   # False
print("".isdigit())   # False
```

## Key Points

- `isalpha()` — only letters (a-z, A-Z)
- `isdigit()` — only digits (0-9)
- `isalnum()` — only letters and digits
- `isspace()` — only whitespace
- `islower()` / `isupper()` — case checks
- Empty strings return `False` for all checks

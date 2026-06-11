# Recursion with Data Structures

Recursion works naturally with strings and lists — you can break them into smaller pieces.

## Strings

### Reverse a String
```python
def reverse(s):
    if len(s) <= 1: return s
    return reverse(s[1:]) + s[0]
```

### Palindrome Check
```python
def is_palindrome(s):
    if len(s) <= 1: return True
    if s[0] != s[-1]: return False
    return is_palindrome(s[1:-1])
```

## Lists

### Sum of List
```python
def list_sum(items):
    if len(items) == 0: return 0
    return items[0] + list_sum(items[1:])
```

### Max Element
```python
def list_max(items):
    if len(items) == 1: return items[0]
    rest_max = list_max(items[1:])
    return items[0] if items[0] > rest_max else rest_max
```

## The Pattern

For strings/lists, the recursive pattern is usually:
1. **Base case**: empty or single element
2. **Recursive case**: process first element + recurse on the rest

## Key Points

- Strings: use `s[0]` (first char) and `s[1:]` (rest)
- Lists: use `items[0]` (first element) and `items[1:]` (rest)
- This "first + rest" pattern is very common

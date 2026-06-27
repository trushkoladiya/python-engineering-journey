# Return Values

Functions can **return** data back to the caller using the `return` keyword.

## The `return` Keyword

```python
def add(a, b):
    return a + b

result = add(3, 5)
print(result)   # 8
```

When Python hits `return`, it:
1. Sends the value back to the caller
2. Exits the function immediately

## Returning a Single Value

```python
def square(n):
    return n * n

answer = square(5)
print(answer)   # 25
```

You can use the return value directly:

```python
print(square(4))           # 16
total = square(3) + square(4)   # 9 + 16 = 25
```

## Returning Multiple Values (as a Tuple)

```python
def min_max(numbers):
    return min(numbers), max(numbers)

low, high = min_max([5, 2, 8, 1, 9])
print(low)    # 1
print(high)   # 9
```

## No Return — Implicit `None`

If a function has no `return` statement, it returns `None`:

```python
def greet(name):
    print(f"Hello, {name}!")

result = greet("Trush")
print(result)   # None
```

## When to Use Return vs Print

- Use `return` when the caller needs the value for further use
- Use `print()` when you just want to display something

## Key Points

- `return` sends a value back to the caller
- The function exits immediately after `return`
- Multiple values are returned as a tuple
- No `return` means the function returns `None`
- Return values can be stored in variables or used in expressions

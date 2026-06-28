# Functions as First-Class Objects

In Python, functions are **objects** — just like numbers, strings, and lists. This means you can:
- Assign them to variables
- Pass them as arguments to other functions
- Return them from other functions

## Assigning Functions to Variables

```python
def greet(name):
    return f"Hello, {name}!"

say_hello = greet   # No parentheses — assigns the function itself
print(say_hello("Trush"))   # Hello, Trush!
```

## Passing Functions as Arguments

```python
def apply(func, value):
    return func(value)

def double(n):
    return n * 2

def square(n):
    return n * n

print(apply(double, 5))   # 10
print(apply(square, 5))   # 25
```

## Returning Functions from Functions

```python
def make_multiplier(factor):
    def multiplier(n):
        return n * factor
    return multiplier

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))   # 10
print(triple(5))   # 15
```

## Key Points

- Functions are objects — they can be stored, passed, and returned
- Assign without `()` to reference the function itself
- Add `()` to call (execute) the function
- Passing functions as arguments enables powerful patterns

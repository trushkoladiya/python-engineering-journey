# Higher-Order Functions

A **higher-order function** is a function that does at least one of:
1. Takes another function as an **argument**
2. **Returns** a function as its result

You've already used higher-order functions — `map()`, `filter()`, and `sorted()` all take functions as arguments!

## Functions as Arguments

```python
def apply(func, value):
    return func(value)

result = apply(len, "hello")   # 5
```

## Functions as Return Values

```python
def make_adder(n):
    def adder(x):
        return x + n
    return adder

add5 = make_adder(5)
print(add5(10))   # 15
```

## Why Higher-Order Functions?

They let you write **reusable, flexible** code:

```python
def process_list(items, transform):
    """Apply ANY transformation to a list."""
    return [transform(item) for item in items]

# Same function, different behaviors
doubled = process_list([1, 2, 3], lambda x: x * 2)
stringed = process_list([1, 2, 3], str)
```

## Key Points

- Higher-order functions accept or return other functions
- `map()`, `filter()`, `sorted()` are built-in higher-order functions
- They enable flexible, reusable code patterns
- This is a core concept in functional programming

# Parameters & Arguments

**Parameters** let you pass data into a function so it can work with different values each time.

## Positional Parameters

Parameters are variables listed in the function definition:

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Trush")   # Hello, Trush!
greet("Rahul")     # Hello, Rahul!
```

Multiple parameters:

```python
def add(a, b):
    print(a + b)

add(3, 5)    # 8
add(10, 20)  # 30
```

## Default Parameters

Give a parameter a default value — used when no argument is provided:

```python
def greet(name="World"):
    print(f"Hello, {name}!")

greet("Trush")   # Hello, Trush!
greet()          # Hello, World!  (uses default)
```

Default parameters must come **after** non-default ones:

```python
def power(base, exponent=2):
    print(base ** exponent)

power(3)      # 9  (3^2)
power(3, 3)   # 27 (3^3)
```

## Keyword Arguments

Pass arguments by name instead of position:

```python
def describe(name, age, city):
    print(f"{name}, {age}, from {city}")

describe(name="Trush", age=21, city="Mumbai")
describe(city="Delhi", name="Rahul", age=30)   # Order doesn't matter
```

## Mixing Argument Types

Positional arguments must come before keyword arguments:

```python
def info(name, age, city="Unknown"):
    print(f"{name}, {age}, {city}")

info("Trush", 21)                    # Positional + default
info("Rahul", 30, city="Delhi")       # Positional + keyword
```

## Key Points

- **Parameters** are in the definition; **arguments** are in the call
- Positional arguments match by position
- Default parameters have fallback values
- Keyword arguments are passed by name
- Positional arguments must come before keyword arguments

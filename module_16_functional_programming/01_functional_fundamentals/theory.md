# Functional Programming Fundamentals

Functional programming is a **style of writing code** where you focus on using functions to transform data, rather than changing variables step by step.

Python is **not purely functional**, but it supports many functional patterns that make code cleaner and more predictable.

## Three Core Ideas

### 1. Functions Are First-Class Citizens

In Python, functions are **values** — just like numbers or strings. You can:
- Assign a function to a variable
- Pass a function as an argument
- Return a function from another function

```python
def greet(name):
    return f"Hello, {name}!"

# Assign function to a variable
say_hello = greet
print(say_hello("Trush"))   # Hello, Trush!
```

You already used this in Module 8 (functions) and Module 13 (callable objects). Functional programming **relies heavily** on this idea.

### 2. Pure Functions

A **pure function** always returns the same output for the same input, and has **no side effects** (doesn't change anything outside itself):

```python
# PURE — depends only on input
def add(a, b):
    return a + b

# IMPURE — modifies external state
total = 0
def add_to_total(x):
    global total
    total += x     # side effect!
```

Pure functions are easier to test, debug, and reason about.

### 3. Immutability

Functional programming prefers **not changing data** — instead, you create new data:

```python
# Imperative style — mutates the list
numbers = [1, 2, 3]
numbers.append(4)       # changed original!

# Functional style — creates new data
numbers = (1, 2, 3)
new_numbers = numbers + (4,)   # original unchanged
```

## Why Use Functional Style?

| Benefit | Explanation |
|---------|-------------|
| Predictable | Pure functions always behave the same way |
| Testable | No hidden state to worry about |
| Composable | Small functions combine into bigger ones |
| Readable | Data transformations are clear pipelines |

## Key Points

- Functional programming is a **style**, not a separate language
- Python supports functional patterns alongside other styles
- The three pillars: first-class functions, pure functions, immutability
- You don't have to go 100% functional — use it where it helps

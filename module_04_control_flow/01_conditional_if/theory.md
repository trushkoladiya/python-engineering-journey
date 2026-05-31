# Conditional Statements (if)

The `if` statement lets Python make decisions. It runs a block of code **only when a condition is True**.

## Basic Syntax

```python
if condition:
    # this code runs only when condition is True
```

- The `condition` is any expression that evaluates to `True` or `False`
- The colon `:` is required after the condition
- The code block **must be indented** (4 spaces is standard)

## Simple Example

```python
age = 21
if age >= 18:
    print("You are an adult")
```

If `age` is 18 or more, Python prints the message. Otherwise, nothing happens.

## Boolean Condition Evaluation

Python evaluates the condition and converts it to a boolean:

```python
x = 10
if x:
    print("x is truthy")    # prints — because 10 is truthy

y = 0
if y:
    print("y is truthy")    # does NOT print — 0 is falsy
```

**Truthy values**: any non-zero number, non-empty string
**Falsy values**: `0`, `0.0`, `""` (empty string), `None`

## Indentation Rules

Everything indented under `if` is part of the block:

```python
score = 90
if score > 80:
    print("Great score, Trush!")   # inside the if block
    print("Keep it up!")            # also inside the if block
print("Done checking")             # outside — always runs
```

## Multiple Conditions

You can use comparison operators from Module 3:

```python
temperature = 35
if temperature > 30:
    print("It's hot outside")
```

## Key Points

- `if` checks a condition — runs the block only when `True`
- The condition must end with `:`
- The block must be indented
- Falsy values: `0`, `0.0`, `""`, `None`
- Code after the `if` block (not indented) always runs

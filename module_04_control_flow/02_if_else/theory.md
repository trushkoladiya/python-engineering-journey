# if-else

The `if-else` statement provides **two-way decision making**. If the condition is `True`, one block runs. If `False`, the other block runs.

## Basic Syntax

```python
if condition:
    # runs when condition is True
else:
    # runs when condition is False
```

- Exactly **one** of the two blocks always runs
- `else` does not have a condition — it catches everything `if` didn't

## Simple Example

```python
age = 21
if age >= 18:
    print("You can vote")
else:
    print("You cannot vote yet")
```

Output: `You can vote` — because 21 is >= 18.

## Default Execution Path

The `else` block acts as a **default** — it runs when the condition fails:

```python
number = 7
if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

Output: `Odd` — because 7 % 2 gives 1, not 0.

## Multiple Lines in Each Block

```python
score = 45
if score >= 50:
    print("Passed!")
    print("Congratulations!")
else:
    print("Failed")
    print("Try again next time")
```

## Using Variables to Store Results

```python
temperature = 25
if temperature > 30:
    status = "Hot"
else:
    status = "Normal"
print("Weather:", status)   # Weather: Normal
```

## Key Points

- `if-else` = two-way decision — one block always runs
- `else` has no condition — it handles the "otherwise" case
- Both blocks must be indented
- `else` must be at the same indentation as its `if`

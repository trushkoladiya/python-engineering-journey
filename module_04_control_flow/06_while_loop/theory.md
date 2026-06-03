# While Loop

A `while` loop **repeats a block of code** as long as a condition remains `True`. This is the first loop you'll learn.

## Basic Syntax

```python
while condition:
    # this block repeats while condition is True
```

## Simple Example

```python
count = 1
while count <= 5:
    print(count)
    count = count + 1
# Output: 1, 2, 3, 4, 5
```

**How it works:**
1. Check the condition → is `count <= 5`?
2. If `True`, run the block
3. Go back to step 1
4. If `False`, stop — move past the loop

## Loop Condition Evaluation

The condition is checked **before each iteration**:

```python
x = 10
while x > 0:
    print(x)
    x = x - 3
# Output: 10, 7, 4, 1
# Stops when x becomes -2 (not > 0)
```

## Infinite Loops

If the condition never becomes `False`, the loop runs forever:

```python
# ⚠️ INTENTIONAL infinite loop (don't run this!)
# while True:
#     print("This never stops")
```

**Common mistake** — forgetting to update the variable:
```python
# ⚠️ ACCIDENTAL infinite loop
# count = 1
# while count <= 5:
#     print(count)
#     # forgot: count = count + 1
```

Always make sure something inside the loop **changes the condition**.

## Using `+=` for Updates

```python
total = 0
num = 1
while num <= 10:
    total += num    # same as total = total + num
    num += 1
print("Sum:", total)  # Sum: 55
```

## Key Points

- `while` repeats as long as the condition is `True`
- The condition is checked **before each iteration**
- Always update the loop variable to avoid infinite loops
- `while True:` creates an intentional infinite loop (useful later with `break`)

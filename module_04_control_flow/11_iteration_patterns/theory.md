# Iteration Patterns

This subtopic covers common **patterns for looping** — the typical ways you'll use `for` and `while` loops in practice.

## Counter-Based Loops

Use a counter variable to repeat a fixed number of times:

```python
# Using for with range
for i in range(5):
    print("Attempt", i + 1)

# Using while with a counter
count = 0
while count < 5:
    print("Attempt", count + 1)
    count += 1
```

## Condition-Based Loops

Loop until a condition changes — you don't know how many iterations in advance:

```python
# Keep halving until less than 1
value = 100
while value >= 1:
    print(value)
    value /= 2
```

## Accumulator Pattern

Build up a result across iterations:

```python
# Sum
total = 0
for i in range(1, 6):
    total += i
print("Sum:", total)    # 15

# Product
product = 1
for i in range(1, 6):
    product *= i
print("Product:", product)    # 120
```

## Iterating with Index

Track position while looping through a string:

```python
text = "Trush"
for i in range(len(text)):
    print("Index", i, "=", text[i])
```

`len()` gives the length, and `range(len(...))` gives indices 0 to length-1.

## Key Points

- **Counter-based**: fixed number of iterations (use `for` + `range`)
- **Condition-based**: unknown iterations (use `while`)
- **Accumulator**: build a result (sum, product, string) over iterations
- **Index-based**: use `range(len(...))` to get both position and value

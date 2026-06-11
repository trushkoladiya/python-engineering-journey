# Nested Loops

A nested loop is a **loop inside another loop**. The inner loop runs completely for each iteration of the outer loop.

## Basic Syntax

```python
for i in range(3):        # outer loop
    for j in range(3):    # inner loop
        print(i, j)
```

## How It Works

For each iteration of the outer loop, the inner loop runs **all its iterations**:

- Outer `i = 0` → Inner runs: `j = 0, 1, 2`
- Outer `i = 1` → Inner runs: `j = 0, 1, 2`
- Outer `i = 2` → Inner runs: `j = 0, 1, 2`

Total iterations = outer × inner = 3 × 3 = 9

## Pattern Example

```python
for i in range(1, 4):
    for j in range(1, 4):
        print(i * j, end=" ")
    print()   # new line after each row
```

Output:
```
1 2 3
2 4 6
3 6 9
```

## Nested While Loops

```python
i = 1
while i <= 3:
    j = 1
    while j <= 3:
        print("*", end=" ")
        j += 1
    print()
    i += 1
```

## Complexity Awareness

Nested loops multiply the work:
- 2 nested loops of `n` → `n × n` = n² iterations
- If `n = 100`, that's 10,000 iterations
- If `n = 1000`, that's 1,000,000 iterations

This is fine for small values, but be aware of performance with large numbers.

## Key Points

- Inner loop completes all its iterations for **each** outer iteration
- Total iterations = outer count × inner count
- You can mix `for` and `while` loops
- `break` only exits the **innermost** loop
- Be careful with large nested loops — they multiply work

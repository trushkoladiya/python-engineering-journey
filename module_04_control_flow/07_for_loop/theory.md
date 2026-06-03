# For Loop

The `for` loop iterates over a **sequence** of items. It's the most common loop in Python.

## Basic Syntax

```python
for variable in sequence:
    # this block runs once for each item
```

## Iterating Over a String

```python
for char in "Trush":
    print(char)
# Output: T, r, u, s, h
```

## Using `range()`

`range()` generates a sequence of numbers — perfect for counting loops.

### `range(stop)` — 0 to stop-1

```python
for i in range(5):
    print(i)
# Output: 0, 1, 2, 3, 4
```

### `range(start, stop)` — start to stop-1

```python
for i in range(1, 6):
    print(i)
# Output: 1, 2, 3, 4, 5
```

### `range(start, stop, step)` — with custom step

```python
for i in range(0, 10, 2):
    print(i)
# Output: 0, 2, 4, 6, 8

for i in range(10, 0, -1):
    print(i)
# Output: 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
```

## Loop Variable Behavior

The loop variable takes the value of each item, one at a time:

```python
for num in range(1, 4):
    print("num is:", num)
# num is: 1
# num is: 2
# num is: 3
```

After the loop ends, the variable keeps its **last value**:

```python
for x in range(3):
    pass
print(x)    # 2 (last value from 0, 1, 2)
```

## Key Points

- `for` iterates over sequences (strings, ranges, etc.)
- `range(n)` gives numbers 0 to n-1
- `range(start, stop)` gives numbers start to stop-1
- `range(start, stop, step)` gives numbers with custom step
- The loop variable keeps its last value after the loop ends

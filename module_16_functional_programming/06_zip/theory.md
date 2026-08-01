# zip() — Combining Iterables

`zip()` takes multiple iterables and **pairs up** their elements into tuples.

## Basic Syntax

```python
zip(iterable1, iterable2, ...)
```

## Simple Examples

```python
names = ["Trush", "Rahul", "Eve"]
ages = [21, 22, 22]

paired = list(zip(names, ages))
# [('Trush', 21), ('Rahul', 22), ('Eve', 22)]
```

## Iterating in Parallel

```python
names = ["Trush", "Rahul", "Eve"]
scores = [85, 92, 78]

for name, score in zip(names, scores):
    print(f"{name}: {score}")
```

## Unequal Lengths

`zip()` stops at the **shortest** iterable:

```python
a = [1, 2, 3]
b = [10, 20]

result = list(zip(a, b))
# [(1, 10), (2, 20)]   ← 3 is dropped
```

## Unzipping

You can "unzip" with `zip(*pairs)`:

```python
pairs = [("Trush", 21), ("Rahul", 22), ("Eve", 22)]
names, ages = zip(*pairs)
# names = ('Trush', 'Rahul', 'Eve')
# ages = (21, 22, 22)
```

## Key Points

- `zip()` combines iterables element-by-element into tuples
- Stops at the shortest iterable
- Returns a lazy iterator
- Great for parallel iteration
- `zip(*pairs)` can "unzip" paired data

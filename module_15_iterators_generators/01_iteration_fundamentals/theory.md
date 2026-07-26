# Iteration Fundamentals

Iteration means **going through items one by one**. You've been doing this since Module 4 with `for` loops. Now you'll learn how it actually works under the hood.

## Iterable vs Iterator

These two terms sound similar but are different:

| Concept | What it is | Example |
|---------|-----------|---------|
| **Iterable** | Something you CAN loop over | `[1, 2, 3]`, `"hello"`, `range(5)` |
| **Iterator** | The object that does the actual looping | Created by `iter()` |

Think of it like a book:
- The **book** is the iterable (it contains pages)
- Your **bookmark** is the iterator (it tracks where you are)

## How `for` Loops Actually Work

When you write:

```python
for item in [1, 2, 3]:
    print(item)
```

Python actually does this behind the scenes:

```python
# 1. Get an iterator from the iterable
iterator = iter([1, 2, 3])

# 2. Call next() repeatedly
print(next(iterator))   # 1
print(next(iterator))   # 2
print(next(iterator))   # 3
# next(iterator)        # StopIteration! (no more items)
```

## The Two Key Functions

- `iter(iterable)` — creates an iterator from an iterable
- `next(iterator)` — gets the next item from an iterator

## Key Points

- An **iterable** is anything you can loop over
- An **iterator** is the object that keeps track of position
- `for` loops use `iter()` and `next()` behind the scenes
- When items run out, `StopIteration` is raised (handled by `for` automatically)

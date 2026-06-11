# Creating Custom Iterators

You can create your own iterators by implementing `__iter__()` and `__next__()` in a class.

## Basic Custom Iterator

```python
class CountUp:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self   # iterator returns itself

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        value = self.current
        self.current += 1
        return value

# Use it like any iterable!
for num in CountUp(1, 5):
    print(num)   # 1, 2, 3, 4, 5
```

## The Pattern

1. `__iter__()` — returns `self` (the iterator object)
2. `__next__()` — returns the next value, updates state, raises `StopIteration` when done

## Stateful Iteration

The iterator keeps track of where it is:

```python
class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value
```

## Key Points

- Implement `__iter__()` and `__next__()` to create an iterator
- `__iter__()` should return `self`
- `__next__()` returns the next value and updates internal state
- Raise `StopIteration` when there are no more values
- Custom iterators work with `for`, `list()`, `next()`, etc.

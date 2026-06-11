# Chaining & Composing Iterators

You can combine multiple iterators together to build powerful data processing pipelines.

## Chaining: Sequential Iteration

Process multiple iterables in sequence:

```python
def chain(*iterables):
    for it in iterables:
        for item in it:
            yield item

for x in chain([1, 2], [3, 4], [5]):
    print(x)   # 1, 2, 3, 4, 5
```

## `yield from` — Delegating to Sub-iterators

A cleaner way to yield all items from another iterable:

```python
def chain(*iterables):
    for it in iterables:
        yield from it   # yield each item from 'it'
```

`yield from` replaces the inner `for` loop — same result, cleaner code.

## `itertools` Module (Intro)

Python's `itertools` provides powerful iterator tools:

```python
import itertools

# chain — combine iterables
itertools.chain([1, 2], [3, 4])   # 1, 2, 3, 4

# islice — slice an iterator
itertools.islice(range(100), 5)   # 0, 1, 2, 3, 4

# count — infinite counter
itertools.count(10)   # 10, 11, 12, 13, ...
```

## Key Points

- Chain iterators to process multiple sources sequentially
- `yield from` delegates to sub-iterators cleanly
- `itertools` provides powerful, memory-efficient iterator tools
- Composing small iterators builds clean data pipelines

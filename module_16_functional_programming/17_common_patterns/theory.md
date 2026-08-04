# Common Patterns (Engineering Thinking)

This subtopic brings everything together with **real-world patterns** you'll use as a Python developer.

## Data Transformation Pipelines

Process data through a series of steps:

```python
raw_data → clean → filter → transform → aggregate → result
```

```python
# Clean → filter → transform → aggregate
result = sum(
    price * 1.1                              # add tax
    for price in map(float, raw_prices)      # convert
    if price > 0                              # filter valid
)
```

## Filtering and Aggregation

```python
# Group and summarize data
from collections import defaultdict

def group_by(items, key_func):
    groups = defaultdict(list)
    for item in items:
        groups[key_func(item)].append(item)
    return dict(groups)
```

## Map-Filter-Reduce Pattern

The classic functional pattern for data processing:

1. **map** — transform each item
2. **filter** — keep items that match
3. **reduce** — combine into a single result

```python
from functools import reduce

# Total revenue from expensive products
revenue = reduce(
    lambda a, b: a + b,
    map(lambda p: p["price"] * p["qty"],
        filter(lambda p: p["price"] > 50, products)),
    0
)
```

## Key Points

- Think in terms of data flowing through transformations
- Break complex operations into small, composable steps
- Use the right tool: comprehensions, map/filter, or generators
- Keep individual functions pure and focused
- Name your pipeline steps for clarity

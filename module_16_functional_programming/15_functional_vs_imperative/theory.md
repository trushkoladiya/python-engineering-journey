# Functional vs Imperative Style

Python supports both **imperative** (step-by-step, mutation-based) and **functional** (expression-based, transformation-based) styles. Knowing when to use each makes you a better programmer.

## Side-by-Side Comparison

### Transforming Data

```python
# Imperative
result = []
for x in numbers:
    if x > 0:
        result.append(x * 2)

# Functional
result = [x * 2 for x in numbers if x > 0]

# Functional (with map/filter)
result = list(map(lambda x: x * 2, filter(lambda x: x > 0, numbers)))
```

### Accumulating a Value

```python
# Imperative
total = 0
for x in numbers:
    total += x

# Functional
total = sum(numbers)

# Functional (reduce)
from functools import reduce
total = reduce(lambda a, b: a + b, numbers)
```

## When to Use Each

| Use Functional When | Use Imperative When |
|--------------------|---------------------|
| Transforming data | Complex multi-step logic |
| No side effects needed | Need to modify state |
| Operations are simple | Operations have conditionals |
| Chaining transformations | Debugging step by step |

## Key Points

- Neither style is "better" — use the right tool for the job
- Functional is great for data pipelines and transformations
- Imperative is better for complex logic with many branches
- Python encourages mixing both styles
- Readability is always the top priority

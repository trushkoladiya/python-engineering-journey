# Lazy Evaluation Patterns

Lazy evaluation means **computing values only when needed**. Generators are Python's primary tool for lazy evaluation.

## Eager vs Lazy

```python
# EAGER — computes everything upfront
data = [x**2 for x in range(1_000_000)]  # 1 million items in memory

# LAZY — computes one at a time
data = (x**2 for x in range(1_000_000))  # almost no memory used
```

## Why Lazy Matters

1. **Large datasets** — process files too big for memory
2. **Streaming** — handle data that arrives continuously
3. **Early stopping** — stop processing when you find what you need

## Processing Large Data

```python
def read_large_file(filename):
    with open(filename) as f:
        for line in f:
            yield line.strip()

# Only one line in memory at a time!
for line in read_large_file("huge_file.txt"):
    if "ERROR" in line:
        print(line)
        break
```

## Pipeline Pattern

Chain generators to process data step by step:

```python
lines = read_file("data.csv")
parsed = parse_csv(lines)
filtered = filter_valid(parsed)
results = transform(filtered)
```

Each step processes one item at a time — minimal memory usage.

## Key Points

- Lazy evaluation = compute only when needed
- Generators are naturally lazy
- Perfect for large files, streams, and early termination
- Pipeline chains keep memory usage constant

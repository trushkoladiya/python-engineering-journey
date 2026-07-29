# Common Patterns (Engineering Thinking)

Real-world uses of iterators and generators for practical problems.

## Infinite Sequences

Generators can produce values forever:

```python
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Take only what you need
import itertools
first_10 = list(itertools.islice(fibonacci(), 10))
```

## Data Pipelines

Chain generators for step-by-step processing:

```python
raw_data = read_file("data.csv")
parsed = parse_rows(raw_data)
filtered = remove_invalid(parsed)
transformed = calculate_totals(filtered)

for result in transformed:
    save(result)
```

Each step processes one item at a time — constant memory.

## Filtering Streams

Process only relevant items from a stream:

```python
def only_errors(log_lines):
    for line in log_lines:
        if "ERROR" in line:
            yield line
```

## Batching

Process items in groups:

```python
def batches(iterable, size):
    batch = []
    for item in iterable:
        batch.append(item)
        if len(batch) == size:
            yield batch
            batch = []
    if batch:
        yield batch
```

## Flattening Nested Data

```python
def flatten(nested):
    for item in nested:
        if isinstance(item, (list, tuple)):
            yield from flatten(item)
        else:
            yield item
```

## Key Points

- Infinite sequences are only possible with generators
- Pipelines chain generators for memory-efficient processing
- Filtering, batching, and flattening are common real-world patterns
- Think of generators as **lazy data streams**

# Best Practices

Guidelines for writing clean, effective iterators and generators.

## When to Use Generators

✅ **Use generators when:**
- Processing large files line by line
- Building data transformation pipelines
- Working with infinite or streaming data
- You only need to iterate once
- Memory efficiency matters

❌ **Use lists when:**
- You need random access (`data[5]`)
- You need to iterate multiple times
- You need `len()`, sorting, or slicing
- Data is small enough to fit in memory

## Keep Generators Simple

```python
# GOOD: small, focused generator
def even_numbers(limit):
    for n in range(0, limit, 2):
        yield n

# BAD: doing too much in one generator
def do_everything(data):
    for item in data:
        cleaned = item.strip()
        if cleaned:
            parsed = int(cleaned)
            if parsed > 0:
                yield parsed ** 2
```

Better: split into small, composable steps.

## Use `yield from` for Delegation

```python
# Instead of:
for item in sub_iterable:
    yield item

# Use:
yield from sub_iterable
```

## Name Generators Clearly

```python
# Clear names that describe what they produce
def read_lines(filename): ...
def parse_records(lines): ...
def filter_valid(records): ...
```

## Key Points

- Choose generators for large/streaming data, lists for small/reusable data
- Keep generators small and composable
- Use `yield from` for cleaner delegation
- Name generators descriptively
- Document whether a function returns a list or a generator

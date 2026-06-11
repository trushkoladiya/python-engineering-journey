# Performance & Memory Concepts

Generators and lists have different performance characteristics. Understanding them helps you choose the right tool.

## Memory: Generators vs Lists

```python
import sys

# List: stores ALL values in memory
big_list = [x for x in range(1_000_000)]
print(sys.getsizeof(big_list))     # ~8 MB

# Generator: stores almost nothing
big_gen = (x for x in range(1_000_000))
print(sys.getsizeof(big_gen))      # ~200 bytes!
```

## Speed Comparison

- **Lists** are faster for repeated access and small data
- **Generators** are faster when you process once and stop early

## When Generators Win

| Scenario | Why Generator Wins |
|----------|-------------------|
| Processing large files | Only one line in memory |
| Finding first match | Stops early, doesn't compute rest |
| Data pipelines | Constant memory usage |
| Infinite sequences | Lists can't be infinite |

## When Lists Win

| Scenario | Why List Wins |
|----------|--------------|
| Need random access (`data[5]`) | Generators are sequential |
| Need to iterate multiple times | Generators exhaust |
| Need `len()` | Generators don't have length |
| Small data | List overhead is negligible |

## Key Points

- Generators use almost no memory regardless of data size
- Lists store everything in memory
- Generators are best for large/streaming/one-pass data
- Lists are best for small/reusable/random-access data
- Profile your code to make informed decisions

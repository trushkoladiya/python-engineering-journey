# Quick Sort

## How It Works

**Quick sort** also uses divide and conquer, but differently from merge sort:

1. **Choose a pivot** element
2. **Partition**: move all smaller elements to the left, larger to the right
3. **Recursively sort** the left and right partitions

## The Partition Step

The key operation: rearrange the list so that:
- Elements **≤ pivot** are on the left
- Elements **> pivot** are on the right
- The pivot is in its **final sorted position**

```python
# Before partition (pivot = 5):
[8, 3, 1, 5, 9, 2, 7]

# After partition:
[3, 1, 2, 5, 9, 8, 7]
#         ^ pivot in correct position
```

## Complexity

| Case | Time |
|------|------|
| Best | O(n log n) |
| Average | O(n log n) |
| Worst | O(n²) — when pivot is always min or max |

**Space**: O(log n) for recursion stack

## Quick Sort vs Merge Sort

| Feature | Merge Sort | Quick Sort |
|---------|-----------|------------|
| Time (worst) | O(n log n) | O(n²) |
| Time (average) | O(n log n) | O(n log n) |
| Space | O(n) | O(log n) |
| In-place | No | Yes |
| Stable | Yes | No |

## Key Points

- **Average O(n log n)**, but worst case O(n²)
- In-place — uses less memory than merge sort
- Pivot choice matters — median-of-three is a common strategy
- Python's `sorted()` uses Timsort, not quick sort
- Understanding partitioning is the key insight

# Merge Sort

## How It Works

**Merge sort** uses **divide and conquer**:

1. **Divide**: Split the list into two halves
2. **Conquer**: Recursively sort each half
3. **Merge**: Combine the two sorted halves into one sorted list

## The Merge Step

The key insight: merging two **already sorted** lists into one sorted list is O(n):

```python
# Two sorted halves:
left  = [1, 4, 7]
right = [2, 5, 8]

# Merge by comparing front elements:
# Compare 1 and 2 → take 1
# Compare 4 and 2 → take 2
# Compare 4 and 5 → take 4
# ...
# Result: [1, 2, 4, 5, 7, 8]
```

## Algorithm

```python
def merge_sort(items):
    if len(items) <= 1:
        return items

    mid = len(items) // 2
    left = merge_sort(items[:mid])
    right = merge_sort(items[mid:])
    return merge(left, right)
```

## Complexity

| Case | Time |
|------|------|
| Best | O(n log n) |
| Average | O(n log n) |
| Worst | O(n log n) |

**Space**: O(n) — needs extra space for merging

## Key Points

- **Always O(n log n)** — consistent performance
- Uses extra memory (not in-place)
- Stable sort
- Divide and conquer approach
- The foundation for understanding efficient sorting

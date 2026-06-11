# Bubble Sort

## How It Works

**Bubble sort** repeatedly steps through the list, compares adjacent elements, and **swaps** them if they're in the wrong order. Larger elements "bubble up" to the end.

## Algorithm

1. Compare each pair of adjacent elements
2. Swap if the left is greater than the right
3. After one pass, the largest element is at the end
4. Repeat for the remaining elements
5. Stop when no swaps are needed

```python
def bubble_sort(items):
    n = len(items)
    for i in range(n):
        swapped = False
        for j in range(n - 1 - i):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True
        if not swapped:
            break    # already sorted!
```

## Complexity

| Case | Time |
|------|------|
| Best | O(n) — already sorted (with early exit) |
| Average | O(n²) |
| Worst | O(n²) — reverse sorted |

**Space**: O(1) — sorts in-place

## Key Points

- Simple to understand and implement
- Inefficient for large data — O(n²)
- In-place sorting (no extra memory)
- Stable sort (equal elements keep their order)
- Useful for learning, not for production code

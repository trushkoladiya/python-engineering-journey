# Selection Sort

## How It Works

**Selection sort** divides the list into two parts:
- **Sorted** (left side, grows each pass)
- **Unsorted** (right side, shrinks each pass)

Each pass finds the **minimum** in the unsorted part and places it at the end of the sorted part.

## Algorithm

1. Find the minimum element in the unsorted portion
2. Swap it with the first unsorted element
3. Expand the sorted portion by one
4. Repeat until the entire list is sorted

```python
def selection_sort(items):
    n = len(items)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if items[j] < items[min_idx]:
                min_idx = j
        items[i], items[min_idx] = items[min_idx], items[i]
```

## Complexity

| Case | Time |
|------|------|
| Best | O(n²) |
| Average | O(n²) |
| Worst | O(n²) |

**Space**: O(1) — in-place

## Key Points

- Always O(n²) — doesn't benefit from partially sorted data
- Makes **fewer swaps** than bubble sort (at most n swaps)
- In-place, but **not stable** (equal elements may change order)
- Simple to understand, but slow for large data

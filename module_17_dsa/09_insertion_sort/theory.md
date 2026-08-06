# Insertion Sort

## How It Works

**Insertion sort** builds the sorted list one element at a time by inserting each new element into its correct position within the already-sorted portion.

Think of it like sorting playing cards in your hand — you pick up one card at a time and slide it into the right spot.

## Algorithm

1. Start from the second element (index 1)
2. Compare it with elements to its left
3. Shift larger elements right to make room
4. Insert the element in its correct position
5. Repeat for all elements

```python
def insertion_sort(items):
    for i in range(1, len(items)):
        key = items[i]
        j = i - 1
        while j >= 0 and items[j] > key:
            items[j + 1] = items[j]    # shift right
            j -= 1
        items[j + 1] = key             # insert
```

## Complexity

| Case | Time |
|------|------|
| Best | O(n) — already sorted |
| Average | O(n²) |
| Worst | O(n²) — reverse sorted |

**Space**: O(1) — in-place

## Key Points

- **Best basic sort** for nearly sorted data — O(n) best case
- Stable sort — preserves order of equal elements
- In-place — no extra memory
- Very efficient for small lists
- Used in practice as part of hybrid sorting algorithms (like Timsort)

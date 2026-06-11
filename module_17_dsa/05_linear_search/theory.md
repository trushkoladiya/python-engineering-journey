# Linear Search

## What Is Linear Search?

**Linear search** (or sequential search) checks each element one by one until it finds the target or reaches the end.

It's the simplest searching algorithm — no special requirements on the data.

## How It Works

1. Start from the first element
2. Compare each element with the target
3. If found → return the position
4. If end reached → target doesn't exist

```python
def linear_search(items, target):
    for i in range(len(items)):
        if items[i] == target:
            return i
    return -1
```

## Complexity

| Case | Time |
|------|------|
| Best | O(1) — found at first position |
| Average | O(n/2) → O(n) |
| Worst | O(n) — found at last position or not at all |

**Space**: O(1) — no extra memory needed

## When to Use

- Data is **unsorted**
- Data is **small**
- You only need to search **once**
- Simplicity matters more than speed

## Key Points

- Works on any list — sorted or unsorted
- Simple but slow for large data
- O(n) time, O(1) space
- For sorted data, binary search is much faster

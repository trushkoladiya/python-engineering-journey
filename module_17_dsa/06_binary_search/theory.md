# Binary Search

## What Is Binary Search?

**Binary search** finds a target in a **sorted** list by repeatedly halving the search space.

Instead of checking every element (like linear search), it:
1. Looks at the **middle** element
2. If target is smaller → search the **left half**
3. If target is larger → search the **right half**
4. Repeat until found or space is empty

## Requirement

The data **must be sorted**. Binary search does not work on unsorted data.

## Iterative Approach

```python
def binary_search(items, target):
    left = 0
    right = len(items) - 1

    while left <= right:
        mid = (left + right) // 2
        if items[mid] == target:
            return mid
        elif items[mid] < target:
            left = mid + 1     # target is in right half
        else:
            right = mid - 1    # target is in left half
    return -1
```

## Recursive Approach

```python
def binary_search_recursive(items, target, left, right):
    if left > right:
        return -1

    mid = (left + right) // 2
    if items[mid] == target:
        return mid
    elif items[mid] < target:
        return binary_search_recursive(items, target, mid + 1, right)
    else:
        return binary_search_recursive(items, target, left, mid - 1)
```

## Complexity

| Case | Time |
|------|------|
| Best | O(1) — target is at the middle |
| Average | O(log n) |
| Worst | O(log n) |

**Space**: O(1) iterative, O(log n) recursive (call stack)

## Why O(log n)?

Each step cuts the search space in **half**:
- 1,000 items → ~10 steps
- 1,000,000 items → ~20 steps
- 1,000,000,000 items → ~30 steps

## Key Points

- Requires **sorted** data
- O(log n) — dramatically faster than linear search for large data
- Two approaches: iterative (preferred) and recursive
- One of the most important algorithms in computer science

# Complexity Analysis (Deeper)

## Beyond Basic Big-O

In subtopic 2, we learned the basics. Now let's go deeper.

## Best, Average, Worst Case

Every algorithm has three cases:

| Case | Meaning | Example (Linear Search) |
|------|---------|------------------------|
| Best | Fastest possible | Target at index 0 → O(1) |
| Average | Typical performance | Target in middle → O(n/2) → O(n) |
| Worst | Slowest possible | Target at end or missing → O(n) |

**We usually focus on worst case** because it guarantees an upper bound.

## Amortized Analysis

Some operations are **usually fast** but **occasionally slow**:

```python
# Python list.append() is O(1) amortized
# Usually O(1), but occasionally O(n) when the
# internal array needs to be resized
```

Amortized = average cost over many operations.

## Space Complexity — Auxiliary Space

**Total space** = input space + auxiliary space
**Auxiliary space** = extra space used by the algorithm

```python
# O(1) auxiliary space — modifies input
def reverse_in_place(items):
    left, right = 0, len(items) - 1
    while left < right:
        items[left], items[right] = items[right], items[left]
        left += 1
        right -= 1

# O(n) auxiliary space — creates new data
def reverse_copy(items):
    return items[::-1]
```

## Common Complexity Classes

| Class | Name | Growth |
|-------|------|--------|
| O(1) | Constant | Flat |
| O(log n) | Logarithmic | Very slow growth |
| O(n) | Linear | Proportional |
| O(n log n) | Linearithmic | Slightly above linear |
| O(n²) | Quadratic | Fast growth |
| O(2ⁿ) | Exponential | Extremely fast growth |
| O(n!) | Factorial | Fastest growth |

## Key Points

- Always consider best, average, and worst case
- Worst case gives the strongest guarantee
- Auxiliary space = extra memory beyond the input
- Amortized analysis accounts for occasional expensive operations
- Trade-offs: time vs space, readability vs performance

# Arrays — Advanced Patterns

## Two-Pointer Technique

The **two-pointer technique** uses two indices that move through a list, often from opposite ends or at different speeds.

### When to Use

- Working with sorted lists
- Finding pairs that satisfy a condition
- Comparing elements from both ends

```python
# Find a pair that sums to a target in a SORTED list
def two_sum_sorted(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left < right:
        current_sum = numbers[left] + numbers[right]
        if current_sum == target:
            return (numbers[left], numbers[right])
        elif current_sum < target:
            left += 1       # need larger sum
        else:
            right -= 1      # need smaller sum
    return None
```

**Time**: O(n) — each pointer moves at most n times
**Space**: O(1) — just two variables

## Sliding Window Technique

The **sliding window** maintains a "window" (a subarray) that slides across the data.

### When to Use

- Finding subarrays of fixed or variable size
- Maximum/minimum sum of k consecutive elements
- Substring problems

```python
# Find maximum sum of k consecutive elements
def max_sum_subarray(numbers, k):
    window_sum = sum(numbers[:k])    # first window
    max_sum = window_sum

    for i in range(k, len(numbers)):
        window_sum += numbers[i]      # add new element
        window_sum -= numbers[i - k]  # remove old element
        max_sum = max(max_sum, window_sum)

    return max_sum
```

**Time**: O(n) — single pass instead of recalculating each window

## Key Points

- Two-pointer works best on **sorted** data
- Sliding window works for **contiguous subarray** problems
- Both reduce O(n²) brute force to O(n)
- These are among the most common DSA interview patterns

# Recursion in DSA

## Recursion Recap

Recursion is when a function **calls itself**. Every recursive function needs:
1. **Base case** — when to stop
2. **Recursive case** — break the problem into smaller subproblems

You learned recursion in Module 9. Now we use it as a **problem-solving tool** for DSA.

## Divide and Conquer

The most powerful recursive strategy:
1. **Divide** the problem into smaller subproblems
2. **Conquer** each subproblem recursively
3. **Combine** the results

```python
# Example: find max in a list using divide and conquer
def find_max(items, start, end):
    if start == end:
        return items[start]

    mid = (start + end) // 2
    left_max = find_max(items, start, mid)
    right_max = find_max(items, mid + 1, end)
    return max(left_max, right_max)
```

## Recursive Problem Solving Patterns

| Pattern | Example |
|---------|---------|
| Break in half | Binary search, merge sort |
| Try all options | Permutations, subsets |
| Build up | Generate combinations |
| Tree traversal | Walk tree structures |

## Key Points

- Recursion is essential for trees, graphs, and divide-and-conquer
- Always define a clear base case
- Think about what changes between calls
- Many recursive solutions can also be done iteratively
- Watch for stack overflow with very deep recursion

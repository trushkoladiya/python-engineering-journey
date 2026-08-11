# Debugging & Testing DSA Code

## Why DSA Code Needs Extra Care

DSA code often has subtle bugs:
- Off-by-one errors (wrong index bounds)
- Missing edge cases (empty input, single element)
- Incorrect loop conditions
- Stack overflow from deep recursion

## Technique 1: Dry Run

**Manually trace** your algorithm on paper with a small input.

```
# Binary search for 7 in [1, 3, 5, 7, 9]
# Step 1: left=0, right=4, mid=2, arr[2]=5 < 7 → go right
# Step 2: left=3, right=4, mid=3, arr[3]=7 = 7 → FOUND!
```

## Technique 2: Edge Cases

Always test with:

| Edge Case | Example |
|-----------|---------|
| Empty input | `[]` |
| Single element | `[5]` |
| Already sorted | `[1, 2, 3]` |
| Reverse sorted | `[3, 2, 1]` |
| All same | `[5, 5, 5]` |
| Negative numbers | `[-3, -1, 2]` |
| Very large input | `range(1_000_000)` |

## Technique 3: Assert Statements

```python
def binary_search(items, target):
    # ... implementation ...
    pass

# Test with assertions
assert binary_search([1, 3, 5, 7], 5) == 2
assert binary_search([1, 3, 5, 7], 4) == -1
assert binary_search([], 1) == -1
```

## Key Points

- Always dry run on a small example first
- Test edge cases systematically
- Use assertions to verify correctness
- Print intermediate values when debugging
- Compare output with a known-correct brute force solution

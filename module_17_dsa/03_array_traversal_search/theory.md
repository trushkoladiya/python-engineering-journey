# Arrays & List-Based Problems — Core Patterns

## Arrays in Python

Python doesn't have a built-in "array" type for DSA. Instead, we use **lists** — they work the same way for algorithm practice.

## Traversal

**Traversal** means visiting every element in a list, one by one.

```python
numbers = [10, 20, 30, 40, 50]

# Forward traversal
for num in numbers:
    print(num)

# Traversal with index
for i in range(len(numbers)):
    print(f"Index {i}: {numbers[i]}")
```

## Linear Search

**Linear search** scans each element until it finds the target — or reaches the end.

```python
def linear_search(items, target):
    for i in range(len(items)):
        if items[i] == target:
            return i       # found at index i
    return -1              # not found

result = linear_search([5, 3, 8, 1, 9], 8)
print(result)   # 2
```

- **Time**: O(n) — may need to check every element
- **Space**: O(1) — no extra memory

## Basic Sorting Concepts

Sorting arranges data in a specific order. Python's built-in `sorted()` is O(n log n), but understanding **how** sorting works is key to DSA thinking.

The simplest idea: repeatedly find the smallest element and place it in order.

## Key Points

- Traversal = visiting each element → O(n)
- Linear search = checking each element for a match → O(n)
- These are the foundation — every other algorithm builds on traversal

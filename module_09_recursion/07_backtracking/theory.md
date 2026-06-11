# Backtracking (Introduction)

**Backtracking** is a technique where you try all possibilities, and **undo** (backtrack) when a path doesn't work.

## The Concept

1. **Make a choice**
2. **Explore** that choice recursively
3. **Undo the choice** (backtrack) and try the next option

```
Try option A → explore → doesn't work → undo A
Try option B → explore → works! → keep it
```

## Generating Subsets

For `[1, 2, 3]`, subsets are: `[], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]`

At each element, you have two choices: **include it** or **skip it**.

```python
def subsets(items, current=[], index=0):
    if index == len(items):
        print(current)
        return
    # Choice 1: include items[index]
    subsets(items, current + [items[index]], index + 1)
    # Choice 2: skip items[index]
    subsets(items, current, index + 1)
```

## Key Points

- Backtracking = try → explore → undo → try next
- Used for: subsets, permutations, puzzles, combinations
- It systematically explores ALL possibilities
- "Undo" means removing the last choice before trying a new one

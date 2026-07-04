# Advanced Recursive Patterns

## Divide and Conquer

Split a problem into **independent** smaller parts, solve each recursively, then combine:

```
Problem
├── Subproblem A  → solve recursively
└── Subproblem B  → solve recursively
    → Combine results
```

### Example: Merge Sort (concept)
1. Split the list in half
2. Sort each half recursively
3. Merge the two sorted halves

## Tree-like Problem Solving

Many real problems have a tree structure:
- File system directories
- Organization charts
- Decision trees

The recursive approach: process the current node, then recurse on children.

## Key Points

- Divide and conquer: split → solve parts → combine
- Works when parts are **independent** (no overlap)
- Tree problems are naturally recursive
- This pattern is the foundation of many algorithms (merge sort, quick sort)

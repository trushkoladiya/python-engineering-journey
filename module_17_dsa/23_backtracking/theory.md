# Backtracking

## What Is Backtracking?

**Backtracking** is a systematic way to explore **all possible solutions** by building candidates incrementally and **abandoning** (backtracking from) candidates as soon as they can't lead to a valid solution.

Think of it as exploring a maze:
- Try a path
- If it's a dead end → **go back** and try another path

## The Pattern

```python
def backtrack(state):
    if is_solution(state):
        record(state)
        return

    for choice in available_choices(state):
        make_choice(choice)
        backtrack(state)
        undo_choice(choice)    # ← backtrack!
```

## Common Problems

| Problem | What You're Building |
|---------|---------------------|
| Subsets | All possible subsets |
| Permutations | All possible orderings |
| N-Queens | Valid queen placements |
| Sudoku | Valid number placements |

## Backtracking vs Brute Force

- **Brute force**: Try everything
- **Backtracking**: Try everything, but **prune** invalid paths early

This pruning makes backtracking much faster in practice.

## Key Points

- Backtracking = controlled recursion with undo
- Explore → choose → recurse → undo
- Prune paths that can't lead to solutions
- Used for constraint satisfaction and combinatorial problems

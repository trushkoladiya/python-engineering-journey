# Greedy Algorithms (Intro)

## What Is a Greedy Algorithm?

A **greedy algorithm** makes the **locally optimal choice** at each step, hoping it leads to a globally optimal solution.

It never reconsiders past choices — it just picks the best option **right now**.

## When Does Greedy Work?

Greedy works when:
- Making the best local choice leads to the best global result
- The problem has **greedy-choice property** and **optimal substructure**

## Classic Example: Coin Change (Greedy)

With US coins (25, 10, 5, 1), making change greedily works:

```python
# Make change for 67 cents
# Pick largest coin that fits: 25 → 25 → 10 → 5 → 1 → 1
# Result: 2×25 + 1×10 + 1×5 + 2×1 = 5 coins ✓
```

**Warning**: Greedy doesn't always give the optimal answer! With coins [1, 3, 4], making 6:
- Greedy: 4 + 1 + 1 = 3 coins
- Optimal: 3 + 3 = 2 coins

## Greedy vs Dynamic Programming

| Feature | Greedy | DP |
|---------|--------|-----|
| Approach | Local best choice | Try all options |
| Speed | Usually faster | Usually slower |
| Correctness | Not always optimal | Always optimal |
| Complexity | Often O(n log n) | Often O(n²) or more |

## Key Points

- Greedy = always pick the best option now
- Doesn't guarantee the global optimum for all problems
- When it works, it's simple and fast
- Common greedy problems: interval scheduling, Huffman coding, coin change (with standard denominations)

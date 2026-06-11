# Complexity Basics

## What Is Complexity?

When we write code, we want to know:
- **How fast** does it run? → **Time complexity**
- **How much memory** does it use? → **Space complexity**

Complexity tells us how our code **scales** as input grows.

## Big-O Notation

Big-O describes the **worst-case growth rate** of an algorithm.

| Big-O | Name | Example |
|-------|------|---------|
| O(1) | Constant | Dict lookup, list index |
| O(log n) | Logarithmic | Binary search |
| O(n) | Linear | Loop through a list |
| O(n log n) | Log-linear | Efficient sorting |
| O(n²) | Quadratic | Nested loops |
| O(2ⁿ) | Exponential | Brute force subsets |

## How to Read Big-O

`n` = the size of the input.

- **O(1)**: Takes the **same time** no matter how big `n` is
- **O(n)**: Time grows **proportionally** with `n`
- **O(n²)**: Time grows with the **square** of `n`

```python
# O(1) — constant
value = my_dict["key"]      # instant lookup

# O(n) — linear
for item in my_list:        # visits every item once
    print(item)

# O(n²) — quadratic
for i in my_list:           # every item...
    for j in my_list:       #   compared with every other
        print(i, j)
```

## Space Complexity

How much **extra memory** your algorithm needs:

```python
# O(1) space — no extra data structures
total = 0
for x in numbers:
    total += x

# O(n) space — creates a new list of same size
doubled = [x * 2 for x in numbers]
```

## Why It Matters

For small data, everything is fast. But as data grows:

| Input Size | O(n) | O(n²) |
|------------|------|-------|
| 100 | 100 ops | 10,000 ops |
| 10,000 | 10,000 ops | 100,000,000 ops |
| 1,000,000 | 1M ops | 1 TRILLION ops |

Choosing O(n) over O(n²) can mean **seconds vs hours**.

## Key Points

- Big-O measures how algorithms scale with input size
- Focus on the **dominant term** — ignore constants
- O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2ⁿ)
- Time and space are separate concerns — sometimes you trade one for the other

# DSA Fundamentals

## What Is DSA?

**DSA** stands for **Data Structures and Algorithms**.

- **Data Structure** = a way to **organize and store** data so it can be used efficiently
- **Algorithm** = a **step-by-step process** to solve a problem

You've already used both:
- Lists, dicts, sets, tuples — these are **data structures**
- Sorting a list, searching for a value — these are **algorithms**

DSA is about choosing the **right structure** and the **right approach** to solve problems **efficiently**.

## Why Does DSA Matter?

Imagine searching for a name in a phone book:
- **Bad approach**: Check every page one by one (slow)
- **Good approach**: Open the middle, decide which half to search (fast)

Both solve the problem — but one is **much faster**. DSA teaches you to think this way.

## Two Key Questions

When solving any problem, ask:

1. **How should I organize the data?** → Pick a data structure
2. **What steps solve the problem?** → Design an algorithm

```python
# Example: Find the largest number in a list

numbers = [34, 12, 89, 45, 67]

# Algorithm: scan every element, track the largest
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num

print(largest)   # 89
```

The **list** is the data structure. The **scan + compare** process is the algorithm.

## Common Data Structures You Know

| Structure | Purpose |
|-----------|---------|
| List | Ordered, changeable collection |
| Tuple | Ordered, unchangeable collection |
| Dict | Key-value lookup |
| Set | Unique items, fast membership check |

In this module, you'll learn **new structures** (stacks, queues, linked lists, trees, graphs) and **algorithms** to work with them.

## Key Points

- DSA = organizing data + solving problems efficiently
- You already use data structures and algorithms in every program
- The goal is to learn **when and why** to use each one
- Efficiency matters when data grows large

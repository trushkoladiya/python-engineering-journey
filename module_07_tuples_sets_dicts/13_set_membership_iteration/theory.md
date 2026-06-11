# Set Membership & Iteration

You can check if elements exist in a set and loop through all elements.

## Membership — `in` and `not in`

```python
fruits = {"apple", "banana", "cherry"}
print("apple" in fruits)       # True
print("mango" in fruits)       # False
print("mango" not in fruits)   # True
```

Membership checks in sets are **very fast** — much faster than in lists.

## Looping Through Sets

Use a `for` loop to iterate through all elements:

```python
colors = {"red", "green", "blue"}
for color in colors:
    print(color)
```

Remember: the order is **not guaranteed**.

## Looping with Enumerate

```python
fruits = {"apple", "banana", "cherry"}
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")
```

## Key Points

- `in` and `not in` work just like with lists and tuples
- Set membership checking is **faster** than lists
- Use `for` to loop through elements
- Order is not guaranteed when iterating

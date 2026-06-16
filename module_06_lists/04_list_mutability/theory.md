# List Mutability

Lists are **mutable** — you can change their contents after creation. This is a major difference from strings.

## Modifying Elements

You can change any element by assigning to its index:

```python
fruits = ["apple", "banana", "cherry"]
fruits[1] = "blueberry"
print(fruits)   # ['apple', 'blueberry', 'cherry']
```

## Updating by Index

```python
scores = [80, 90, 70]
scores[2] = 95     # change third score
print(scores)      # [80, 90, 95]
```

## Difference from Strings

**Strings** are immutable — you **cannot** change characters in place:

```python
word = "Hello"
# word[0] = "J"   # ❌ TypeError!

# But lists CAN be changed:
letters = ["H", "e", "l", "l", "o"]
letters[0] = "J"   # ✅ Works!
print(letters)      # ['J', 'e', 'l', 'l', 'o']
```

## Modifying with Slices

You can replace multiple elements at once:

```python
nums = [1, 2, 3, 4, 5]
nums[1:3] = [20, 30]
print(nums)   # [1, 20, 30, 4, 5]
```

## Key Points

- Lists are **mutable** — elements can be changed in place
- Strings are **immutable** — they cannot be changed in place
- Use index assignment (`list[i] = value`) to modify elements
- Use slice assignment to replace multiple elements at once

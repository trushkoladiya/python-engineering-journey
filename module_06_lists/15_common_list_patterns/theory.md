# Common List Patterns (Engineering Thinking)

These are frequently used patterns that combine everything from Module 6.

## Finding Max/Min

```python
nums = [45, 12, 89, 23, 67]
print(max(nums))   # 89
print(min(nums))   # 12
```

## Removing Duplicates

```python
data = [1, 2, 3, 2, 4, 1, 5]
unique = []
for item in data:
    if item not in unique:
        unique.append(item)
print(unique)   # [1, 2, 3, 4, 5]
```

## Frequency Counting

```python
data = ["a", "b", "a", "c", "b", "a"]
counted = []
for item in data:
    if item not in counted:
        print(f"'{item}': {data.count(item)}")
        counted.append(item)
```

## Two-Pointer Technique (Intro)

Use two indices to scan a list from both ends:

```python
nums = [1, 2, 3, 4, 5]
left = 0
right = len(nums) - 1
while left < right:
    print(f"Pair: {nums[left]}, {nums[right]}")
    left += 1
    right -= 1
```

## Flattening Nested Lists

```python
nested = [[1, 2], [3, 4], [5, 6]]
flat = [item for row in nested for item in row]
print(flat)   # [1, 2, 3, 4, 5, 6]
```

## Key Points

- Use `max()`, `min()`, `sum()` for quick stats
- Remove duplicates by tracking what you've seen
- Count frequency with `count()` in a loop
- Two pointers: scan from both ends simultaneously
- Flatten with nested comprehension

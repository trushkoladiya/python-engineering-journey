# List Slicing

Slicing lets you extract a **portion** of a list, just like with strings.

## Basic Slicing: `start:end`

```python
nums = [10, 20, 30, 40, 50]
print(nums[1:4])   # [20, 30, 40] — index 1, 2, 3
print(nums[0:3])   # [10, 20, 30] — index 0, 1, 2
```

- `start` is **included**, `end` is **excluded**

## Omitting Start or End

```python
nums = [10, 20, 30, 40, 50]
print(nums[:3])    # [10, 20, 30] — from beginning
print(nums[2:])    # [30, 40, 50] — to the end
print(nums[:])     # [10, 20, 30, 40, 50] — full copy
```

## Step Slicing: `start:end:step`

```python
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(nums[::2])     # [0, 2, 4, 6, 8] — every 2nd
print(nums[1::2])    # [1, 3, 5, 7, 9] — every 2nd from index 1
```

## Reversing a List

```python
nums = [1, 2, 3, 4, 5]
print(nums[::-1])   # [5, 4, 3, 2, 1]
```

## Copying a List with Slicing

```python
original = [1, 2, 3]
copy = original[:]
print(copy)   # [1, 2, 3] — a separate copy
```

This is important because `copy = original` does **not** create a copy (covered later).

## Key Points

- `list[start:end]` — end is excluded
- Omit `start` = from beginning; omit `end` = to the end
- `list[::step]` — skip elements by step
- `list[::-1]` — reverses the list
- `list[:]` — creates a shallow copy

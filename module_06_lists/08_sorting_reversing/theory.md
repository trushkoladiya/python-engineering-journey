# Sorting & Reversing

Python gives you several ways to sort and reverse lists.

## `sort()` — Sort in Place

Sorts the list **in place** (modifies the original):

```python
nums = [3, 1, 4, 1, 5, 9, 2]
nums.sort()
print(nums)   # [1, 1, 2, 3, 4, 5, 9]
```

Sort in reverse (descending):

```python
nums = [3, 1, 4, 1, 5]
nums.sort(reverse=True)
print(nums)   # [5, 4, 3, 1, 1]
```

## `sorted()` — Return a New Sorted List

Does **not** change the original — returns a new list:

```python
nums = [3, 1, 4, 1, 5]
new = sorted(nums)
print(new)    # [1, 1, 3, 4, 5]
print(nums)   # [3, 1, 4, 1, 5] — unchanged!
```

## `reverse()` — Reverse in Place

```python
nums = [1, 2, 3, 4, 5]
nums.reverse()
print(nums)   # [5, 4, 3, 2, 1]
```

## Custom Sorting with `key`

Sort by a criteria using the `key` parameter:

```python
words = ["banana", "apple", "cherry", "date"]
words.sort(key=len)
print(words)   # ['date', 'apple', 'banana', 'cherry']
```

This sorts by the **length** of each word.

## Key Points

- `sort()` modifies the list in place, returns `None`
- `sorted()` returns a new sorted list, original unchanged
- `reverse()` reverses in place
- Use `reverse=True` for descending order
- Use `key=` to customize sorting criteria

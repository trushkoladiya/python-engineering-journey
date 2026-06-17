# List Methods (Core)

List methods **modify the list in place** (unlike string methods which return new strings).

## Adding Elements

### `append()` — Add one item to the end

```python
fruits = ["apple", "banana"]
fruits.append("cherry")
print(fruits)   # ['apple', 'banana', 'cherry']
```

### `extend()` — Add multiple items from another list

```python
a = [1, 2, 3]
a.extend([4, 5, 6])
print(a)   # [1, 2, 3, 4, 5, 6]
```

### `insert()` — Add item at a specific position

```python
fruits = ["apple", "cherry"]
fruits.insert(1, "banana")   # insert at index 1
print(fruits)   # ['apple', 'banana', 'cherry']
```

## Removing Elements

### `remove()` — Remove first occurrence of a value

```python
nums = [1, 2, 3, 2, 1]
nums.remove(2)
print(nums)   # [1, 3, 2, 1] — only first 2 removed
```

### `pop()` — Remove and return an item by index

```python
fruits = ["apple", "banana", "cherry"]
removed = fruits.pop()     # removes last item
print(removed)   # cherry
print(fruits)    # ['apple', 'banana']

removed = fruits.pop(0)   # removes first item
print(removed)   # apple
```

### `clear()` — Remove all items

```python
nums = [1, 2, 3, 4, 5]
nums.clear()
print(nums)   # []
```

## Key Points

- `append()` adds **one** item to the end
- `extend()` adds **multiple** items from another list
- `insert(index, item)` adds at a specific position
- `remove(value)` removes first occurrence
- `pop(index)` removes by index and returns the item
- `clear()` empties the entire list
- All these methods **modify the list in place**

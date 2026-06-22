# Set Operations (Core)

Sets provide methods to **add** and **remove** elements.

## Adding Elements

### `add()` — Add a single element

```python
fruits = {"apple", "banana"}
fruits.add("cherry")
print(fruits)   # {'apple', 'banana', 'cherry'}
```

### `update()` — Add multiple elements

```python
fruits = {"apple", "banana"}
fruits.update(["cherry", "date", "elderberry"])
print(fruits)   # {'apple', 'banana', 'cherry', 'date', 'elderberry'}
```

## Removing Elements

### `remove()` — Removes element (error if not found)

```python
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
print(fruits)   # {'apple', 'cherry'}
# fruits.remove("mango")   # KeyError!
```

### `discard()` — Removes element (no error if not found)

```python
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")    # Removed
fruits.discard("mango")     # No error!
print(fruits)   # {'apple', 'cherry'}
```

### `pop()` — Removes and returns a random element

```python
fruits = {"apple", "banana", "cherry"}
removed = fruits.pop()
print(removed)   # Random element
print(fruits)    # Remaining elements
```

### `clear()` — Removes all elements

```python
fruits = {"apple", "banana", "cherry"}
fruits.clear()
print(fruits)   # set()
```

## Key Points

- `add()` adds one element, `update()` adds multiple
- `remove()` raises error if element missing; `discard()` does not
- `pop()` removes a random element (sets are unordered)
- `clear()` empties the entire set

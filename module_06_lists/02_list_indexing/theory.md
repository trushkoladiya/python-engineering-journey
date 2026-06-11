# List Indexing

Just like strings, every element in a list has a **position number** (index).

## Positive Indexing

Counting starts from `0`:

```python
fruits = ["apple", "banana", "cherry", "date"]
#          0         1         2         3

print(fruits[0])   # apple  (first)
print(fruits[1])   # banana (second)
print(fruits[3])   # date   (last)
```

## Negative Indexing

Count backwards from the end using negative numbers:

```python
fruits = ["apple", "banana", "cherry", "date"]
#          -4        -3        -2        -1

print(fruits[-1])   # date   (last)
print(fruits[-2])   # cherry (second from last)
print(fruits[-4])   # apple  (first)
```

## Accessing Elements

```python
colors = ["red", "green", "blue"]
first = colors[0]
last = colors[-1]
print(f"First: {first}, Last: {last}")
```

## IndexError

Going beyond the list length causes an error:

```python
nums = [10, 20, 30]
# nums[5]   → IndexError: list index out of range
```

Always check that the index is within range (0 to `len(list) - 1`).

## Key Points

- Indexing starts at `0`
- Negative indexing starts at `-1` (last element)
- `list[0]` is the first element, `list[-1]` is the last
- Out-of-range indices cause `IndexError`

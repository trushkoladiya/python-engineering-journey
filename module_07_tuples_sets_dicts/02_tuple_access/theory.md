# Tuple Access

Accessing elements in a tuple works the same way as with lists — using **indexing** and **slicing**.

## Positive Indexing

Index starts at `0`:

```python
fruits = ("apple", "banana", "cherry", "date")
print(fruits[0])   # apple
print(fruits[1])   # banana
print(fruits[3])   # date
```

## Negative Indexing

Negative index starts from the end at `-1`:

```python
fruits = ("apple", "banana", "cherry", "date")
print(fruits[-1])   # date
print(fruits[-2])   # cherry
print(fruits[-4])   # apple
```

## Slicing

Works just like list slicing — `tuple[start:end]` (end is excluded):

```python
numbers = (10, 20, 30, 40, 50)
print(numbers[1:4])    # (20, 30, 40)
print(numbers[:3])     # (10, 20, 30)
print(numbers[2:])     # (30, 40, 50)
```

## Step Slicing

```python
numbers = (10, 20, 30, 40, 50, 60)
print(numbers[::2])    # (10, 30, 50)    — every 2nd element
print(numbers[1::2])   # (20, 40, 60)    — every 2nd from index 1
print(numbers[::-1])   # (60, 50, 40, 30, 20, 10) — reversed
```

## Accessing Nested Tuples

```python
nested = ((1, 2), (3, 4), (5, 6))
print(nested[0])       # (1, 2)
print(nested[0][1])    # 2
print(nested[2][0])    # 5
```

## Key Points

- Indexing and slicing work identically to lists
- Positive index: starts at `0` from the left
- Negative index: starts at `-1` from the right
- Slicing returns a **new tuple**
- Use double indexing for nested tuples: `tuple[i][j]`

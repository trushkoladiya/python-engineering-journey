# Dictionary Comprehension

A concise way to create dictionaries from loops — similar to list comprehensions.

## Basic Comprehension

```python
squares = {x: x * x for x in range(1, 6)}
print(squares)   # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

## With Condition

```python
# Only even numbers
even_squares = {x: x * x for x in range(1, 11) if x % 2 == 0}
print(even_squares)   # {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}
```

## From Two Lists

```python
names = ["Trush", "Rahul", "Charlie"]
scores = [95, 87, 92]
result = {name: score for name, score in zip(names, scores)}
print(result)   # {'Trush': 95, 'Rahul': 87, 'Charlie': 92}
```

## Transforming a Dictionary

```python
prices = {"apple": 2.50, "banana": 1.75, "cherry": 4.00}
discounted = {item: round(price * 0.8, 2) for item, price in prices.items()}
print(discounted)
```

## Key Points

- Syntax: `{key: value for item in iterable}`
- Add `if condition` to filter
- Great for transforming existing data
- Keep comprehensions simple and readable

# Use Cases of Tuples

Understanding **when** to use tuples instead of lists is an important skill.

## Fixed Data Collections

Use tuples when data should **not change**:

```python
# Days of the week — never change
days = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")

# RGB color — fixed values
red = (255, 0, 0)

# Geographic coordinates
location = (40.7128, -74.0060)
```

## As Dictionary Keys

Lists **cannot** be dictionary keys, but tuples **can**:

```python
distances = {}
distances[("Delhi", "Mumbai")] = 1400
distances[("Mumbai", "Chennai")] = 1330
print(distances[("Delhi", "Mumbai")])   # 1400
```

## As Set Elements

Similarly, tuples can be added to sets:

```python
visited = set()
visited.add((28.6, 77.2))   # Delhi
visited.add((19.0, 72.8))   # Mumbai
print(visited)
```

## Storing Records

Tuples work well for storing structured data:

```python
students = [
    ("Trush", 95),
    ("Rahul", 87),
    ("Charlie", 92)
]
for name, score in students:
    print(f"{name}: {score}")
```

## Multiple Assignment

```python
x, y, z = 10, 20, 30
```

## Key Points

- Use tuples for **fixed** data that shouldn't change
- Use tuples as dictionary keys or set elements
- Use tuples for structured records (like rows of data)
- Use tuples when you want to protect data from modification
- Lists are better when you need to add, remove, or change elements

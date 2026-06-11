# Tuple Packing & Unpacking

Python allows you to **pack** multiple values into a tuple and **unpack** them back into individual variables.

## Packing

When you assign multiple values separated by commas, Python automatically creates a tuple:

```python
person = "Trush", 21, "New York"
print(person)        # ('Trush', 21, 'New York')
print(type(person))  # <class 'tuple'>
```

## Unpacking

You can assign each element of a tuple to a separate variable:

```python
person = ("Trush", 21, "New York")
name, age, city = person

print(name)   # Trush
print(age)    # 21
print(city)   # New York
```

The number of variables **must match** the number of elements:

```python
# a, b = (1, 2, 3)   # ValueError: too many values to unpack
```

## Extended Unpacking (`*`)

Use `*` to capture remaining elements into a list:

```python
numbers = (1, 2, 3, 4, 5)
first, *rest = numbers
print(first)   # 1
print(rest)    # [2, 3, 4, 5]

first, *middle, last = numbers
print(first)    # 1
print(middle)   # [2, 3, 4]
print(last)     # 5
```

## Swapping Variables

Tuple unpacking makes swapping easy:

```python
a = 10
b = 20
a, b = b, a
print(a)   # 20
print(b)   # 10
```

## Key Points

- **Packing**: comma-separated values → tuple
- **Unpacking**: tuple → individual variables
- Number of variables must match tuple length (unless using `*`)
- `*variable` captures remaining elements as a list
- Swapping with `a, b = b, a` uses tuple unpacking

# enumerate() — Indexed Iteration

`enumerate()` adds an **index counter** to any iterable, giving you both the index and the value.

## Basic Syntax

```python
enumerate(iterable, start=0)
```

## Simple Example

```python
fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
# 0: apple
# 1: banana
# 2: cherry
```

## Custom Start Index

```python
for i, fruit in enumerate(fruits, start=1):
    print(f"{i}. {fruit}")
# 1. apple
# 2. banana
# 3. cherry
```

## Without enumerate (Old Way)

```python
# Manual counter — messy
i = 0
for fruit in fruits:
    print(f"{i}: {fruit}")
    i += 1

# enumerate is cleaner!
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")
```

## Key Points

- `enumerate()` gives you `(index, value)` pairs
- Default starting index is 0
- Use `start=` to change the starting number
- Returns a lazy iterator
- Much cleaner than maintaining a manual counter

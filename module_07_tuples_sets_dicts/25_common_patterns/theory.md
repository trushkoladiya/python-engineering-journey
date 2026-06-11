# Common Patterns (Engineering Thinking)

Practical patterns that combine tuples, sets, and dictionaries for real-world problems.

## With Tuples

### Swapping Variables
```python
a, b = 10, 20
a, b = b, a
```

### Multiple Return-Like Values
```python
result = (True, "Success", 200)
status, message, code = result
```

## With Sets

### Removing Duplicates from a List
```python
data = [1, 2, 2, 3, 3, 4]
unique = list(set(data))
```

### Fast Membership Testing
```python
valid = {"admin", "user", "moderator"}
if role in valid:
    print("Access granted")
```

## With Dictionaries

### Frequency Counting
```python
text = "hello world"
freq = {}
for char in text:
    freq[char] = freq.get(char, 0) + 1
```

### Grouping Data
```python
students = [("Trush", "A"), ("Rahul", "B"), ("Charlie", "A")]
groups = {}
for name, grade in students:
    if grade not in groups:
        groups[grade] = []
    groups[grade].append(name)
```

### Lookup Tables
```python
day_names = {1: "Monday", 2: "Tuesday", 3: "Wednesday"}
print(day_names.get(1, "Unknown"))
```

## Key Points

- Use tuple unpacking for clean variable swaps
- Use sets for fast duplicate removal and membership testing
- Use dicts for counting, grouping, and lookup tables
- These patterns appear frequently in real programming
